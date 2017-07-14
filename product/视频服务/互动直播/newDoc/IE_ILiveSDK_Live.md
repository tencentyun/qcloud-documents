# 互动消息

iLiveSDK(IE)提供了消息通讯的功能。基于消息通讯可以实现房间内成员的群消息，两个用户之间的C2C消息（不用加好友）。当前SDK只支持发文本消息和自定义消息。

## 发群消息
当前仅支持给当前所在房间发群消息，房间内其他成员都会收到改消息。

```JS
//ILiveMessageElem, ILiveMessage的参数说明详见接口文档
var elem = new ILiveMessageElem(0, "message content");
var elems = [];
elems.push(elem);
var message = new ILiveMessage(elems);
sdk.sendGroupMessage(message, function () {
    alert("send message succ");
}, function (errMsg) {
    alert("错误码:" + errMsg.code + " 错误信息:" + errMsg.desc);
});
```

## 接收群消息
设置群消息监听后可以收到群消息，群消息可以在初始化后设置。

```JS
sdk.setGroupListener(function (msg) {
    //msg的定义详见接口文档
})
```

## 发C2C消息
C2C消息指的是两个用户之间的点对点聊天消息。邀请房间成员上麦等消息可以在业务层通过C2C自定义消息实现。具体的实现可以参考demo。

```JS
//ILiveMessageElem, ILiveMessage的参数说明详见接口文档
var elem = new ILiveMessageElem(0, "message content");
var elems = [];
elems.push(elem);
var message = new ILiveMessage(elems);
sdk.sendC2CMessage("somebody", message, function () {
    alert("send message succ");
}, function (errMsg) {
    alert("错误码:" + errMsg.code + " 错误信息:" + errMsg.desc);
});
```

## 接收C2C消息
设置C2C消息监听后可以收到C2C消息，C2C消息可以在初始化后设置。

```JS
sdk.setC2CListener(function (msg) {
    //msg的定义详见接口文档
})
```


## 连麦互动
上麦行为主要通过修改音视频权限达到。其中上麦流程是

> 切换角色 --> 打开摄像头 -->渲染画面

下麦流程是

> 切换角色 --> 关闭摄像头 -->结束渲染

您可以在控制台[配置场景和角色](https://www.qcloud.com/document/product/268/7599)，然后调用接口切换角色：

```js
//其中liveMaster是控制台配置的角色
sdk.changeRole("LiveMaster");
```
