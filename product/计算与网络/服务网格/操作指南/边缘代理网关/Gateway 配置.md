

边缘代理网关的端口、监听规则通过 Gateway CRD 配置。以下是一个 Gateway 配置的示例，重要字段的解释通过注释说明：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: gateway-sample
  namespace: defualt
spec:
  selector: # 根据填写的标签匹配 Gateway 配置下发的 Pod
    istio: ingressgateway
    app: istio-ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - uk.bookinfo.com
    - eu.bookinfo.com
    tls:
      httpsRedirect: true # 发送 301 https 重定向
  - port:
      number: 443
      name: https-443
      protocol: HTTPS # 开启端口 HTTPS
    hosts:
    - uk.bookinfo.com
    - eu.bookinfo.com
    tls:
      mode: SIMPLE # TLS 单向认证
      serverCertificate: /etc/certs/servercert.pem # 文件挂载方式加载证书
      privateKey: /etc/certs/privatekey.pem
  - port:
      number: 9443
      name: https-9443
      protocol: HTTPS # 开启端口 HTTPS
    hosts:
    - "bookinfo-namespace/*.bookinfo.com"
    tls:
      mode: SIMPLE # TLS 单向认证
      credentialName: bookinfo-secret # 通过 SDS 方式从 Kubernetes secret 加载证书
  - port:
      number: 5443
      name: https-ssl
      protocol: HTTPS # 开启端口 HTTPS
    hosts:
    - "*"
    tls:
      mode: SIMPLE # TLS 单向认证
      credentialName: qcloud-abcdABCD # 通过 SDS 方式从腾讯云 SSL 平台加载证书 ID 为 abcdABCD 的证书
  - port:
      number: 6443
      name: clb-https-6443-ABCDabcd # 6443启用证书解包上移至 CLB，使用 ID 为 ABCDabcd 的 SSL 平台证书
      protocol: HTTP
    hosts:
    - "tcm.tencent.com"

```

## Gateway 配置字段说明

以下是 Gateway CRD 重要字段的说明：

| 字段名称 | 字段类型 | 字段说明 |
| ----- | ---- | ----- |
| `metadata.name` | `string` | Gateway 名称 | 
| `metadata.namespace` | `string` | Gateway 命名空间 | 
| `spec.selector` | `map<string, string>` | Gateway 使用填写的标签键值对匹配配置下发的边缘代理网关实例 |
| `spec.servers.port.number` | `uint32` | 端口 |
| `spec.servers.port.protocol` | `string` | 通信协议，支持：`HTTP, HTTPS, GRPC, HTTP2, MONGO, TCP, TLS`，请注意同一网关同一端口的协议配置需要保持一致。 |
| `spec.servers.port.name` | `string` | 端口名称，当前 TCM 实现了通过端口名称指定 SSL 证书解包上移至 CLB 的功能，如您需要配置证书上移，您可以按照 `clb-https-{端口号}-{ssl 平台证书 ID}` 的方式命名，证书上移功能仅在当前端口通信协议指定为 HTTP 时生效，边缘代理网关控制器会自动创建 CLB 7层监听器实现证书上移，CLB SSL 解包完成后，CLB 实例与 Ingress Gateway Pod 采用明文通信。请注意同一网关同一端口的证书上移配置需要保持一致，否则会引起配置冲突。 |
| `spec.severs.hosts` | `string[]` | 域名，支持通配符 `*` |
| `spec.servers.tls.httpsRedirect` | `bool` | 值为 `true` 时，边缘代理网关会对所有 http 请求返回 301 重定向，要求客户端发起 https 请求 |
| `spec.servers.tls.mode` | - | 配置当前端口的 TLS 安全认证模式，如需要开启当前端口的安全认证则需要填写。支持：`PASSTHROUGH, SIMPLE, MUTUAL, AUTO_PASSTHROUGH, ISTIO_MUTUAL` |
| `spec.servers.tls.credentialName` | `string` | 配置发现 TLS 证书密钥的 secret 的名称，支持从 Ingress Gateway 实例在同一 namespace 下的 Kubernetes secret 中加载证书与密钥，您需要确保填写的 secret 中包含合适的证书与密钥。 TCM 还实现了加载腾讯云 SSL 平台证书的功能，按照 `qcloud-{ssl 平台证书 ID}` 格式填写本字段，TCM 边缘代理网关控制器即会为边缘代理网关加载 SSL 平台的证书。当前仅支持从 SSL 平台加载单向认证 SIMPLE 模式的服务器证书和私钥 |
| `spec.servers.tls.serverCertificate` | `string` | 设置端口的 TLS 证书密钥通过 file mount 形式（不推荐，推荐采用填写 `credentialName` 字段加载证书私钥）挂载时需要填写的证书路径字段，Istio 默认使用网关所在命名空间下 istio-ingressgateway-certs secret 加载证书至路径 `/etc/istio/ingressgateway-certs` |
| `spec.servers.tls.privateKey ` | `string` | 设置端口的 TLS 证书密钥通过 file mount 形式（不推荐，推荐采用填写 `credentialName` 字段加载证书私钥）挂载时需要填写的私钥路径字段，Istio 默认使用网关所在命名空间下 istio-ingressgateway-certs secret 加载私钥至路径 `/etc/istio/ingressgateway-certs` |
| `spec.servers.tls.caCertificates` | `string` | 设置端口的 TLS 证书密钥通过 file mount 形式（不推荐，推荐采用填写 `credentialName` 字段加载证书私钥）挂载时需要填写的跟证书路径字段，Istio 默认使用网关所在命名空间下 istio-ingressgateway-ca-certs 加载根证书至路径 `/etc/istio/ingressgateway-ca-certs`，双向认证时需要配置根证书 |


## 示例

#### 从 Kubernetes Secret 加载证书至边缘代理网关配置示例

<dx-tabs>
::: YAML 配置示例
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: sample-gw
  namespace: default
spec:
  servers:
    - port:
        number: 443
        name: HTTPS-443-6cph
        protocol: HTTPS
      hosts:
        - '*'
      tls:
        mode: SIMPLE
        credentialName: {kubernetes secret 名称}
  selector:
    app: istio-ingressgateway
    istio: ingressgateway
```
:::
::: 控制台配置示例
控制台创建 Gateway 配置 Ingress Gateway HTTPS 协议 SSL 证书从 Kubernetes secret 加载（单向认证）的过程如下：

