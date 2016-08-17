## 1. 未读消息

未读消息是指用户没有读过的消息（而非对方是否已经阅读，这种情况需要回执才能实现，目前ImSDK没有此功能。），TIMMessage 方法 isReaded 标识消息是否已读，要想显示正确的未读计数，需要开发者显示调用已读上报，告诉app某条消息是否已读，例如，当用户进入聊天界面，可以设置整个会话的消息已读。对于聊天室，Server不保存未读计数，每次登录后跟Server同步未读计数后将会清零。

```
@interface TIMMessage : NSObject

/**
 *  是否已读
 *
 *  @return TRUE 已读  FALSE 未读
 */
-(BOOL) isReaded;

@end
```

## 2. 获取当前未读消息数量

可通过 TIMConversation 的 getUnReadMessageNum 方法获取当前会话中未读消息的数量，对于聊天室，Server不保存未读计数，每次登录后跟Server同步未读计数后将会清零。： 

**原型： **

```
@interface TIMConversation : NSObject

-(int) getUnReadMessageNum;

@end
```
**示例：**

```
TIMConversation * conversation = [[TIMManager sharedInstance] getConversation:TIM_C2C receiver:@"iOS_002"];

[conversation getUnReadMessageNum]; 
```

## 3. 已读上报 

当用户阅读某个会话的数据后，需要进行会话消息的已读上报，SDK根据会话中最后一条阅读的消息，设置会话中之前所有消息为已读。 

**原型： **

```
@interface TIMConversation : NSObject

-(int) setReadMessage: (TIMMessage*)readed;
-(int) setReadMessage;

@end
```
**参数说明：**

参数|说明
---|---
readed | 为当前会话中最后一条读过的消息；ImSDK会把比readed时间更早的消息标记为已读消息。

无参数的版本设置一个会话中所有消息为已读状态，对于单聊会话，无参数版本性能要高很多，大多数情况下使用无参数版本即可。

** 示例1：**

```
TIMConversation * conversation = [[TIMManager sharedInstance] getConversation:TIM_C2C receiver:@"iOS_002"];
    
TIMMessage * msg = [[TIMMessage alloc] init];
[conversation setReadMessage:msg];
```

此示例设置C2C会话内的所有消息为已读。 

**示例2：**

```
TIMConversation * conversation = [[TIMManager sharedInstance] getConversation:TIM_GROUP receiver:@"TGID1JYSZEAEQ"];
    
[conversation setReadMessage];
```

此示例设置群组@"TGID1JYSZEAEQ"内所有消息为已读，C2C和群组设置已读用法相同，区别在于会话类型。

## 4. 禁用自动上报

在 1.9 以上版本引入的方法，在单终端情况下，默认设置可以满足需求，出于性能考虑，未读消息由SDK拉回到本地，Server默认会删除未读消息，切换终端以后无法看到之前终端已经拉回的未读消息，如果仅在一个终端，未读计数没有问题。如果需要多终端情况下仍然会有未读，可以禁用自动上报，IM通讯云不会代替用户已读上报，**一旦禁用自动上报，需要开发者显式调用setReadMessage**。

```
@interface TIMManager : NSObject

/**
 *  禁止未读自动上报，默认启用
 */
-(void) disableAutoReport;

@end
```

在 TIMManager 初始化之前禁用自动已读即可生效。

## 5. 多终端已读同步

在2.0以上版本中引入的功能，在多终端情况下，未读消息计数由Server下发同步通知，SDK在本地更新未读计数后，通知用户更新会话。

**原型：**

```
@protocol TIMRefreshListener <NSObject>
@optional
/**
 *  刷新部分会话（包括多终端已读上报同步）
 *
 *  @param conversations 会话（TIMConversation*）列表
 */
- (void) onRefreshConversations:(NSArray*)conversations;
@end

@interface TIMManager : NSObject

-(int) setRefreshListener: (id<TIMRefreshListener>)listener;

@end
```

在 TIMManager 登录之前设置即可生效。