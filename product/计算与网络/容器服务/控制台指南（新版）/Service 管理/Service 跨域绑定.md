## 简介

使用公网 CLB 型 Service 时，默认是在当前集群所在 VPC 内的随机可用区生成 CLB，现目前  TKE 的公网 CLB Service 已支持指定可用区、包括其他地域的可用区。本文将为您介绍如何通过控制台和 YAML 两种方式为 CLB Service 跨域绑定和指定可用区。


## 应用场景

- 需要支持 CLB 的跨地域接入或跨 VPC 接入，即 CLB 所在的 VPC 和当前集群所在的 VPC 不在同一 VPC 内。
- 需要指定 CLB 的可用区已实现资源的统一管理。

>?
> 1. 跨域绑定仅支持“带宽上移账户”。若您无法确定账户类型，请参见 [判断账户类型](https://cloud.tencent.com/document/product/1199/49090#judge)。
> 2. 如需使用非本集群所在 VPC 的 CLB，需先通过 [云联网](https://cloud.tencent.com/document/product/877/18752) 打通当前集群 VPC 和 CLB 所在的 VPC。
> 2. 在确保 VPC 已经打通之后，请 [在线咨询](https://cloud.tencent.com/act/event/connect-service) 申请使用该功能。
> 3. 以下 YAML 中，需要您输入地域 ID ，您可以通过 [地域和可用区](https://cloud.tencent.com/document/product/457/44787#.E4.B8.AD.E5.9B.BD) 查看地域 ID。


## 操作步骤

公网 CLB Service 跨域绑定和指定可用区支持通过控制台和 YAML 两种方式进行操作，操作步骤如下：


<dx-tabs>
::: 控制台方式
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击需要创建 Service 的集群 ID，进入待创建 Service 的集群管理页面。
3. 选择**服务与路由** > **Service**，进入 “Service” 管理页面。如下图所示：
   ![](https://main.qcloudimg.com/raw/c7ac45e1efc03a0cdbd937a35ade9037.png)
4. 单击**新建**，进入“新建Service”页面。
6. 在“新建 Service”页面中配置相关可用区规则。配置规则说明如下：
 - **服务访问方式**：选择“公网LB访问”。
 - **当前VPC**：使用本集群所在 VPC 内的 CLB，建议使用随机可用区，若指定可用区的资源售罄将无法创建相关实例。
 - **其它VPC**：仅支持通过 [云联网](https://console.cloud.tencent.com/vpc/ccn) 与当前集群的 VPC 打通的其他 VPC。建议使用随机可用区，若指定可用区的资源售罄将无法创建相关实例。
     ![](https://main.qcloudimg.com/raw/a94769f097ec3385b492a7078f69cd5a.png)
:::
::: YAML\s方式
<dx-alert infotype="explain" title="">
1. 如需使用非本集群所在 VPC 的 CLB，需先通过 [云联网](https://cloud.tencent.com/document/product/877/18752) 打通当前集群 VPC 和 CLB 所在的 VPC。
2. 在确保 VPC 已经打通之后，请 [在线咨询](https://cloud.tencent.com/act/event/connect-service) 申请使用该功能。
</dx-alert>
#### 示例1
如果仅需指定本集群所在 VPC 的可用区，例如集群的 VPC 在广州地域，CLB Service 需要指定广州一区的 CLB，可以在 Service 的 YAML 中添加如下 annotation：
```sh
service.kubernetes.io/service.extensiveParameters: '{"ZoneId":"ap-guangzhou-1"}'
```
#### 示例2
如需使用非本集群所在 VPC 内的 CLB，可以在 Service 的 YAML 中添加如下 annotation：
<dx-codeblock>
:::  sh
service.cloud.tencent.com/cross-region-id: "ap-guangzhou" 
service.cloud.tencent.com/cross-vpc-id: "vpc-646vhcjj"
:::
</dx-codeblock><dx-alert infotype="notice" title="">
如果您还需要指定可用区，需要再添加示例1中的 annotation。
</dx-alert>
#### 示例3
选择已有负载均衡进行异地接入，示例如下：
<dx-codeblock>
:::  yaml
service.cloud.tencent.com/cross-region-id: "ap-guangzhou" 
service.kubernetes.io/tke-existed-lbid: "lb-342wppll"
:::
</dx-codeblock>
#### 示例4 
annotation 在 Service YAML 中的写法如下所示：
<dx-codeblock>
:::  yaml
# 创建异地接入的负载均衡
apiVersion: v1
kind: Service
metadata: 
  annotations: 
    service.cloud.tencent.com/cross-region-id: "ap-chongqing"
    service.cloud.tencent.com/cross-vpc-id: "vpc-mjekzyps"
  name: echo-server-service
  namespace: default
spec: 
  ...... 
--- 
# 用户复用其他地域负载均衡的场景
apiVersion: v1
kind: Service
metadata: 
  annotations: 
    service.cloud.tencent.com/cross-region-id: "ap-chongqing"
    service.kubernetes.io/tke-existed-lbid: "lb-o8ugf2wb"
  name: echo-server-service
  namespace: default
spec: 
  ...... 
:::
</dx-codeblock>完整 Service Annotation 说明请参见 [Service Annotation 说明](https://cloud.tencent.com/document/product/457/51258) 文档。
:::
</dx-tabs>
