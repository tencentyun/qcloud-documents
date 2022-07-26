本文档主要介绍主播如何发布自己的音视频流，所谓“发布”，也就是打开麦克风和摄像头，让自己的声音和视频能够被房间中其他用户听到和看到的意思。

![](https://qcloudimg.tencent-cloud.cn/raw/b887b390411aef1396bd593ccdd9eb0e.png)

在使用 TRTC Web SDK 中，经常会接触到以下对象：
- Client 对象，代表一个本地客户端。[Client](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html) 类的方法提供了加入通话房间、发布本地流、订阅远端流等功能。
- Stream 对象，代表一个音视频流对象，包括本地音视频流对象 [LocalStream](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html) 和远端音视频流对象 [RemoteStream](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/RemoteStream.html)。Stream 类的方法主要提供音视频流对象的行为，包括音频和视频的播放控制。

[](id:step1)
## 步骤1：完成前序步骤
可以参考文档 [进入房间](https://cloud.tencent.com/document/product/647/74636)，创建 Client 并进入房间，为接下来发布音视频流做准备。


[](id:step2)
## 步骤2：创建本地流
使用 [TRTC.createStream()](https://web.sdk.qcloud.com/trtc/webrtc/doc/en/TRTC.html#createStream) 方法创建本地音视频流，参数设置如下：

| 参数名称 | 字段含义 | 补充说明 | 数据类型 |填写示例 | 默认值 | 备注 | 
|---------|---------|---------|---------|---------|---------|---------|
| userId | 用户 ID | 即用户名，与创建的 Client 的 userId 保持一致 | string | “denny” 或者 “123321”| 无 | **必填** |
| audio | 是否采集音频 | 选择是否通过麦克风采集音频 | boolean | true |  无 |**必填** |
| video | 是否采集视频 | 选择是否通过摄像头采集视频 | boolean | true |  无 |**必填** |

更详细的参数说明参见 [TRTC.createStream()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#createStream)。 

```javascript
const localStream = TRTC.createStream({ userId, audio: true, video: true });
```

在发布之前需要调用 [LocalStream.initialize()](https://web.sdk.qcloud.com/trtc/webrtc/doc/en/LocalStream.html#initialize) 初始化本地音视频流。
需要注意的是，在初始化过程中，会通过浏览器获取摄像头和麦克风的使用权限，需要您授权允许使用设备，浏览器弹出的对话框如下。

![](https://main.qcloudimg.com/raw/1a2c1e7036720b11f921f8ee1829762a.png)
![](https://qcloudimg.tencent-cloud.cn/raw/f72b0f28f57ba15c9c42f7b1921a1b8f.png)

在初始化成功的回调中，通过调用 [LocalStream.play()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html#play) 方法可以在页面中预览播放本地音视频。

```javascript
// 使用 Promise 的语法
localStream
  .initialize()
  .then(() => {
    console.log('初始化本地流成功');
    localStream.play('local_stream');
  })
  .catch(error => {
    console.error('初始化本地流失败 ' + error);
  });

// 建议使用 async/await 的语法，实现同样的效果
try {
  await localStream.initialize();
  localStream.play('local_stream');
  console.log('初始化本地流成功');
} catch (error) {
  console.error('初始化本地流失败 ' + error);
}
```


[](id:step3)
## 步骤3：发布本地流
在本地流初始化成功后，调用 [Client.publish()](https://web.sdk.qcloud.com/trtc/webrtc/doc/en/Client.html#publish) 方法发布本地流。
```javascript
// 使用 Promise 的语法
client
  .publish(localStream)
  .then(() => {
    console.log('本地流发布成功');
  })
  .catch(error => {
    console.error('本地流发布失败 ' + error);
  });

// 建议使用 async/await 的语法，实现同样的效果
try {
  await client.publish(localStream);
  console.log('本地流发布成功');
} catch (error) {
  console.error('本地流发布失败 ' + error);
}
```

## 完整代码
```javascript
const client = TRTC.createClient({
  mode: 'rtc',
  sdkAppId,
  userId,
  userSig
});
const localStream = TRTC.createStream({ userId, audio: true, video: true });

try {
  await client.join({ roomId });
  console.log('进房成功');
} catch (error) {
  console.error('进房失败，请稍后再试' + error);
}

try {
  await localStream.initialize();
  localStream.play('local_stream');
  console.log('初始化本地流成功');
} catch (error) {
  console.error('初始化本地流失败 ' + error);
}

try {
  await client.publish(localStream);
  console.log('本地流发布成功');
} catch (error) {
  console.error('本地流发布失败 ' + error);
}
```
