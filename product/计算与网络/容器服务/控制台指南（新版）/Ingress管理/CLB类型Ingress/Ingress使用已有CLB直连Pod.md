腾讯云容器服务 TKE 具备通过 `kubernetes.io/ingress.existLbId: <LoadBalanceId>` 注解使用已有负载均衡的功能，您可使用该注解指定 Ingress 关联的负载均衡实例。
>? Ingress 与 Service 的区别：Ingress 不支持多个实例使用同一个负载均衡实例，即不支持复用功能。

## 注意事项
- 请确保您的容器业务不与云服务器 CVM 业务共用一个负载均衡资源。
- 不支持在负载均衡控制台操作 `Ingress Controller` 管理的负载均衡监听器以及后端绑定的服务器，更改会被 `Ingress Controller` 自动覆盖。
- 使用已有负载均衡时：
  - 不支持多个 Ingress 复用同一个负载均衡。
  - 指定的负载均衡不能存在任何已有监听器。如已存在，请提前删除。
  - 仅支持使用通过负载均衡控制台创建的负载均衡器，不支持使用由 `Service Controller` 自动创建和管理的负载均衡，即 Service 和 Ingress 不能混用同一个负载均衡。
  - `Ingress Controller` 不负责负载均衡的资源管理，即在 Ingress 资源删除时，负载均衡资源不会被删除回收。

## 使用场景示例

### 使用包年包月的负载均衡对外提供服务
`Ingress Controller` 管理负载均衡生命周期时，仅支持购买按量计费的资源。但由于包年包月的负载均衡在价格上有一定的优势，用户需要长时间使用负载均衡时，通常会优先选择购买包年包月负载均衡。

在此类场景下，用户就可以独立购买和管理负载均衡。通过注解控制 Ingress 使用已有负载均衡，将负载均衡的生命周期管理从 `Ingress Controller` 中剥离。示例如下：
```Yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.existLbId: lb-mgzu3mpx
  name: nginx-ingress
spec:
  rules:
    - http:
        paths:
          - backend:
              serviceName: nginx-service
              servicePort: 80
            path: /
```
>? `kubernetes.io/ingress.existLbId: lb-mgzu3mpx` 注解表明了该 Ingress 将使用已有负载均衡 `lb-mgzu3mpx` 进行 Ingress 服务配置。
