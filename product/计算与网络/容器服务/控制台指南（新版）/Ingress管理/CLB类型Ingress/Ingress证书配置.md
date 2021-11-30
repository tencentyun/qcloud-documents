## 操作场景
本文档介绍 Ingress 证书使用相关的内容，您可在以下场景中进行 Ingress 证书配置：
- 创建 Ingress 选用 HTTPS 监听协议时，选用合适的服务器证书能够确保访问安全。
- 为所有的 HTTPS 域名绑定同一个证书，简化配置 Ingress 下所有 HTTPS 规则的证书，使更新操作更加便捷。
- 为不同的域名绑定不同的证书，改善服务器与客户端 SSL/TLS。

## 注意事项
- 需提前创建需配置的证书，详情请参见 [通过控制台新建服务器证书](#create)。
- 需使用 Secret 形式来设置 Ingress 证书。腾讯云容器服务 TKE Ingress 会默认创建同名 Secret，其内容包含证书 ID。
- Secret 证书资源需和 Ingress 资源放置在同一个 Namespace 下。
- 由于控制台默认会创建同名 Secret 证书资源，若同名 Secret 资源已存在，则 Ingress 将无法创建。
- 通常情况下，在创建 Ingress 时，不会复用 Secret 关联的证书资源。但仍支持在创建 Ingress 复用 Secret 关联的证书资源，更新 Secret 时，会同步更新所有引用该 Secret 的 Ingress 的证书。
- 为域名增加匹配证书后，将同步开启负载均衡 CLB SNI 功能（不支持关闭）。若删除证书对应的域名，则该证书将默认匹配 Ingress 所对应的 HTTPS 域名。
- 传统型负载均衡不支持基于域名和 URL 的转发，由传统型负载均衡创建的 Ingress 不支持配置多证书。




## 示例
TKE 支持通过 Ingress 中的 `spec.tls` 的字段，为 Ingress 创建的 CLB HTTPS 监听器配置证书。其中，secretName 为包含腾讯云证书 ID 的 Kubernetes Secret 资源。 示例如下：
- **ingress**
```yaml
spec:
    tls:
    - hosts:
      - www.abc.com
      secretName: secret-tls-2
```
- **Sercret**
```yaml
apiVersion: v1
stringData:
    qcloud_cert_id: Xxxxxxxx ## 配置证书 ID 为 Xxxxxxxx
kind: Secret
metadata:
    name: tencent-com-cert
    namespace: default
type: Opaque
```
>?您还可参考 [创建 Secret](https://cloud.tencent.com/document/product/457/31718#.E5.88.9B.E5.BB.BA-secret)，通过容器服务控制台进行创建。主要参数配置如下：
>- **名称**：自定义，本文以 cos-secret 为例。
>- **Secret类型**：选择**Opaque**，该类型适用于保存密钥证书和配置文件，Value 将以 Base64 格式编码。
>- **生效范围**：按需选择，需确保与 Ingress 在同一 Namespace 下。
>- **内容**：变量名设置为 `qcloud_cert_id`，变量值配置为 qcloud_cert_id 所对应的证书 ID。
>

## Ingress 证书配置的行为
- 仅配置单个 `spec.secretName` 且未配置 hosts 的情况下，将会为所有的 HTTPS 的转发规则配置该证书。示例如下：
```yaml
spec:
    tls:
    - secretName: secret-tls
```
- 支持配置一级泛域名统配。 示例如下：
```yaml
spec:
    tls: 
    - hosts:
      - *.abc.com
      secretName: secret-tls
```
-  若同时配置证书与泛域名证书，将优先选择一个证书。 示例如下，`www.abc.com` 将会使用 `secret-tls-2` 中描述的证书。
```yaml
spec:
    tls: 
    - hosts:
      - *.abc.com
      secretName: secret-tls-1
    - hosts:
      - www.abc.com
      secretName: secret-tls-2
```
- 对已使用多个证书的 Ingress 进行更新时，TKE Ingress controller 将进行以下行为判断：
   - HTTPS 的 rules.host 无任何匹配时，若判断不通过，则不能提交更新。
   - HTTPS 的 rules.host 匹配中单个 TLS 时，可提交更新，并为该 host 配置对 Secret 中对应的证书。
   - 修改 TLS 的 SecretName 时仅校验 SecretName 的存在性，而不校验 Secret 内容， Secret 存在即可提交更新。
   > ! 请确保 Secret 中证书 ID 符合要求。





## 操作步骤
### 通过控制台新建服务器证书[](id:create)
>?若您已具备需配置的证书，则请跳过此步骤。
>
1. 登录负载均衡控制台，选择左侧导航栏中的 **[证书管理](https://console.cloud.tencent.com/clb/cert)**。
2. 在“证书管理”页面中，单击**新建**。
3. 在弹出的“新建证书”窗口中，参考以下信息进行设置。
 - **证书名称**：自定义设置。
 - **证书类型**：选择“服务器证书”。
**服务器证书**：即 SSL 证书（SSL Certificates）。基于 SSL 证书，可将站点由 HTTP（Hypertext Transfer Protocol）切换到 HTTPS（Hyper Text Transfer Protocol over Secure Socket Layer），即基于安全套接字层（SSL）进行安全数据传输的加密版 HTTP 协议。
   - **证书内容**：根据实际情况填写证书内容，证书格式要求请参见文档[ SSL 证书格式要求及格式转换说明](https://cloud.tencent.com/document/product/214/5369)。
   - **密钥内容**：仅当证书类型选择为“服务器证书”时，该选项才会显示。请参考文档[ SSL 证书格式要求及格式转换说明](https://cloud.tencent.com/document/product/214/5369) 添加相关密钥内容。
4. 单击**提交**即可完成创建。

### 创建使用证书的 Ingress 对象
参考 [创建 Ingress ](https://cloud.tencent.com/document/product/457/31711#.E5.88.9B.E5.BB.BA-ingress) 完成 Ingress 新建，其中监听端口勾选**Https:443**。

>!
>- 当控制台创建的 Ingress 开启 HTTPS 服务，会先创建同名的 Secret 资源用于存放证书 ID，并在 Ingress 中使用并监听该 Secret。
- TLS 配置域名与证书的对应关系如下：
 - 可以使用一级泛域名统配。
 - 若域名匹配中多个不同的证书，将随机选择一个证书，不建议相同域名使用不同证书。
 - 需为所有 HTTPS 域名配置证书，否则会创建不通过。


### 修改证书
>! 
>- 如果您需要修改证书， 请确认所有使用该证书的 Ingress。如用户的多个 Ingress 配置使用同一个 Secret 资源，那么这些 Ingress 对应 CLB 的证书会同步变更。
>- 证书需要通过修改 Secret 进行修改， Secret 内容中包含您使用的腾讯云证书的 ID。
>
1. 执行以下命令，使用默认编辑器打开需修改的 Secret。其中，`[secret-name]` 需更换为需修改的 Secret 的名称。
```
kubectl edit secrets [secret-name]
```
2. 修改 Secret 资源，将 `qcloud_cert_id` 的值修改为新的证书 ID。
与创建 Secret 相同，修改 Secret 证书 ID 需要进行 Base64 编码，请根据实际需求选择 Base64 手动编码或者指定 `stringData` 进行 Base64 自动编码。

### 更新 Ingress 对象

#### 通过控制台更新
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面，选择需修改 Ingress 的集群 ID。
3. 在集群详情页，选择左侧**服务与路由** > **Ingress**。如下图所示：
![](https://main.qcloudimg.com/raw/69e9c55ea644144ea5848c98b9d0462a.png)
4. 单击目标 Ingress 所在行右侧的**更新转发配置**。
5. 在“更新转发配置”页面中，根据实际情况进行转发配置规则更新。
6. 单击**更新转发配置**即可完成更新操作。

#### 通过 yaml 更新
执行以下命令，使用默认编辑器打开需修改的 ingress，修改 yaml 文件并保存即可完成更新操作。
```
kubectl edit ingress <ingressname> -n <namespaces>
```


