## 未定义 http1MaxPendingRequests导致熔断不生效

我们给 DR 配置了 `maxConnections`：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: nginx
spec:
  host: nginx
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 1
```

但测试当并发超过这里定义的最大连接数时，并没有触发熔断，只是 QPS 很低。通常是因为没有配置 `http1MaxPendingRequests`，不配置默认为 `2^32-1`，非常大，表示如果超过最大连接数，请求就先等待(不直接返回503)，当连接数低于最大值时再继续转发。

如果希望连接达到上限或超过上限一定量后或直接熔断(响应503)，那么就需要显式指定一下 `http1MaxPendingRequests`：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: nginx
spec:
  host: nginx
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 1
      http:
        http1MaxPendingRequests: 1
```
