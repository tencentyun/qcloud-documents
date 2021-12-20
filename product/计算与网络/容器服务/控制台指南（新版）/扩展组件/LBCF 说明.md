## 简介

### 组件介绍

Load Balancer Controlling Framework（LBCF）是一款部署在 Kubernetes 内的通用负载均衡控制面框架，旨在降低容器对接负载均衡的实现难度，并提供强大的扩展能力以满足业务方在使用负载均衡时的个性化需求。

### 部署在集群内的 Kubernetes 对象

在集群内部署 LBCF 组件，将在集群内部署以下 Kubernetes 对象：

| Kubernetes 对象名称                                 | 类型                             | 默认占用资源 | 所属 Namespaces |
| ---------------------------------------------- | ------------------------------ | ------ | ------------ |
| lbcf-controller                                | Deployment                     | -      | kube-system  |
| lbcf-controller                                | ServiceAccount                 | -      | kube-system  |
| lbcf-controller                                | ClusterRole                    | -      | -            |
| lbcf-controller                                | ClusterRoleBinding             | -      | -            |
| lbcf-controller                                | Secret                         | -      | kube-system  |
| lbcf-controller                                | Service                        | -      | kube-system  |
| backendrecords.lbcf.tke.cloud.tencent.com      | CustomResourceDefinition       | -      | -            |
| backendgroups.lbcf.tke.cloud.tencent.com       | CustomResourceDefinition       | -      | -            |
| loadbalancers.lbcf.tke.cloud.tencent.com       | CustomResourceDefinition       | -      | -            |
| loadbalancerdrivers.lbcf.tke.cloud.tencent.com | CustomResourceDefinition       | -      | -            |
| lbcf-mutate                                    | MutatingWebhookConfiguration   | -      | -            |
| lbcf-validate                                  | ValidatingWebhookConfiguration | -      | -            |

## 使用场景

LBCF 对 Kubernetes 内部晦涩的运行机制进行了封装并以 Webhook 的形式对外暴露，在容器的全生命周期中提供了多达8种 Webhook。通过这些 Webhook，开发人员可以轻松实现下述功能：

- 对接任意负载均衡/名字服务，并自定义对接过程。
- 实现自定义灰度升级策略。
- 容器环境与其他环境共享同一个负载均衡。
- 解耦负载均衡数据面与控制面。

##  限制条件
LBCF 对系统有以下要求： 
- 支持 Kubernetes 1.10 及以上版本的集群。
- 需开启 Dynamic Admission Control，并在 apiserver 中添加以下启动参数：
```
-enable-admission-plugins=MutatingAdmissionWebhook,ValidatingAdmissionWebhook
```
- Kubernetes 1.10 版本，则需在 apiserver 中额外添加以下参数：
```
--feature-gates=CustomResourceSubresources=true
```

