 
 ## 操作场景
 购物车服务由多个 pod 副本运行，需要会话保持功能，以保证同一用户请求被路由至同一个 pod，保证同一用户的购物车信息不会丢失。
会话保持如下图所示：
![会话保持](https://qcloudimg.tencent-cloud.cn/raw/4379400bd7fa29e6e1e66f5eebf4bb3e.svg)
 

 ## 操作步骤
会话保持功能可通过设置 cart 服务 DestinationRule 的负载均衡策略实现，以请求中 header 中的 UserID 做一致性 hash 负载均衡。

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: cart
  namespace: base
spec:
  host: cart
  trafficPolicy:
    loadBalancer:
      consistentHash:
        httpHeaderName: UserID
  exportTo:
    - '*'
```

配置完成后，可在登录状态多次点击 “Your Cart” 或点击 “ADD TO CART” 调用 cart 服务验证会话保持功能，同一用户的多次请求会被路由至同一个 pod，左下角悬浮窗可查看提供 cart 服务的 pod name。同一用户多次请求的 pod name 不会变化。来自同一用户的多次请求被负载均衡至相同 pod 如下图所示：

![来自同一用户的多次请求被负载均衡至相同 pod](https://qcloudimg.tencent-cloud.cn/raw/28235220c55b260dc436c143ef9a3f97.png)
 
