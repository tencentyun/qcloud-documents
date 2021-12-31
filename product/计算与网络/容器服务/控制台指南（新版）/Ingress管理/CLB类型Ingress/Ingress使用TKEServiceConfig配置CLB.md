## TkeServiceConfig
TkeServiceConfig 是腾讯云容器服务 TKE 提供的自定义资源 CRD，通过 TkeServiceConfig 能够帮助您更灵活的进行 Ingress 管理负载均衡的各种配置。

### 使用场景
Ingress YAML 的语义无法定义的负载均衡参数和功能，可以通过 TkeServiceConfig 来配置。

### 配置说明
使用 TkeServiceConfig 能够帮您快速进行负载均衡器的配置。通过 Ingress 注解 **ingress.cloud.tencent.com/tke-service-config:&lt;config-name&gt;**，您可以指定目标配置应用到 Ingress 中。
>! TkeServiceConfig 资源需要和 Ingress 处于同一命名空间。

TkeServiceConfig 不会帮您配置并修改协议、端口、域名以及转发路径，您需要在配置中描述协议、端口、域名还有转发路径以便指定配置下发的转发规则。

每个七层的监听器下可有多个域名，每个域名下可有多个转发路径。因此，在一个 `TkeServiceConfig` 中可以声明多组域名、转发规则配置，目前主要针对负载均衡的健康检查以及对后端访问提供配置。
- 通过指定协议和端口，配置能够被准确地下发到对应监听器：
 - `spec.loadBalancer.l7Listeners.protocol`：七层协议
 - `spec.loadBalancer.l7Listeners.port`：监听端口
