在开发包含IM功能的APP时，经常需要考虑导入历史消息的问题。例如，在集成IMSdk前，我们的APP使用了其他的消息子系统。那么在集成IMSdk的时候，可以考虑使用导入历史消息的功能，来导入旧的消息，并保存到本地。进而用户在查看历史消息的时候，能够找出集成IMSdk前的固有消息，从而提升用户体验。

## 导入历史消息功能介绍

IMSdk针对历史消息，抽象了一种消息状态 `#define TIM_MSG_STATUS_LOCAL_IMPORTED 5` “本地导入”。当获取消息状态返回该值时，表明该消息为本地导入的历史消息。业务集成时可以根据根据该状态值区分消息是否为本地导入的历史消息。

当集成历史消息导入功能的时候，对于将导入的消息，必须先设置消息状态为“本地导入”（即`#define TIM_MSG_STATUS_LOCAL_IMPORTED 5`）。对于处在非“本地导入”状态的消息，导入消息会失败。

### 变更消息状态为本地导入

**原型：**

```
/**
Description:	将该消息转为本地消息， 用于导入历史消息
					（该操作永久改变消息状态）
@param	[in]	handle
@return			bool	TRUE：成功 FALSE:失败
@exception      none
*/
TIM_DECL bool	ConvertMsgStatusToLocalImported(TIMMessageHandle handle);
```

**参数说明：**

参数 | 说明
---|---
handle | tim message handle

### 修改消息时戳

当导入消息的时候，为了矫正会话中消息的排序，并且显示正确的历史消息时间，需要针对历史消息显示的设置时间。

**原型：**

```
/**
	Description:	设置本地消息的时戳，仅用于本地消息
	@param	[in]	handle
	@param	[in]	time	时戳
	@return			bool	TRUE：成功 FALSE:失败
	@exception      none
	*/
	TIM_DECL bool SetMsgTimestamp(TIMMessageHandle handle, uint32_t time);
```

**参数说明：**
参数 | 说明
---|---
handle | tim message handle
time | Unix时戳

### 修改消息发送人ID

导入的历史消息不同于正常发送的消息，针对一个对话，导入的消息需要指定发送方。

**原型：**

```
/**
Description:	设置本地消息的发送方ID，仅用于本地消息
@param	[in]	handle
@param	[in]	id		用户ID
@return			bool	TRUE：成功 FALSE:失败
@exception      none
*/
TIM_DECL bool SetMsgSender(TIMMessageHandle handle, const char* id);
```

**参数说明：**
参数 | 说明
---|---
handle | tim message handle
id | 发送方ID

### 导入历史消息

**关于导入历史消息支持的消息元素类型：**
由于不同消息元素的接口和功能不同，需要设置的信息也不尽相同。因此，针对导入历史消息功能，目前仅支持文本，表情，自定义消息元素和其他外部可以明确设置元素全部资源信息的消息元素类型。对于例如图片，声音等消息元素类型不支持直接导入。可以考虑使用自定义元素类型或者使用消息的自定义字段完成对这种历史消息的描述。

**原型：**

```
	/**
	Description:	导入历史消息
	@param	[in]	conv_handle	conversation handle
	@param	[in]	msg_handles msg handle数组
	@param	[in]	msg_num		msg个数
	@return			int	0：成功 非0：失败
	@exception      none
	*/
	TIM_DECL int	ImportMsgs(TIMConversationHandle conv_handle, TIMMessageHandle* msg_handles, uint32_t msg_num);
```

**参数说明：**
参数 | 说明
---|---
conv_handle|conversation handle
msg_handles | tim message handle 数组
msg_num | msg个数

**示例：**

```
void DemoLoadMsg()
{
	const uint32_t id_num = 3;
	const char id[] = "test";

	TIMMessageHandle msg = CreateTIMMessage();
	ConvertMsgStatusToLocalImported(msg);
	SetMsgSender(msg, id);
	SetMsgTimestamp(msg, 0);
	TIMMsgTextElemHandle elem = CreateMsgTextElem();
	char content[20] = { 0 };
	sprintf(content, "%s%s", "msg from ", "here");
	SetContent(elem, content);
	AddElem(msg, elem);

	TIMMessageHandle* msgs = new TIMMessageHandle;
	msgs[0] = msg;

	TIMConversationHandle conv = CreateConversation();
	TIMGetConversation(conv, kCnvC2C, "test2");

	ImportMsgs(conv, msgs, 1);
}
```

