## 操作场景
腾讯云支持在云服务器购买页面生成已选配置对应的创建实例 OpenAPI 最佳实践脚本代码，您可保存代码用于购买同配置云服务器。

## 前提条件
- 登录腾讯云官网，并进入云服务器的 [自定义配置购买页面](https://buy.cloud.tencent.com/cvm?tab=custom)。
- 已按需选择云服务器配置，并进入确认配置信息页面。如需了解购买云服务器的配置项，请参见 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855)。

## 操作步骤
1. 在确认配置信息页面，单击**生成 API Explorer 最佳实践脚本**。如下图所示：
![](https://main.qcloudimg.com/raw/cea4614cd032b5c5fbca0c7750b40521.png)
2. 在弹出的“生成 API Explorer 最佳实践脚本”窗口中，您可查看以下信息。如下图所示：
![](https://main.qcloudimg.com/raw/a583939b7ea72e4f7cdd889be7905a6b.png)
 - **API工作流**：您可以查看创建实例接口 RunInstances 及所选配置对应该接口的实际参数。其中，使用 `*` 标记的参数为该接口的必填参数。 对于窗口显示不全的数据，您可将鼠标悬浮在数据上方查看对应内容。
 - **API脚本**：您可按需选择 Java 或 Python 作为生成脚本的代码语言。选择右上角的**复制脚本**即可获取脚本代码，保存的代码可用于购买相同配置的云服务器。
<dx-alert infotype="explain" title="">
- 由于密码为敏感信息，如果您设置了实例密码，将不会在页面及生成的脚本代码中展示，请自行修改。 
- API Explorer 实践脚本不支持统一到期日，您可在创建实例后另行设置。
</dx-alert>




