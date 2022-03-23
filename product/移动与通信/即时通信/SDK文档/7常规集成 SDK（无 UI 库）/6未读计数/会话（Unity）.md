## 展示会话列表

用户在登录 App 后，可以像微信那样展示最近会话列表。整个过程分为**拉取会话列表**、**处理更新通知**和**更新 UI 内容（包括未读计数）**，本文主要介绍这些步骤的详细细节。

## 拉取会话列表

用户可以通过 [ConvGetConvList](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_ConvGetConvList_com_tencent_imsdk_unity_callback_ValueCallback_) 拉取全部的会话列表，Unity SDK 暂时不支持对会话进行分页。

## 会话更新

当会话中的信息发生改变时，SDK 会通过 ConvEventCallback 将信息回调给开发者。

```c#
TencentIMSDK.ConvEventCallback((TIMConvEvent conv_event, List<ConvInfo> conv_list, string user_data)=>{
	// 会话变更的相关信息。
});
```

更新场景如下：

- lastMessage 更新
- 断网重连
- 新增会话
- 会话置顶
- 会话接收消息选项更改

## 获取所有会话未读数

可以通过 [ConvGetTotalUnreadMessageCount](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_ConvGetTotalUnreadMessageCount_com_tencent_imsdk_unity_callback_ValueCallback_) 获取所有会话未读数，调用如下：

```c#
TencentIMSDK.ConvGetTotalUnreadMessageCount((int code, string desc, string json_param, string user_data)=>{
	
})
```

## 设置所有会话已读

Unity SDK 提供一键设置会话已读功能，可以调用 [MsgMarkAllMessageAsRead](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_MsgMarkAllMessageAsRead_com_tencent_imsdk_unity_callback_ValueCallback_)。

```c#
TencentIMSDK.MsgMarkAllMessageAsRead((int code, string desc, string json_param, string user_data)=>{
	
})
```

## 置顶会话

会话置顶指的是把特定的好友或者群会话固定在会话列表的最前面，新版本 SDK 增加了主动设置或者取消会话置顶的接口 [ConvPinConversation](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_ConvPinConversation_System_String_com_tencent_imsdk_unity_enums_TIMConvType_System_Boolean_com_tencent_imsdk_unity_callback_ValueCallback_)，同时支持漫游和多端同步。
会话对象 [ConvInfo](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.types.ConvInfo.html) 新增了字段 [conv_is_pinned](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.types.ConvInfo.html#com_tencent_imsdk_unity_types_ConvInfo_conv_is_pinned)，用于判断会话的置顶状态。当会话的置顶状态发生变更的时候，SDK 会向您的 App 回调 [ConvEventCallback](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.callback.ConvEventCallback.html)。

```c#
TencentIMSDK.ConvPinConversation(conv_id,conv_type,is_pinned,(int code, string desc, string json_param, string user_data)=>{
	
})
```

## 删除会话

调用 [ConvDelete](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_ConvDelete_System_String_com_tencent_imsdk_unity_enums_TIMConvType_com_tencent_imsdk_unity_callback_ValueCallback_) 接口可以删除某个会话，会话删除默认关闭多端同步，可在控制台开启多端同步，删除会话时默认删除本地和服务器历史消息，且无法恢复。

```c#
TencentIMSDK.ConvDelete(conv_id,conv_type,(int code, string desc, string json_param, string user_data)=>{

})
```

## 草稿箱

在发送消息时，可能会遇到消息尚未编辑完就要切换至其它聊天窗口的情况，这些未编辑完的消息可通过 [ConvSetDraft](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_ConvSetDraft_System_String_com_tencent_imsdk_unity_enums_TIMConvType_com_tencent_imsdk_unity_types_DraftParam_) 接口保存，以便于回到聊天界面使用 [ConvInfo](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.types.ConvInfo.html) 的 [conv_draft](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.types.ConvInfo.html#com_tencent_imsdk_unity_types_ConvInfo_conv_draft) 字段 继续编辑内容。

## 常见问题

### 1. 最近会话列表的保存数量上限是多少？

本地存储的会话列表没有数量上限，云端存储的会话列表最大数量为100。
如果一个会话长时间没有信息变更，该会话在云端最多保存7天，如需放宽限制，请 [联系我们](https://cloud.tencent.com/document/product/269/59590)。

### 2. 为什么换了一个手机登录相同帐号后拉取的会话列表不一致？

本地存储的会话和云端存储的会话并不总是一致的，如果用户不主动调用 ConvDelete 接口删除本地的会话，该会话就会一直存在。而云端存储的会话最大只会保存100条，且对于长时间没有信息变更的会话，云端最多保存7天，所以不同的终端本地显示的会话可能会不一样。

### 3. 为什么会拉取到重复的会话？

调用 ConvGetConvList 接口拉取的会话可能已经通过 ConvEventCallback 回调接口添加到了 UI 会话列表的数据源中，因此为了避免重复添加同一个会话，您需要在 UI 会话列表数据源中根据 conv_id 找到相同的会话并做替换。
