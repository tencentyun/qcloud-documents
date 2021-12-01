在 istio 中业务容器访问同集群一 Pod IP 返回 404，在 istio-proxy 中访问却正常。

## 原因

Pod 属于 StatefulSet，使用 headless svc，在 istio 中对 headless svc 的支持跟普通 svc 不太一样，如果 pod 用的普通 svc，对应的 listener 有兜底的 passthrough，即转发到报文对应的真实目的IP+Port，但 headless svc 的就没有，我们理解是因为 headless svc 没有 vip，它的路由是确定的，只指向后端固定的 pod，如果路由匹配不上就肯定出了问题，如果也用 passthrough 兜底路由，只会掩盖问题，所以就没有为 headless svc 创建 passthrough 兜底路由。同样的业务，上了 istio 才会有这个问题，也算是 istio 的设计或实现问题。

## 示例场景

使用了自己的服务发现，业务直接使用 Pod IP 调用 StatefulSet 的 Pod IP。

## 解决方案

同集群访问 statefulset pod ip 带上 host，以匹配上 headless svc 路由，避免匹配不到发生404。

