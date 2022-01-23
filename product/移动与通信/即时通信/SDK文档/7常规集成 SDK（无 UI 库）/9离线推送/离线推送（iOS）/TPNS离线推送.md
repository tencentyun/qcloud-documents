即时通信 IM 的离线推送功能由 [TPNS（Tencent Push Notification Service）](https://cloud.tencent.com/document/product/548/36645)提供，本文向您介绍接入 TPNS 并跑通离线推送功能的详细步骤。

>!
>- 接入 TPNS 需升级 IMSDK 至 [6.0.1975 及以上版本](https://cloud.tencent.com/document/product/269/36887)。
>- 如果 IMSDK 版本是 6.0.1975 以前且没有接入 TPNS 的客户，请参照 [APNS 离线推送](https://cloud.tencent.com/document/product/269/44517) 接入推送功能。
## 接入 TPNS 推送跑通离线推送功能

[](id:step1)
### 步骤一：申请苹果推送证书

离线推送依赖于苹果的原生推送通道，在配置 TPNS 推送之前，需要参照 [推送证书获取指引](https://cloud.tencent.com/document/product/548/36664)  获取苹果推送证书。

[](id:step2)
### 步骤二：TPNS 控制台配置

如果您之前没有在 IM 控制台配置过离线推送信息，请您直接登录到 [TPNS 控制台](https://console.cloud.tencent.com/tpns/product) ，按照下面的步骤配置离线推送信息。

1. 创建产品：进入 **TPNS 控制台** > **产品管理** > **新增产品**, 输入名称和描述等信息。
>!服务接入点的选择：
>- 需要支持海外客户，请选择新加坡/中国香港接入点。
>- 仅支持国内客户，请选择广州/上海接入点。
>
![](https://qcloudimg.tencent-cloud.cn/raw/44b868c7e3781ceed24c5e1e925ab2c3.png)
2. 在基础配置栏，选择新增的产品，输入配置应用的BundleID。
![](https://qcloudimg.tencent-cloud.cn/raw/8ab7746b97b0dea6690ec0bdf8cb7c21.png)
3. 产品创建成功后，得到 TPNS 的 AccessID 和 AsscessKey 等参数。
![](https://qcloudimg.tencent-cloud.cn/raw/1f510d09d97d1eb25fd5f4efc51fc7cc.png)
4. 上传推送证书：进入 **TPNS 控制台** > **选择产品** > **基础配置** > **推送证书** > **上传**，将您在步骤一中申请的苹果推送证书配置到 TPNS。
![](https://qcloudimg.tencent-cloud.cn/raw/f406d41e17ffa726bedb65e2855767ad.png)
5.  第三方服务授权：进入第三方服务授权，把 IM 应用的离线推送功能授权给 TPNS。
  1. 选择云 IM 应用授权，单击**新增授权**。
![](https://qcloudimg.tencent-cloud.cn/raw/5e6aff8a59c09303897fe7fb040f9fd1.png)
  2. 选择要授权绑定的 IM 应用，选择新建的 TPNS 产品应用，提交授权。
<img src="https://qcloudimg.tencent-cloud.cn/raw/8b50ddd0eb4b1e3a734845ffd3046226.png" width=450>

>? 如果您之前已经在 IM 控制台配置了离线推送信息, 我们会自动把这些配置信息迁移到  [TPNS 控制台](https://console.cloud.tencent.com/tpns/product)，您可以登录  [TPNS 控制台](https://console.cloud.tencent.com/tpns/product)修改配置信息。即时通信 IM 会继续使用这些配置信息进行离线推送。
![](https://qcloudimg.tencent-cloud.cn/raw/501fbd5af9d19961827968d608755bf3.png)


[](id:step3)
### 步骤三：TPNS-iOS SDK 接入

参照 TPNS 的 [SDK 接入文档](https://cloud.tencent.com/document/product/548/36663) 在工程中集成 TPNS-iOS SDK，推荐使用 `cocoapods` 集成。

[](id:step4)
### 步骤四：IM 相关接入

可参照 TUIKitDemo 内的 [AppDelegate+Push](https://github.com/tencentyun/TIMSDK/blob/master/iOS/Demo/TUIKitDemo/AppDelegate+Push.h) 以及 [AppDelegate+TPNS](https://github.com/tencentyun/TIMSDK/blob/master/iOS/Demo/TUIKitDemo/AppDelegate+TPNS.m) 文件快速打通 IM 和 TPNS。

1. **初始化推送服务**。初始化 TPNS 推送服务时，需要调用 TPNS 的接口设置：
	-  `- configureClusterDomainName:` 配置接入点，此处的接入点与 [步骤二](#step2) 中创建产品时选择的接入点保持一致。如果创建产品时选择是广州，此设置可以忽略。
	-  `- startXGWithAccessID:accessKey:delegate:` 初始化 TPNS 服务，此处的`tpnsAccessID` 以及 `tpnsAccessKey` 可在 [步骤二](#step2) 中对应产品的控制台获取。
```
- (void)push_init
{
    //打开 debug 开关
#if DEBUG
    [[XGPush defaultManager] setEnableDebug:YES];
#endif
    // 如果 tpns 控制台配置的是广州接入点，此处可忽略
    [[XGPush defaultManager] configureClusterDomainName:@"tpns.hk.tencent.com"];
    [[XGPush defaultManager] startXGWithAccessID:tpnsAccessID accessKey:tpnsAccessKey delegate:self];
    NSLog(@"[PUSH][TPNS] %s", __func__);
}
```
2. **登录时绑定账号**。IMSDK 登录完成之后，需要做两个操作：
	 1. 在 TPNS-iOS SDK 的回调 `- xgPushDidRegisteredDeviceToken:xgToken:error:`中获取 TPNS 注册的 token，并保存。
	 2.  将当前的登录 IM 账号与 TPNS 的推送绑定。
```
/**
@brief 注册推送服务回调
@param deviceToken APNs 生成的 Device Token
@param xgToken TPNS 生成的 Token，推送消息时需要使用此值。TPNS 维护此值与 APNs 的 Device Token 的映射关系
@param error 错误信息，若 error 为 nil 则注册推送服务成功
@note TPNS SDK1.2.6.0+
*/
- (void)xgPushDidRegisteredDeviceToken:(nullable NSString *)deviceToken xgToken:(nullable NSString *)xgToken error:(nullable NSError *)error
{
    NSLog(@"[PUSH][TPNS] %s, deviceToken:%@, xgToken:%@, error:%@", __func__, deviceToken, xgToken, error);
    if (error == nil) {
        // 1. 保存 tpns 的 token
        NSData *data = [xgToken dataUsingEncoding:NSUTF8StringEncoding];
        self.deviceToken = data;
        
        // 2. 登录时注册token并绑定账号
        [self push_registerIfLogined:_currentAccount];
    }
}

// 该方法需要在两个位置调用:
// 1. 在 IMSDK 登录完成之后需要调用该方法
// 2. 在 TPNS 的回调 xgPushDidRegisteredDeviceToken:xgToken:error: 获取到 token 之后
- (void)push_registerIfLogined:(NSString *)userID
{
    NSLog(@"[PUSH] %s, %@", __func__, userID);
    // 1. 上报 token
    if (self.deviceToken) {
        V2TIMAPNSConfig *confg = [[V2TIMAPNSConfig alloc] init];
        // 如果是 TPNS 的话， businessID 无需填写
        confg.businessID = 0;
        // 如果是 TPNS 的话，此处需要上报获取的 TPNS token
        confg.token = self.deviceToken;
        // 标记当前 token 是 TPNS 的 token
        confg.isTPNSToken = YES;
        [[V2TIMManager sharedInstance] setAPNS:confg succ:^{
             NSLog(@"%s, succ, %@", __func__, supportTPNS ? @"TPNS": @"APNS");
        } fail:^(int code, NSString *msg) {
             NSLog(@"%s, fail, %d, %@", __func__, code, msg);
        }];
    }
    
    // 2. 登录后绑定账号
    [XGPushTokenManager.defaultTokenManager upsertAccountsByDict:@{ @(0): userID?:@"" }];
}
```
3. **退出时解绑账号**。在 IMSDK 退出登录之后，需要调用下面的方法解绑 TPNS 推送账号，以免出现退出登录之后还可以收到推送的问题。
```
- (void)push_unregisterIfLogouted
{
    // 解绑账号
    [XGPushTokenManager.defaultTokenManager delAccountsByKeys:[NSSet setWithObject:@(0)]];
    NSLog(@"[PUSH][TPNS] %s", __func__);
}
```
4. **发消息时设置离线推送参数**。
调用 [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a3694cd507a21c7cfdf7dfafdb0959e56) 发送消息时，您可以通过 [V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html) 设置离线推送参数，可以参照 TUIKitDemo 的 [TUIMessageDataProvider](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/DataProvider/TUIMessageDataProvider.m)的 `+ sendMessage:toConversation:isSendPushInfo:isOnlineUserOnly:priority:Progress:SuccBlock:FailBlock:` 方法：
```java
    NSString *userID = conversationData.userID;
    NSString *groupID = conversationData.groupID;
    NSAssert(userID || groupID, @"目标会话至少需要一个");
    NSParameterAssert(message);
    
    V2TIMOfflinePushInfo *pushInfo = nil;
    if (isSendPushInfo) {
        pushInfo = [[V2TIMOfflinePushInfo alloc] init];
        BOOL isGroup = groupID.length > 0;
        NSString *senderId = isGroup ? (groupID) : ([TUILogin getUserID]);
        senderId = senderId?:@"";
        NSString *nickName = isGroup ? (conversationData.title) : ([TUILogin getNickName]?:[TUILogin getUserID]);
        nickName = nickName ?: @"";
        NSDictionary *ext = @{
            @"entity": @{
                    @"action": @1,
                    @"content": [self getDisplayString:message],
                    @"sender": senderId,
                    @"nickname": nickName,
                    @"faceUrl": [TUILogin getFaceUrl]?:@"",
                    @"chatType": isGroup?@(V2TIM_GROUP):@(V2TIM_C2C)
            }
        };
        NSData *data = [NSJSONSerialization dataWithJSONObject:ext options:NSJSONWritingPrettyPrinted error:nil];
        pushInfo.ext = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
        // 兼容 Android oppo 机型字段，此处设置可忽略
        pushInfo.AndroidOPPOChannelID = @"tuikit";
    }
    
    return [V2TIMManager.sharedInstance sendMessage:message
                                           receiver:userID
                                            groupID:groupID
                                           priority:priority
                                     onlineUserOnly:isOnlineUserOnly
                                    offlinePushInfo:pushInfo
                                           progress:progress
                                               succ:succ
                                               fail:fail];
```
5. **解析离线推送的消息**。
接入 TPNS 之后，可以在 TPNS 的回调 `- xgPushDidReceiveNotificationResponse:withCompletionHandler:`  中监听通知栏推送的单击，根据 [步骤四](#step4) 中通过  [V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html)  设置的离线推送格式解析并跳转。可参考 TUIKitDemo 中关于离线推送消息的解析代码。
```
 /// 统一单击回调
/// @param response 如果iOS 10+/macOS 10.14+则为UNNotificationResponse，低于目标版本则为NSDictionary
- (void)xgPushDidReceiveNotificationResponse:(nonnull id)response withCompletionHandler:(nonnull void (^)(void))completionHandler {
    /// code
    NSDictionary *custom = nil;
    if (@available(iOS 10.0, *)) {
        /// iOS10+消息体获取
        if ([response isKindOfClass:UNNotificationResponse.class]) {
            NSDictionary *userInfo = ((UNNotificationResponse *)response).notification.request.content.userInfo;
            if ([userInfo.allKeys containsObject:@"custom"]) {
                NSString *customStr = userInfo[@"custom"];
                custom = [TCUtil jsonSring2Dictionary:customStr];
            }
        }
    } else {
        /// <IOS10消息体获取
        NSLog(@"notification dic: %@", response);
        custom = response;
    }
    
    if (custom == nil || ![custom isKindOfClass:NSDictionary.class]) {
        completionHandler();
        return;
    }
    
    if (![custom.allKeys containsObject:@"entity"]) {
        completionHandler();
        return;
    }
    
    // 响应具体的消息内容
    [self onReceiveOfflinePushEntity:custom[@"entity"]];
    
    completionHandler();
}

- (void)onReceiveOfflinePushEntity:(NSDictionary *)entity
{
    NSLog(@"[PUSH] %s, %@", __func__, entity);
    if (entity == nil ||
        ![entity.allKeys containsObject:@"action"] ||
        ![entity.allKeys containsObject:@"chatType"]) {
        return;
    }
    // 业务，   action : 1 普通文本推送。2 音视频通话推送
    // 聊天类型，chatType : 1 单聊。2 群聊
    NSString *action = entity[@"action"];
    NSString *chatType = entity[@"chatType"];
    if (action == nil || chatType == nil) {
        return;
    }

    // action : 1 普通消息推送
    if ([action intValue] == APNs_Business_NormalMsg) {
        if ([chatType intValue] == 1) {   //C2C
            self.userID = entity[@"sender"];
        } else if ([chatType intValue] == 2) { //Group
            self.groupID = entity[@"sender"];
        }
        if ([[V2TIMManager sharedInstance] getLoginStatus] == V2TIM_STATUS_LOGINED) {
            
            // 响应普通的离线消息，可跳转到对应的聊天页面
            ...
        }
    }
    // action : 2 音视频通话推送
    else if ([action intValue] == APNs_Business_Call) {
        // 单聊中的音视频邀请推送不需处理，APP 启动后，TUIkit 会自动处理
        if ([chatType intValue] == 1) {   //C2C
            return;
        }
        // 内容
        NSDictionary *content = [TCUtil jsonSring2Dictionary:entity[@"content"]];
        if (!content) {
            return;
        }
        UInt64 sendTime = [entity[@"sendTime"] integerValue];
        uint32_t timeout = [content[@"timeout"] intValue];
        UInt64 curTime = [[V2TIMManager sharedInstance] getServerTime];
        if (curTime - sendTime > timeout) {
            [TUITool makeToast:@"通话接收超时"];
            return;
        }
        self.signalingInfo = [[V2TIMSignalingInfo alloc] init];
        self.signalingInfo.actionType = (SignalingActionType)[content[@"action"] intValue];
        self.signalingInfo.inviteID = content[@"call_id"];
        self.signalingInfo.inviter = entity[@"sender"];
        self.signalingInfo.inviteeList = content[@"invited_list"];
        self.signalingInfo.groupID = content[@"group_id"];
        self.signalingInfo.timeout = timeout;
        self.signalingInfo.data = [TCUtil dictionary2JsonStr:@{@"room_id" : content[@"room_id"],
                                                               @"version" : content[@"version"],
                                                               @"call_type" : content[@"call_type"]}];
        if ([[V2TIMManager sharedInstance] getLoginStatus] == V2TIM_STATUS_LOGINED) {
            // 响应群通话的离线消息，可直接打开群通话界面
            ...
        }
    }
}


```



## 常见问题

### 普通消息为什么收不到离线推送？

首先，请检查下 App 的运行环境和证书的环境是否一致，如果不一致，收不到离线推送。

### 自定义消息为什么收不到离线推送？

自定义消息的离线推送和普通消息不太一样，自定义消息的内容我们无法解析，不能确定推送的内容，所以默认不推送，如果您有推送需求，需要您在 [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a3694cd507a21c7cfdf7dfafdb0959e56) 的时候设置 [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html) 的 `desc`字段，推送的时候会默认展示 `desc` 信息。

### 如何关闭离线推送消息的接收？

如果您想关闭离线推送消息的接收，可以通过设置 [setAPNS](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07APNS_08.html#a6aecbdc0edaa311c3e4e0ed3e71495b1) 接口的 `config` 参数为 `nil` 来实现。该功能从5.6.1200版本开始支持。

### 推送的未读角标不正确?
集成 TPNS 推送之后，需要设置 TPNS 离线推送角标，可参考 [AppDelegate+TPNS](https://github.com/tencentyun/TIMSDK/blob/master/iOS/Demo/TUIKitDemo/AppDelegate+TPNS.m) 的 `-onTPNSBadgeChanged:`方法，将本地的角标设置给 TPNS。






