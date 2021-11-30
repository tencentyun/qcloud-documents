Istio 为 Envoy 设置了缺省的重试策略，会在 connect-failure,refused-stream, unavailable, cancelled, retriable-status-codes 等情况下缺省重试两次。出现错误时，可能已经触发了服务器逻辑，在操作不是幂等（任意多次执行所产生的影响均与一次执行的影响相同）的情况下，可能会导致错误。

## 解决方案

可以通过配置 VS 关闭重试：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: ratings
spec:
  hosts:
  - ratings
  http:
  - retries:
      attempts: 0
```

