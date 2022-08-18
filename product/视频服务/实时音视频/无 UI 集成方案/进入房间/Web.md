本文档主要介绍如何进入 TRTC 房间中，只有在进入音视频房间后，用户才能订阅房间中其他用户的音视频流，或者向房间中的其他用户发布自己的音视频流。
![](https://qcloudimg.tencent-cloud.cn/raw/861153473c6e4679affdb2d24a71f775.png)

在使用 TRTC Web SDK 中，经常会接触到以下对象：
- Client 对象，代表一个本地客户端。[Client](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html) 类的方法提供了进入通话房间、发布本地流、订阅远端流等功能。
- Stream 对象，代表一个音视频流对象，包括本地音视频流对象 [LocalStream](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html) 和远端音视频流对象 [RemoteStream](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/RemoteStream.html)。Stream 类的方法主要提供音视频流对象的行为，包括音频和视频的播放控制。

[](id:step1)
## 步骤1：创建 Client 对象
通过 [TRTC.createClient()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#createClient) 方法创建 [Client](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html) 对象，主要参数如下：

| 参数名称 | 字段含义 | 补充说明 | 数据类型 |填写示例 | 默认值 | 备注 |
|---------|---------|---------|---------|---------|---------|---------|
| mode | 应用场景 | 实时通话模式设置为 `rtc`，该模式适合 1对1 的音视频通话，或者参会人数在 300 人以内的在线会议。<br> 在线直播模式设置为 `live`，该模式适合十万人以内的在线直播场景 | string | rtc | rtc | -|
| sdkAppId | 应用 ID | 您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中找到这个 sdkAppId，如果没有就单击“创建应用”按钮创建一个新的应用。| number | 1400000123 | 无 |必填 |
| userId | 用户 ID | 即用户名，只允许包含大小写英文字母（a-z、A-Z）、数字（0-9）及下划线和连词符。<br> **注意：** TRTC 不支持同一个 userId 在两台不同的设备上同时进入房间，否则会相互干扰。| string | “denny” 或者 “123321”| 无 |必填 |
| userSig | 进房鉴权票据 | 计算方法请参见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275) 。|string| eJyrVareCeYrSy1SslI... | 无 |必填 |
| useStringRoomId | 字符串房间号开关 | 是否使用 string 类型的 roomId。|boolean| true | false | - |

更详细的参数说明参见 [TRTC.createClient()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#createClient)。 

```javascript
// 实时通话模式下创建客户端对象
const client = TRTC.createClient({
  mode: 'rtc',
  sdkAppId,
  userId,
  userSig
});

// 互动直播模式下创建客户端对象
const client = TRTC.createClient({
  mode: 'live',
  sdkAppId,
  userId,
  userSig
});
```

[](id:step2)
## 步骤2：进入音视频通话房间

调用 [Client.join()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html#join) 进入音视频通话房间。主要参数如下：

| 参数名称 | 字段含义 | 补充说明 | 数据类型 |填写示例 | 默认值 | 备注  |
|---------|---------|---------|---------|---------|---------|---------|
| roomId | 房间号 | 默认是 number 类型，如需使用 string 类型的 roomId，请在 createClient() 中设置 useStringRoomId 参数为 true<br> - roomId 为 number 类型时，取值要求为 [1, 4294967294] 的整数;<br> - roomId 为 string 类型时，限制长度为64字节，且仅支持以下范围的字符集： <br> 大小写英文字母（a-zA-Z）; 数字（0-9）; 空格、!、#、$、%、&、(、)、+、-、:、;、<、=、.、>、?、@、[、]、^、_、 {、}、\|、~、, |   number / string  | 3364 或 class-room | 无 | 必填 |
| role | 角色 | 用户角色仅在 `live` 模式才需要设置，目前支持两种角色：`anchor` 主播，`audience` 观众 | string | anchor |  audience | - |

更详细的参数说明参见 [Client.join()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html#join)。 

```javascript
// 使用 Promise 的语法
client
  .join({ roomId })
  .then(() => {
    console.log('进房成功');
  })
  .catch(error => {
    console.error('进房失败，请稍后再试' + error);
  });

// 建议使用 async/await 的语法，实现同样的效果
try {
  await client.join({ roomId });
  console.log('进房成功');
} catch (error) {
  console.error('进房失败，请稍后再试' + error);
}

// 以主播角色进入房间
try {
  await client.join({ 
    roomId,
    role: 'anchor' 
  });
  console.log('进房成功');
} catch (error) {
  console.error('进房失败，请稍后再试' + error);
}
```
