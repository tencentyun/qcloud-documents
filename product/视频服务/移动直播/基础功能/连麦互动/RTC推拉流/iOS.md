
[](id:step1)
## 服务开通 
使用 RTC 直播或者连麦互动需要在开始接入前，先开通腾讯云 [**实时音视频**](https://cloud.tencent.com/document/product/647) 服务，具体步骤如下：

1. 您需要 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 登录实时音视频控制台，选择 **[应用管理](https://console.cloud.tencent.com/trtc/app)**。
3. 单击 **创建应用**，输入应用名称，例如 `V2Demo`，单击 **确定**。
4. 创建成功后，单击应用列表中 **应用名称** 为 `V2Demo` 这行右侧的 **应用信息**，查看应用对应的 `SDKAppID` 信息。
![](https://main.qcloudimg.com/raw/10e6a9395d2ebc19825d1183d5bef8f1.png)
5. 单击 **开发辅助** > **快速跑通Demo**，选中 **选择已有应用**，在下拉列表中选择 `V2Demo`，单击 **创建**。
<img src="https://main.qcloudimg.com/raw/105c7afd43f689e6f4db64bb737e6d9a.png" width=528>
6. 在创建成功后的页面，单击 **已下载，下一步**。
7. 在 **修改配置** 页面可以记录出现的 **密钥**，下文中将会替换 `SECRETKEY`，计算出 `UserSig`。
<img src="https://main.qcloudimg.com/raw/88ac7e12dfe38069ea7dc155d09e13af.png" width=528>
> !
> - 本文提到的生成 UserSig 的方案是在客户端代码中配置 UserSig，该UserSig 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此 **该方法仅适合本地跑通 Demo 和功能调试**。
> - 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。
8. 若您的播放端需要进行 CDN 播放，则需要在 [**应用管理**](https://console.cloud.tencent.com/trtc/app) 中选择 `V2Demo` 行右侧的 **应用信息**，选择 **功能配置** 页，开启 **旁路推流** 功能。
![](https://main.qcloudimg.com/raw/0dbafd4ba41100d7d2f50038b9232ceb.png)
>? 
>- 旁路推流的方式默认选择 `指定流旁路` 即可，对于 V2TXLivePusher 两种方式没有区别。
>- 下面以 [跑通 Demo](https://cloud.tencent.com/document/product/454/60985) 中的 `MLVB-API-Example` 工程来演示如何拼接 RTC 推流和拉流的地址。

[](id:step2)
## V2TXLivePusher RTC 推流
[](id:step2_1)
### 1. 配置 MLVB-API-Example 工程文件
1. 根据实际业务下载对应的 [SDK](https://cloud.tencent.com/document/product/454/7873)，这里以 [Professional](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Professional_iOS_latest.zip) 为例。
2. 找到并打开 `LiteAVSDK_Professional_iOS_版本号/MLVB-API-Example-OC/Debug/GenerateTestUserSig.h` 文件。
3. 根据上面  [服务开通](#step1) 设置  [GenerateTestUserSig.](https://github.com/tencentyun/MLVBSDK/blob/master/iOS/MLVB-API-Example/Debug/GenerateTestUserSig.h)  文件中的相关参数：
 - SDKAppID：默认为 0 ，请设置为实际的 SDKAppID。
 - SECRETKEY：默认为空 ，请设置为实际的密钥信息。
 <img src="https://main.qcloudimg.com/raw/861170156910720be7ba980bcb625ceb.png" width=700px>

[](id:step2_2)
### 2. 推流 URL 拼接
[](id:step2_2_1)
#### URL 字段说明
具体的推流 URL 字符串，需要开发者按照下方协议解析中的规则，在工程代码中自行拼接。URL 的示例如下：
```http
trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=A&usersig=xxxxx
```
在上述的 URL 中，存在一些关键字段，关于其中关键字段的含义信息，详见下表：

| 字段名称              | 字段含义                                                     |
| --------------------- | ------------------------------------------------------------ |
| trtc://           | 互动直播推流 URL 的前缀字段                                  |
| cloud.tencent.com | 互动直播特定域名，**请勿修改**                               |
| push              | 标识位，表示推流                                             |
| streamid       | 流 ID，需要由开发者自定义                                            |
| sdkappid      | 对应 [服务开通](#step1) 一节中生成的 SDKAppID |
| userId           | 主播 ID，需要由开发者自定义                                  |
| usersig         | 由 [服务开通](#step1) 一节中获取的密钥计算得出 |

[](id:step2_2_2)
#### Demo 示例代码详解：
- URL 拼接流程，可以参考 [LiveUrl.m#generateTRTCPushUrl()](https://github.com/tencentyun/MLVBSDK/blob/master/iOS/MLVB-API-Example/App/Common/LiveUrl.m) 方法。
```
+ (NSString*)generateTRTCPushUrl:(NSString*)streamId userId:(NSString*)userId {
    NSString *url = [NSString stringWithFormat:@"trtc://cloud.tencent.com/push/%@?sdkappid=%d&amp;userid=%@&amp;usersig=%@&amp;appscene=live",streamId, SDKAppID, userId, [GenerateTestUserSig genTestUserSig:userId]];
    return url;
}
```
- 拼接好 URL 即可开始推流，可以在 MLVB-API-Example 中的 **连麦互动** 或者 **PK互动** 两处基础功能中体验：
	<img src="https://main.qcloudimg.com/raw/088f88d78fff2fea11e24310a53bb2c6.png" width=300>

	这里代码示例以 [LivePkAnchorViewController.m#startPush()](https://github.com/tencentyun/MLVBSDK/blob/master/iOS/MLVB-API-Example/Basic/LivePK/LivePkAnchorViewController.m) 为例：
```objc
// 拼接推流 URL
NSString *url = [LiveUrl generateTRTCPushUrl:self.streamId userId:self.userId];
// 创建⼀个 V2TXLivePusher 对象，并指定模式为 TXLiveMode_RTC；
if (!_livePusher) {
    _livePusher = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTC];
}
[self.livePusher startCamera:true]; 
[self.livePusher startMicrophone]; 
[self.livePusher setRenderView:self.mainView];
// 传⼊推流 URL，即可开始推流；
 V2TXLiveCode code = [self.livePusher startPush:url];
 if (code != V2TXLIVE_OK) {
     [self.livePusher stopMicrophone];
     [self.livePusher stopCamera];
 }
```

[](id:step3)
## V2TXLivePlayer 播放
[](id:step3_1)
### 播放协议选择
- 播放端有以下多种播放协议可供选择，这些协议的 URL 拼接请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。
<table>
<tr><th width="18%">播放协议</th><th width=35%>播放前缀</th><th>备注</th></tr>
<tr>
<td>WebRTC</td>
<td><code>webrtc://</code></td>
<td>强烈推荐，秒开效果最好，支持超高并发</td>
</tr><tr>
<td>HTTP-FLV</td>
<td><code>http://</code>  或  <code>https://</code></td>
<td>推荐，秒开效果好，支持超高并发</td>
</tr><tr>
<td>RTMP</td>
<td><code>rtmp://</code></td>
<td>不推荐，秒开效果差，不支持高并发</td>
</tr><tr>
<td>HLS（m3u8）</td>
<td><code>http://</code> 或 <code>https://</code></td>
<td>手机端和 Mac safari 浏览器推荐的播放协议</td>
</tr></table>
- 对于 RTC 推流来说，还有一种延迟更低的播放协议 `trtc://`，在连麦互动场景下更推荐这种协议。
<table>
<tr><th>播放协议</th><th>播放前缀</th><th>备注</th></tr>
<tr>
<td>RTC</td>
<td><code>trtc://</code></td>
<td>超低延迟播放，互动效果最好</td>
</tr></table>
- `trtc://` 协议的播放 URL 示例如下：
```http
trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=A&usersig=xxxxx
```
在上述的 URL 中，存在一些关键字段，关于其中关键字段的含义信息，详见下表：
<table>
<tr><th>字段名称</th><th>字段含义</th></tr>
<tr>
<td>trtc://</td><td>互动直播推流 URL 的前缀字段</td>
</tr><tr>
<td>cloud.tencent.com</td><td>互动直播特定域名，<strong>请勿修改</strong></td>
</tr><tr>
<td>play</td><td>标识位，表示拉流</td>
</tr><tr>
<td>streamid</td><td>流 ID，对应推流中的 streamid</td>
</tr><tr>
<td>sdkappid</td><td>对应 <a href="#step1">服务开通</a> 一节中生成的 SDKAppID</td>
</tr><tr>
<td>userId</td><td>拉流端的用户 ID</td>
</tr><tr>
<td>usersig</td><td>由 <a href="#step1">服务开通</a> 一节中获取的密钥计算得出</td>
</tr></table>

[](id:step3_2)
### Demo 示例代码详解
- 单击 **基础功能** > **直播拉流**，即可以到直播拉流界面，输入推流端的 streamId 即可观看。
>? 在此之前，请参考 [跑通 Demo](https://cloud.tencent.com/document/product/454/60985) 配置好播放相关的 `PLAY_DOMAIN` 等信息。
<img src="https://main.qcloudimg.com/raw/049435938c2343c4398861f056bf2a35.png" width=400px>
- V2TXLivePlayer 的构造和播放相关的代码请参见[LivePlayViewController.m#startPlay()](https://github.com/tencentyun/MLVBSDK/blob/master/iOS/MLVB-API-Example/Basic/LivePlay/LivePlayViewController.m)。
```
// 随机生成一个 userId
String userId = String.valueOf(new Random().nextInt(10000));
// 根据播放协议生成播放 URL
String playURL = AddressUtils.generatePlayUrl(mStreamId, userId, mStreamType);
mLivePlayer = new V2TXLivePlayerImpl(LivePlayActivity.this);
mLivePlayer.setRenderView(mPlayRenderView);
// 传⼊互动直播播放协议地址，即可开始播放
int result = mLivePlayer.startPlay(playURL);
Log.d(TAG, "startPlay : " + result);
```
其中 URL 的生成可以按照 [LiveUrl.m#generateRtmpPlayUrl()](https://github.com/tencentyun/MLVBSDK/blob/master/iOS/MLVB-API-Example/App/Common/LiveUrl.m) 拼接：
```
// rtmp 协议
+ (NSString*)generateRtmpPlayUrl:(NSString*)streamId {
    NSString *url = [NSString stringWithFormat:@"rtmp://%d.liveplay.myqcloud.com/live/%@",
           BIZID, streamId];
    return url;
}

// trtc 协议
+ (NSString*)generateTRTCPlayUrl:(NSString*)streamId {
    NSString *userId = [NSString generateRandomUserId];
    return [LiveUrl generateTRTCPlayUrl:streamId userId:userId];
}
+ (NSString*)generateTRTCPlayUrl:(NSString*)streamId userId:(NSString*)userId {
    NSString *url = [NSString stringWithFormat:@"trtc://cloud.tencent.com/play/%@?sdkappid=%d&userid=%@&usersig=%@&appscene=live",
                streamId, SDKAppID, userId, [GenerateTestUserSig genTestUserSig:userId]];
    return url;
}

// webrtc 协议
+ (NSString*)generateLebPlayUrl:(NSString*)streamId {
    NSString *url = [NSString stringWithFormat:@"webrtc://%d.liveplay.myqcloud.com/live/%@",
           BIZID, streamId];
    return url;
}
```

[](id:que)
## 常见问题
[](id:que1)
### 1. 为什么使用 `V2TXLivePusher&V2TXLivePlayer` 接口时，同一台设备不支持使用相同 streamid 同时推流和拉流，而 `TXLivePusher&TXLivePlayer` 可以支持？

是的，目前 `V2TXLivePusher&V2TXLivePlayer` 是 [腾讯云 TRTC](https://cloud.tencent.com/document/product/647/45151) 协议实现，其基于 UDP 的超低延时的私有协议暂时还不支持**同一台设备，使用相同的 streamid，一边推超低延时流，一边拉超低延时的流**，同时考虑到用户的使用场景，所以暂时并未支持，后续会酌情考虑此问题的优化。

[](id:que2)
### 2. [**服务开通**](#step1) 章节中生成参数都是什么意思呢？
SDKAppID 用于标识您的应用，UserID 用于标识您的用户，而 UserSig 则是基于前两者计算出的安全签名，它由 **HMAC SHA256** 加密算法计算得出。只要攻击者不能伪造 UserSig，就无法盗用您的云服务流量。UserSig 的计算原理如下图所示，其本质就是对 SDKAppID、UserID、ExpireTime 等关键信息进行了一次哈希加密：
```Cpp
//UserSig 计算公式，其中 secretkey 为计算 usersig 用的加密密钥

usersig = hmacsha256(secretkey, (userid + sdkappid + currtime + expire + 
                                 base64(userid + sdkappid + currtime + expire)))
```

[](id:que3)
### 3. `[livePusher startPush:pushUrl]` 返回错误码：`-5`，代表什么意思？
-5表示由于许可证无效，因此无法调用API，对应的枚举值为：[V2TXLIVE_ERROR_INVALID_LICENSE](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLiveCode__ios.html)，更多错误码请参见 [API 状态码](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLiveCode__ios.html)。

[](id:que4)
### 4. RTC 推流成功后，使用 CDN 拉流一直提示404？
检查一下是否有开启实时音视频服务的旁路直播功能，基本原理是 RTC 协议推流后，如果需要使用 CDN 播放，RTC 会在后台服务中旁路流信息到 CDN 上。
