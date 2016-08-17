
## 1. 设置通信模式 

设置接入模式(可选) 调用init初始化前, 可使用此接口指定接入模式。SDK支持两种连接模式： 

* IM模式 
* 只登陆模式 

当用户需要使用IM功能时，例如收发C2C消息，群组消息等相关IM功能，需要设置SDK使用IM模式。当用户不需要IM功能，只需要登入登出功能时，可设置连接模式为只登陆模式
 
**原型：**

```
	/**
	Description:	设置接入模式
	@param	[in]	mode	1 – IM连接模式 / 0或不调用此接口 – 只登陆模式 
	@return			void
	@exception      none
	*/
	TIM_DECL void	TIMSetMode(int mode);
```

**示例：**

```
TIMSetMode (1); //设置为IM连接模式
```

## 2. 设置日志等文件路径（可选） 

设置SDK日志和其他SDK所写文件的生成路径。 调用init初始化前, 可使用此接口指定SDK日志文件路径。当SDK运行时，如写文件失败会导致部分功能异常，所以用户在某些特定不可写环境运行SDK时，需先设置此路径为可写目录。
如果不设置，则默认为当前路径（workspace） 

**原型：**

```
	/**
	Description:	设置SDK日志和其他SDK所写文件的生成路径
	@param	[in]	path	路径
	@return			void
	@exception      none
	*/
	TIM_DECL void	TIMSetPath(const char* path);
```

**示例：**

```
TIMSetPath("./"); //设置SDK日志文件为当前路径
```
## 3. 设置日志级别

ImSDK内部日志级别可通过TIMSetLogLevell进行修改，控制ImSDK的日志输出。

**原型：**

```
enum TIMLogLevel
{
	klogNone = 0,
	kLogError,
	kLogWarn,
	kLogInfo,
	kLogDebug
};
	
TIM_DECL void	TIMSetLogLevel(TIMLogLevel level);
```

可以通过设置日志级别为klogNoneE来关闭ImSDK的日志输出，提升性能，建议在开发期间打开日志，方便排查问题。

## 4. 新消息通知 

在多数情况下，用户需要感知新消息的通知，这时只需注册新消息通知回调。在用户登录状态下，会拉取离线消息，为了不漏掉消息通知，需要在登录之前注册新消息通知。 

**原型：**

```
typedef void* TIMMessageHandle;
typedef void (*CBOnNewMessage) (TIMMessageHandle* handles, uint32_t msg_num, void* data);
typedef struct _TIMMessageCB_C
{
	CBOnNewMessage OnNewMessage;
	void* data;
}TIMMessageCB;
```
回调消息内容通过参数TIMMessageHandle传递，通过TIMMessageHandle可以获取消息和相关会话的详细信息，如消息文本，语音数据，图片等等，可参阅（消息解析）部分。
 
**示例：**

```
void CBOnNewMessageImp(TIMMessageHandle* handles, uint32_t msg_num, void* data)
{
	const uint32_t MAX_TXT_LEN = 100;
	static int msg_count = 0;
	static char buffer[MAX_TXT_LEN] = {};
	for (int msg_idx = 0; msg_idx < msg_num; msg_idx++)
	{
		printf("new message %d\n", msg_count++);
		TIMMessageHandle handle = handles[msg_idx];
		TIMConversationHandle conv = CreateConversation();
		GetConversationFromMsg(conv, handle);
		for (int i = 0; i < GetElemCount(handle); i++)
		{
			auto elem = GetElem(handle, i);
			auto type = GetElemType(elem);
			printf("type = <%d>\n", type);
			if (type == kElemText)
			{
				auto len = MAX_TXT_LEN; GetContent(elem, buffer, &len); printf("text msg:%s", buffer);
			}
		}
		DestroyConversation(conv);
	}
}
//设置消息监听器，收到新消息时，通过此监听器回调
void SetNewMsgCallBack()
{
	static TIMMessageCB callback;
	callback.OnNewMessage = CBOnNewMessageImp;
	TIMSetMessageCallBack(&callback);
}
```
示例中设置消息回调通知，并且在有新消息时直接打印消息，更详细的消息解析，可参阅（消息解析）部分。 

