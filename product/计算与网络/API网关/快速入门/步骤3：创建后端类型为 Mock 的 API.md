## 操作场景

该任务指导通过 API 网关控制台在已创建好的服务下创建一个后端对接 Mock 的 API。

>!后端对接 Mock 仅能返回固定数据，建议您在测试过程中使用，不建议在真实业务场景中使用。

## 前提条件

已 [创建服务](https://cloud.tencent.com/document/product/628/64197)。

## 操作步骤

1. 在服务列表页单击服务名称，进入 API 列表页。
2. 在**通用 API** 页签选择**新建**，输入 API 前端配置信息。
   - API名称：API 名称，此处我们输入“exampleapi”。
   - 前端类型：支持 HTTP&HTTPS、WS&WSS 两种前端类型，此处我们选择“HTTP&HTTPS”。
   - 路径：此 API 的访问路径，此处我们填写“/”。
   - 请求方法：此 API 的请求方法，此处我们选择GET。
   - 鉴权类型：此 API 的鉴权类型，此处我们选择“免认证”。
   - 支持CORS：此 API 是否支持跨域资源共享，此处我们选择“是”。
   - 备注：此 API 的备注信息，此处我们填写“测试”
   - 参数配置：此 API 的前端参数，此处我们不填写。
		
		<img src="https://qcloudimg.tencent-cloud.cn/raw/0942e93bd6643696cef11c223e65d2ff.png" width=600/>
3. 单击**下一步**，输入 API 后端配置信息。
   - 后端类型：此 API 后端服务所属类型，此处我们选择“Mock”。
   - 返回数据：Mock 返回数据，此处我们输入“hello world, hello apigateway”。

		<img src="https://qcloudimg.tencent-cloud.cn/raw/0257ffa3fff4397ad86289fddd6c450b.png" width=600/>
4. 单击**完成**，即可完成创建后端类型为 Mock 的 API。

