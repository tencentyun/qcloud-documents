本文档主要介绍如何进入 TRTC 房间中，只有在进入音视频房间后，用户才能订阅房间中其他用户的音视频流，或者向房间中的其他用户发布自己的音视频流。

## 调用指引
[](id:step1)
### 步骤1：导入 SDK 并设置 App 权限
请参考文档 [导入 SDK 到项目中](https://cloud.tencent.com/document/product/647/73371) 完成 SDK 的导入工作。

[](id:step2)
### 步骤2：创建 SDK 实例并设置事件监听器
创建 TRTC 的对象实例。
```javascript
import TrtcCloud from "@/TrtcCloud/lib/index";
this.trtcCloud = TrtcCloud.createInstance();
```

[](id:step3)
### 步骤3：监听 SDK 的事件
```javascript
this.trtcCloud.on('onWarning', (res) => {
	console.log('- onWarning: ', JSON.stringify(res));
});
this.trtcCloud.on('onError', (res) => {
	console.log('- onError: ', JSON.stringify(res));
});
```

[](id:step4)
### 步骤4：准备进房参数 TRTCParams
在调用 [enterRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#enterRoom) 接口时需要填写两个关键参数，即 `TRTCParams` 和 `TRTCAppScene`，接下来进行详细介绍：

#### 参数一：TRTCAppScene
该参数用于指定您的应用场景，即**在线直播**还是**实时通话**：
- **实时通话：**
包含 `TRTCAppSceneVideoCall` 和 `TRTCAppSceneAudioCall` 两个可选项，分别是视频通话和语音通话，该模式适合 1对1 的音视频通话，或者参会人数在 300 人以内的在线会议。
- **在线直播：**
包含 `TRTCAppSceneLIVE` 和 `TRTCAppSceneVoiceChatRoom` 两个可选项，分别是视频直播和语音直播，该模式适合十万人以内的在线直播场景，但需要您在接下来介绍的 TRTCParams 参数中指定 **角色(role)** 这个字段，也就是将房间中的用户区分为 **主播(anchor)** 和 **观众(audience)** 两种不同的角色。

#### 参数二：TRTCParams
TRTCParams 由很多的字段构成，但通常您只需要关心如下几个字段的填写：

| 参数名称  | 字段含义     | 补充说明  | 数据类型 | 填写示例                           |
| --------- | ------------ | ------------ | -------- | ---------------------------------- |
| sdkAppId  | 应用 ID      | 您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中找到这个 SDKAppID，如果没有就单击“创建应用”按钮创建一个新的应用。      | 数字     | 1400000123                         |
| userId    | 用户 ID      | 即用户名，只允许包含大小写英文字母（a-z、A-Z）、数字（0-9）及下划线和连词符。注意 TRTC 不支持同一个 userId 在两台不同的设备上同时进入房间，否则会相互干扰。 | 字符串   | “denny” 或者 “123321”              |
| userSig   | 进房鉴权票据 | 您可以使用 sdkAppId 和 userId 计算出 userSig，计算方法请参见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275) 。              | 字符串   | eJyrVareCeYrSy1SslI...             |
| roomId    | 房间号       | 数字类型的房间号。注意如果您想使用字符串类型的房间号，请使用 **strRoomId** 字段，而不要使用 roomId 字段，因为 strRoomId 和 roomId 不可以混用。              | 数字     | 29834                              |
| strRoomId | 房间号       | 字符串类型的房间号。注意 strRoomId 和 roomId 不可以混用，“123” 和 123 在 TRTC 后台服务看来并不是同一个房间。                                                | 数字     | 29834                              |
| role      | 角色         | 分为“主播”和“观众”两种角色，只有当 TRTCAppScene 被指定为 `TRTCAppSceneLIVE` 或 `TRTCAppSceneVoiceChatRoom` 这两种直播场景时才需要指定该字段。               | 枚举值   | TRTCRoleAnchor 或 TRTCRoleAudience |

>!
>- TRTC 不支持同一个 userId 在两台不同的设备上同时进入房间，否则会相互干扰。
>- 每个端在应用场景 appScene 上必须要进行统一，否则会出现一些不可预料的问题。


[](id:step5)
### 步骤5：进入房间（enterRoom）
在准备好 [步骤4](#step4) 中两个参数（TRTCAppScene 和 TRTCParams）后，就可以调用 [enterRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#enterRoom) 接口函数进入房间了。

```javascript
import TrtcCloud from '@/TrtcCloud/lib/index';
import { TRTCAppScene, TRTCRoleType } from '@/TrtcCloud/lib/TrtcDefines';

this.trtcCloud = TrtcCloud.createInstance();

// 组装 TRTC 进房参数，请将 TRTCParams 中的各字段都替换成您自己的参数
// Please replace each field in TRTCParams with your own parameters
const params = {
	sdkAppId: 1400000123;  // Please replace with your own sdkAppId
	userId: "denny";       // Please replace with your own userid
	roomId: 123321;       // Please replace with your own room number 
	userSig: "xxx";       // Please replace with your own userSig
	role: TRTCRoleType.TRTCRoleAnchor;
};

// 如果您的场景是“在线直播”，请将应用场景设置为 TRTC_APP_SCENE_LIVE
// If your application scenario is a video call between several people, please use "TRTC_APP_SCENE_LIVE"
this.trtcCloud.enterRoom(params, TRTCAppScene.TRTCAppSceneVideoCall);   
```

**事件回调**
如果进入房间成功，SDK 会回调 [onEnterRoom(result)](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onEnterRoom) 事件，其中 `result` 会是一个大于 0 的数值，代表加入房间所消耗的时间，单位为毫秒（ms）。
如果进入房间失败，SDK 同样会回调 [onEnterRoom(result)](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onEnterRoom) 事件，但参数 `result` 会是一个负数，其数值为进房失败的错误码。
```javascript
import TrtcCloud from '@/TrtcCloud/lib/index';
this.trtcCloud = TrtcCloud.createInstance();

// 监听 SDK 的 onEnterRoom 事件并获知是否成功进入房间
// Listen to the onEnterRoom event of the SDK and learn whether the room is successfully entered
this.trtcCloud.on("onEnterRoom", (result) => {
	if (result > 0) {
		console.log(`进房成功，耗时: ${result}ms`);
	}
});
```
