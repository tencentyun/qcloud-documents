本文为您详细介绍如何使用 Serverless 实现动态准入控制，实现 K8S 两步验证。

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 选择左侧菜单【持续部署】。

## 背景

如果对 Kubernetes 集群安全特别关注，那么我们可能想要实现这些需求：
*   如何实现 Kubernetes 集群的两步验证，除了集群凭据，还需要提供一次性的 Token 校验？
*   如何验证部署的镜像是否安全合规，使得仅允许部署公司内部镜像仓库的 Docker 镜像？
*   如何实现对每一个 Deployment 动态注入 sidecar ，满足特定安全或业务需求？
*   如何实现集群级的 imagePullSecrets ，当创建新的命名空间的时候，自动将 imagePullSecrets 注入到新的命名空间？

> 本文以实现 Kubernetes 两步验证为例，利用 `Kubernetes Admission` 动态准入控制，同时借助 `Serverless` 实现一个`两步验证`的 Demo，使读者对`动态准入控制`和`Serverless`有较深入的了解。

## 实现效果

**Token 两步验证失败，不允许部署**

![](https://blog-img-1301285745.cos.ap-guangzhou.myqcloud.com/kubernetes-admission/1-Fail-Two-Step.gif)

**Token 两步验证成功，允许部署**

![](https://blog-img-1301285745.cos.ap-guangzhou.myqcloud.com/kubernetes-admission/2-Success-Two-Step.gif)

## 什么是 Admission

Admission 是在用户执行 kubectl 通过认证之后，在将资源持久化到 ETCD 之前的步骤，Kubernetes 为了将这部分逻辑解耦，通过调用 Webhook 的方式来实现用户自定义业务逻辑的补充。而以上过程，都是在用户执行 kuberctl 并等待 API Server 同步返回结果的生命周期内。

![](https://blog-img-1301285745.cos.ap-guangzhou.myqcloud.com/kubernetes-admission/3-Architecture.png)

上图标注的 ① 和 ② 是 Admission 介入的工作流程，我们会发现有这些特点：
1.  Admission 工作在集群认证通过之后
2.  Admission 一共有两种：`Mutating` 和 `Validating`
3.  这两种具体的实现方式都是以 `Webhook` 实现的
4.  Admission 的操作对象可以是当前部署的用户、Yaml 内容等

## Admission Mutating

`Mutating` 的字面理解是“变异”的意思，真正的含义是，在资源持久化到 ETCD 之前，`Mutating` 控制器可以修改所部署的资源文件，比如给特定的 POD 动态增加 Labels，动态注入 `sidecar` 等。
细心的读者会发现，`Admission Mutating` 在很多产品都被用到，比如 `Istio` 里面就是使用它来动态的给每一个容器注入 sidecar  `Envoy` 容器来实现流量的劫持和管理。

## Admission Validating

`Validating` 比较好理解，也就是“验证”，它在 `Mutating` 之后，我们可以将自定义的验证逻辑放在这个阶段实现。本文我们就是利用它来实现一个简单的两步验证机制。

## 什么是 Admission Webhook

`Admission Webhook` 其实就是 `Mutating Controllers` 和 `Validating Controllers` 的具体实现方式，也就是说，我们需要给 Kubernetes 集群提供一个外部 Webhook Endpoint，API Server 执行到对应流程时，会调用我们预定义的 Webhook 来实现我们预定义的业务逻辑，通过返回规定的数据结构，来实现对 Yaml 文件的变更或者验证。

## 动手实践
### 集群条件

根据官方文档，先决条件有以下几点：
*   Kubernetes 集群版本至少为 v1.16
*   启用了 MutatingAdmissionWebhook 和 ValidatingAdmissionWebhook 控制器

如果不确定，可以通过以下命令查询：

```sh
kubectl get pods kube-apiserver -n kube-system -o yaml | grep MutatingAdmissionWebhook,ValidatingAdmissionWebhook
```
如果你使用的是托管集群，那么请使用以下命令查询：

```sh
kubectl api-versions | grep admission
```

如果出现 `admissionregistration.k8s.io/v1beta1` 说明集群支持，进行下一步。

### 其他条件

*   开通 [CODING DevOps](https://coding.net)
*   [克隆代码仓库地址](https://e.coding.net/wangweicoding/admission-webhook-example.git) 并推送到自己的 CODING Git 仓库
*   准备一个 [腾讯云账户](https://cloud.tencent.com)

### 部署腾讯 Serverless 服务

1.  登陆 CODING，并在配置 Serverless 身份授权，记录凭据 ID （类似：b68948cb-2ad9-4b67-8a49-ad7ba910ed92），稍后使用。

![](https://blog-img-1301285745.cos.ap-guangzhou.myqcloud.com/kubernetes-admission/4-Credentials.gif)

2.  克隆代码仓库 `admission-webhook-example`

```sh
git clone https://e.coding.net/wangweicoding/admission-webhook-example.git
```

3.  修改根目录下的文件

*   根目录下的 Jenkinsfile，将上一步获取的凭据 ID 替换光标处的凭据 ID
![](https://blog-img-1301285745.cos.ap-guangzhou.myqcloud.com/kubernetes-admission/5-Edit-Credentials.png)
*   修改 serverless/.env 的 `VPC_ID` 和 `SUBNET_ID`，这两项可以在腾讯云控制台“[私有网络](https://console.cloud.tencent.com/product/vpc)”找到；如果没有私有网络和子网，则可以自己新建一个，注意地域选择“广州”
![](https://blog-img-1301285745.cos.ap-guangzhou.myqcloud.com/kubernetes-admission/6-Edit-Env.png)
![](https://blog-img-1301285745.cos.ap-guangzhou.myqcloud.com/kubernetes-admission/7-VPC.png)
*   修改完成后，将代码推送到你自己的 `CODING Git` 代码仓库；

4.  使用“空白模板”创建构建计划，选择“使用代码仓库的 Jenkinsfile”
![](https://blog-img-1301285745.cos.ap-guangzhou.myqcloud.com/kubernetes-admission/8-Setup-CI.png)

5.  运行构建计划，部署 Serverless 服务
![](https://blog-img-1301285745.cos.ap-guangzhou.myqcloud.com/kubernetes-admission/9-Copy-Serverless-Endpoint.png)
运行完成后，点击“输出 Endpoint”阶段，查看输出的 URL（[类似页面](https://service-faeax9cy-1301578102.gz.apigw.tencentcs.com/release/index)）， 此 URL 即为 Serverless 服务对外提供服务的 URL 。**记录供下一个阶段使用**

至此，腾讯云 Serverless 服务已部署完成。

## Kubernetes 集群部署 Validating Webhook

因为 Admission Webhook 只允许 https 协议并且需要提供证书信息，所以需要我们提前生成，代码仓库已经提供脚本，运行即可配置集群证书。

```sh
$ ./deployment/webhook-create-signed-cert.sh

creating certs in tmpdir /var/folders/mt/965plkfs62v6wqx2839qthz40000gq/T/tmp.i1imELSt
Generating RSA private key, 2048 bit long modulus (2 primes)
...................+++++
....+++++
e is 65537 (0x010001)
certificatesigningrequest.certificates.k8s.io/admission-webhook-example-svc.default created
NAME                                    AGE   REQUESTOR   CONDITION
admission-webhook-example-svc.default   1s    admin       Pending
certificatesigningrequest.certificates.k8s.io/admission-webhook-example-svc.default approved
secret/admission-webhook-example-certs configured
(base)
```
修改 `deployment/deployment.yaml` 文件，将 `serverlessURL` 替换为上一个阶段记录下的 `Endpoint`。[参考例子](https://service-faeax9cy-1301578102.gz.apigw.tencentcs.com/release/index)
![](https://blog-img-1301285745.cos.ap-guangzhou.myqcloud.com/kubernetes-admission/10-Edit-Serverless-Endpoint.png)

证书创建成功后，部署 Deployment 和 Services

```sh
$ kubectl create -f deployment/deployment.yaml
deployment.apps "admission-webhook-example-deployment" created

$ kubectl create -f deployment/service.yaml
service "admission-webhook-example-svc" created
```

至此我们用来接收 Validating 请求的服务已经部署完成，最后配置 `ValidatingWebhookConfiguration`，运行以下命令：

```sh
cat ./deployment/validatingwebhook.yaml | ./deployment/webhook-patch-ca-bundle.sh > ./deployment/validatingwebhook-ca-bundle.yaml
```
执行完成后，可以看到 `validatingwebhook-ca-bundle.yaml` 的 `caBundle` 字段已经被替换。

> 脚本运行依赖于 jq （Shell 读取 JSON 工具），如果你还没有安装，[请移步访问](https://www.ibm.com/developerworks/cn/linux/1612_chengg_jq/index.html)。
> 
> Mac 系统可以直接使用：brew install jq 进行安装。

接下来，我们为 `default` 命名空间打标签，因为我们的 `ValidatingWebhookConfiguration` 使用了 `namespaceSelector` 只对包含特定 labels 的命名空间做两步验证。

```sh
$ kubectl label namespace default admission-webhook-example=enabled
namespace "default" labeled
```

最后，创建 `ValidatingWebhookConfiguration`

```sh
$ kubectl create -f deployment/validatingwebhook-ca-bundle.yaml
validatingwebhookconfiguration.admissionregistration.k8s.io "validation-webhook-example-cfg" created
```

这样，一旦在 `default` 命名空间创建资源，我们部署的服务（Deployment） 将会拦截请求，并进行二次校验。

### 尝试两步验证

至此，我们已经成功部署了两步验证的 Demo，整体架构图现在变成了：

![](https://blog-img-1301285745.cos.ap-guangzhou.myqcloud.com/kubernetes-admission/11-New-Architecture.png)

现在，我们可以尝试部署

```sh
$ kubectl apply -f deployment/sleep.yaml
Error from server (Token 错误，不允许部署): error when creating "deployment/sleep.yaml": admission webhook "required-labels.coding.net" denied the request: Token 错误，不允许部署
```

由于我们在创建 Serverless 服务的时候，预先向数据库配置了四组 token，分别是：1111、2222、3333、4444，所以我们可以修改 `sleep.yaml` ，将注解`metadata.annotations.token` 修改为 `1111`，再次尝试部署

```sh
$ kubectl apply -f deployment/sleep.yaml
deployment.apps/sleep created
```
部署成功，如果重复使用此 token，是无法验证通过的。至此，基于 Serverless 的两步验证已经完成。

## 源码分析
### 我们部署的 Deployment 做了什么

当执行 kubectl apply 之后， API Server 将请求转发到我们部署的 POD ，核心代码在项目根目录下，主要是 `main.go` 和 `webhook.go`

main.go 主要是启动了一个 HTTP 服务，并从命令行读取了我们创建的证书以及 Serverless Endpoint

```go
// main.go

flag.IntVar(&parameters.port, "port", 443, "Webhook server port.")
flag.StringVar(&parameters.certFile, "tlsCertFile", "/etc/webhook/certs/cert.pem", "File containing the x509 Certificate for HTTPS.")
flag.StringVar(&parameters.keyFile, "tlsKeyFile", "/etc/webhook/certs/key.pem", "File containing the x509 private key to --tlsCertFile.")
flag.StringVar(&parameters.serverlessURL, "serverlessURL", "https://example.com", "serverless endpoint URL.")
```
webhook.go 主要是转发 API Server 发送的请求，我们将 `validate` 重新改写，将所有请求转发到 Serverless Endpoint。

```go
// webhook.go

glog.Infof("parameters.serverlessURL is %v", whsvr.parameters.serverlessURL)
res, _ := Post(whsvr.parameters.serverlessURL, req)
// 初始化请求变量结构
jsonData := make(map[string]string)
// 调用json包的解析，解析请求body
_ = json.NewDecoder(res.Body).Decode(&jsonData)
glog.Infof("res is %v", jsonData)
allowed := false
reason := &metav1.Status{
    Reason: "Token 错误，不允许部署",
}
if jsonData["allow"] == "true" {
    allowed = true
}
return &v1beta1.AdmissionResponse{
    Allowed: allowed,
    Result:  reason,
}
```

POD 将请求转发到我们的 Serverless 函数之后，由它来做业务逻辑判断是否允许准入。随后，POD 将 Serverless 的结果重新格式化之后返回给 API Server。

### Serverless 起到了什么作用

我们部署的 Serverless 服务，主要包含了四个部分：
*   API Gateway
*   云函数
*   Postgresql
*   VPC

我们使用 CODING DevOps 在腾讯云部署了以上几个 Serverless 服务，Jenkinsfile 核心代码：

```groovy
stage('部署 Serverless 服务') {
  steps {
    withCredentials([string(credentialsId:"b68948cb-2ad9-4b67-8a49-ad7ba910ed92", variable:'tencent_serverless')]) {
      sh 'echo "${tencent_serverless}" > .tmp'
      sh '''
        SecretId=$(cat .tmp | jq -r .SecretId)
        SecretKey=$(cat .tmp | jq -r .SecretKey)
        token=$(cat .tmp | jq -r .token)
        AppId=$(cat .tmp | jq -r .AppId)
        echo "TENCENT_SECRET_ID=${SecretId}" >> ./serverless/.env
        echo "TENCENT_SECRET_KEY=${SecretKey}" >> ./serverless/.env
        echo "TENCENT_APP_ID=${AppId}" >> ./serverless/.env
        echo "TENCENT_TOKEN=${token}" >> ./serverless/.env
         '''
      sh 'cd serverless && cat .env'
      sh 'cd serverless && npm run bootstrap && sls deploy --all | tee log.log'
      sh 'rm ./serverless/.env'
    }
    echo '部署完成'
  }
}
stage('输出 Endpoint') {
  steps {
    sh 'cd serverless && cat log.log | grep apigw.tencentcs.com'
  }
}
```
这里主要是使用临时凭据，以及使用 Serverless SDK 对预定义的 serverless.yml 进行部署。

**API Gateway 负责对外提供外网访问**

```yaml
# ./serverless/api/serverless.yml API Gateway 部署文件

events:
  - apigw:
      name: k8sAdmission
      parameters:
        protocols:
          - http
          - https
        serviceName:
        description: Based on Tencent Cloud Serverless, it provides dynamic access control for K8S
        environment: release
        endpoints:
          - path: /index
            method: POST

```

**Postgresql 负责存储预定义的 tokens**

```yaml
# ./serverless/db/serverless.yml  数据库部署文件

org: k8sAdmission
app: k8sAdmission-db
stage: dev

component: postgresql
name: fullstackDB

inputs:
  region: ${env:REGION}
  zone: ${env:ZONE}
  dBInstanceName: ${name}
  vpcConfig:
    vpcId: ${output:${stage}:${app}:serverlessVpc.vpcId}
    subnetId: ${output:${stage}:${app}:serverlessVpc.subnetId}
  extranetAccess: false
```

**VPC 实现将云函数和 Postgresql 网络互通**

```yaml
# ./serverless/vpc/serverless.yml VPC部署文件

org: k8sAdmission
app: k8sAdmission-db
stage: dev

component: vpc # (required) name of the component.  In that case, it's vpc.
name: serverlessVpc # (required) name of your vpc component instance.

inputs:
  region: ${env:REGION}
  zone: ${env:ZONE}
  vpcName: serverless
  subnetName: serverless
```

**云函数负责准入逻辑判断，可以看到 `handler: api_service.main_handler`，也就是说云函数的入口函数是 `main_handler`，当有外部请求过来时，将会执行 `main_handler` 函数**

```yaml
# ./serverless/api/serverless.yml 云函数部署文件

org: k8sAdmission
component: scf # (必填) 引用 component 的名称，当前用到的是 tencent-scf 组件
name: k8s # (必填) 该组件创建的实例名称
app: k8sAdmission-db # (可选) 该 SCF 应用名称
stage: dev # (可选) 用于区分环境信息，默认值是 dev

inputs:
  src: ./
  name: ${name}
  description: 基于腾讯云 Serverless 的 K8S 动态准入控制
  handler: api_service.main_handler  # 入口函数
  runtime: Python3.6 # 云函数的运行时环境。除 Nodejs10.15 外，可选值为：Python2.7、Python3.6、Nodejs6.10、Nodejs8.9、PHP5、PHP7、Golang1、Java8。
  region: ${env:REGION}
  vpcConfig:
    vpcId: ${output:${stage}:${app}:serverlessVpc.vpcId}
    subnetId: ${output:${stage}:${app}:serverlessVpc.subnetId}
  timeout: 10
  environment:
    variables:
      PG_CONNECT_STRING: ${output:${stage}:${app}:fullstackDB.private.connectionString}
      PG_DN_NAME: ${output:${stage}:${app}:fullstackDB.private.dbname}
  events:
    - apigw:
        name: k8sAdmission
        parameters:
          protocols:
            - http
            - https
          serviceName:
          description: Based on Tencent Cloud Serverless, it provides dynamic access control for K8S
          environment: release
          endpoints:
            - path: /index
              method: POST
```
**云函数关键代码**

> 我们将在首次触发（请求）时创建 TOKENS 表，并将 4 组预定义的 tokens 插入到表内。并检查我们在执行 kubectl apply yaml 文件 `annotations(注解)` 内携带的 tokens 是否合法，并将 token 和 Postgresql 数据库存储的 token 进行比对。

```py
# ./serverless/api/api_service.py 云函数业务逻辑

def main_handler(event,content):
    logger.info('start main_handler')
    logger.info('got event{}'.format(event))
    logger.info('got content{}'.format(content))
    # 连接数据库
    print('Start Serverlsess DB SDK function')

    conn = psycopg2.connect(DB_HOST)
    print("Opened database successfully")

    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS TOKENS
           (ID INT PRIMARY KEY     NOT NULL,
           tokens TEXT    NOT NULL);''')
    conn.commit()

    cur.execute("select *   from TOKENS")
    myresult = cur.fetchall()
    for row in myresult:
       print("ID = " + str(row[0]))
       print("tokens = " + row[1])

    if not bool(cur.rowcount):
        print("insert default tokens")
        cur.execute("INSERT INTO TOKENS (ID,tokens) \
            VALUES (1, '1111')")
        cur.execute("INSERT INTO TOKENS (ID,tokens) \
            VALUES (2, '2222')")
        cur.execute("INSERT INTO TOKENS (ID,tokens) \
            VALUES (3, '3333')")
        cur.execute("INSERT INTO TOKENS (ID,tokens) \
            VALUES (4, '4444')")
        conn.commit()

    json_dict = json.loads(event["body"])
    if json_dict["object"]["metadata"]["annotations"]["token"] == "":
        return {"errorCode":0,"errorMsg":"","allow":"false"}
    cur.execute("SELECT *   FROM TOKENS where tokens=%s",[json_dict["object"]["metadata"]["annotations"]["token"]])
    myresult = cur.fetchall()
    allow = "false"
    if len(myresult) > 0:
        allow = "true"
        query_id = myresult[0][0]
        cur.execute("DELETE FROM TOKENS where ID=%s",[query_id])
        conn.commit()
    conn.close()
    return {"errorCode":0,"errorMsg":json_dict["object"]["metadata"]["annotations"]["token"],"allow":allow}
```

如果 token 在数据库内存在，则从数据库删除本次使用的 token，并返回 JSON 给**我们在集群内部署的 POD**

```sh
{"errorCode":0,"errorMsg":"tokens","allow":"true"}
```

POD 根据 Serverless 返回的结果重新组装信息，返回如下 JSON 给 `Kubernetes API Server`：

```json
{
    "UID":"b24ab5f7-8b6b-4ea2-83ff-6f9834a9937e",
    "Allowed":false,
    "Result":{
        "ListMeta":{
            "SelfLink":"",
            "ResourceVersion":"",
            "Continue":""
        },
        "Status":"",
        "Message":"",
        "Reason":"Token 错误，不允许部署",
        "Details":"",
        "Code":0
    },
    "Patch":"",
    "PatchType":""
}
```
其中，`Allowed` 字段为本次 `kubectl apply` 是否准入关键，`Reason` 信息将作为结果展示。

> 这里可能有同学会问，为啥要通过我们部署的 POD 再调用 Serverless 服务？让 API Server 直接请求 Serverless Endpoint 不行吗？答案是不行的，因为 API Server 请求的 webhook URL 要求双向 TLS 验证，我们需要创建 Kubernetes CA 签名的 TLS 证书，确保 Webhook 和 Api Server 之间通信的安全，所以我们采用这种方式来实现。

## 结束语

至此，我们实现了简单的 Kubernetes 两步验证。如果想实现更多的逻辑，比如判断 image 合规性、对于来源于非公司内部仓库的镜像拒绝部署，都可以在 Serverless 云函数内实现。

在生产实践中，如本例的 token，属于动态的 yaml 制品类型部署，我们可以结合 `CODING 持续部署`来为制品文件提供动态的参数绑定。

如果想要实现对 Deployment 动态注入 sidecar，可以利用 Mutating Webhook 监听部署的 Deployment，将需要注入的 sidecar 动态 Patch 注入。

如果想要实现集群级的 imagePullSecrets ，一个可行的思路是利用 Mutating Webhook 监听创建 namespaces 行为，自动将已存在的 imagePullSecrets Patch 到新的 namespaces 内。

实现 Mutating Webhook ，请留意项目根目录的 webhook.go 文件的 `mutate` 函数，原理与 Validating Webhook 类似，不同点在于其主要通过 Patch 来实现。

`Kubernetes admission` 通过 Webhook 的方式解耦了 kubectl 的过程，使得我们自己的业务逻辑能够动态加入到用户执行 kubectl 到返回结果的过程当中，本文的两步验证只是一个简单的 Demo，想要更加深入了解，可以浏览“参考资料”的链接。

## 参考资料

*   [In-depth introduction to Kubernetes admission webhooks](https://banzaicloud.com/img/blog/admission-webhooks/webhooks.png)
*   [可扩展 Admission 进入 Beta 阶段](https://blog.fleeto.us/post/admission-beta/)
*   [动态准入控制](https://kubernetes.io/zh/docs/reference/access-authn-authz/extensible-admission-controllers/)
*   [Tencent Serverless](https://console.cloud.tencent.com/product/sls)
*   [本项目 Fork 的源码](https://github.com/banzaicloud/admission-webhook-example)