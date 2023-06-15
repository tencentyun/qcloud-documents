## 操作场景
通过 API 调试页面，您可以在配置完 API 后立即验证 API 的正确性，发起模拟 API 调用并查看具体请求响应。如果 API 未按照您期望的方式工作，可以根据响应，重新修改配置以符合您的设计期望。

## 前提条件
已完成 [创建通用 API](https://cloud.tencent.com/document/product/628/11797)。

## 操作步骤
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，在左侧菜单栏中单击**服务**，进入服务列表页。
2. 单击服务名，进入服务详情页，单击页面顶部的**管理 API**，进行 API 管理。
3. 选择需要调试的 API，单击 **API调试**，进入调试页面。
在调试页面，您可以看到需调试 API 的前端配置信息，包括路径、请求方法和 Content-Type 等。在请求参数（未配置则不显示）位置：
	- 如果您配置了参数具有默认值，则默认值会默认填充到输入框中；
	- 如果您配置了参数必填，则在测试前会检查是否已填写必填参数；
	- 如果您的请求方法为 POST、PUT、DELETE，则会有 Body 参数需要您填写。
>?如果非必填参数，用户不填写任何参数，则默认 API 网关会给后端传一个 null。
4. 单击**发送请求**，您将看到响应 Body和 Header。下图示例中后端响应内容为“Hello World”。
	<img src="https://qcloudimg.tencent-cloud.cn/raw/1017658b99ce79ba48cfc8436e815cbf.png" width=700/>


