## 简介

使用 CLB 型 Ingress 时，默认是在当前集群所在 VPC 内的随机可用区生成 CLB。现目前 TKE 的 CLB Ingress 已支持指定可用区、包括其他地域的可用区。本文将为您介绍如何通过控制台和 YAML 两种方式为 CLB Ingress 跨域绑定和指定可用区。



## 应用场景

- 需要支持 CLB 的跨地域接入或跨 VPC 接入，即 CLB 所在的 VPC 和当前集群所在的 VPC 不在同一 VPC 内。
- 需要指定 CLB 的可用区已实现资源的统一管理。

>?
> 1. 如需使用非本集群所在 VPC 的 CLB，需先通过 [云联网](https://cloud.tencent.com/document/product/877/18752) 打通当前集群 VPC 和 CLB 所在的 VPC。
> 2. 在确保 VPC 已经打通之后，请 [在线咨询](https://cloud.tencent.com/online-service?from=doc_457) 申请使用该功能。
> 3. 以下 YAML 中，需要您输入地域 ID ，您可以通过 [地域和可用区](https://cloud.tencent.com/document/product/457/44787#.E4.B8.AD.E5.9B.BD) 查看地域 ID。



## 操作步骤


CLB Ingress 跨域绑定和指定可用区支持通过控制台和 YAML 两种方式进行操作，操作步骤如下：


<dx-tabs>
::: 控制台方式
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面，选择需修改 Ingress 的集群 ID。
3. 在集群详情页，选择左侧**服务与路由** > **Ingress**。如下图所示：
   ![](https://main.qcloudimg.com/raw/69e9c55ea644144ea5848c98b9d0462a.png)
4. 单击**新建**，在“新建 Ingress”页面中配置相关可用区规则。配置规则说明如下：
   - **当前VPC**：使用本集群所在 VPC 内的 CLB，建议使用随机可用区，若指定可用区的资源售罄将无法创建相关实例。
   - **其它VPC**：仅支持通过 [云联网](https://console.cloud.tencent.com/vpc/ccn) 与当前集群的 VPC 打通的其他 VPC。建议使用随机可用区，若指定可用区的资源售罄将无法创建相关实例。
     ![](https://main.qcloudimg.com/raw/7b7b1c184e1f39b18ccef45e0ccac616.png)
:::
::: YAML\s方式
<dx-alert infotype="explain" title="">
1. 如需使用非本集群所在 VPC 的 CLB，需先通过 [云联网](https://cloud.tencent.com/document/product/877/18752) 打通当前集群 VPC 和 CLB 所在的 VPC。
2. 在确保 VPC 已经打通之后，请 [在线咨询](https://cloud.tencent.com/online-service?from=doc_457) 申请使用该功能。
</dx-alert>
#### 示例1
如果仅需要指定本集群所在 VPC 的可用区，例如集群的 VPC 在广州地域，CLB Ingress 需要指定广州一区的 CLB，可以在 Ingress 的 YAML 中添加如下 annotation：
<dx-codeblock>
:::  yaml
kubernetes.io/ingress.extensiveParameters: '{"ZoneId":"ap-guangzhou-1"}'
:::
</dx-codeblock>
#### 示例2
如需使用非本集群所在 VPC 内的 CLB，需先添加如下两条 annotation：
<dx-codeblock>
:::  yaml
ingress.cloud.tencent.com/cross-region-id: 
ingress.cloud.tencent.com/cross-vpc-id:
:::
</dx-codeblock>具体示例如下：
- 创建异地接入的负载均衡，需先添加如下两条 annotation：
<dx-codeblock>
:::  yaml
ingress.cloud.tencent.com/cross-region-id: "ap-guangzhou" 
ingress.cloud.tencent.com/cross-vpc-id: "vpc-646vhcjj"
:::
</dx-codeblock><dx-alert infotype="notice" title="">
若您还需指定可用区，则需要再添加示例1中的 annotation。
</dx-alert>
- 选择已有负载均衡进行异地接入，添加如下两条 annotation：
<dx-codeblock>
:::  yaml
ingress.cloud.tencent.com/cross-region-id: "ap-guangzhou" 
kubernetes.io/ingress.existLbId: "lb-342wppll"
:::
</dx-codeblock><dx-alert infotype="notice" title="">
若您还需指定可用区，则需要再添加示例1中的 annotation。
</dx-alert>
完整 Ingress Annotation 说明请参见 [Ingress Annotation 说明](https://cloud.tencent.com/document/product/457/56112)。
:::
</dx-tabs>
