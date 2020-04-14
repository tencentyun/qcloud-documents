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
<script src="https://resources-tiw.qcloudtrtc.com/board/third/axios/axios.min.js"></script>
<!-- COS SDK -->
<script src="https://resources-tiw.qcloudtrtc.com/board/third/cos/5.1.0/cos.min.js"></script>
<!-- TEduBoard SDK -->
<script src="https://resources-tiw.qcloudtrtc.com/board/2.4.6/TEduBoard.min.js"></script>
```

如果您需要添加视频文件还需要添加以下代码：
```html
<link href="https://resources-tiw.qcloudtrtc.com/board/third/videojs/video-js.min.css" rel="stylesheet">
<script src="https://resources-tiw.qcloudtrtc.com/board/third/videojs/video.min.js"></script>
```

## 使用 TEduBoard SDK

#### 1. 创建白板控制器


```
var initParams = {
  id: domId, // dom节点id
  classId: classId, // 整数
  sdkAppId: sdkAppId, // 整数
  userId: userId, // 字符串
  userSig: userSig, // 字符串
};
var teduBoard = new TEduBoard(initParams);
```

#### 2. 白板数据同步

白板在使用过程中，需要在不同的用户之间进行数据同步（涂鸦数据等），SDK 支持两种不同的数据同步模式。

**使用腾讯云 IMSDK 同步数据**

 - 监听事件 TEduBoard.EVENT.TEB_SYNCDATA

```
// 1. 监听操作白板参数的数据，并将回调的数据通过 im 发送到接收者
teduBoard.on(TEduBoard.EVENT.TEB_SYNCDATA, data => {
  let message = this.tim.createCustomMessage({
    to: '课堂号',
    conversationType: window.TIM.TYPES.CONV_GROUP,
    payload: {
      data: JSON.stringify(data), 
      description: '',
      extension: 'TXWhiteBoardExt'
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
      if (message.to === '课堂号') { // 如果是当前群组
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

**使用自定义的数据通道同步数据**

```
teduBoard.on(TEduBoard.EVENT.TEB_SYNCDATA, data => {
  // 通过自定义数据通道同步出去
});

// 在收到其他用户的信息时，将消息传递给 TEduBoard
teduBoard.addSyncData(data);
```

> 以下两种情况，实时录制功能可不可用：
- 实时录制功能在使用腾讯云 IMSDK 同步数据时，自定义消息中的 extension 不等于'TXWhiteBoardExt'时不可用。
- 实时录制功能在自定义数据通道模式下不可用。
