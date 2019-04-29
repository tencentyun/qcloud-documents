本文将指导您实现房间内的用户如何收发 IM 消息。

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/demo_msg.zip)
## 相关概念
* [群组系统](/document/product/647/16792#.E7.BE.A4.E7.BB.84.E7.B3.BB.E7.BB.9F)

|名称|类|描述|
|--|--|--|
|文本消息|ILVLiveTextMessage|消息内容为一个字符串( String 类型)|
|自定义消息|ILVLiveCustomMessage|消息内容为一个 NSData 对象|
|其它消息|TIMMessage|[ IMSDK 消息类型 ](https://cloud.tencent.com/document/product/269/9232#1.2-.E6.96.87.E6.9C.AC.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81)其它消息的封装|

## 开启IM功能
首先我们得开启IM功能，修改创建和加入房间时的配置属性 imSupport 为YES，即开启了房间内的IM功能。

> 在配置imSupport为YES时，createRoom会自动创建IM群组，quitRoom时创建者会自动解散群组

```objc
option.imOption.imSupport = YES;
```

## 发送消息
房间内成员可以发送实时消息交流互动，这个功能是由 IMSDK 提供的，在 ILiveRoomManager 中对 IMSDK 的接口进行了封装，便于使用，先来看看如何发送消息。

```objc
/**
 发送C2C消息

 @param dstUser 接收方ID
 @param message IM消息
 @param succ    发送成功回调
 @param fail    发送失败回调
 */
- (void)sendC2CMessage:(NSString *)dstUser message:(TIMMessage *)message succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)fail;

/**
 发送在线C2C消息

 @param dstUser 接收方ID
 @param message IM消息
 @param succ 发送成功回调
 @param fail 发送失败回调
 */
- (void)sendOnlineC2CMessage:(NSString *)dstUser message:(TIMMessage *)message succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)fail;

/**
 发送Group消息
 此处发送group，仅限于在当前直播间中发送group消息,或者绑定过IM群组id

 @param message IM消息
 @param succ    发送成功回调
 @param fail    发送失败回调
 */
- (void)sendGroupMessage:(TIMMessage *)message succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)fail;

/**
 发送Group消息

 @param message IM消息
 @param succ 发送成功回调
 @param fail 发送失败回调
 */
- (void)sendOnlineGroupMessage:(TIMMessage *)message succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)fail;
```
> 注释：
> 这里可以看到消息分为群组类型和 C2C 类型（个人发给个人，可以理解为私聊），且分别提供了两种接口，在线消息和非在线消息，它们的区别就是，服务器不会存储在线消息，消息发出时，要是接收者不在线，下次接收者登录后也不会收到发送给自己的在线消息，而非在线消息则会被服务器存储，如果发送时接收者不在线，在他下次登录时会再次发给他。

接口使用起来也比较方便，创建一个想要发送的消息类型对象，然后调用方法即可。
这里以发送一条群组文本消息为例（实时音视频的群组中一般都是此类消息）：

```objc
    // 1. 创建消息对象
    TIMMessage *msg = [[TIMMessage alloc] init];

    // 1.1 设置消息文本
    TIMTextElem *textElem = [[TIMTextElem alloc] init];
    textElem.text = @"Hello ILiveSDK!";
    [msg addElem:textElem];

    // 2. 调用接口发送消息
    [[ILiveRoomManager getInstance] sendGroupMessage:msg succ:^{
        NSLog(@"消息发送成功");
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        NSLog(@"消息发送失败");
    }];
```


## 接收消息
房间内所有的音视频事件都是通过音视频回调方法通知，IM 消息也是一样，房间内所有类型的消息都是通过各自的回调方法通知，只需要设置监听对象，然后实现相应的监听回调方法即可：

```objc
> LiveRoomViewController.m

// 设置IM消息监听
[[[ILiveSDK getInstance] getTIMManager] addMessageListener:self];

// 实现代理协议方法
#pragma mark - TIMMessageListener
/**
 *  新消息回调通知
 *
 *  @param msgs 新消息列表，TIMMessage 类型数组
 */
- (void)onNewMessage:(NSArray*) msgs {
    for (TIMMessage *msg in msgs) {
        TIMConversation *conversation = [msg getConversation];
        int count = [msg elemCount];
        for(int i = 0; i < count; i++) {
            TIMElem *elem = [msg getElem:i];
            if([elem isKindOfClass:[TIMTextElem class]]){
                // 接收到房间内其他成员发出的文本消息
            }
        }
    }
}

```
>注释：
实现细节：在我们调用创建房间或者加入房间的接口时，方法内部会调用 IMSDK 的接口，将用户加入一个 IM 群组（ 即本节名词解释中介绍的实时音视频聊天室 ），用户发送的消息会转发给群组内所有人，也就是同一个房间内的所有人都能收到其他人发出的群组消息（ 自己发出的群组消息自己不会收到 ）。

## UI开发
收发消息时，房间内应该有一个公屏消息列表来展示这些消息，本文 Demo 只是简单实现了一个展示效果，您可以根据自己的需求自己实现。

## 常见问题
- 加入房间失败，错误模块 IMSDK，错误码 10010。
> 这表示要加入的IM群组不存在，需要检测是否先创建了群组(创建房间时传入的配置对象中 imsupport 为 true 时会自动创建群组)，并确认群组类型一致。