## 5. 网络事件通知 

可选设置，如果要用户感知是否已经连接服务器，需要设置此回调，用于通知调用者跟通讯后台链接的连接和断开事件，另外，如果断开网络，等网络恢复后会自动重连，自动拉取消息通知用户，用户无需关心网络状态，仅作通知之用。注意：这里的网络事件不表示用户本地网络状态，仅指明SDK是否与IM云Server连接状态。只要用户处于登录状态，**ImSDK内部会进行断网重连，用户无需关心。**
 
**原型：**

```
voidTIMSetConnCallBack(TIMConnCB *callback);

typedef void (*CBConnOnConnected) (void* data);
typedef void (*CBConnOnDisconnected) (void* data);

typedef struct _TIMConnCallBack_c
{
	CBConnOnConnected		OnConnected;
	CBConnOnDisconnected	OnDisconnected;
	void* data;
}TIMConnCB;
```
**示例： **   

```
以下示例监听网络事件

void CBConnOnConnectedImp(void* data)
{
	printf("OnConnect! callback:%x", data);
}

void CBConnOnDisconnectedImp(void* data)
{
	printf("OnDisconnect! callback:%x", data);
}


voids SetConnCallBack()
{
	static TIMConnCB callback;
	callback.OnConnected = CBConnOnConnectedImp;
	callback.OnDisconnected = CBConnOnDisconnectedImp;
	callback.data = &callback;
	TIMSetConnCallBack(&callback);
}
```

## 6. 用户状态变更 （互踢）

用户如果在其他终端登录，会被踢下线，这时会收到用户被踢下线的通知，出现这种情况常规的做法是提示用户进行操作（退出，或者再次把对方踢下线）。 

**原型：**

```
void TIMSetKickOfflineCallBack(TIMForceOfflineCB* callback);

typedef void (*CBKickOffline) (void* data);
typedef struct _TIMKickOfflineCallBack_c
{
	CBKickOffline OnKickOffline;
	void* data;
}TIMForceOfflineCB;
```
>注意：
用户如果在离线状态下被踢，下次登录将会失败，可以给用户一个非常强的提醒（登录错误码ERR_IMSDK_KICKED_BY_OTHERS：6208），开发者也可以选择忽略这次错误，再次登录即可。

用户在线情况下的互踢情况如下图所示：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151015021645_19906.png)

图示中，用户在设备1登录，保持在线状态下，该用户又在设备2登录，这时用户会在设备1上强制下线，收到OnKickOffline回调。用户在设备1上收到回调后，提示用户，可继续调用login上线，强制设备2下线。这里是在线情况下互踢过程。

用户离线状态互踢如下图所示：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151015021702_68733.png)

用户在设备1登录，没有进行logout情况下进程退出。该用户在设备2登录，此时由于用户不在线，无法感知此事件，为了显式提醒用户，避免无感知的互踢，用户在设备1重新登录时，会返回（ERR_IMSDK_KICKED_BY_OTHERS：6208）错误码，表明之前被踢，是否需要把对方踢下线。如果需要，则再次调用login强制上线，设备2的登录的实例将会收到onForceOffline回调。
 
 ## 9. 禁用存储

默认情况ImSDK会进行消息的存储，如无需存储，可选择关闭存储来提升处理性能：

**原型:**

```
/**
Description:	禁用存储
@return		void
@exception      none
*/
TIM_DECL void		TIMDisableStorage();
```

## 7. 初始化 

在使用SDK进一步操作之前，需要初始SDK： 

**原型：**

```
/**
Description:	初始化SDK
@return			int 0:成功 非0:失败
@exception      none
*/
TIM_DECL int	TIMInit();
```

**示例：**

```
TIMInit();
```