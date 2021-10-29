认证策略包含 PeerAuthentication 和 RequestAuthentication。其中，PeerAuthentication 策略用于配置服务通信的 mTLS 模式，RequestAuthentication 策略用于配置服务的请求身份验证方法。

## PeerAuthentication 配置字段说明

以下是 PeerAuthentication 重要字段说明：

| 字段名称 | 字段类型 | 字段说明 |
| ----- | ---- | ----- |
| `metadata.name` | `string` | PeerAuthentication 名称 | 
| `metadata.namespace` | `string` | PeerAuthentication 命名空间 | 
| `spec.selector` | `map<string, string>` | PeerAuthentication 使用填写的标签键值对，配合填写的 namespace，匹配配置下发的 Workload 范围：<li>namespace 填写 istio-system，且 selector 字段不填写时，该策略生效范围为整个网格<li>namespace 填写非 istio-system 的 namespace，且 selector 字段不填写时，策略生效范围为填写的 namespace<li>namespace 填写非 istio-system 的 namespace，且 selector 字段填写了有效键值对时，策略的生效范围为在所填 namespace 下根据 selector 匹配到的Workload |
| `spec.mtls.mode` | - | 配置 mTLS 的模式，支持：`UNSET|DISABLE|PERMISSIVE|STRICT` 四种模式：<li>UNSET 模式为继承父范围的 mTLS 模式（如有），否则视为 PERMISSIVE 模式<li>DISABLE 模式为明文连接，不使用 mTLS 加密（不推荐使用），同时需要配置相同应用范围的 DestinationRule TLS 模式为 DISABLE 使用<li>PERMISSIVE 模式连接可以是明文或密文，业务改造过程中推荐使用此模式<li>STRICT 模式下连接必须使用 mTLS 加密。 |
| `spec.portLevelMtls` | `map<uint32, mTLS mode>` | 设置端口级别的 mTLS 模式 |



>?mTLS 模式配置，不同选择范围的生效效力为：端口 > 服务/Workload > namespace > 网格。

## 使用 PeerAuthentication 配置网格内服务通信 mTLS 模式

服务网格默认网格内 mTLS 模式为 PERMISSIVE，即服务间的通信既可以使用 mTLS 加密，也可以使用 plaintext 明文连接。

为测试 mTLS 模式配置的效果，您可以首先对您网格内的服务发起明文请求，测试明文请求的连通性。以下是登录网格内 istio-proxy 容器对另外的服务发起明文请求的示例：

