## 简介
创建 Ingress 选用 HTTPS 监听协议时，选用合适的服务器证书能够确保访问安全。本文档介绍 Ingress 证书使用相关的内容，与证书相关的 Annotation 如下：

- `kubernetes.io/ingress.http-rules`
- `kubernetes.io/ingress.https-rules`
- `kubernetes.io/ingress.rule-mix`
- `qcloud_cert_id`（只读）

## 注意事项

- Ingress Annotation 中的 `qcloud_cert_id` 是只读的，可快速了解当前 Ingress 对应的证书 ID。
- Secret 证书资源必须和 Ingress 资源放置在同一个 Namespace 下。
- 由于控制台默认会创建同名 Secret 证书资源，若 Secret 资源已存在，Ingress 将无法创建。
- 默认情况下，容器服务中的 Ingress 不会复用 Secret 资源。但 Secret 证书资源被允许复用于 Ingress ，需注意更新 Secret 的同时，会使所有 Ingress 的证书得到更新。 

## 操作步骤

### 使用证书

1. 登录负载均衡控制台，选择左侧导航栏中的 [**证书管理**](https://console.cloud.tencent.com/clb/cert)，在“证书管理”页面新建证书。
2. 参考 [创建 Ingress ](https://cloud.tencent.com/document/product/457/31711#.E5.88.9B.E5.BB.BA-ingress) 完成 Ingress 新建。
其中监听端口勾选**Https:443**，并选择合适的服务器证书。

>?
> -  当控制台创建的 Ingress 开启 HTTPS 服务，会先创建同名的 Secret 资源用于存放证书 ID，然后在 Ingress 中使用并监听该 Secret。
> - 在容器服务控制台修改证书时，会修改对应当前 Ingress 的证书资源。需注意的是，如用户的多个 Ingress 配置使用同一个 Secret 资源，那么这些 Ingress 对应负载均衡的证书会一起变更。
> - 当您直接在负载均衡控制台修改证书后，请务必参照[ 修改证书 ](#ModifySecret)步骤，及时修改使用该证书创建 Ingress 时控制台默认生成的同名 Secret 证书资源。否则 Ingress 配置的证书仍保持旧版本，将会导致您的证书更新失效。

### 更换证书
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 在“集群管理”页面，选择需更换证书集群 ID。
3. 在集群详情页，选择左侧**服务与路由** > **Ingress**。如下图所示：
![](https://main.qcloudimg.com/raw/69e9c55ea644144ea5848c98b9d0462a.png)
4. 选择需更换证书 Ingress 所在行右侧的**更新转发配置**。
5. 在“更新转发配置”页面中，按需更新“服务器证书”。如下图所示：
![](https://main.qcloudimg.com/raw/b063a80ad38e095d55655847e3ff3ff2.png)
6. 单击**更新转发配置**即可完成更新操作。



### Kubectl 操作指引

#### 配置证书并创建一个 HTTPS 服务[](id:CreatingSecret)

1. 执行以下命令，计算证书 “XczRzegn” 的 ID。
```yaml
echo -n "XczRzegn" | base64
```
返回结果如下：
```
WGN6UnplZ24=
```
1. 创建 Secret 资源。
 - Base64 手动编码。YAML 示例如下：
```yaml
apiVersion: v1
data:
  qcloud_cert_id: WGN6UnplZ24= ##  配置证书 ID 为 XczRzegn
kind: Secret
metadata:
  name: tencent-com-cert
  namespace: default
type: Opaque
```
 - Base64 自动编码：创建时使用 `stringData` 进行声明，避免手工进行 Base64 编码。YAML 示例如下：
```yaml
apiVersion: v1
stringData:
  qcloud_cert_id: XczRzegn
kind: Secret
metadata:
  name: tencent-com-cert
  namespace: default
type: Opaque
```
2. 创建 Ingress 资源。
创建 Ingress 资源时，请注意指定后端 Service 为 `sample-service:80`，指定 secretName 为 `tencent-com-cert`。YAML 示例如下：
<pre>
<span class="hljs-section">apiVersion: extensions/v1beta1</span>
<span class="hljs-section">kind: Ingress</span>
<span class="hljs-section">metadata:</span>
     annotations:
       kubernetes.io/ingress.class: qcloud
       qcloud_cert_id: XczRzegn
     name: sample-ingress
     namespace: default
<span class="hljs-section">spec:</span>
     rules:
     - http:
         paths:
         - backend:
             serviceName: sample-service
             servicePort: 80
         path: /
     tls:
     - secretName: tencent-com-cert
</pre>


#### 修改证书[](id:ModifySecret)

1. 执行以下命令，使用默认编辑器打开需修改的 Secret。
```
kubectl edit secrets
```
本文以 [创建 Secret 资源](#CreatingSecret) 中的 Secret 为例，则执行以下命令：
```
kubectl edit secrets tencent-com-cert
```
2. 修改 Secret 资源，将 `qcloud_cert_id` 的值修改为新的证书 ID。
>! 与创建 Secret 相同，修改 Secret 证书 ID 需要进行 Base64 编码，请根据实际需求选择 Base64 手动编码或者指定 `stringData` 进行 Base64 自动编码。


#### 混合规则配置

TKE Ingress Controller 支持混合配置 HTTP/HTTPS 规则，步骤如下：
1. 开启混合规则
将 `kubernetes.io/ingress.rule-mix` 设置为 True。
当 Ingress 模板未配置 TLS 时，不会提供证书资源，所有规则都将以 HTTP 服务暴露，上述注解将不会生效。
2. 规则匹配
将 Ingress 中的每一条规则与 `kubernetes.io/ingress.http-rules` 、`kubernetes.io/ingress.https-rules` 进行匹配并添加到对应规则集中。若 Ingress 中的规则未匹配，则默认添加到 HTTPS 规则集中。
3. 校验匹配项
匹配时请注意校验 Host、Path、ServiceName、ServicePort（其中 Host 默认为 `VIP`、Path 默认为 `/`）。
请注意 [IPv6](https://cloud.tencent.com/document/product/1142/38134) 的 CLB 不具备提供默认域名的功能。

#### YAML 示例

请参照下述 YAML 示例开启混合规则，同时配置后端服务为暴露 HTTP/HTTPS 服务。
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.http-rules: '[{"host":"www.tencent.com","path":"/","backend":{"serviceName":"sample-service","servicePort":"80"}}]'
    kubernetes.io/ingress.https-rules: '[{"host":"www.tencent.com","path":"/","backend":{"serviceName":"sample-service","servicePort":"80"}}]'
    kubernetes.io/ingress.rule-mix: "true"
    kubernetes.io/ingress.class: qcloud
    qcloud_cert_id: XczRzegn
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

## 常见问题
- 是否能修改 Ingress 中的 `tls.secretName` ，指向另一个 Secret 资源？
可以。更新后的 Secret 证书资源中指定的证书将很快同步到 Ingress 对应的负载均衡。

- 如何获取证书 ID？
登录负载均衡控制台，选择左侧导航栏中的 [**证书管理**](https://console.cloud.tencent.com/clb/cert)，在“证书管理”页面获取。



## 相关资料

更多内容请参考 Kubenetes 官网文档 [Secret](https://kubernetes.io/zh/docs/concepts/configuration/secret/)。



