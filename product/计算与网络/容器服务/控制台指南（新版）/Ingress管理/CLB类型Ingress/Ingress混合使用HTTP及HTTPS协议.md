## 混合规则
默认场景下，当 Ingress 中不配置 TLS 时，服务将以 HTTP 协议的方式对外暴露。当 Ingress 配置 TLS 时，服务将以 HTTPS 协议的方式对外暴露。Ingress 描述的服务只能以其中一种协议暴露服务，基于此规则的局限性，腾讯云容器服务 TKE 提供了混合协议的支持。

用户需要同时暴露 HTTP 及 HTTPS 服务时，只需参考本文，开启混合协议并配置所有的转发规则到 `kubernetes.io/ingress.http-rules` 及 `kubernetes.io/ingress.https-rules` 注解中即可。

## 规则格式
`kubernetes.io/ingress.http-rules` 及 `kubernetes.io/ingress.https-rules` 的规则格式是一个 `Json Array`。每个对象的格式如下：
```
{
  "host": "<domain>",
  "path": "<path>",
  "backend": {
    "serviceName": "<service name>",
    "servicePort": "<service port>"
  }
}
```

## 混合规则配置步骤
`TKE Ingress Controller` 支持混合配置 `HTTP` 及 `HTTPS` 规则，步骤如下：

1. **开启混合规则**    
    在 Ingress 中添加注解 `kubernetes.io/ingress.rule-mix`，并设置为 true。
2. **规则匹配**     
将 Ingress 中的每条转发规则与 `kubernetes.io/ingress.http-rules` 及 `kubernetes.io/ingress.https-rules` 进行匹配，并添加到对应规则集中。若 Ingress 注解中的未找到对应规则，则默认添加到 HTTPS 规则集中。
3. **校验匹配项**    
  匹配时请注意校验 Host、Path、ServiceName 及 ServicePort，其中 Host 默认为 `VIP`、Path 默认为 `/`。
> !  [IPv6](https://cloud.tencent.com/document/product/1142/38134) 的负载均衡没有 IPv4 地址，不具备提供默认域名的功能。

## 示例

### Ingress 示例：sample-ingress.yaml
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.http-rules: '[{"host":"www.tencent.com","path":"/","backend":{"serviceName":"sample-service","servicePort":"80"}}]'
    kubernetes.io/ingress.https-rules: '[{"host":"www.tencent.com","path":"/","backend":{"serviceName":"sample-service","servicePort":"80"}}]'
    kubernetes.io/ingress.rule-mix: "true"
  name: sample-ingress
  namespace: default
spec:
  rules:
  - host: www.tencent.com
    http:
      paths:
      - backend:
          serviceName: sample-service
          servicePort: 80
        path: /
  tls:
  - secretName: tencent-com-cert
```
该示例包含以下配置：
- 描述了默认证书，证书 ID 应该存在于名为 `tencent-com-cert` 的 Secret 资源中。
- 开启了混合协议，并在 `kubernetes.io/ingress.http-rules` 及 `kubernetes.io/ingress.https-rules` 中都描述了 `ingress.spec.rule` 中描述的转发规则。
3. 此时负载均衡会同时在 HTTP、HTTPS 中配置转发规则对外暴露服务。
