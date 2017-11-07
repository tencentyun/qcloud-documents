
## 功能描述
分享到 QQ 空间的接口用于取代旧版本的分享接口 addShareWithParams（该接口已被废弃）。

在用户安装了手机 QQ（4.6 版本以上）时通过手机 QQ 中的 QZone 结合版进行分享，否则调用浏览器页面进行分享。其中文本消息，图文消息和音频消息的 title 是必须填写的，summary 可以不填。使用分享到 QQ 空间功能需要设置 QQ 业务回调，请参考处理 [处理 QQ 业务的回调](https://cloud.tencent.com/document/product/630/11887)。

在分享到 QQ 好友和 QQ 空间的时候，根据是本地分享还是浏览器分享的不同，支持分享的消息类型也不同。因为 webQQ 好友分享和 webQQ 空间的分享都不支持非 URL 类型的分享，所以这里建议在分享到 QQ 好友或者 QQ 空间的时候尽量避免这两种类型的调用，避免发生不支持的错误。下表列举了在不同应用中，不同消息类型是否被支持分享。


| 分享消息类型 | QQ好友 | QQ空间 |web QQ好友|web QQ空间|
|---------|---------|---------|
| QQApiTextObject | 支持 | 不支持 |不支持|不支持|
| QQApiImageObject | 支持 | 不支持 |不支持|不支持|
| QQApiNewsObject | 支持 | 支持 |支持|支持|
| QQApiAudioObject | 支持 | 支持 |支持|支持|
| QQApiVideoObject | 支持 | 支持 |支持|支持|
| QQApiGroupTribeImageObject | 仅群部落 | 不支持 |不支持|不支持|
| QQApiAddFriendObject | 游戏好友 | 不支持 |不支持|不支持|
| QQApiFileObject | 仅数据线 | 不支持 |不支持|不支持|
|QQApiGameConsortiumBindingGroupObject | 仅群部落 | 不支持 |不支持|不支持|

## 方法原型

```
/**
 向手Q QZone结合版发起分享请求
 \note H5分享只支持单张网络图片的传递
 \param req 分享内容的请求
 \return 请求发送结果码
 */
+ (QQApiSendResultCode)SendReqToQZone:(QQBaseReq *)req;
```

## 参数说明 

|参数名 | 必选 | 类型 |参数说明|
|---------|---------|---------|
| req | 必选| QQBaseReq * |分享内容的请求|
