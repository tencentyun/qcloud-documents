游戏 SDK 增加了 3 个新的 API，分别为：添加表情包到 QQ、设置资料卡名片以及样式，和发送公众号消息给指定 QQ 好友。

## 添加表情包到 QQ

下面是添加表情包到 QQ 的示例代码：
```
(void)onAddQQEmoji:(UIButton *)sender {
    NSString *emojiID = @”1234”;
    [_oauth addQQEmoji:emojiID];
}
```
这里的 emojiID 是表情包的 ID，详情请咨询游戏 SDK 的开发。 调用此接口后，TencentOAuth 对象的 delegate 会收到一个回调：
```
(void)tencentOAuth:(TencentOAuth *)tencentOAuth didCompleteAddQQEmojiWithError:(NSError *)error serverResponse:(NSDictionary * _Nullable)response
```

如果请求出现错误，这里的 error 对象描述了错误原因以及错误码等信息。
response 表示服务器返回的数据，如果是因为网络原因或者参数错误导致请求没有发出，则 response 可能为空。response 的示例如下：
```
{
    "ret":0,        //中转cgi返回码
    "msg":"ok",     //中转cgi返回信息
    "data": 
    {
        "ret":0,      //0-成功，其他-失败
        "msg":"xx",   //错误描述，活动类型表情鉴权失败时，该值表示活动描述
        "data":{"url":""}
    }
}
```
当出现错误时，调用方可以参考 response 中的 msg 以及 ret 字段来检查错误原因。

## 设置资料卡名片和样式
下面是设置手机 QQ 资料卡的名片和样式的示例代码：
```
(void)onSetSummaryCard:( UIButton *)sender {
　　NSString *cardID = @”1234”;
　　NSString *styleID = @”2414”;
    [_oauth setQQSummaryCardID:cardID styleID:styleID];
}
```
调用接口之后，TencentOAuth 对象的 delegate 会收到一个回调：
```
(void)tencentOAuth:(TencentOAuth *)tencentOAuth didCompleteSetQQSummaryCardWithError:(NSError *)error serverResponse:(NSDictionary * _Nullable)response
```

## 发送公众号消息给 QQ 好友
下面是发送公众号消息给指定好友的示例代码：
```
(void)onSendPublicAccountMessage:( UIButton *)sender {
　　NSString * openIDS = @” [{\"type\":0,\"openid\":\"962f1d0f4cfcdc2981c51bcc0a630057\"}]”;
　　NSString * openIDS = @” MSG_SHARE_FRIEND_DOUBLE”;
　　NSString * previewURL = [NSURL URLWithString:@” https://egame.gtimg.cn/club/pgg/v2.0/img/index/icon.png”];
　　NSString * redirectingURL = [NSURL URLWithString: @” https://egame.qq.com/”];
　　 [_oauth sendPublicAccountMessageToQQOpenIDs:openIDS withMessageTag:messageTag WithPreviewImageURL:previewURL andRedirectingURL:redirectingURL];
}
```
调用接口之后，TencentOAuth 对象的 delegate 会收到一个回调：
```
(void)tencentOAuth:(TencentOAuth *)tencentOAuth didCompleteSendPublicAccountMessageWithError:(NSError *)error serverResponse:(NSDictionary * _Nullable)response
```
>**注意：**
>调用此接口必须确保对方已经是自己的好友，而且关注了公众号，否则对方会收不到消息。