- 通过指定协议、端口、域名以及访问路径，可以配置转发规则级别的配置。例如，后端健康检查、负载均衡方式。
 - `spec.loadBalancer.l7Listeners.protocol`：七层协议
 - `spec.loadBalancer.l7Listeners.port`：监听端口
 - `spec.loadBalancer.l7Listeners.domains[].domain`：域名
 - `spec.loadBalancer.l7Listeners.domains[].rules[].url`：转发路径
 - `spec.loadBalancer.l7listeners.protocol.domain.rules.url.forwardType`: 指定后端协议
    - 后端协议是指 CLB 与后端服务之间的协议：后端协议选择 HTTP 时，后端服务需部署 HTTP 服务。后端协议选中 HTTPS 时，后端服务需部署 HTTPS 服务，HTTPS 服务的加解密会让后端服务消耗更多资源。更多请查看 [CLB 配置 HTTPS 监听器](https://cloud.tencent.com/document/product/214/36385)

>?当您的域名配置为默认值，即公网或内网 VIP 时，可以通过 domain 填空值的方式进行配置。


## Ingress 与 TkeServiceConfig 关联行为
1. 创建 Ingress 时，设置 **ingress.cloud.tencent.com/tke-service-config-auto:&lt;true&gt;** ，将自动创建 &lt;IngressName>-auto-ingress-config。 您也可以通过 **ingress.cloud.tencent.com/tke-service-config:&lt;config-name&gt;** 直接指定您自行创建的 TkeServiceConfig。两个注解不可同时使用。 
2. 您为 Service\Ingress 使用的自定义配置，名称不能以 `-auto-service-config` 与 `-auto-ingress-config` 为后缀。
3. 其中自动创建的 TkeServiceConfig 存在以下同步行为：
  - 更新 Ingress 资源时，新增若干7层转发规则，如果该转发规则没有对应的 TkeServiceConfig 配置片段。Ingress-Controller 将主动添加 TkeServiceConfig 对应片段。
  - 删除若干7层转发规则时，Ingress-Controller 组件将主动删除 TkeServiceConfig 对应片段。
  - 删除 Ingress 资源时，联级删除该 TkeServiceConfig。
  - 用户修改 Ingress 默认的 TkeServiceConfig，TkeServiceConfig 内容同样会被应用到负载均衡。
4. 您也可以参考下列 TkeServiceConfig 完整配置参考，自行创建需要的 CLB 配置，Service 通过注解 **ingress.cloud.tencent.com/tke-service-config:&lt;config-name&gt;** 引用该配置。
5. 其中您手动创建的 TkeServiceConfig 存在以下同步行为：
  - 当用户在 Ingress 中使用配置注解时，负载均衡将会即刻进行设置同步。
  - 当用户在 Ingress 中删除配置注解时，负载均衡将会保持不变。
  - 修改 TkeServiceConfig 配置时，引用该配置的 Ingress 的负载均衡将会根据新的 TkeServiceConfig 进行设置同步。
  - 当 Ingress 的监听器没有找到对应配置时，该监听器将不会进行修改。
  - Ingress 的监听器找到对应配置时，若配置中没有声明的属性，该监听器将不会进行修改。

## 示例

### Deployment 示例：jetty-deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: jetty
  name: jetty-deployment
  namespace: default
spec:
  progressDeadlineSeconds: 600
  replicas: 3
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      app: jetty
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: jetty
    spec:
      containers:
      - image: jetty:9.4.27-jre11
        imagePullPolicy: IfNotPresent
        name: jetty
        ports:
        - containerPort: 80
          protocol: TCP
        - containerPort: 443
          protocol: TCP
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
```

### Service 示例：jetty-service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: jetty-service
  namespace: default
spec:
  ports:
  - name: tcp-80-80
    port: 80
    protocol: TCP
    targetPort: 80
  - name: tcp-443-443
    port: 443
    protocol: TCP
    targetPort: 443
  selector:
    app: jetty
  type: NodePort
```
该示例包含以下配置：
Service 的 NodePort 类型，声明了两个 TCP 服务。一个在80端口，一个在443端口。

### Ingress：jetty-ingress.yaml
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.rule-mix: "true"
    kubernetes.io/ingress.http-rules: '[{"path":"/health","backend":{"serviceName":"jetty-service","servicePort":"80"}}]'
    kubernetes.io/ingress.https-rules: '[{"path":"/","backend":{"serviceName":"jetty-service","servicePort":"443","host":"sample.tencent.com"}}]'
    ingress.cloud.tencent.com/tke-service-config: jetty-ingress-config
    # 指定已有的 tke-service-config
    # service.cloud.tencent.com/tke-service-config-auto: true 
    # 自动创建 tke-service-config
  name: jetty-ingress
  namespace: default
spec:
  rules:
  - http:
      paths:
      - backend:
          serviceName: jetty-service
          servicePort: 80
        path: /health
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
该示例包含以下配置：
- 使用了混合协议，使用默认域名（公网 IP）暴露了一个 HTTP 服务，使用 `sample.tencent.com` 域名暴露了一个 HTTPS 服务。<!-- 详情请参见 [Ingress 混合使用 HTTP 及 HTTPS 协议]()。-->
- HTTP 服务的转发路径是 `/health`，HTTPS 服务的转发路径是`/`。
- 使用了 `jetty-ingress-config` 负载均衡配置。

### TkeServiceConfig 示例：jetty-ingress-config.yaml
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
      - domain: ""     # domain为空表示使用VIP作为域名
        rules:
        - url: "/health"
          forwardType: HTTP # 指定后端协议为 HTTP
          healthCheck:
            enable: false
    - protocol: HTTPS
      port: 443
      domains:
      - domain: "sample.tencent.com"
        rules:
        - url: "/"
          forwardType: HTTPS # 指定后端协议为 HTTPS
          session:
            enable: true
            sessionExpireTime: 3600
          healthCheck:
            enable: true
            intervalTime: 10
            healthNum: 2
            unHealthNum: 2
            httpCheckPath: "/checkHealth"
            httpCheckDomain: "sample.tencent.com" #注意：健康检查必须使用固定域名进行探测，如果您在.spec.loadBalancer.l7Listeners.protocol.domains.domain 里填写的是泛域名，一定要使用 httpCheckDomain 字段明确具体需要健康检查的域名，否则泛域名不支持健康检查。
            httpCheckMethod: HEAD
          scheduler: WRR
```
该示例包含以下配置：
该 TkeServiceConfig 名称为 `jetty-ingress-config`。且在七层监听器配置中，声明了两段配置：
1. 80端口的 HTTP 监听器将会被配置，其中包含域名配置，是默认域名对应负载均衡的 VIP。
 `/health` 路径下的健康检查被关闭了。
2. 443端口的 HTTPS 监听器将会被配置。其中包含域名配置，域名是 `sample.tencent.com`。该域名下仅描述了一个转发路径为`/`的转发规则配置，其中配置包含以下内容：
 - 打开健康检查，健康检查间隔调整为10s，健康阈值2次，不健康阈值2次。通过 HEAD 请求进行健康检查，检查路径为 `/checkHealth`，检查域名为 `sample.tencent.com`。
 - 打开会话保持功能，会话保持的超时时间设置为3600s。
 - 转发策略配置为：按权重轮询。

### kubectl 配置命令
```
➜ kubectl apply -f jetty-deployment.yaml
➜ kubectl apply -f jetty-service.yaml
➜ kubectl apply -f jetty-ingress.yaml
➜ kubectl apply -f jetty-ingress-config.yaml

➜ kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
jetty-deployment-8694c44b4c-cxscn   1/1     Running   0          8m8s
jetty-deployment-8694c44b4c-mk285   1/1     Running   0          8m8s
jetty-deployment-8694c44b4c-rjrtm   1/1     Running   0          8m8s

# 获取TkeServiceConfig配置列表
➜ kubectl get tkeserviceconfigs.cloud.tencent.com
NAME                   AGE
jetty-ingress-config   52s

# 更新修改TkeServiceConfig配置
➜ kubectl edit tkeserviceconfigs.cloud.tencent.com jetty-ingress-config
tkeserviceconfigs.cloud.tencent.com/jetty-ingress-config edited
```
