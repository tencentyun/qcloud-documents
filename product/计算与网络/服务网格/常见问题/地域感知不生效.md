使用 istio 地域感知能力时，测试发现没生效，本文介绍几个常见原因。

## DestinationRule 未配置 outlierDetection

地域感知默认开启，但还需要配置 DestinationRule，且指定 `outlierDetection` 才可以生效，指定这个配置的作用主要是让 istio 感知 endpoints 是否异常，当前 locality 的 endpoints 发生异常时会 failover 到其它地方的 endpoints。

配置示例：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: nginx
spec:
  host: nginx
  trafficPolicy:
    outlierDetection:
      consecutive5xxErrors: 3
      interval: 30s
      baseEjectionTime: 30s
```

## client 没配置 service

istio 控制面会为每个数据面单独下发 EDS，不同数据面实例(Envoy)的locality可能不一样，生成的 EDS 也就可能不一样。istio会获取数据面的locality信息，获取方式主要是找到数据面对应的 endpoint 上保存的 region、zone 等信息，如果 client 没有任何 service，也就不会有 endpoint，控制面也就无法获取 client 的 locality 信息，也就无法实现地域感知。

#### 解决方案
为 client 配置 service，selector 选中 client 的 label。如果 client 本身不对外提供服务，service 的 ports 也可以随便定义一个。

## 使用了 headless service

如果是访问 headless service，本身是不支持地域感知的，因为 istio 会对 headless service 请求直接 passthrough，不做负载均衡，客户端会直接访问到 dns 解析出来的 pod ip。

#### 解决方案
单独再创建一个 service (非 headless)。
