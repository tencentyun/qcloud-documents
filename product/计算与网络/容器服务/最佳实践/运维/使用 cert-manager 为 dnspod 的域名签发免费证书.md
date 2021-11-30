## 概述

如果您的域名使用腾讯云 [DNSPod](https://docs.dnspod.cn/) 管理，并期望在 Kubernetes 上为域名自动签发免费证书，可以使用 cert-manager 来实现。

cert-manager 支持许多 DNS provider，但不支持国内的 DNSPod，不过 cert-manager 提供了 [Webhook](https://cert-manager.io/docs/concepts/webhook/) 机制来扩展 provider，社区也有 DNSPod 的 provider 实现。本文将介绍如何结合 cert-manager 与 [cert-manager-webhook-dnspod](https://github.com/qqshfox/cert-manager-webhook-dnspod) 来实现为 DNSPod 上的域名自动签发免费证书。

## 基础知识

推荐先阅读 [使用 cert-manager 签发免费证书](https://cloud.tencent.com/document/product/457/49368) 。

## 操作步骤

### 1. 创建 DNSPod 密钥

登录 DNSPod 控制台，在 [密钥管理](https://console.dnspod.cn/account/token) 中创建密钥，复制自动生成的 `ID` 和 `Token` 并保存。如下图所示：
![](https://main.qcloudimg.com/raw/2c7f32cae8693fd855b835dfd1f9d532.png)

### 2. 安装 cert-manager
安装 cert-manager，详情可参见 [使用 cert-manager 签发免费证书 ](https://cloud.tencent.com/document/product/457/49368)。



### 3. 安装 cert-manager-webhook-dnspod

使用 HELM 来安装 cert-manager-webhook-dnspod，需准备 HELM 配置文件。
`dnspod-webhook-values.yaml` 示例如下：
<dx-codeblock>
:::  yaml
groupName: example.your.domain # 写一个标识 group 的名称，可以任意写

secrets: # 将前面生成的 id 和 token 粘贴到下面
  apiID: "<ID>"
  apiToken: "<Token>"

clusterIssuer:
  enabled: true # 自动创建出一个 ClusterIssuer
  email: your@email.com # 填写你的邮箱地址
:::
</dx-codeblock>

完整配置请参见 [values.yaml](https://github.com/qqshfox/cert-manager-webhook-dnspod/blob/master/deploy/cert-manager-webhook-dnspod/values.yaml)。

使用 HELM 进行安装：
<dx-codeblock>
:::  bash
git clone --depth 1 https://github.com/qqshfox/cert-manager-webhook-dnspod.git
helm upgrade --install -n cert-manager -f dnspod-webhook-values.yaml cert-manager-webhook-dnspod ./cert-manager-webhook-dnspod/deploy/cert-manager-webhook-dnspod
:::
</dx-codeblock>


### 4. 创建证书

使用如下所示 YAML 文件创建 `Certificate` 对象来签发免费证书：

<dx-codeblock>
:::  yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: example-com-crt
  namespace: istio-system
spec:
  secretName: example-com-crt-secret # 证书保存在这个 secret 中
  issuerRef:
    name: cert-manager-webhook-dnspod-cluster-issuer # 这里使用自动生成出来的 ClusterIssuer
    kind: ClusterIssuer
    group: cert-manager.io
  dnsNames: # 填入需要签发证书的域名列表，确保域名是使用 dnspod 管理的
  - example.com
  - test.example.com
:::
</dx-codeblock>

等待状态变成 Ready 表示签发成功：

<dx-codeblock>
:::  bash
$ kubectl -n istio-system get certificates.cert-manager.io
NAME              READY   SECRET                   AGE
example-com-crt   True    example-com-crt-secret   25d
:::
</dx-codeblock>

若签发失败可通过 describe 查看原因：

<dx-codeblock>
:::  bash
kubectl -n istio-system describe certificates.cert-manager.io example-com-crt
:::
</dx-codeblock>

### 5. 使用证书

证书签发成功后会保存到指定的 Secret 中，可参考以下使用示例：
<dx-tabs>
::: 在 Ingress 中使用
<dx-codeblock>
:::  yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: test-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
spec:
  rules:
  - host: test.example.com
    http:
      paths:
      - path: /
        backend:
          serviceName: web
          servicePort: 80
  tls:
    hosts:
    - test.example.com
    secretName: example-com-crt-secret # 引用证书 secret
:::
</dx-codeblock>
:::
::: 在 Istio 的 ingressgateway 中使用
<dx-codeblock>
:::  yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: example-gw
  namespace: istio-system
spec:
  selector:
    app: istio-ingressgateway
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: HTTP-80
      protocol: HTTP
    hosts:
    - example.com
    - test.example.com
    tls:
      httpsRedirect: true # http 重定向 https (强制 https)
  - port:
      number: 443
      name: HTTPS-443
      protocol: HTTPS
    hosts:
    - example.com
    - test.example.com
    tls:
      mode: SIMPLE
      credentialName: example-com-crt-secret # 引用证书 secret
---
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: example-vs
  namespace: test
spec:
  gateways:
  - istio-system/example-gw # 转发规则绑定到 ingressgateway，将服务暴露出去
  hosts:
  - 'test.example.com'
  http:
  - route:
    - destination:
        host: example
        port:
          number: 80
:::
</dx-codeblock>
:::
</dx-tabs>

