授权策略用于配置网格、namespace、服务/Workload 范围的访问管理规则。您可以通过 AuthorizationPolicy CRD 配置授权规则。AuthorizationPolicy 主要包含以下部分：

- selector：指定策略的生效范围。
- action：指定该策略是 `ALLOW` 策略还是 `DENY` 策略。
- rules：授权规则主体，由 from，to，where 3 部分构成。
	- from：指定请求的来源特征。
	- to：指定请求的操作特征。
	- when：指定授权规则的生效条件。

当有 AuthorizationPolicy 的 `ALLOW` 和 `DENY` 策略应用于同一范围时，`DNEY` 策略的优先级高于 `ALLOW` 策略，生效的规则如下：

1. 如请求匹配任何一条 `DENY` 策略，则拒绝该请求的访问。
2. 如该范围没有任何 `ALLOW` 策略，则允许该请求的访问。
3. 如当前该范围存在 `ALLOW` 策略，且请求匹配到了任何一条 `ALLOW` 策略，则允许该请求的访问。
4. 拒绝该请求的访问。
![](https://main.qcloudimg.com/raw/f513040eef15fbff345791a89cb406a2.png)

以下是两种特殊 AuthorizationPolicy 示例：
- default namespace 的服务允许所有请求访问：
```
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-all
  namespace: default
spec:
  action: ALLOW
  rules:
  - {} # 规则可以匹配任何请求
```

- default namespace 的服务拒绝所有请求访问：
```
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: deny-all
  namespace: default
spec:
  {} # action 字段没有填写时默认是 ALLOW，此时请求无法匹配任何规则
```


## AuthorizationPolicy 重要字段说明

以下是 AuthorizationPolicy 重要字段说明：

| 字段名称 | 字段类型 | 字段说明 |
| ----- | ---- | ----- |
| `metadata.name` | `string` | AuthorizationPolicy 名称 | 
| `metadata.namespace` | `string` | AuthorizationPolicy 命名空间 | 
| `spec.selector` | `map<string, string>` | AuthorizationPolicy 使用填写的标签键值对，配合填写的 namespace，匹配配置下发的 Workload 范围：<li>namespace 填写 istio-system，且 selector 字段不填写时，该策略生效范围为整个网格<li>namespace 填写非 istio-system 的 namespace，且 selector 字段不填写时，策略生效范围为填写的 namespace<li>namespace 填写非 istio-system 的 namespace，且 selector 字段填写了有效键值对时，策略的生效范围为在所填 namespace 下根据 selector 匹配到的 Workload |
| `spec.action` | - |指定该策略是 `ALLOW` 策略还是 `DENY` 策略 |
| `spec.rules.from.source.principals` | `string[]` | 源对等身份列表（即 service account），匹配 `source.principal` 字段 ，要求启用 mTLS，未填写时则允许任何 principal |
| `spec.rules.from.source.requestPrincipals` | `string[]` | 请求身份列表（即 iss/sub claim），匹配 `request.auth.principal` 字段，未填写时则允许任何 requestPrincipals |
| `spec.rules.from.source.namespaces` | `string[]` | 请求源的 namespace 列表，匹配 `source.namespace` 字段，要求启用 mTLS，未填写时允许来自任何 namespace 的请求 |
| `spec.rules.from.source.ipBlocks` | `string[]` | IP block 列表，匹配 `source.ip` 字段，支持单 IP 写法（如 `1.2.3.4`）或 CIDR 写法（如 `1.2.3.4/24`），未填写时允许任何源 IP 的访问 |
| `spec.rules.to.operation.hosts` | `string[]` | 请求的域名列表，匹配 `request.host` 字段，未填写时允许任何域名，仅支持在 HTTP 协议请求中使用 |
| `spec.rules.to.operation.ports` | `string[]` | 请求的端口列表，匹配 `destination.port` 字段，未填写时允许任何端口 |
| `spec.rules.to.operation.methods` | `string[]` | 请求的方法列表，匹配 `request.method` 字段，使用 gRPC 协议时该值始终应为 `POST`。未填写时允许任何方法 ，仅支持在 HTTP 协议请求中使用 |
| `spec.rules.to.operation.paths` | `string[]` | 请求的路径，匹配 `request.url_path` 字段，未填写时允许任何路径，仅支持在 HTTP 协议请求中使用 |
| `spec.rules.when.condition.key` | `string` | Istio 支持的条件字段名称，详见 [Authorization Policy Conditions](https://istio.io/latest/docs/reference/config/security/conditions/) |
| `spec.rules.when.condition.values` | `string[]` | 填写对应条件的值列表 |

## 使用 AuthorizationPolicy 配置 namespace 的访问权限

为查看配置的 AuthorizationPolicy 策略效果，我们首先部署一套测试程序到网格管理的集群，部署完成后位于 test namespace 的 client 服务会自动发起对 base namespace user 服务的访问：

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: test
  labels:
    istio.io/rev: 1-6-9 # sidecar 自动注入（istio 1.6.9）
spec:
  finalizers:
    - kubernetes
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: client
  namespace: test
  labels:
    app: client
spec:
  replicas: 10
  selector:
    matchLabels:
      app: client
  template:
    metadata:
      labels:
        app: client
    spec:
      containers:
        - name: client
          image: ccr.ccs.tencentyun.com/zhulei/testclient:v1
          imagePullPolicy: Always
          env:
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: REGION
              value: "guangzhou-zoneA"
          ports:
            - containerPort: 7000
              protocol: TCP
---

apiVersion: v1
kind: Service
metadata:
  name: client
  namespace: test
  labels:
    app: client
spec:
  ports:
    - name: http
      port: 7000
      protocol: TCP
  selector:
    app: client
  type: ClusterIP
---
apiVersion: v1
kind: Namespace
metadata:
  name: base
  labels:
    istio.io/rev: 1-6-9
spec:
  finalizers:
    - kubernetes
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user
  namespace: base
  labels:
    app: user
spec:
  replicas: 1
  selector:
    matchLabels:
      app: user
  template:
    metadata:
      labels:
        app: user
    spec:
      containers:
        - name: user
          image: ccr.ccs.tencentyun.com/zhulei/testuser:v1
          imagePullPolicy: Always
          env:
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: REGION
              value: "guangzhou-zoneB"
          ports:
            - containerPort: 7000
---

apiVersion: v1
kind: Service
metadata:
  name: user
  namespace: base
  labels:
    app: user
spec:
  ports:
    - port: 7000
      name: http
  selector:
    app: user
```

查看 client 容器的日志，会发现访问成功，正确返回了 user 信息：

![](https://main.qcloudimg.com/raw/031025872eb71ef8a925977c655586ef.jpg)

接下来将配置 Authorization 策略，不允许 base namespace 的服务被 test namespace 的服务访问（需要开启 mTLS）。


<dx-tabs>
::: YAML 配置示例
```
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: base-authz
  namespace: base
spec:
  action: DENY
  rules:
    - from:
        - source:
            namespaces:
              - test
```
:::
::: 控制台配置示例
![](https://main.qcloudimg.com/raw/ab0cacaa38cdb23a784f37c5b25d4d59.png)
:::
</dx-tabs>




配置完成后再次查看 client 的容器日志，发现所有访问均失败，没有返回 user 信息，AuthorizationPolicy 生效。

![](https://main.qcloudimg.com/raw/47aa447543f546d5aff80a95c10575dc.png)


## 使用 AuthorizationPolicy 配置 Ingress Gateway 的 IP 黑白名单

您可以使用 AuthorizationPolicy 为边缘代理网关 Ingress Gateway 配置 IP 黑/白名单。

为验证黑白名单的配置效果，您首先需要部署一个测试程序 `httpbin.foo`，并配置通过 Ingress Gateway 暴露此服务到公网：

- 创建 foo namespace，开启 sidecar 自动注入，部署 httpbin 服务到 foo namespace：
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: foo
  labels:
    istio.io/rev: 1-6-9 # 开启 namespace 的 sidecar 自动注入（istio 版本 1.6.9）
spec:
  finalizers:
    - kubernetes
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: httpbin
  namespace: foo
---
apiVersion: v1
kind: Service
metadata:
  name: httpbin
  namespace: foo
  labels:
    app: httpbin
    service: httpbin
spec:
  ports:
  - name: http
    port: 8000
    targetPort: 80
  selector:
    app: httpbin
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: httpbin
  namespace: foo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: httpbin
      version: v1
  template:
    metadata:
      labels:
        app: httpbin
        version: v1
    spec:
      serviceAccountName: httpbin
      containers:
      - image: docker.io/kennethreitz/httpbin
        imagePullPolicy: IfNotPresent
        name: httpbin
        ports:
        - containerPort: 80
```
- 配置通过 Ingress Gateway 暴露 httpbin 服务至公网访问：
```
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: httpbin-gateway
  namespace: foo
spec:
  selector:
    app: istio-ingressgateway
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "*"
---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: httpbin
  namespace: foo
spec:
  hosts:
  - "*"
  gateways:
  - httpbin-gateway
  http:
  - route:
    - destination:
        port:
          number: 8000
        host: httpbin.foo.svc.cluster.local
```

- 通过 curl 语句 `curl "$INGRESS_IP:80/headers" -s -o /dev/null -w "%{http_code}\n"` 测试服务的连通性，注意您需要将代码中的 `$INGRESS_IP` 替换为您的边缘代理网关 IP 地址，正常情况下会返回 `200` 返回码。
- 为使 Ingress Gateway 能正确获取真实客户端源 IP，我们需要修改 Ingress Gateway Service 的 ExternalTrafficPolicy 为 Local，保证流量仅在本节点转发不做 SNAT。
![](https://main.qcloudimg.com/raw/b4c8372cfdf171074df87e76370b7f7d.png)


下面将会使用 AuthorizationPolicy 把本机的 IP 地址列入 Ingress Gateway 的黑名单，并验证黑名单是否生效。


<dx-tabs>
::: YAML 配置示例
```
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: black-list
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
      istio: ingressgateway
  rules:
    - from:
        - source:
            ipBlocks:
              - $您的本机 IP 地址
  action: DENY
```
:::
::: 控制台配置示例
![](https://main.qcloudimg.com/raw/aaec6a1f51df3706f17593ff6976a222.png)
:::
</dx-tabs>




配置完成后再次通过 curl 语句 `curl "$INGRESS_IP:80/headers" -s -o /dev/null -w "%{http_code}\n"` 测试服务的连通性，注意您需要将代码中的 `$INGRESS_IP` 替换为您的边缘代理网关 IP 地址，此时访问失败，返回 `403` 返回码，黑名单策略生效。
