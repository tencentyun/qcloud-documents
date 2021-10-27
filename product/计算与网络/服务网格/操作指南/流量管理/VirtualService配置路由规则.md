VirtualService 定义了指定 hosts 的一系列路由规则和流量操作（权重路由，故障注入等），其中每一条路由规则都定义了指定流量协议的匹配规则，如流量匹配，则被路由至指定的服务或服务的版本。VirtualService 配置主要包含以下部分：

- **hosts**：定义路由规则关联的 hosts，可以是带有通配符的 DNS 名称或者 IP 地址。
- **gateways**：定义应用路由规则的来源流量，可以是：
	- 一个或多个网关。
	- 网格内部的 sidecar。
- **路由规则**：定义详细的路由规则，包括 HTTP，TLS/HTTPS，TCP 三种协议类型的路由规则。
	- http：定义一组有序的应用于 HTTP 流量的路由规则。
	- tcp：定义一组有序的应用于 TCP 流量的路由规则。
	- tls：定义一组有序的应用于未终止的 TLS 或 HTTPS 流量的路由规则。

## VirtualService 重要字段说明

以下是 VirtualService 的重要字段说明：

| 字段名称 | 字段类型 | 字段说明 |
| ----- | ---- | ----- |
| `spec.hosts` | `string[]`| 定义路由规则关联一组的 hosts，可以是带有通配符的 DNS 名称或者 IP 地址（IP 地址仅能应用于来源流量为边缘代理网关）。该字段能应用于 HTTP 和 TCP 流量。在 Kubernetes 环境中，可以使用 service 的名称作为缩写，Istio 会按照 VirtualService所在 namespace 补齐缩写，例如在 default namespace 的 VirtualService 包含 host 缩写 `reviews` 会被补齐为 `reviews.default.svc.cluster.local`。为避免误配置，推荐填写 host 全称 |
| `spec.gateways ` | `string[]` | 定义应用路由规则的来源流量，可以是一个或多个网关，或网格内部的 sidecar，指定方式为 `<gateway namespace>/<gateway name>`，保留字段 `mesh` 表示网格内部所有的 sidecar，当该参数缺省时，会默认填写 `mesh`，即该路由规则的来源流量为网格内部所有 sidecar |
| `spec.http` | `HTTPRoute[]` | 定义一组有序的（优先匹配靠前的路由规则）应用于 HTTP 流量的路由规则，HTTP 路由规则会应用于网格内部的 service 端口命名为 `http-`, `http2-`, `grpc-` 开头的流量以及来自 gateway 的协议为 `HTTP, HTTP2, GRPC, TLS-Terminated-HTTPS` 的流量|
| `spec.http.match` | `HTTPMatchRequest[]` | 定义路由的匹配规则列表，单个匹配规则项内所有条件是且关系，列表中多个匹配规则之间为或关系|
| `spec.http.route` | `HTTPRouteDestination[]` | 定义路由转发目的地列表，一条 HTTP 路由可以是重定向或转发（默认），转发的目的地可以是一个或多个服务（服务版本）。同时也可以配置权重、header 操作等行为 |
| `spec.http.redirect` | `HTTPRedirect` | 定义路由重定向，一条 HTTP 路由可以是重定向或转发（默认），如规则中指定了 `passthrough ` 选项，route、redirect 均会被忽略。可将 HTTP 301 重定向到另外的 URL 或 Authority |
| `spec.http.rewrite` | `HTTPRewrite` | 定义重写 HTTP URL 或 Authority headers，不能与重定向同时配置，重写操作会在转发前执行 |
| `spec.http.timeout` | [Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) | 定义 HTTP 请求的超时时间 |
| `spec.http.retries` | `HTTPRetry` | 定义 HTTP 请求的重试策略 |
| `spec.http.fault` | `HTTPFaultInjection` | 定义 HTTP 流量的故障注入策略，开启时超时和重试策略不会开启 |
| `spec.http.mirror` | `Destination` | 定义将 HTTP 流量复制到另一个指定的目的端，被复制的流量按照“best effort”原则，sidecar/网关不会等待复制流量的响应结果就会从源目的端返回响应。镜像流量的目的服务端会产生监控指标。 |
| `spec.http.mirrorPercent` | `uint32 ` | 定义流量镜像的复制百分比，缺省时复制100%的流量。最大值为100 |
| `spec.http.corsPolicy` | `CorsPolicy` | 定义 CORS 策略（跨域资源共享，Cross-Origin Resource Sharing，CORS），更多关于 CORS 的介绍请参见 [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)，关于 Istio CORS 策略配置语法请参见 [CorsPolicy](https://istio.io/latest/docs/reference/config/networking/virtual-service/#CorsPolicy) |
| `spec.http.headers` | `Headers` | 定义 header 操作规则，包括 request 和 response header 的更新，增加，移除操作|
| `spec.tcp` | `TCPRoute[]` | 定义一组有序的（优先匹配靠前的路由规则）应用于 TCP 流量的路由规则，该路由规则会应用于任何非 HTTP 和 TLS 的端口 |
| `spec.tcp.match` | `L4MatchAttributes[]` | 定义 TCP 流量路由的匹配规则列表，单个匹配规则项内所有条件是且关系，列表中多个匹配规则之间为或关系 |
| `spec.tcp.route` | `RouteDestination[]`| 定义 TCP 连接转发的目的端 |
| `spec.tls` | `TLSRoute[]` | 定义一组有序的（优先匹配靠前的路由规则）应用于未终止的 TLS 或 HTTPS 流量的路由规则，该路由规则会应用于网格内部的 service 端口命名为 `https-`，`tls-` 开头的流量，来自 gateway 的端口协议为 `HTTPS, TLS` 的未终止加密流量，Service Entry 使用 `HTTPS, TLS` 协议的端口。当 `https-`, `tls-` 端口未关联 VirtualService 规则时将会被视为 TCP 流量 |
| `spec.tls.match` | `TLSMatchAttributes[]` | 定义 TLS 流量路由的匹配规则列表，单个匹配规则项内所有条件是且关系，列表中多个匹配规则之间为或关系 |
| `spec.tls.route` | `RouteDestination[]` | 定义连接转发的目的端 |

## 配置来自 Gateway 流量（南北向）的路由规则

VirtualService 可通过控制台 UI 和 YAML 编辑两种方式配置。下面将展示将来自 Gateway 流量路由至服务 frontend 的 VirtualService 配置。相关的 Gateway 配置如下：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: frontend-gw
  namespace: base
spec:
  servers:
    - port:
        number: 80
        name: http
        protocol: HTTP
      hosts:
        - '*'
  selector:
    app: istio-ingressgateway
    istio: ingressgateway
```

<dx-tabs>
::: YAML 配置示例
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: frontend-vs
  namespace: base
spec:
  hosts:
    - '*'
  gateways:
    - base/frontend-gw # VS 挂载的 Gateway 填写按照 {namespace}/{Gateway 名称}
  http:
    - route:
        - destination:
            host: frontend.base.svc.cluster.local # 路由目的地填写 frontend 服务的 host 全称
```
:::
::: 控制台配置示例
![](https://main.qcloudimg.com/raw/8f7ee1c7bae86cc8c64b06bf3acd6c03.png)
:::
</dx-tabs>



## 配置来自 Mesh 内部流量（东西向）的路由规则

以下是设置将来自网格内部访问 product 服务 host: `product.base.svc.cluster.local` 的流量的路由规则：50%的流量路由至 v1 版本，50%的流量路由至 v2 版本的 VirtualService 配置示例（灰度发布）。其中 product 的服务版本是通过以下 DestinationRule 定义：

```yaml
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
        version: v1
    - name: v2
      labels:
        version: v2
```

<dx-tabs>
::: YAML 配置示例
```
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: product-vs
  namespace: base
spec: # 缺省 gateway 参数，表示该路由配置应用于 mesh 内部 sidecar 的流量
  hosts:
    - "product.base.svc.cluster.local" # 匹配访问该 host 的流量
  http:
    - match:
        - uri:
            exact: /product
      route:
        - destination: # 配置目的端及权重
            host: product.base.svc.cluster.local
            subset: v1
            port:
              number: 7000
          weight: 50
        - destination:
            host: product.base.svc.cluster.local
            subset: v2
            port:
              number: 7000
          weight: 50
```

:::
::: 控制台配置示例
![](https://main.qcloudimg.com/raw/4de8befe5c17f08022f2c60517144a7f.png)
:::
</dx-tabs>

