

# 在 TKE 中使用动态准入控制器



## 原理概述

动态准入控制器 Webhook 在访问鉴权过程中可以更改请求对象或完全拒绝该请求，其调用 Webhook 服务的方式使其独立于集群组件，具有非常大的灵活性，可以方便的做很多自定义准入控制，下图为动态准入控制在 API 请求调用链的位置（来源于 [Kubernetes 官网](https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/)）：

![admission-controller-phases](https://main.qcloudimg.com/raw/85a757f42598097d24f3eae3736261b9.png)

从上图可以看出，动态准入控制过程分为两个阶段：首先执行 Mutating 阶段，可以对到达请求进行修改，然后执行 Validating 阶段来验证到达的请求是否被允许，两个阶段可以单独使用也可以组合使用，本文将在 TKE 中实现一个简单的动态准入控制调用示例。



## 查看验证插件

在 TKE 现有集群版本中（1.10.5 及以上）已经默认开启了 [validating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook) 和  [mutating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook) API，如果是更低版本的集群，可以在 Apiserver Pod 中执行 `kube-apiserver -h | grep enable-admission-plugins` 验证当前集群是否开启，输出插件列表中如果有 `MutatingAdmissionWebhook` 和 `ValidatingAdmissionWebhook`  就说明当前集群开启了动态准入的控制器插件，如下图所示：

![image-20201117102438615](https://main.qcloudimg.com/raw/534694e9a6976d0ec18d2e1074932126.png)



## 签发证书

为了确保动态准入控制器调用的是可信任的 Webhook 服务端，必须通过 HTTPS 来调用 Webhook 服务（TLS认证）， 所以需要为 Webhook 服务端颁发证书，并且在注册动态准入控制 Webhook 时为  `caBundle`  字段（ `ValidatingWebhookConfiguration` 和 `MutatingAdmissionWebhook` 资源清单中的 `caBundle` 字段）绑定受信任的颁发机构证书（CA）来核验 Webhook 服务端的证书是否可信任， 这里分别介绍两种推荐的颁发证书方法：

> 注意：当`ValidatingWebhookConfiguration` 和 `MutatingAdmissionWebhook` 使用 `clientConfig.service` 配置时（Webhook 服务在集群内），为服务器端颁发的证书域名必须为 `<svc_name>.<svc_namespace>.svc`。

### 方法一： 制作自签证书

制作自签证书的方法比较独立，不依赖于 k8s 集群，类似于为一个网站做一个自签证书，有很多工具可以制作自签证书，本示例使用 Openssl 制作自签证书，操作步骤如下所示：

1. 生成密钥位数为 2048 的 ca.key：

   ```bash
   openssl genrsa -out ca.key 2048
   ```

2. 依据 ca.key 生成 ca.crt，"webserver.default.svc" 为 Webhook 服务端在集群中的域名，使用 `-days` 参数来设置证书有效时间：

   ```bash
   openssl req -x509 -new -nodes -key ca.key -subj "/CN=webserver.default.svc" -days 10000 -out ca.crt
   ```

3. 生成密钥位数为 2048 的 server.key：

   ```bash
   openssl genrsa -out server.key 2048
   ```

 4. 创建用于生成证书签名请求（CSR）的配置文件 csr.conf 示例如下： 

    ```text
    [ req ]
    default_bits = 2048
    prompt = no
    default_md = sha256
    distinguished_name = dn
    
    [ dn ]
    C = cn
    ST = shaanxi
    L = xi'an
    O = default
    OU = websever
    CN = webserver.default.svc
    
    [ v3_ext ]
    authorityKeyIdentifier=keyid,issuer:always
    basicConstraints=CA:FALSE
    keyUsage=keyEncipherment,dataEncipherment
    extendedKeyUsage=serverAuth,clientAuth
    ```

5. 基于配置文件 csr.conf 生成证书签名请求：

   ```bash
   openssl req -new -key server.key -out server.csr -config csr.conf
   ```

6. 使用 ca.key、ca.crt 和 server.csr 颁发生成服务器证书（x509签名）：

   ```bash
   openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key \
     -CAcreateserial -out server.crt -days 10000 \
     -extensions v3_ext -extfile csr.conf
   ```

7. 查看 Webhook server端证书：

   ```bash
   openssl x509  -noout -text -in ./server.crt
   ```

其中，生成的证书、密钥文件说明如下：

ca.crt 为颁发机构证书，ca.key 为颁发机构证书密钥，用于服务端证书颁发。

server.crt 为 颁发的服务端证书，server.key 为颁发的服务端证书密钥.



### 方法二：使用 K8S CSR API 签发

除了使用方案一加密工具制作自签证书，还可以使用 k8s 的证书颁发机构系统来下发证书，执行下面脚本可使用 K8S 集群根证书和根密钥签发一个可信任的证书用户，需要注意的是用户名应该为 Webhook  服务在集群中的域名：

```bash
USERNAME='webserver.default.svc' # 设置需要创建的用户名为 Webhook 服务在集群中的域名
# 使用 Openssl 生成自签证书 key
openssl genrsa -out ${USERNAME}.key 2048
# 使用 Openssl 生成自签证书 CSR 文件, CN 代表用户名，O 代表组名
openssl req -new -key ${USERNAME}.key -out ${USERNAME}.csr -subj "/CN=${USERNAME}/O=${USERNAME}" 
# 创建 Kubernetes 证书签名请求（CSR）
cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1beta1
kind: CertificateSigningRequest
metadata:
  name: ${USERNAME}
spec:
  request: $(cat ${USERNAME}.csr | base64 | tr -d '\n')
  usages:
  - digital signature
  - key encipherment
  - server auth
EOF
# 证书审批允许信任
kubectl certificate approve ${USERNAME}
# 获取自签证书 CRT
kubectl get csr ${USERNAME} -o jsonpath={.status.certificate} > ${USERNAME}.crt
```

 其中， `${USERNAME}`.crt 为服务端证书， `${USERNAME}`.key 为 Webhook 服务端证书密钥。



## 操作示例

下面将使用 `ValidatingWebhookConfiguration` 资源在 TKE 中实现一个动态准入 Webhook 调用示例，本示例代码可在 [示例代码](https://github.com/imjokey/hello-dynamic-admission-control) 中获取（为了确保可访问性，示例代码 Fork 自 [原代码库](https://github.com/larkintuckerllc/hello-dynamic-admission-control.git)，作者实现了一个简单的动态准入 Webhook 请求和响应的接口，具体接口格式请参考 [Webhook 请求和响应](https://kubernetes.io/zh/docs/reference/access-authn-authz/extensible-admission-controllers/#request) 。为了方便，我将使用它作为我们的 Webhook 服务端代码。

1. 准备 `caBundle` 内容

   - 若颁发证书方法是方案一, 使用 `base64`  编码 ca.crt 生成 `caBundle` 字段内容：

     ```bash
      cat ca.crt | base64 --wrap=0 
     ```
   
   - 若颁发证书方法是方案二，集群的根证书即为 `caBundle` 字段内容，可以通过 TKE 集群控制台【基本信息】-> 【集群APIServer信息】Kubeconfig 内容中的  `clusters.cluster[].certificate-authority-data ` 字段获取，该字段已经 `base64` 编码过了，无需再做处理。 

2. 复制生成的 ca.crt （颁发机构证书），server.crt（HTTPS 证书)）, server.key（HTTPS 密钥） 到项目主目录：

   ![image-20201117131409795](https://main.qcloudimg.com/raw/61d2ad7f881606af8271abfbbb78d88b.png)

3. 修改项目中的 Dockerfile ，添加三个证书文件到容器工作目录：
   ![image-20201117131639307](https://main.qcloudimg.com/raw/a2faa20c9c1db85075458bde232840ea.png)

   然后使用 docker 命令构建 Webhook 服务端镜像：

   ```
   docker build -t webserver .
   ```

4. 部署一个域名为 "weserver.default.svc" 的 Webhook 后端服务，修改适配后的 controller.yaml 如下：

   ![image-20201117131843384](https://main.qcloudimg.com/raw/4d06816731be0b1ea3478a5fc3938f8b.png)

5. 注册创建类型为 `ValidatingWebhookConfiguration` 的资源，本示例配置的 Webhook 触发规则是当创建 `pods`类型，API 版本 "v1" 时触发调用，`clientConfig` 配置对应上述在集群中创建的的 Webhook 后端服务， `caBundle`  字段内容为证书颁发方法一获取的ca.crt 内容，修改适配项目中的 admission.yaml 文件如下图：

   ![image-20201117132424740](https://main.qcloudimg.com/raw/a641a63f32aeb108c4916b73d51cd2d0.png)

6. 注册好后创建一个 Pod 类型， API 版本为 "v1" 的测试资源如下：

   ![image-20201117132642385](https://main.qcloudimg.com/raw/cc2b9a842085f319a42b54ec7366936a.png)  

7. 测试代码有打印请求日志， 查看 Webhook 服务端日志可以看到动态准入控制器触发了 webhook 调用，如下图：

   ![image-20201117132840262](https://main.qcloudimg.com/raw/877c7eb459fff8f3e8e4a56c6893d0f5.png)



8. 此时查看创建的测试pod 是成功创建的，是因为测试 Webhook 服务端代码写死的 `allowed: true`，所以是可以创建成功的，如下图：
   ![image-20201117133024888](https://main.qcloudimg.com/raw/092657ff9ebdb4be6f16abab131a0c09.png) 



9. 为了进一步验证，我们把 "allowed" 改成 "false" ，然后重复上述步骤重新打 Webserver 服务端镜像，并重新部署 controller.yaml 和 admission.yaml 资源，当再次尝试创建 "pods" 资源时请求被动态准入拦截，说明配置的动态准入策略是生效的，如下图所示：

   ![image-20201117133504920](https://main.qcloudimg.com/raw/3df15331208bf316fc06e432598658ae.png)



## 总结

本文主要介绍了动态准入控制器 Webhook 的概念和作用、如何在 TKE 集群中签发动态准入控制器所需的证书，并使用简单示例演示如何配置和使用动态准入 Webhook 功能。



## 参考

参考博文：  https://codeburst.io/kubernetes-dynamic-admission-control-by-example-d8cc2912027c 

参考官网： https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/

