## 未读消息

未读消息是指用户没有读过的消息（而非对方是否已经阅读，这种情况需要回执才能实现，目前 ImSDK 没有此功能），`isReaded` 属性标识消息是否已读，要想显示正确的未读计数，需要开发者显示调用已读上报，告诉 App 某条消息是否已读，例如，当用户进入聊天界面，可以设置整个会话的消息已读。对于聊天室，Server 不保存未读计数，每次登录后跟 Server 同步未读计数后将会清零。

## 获取当前未读消息数量

可通过 `GetUnreadMessageNum` 方法获取当前会话中未读消息的数量，对于聊天室，Server 不保存未读计数，每次登录后跟 Server 同步未读计数后将会清零。

**原型： **

```
 	/**
 	Description:	获取当前会话中未读消息的数量
 	@param	[in]	conv_handle	TIMConversationHandle
 	@return			uint64_t	未读数
 	@exception      none
 	*/
 	TIM_DECL uint64_t GetUnreadMessageNum(TIMConversationHandle conv_handle);
```

## 已读上报 

当用户阅读某个会话的数据后，需要进行会话消息的已读上报，SDK 根据会话中最后一条阅读的消息，设置会话中之前所有消息为已读。C2C 和群组设置已读用法相同，区别在于会话类型。 

**原型：** 

```
	/**
	Description:	已读上报 ImSDK 会把比 last_read_msg 时间更早的消息标记为已读消息
	@param	[in]	conv_handle		TIMConversationHandle
	@param	[in]	last_read_msg	上报已读的消息
	@return			void
	@exception      none
	*/
	TIM_DECL void SetReadMsg(TIMConversationHandle conv_handle, TIMMessageHandle last_read_msg);
```

**参数说明：**

`last_read_msg`：为当前会话中最后一条读过的消息，ImSDK 会把比 `last_read_msg` 时间更早的消息标记为已读消息。 

## 禁用自动上报

在 1.9 以上版本引入的方法，在单终端情况下，默认设置可以满足需求，出于性能考虑，未读消息由 ImSDK 拉回到本地，Server 默认会删除未读消息，切换终端以后无法看到之前终端已经拉回的未读消息，如果仅在一个终端，未读计数没有问题。在 ImSDK 初始化之前禁用自动已读即可生效。如果需要多终端情况下仍然会有未读，可以禁用自动上报，IM 通讯云不会代替用户已读上报，**一旦禁用自动上报，需要开发者显式调用 `setReadMessage`**。

```
	/**
	Description:	禁用自动已读上报（如果禁用，开发者必须显式调用回话的已读上报）
	@return			TIM_DECL void
	@exception      none
	*/
	TIM_DECL void		TIMDisableAutoReport();
```