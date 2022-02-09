腾讯实时音视频内容审核服务提供实时的音视频内容识别与审核，客户至需要调用音视频流接口即可实时检测音视频流中是否出现违规内容，腾讯实时音视频审核服务会通过回调把违规信息发送给客户制定的 URL。

## 实现原理
直播内容安全通过“哑终端”的形式进入指定的 TRTC 房间，作为“观众”拉取音视频流，并针对拉取到音视频流进行内容审核，然后通过回调把违规信息发送到用户指定的 HTTP/HTTPS 服务上。

![](https://qcloudimg.tencent-cloud.cn/raw/4a2e43462a99c00539a11211af7611f5.png)

## 开通服务
1. 进入 [腾讯云 TRTC 控制台](https://console.cloud.tencent.com/trtc)，开通 TRTC 服务。TRTC 会分配 SDKAppID，在创建内容审核时需要用到。（已经成功接入 TRTC 可以忽略该步骤）。
2. 进入 [内容安全控制台](https://console.cloud.tencent.com/cms/livevideo/overview)，选择要使用的产品。选择直播音频或者直播视频时：
	- 如果是实时语音聊天应用，则选择直播音频内容安全 [ams]。
	- 如果是实时视频通话或者单人/多人互动直播，则选择直播视频内容安全 [vm]。
![](https://qcloudimg.tencent-cloud.cn/raw/395af0416aefed1872d3dc4c758269e0.png)
3. 选择产品后会弹出服务开通界面，单击**开通**。
> ! 由于音视频产品需要使用用户的 COS 桶进行存储审核的音频切片和图片帧，单击**开通**后，需要用户授权内容安全产品访问用户 COS 桶，单击**授权**后，会弹出授权成功界面。
4. 开通服务后，在服务管理可以看到授权的 COS 桶信息。也可以在 [COS](https://console.cloud.tencent.com/cos5) 的控制台界面中看到该 COS 桶，用户可以根据实际情况在 COS 控制台中设置授权的 COS 桶中音频切片/图片截帧信息的存储周期。
![](https://qcloudimg.tencent-cloud.cn/raw/895a7041695b25df701288635dcf4639.png)
5. 开通完服务，用户可以在 [腾讯云接口测试界面](https://console.cloud.tencent.com/api/explorer?Product=ams&Version=2020-12-29&Action=CreateAudioModerationTask&SignVersion=) 发起审核，接入流程见 [审核接入流程](https://cloud.tencent.com/document/product/647/69054)。
