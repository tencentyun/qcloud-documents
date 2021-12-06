## 集成 SDK

本文主要介绍如何快速的将腾讯云 TEduBoard SDK 集成到您的项目中。

## 支持平台

| 操作系统平台  | 浏览器/Webview  | 版本要求  |  备注|
| ------------------------- | -------- | ---------------------- |------- |
| Windows  | Chrome | 50+   |   Win7+   |
| Windows  | IE | 10+ | Win7+    |
| Windows  | Firefox | 50+ | Win7+    |
| Mac  | Chrome | 50+   |   -   |
| Mac  | Safari | 8+ | -    |
| Mac  | Firefox | 50+ | -    |
| iOS          | - | 系统版本 8.1+ | - |
| Android      | - | 系统版本 4.2+ | 推荐使用 Chrome 浏览器，微信浏览器，手机 QQ 浏览器 |

## 集成 TEduBoard SDK

您只需要在您的 Web 页面中添加如下代码即可：

```html
<!-- axios SDK -->
<script src="https://res.qcloudtiw.com/board/third/axios/axios.min.js"></script>
<!-- COS SDK -->
<script src="https://res.qcloudtiw.com/board/third/cos/5.1.0/cos.min.js"></script>
<!-- TEduBoard SDK -->
<script src="https://res.qcloudtiw.com/board/2.6.7/TEduBoard.min.js"></script>
```

如果您需要添加视频文件还需要添加以下代码：
```html
<link href="https://res.qcloudtiw.com/board/third/videojs/1.0.0/video-js.min.css" rel="stylesheet">
<script src="https://res.qcloudtiw.com/board/third/videojs/1.0.0/video.min.js"></script>
```

目前互动白板中依赖 axios、cos，请使用 script:src 的方式加载，这样能够保证在全局访问到 axios 和 cos，不支持 import 的方式。

## 使用 TEduBoard SDK

#### 1. 创建白板控制器

```
var initParams = {
  id: domId, // dom节点id
  classId: classId, // 课堂 ID，32位整型，取值范围[1, 4294967294]
  sdkAppId: sdkAppId, // 整数
  userId: userId, // 字符串
  userSig: userSig, // 字符串
};
var teduBoard = new TEduBoard(initParams);
```

#### 2. 监听白板关键事件

使用 on 监听白板关键事件

- [onTEBError 错误详情](https://cloud.tencent.com/document/product/1137/60716#.E9.94.99.E8.AF.AF.E4.BA.8B.E4.BB.B6)
- [onTEBWarning 警告详情](https://cloud.tencent.com/document/product/1137/60716#.E8.AD.A6.E5.91.8A.E4.BA.8B.E4.BB.B6)

```
// 监听白板错误事件
teduBoard.on(TEduBoard.EVENT.TEB_ERROR, (code, msg) => {

});
```

```
// 监听白板告警事件
teduBoard.on(TEduBoard.EVENT.TEB_WARNING, (code, msg) => {

});
```

#### 3. 白板数据同步

白板在使用过程中，需要在不同的用户之间进行数据同步（涂鸦数据等），SDK 默认使用 IMSDK 作为信令通道，您需要自行实现 IMSDK 的初始化、登录、加入群组操作，确保白板初始化时，IMSDK 已处于所指定的群组内。

监听事件 TEduBoard.EVENT.TEB_SYNCDATA

>!因为 TIM 消息有限频，请将白板消息的优先级设置为最高，以保证白板信令消息不会被丢弃。

```
// 1. 监听操作白板参数的数据，并将回调的数据通过 im 发送到接收者
teduBoard.on(TEduBoard.EVENT.TEB_SYNCDATA, data => {
  let message = this.tim.createCustomMessage({
    to: '课堂号',
    conversationType: window.TIM.TYPES.CONV_GROUP,
    priority: TIM.TYPES.MSG_PRIORITY_HIGH,  // 因为im消息有限频，白板消息的优先级调整为最高
    payload: {
      data: JSON.stringify(data), 
      description: '',
      extension: 'TXWhiteBoardExt' // 固定写法，各端会以extension: 'TXWhiteBoardExt'为标志作为白板信令
    }
  })
  this.tim.sendMessage(message).then(() => {
    // 同步成功
  }, () => {
    // 同步失败
  });
});
```
 - 将收到的数据添加到白板中 addSyncData

```
// 2. 接收者通过监听 im 消息回调，将收到的数据添加到白板中
this.tim.on(window.TIM.EVENT.MESSAGE_RECEIVED, () => {
  let messages = event.data;
  messages.forEach((message) => {
    // 群组消息
    if (message.conversationType === window.TIM.TYPES.CONV_GROUP) {
      if (message.to === '课堂号') { // 如果是当前课堂，这里需要注意一定只能接受当前课堂群组的信令。如果用户加入多个im群组，恰巧这几个群组也在上课，白板信令则会多个课堂错乱，引发互动白板不能同步的异常行为。
        let elements = message.getElements();
        if (elements.length) {
          elements.forEach((element) => {
            if (element.type === 'TIMCustomElem') {
              if (element.content.extension === 'TXWhiteBoardExt') {
                if (message.from != this.userId) {
                  teduBoard.addSyncData(JSON.parse(element.content.data));
                }
              }
            }
          });
        }
      } else {
        // 其他群组消息忽略
      }
    }
  });
}, this)

```
