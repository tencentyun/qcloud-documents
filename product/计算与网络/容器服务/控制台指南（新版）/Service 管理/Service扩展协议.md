##  Service 默认支持的协议

 Service 是 Kubernetes 暴露应用程序到集群外的一种机制与抽象，您可以通过 Serivce 访问集群内的应用程序。


<dx-alert infotype="notice" title="">
- 在 [直连场景](https://cloud.tencent.com/document/product/457/41897) 下接入，使用扩展协议时没有任何限制，支持 TCP 和 UDP 协议混用。
- 非直连场景下，ClusterIP 和 NodePort 模式支持混用。但社区对 LoadBalance 类型的 Service 有限制，目前仅能使用同类型协议。
- 当 LoadBalance 声明为 TCP 时，端口可以使用扩展协议的能力，将负载均衡的协议变更为 TCP_SSL、HTTP、HTTPS。
- 当 LoadBalance 声明为 UDP 时，端口可以使用扩展协议的能力，将负载均衡的协议变更为 UDP。
</dx-alert>



## TKE 扩展 Service 转发协议

在原生的 Service 支持的协议的规则上，存在部分场景需要在 Service 上同时支持 TCP 和 UDP 混合，且需 Service 能够支持 TCP SSL、HTTP、HTTPS 协议。TKE 针对 LoadBalancer 模式扩展了更多协议的支持。



### 前置说明

- 扩展协议仅对 LoadBalancer 模式的 Service 生效。
- 扩展协议通过注解 Annotation 的形式描述协议与端口的关系。
- 扩展协议与注解 Annotation 关系如下：
   - 当扩展协议注解中没有覆盖 Service Spec 中描述的端口时，Service Spec 按照用户描述配置。
   - 当扩展协议注解中描述的端口在 Service Spec 中不存在时，忽略该配置。
   - 当扩展协议注解中描述的端口在 Service Spec 中存在时，覆盖用户在 Service Spec 中声明的协议配置。



### 注解名称
`service.cloud.tencent.com/specify-protocol`

### 扩展协议注解示例

<dx-tabs>
::: TCP_SSL 示例
<dx-codeblock>
::: xml 
{"80":{"protocol":["TCP_SSL"],"tls":"cert-secret"}}
:::
</dx-codeblock>
:::
::: HTTP 示例
<dx-codeblock>
::: xml 
{"80":{"protocol":["HTTP"],"hosts":{"a.tencent.com":{},"b.tencent.com":{}}}}
:::
</dx-codeblock>
:::
::: HTTPS 示例
<dx-codeblock>
::: xml 
 {"80":{"protocol":["HTTPS"],"hosts":{"a.tencent.com":{"tls":"cert-secret-a"},"b.tencent.com":{"tls":"cert-secret-b"}}}}
:::
</dx-codeblock>
:::
::: TCP/UDP混合示例
<dx-codeblock>
::: xml 
{"80":{"protocol":["TCP","UDP"]}} # 仅[直连模式](https://cloud.tencent.com/document/product/457/41897)支持
:::
</dx-codeblock>
:::
::: 混合示例
<dx-codeblock>
::: xml 
 {"80":{"protocol":["TCP_SSL","UDP"],"tls":"cert-secret"}} # 仅[直连模式](https://cloud.tencent.com/document/product/457/41897)支持
:::
</dx-codeblock>
:::
</dx-tabs>




### 扩展协议使用说明
<dx-tabs>
::: 扩展协议YAML使用说明
```yaml
apiVersion: v1
kind: Service
metadata:
    annotations:  
      service.cloud.tencent.com/specify-protocol: '{"80":{"protocol":["TCP_SSL"],"tls":"cert-secret"}}' # 若要使用别的协议，修改该键值对的值为上述内容
    name: test
   ....
```
:::
::: 扩展协议控制台使用说明
- 在创建 Service 时，若以“**公网LB**”或“**内网LB**”的形式暴露服务，非 [直连模式](https://cloud.tencent.com/document/product/457/41897) 情况下，“端口映射”中，仅支持 TCP 和 TCP SSL 一起使用。如下图所示：
![](https://main.qcloudimg.com/raw/06e722b64ab53446c434b4eca543de65.png)

- 当 Service 为“**仅在集群内访问**（ClusterIP）”或“**主机端口访问**（NodePort）”模式时，支持任意协议混用。
- [直连模式](https://cloud.tencent.com/document/product/457/41897)，支持任意协议混用。
:::
</dx-tabs>



