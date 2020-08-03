## 操作场景
通过 API 调试页面，您可以在配置完 API 后立即验证 API 的正确性，发起模拟 API 调用并查看具体请求响应。如果 API 未按照您期望的方式工作，可以根据响应，重新修改配置以符合您的设计期望。

## 前提条件
已完成 [创建微服务 API](https://cloud.tencent.com/document/product/628/17561)。

## 操作步骤
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，在左侧菜单栏中单击【服务】，进入服务列表页。
2. 单击服务名，进入服务详情页，单击页面顶部的【管理API】，进行 API 管理。
3. 在微服务 API 列表中，选择需要调试的 API，单击操作列的【调试】，进入调试页面。
4. 在调试页面中填写对应的请求参数后，单击【发送请求】即可。
![](https://main.qcloudimg.com/raw/505b0481c9e871b70f6f3e16e6017de8.jpg)
这里 X-NameSpace-Code、X-MicroService-Name 两个参数为必填参数，若您配置了其他参数，填写规则可参考 [调试通用 API](https://cloud.tencent.com/document/product/628/12005)。  
