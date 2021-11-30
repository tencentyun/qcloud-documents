### 旧版 WebIM 的文档如何获取？

1.7.x版本的 WebIM 的文档已从官网下线，可访问 Github 获取 [备份](https://github.com/tencentyun/TIMSDK/tree/master/H5/v1.7.x)。

### 登录时提示 Err_TLS_Third_Sig_Check_Session_Key_Too_Long 是什么原因？

密钥问题导致生成的 UserSig 鉴权失败，请使用正确的 UserSig，生成 UserSig 的具体操作请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)。

###  登录时提示 TypeError: wx.$app.ready is not a function 该怎么处理？
请通过监听事件 [TIM.EVENT.SDK_READY](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.SDK_READY) 代替直接使用 ready 函数，ready 函数已经废弃。

### 登录成功后不能发送消息，提示接口调用时机不合理，该怎么处理？
请监听事件 [TIM.EVENT.SDK_READY](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.SDK_READY)，待 SDK ready 后再调用发送消息等需要鉴权的接口。

###  小程序从哪个版本开始支持发语音消息？

小程序端从2.1.1版本开始支持发语音消息。

### 使用1.7.x版本的 WebIM 无法播放语音消息，该如何解决？

建议使用最新版本的 WebIM，如果短时间内无法升级，请修改旧版本 WebIM 代码：
```
// 旧版 WebIM 代码
Msg.Elem.Sound = function (uuid, second, size, senderId, receiverId, downFlag, chatType, url) {
  this.uuid = uuid; //文件 ID
  this.second = second; //时长，单位：秒
  this.size = size; //大小，单位：字节
  this.senderId = senderId; //发送者
  this.receiverId = receiverId; //接收方 ID
  this.downFlag = downFlag; //下载标志位
  this.busiId = chatType == SESSION_TYPE.C2C ? 2 : 1; //busi_id ( 1：群，2:C2C)
  if (downFlag == 0) {
    this.downUrl = getSoundDownUrl(uuid, senderId, second); //下载地址
  } else if (downFlag == 2 && url != null) {
    this.downUrl = url;
  }
}
```

在 IM 后台返回的消息结构中，当 Download_Flag 值为 0 时，客户端通过 uuid 获取 URL；当 Download_Flag 值为 2 时，客户端可直接使用 URL。

### 2.x版本的 WebIM 怎样拉取历史消息？没有 getC2CHistoryMsgs 接口吗？

2.x版本的 WebIM 没有 getC2CHistoryMsgs 接口，可通过 [getMessageList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getMessageList) 接口拉取历史消息。

### 我想在音视频聊天室实现点赞，送鲜花的功能，该如何操作？

可以通过 [createCustomMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createCustomMessage) 和 [sendMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 接口实现。

### 使用最新版本的 WebIM，终端发送的视频消息在 iOS 浏览器上无法播放，该如何解决？

请升级 [Tuikit](https://cloud.tencent.com/document/product/269/36887) 至4.5.111或更高版本。

### 我的项目用的是 React，发图片消息总是失败，该如何解决？

请升级 SDK 版本至2.0.11或更高版本。

### 新旧 WebIM 消息是互通的吗？

是互通的。如果条件允许，建议使用最新的 WebIM，获得更好的体验和维护。

### 调用 createGroup 接口创建音视频聊天室后无法收到消息，该如何解决？

调用 [createGroup](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createGroup) 接口创建音视频聊天室后，需调用 [joinGroup](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#joinGroup) 接口加入群组（必须带上类型 TIM.TYPES.GRP_AVCHATROOM），才能进行消息收发流程。
```
let promise = tim.joinGroup({ groupID: 'group1', type: TIM.TYPES.GRP_AVCHATROOM });
promise.then(function(imResponse) {
  switch (imResponse.data.status) {
    case TIM.TYPES.JOIN_STATUS_WAIT_APPROVAL:
      break; // 等待管理员同意
    case TIM.TYPES.JOIN_STATUS_SUCCESS: // 加群成功
      console.log(imResponse.data.group); // 加入的群组资料
      break;
    default:
      break;
  }
}).catch(function(imError){
  console.warn('joinGroup error:', imError); // 申请加群失败的相关信息
});
```

### 音视频聊天室怎么没有未读消息计数？为什么拉取不到历史消息？
音视频聊天室不支持未读消息计数，也不支持查看入群前历史消息，更多信息请参见 [群组系统](https://cloud.tencent.com/document/product/269/1502)。

### 可以同时加入两个或多个音视频聊天室吗？

目前不可以。同一用户同时只能加入一个音视频聊天室。
例如，用户已在音视频聊天室 A 中，再加入音视频聊天室 B，SDK 会先退出音视频聊天室 A，然后加入音视频聊天室 B。
更多信息请参见 [joinGroup](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#joinGroup)。

### 获取群列表时，可以同时获取每个群的在线人数等信息吗？目前看只能获取群类型、群名称、群头像等信息。

可以，请升级 SDK 版本至2.1.2或更高版本。更多信息请参见 [getGroupList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getGroupList)。
