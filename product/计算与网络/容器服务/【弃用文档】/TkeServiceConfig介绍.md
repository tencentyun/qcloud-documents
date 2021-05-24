## 简介

TkeServiceConfig 可为 Service 及 Ingress 提供扩展式的资源配置，其设计紧贴负载均衡（CLB）能力，以确保 CLB 可扩展性。因此，您可以通过 TkeServiceConfig 更友好的配置 CLB 参数。

## TkeServiceConfig 功能

```yaml
apiVersion: cloud.tencent.com/v1alpha1
kind: TkeServiceConfig
metadata:
  name: sample
  namespace: default
spec:
  loadBalancer:
    l4Listeners: # 四层规则配置，适用于Service的监听器配置。
    - protocol: TCP # 协议端口锚定Service的四层规则。必填，枚举值：TCP|UDP。
      port: 80 # 必填，可选值：1~65535。
      session: # 会话保持相关配置。选填
        enabled: ture # 是否开启会话保持。必填，布尔值
        sessionExpireTime: 100 # 会话保持的时间。选填，默认值：30，可选值：30~3600，单位：秒。
      healthCheck: # 健康检查相关配置。选填
        enabled: true # 是否开启会话保持。必填，布尔值
        intervalTime: 10 # 健康检查探测间隔时间。选填，默认值：5，可选值：5~300，单位：秒。
        healthNum: 2 # 健康阈值，表示当连续探测几次健康则表示该转发正常。选填，默认值：3，可选值：2~10，单位：次。
        unHealthNum: 3 # 不健康阈值，表示当连续探测几次健康则表示该转发异常。选填，默认值：3，可选值：2~10，单位：次。
        timeout: 10 # 健康检查的响应超时时间，响应超时时间要小于检查间隔时间。选填，默认值：2，可选值：2~60，单位：秒。
        checkPort: 8080 # 自定义探测相关参数。健康检查端口，默认为后端服务的端口，除非您希望指定特定端口，否则建议留空。选填，可选值：1~65535。暂未加入一期计划。
        checkType: CUSTOM # 自定义探测相关参数。健康检查使用的协议：TCP | HTTP | CUSTOM（仅适用于TCP/UDP监听器，其中UDP监听器只支持CUSTOM；如果使用自定义健康检查功能，则必传）。暂未加入一期计划。
        contextType: TEXT # 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查的输入格式，可取值：HEX或TEXT；取值为HEX时，SendContext和RecvContext的字符只能在0123456789ABCDEF中选取且长度必须是偶数位。暂未加入一期计划。
        sendContext: "ping" # 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查发送的请求内容，只允许ASCII可见字符，最大长度限制500。暂未加入一期计划。
        recvContext: "ok" # 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查返回的结果，只允许ASCII可见字符，最大长度限制500。暂未加入一期计划。
        httpVersion: "HTTP/1.1" # 自定义探测相关参数。健康检查协议CheckType的值取HTTP时，必传此字段，代表后端服务的HTTP版本：HTTP/1.0、HTTP/1.1。（仅适用于TCP监听器）。暂未加入一期计划。
      scheduler: WRR # 请求转发方式配置。WRR、LEAST_CONN、IP_HASH分别表示按权重轮询、最小连接数、按IP哈希。选填，枚举值：WRR|LEAST_CONN。
    l7Listeners: # 七层规则配置，试用于Ingress的监听器配置。
    - protocol: HTTPS # 协议端口锚定Ingress的七层监听器。必填，枚举值：HTTP|HTTPS。
      port: 443 # 必填，可选值：1~65535。
      sniSwitch: true # 是否开启SNI功能。因目前功能无法关闭，暂未加入一期计划。选填，布尔值。
      defaultDomain: # 域名级别的默认配置，暂未加入一期计划（字段含义参考l7Listeners）。选填
        defaultRule:
          session:
            enabled: ture
            sessionExpireTime: 100
          healthCheck:
            enabled: true
            intervalTime: 10
            healthNum: 2
            unHealthNum: 3
            httpCode: 31
            httpCheckPath: "/"
            httpCheckDomain: ""
            httpCheckMethod: GET
          scheduler: WRR
      domains: # 协议端口域名锚定Ingress的七层监听器域名。
      - domain: "" # 七层监听器域名匹配Ingress中对应域名。域名为空时默认为负载均衡的IPv4地址。必填
        certificate: # SNI功能配置，配置域名对应的证书。因目前功能无法关闭，暂未加入一期计划。选填。
          sslMode: UNIDIRECTIONAL # 认证类型，UNIDIRECTIONAL：单向认证，MUTUAL：双向认证。必填，枚举值：UNIDIRECTIONAL|MUTUAL。
          certId: id-123 # 服务端证书的ID。必填。
          certCaId: id-345 # 客户端证书的 ID，当监听器采用双向认证，即 SSLMode=MUTUAL 时必填。选填。
        ruleDefault: # 规则级别的默认配置，暂未加入一期计划（字段含义参考l7Listeners）。选填
          session:
            enabled: ture
            sessionExpireTime: 100
          healthCheck:
            enabled: true
            intervalTime: 10
            healthNum: 2
            unHealthNum: 3
            httpCode: 31
            httpCheckPath: "/"
            httpCheckDomain: ""
            httpCheckMethod: GET
          scheduler: WRR
        rules: # 协议端口域名路径锚定Ingress的七层监听器转发规则。
        - url: "/" # 协议端口域名路径锚定Ingress的七层监听器转发规则。
          session: # 会话保持相关配置。选填
            enabled: ture # 是否开启会话保持。必填，布尔值
            sessionExpireTime: 100 # 会话保持的时间。选填，默认值：30，可选值：30~3600，单位：秒。
          healthCheck: # 健康检查相关配置。选填
            enabled: true # 是否开启会话保持。必填，布尔值
            intervalTime: 10 # 健康检查探测间隔时间。选填，默认值：5，可选值：5~300，单位：秒。
            healthNum: 2 # 健康阈值，表示当连续探测几次健康则表示该转发正常。选填，默认值：3，可选值：2~10，单位：次。
            unHealthNum: 3 # 不健康阈值，表示当连续探测几次健康则表示该转发异常。选填，默认值：3，可选值：2~10，单位：次。
            httpCode: 31 # 健康检查状态码。选填，默认值：31，可选值：1~31。1 表示探测后返回值 1xx 代表健康，2 表示返回 2xx 代表健康，4 表示返回 3xx 代表健康，8 表示返回 4xx 代表健康，16 表示返回 5xx 代表健康。若希望多种返回码都可代表健康，则将相应的值相加。
            httpCheckPath: "/" # 健康检查路径。选填。长度范围：1~200
            httpCheckDomain: "" # 健康检查域名。选填。长度范围：1~80
            httpCheckMethod: GET # 健康检查方法。选填。默认值：HEAD，可选值：HEAD|GET。
          scheduler: WRR # 请求转发方式配置。WRR、LEAST_CONN、IP_HASH分别表示按权重轮询、最小连接数、按IP哈希。选填，枚举值：WRR|LEAST_CONN|IP_HASH。
    internetMaxBandwidthOut: 100 # 最大出带宽，仅对公网属性的LB生效。选填，可选值：0~2048，单位Mbps。
```

