## 简介
腾讯会议 Postman模板调试工具是为方便开发者进行腾讯会议 Rest API 接口联调而提供第三方开发调试工具。目前该工具支持 OAuth 鉴权与接口调试。下文将描述如何利用 Postman 工具调试 REST API。

## 操作步骤
### 步骤1：调试前准备
我们提供两种方式导入模板。

#### 方式1：在线运行 Postman 模板库
通过这种方式，当模板更新后，您可以通过“Merge Changes”方式获取最新内容。
1. 单击以下按钮。
<div style="background-color:#ff6c37; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://app.getpostman.com/run-collection/7490232-6a52c208-8969-4a15-bf8a-75af40214215?action=collection%2Ffork&collection-url=entityId%3D7490232-6a52c208-8969-4a15-bf8a-75af40214215%26entityType%3Dcollection%26workspaceId%3D39300aff-7c56-443d-8806-6b65304d62da#?env%5Boauth_environment%5D=W3sia2V5IjoiT0F1dGhIT1NUIiwidmFsdWUiOiJtZWV0aW5nLnRlbmNlbnQuY29tIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQiLCJzZXNzaW9uVmFsdWUiOiJtZWV0aW5nLnRlbmNlbnQuY29tIiwic2Vzc2lvbkluZGV4IjowfSx7ImtleSI6InNka19pZCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQiLCJzZXNzaW9uVmFsdWUiOiIiLCJzZXNzaW9uSW5kZXgiOjF9LHsia2V5Ijoic2VjcmV0IiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCIsInNlc3Npb25WYWx1ZSI6IiIsInNlc3Npb25JbmRleCI6Mn0seyJrZXkiOiJyZWRpcmVjdF91cmkiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0Iiwic2Vzc2lvblZhbHVlIjoiIiwic2Vzc2lvbkluZGV4IjozfSx7ImtleSI6InJlZnJlc2hfdG9rZW4iLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0Iiwic2Vzc2lvblZhbHVlIjoiIiwic2Vzc2lvbkluZGV4Ijo0fSx7ImtleSI6InByb3RvY29sIiwidmFsdWUiOiJodHRwcyIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0Iiwic2Vzc2lvblZhbHVlIjoiaHR0cHMiLCJzZXNzaW9uSW5kZXgiOjV9LHsia2V5IjoiYXBpaG9zdCIsInZhbHVlIjoiYXBpLm1lZXRpbmcucXEuY29tIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQiLCJzZXNzaW9uVmFsdWUiOiJhcGkubWVldGluZy5xcS5jb20iLCJzZXNzaW9uSW5kZXgiOjZ9LHsia2V5IjoicG9ydCIsInZhbHVlIjoiNDQzIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQiLCJzZXNzaW9uVmFsdWUiOiI0NDMiLCJzZXNzaW9uSW5kZXgiOjd9LHsia2V5IjoiQWNjZXNzVG9rZW4iLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0Iiwic2Vzc2lvblZhbHVlIjoiIiwic2Vzc2lvbkluZGV4Ijo4fSx7ImtleSI6Ik9wZW5JZCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQiLCJzZXNzaW9uVmFsdWUiOiIiLCJzZXNzaW9uSW5kZXgiOjl9LHsia2V5IjoiWFRjTm9uY2UiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJhbnkiLCJzZXNzaW9uVmFsdWUiOiIiLCJzZXNzaW9uSW5kZXgiOjEwfSx7ImtleSI6Im1lZXRpbmdfaWQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0Iiwic2Vzc2lvblZhbHVlIjoiIiwic2Vzc2lvbkluZGV4IjoxMX1d" target="_blank"  style="color: white; font-size:16px;">Run in Postman</a></div>
2. 单击 **Fork Collection**，登录账号或创建一个账号。
![](https://qcloudimg.tencent-cloud.cn/raw/4ec6e441797c3ef991ef3d8832599923.png)
3. 再次单击 **Fork collection**，可以在 Collection 中看到导入进来的模板，切换环境为 oauth_environment 即导入完毕。
![](https://qcloudimg.tencent-cloud.cn/raw/b795da6579cc1ab801ace904405c91f7.png)
4. 您可以通过单击 **Merge Changes** 来获取最新内容。<br>
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/1c0a3c2fee58aca63a316fed2310273b.png" />

#### 方式2：将模板库文件导入 Postman 工具
在 Postman 中导入环境配置文件和接口模板，首先单击下面两个链接分别下载环境文件与接口集合文件到本地。
- [接口集合](https://drive.weixin.qq.com/s?k=AJEAIQdfAAo1pUHgmHAX4AFwb1ANc)
- [环境](https://drive.weixin.qq.com/s?k=AJEAIQdfAAo9FtjtIXAX4AFwb1ANc)

进入 Postman 并在 workspace 下单击 **Import**，导入两个文件。
![](https://qcloudimg.tencent-cloud.cn/raw/74690439e799cd4ff6cd5f203f5fe98d.jpg)
如下图左侧 Tab 栏，Collection 中可以看到导入的新接口模板，里面接口包含 OAuth 鉴权环节接口和可供 OAuth 鉴权调试的会议 RestAPI ；Environment 中可以看到导入的环境，在这里可以配置环境参数，目前已提供一个测试应用用于调试，可以将其中内容替换为所测应用的信息。
![](https://qcloudimg.tencent-cloud.cn/raw/9a310b2b2bb8590b24ee2c68b3791f57.jpg)
环境参数中，将 sdk_id，secret，redirect_uri 替换为您测试应用的信息，您可以通过 [腾讯会议](https://meeting.tencent.com/marketplace/user-third-party) 应用详情中查看。 
![](https://qcloudimg.tencent-cloud.cn/raw/6c3b1d88fb4cf598a73c49f81c6c5b6d.jpg)

### 步骤2：获取授权码
右上角切换环境为 oauth_environment，选择**获取 auth_code**，单击 **send** 发送请求。
![](https://qcloudimg.tencent-cloud.cn/raw/b6879d90670631689901a4ee32dbd4d8.jpg)
复制这个链接到浏览器中打开，并且完成授权操作。
![](https://qcloudimg.tencent-cloud.cn/raw/842a1873553bcb2d4020b3a08da5cb2c.jpg)
在浏览器 URL 处拿到 auth_code。
![](https://qcloudimg.tencent-cloud.cn/raw/501ff214d26fee45509f5544de61286a.jpg)

### 步骤3：获取 access_token
根据第二步中获取的 auth_code，调用此接口，替换 auth_code 内容。
![](https://qcloudimg.tencent-cloud.cn/raw/b31a65e00bba1a8191f6553a0c77fe01.jpg)
获得 access_token，refresh_token 和 open_id。
![](https://qcloudimg.tencent-cloud.cn/raw/632bd26d02aa3a52780af95cdc6c4cfe.jpg)

### 步骤4：调用接口
准备 open_id 与 access_token，准备要测试的接口，以**创建会议**为例介绍调试过程：
1. 环境变量
设置环境中的 OpenId 和 AccessToken 变量，替换为步骤2中获取到的自己刚才保存的值。
![](https://qcloudimg.tencent-cloud.cn/raw/6c4e2a00ce2d30654f51c2f5cbc79fc0.jpg)
2. 编辑 Header
根据 OAuth 鉴权 Header 要求，确认必填字段已填入。
![](https://qcloudimg.tencent-cloud.cn/raw/a8205695eec9a374944f5e56f2cfa141.jpg)
3. 编辑 Params 和 Body，单击 **send** 发送请求。
4. 查看调试结果。
![](https://qcloudimg.tencent-cloud.cn/raw/aa7ae85ab5d40fb9f64fd9cd532980da.jpg)

### 步骤5：刷新 access_token
由于 access_token 有效期为6小时，在过期之后需要通过 refresh_token 刷新 access_token 字段，用于继续正常调试接口。在 Body 中将 refresh_token 字段内容替换为请求 access_token 时获取到的 refresh_token 值。
![](https://qcloudimg.tencent-cloud.cn/raw/8ed50722f03e5ff3b9df412faead48bb.jpg)
