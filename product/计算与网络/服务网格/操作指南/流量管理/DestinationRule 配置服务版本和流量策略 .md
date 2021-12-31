DestinationRule 定义服务的版本和路由发生后的流量策略，包括负载均衡、连接池大小、健康检查（从负载均衡后端中剔除不健康的 hosts）等流量策略。服务与 DestinationRule 是一对一的绑定关系。

## DestinationRule 重要字段说明

以下是 DestinationRule 的重要字段说明：

| 字段名称 | 字段类型 | 字段说明 |
| ----- | ---- | ----- |
| `spec.host` | `string` | 关联 DestinationRule 配置的服务名称，可以是自动发现的服务（例如 Kubernetes service name），或通过 ServiceEntry 声明的 hosts。如填写的服务名无法在上述源中找到，则该 DestinationRule 中定义的规则无效 |
| `spec.subsets` | `Subset[]` | 定义服务的版本（subsets），版本可通过标签键值对匹配匹配服务中的endpoints。可以在 subsets 级覆盖流量策略配置 |
| `spec.trafficPolicy` | `trafficPolicy` | 定义流量策略，包括负载均衡、连接池、健康检查、TLS 策略 |
| `spec.trafficPolicy.loadBalancer` | - | 配置负载均衡算法，可配置：简单负载均衡算法（round robin, least conn, random...），一致性哈希（会话保持，支持按 header name，cookie，IP，query parameter 哈希），地域感知负载均衡算法 |
| `spec.trafficPolicy.connectionPool` | - | 配置与上游服务的连接量，可设置 TCP/HTTP 的连接池 |
| `spec.trafficPolicy.outlierDetection` | - | 配置从负载均衡池中驱逐不健康的 hosts |
| `spec.trafficPolicy.tls` | - | 连接上游服务的 client 端 TLS 相关配置，与 PeerAuthentication 策略（server 端 TLS 模式配置）配合使用 |
| `spec.trafficPolicy.portLevelSettings` | - | 配置端口级别的流量策略，端口级别的流量策略会覆盖服务 / subsets 级别的流量策略配置 |

## 定义服务的版本（subsets）

DestinationRule 可定义服务的版本（subsets），而 subset 则是腾讯云服务网格的最小流量管理单元。例如，您可以配置将流量路由至某个指定服务的指定 subset。以下是 DestinationRule 定义 product 服务两个 subset 的配置示例。

<dx-tabs>
::: YAML 配置示例
```
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: product
  namespace: base
spec:
  host: product 
  subsets:
    - name: v1
      labels:
        version: v1 # subset v1 通过标签 version:v1 来匹配该服务的endpoint
    - name: v2
      labels:
        version: v2 # subset v2 通过标签 version:v2 来匹配该服务的endpoint
```
:::
::: 控制台配置示例
DestinationRule 和服务是一一对应的绑定关系，配置 product 服务的 DestinationRule，需要从服务列表页进入 product 服务的详情页，在基本信息 Tab 配置。控制台配置 product 服务两个版本的步骤如下：

1. 在服务列表页面，单击进入 product 服务的详情页面。
![](https://main.qcloudimg.com/raw/83fcacd9c9d8869ebfed3185e74bf268.png)
2. 在服务详情页**基本信息**，第三个DestinationRule card 区域，单击**新建 DestinationRule**进入新建弹窗。
![](https://main.qcloudimg.com/raw/77d8c7f446d9108a7cd614a3ee9922b2.png)
3. 在弹窗页面为 product 服务添加两个版本，点击保存。
![](https://qcloudimg.tencent-cloud.cn/raw/5adfe509520625b4b401584d3886ad42.png)
4. product 服务版本配置完成。
![](https://main.qcloudimg.com/raw/a18963bf33e8ebeb54a6e4a4925a88a4.png)

:::
</dx-tabs>



## 配置一致性哈希负载均衡

以下是用 DestinationRule 配置 cart 服务按照 http header name 做一致性哈希负载均衡的配置示例。

<dx-tabs>
::: YAML 配置示例
```
kind: DestinationRule
metadata:
  name: cart
  namespace: base
spec:
  host: cart
  trafficPolicy:
    loadBalancer:
      consistentHash:
        httpHeaderName: UserID # 配置访问 cart 服务的流量按照 header UserID 做一致性哈希负载均衡
```
:::
::: 控制台配置示例
![](https://qcloudimg.tencent-cloud.cn/raw/5c45fab53bd927158766179ec7e58efa.png)
:::
</dx-tabs>