>?推荐您在 [腾讯云容器服务](https://cloud.tencent.com/product/tke2) 中购买 1.12.4 版本集群，无需修改任何参数，开箱可用。

## 使用方法
### 组件安装
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**扩展组件**。
2. 在“扩展组件”管理页面上方，选择地域及需安装 LBCF 的集群，并单击**新建**。如下图所示：
![](https://main.qcloudimg.com/raw/887d95fb6d298edbb4e9a329440c22c1.png)
3. 开发或选择安装 LBCF Webhook 规范，实现 Webhook 服务器。






### LBCF CLB driver
本文以腾讯云 CLB 开发的 Webhook 服务器为例。

#### 功能列表

- 使用已有负载均衡。
- 创建新的负载均衡（四层/七层）。
- 绑定 Service NodePort。
- CLB 直通 Pod（直接绑定 Pod 至 CLB，不通过 Service）。
- 权重调整。
- 能够校验并拒绝非法参数。

#### 部署 LBCF CLB driver
1. 请使用 [附录](#other) 中提供的 yaml 文件进行部署，部署前需修改 `deploy.yaml` 的以下信息：
	- 镜像信息
	- 所在地域
	- 所在 vpcID，绑定 service NodePort 时用来查找节点对应的 instanceID。
	- secret-id 及 secret-key，可前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取。
```
    spec:
      priorityClassName: "system-node-critical"
      containers:
        - name: driver
          image: ${image-name}
          args:
            - "--region=${your-region}"
            - "--vpc-id=${your-vpc-id}"
            - "--secret-id=${your-account-secret-id}"
            - "--secret-key=${your-account-secret-key}"
```
2. 登录集群，使用以下命令安装 YAML 。
```
kubectl apply -f configmap.yaml
kubectl apply -f deploy.yaml
kubectl apply -f service.yaml
```

#### 具体示例
- 使用已有四层 CLB。
本例中使用了 ID 为 `lb-7wf394rv` 的负载均衡实例，监听器为四层监听器，端口号为20000，协议类型 TCP。
>!程序会以**端口号20000，协议类型 TCP** 为条件查询监听器，若不存在，将自动新建。
>
```
apiVersion: lbcf.tke.cloud.tencent.com/v1beta1
kind: LoadBalancer
metadata:
  name: example-of-existing-lb 
  namespace: kube-system
spec:
  lbDriver: lbcf-clb-driver
  lbSpec:
    loadBalancerID: "lb-7wf394rv"
    listenerPort: "20000"
    listenerProtocol: "TCP"
  ensurePolicy:
    policy: Always
```

- 创建新的七层 CLB。
本例在 VPC `vpc-b5hcoxj4` 中创建了公网（OPEN）负载均衡实例，并为之创建了端口号为9999的 HTTP 监听器，最终会在监听器中创建 `mytest.com/index.html` 的转发规则。
```
apiVersion: lbcf.tke.cloud.tencent.com/v1beta1
kind: LoadBalancer
metadata:
  name: example-of-create-new-lb 
  namespace: kube-system
spec:
  lbDriver: lbcf-clb-driver
  lbSpec:
    vpcID: vpc-b5hcoxj4
    loadBalancerType: "OPEN"
    listenerPort: "9999"
    listenerProtocol: "HTTP"
    domain: "mytest.com"
    url: "/index.html"
  ensurePolicy:
    policy: Always
```
- 设定 backend 权重。
本例展示了 Service NodePort 的绑定。被绑定 Service 的名称为 svc-test，service port 为80（TCP），绑定到 CLB 的每个`Node:NodePort` 的权重都是66。
```
apiVersion: lbcf.tke.cloud.tencent.com/v1beta1
kind: BackendGroup
metadata:
  name: web-svc-backend-group
  namespace: kube-system
spec:
  lbName: test-clb-load-balancer
  service:
    name: svc-test
    port:
      portNumber: 80
  parameters:
    weight: "66"
```

## 附录[](id:other)

### 腾讯云 CLB LBCF driver
#### ConfigMap
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: trusted-tencentcloudapi
  namespace: kube-system
data:
  tencentcloudapi.pem: |
    -----BEGIN CERTIFICATE-----
    MIIGgDCCBWigAwIBAgIMIsk10+Y2GGXUKTrmMA0GCSqGSIb3DQEBCwUAMGYxCzAJ
    BgNVBAYTAkJFMRkwFwYDVQQKExBHbG9iYWxTaWduIG52LXNhMTwwOgYDVQQDEzNH
    bG9iYWxTaWduIE9yZ2FuaXphdGlvbiBWYWxpZGF0aW9uIENBIC0gU0hBMjU2IC0g
    RzIwHhcNMTgxMjIwMDcxNTA5WhcNMTkxMjIxMDcxNTA5WjCBjDELMAkGA1UEBhMC
    Q04xEjAQBgNVBAgTCWd1YW5nZG9uZzERMA8GA1UEBxMIc2hlbnpoZW4xNjA0BgNV
    BAoTLVRlbmNlbnQgVGVjaG5vbG9neSAoU2hlbnpoZW4pIENvbXBhbnkgTGltaXRl
    ZDEeMBwGA1UEAwwVKi50ZW5jZW50Y2xvdWRhcGkuY29tMIIBIjANBgkqhkiG9w0B
    AQEFAAOCAQ8AMIIBCgKCAQEAyepbdY0laI2rgfm1qe4TUv0kR9r0YJQwTwXN3LM6
    2W75Y5m2k9WcfFilcoah9q4J1ndkbtiDSaLRYJYce7ivObmR79gb4MGCrnVix0eI
    KYW1qiFIBjETxhzTZt4sVztty4LW0F+R4lggraAP8d7qdsbFTyk4y9dKHS1FANQc
    xVkxdFIMCk+WoppMmTI2DpNg9kY6BrL7TiLyjx8gpF1XymKl0CefqYxwZt/+KEaA
    75G/R361h2wi5lFC1ybhGtlPT6t285A6j6avC7AqEhdZQqoAv60iQud2Hj7bmkbf
    OTgE24+5LepekWyK0iEDCHX8aN/wtfKPLqA3oQVlnLLlbQIDAQABo4IDBTCCAwEw
    DgYDVR0PAQH/BAQDAgWgMIGgBggrBgEFBQcBAQSBkzCBkDBNBggrBgEFBQcwAoZB
    aHR0cDovL3NlY3VyZS5nbG9iYWxzaWduLmNvbS9jYWNlcnQvZ3Nvcmdhbml6YXRp
    b252YWxzaGEyZzJyMS5jcnQwPwYIKwYBBQUHMAGGM2h0dHA6Ly9vY3NwMi5nbG9i
    YWxzaWduLmNvbS9nc29yZ2FuaXphdGlvbnZhbHNoYTJnMjBWBgNVHSAETzBNMEEG
    CSsGAQQBoDIBFDA0MDIGCCsGAQUFBwIBFiZodHRwczovL3d3dy5nbG9iYWxzaWdu
    LmNvbS9yZXBvc2l0b3J5LzAIBgZngQwBAgIwCQYDVR0TBAIwADBJBgNVHR8EQjBA
    MD6gPKA6hjhodHRwOi8vY3JsLmdsb2JhbHNpZ24uY29tL2dzL2dzb3JnYW5pemF0
    aW9udmFsc2hhMmcyLmNybDA1BgNVHREELjAsghUqLnRlbmNlbnRjbG91ZGFwaS5j
    b22CE3RlbmNlbnRjbG91ZGFwaS5jb20wHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsG
    AQUFBwMCMB0GA1UdDgQWBBRR63cbhz8Aloch9ZEw6Y4TZKXspjAfBgNVHSMEGDAW
    gBSW3mHxvRwWKVMcwMx9O4MAQOYafDCCAQYGCisGAQQB1nkCBAIEgfcEgfQA8gB3
    AFWB1MIWkDYBSuoLm1c8U/DA5Dh4cCUIFy+jqh0HE9MMAAABZ8p32P4AAAQDAEgw
    RgIhAOBSocmwefb43lFbW9CVd9Kx6P6o35YLoXR5YO6vae2bAiEAwVSFT6xIb7wG
    mQqVwUItRUG9LtqjuQNhfMkhPiCV3zsAdwDuS723dc5guuFCaR+r4Z5mow9+X7By
    2IMAxHuJeqj9ywAAAWfKd9YUAAAEAwBIMEYCIQC8txn4L1STQ9ai4JcWJ6vwNoc4
    5tFfQsKXDGs4CXHaUgIhAJ7PTTgajS5A9xTvTdD0Tw3iH643MjjdLTKH83Qdu2ty
    MA0GCSqGSIb3DQEBCwUAA4IBAQDFu2JcyLG3Bg8YhJi+IqoTljwGsYC98i148hoT
    CwlbwH3UaHrPlR1crX8Hv+XEsHj4Ot3/krdiuYGWEZVhY61e8DT3QovUTXh6pvG+
    R9Q22SfGMuGuwrgTdhfR5QYv4whE/Mj4TqJQDRGBetb9dpPkhhLN6E+h/9/WmGyC
    HObUUZyEP1rTqgPxLk8e5Xyt8yv/loo5eptQXvduY/v4ngpvJScqepDXedSJd3SK
    Muu7gepolidg/fBlZjfpksLWSUGVVuVUS4zT2gaMpTqD/NjxHwC3roIiP9pSnY7w
    GcPWfnp6Xs8ahCmiYdOEwbrMH/QtEdRdonsPyMS2FU3Rv7hD
    -----END CERTIFICATE-----
```

#### Deploy
```yaml
apiVersion: lbcf.tke.cloud.tencent.com/v1beta1
kind: LoadBalancerDriver
metadata:
  name: lbcf-clb-driver
  namespace: kube-system
spec:
  driverType: Webhook
  url: "http://lbcf-clb-driver.kube-system.svc"
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: lbcf-clb-driver
  namespace: kube-system
spec:
  replicas: 1
  selector:
    matchLabels:
      lbcf.tke.cloud.tencent.com/component: lbcf-clb-driver
  template:
    metadata:
      labels:
        lbcf.tke.cloud.tencent.com/component: lbcf-clb-driver
    spec:
      priorityClassName: "system-node-critical"
      containers:
        - name: driver
          image: ${image-name}
          args:
            - "--region=${your-region}"
            - "--vpc-id=${your-vpc-id}"
            - "--secret-id=${your-account-secret-id}"
            - "--secret-key=${your-account-secret-key}"
          ports:
            - containerPort: 80
              name: insecure
          imagePullPolicy: Always
          volumeMounts:
            - name: trusted-ca
              mountPath: /etc/ssl/certs
              readOnly: true
      volumes:
        - name: trusted-ca
          configMap:
            name: trusted-tencentcloudapi
```

#### Service
```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
  name: lbcf-clb-driver
  namespace: kube-system
spec:
  ports:
    - name: insecure
      port: 80
      targetPort: 80
  selector:
    lbcf.tke.cloud.tencent.com/component: lbcf-clb-driver
  sessionAffinity: None
  type: ClusterIP
```


