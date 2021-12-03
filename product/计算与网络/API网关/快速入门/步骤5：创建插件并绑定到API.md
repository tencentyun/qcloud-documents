## 操作场景

该任务指导通过 API 网关控制台创建一个插件并绑定到已创建好的 API 上。

## 前提条件

已 [创建 API](https://cloud.tencent.com/document/product/628/64198)。

## 操作步骤

1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway) 左侧导航栏选择 **插件** > **系统插件**。
2. 单击**新建**，填写插件信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/6c92c031f1a203e3349f194851261413.png)
   - 插件名称：最长50个字符，支持 `a-z`、`A-Z`、`0-9`、`_`，_此处填写“exampleplugin”。
   - 类型：选择**IP访问控制**。
   - 插件描述：此插件描述信息，此处我们填写“测试”
   - 属性：支持黑名单和白名单，此处我们选择“白名单”。
   - IP：填写该 API 允许访问的 IP 地址或者 CIDR。
   - 标签：用于分类管理资源，可不选。
3. 单击**保存**，完成插件创建。
4. 在插件列表页面，单击刚刚创建好的插件操作列的**绑定API**。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/47e97a4e1c6e4ede0739a3140733f508.png)
   - 服务：选择刚刚创建的服务“exampleservice”。
   - 选择环境：选择**发布**。
   - 选择要绑定的 API：选择刚刚创建的 API“exampleapi”
5. 单击**确定**，完成绑定。

