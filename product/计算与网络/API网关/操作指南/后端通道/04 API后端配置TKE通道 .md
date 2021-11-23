## 操作场景

您可以直接在 API 的后端中，配置后端类型为 TKE 通道，让 API 网关的请求，直接转到 TKE 通道的对应的 Pod 上。

## **前提条件**

1. 配置 TKE 类型的后端通道。
2. 在专享 API 网关的服务上，才能配置 API 后端为 TKE 通道。

## **操作步骤**

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index)。

2. 在左侧导航栏选择**服务**，单击目标服务的“ID”，进入管理 API 页面。

3. 单击**新建**，创建通用 API。

4. 输入前端配置，然后点击**下一步**。

   ![](https://qcloudimg.tencent-cloud.cn/raw/c3de742d4bf12c69d8f3d6facbbd538b.png)        

5. 选择后端类型为**VPC内资源**，并且选择后端通道类型为**TKE通道**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/52eb0f2b7cf130808223fd7aeca8d8bd.png)        

6. 点击**下一步**，再点击**完成**。

## **注意事项**

TKE 通道和 API 网关专享在同一个 VPC 下才能使用，目前 API 网关暂时不支持直接跨 VPC。
