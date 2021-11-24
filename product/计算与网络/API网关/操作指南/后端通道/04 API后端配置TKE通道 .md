## 操作场景

您可以直接在 API 的后端中，配置后端类型为 TKE 通道，让 API 网关的请求，直接转到 TKE 通道的对应的 Pod 上。

## 前提条件

已 [配置 TKE 类型的后端通道](https://cloud.tencent.com/document/product/628/64688)。


## 操作步骤

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index)。
2. 在左侧导航栏选择**服务**，单击目标服务的“ID”，进入管理 API 页面。
3. 单击**新建**，创建通用 API。
4. 输入前端配置，然后点击**下一步**。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/d0afa98fcc4c5a83bc1a8f1ddd5e464e.png)
5. 选择后端类型为 **VPC内资源**，并且选择后端通道类型为 **TKE通道**，单击**下一步**。  
	 ![](https://qcloudimg.tencent-cloud.cn/raw/d3365999710dea204a252c2619230616.png)
6. 设置响应结果，并单击**完成**。

## 注意事项

TKE 通道和 API 网关专享在同一个 VPC 下才能使用，目前 API 网关暂时不支持直接跨 VPC。
