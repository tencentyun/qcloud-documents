视频通话流程图如下：
![trtc demo](https://main.qcloudimg.com/raw/d097f4090d52a73c8ca6c82767b49b3d.png)

1. 通过即时通信 IM SDK 对自定义的通信协议消息体进行发送以及接收处理。
2. 通过 TUIKit 对自定义消息进行展示。
3. 当用户取得进入视频房间条件时，通过实时音视频 TRTC 创建视频房间，开始进行视频通话或视频会议。

## 步骤1：配置工程文件

1. 在 podfile 文件中添加以下内容。
 ```
pod 'TXLiteAVSDK_TRTC'
```
2. 执行以下命令，下载第三方库至当前工程。
```
pod install
```

## 步骤2：开通音视频服务
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片，进入应用的基础配置页面。
2. 单击【开通腾讯实时音视频服务】区域的【立即开通】。
3. 在弹出的开通实时音视频 TRTC 服务对话框中，单击【确认】。
 系统将为您在 [实时音视频控制台](https://console.cloud.tencent.com/trtc) 创建一个与当前 IM 应用相同 SDKAppID 的实时音视频应用，二者帐号与鉴权可复用。

## 步骤3：增加视频聊天功能入口
<ol><li>在 demo ChatViewController ViewDidLoad 中 _chat.moreMenus = moreMenus 之前添加如下代码，绘制入口 UI。
<pre style="padding-top: 24px; padding-bottom: 24px;">
<code>[moreMenus addObject:({
            TUIInputMoreCellData *data = [TUIInputMoreCellData new];
            data.image = [UIImage tk_imageNamed:@"more_video"];
            data.title = <span class="hljs-string">@"视频通话"</span>;
            data;
        })];
</code></pre></li>
<li>在 onSelectMoreCell 回调中处理按钮响应事件。
<pre>
<code>- (void)chatController:(TUIChatController *)chatController onSelectMoreCell:(TUIInputMoreCell *)cell
{
    if ([cell.data.title isEqualToString:<span class="hljs-string">@"视频通话"</span>]) {
        [[VideoCallManager shareInstance] setConversationData:self.conversationData];
        [[VideoCallManager shareInstance] videoCall:chatController];
    }
}
</code></pre></li></ol>


## 步骤4：增加通信逻辑和消息展示效果
[Demo](https://github.com/tencentyun/TIMSDK) 的 Chat/VideoCall 文件夹中已包含音视频通信协议和消息渲染处理代码，您可以直接引用，也可以自定义一套音视频通话协议、消息体结构等，以便满足发起视频请求、用户接受或者拒绝、以及用户不在线超时等需求。

本文以直接引用 Demo 中提供的音视频通信协议和消息渲染处理代码为例。

1. 将 Demo 中的 Chat/VideoCall 文件夹拷贝到当前项目工程中。

```
typedef NS_ENUM(UInt32, videoCallState)
{
    //UserA 向 UserB 发起通话请求
		
    VIDEOCALL_REQUESTING = 0,         //请求发起
    VIDEOCALL_USER_CANCEL,            //用户取消 [UserA 在 UserB 未回应时主动取消视频请求](UserA 展示：用户取消 UserB 展示：未接听)
    VIDEOCALL_USER_REJECT,            //用户拒绝 [UserB 拒绝通话](UserA 展示：对方已拒绝 UserB 展示：未接听)
    VIDEOCALL_USER_NO_RESP,           //用户未应答 [UserB 超时未回复](UserA 展示：对方未应答 UserB 展示：未接听) 
    VIDEOCALL_USER_CONNECTTING,       //用户同意并进行连接 [UserB 接受通话](UserA 执行：enterRoom UserB 执行：enterRoom)
    VIDEOCALL_USER_HANUGUP,           //用户挂断 [UserA or UserB 挂断通话](UserA 展示：已结束 UserB 展示：已结束)
    VIDEOCALL_USER_ONCALLING          //用户通话中 [UserB 通话中](UserA 展示：对方通话中 UserB 展示：未接听)
};

public class videoCallMessageData {
    int version = 2;                //消息标识符
    requestUser = "xxxx";           //视频发起用户
    roomID = 938283919212;          //视频房间号
    videoState = 5;                 //视频通话状态
    duration = 20;                  //视频通话时长
}
```

2. 在 **ConversationController** 中注册监听 **TUIKitNotification_TIMMessageListener** 消息，监听新消息通知，并筛选出视频会话消息进行处理。

```
[[NSNotificationCenter defaultCenter] addObserver:self
    selector:@selector(onNewMessageNotification:) name:TUIKitNotification_TIMMessageListener object:nil];

- (void)onNewMessageNotification:(NSNotification *)no
{
    NSArray<TIMMessage *> *msgs = no.object;
    for (TIMMessage *msg in msgs) {
        
        TIMElem *elem = [msg getElem:0];
        if ([elem isKindOfClass:[TIMCustomElem class]]) {
            TIMCustomElem *custom = (TIMCustomElem *)elem;
            NSDictionary *param = [TCUtil jsonData2Dictionary:[custom data]];
            if (param != nil && [param[@"version"] integerValue] == 2) {
                [[VideoCallManager shareInstance] onNewVideoCallMessage:msg];
            }
        }
    }
}
```

3. 渲染自定义消息。

```
- (TUIMessageCell *)chatController:(TUIChatController *)controller onShowMessageData:(TUIMessageCellData *)cellData {
    if ([data isKindOfClass:[VideoCallCellData class]]) {
        UInt32 state = [(VideoCallCellData *)data videoState];
        if (state == VIDEOCALL_REQUESTING || state == VIDEOCALL_USER_CONNECTTING) {
            return nil;
        } else {
            VideoCallCell *videoCallCell = [[VideoCallCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:@"VideoCell"];
            [videoCallCell fillWithData:(VideoCallCellData *)data];
            @weakify(self);
            @weakify(controller);
            [videoCallCell setVidelClick:^{
                @strongify(self);
                @strongify(controller);
                [[VideoCallManager shareInstance] setConversationData:self.conversationData];
                [[VideoCallManager shareInstance] videoCall:controller];
            }];
            return videoCallCell;
        }
    }
    return nil;
}
```

>?如果不处理自定义消息，则该消息默认不渲染。

## 步骤5：进入视频房间
 [Demo](https://github.com/tencentyun/TIMSDK) 中的 Chat/Meeting 文件夹中已包含视频房间进入/退出逻辑，您可以直接拷贝到当前项目工程中。

进入视频房间示例代码如下，更多详情请参见 [TRTCParams 配置](http://doc.qcloudtrtc.com/group__TRTCCloudDef__ios.html#interfaceTRTCParams)。

```
- (void)_enterMeetingRoom {
    // TRTC相关参数设置
    TRTCParams *param = [[TRTCParams alloc] init];
    param.sdkAppId = sdkAppid;
    param.userId = [self currentUserIdentifier];                         //当前用户的 ID
    param.roomId = self.currentRoomID;                                   //用户可通过服务器生成唯一 ID，Demo 仅为示例随机生成
    param.userSig = [self genTestUserSig:[self currentUserIdentifier]];  //实时音视频应用的 UserSig
    param.privateMapKey = @"";

    [[TRTCCloud sharedInstance] setDelegate:self];
    [[TRTCCloud sharedInstance] enterRoom:param appScene:(TRTCAppSceneVideoCall)];
    [[TRTCCloud sharedInstance] startLocalPreview:YES view:self.localVideoView];
}
```
>!`param.userSig`参数需设置为当前实时音视频应用 SDKAppID 所对应的 UserSig。若实时音视频 SDKAppID 与即时通信 SDKAppID 一致，可直接复用 UserSig，否则请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275) 生成实时音视频 SDKAppID 对应的 UserSig 再进行鉴权。
 
退出视频房间示例代码如下：

```
-(void)_quitMeetingRoom {
    [self setRoomStatus:TRTC_IDLE];
    [[TRTCCloud sharedInstance] stopLocalPreview];
    [[TRTCCloud sharedInstance] exitRoom];
}
```

更多关于 TRTC 回调，设置渲染页面等完整逻辑，请参见 [Demo](https://github.com/tencentyun/TIMSDK) Chat/Meeting/**VideoCallManager+videoMeeting.h**文件。


## 常见问题
**1. 若已分别创建实时音视频 SDKAppID 和即时通信 SDKAppID，现需要同时集成 IM SDK 和 TRTC SDK，需要注意什么?**

 若已分别创建实时音视频 SDKAppID 和即时通信 SDKAppID，即 SDKAppID 不一致场景，则二者帐号与鉴权不可复用，您需要生成实时音视频 SDKAppID 对应的 UserSig 进行鉴权。生成 UserSig 的具体操作请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。
