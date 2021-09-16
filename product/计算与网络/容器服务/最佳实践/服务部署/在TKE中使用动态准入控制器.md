## 操作场景
动态准入控制器 Webhook 在访问鉴权的过程中可以更改请求对象或完全拒绝该请求，其调用 Webhook 服务的方式使其独立于集群组件。
动态准入控制器具有很大的灵活性，可便捷地进行众多自定义准入控制。下图为动态准入控制在 API 请求调用链的位置，如需了解更多信息，请前往 [Kubernetes 官网](https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/)。
![admission-controller-phases](https://main.qcloudimg.com/raw/85a757f42598097d24f3eae3736261b9.png)
由图可知，动态准入控制分为执行及验证两个阶段。首先执行 Mutating 阶段，该阶段可对到达请求进行修改，然后执行 Validating 阶段来验证到达的请求是否被允许，两个阶段可单独或组合使用。

本文将在容器服务 TKE 中实现一个简单的动态准入控制调用示例，您可结合实际需求参考本文进行操作。

## 操作步骤
### 查看及验证插件
TKE 现有集群版本（1.10.5及以上）已默认开启了 [validating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook) 和  [mutating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook) API。若您的集群版本低于 1.10.5，则可执行以下命令验证当前集群是否开启插件。
```
kube-apiserver -h | grep enable-admission-plugins
```
返回结果如已包含 `MutatingAdmissionWebhook` 和 `ValidatingAdmissionWebhook`，则说明当前集群已开启动态准入控制器插件。如下图所示：
![image-20201117102438615](https://main.qcloudimg.com/raw/534694e9a6976d0ec18d2e1074932126.png)

### 签发证书
为确保动态准入控制器调用可信任的 Webhook 服务端，须通过 HTTPS 调用 Webhook 服务（TLS 认证），则需为 Webhook 服务端颁发证书，并且在注册动态准入控制 Webhook 时为 `caBundle`  字段（ `ValidatingWebhookConfiguration` 和 `MutatingAdmissionWebhook` 资源清单中的 `caBundle` 字段）绑定受信任的颁发机构证书（CA）来核验 Webhook 服务端的证书是否可信任。本文介绍了 [制作自签证书](#MakeSignedCertificate) 及 [使用 K8S CSR API 签发证书](#K8SCertificate) 两种推荐的颁发证书方法。
>!当 `ValidatingWebhookConfiguration` 和 `MutatingAdmissionWebhook` 使用 `clientConfig.service` 配置时（Webhook 服务在集群内），为服务器端颁发的证书域名必须为 `<svc_name>.<svc_namespace>.svc`。

#### [方法1：制作自签证书](id:MakeSignedCertificate)
制作自签证书的方法不依赖于 K8S 集群，比较独立，类似于为网站制作自签证书。目前有很多工具可制作自签证书，本文以使用 Openssl 为例。具体步骤如下：
1. 执行以下命令，生成密钥位数为2048的 `ca.key`。
```bash
openssl genrsa -out ca.key 2048
```
2. 执行以下命令，依据 `ca.key` 生成 `ca.crt`。
"webserver.default.svc" 为 Webhook 服务端在集群中的域名，`-days` 参数用于设置证书有效时间。
```bash
openssl req -x509 -new -nodes -key ca.key -subj "/CN=webserver.default.svc" -days 10000 -out ca.crt
```
3. 执行以下命令，生成密钥位数为2048的 `server.key`。
```bash
openssl genrsa -out server.key 2048
```
4. 创建用于生成证书签名请求（CSR）的配置文件 `csr.conf`。示例如下： 
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

subjectAltName = @alt_names

[ alt_names ]
DNS.1 = webserver.default.svc

[ v3_ext ]
authorityKeyIdentifier=keyid,issuer:always
basicConstraints=CA:FALSE
keyUsage=keyEncipherment,dataEncipherment
extendedKeyUsage=serverAuth,clientAuth
subjectAltName=@alt_names
```
5. 执行以下命令，基于配置文件 `csr.conf` 生成证书签名请求。
```bash
openssl req -new -key server.key -out server.csr -config csr.conf
```
6. 执行以下命令，使用 `ca.key`、`ca.crt` 和 `server.csr` 颁发生成服务器证书（x509签名）。
```bash
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key \
 -CAcreateserial -out server.crt -days 10000 \
 -extensions v3_ext -extfile csr.conf
```
7. 执行以下命令，查看 Webhook server 端证书。
```bash
openssl x509  -noout -text -in ./server.crt
```
生成的证书及密钥文件说明如下：
- `ca.crt`：为颁发机构证书。
- `ca.key`：为颁发机构证书密钥，用于服务端证书颁发。
- `server.crt`：为颁发的服务端证书。
- `server.key`：为颁发的服务端证书密钥。

#### [方法2：使用 K8S CSR API 签发证书](id:K8SCertificate)
可使用 K8S 的证书颁发机构系统来下发证书，执行以下脚本可使用 K8S 集群根证书和根密钥签发一个可信任的证书用户。
>!用户名需为 Webhook  服务在集群中的域名。
>
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
 - `${USERNAME}`.crt：为 Webhook 服务端证书。
 -  `${USERNAME}`.key：为 Webhook 服务端证书密钥。


## 使用示例
本文将使用 `ValidatingWebhookConfiguration` 资源在 TKE 中实现一个动态准入 Webhook 调用示例。
为了确保可访问性，示例代码 Fork 自 [原代码库](https://github.com/larkintuckerllc/hello-dynamic-admission-control.git)，示例代码实现了一个简单的动态准入 Webhook 请求和响应的接口，具体接口格式请参见 [Webhook 请求和响应](https://kubernetes.io/zh/docs/reference/access-authn-authz/extensible-admission-controllers/#request) 。示例代码可在 [示例代码](https://github.com/imjokey/hello-dynamic-admission-control) 中获取，本文将使用其作为 Webhook 服务端代码。
1. 对应实际使用颁发证书方法，准备 `caBundle` 内容。
 - 若颁发证书使用方法1，则执行以下命令，使用 `base64`  编码 `ca.crt` 生成 `caBundle` 字段内容。
```bash
cat ca.crt | base64 --wrap=0 
```
 - 若颁发证书使用方法2，集群的根证书即为 `caBundle` 字段内容。获取步骤如下：
    1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster?rid=1)**。
    2. 在“集群管理”页面，选择集群 ID。
    3. 在集群详情页面，选择左侧的**基本信息**。
    4. 从“基本信息”页面的“集群APIServer信息”模块的 “Kubeconfig” 中的 `clusters.cluster[].certificate-authority-data` 字段进行获取，该字段已进行 `base64` 编码，无需再进行处理。
2. 复制生成的 `ca.crt`（颁发机构证书）、`server.crt`（HTTPS 证书）及 `server.key`（HTTPS 密钥） 到项目主目录。如下图所示：
![image-20201117131409795](https://main.qcloudimg.com/raw/61d2ad7f881606af8271abfbbb78d88b.png)
3. 修改项目中的 Dockerfile，添加三个证书文件到容器工作目录。如下图所示：
![image-20201117131639307](https://main.qcloudimg.com/raw/a2faa20c9c1db85075458bde232840ea.png)
4. 执行以下命令，构建 Webhook 服务端镜像。
```
docker build -t webserver .
```
5. 部署一个域名为 “weserver.default.svc” 的 Webhook 后端服务，修改适配后的 `controller.yaml` 如下所示：
![image-20201117131843384](https://main.qcloudimg.com/raw/4d06816731be0b1ea3478a5fc3938f8b.png)
6. 注册创建类型为 `ValidatingWebhookConfiguration` 的资源，修改适配项目中的 `admission.yaml` 文件。如下图所示：
本示例配置的 Webhook 触发规则为：当创建 `pods`类型、API 版本 “v1” 时触发调用，`clientConfig` 配置对应上述在集群中创建的 Webhook 后端服务，`caBundle`  字段内容为证书颁发方法一获取的 `ca.crt` 内容。
![](https://main.qcloudimg.com/raw/239814926510536dc17619bd77d8acad.png)
7. 注册好后创建一个 Pod 类型且 API 版本为 “v1” 的测试资源。如下图所示：
![image-20201117132642385](https://main.qcloudimg.com/raw/cc2b9a842085f319a42b54ec7366936a.png)  
8. 测试代码已打印请求日志，查看 Webhook 服务端日志即可查看动态准入控制器触发了 webhook 调用。如下图所示：
![image-20201117132840262](https://main.qcloudimg.com/raw/877c7eb459fff8f3e8e4a56c6893d0f5.png)
9. 此时查看创建的测试 pod 已成功创建，由于测试 Webhook 服务端代码已具备 `allowed: true` 配置项，即可创建成功该测试 pod。如下图所示：
![](https://main.qcloudimg.com/raw/1d46955ef82a072194a80b9c434cbd89.png)
如需进一步验证，将 “allowed” 改为 “false” 后重复上述步骤重新构建 Webserver 服务端镜像，并重新部署 `controller.yaml` 和 `admission.yaml` 资源。当再次尝试创建 pods 资源时请求被动态准入拦截，则说明配置的动态准入策略已生效。如下图所示：
   ![image-20201117133504920](https://main.qcloudimg.com/raw/3df15331208bf316fc06e432598658ae.png)

## 总结
本文主要介绍了动态准入控制器 Webhook 的概念和作用、如何在 TKE 集群中签发动态准入控制器所需的证书，并使用简单示例演示如何配置和使用动态准入 Webhook 功能。



## 参考资料
- [Kubernetes Dynamic Admission Control by Example]( https://codeburst.io/kubernetes-dynamic-admission-control-by-example-d8cc2912027c )
- [Dynamic Admission Control](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/)