1. 在网格管理的 TKE 集群控制台，登录 istio-proxy 容器。
![](https://qcloudimg.tencent-cloud.cn/raw/3af9d26b785d0581e3d48b97691d08f4.png)
2. 输入命令 `curl http://product.base.svc.cluster.local:7000/product` 明文访问命名空间 base 下的 product 服务。
3. 查看明文访问结果，正确返回了 Product 信息，明文访问成功。
![](https://main.qcloudimg.com/raw/fd33ded000a3643314f21e4ee1ea5667.png)

下面我们将会配置 base namespace 的 mTLS 模式为 STRICT，并验证配置是否生效。

<dx-tabs>
::: YAML 配置示例
```
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: base-strict
  namespace: base
spec:
  mtls:
    mode: STRICT
```
:::
::: 控制台配置示例
![](https://main.qcloudimg.com/raw/548a16f867067d78346a7e441e677573.png)




:::
</dx-tabs>
配置完成后，重新以明文的方式访问 base 命名空间下的 product 服务，提示访问失败，mTLS STRICT 模式配置生效。

![](https://main.qcloudimg.com/raw/a7332a9e838cd6d4f10c6feec12b8ab6.png)






## RequestAuthentication 配置字段说明

以下是 RequestAuthentication 重要配置字段说明：

| 字段名称 | 字段类型 | 字段说明 |
| ----- | ---- | ----- |
| `metadata.name` | `string` | RequestAuthentication 名称 | 
| `metadata.namespace` | `string` | RequestAuthentication 命名空间 | 
| `spec.selector` | `map<string, string>` | RequestAuthentication 使用填写的标签键值对，配合填写的namespace，匹配配置下发的 Workload 范围，namespace 填写 istio-system，且 selector 字段不填写时，该策略生效范围为整个网格；namespace 填写非 istio-system 的 namespace，且 selector 字段不填写时，策略生效范围为填写的 namespace；namespace 填写非 istio-system 的 namespace，且 selector 字段填写了有效键值对时，策略的生效范围为在所填 namespace 下根据 selector 匹配到的Workload |
| `spec.jwtRules.issuer` | `string` | 配置 JWT token 的 issuer，详情参见 [iss claim](https://tools.ietf.org/html/rfc7519#section-4.1.1) |
| `spec.jwtRules.audiences` | `string[]` | 配置允许访问的 JWT [audience](https://tools.ietf.org/html/rfc7519#section-4.1.3) 列表。当 audience 列表为空时，使用 service name 则被允许访问 |
| `spec.jwtRules.jwksUri` | `string` | 配置验证 JWT 签名的公钥 URL，详情参见 [OpenID Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata)。同时配置 jwksUri 和 jwks 字段时，jwksUri 将被忽略 |
| `spec.jwtRules.jwks` | `string` | 验证 JWT 签名的 [JSON Web Key Set](https://auth0.com/docs/tokens/json-web-tokens/json-web-key-sets) 公钥。同时配置 jwksUri 和 jwks 字段时，jwksUri 将被忽略 |
| `spec.jwtRules.fromHeaders` | `map<string,string>[]` | 配置 JWT 从 header 中的提取位置列表 |
| `spec.jwtRules.fromParams` | `string[]` | 配置 JWT 从 header 中提取的 parameters，例如从 parameter mytoken（`/path?my_token=`）中提取 |
| `spec.jwtRules.outputPayloadToHeader ` | `string` | 配置成功验证的 JWT payload 输出的 header 名称，转发的数据为 `base64_encoded(jwt_payload_in_JSON)`。未填写时默认不会输出 JWT payload |
| `spec.jwtRules.forwardOriginalToken` | `bool` | 配置是否将原始 JWT 转发至 upstream。默认值为 `false` |

## 使用 RequestAuthentication 配置请求 JWT 认证

为验证请求 JWT 认证配置的效果，您首先需要部署一个测试程序 `httpbin.foo`，并配置通过 Ingress Gateway 暴露此服务到公网：

- 创建 foo namespace，开启 sidecar 自动注入，部署httpbin服务到foo namespace：
```
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

下面将会为边缘代理网关配置 JWT 认证规则，放通带有符合条件的 JWT 令牌的请求。



<dx-tabs>
::: YAML 配置示例
```
apiVersion: "security.istio.io/v1beta1"
kind: "RequestAuthentication"
metadata:
  name: "jwt-example"
  namespace: istio-system
spec:
  selector:
    matchLabels:
      istio: ingressgateway
      app: istio-ingressgateway
  jwtRules:
  - issuer: "testing@secure.istio.io"
    jwksUri: "https://raw.githubusercontent.com/istio/istio/release-1.9/security/tools/jwt/samples/jwks.json"
```

:::
::: 控制台配置示例
![](https://main.qcloudimg.com/raw/2267dee435e392c0c7d2007d46f0e0d9.png)

:::
</dx-tabs>



配置完成后，我们来验证配置的 JWT 验证规则是否生效。

- 通过以下代码，携带一个非法的 JWT 令牌发起访问，注意您需要将代码中的 `$INGRESS_IP` 替换为您的边缘代理网关 IP 地址。边缘代理网关不会放通携带非法 JWT 令牌的请求，因此会返回 `401` 返回码。

```
curl --header "Authorization: Bearer deadbeef" "$INGRESS_IP:80/headers" -s -o /dev/null -w "%{http_code}\n"
```

- 通过以下代码，携带一个合法的 JWT 令牌发起访问，注意您需要将代码中的 `$INGRESS_IP` 替换为您的边缘代理网关 IP 地址。边缘代理网关会放通携带合法 JWT 令牌的请求，因此会返回 `200` 返回码。

```
TOKEN=$(curl https://raw.githubusercontent.com/istio/istio/release-1.9/security/tools/jwt/samples/demo.jwt -s)
curl --header "Authorization: Bearer $TOKEN" "$INGRESS_IP:80/headers" -s -o /dev/null -w "%{http_code}\n"
```

通过验证，您可以发现您为边缘代理网关配置的请求 JWT 认证规则已经生效。但此时仅仅配置了 JWT 认证规则，Ingress Gateway 仍会放通未携带 JWT 令牌的请求。限制未携带 JWT 令牌的请求需要配置 AuthorizationPolicy。应用以下 YAML 文件至服务网格即可限制 Ingress Gateway 拒绝未携带 JWT 令牌的请求：

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: frontend-ingress
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
      istio: ingressgateway
  rules:
    - from:
        - source:
            notRequestPrincipals:
              - '*'
  action: DENY
```

再次用未携带 JWT 令牌的方式发起访问 `curl "$INGRESS_IP:80/headers" -s -o /dev/null -w "%{http_code}\n"`，发现访问失败，返回 `403` 返回码，AuthorizationPolicy 策略生效。
