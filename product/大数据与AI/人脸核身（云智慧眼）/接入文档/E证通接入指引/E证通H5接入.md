本文为您描述如何接入E证通 H5，接入相关指引连接如下：
1. [开通E证通](https://cloud.tencent.com/document/product/1007/56642)
2. [申请商户 ID](#spang)
3. [获取 EidToken](#eidtoken)
4. [跳转至 H5 进行核身](#eidh5)
5. [获取E证通核验结果信息](#jieguo)
6. [查看错误码](https://cloud.tencent.com/document/product/1007/47912)
7. [对账指引](https://cloud.tencent.com/document/product/1007/51816)

详细接入操作如下：

[](id:spang)
## 1. 申请商户 ID
1.1 登录腾讯云慧眼 [人脸核身控制台](https://console.cloud.tencent.com/faceid)，单击**自助接入**>**E证通服务**>**申请商户 ID**
![](https://main.qcloudimg.com/raw/ee9d314f001f83023b36145271fce756.png)
1.2 填写完相关申请信息，单击**提交**，审核时间需要3-5天，请您耐心等待。
![](https://main.qcloudimg.com/raw/14565c77b200b1be75664b33fc6a84b9.png)
1.3 审核通过后，可以在自助接入列表页，查看商户 ID，后续需要使用商户 ID 获取E证通服务流程唯一标识 EidToken。 

[](id:eidtoken)
## 2. 获取 EidToken 和 URL
接入方服务端调用 [获取E证通 Token](https://cloud.tencent.com/document/product/1007/54089) 接口，传入E证通服务所需信息获取到 EidToken 以及核身 URL。该 URL 有效为十分钟，且仅能使用一次。

[](id:eidh5)
## 3. 跳转至 H5 进行核身
用户跳转至第二步获取到的 URL 完成核身之后，接入方可以有两种方式获取核身结果事件：接入方后台轮询、E证通重定向。

### 3.1 接入方后台轮询方式
如果接入方业务全程都在 PC 端的网页进行，可以将第二步获取到的核身 URL 转换为二维码进行展示，提示用户使用手机微信扫码进入E证通业务流程。接入方通过后台轮询 [CheckEidTokenStatus](https://cloud.tencent.com/document/product/1007/58231) 接口的方式实时检查用户的验证状态，然后根据返回的状态合理设计业务流程。
>!建议轮询间隔为1秒。遇到网络错误等异常状态连续三次以上才认为失败，否则均保持上一次状态。
 
 
### 3.2 重定向方式
如果接入方有自己的 H5，需要在第二步获取 EidToken 传入 `RedirectUrl`，在用户核身完成之后，Eid 会在微信 H5 中重定向到 RedirectUrl 并在 query 参数携带 `token={EidToken}`。接入方 H5 接收到参数后可以进行后续流程。 

>!建议接入方重定向地址为后端接口，并在 URL 中有自身的鉴权信息，核身结果根据 EidToken 从腾讯云后台拉取。  

[](id:jieguo)
## 4. 获取E证通核验结果信息

接入方获取到完成事件后，调用 [获取 Eid 核身结果信息](https://cloud.tencent.com/document/product/1007/54090) 接口去获取本次核身的详细信息。

## 接入时序图（轮询）
>!轮询应从获取 EidTtoken 之后就开始，对 EidToken 状态相应处理，如果核身完成就可以拉取核身结果。

![](https://main.qcloudimg.com/raw/4234f67c18e1292b89420a5bb26fc9bf.svg)
 

 
## 接入时序图（重定向）

![](https://main.qcloudimg.com/raw/3d9ab9879ab9101c57d56e513ad9b196.svg)
