## 操作场景

通过 API 调试页面，您可以在配置完 API 后立即验证 API 的正确性，发起模拟 API 调用并查看具体请求响应。如果 API 未按照您期望的方式工作，可以根据响应，重新修改配置以符合您的设计期望。

## 前提条件

已完成 [创建 API](https://cloud.tencent.com/document/product/628/64198)。

## 操作步骤

1. 在 API 列表页找到 [步骤3](https://cloud.tencent.com/document/product/628/64198) 中刚创建的 API ，在操作栏中单击**API调试**，进入 API 调试页面。
2. 由于在步骤3中我们已经设置了GET请求，此时单击**发送**，即可查看本次调试的返回结果。
	状态码对应我们设置的200，body返回内容对应我们设置的“hello world, hello apigateway”。
	
	<img src="https://qcloudimg.tencent-cloud.cn/raw/7519cc159382c661114507b799b8d4d5.png" width=700 />