## Service 配置示例

### Service
```yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.cloud.tencent.com/tke-service-config: jetty-service-config
  name: jetty-service
  namespace: default
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  - port: 443
    protocol: TCP
    targetPort: 443
  selector:
    app: jetty
  type: LoadBalancer
```

### TkeServiceConfig
```yaml
apiVersion: cloud.tencent.com/v1alpha1
kind: TkeServiceConfig
metadata:
  name: jetty-service-config
  namespace: default
spec:
  loadBalancer:
    l4Listeners:
    - protocol: TCP
      port: 80
      healthCheck:
        enabled: false
    - protocol: TCP
      port: 443
      session:
        enabled: ture
        sessionExpireTime: 3600
      healthCheck:
        enabled: true
        intervalTime: 10
        healthNum: 2
        unHealthNum: 2
        timeout: 5
      scheduler: LEAST_CONN
```

## Ingress 配置示例

### Ingress
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: qcloud
    kubernetes.io/ingress.qcloud-loadbalance-id: lb-lts4lvtw
    kubernetes.io/ingress.rule-mix: "true"
    kubernetes.io/ingress.http-rules: '[{"path":"/","backend":{"serviceName":"jetty-service","servicePort":"80"}}]'
    kubernetes.io/ingress.https-rules: '[{"path":"/","backend":{"serviceName":"jetty-service","servicePort":"443","host":"sample.tencent.com"}}]'
    ingress.cloud.tencent.com/tke-service-config: jetty-ingress-config
  name: jetty-ingress
  namespace: default
spec:
  rules:
  - http:
      paths:
      - backend:
          serviceName: jetty-service
          servicePort: 80
        path: /
  - host: "sample.tencent.com"
    http:
      paths:
      - backend:
          serviceName: jetty-service
          servicePort: 443
        path: /
        
  tls:
  - secretName: jetty-cert-secret
```

### TkeServiceConfig
```yaml
apiVersion: cloud.tencent.com/v1alpha1
kind: TkeServiceConfig
metadata:
  name: jetty-ingress-config
  namespace: default
spec:
  loadBalancer:
    l7Listeners:
    - protocol: HTTP
      port: 80
      domains:
      - domain: ""
        rules:
        - url: "/"
          healthCheck:
            enabled: false
    - protocol: HTTPS
      port: 443
      domains:
      - domain: "sample.tencent.com"
        rules:
        - url: "/"
          session:
            enabled: ture
            sessionExpireTime: 3600
          healthCheck:
            enabled: true
            intervalTime: 10
            healthNum: 2
            unHealthNum: 2
            httpCode: 2
            httpCheckPath: "/checkHealth"
            httpCheckDomain: "sample.tencent.com"
            httpCheckMethod: HEAD
          scheduler: IP_HASH
```