1. 选择协议为**HTTPS**，TLS 模式为**SIMPLE**
2. 证书解包选择**边缘代理网关解包**
3. 证书挂载模式选择**SDS加载**
4. 证书来源选择**K8S Secret**
5. K8S Secret 选择**选择已有**，选择当前所选边缘代理网关所在 namespace 下的 Secret，请您确保所选 Secret 中包含合适的证书/私钥/根证书
![](https://main.qcloudimg.com/raw/bedf6f7589c35e39719956148c1c1ecd.png)
6. 如当前 Secret 中未有合适证书，您可以选择**新建**K8S Secret，复制合适的证书/私钥/跟证书内容至对应输入框
![](https://main.qcloudimg.com/raw/516797c700455ed6a68fb547b49cc744.png)
:::
</dx-tabs>



#### 从 SSL 平台加载证书至边缘代理网关配置示例

<dx-tabs>
::: YAML 配置示例
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: test-gw
spec:
  servers:
    - port:
        number: 443
        name: HTTPS-443-9ufr
        protocol: HTTPS
      hosts:
        - '*'
      tls:
        mode: SIMPLE
        credentialName: qcloud-{证书ID}
  selector:
    app: istio-ingressgateway
    istio: ingressgateway
```
:::
::: 控制台配置示例
除了通过 YAML 文件配置，您也可以在控制台上通过 UI 创建 Gateway 配置。以下是配置从 SSL 平台加载证书至边缘代理网关的配置示例，您选择证书来源为 **SSL 平台证书**即可选择需要加载的 SSL 平台证书。
 
 ![](https://main.qcloudimg.com/raw/696020c23796f0bd73e6d7daaeb6bfe2.png)

:::
</dx-tabs>





#### SSL 证书解包上移至 CLB 配置示例

<dx-tabs>
::: YAML 配置示例
以下是配置 443 端口证书解包上移至 CLB，且为该端口启用 SNI，域名 `sample.hosta.org` 使用证书1，域名 `sample.hostb.org` 使用证书2。
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: test-gw
spec:
  servers:
    - port:
        number: 443
        name: clb-https-443-{证书ID 1}
        protocol: HTTP
      hosts:
        - sample.hosta.org
    - port:
        number: 443
        name: clb-https-443-{证书ID 2} 
        protocol: HTTP
      hosts:
        - sample.hostb.org
  selector:
    app: istio-ingressgateway
    istio: ingressgateway
```
:::
::: 控制台配置示例
在控制台 UI 创建 Gateway 配置使用证书上移功能流程如下：

1. 选择协议为 HTTPS，出现**TLS 模式选项**。
2. 选择**TLS 模式**为**SIMPLE**。
3. 选择**证书解包**为**CLB 解包**，此时端口协议将自动变化为 HTTP（选择证书上移后网关处按照明文 HTTP 处理流量）。
4. 选择合适的**服务器证书**。

![](https://main.qcloudimg.com/raw/4f87fd189a225bf3c8c702a301031c7f.png)

创建成功将跳转至创建完成的 Gateway CRD 详情页面：

![](https://main.qcloudimg.com/raw/83becd79146dae9c76fe4f71cfbdabba.png)
:::
</dx-tabs>
