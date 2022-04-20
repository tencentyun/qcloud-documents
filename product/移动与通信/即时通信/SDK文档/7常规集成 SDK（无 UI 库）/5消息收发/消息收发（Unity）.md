## 消息分类

腾讯云 IM 消息按照消息的发送目标可以分为：“单聊消息”（又称 “C2C 消息”）和“群聊消息” 两种：

| 消息分类 | API 关键词 | 说明 |
|---------|---------|---------|
| 单聊消息 | C2CMessage | 又称 C2C 消息，在发送时需要指定消息接收者的 UserID，只有接收者可以收到该消息 |
| 群聊消息 | GroupMessage | 在发送时需要指定目标群组的 groupID，该群中的所有用户均能收到消息|

按照消息承载的内容可以分为：“文本消息”、“图片消息”、“视频消息”、“语音消息”、“文件消息”、“位置消息”、“合并消息”、“群 Tips 消息”等几种类型。

| 消息分类 | API 关键词 | 说明 |
|---------|---------|---------|
| 文本消息 | kTIMElem_Text | 即普通的文字消息，该类消息会经过即时通信 IM 的敏感词过滤，发送包含的敏感词消息时会报80001错误码 |
| 自定义消息 | kTIMElem_Custom | 即一段二进制 buffer，通常用于传输您应用中的自定义信令，内容不会经过敏感词过滤 |
| 图片消息 | kTIMElem_Image | SDK 会在发送原始图片的同时，自动生成两种不同尺寸的缩略图，三张图分别被称为原图、大图、微缩图 |
| 视频消息 | kTIMElem_Video | 一条视频消息包含一个视频文件和一张配套的缩略图 |
| 语音消息 | kTIMElem_Sound | 支持语音是否播放红点展示 |
| 文件消息 | kTIMElem_File | 文件消息最大支持100MB|
| 位置消息 | kTIMElem_Location | 地理位置消息由位置描述、经度（longitude ）和纬度（latitude）三个字段组成 |
| 合并消息 | kTIMElem_Merge | 最大支持 300 条消息合并 |
| 群 Tips 消息 | kTIMElem_GroupTips | 群 Tips 消息常被用于承载群中的系统性通知消息，例如有成员进出群组，群的描述信息被修改，群成员的资料发生变化等|

## 发送文本消息

```c#
public static void MsgSendMessage() {
        string conv_id = ""; // c2c 消息会话 ID 为 userID，群消息会话 ID 为 groupID
        Message message = new Message();
        message.message_conv_id = conv_id;
        message.message_conv_type = TIMConvType.kTIMConv_C2C;// 群消息为TIMConvType.kTIMConv_Group
        List<Elem> messageElems = new List<Elem>(); 
        Elem textMessage = new Elem(); // 创建消息
        textMessage.elem_type = TIMElemType.kTIMElem_Text;
        textMessage.text_elem_content = "这是一个普通文本消息";
        messageElems.Add(textMessage);
        message.message_elem_array = messageElems;
        StringBuilder messageId = new StringBuilder(128);

        TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc, 						string json_param, string user_data)=>{
          // 消息发送异步结果
        });
  			// 消息发送同步返回的消息ID messageId
}
```

## 发送图片消息

```c#
public static void MsgSendMessage() {
        string conv_id = ""; // c2c 消息会话 ID 为 userID，群消息会话 ID 为 groupID
        Message message = new Message();
        message.message_conv_id = conv_id;
        message.message_conv_type = TIMConvType.kTIMConv_C2C;// 群消息为TIMConvType.kTIMConv_Group
        List<Elem> messageElems = new List<Elem>(); 
        Elem imageMessage = new Elem(); // 创建消息
        imageMessage.elem_type = TIMElemType.kTIMElem_Image;
        imageMessage.image_elem_orig_path = "/Users/xxx/xxx.png"; // 文件绝对路径
  			imageMessage.image_elem_level = TIMImageLevel.kTIMImageLevel_Orig; // 原图发送
        messageElems.Add(imageMessage);
        message.message_elem_array = messageElems;
        StringBuilder messageId = new StringBuilder(128);

        TIMResult res = TencentIMSDK.MsgSendMessage(conv_id, TIMConvType.kTIMConv_C2C, message, messageId, (int code, string desc, 						string json_param, string user_data)=>{
          // 消息发送异步结果
        });
  			// 消息发送同步返回的消息ID messageId
}
```

## 消息发送进度获取

```c#
TencentIMSDK.SetMsgElemUploadProgressCallback((Message message, int index, int cur_size, int total_size, string user_data)=>{
	// message 当前正在发送的消息实例
  // index 当前正在上传的文件序号
  // cur_size 当前正在上传的文件大小MB
  // total_size 当前正在上传的文件总大小
})
```

## 接收消息

```c#
// 注册接收消息监听
TencentIMSDK.RecvNewMsgCallback((List<Message> message, string user_data)=>{

})
```

## 消息字段含义

| 字段                                  | 含义                                                         |
| ------------------------------------- | ------------------------------------------------------------ |
| message_elem_array                    | 消息内元素列表                                               |
| message_conv_id                       | 消息所属会话 ID                                               |
| message_conv_type                     | 消息所属会话类型                                             |
| message_sender                        | 消息的发送者                                                 |
| message_priority                      | 消息优先级                                                   |
| message_client_time                   | 客户端时间                                                   |
| message_server_time                   | 服务端时间                                                   |
| message_is_from_self                  | 消息是否来自自己                                             |
| message_platform                      | 发送消息的平台                                               |
| message_is_read                       | 消息是否已读                                                 |
| message_is_online_msg                 | 消息是否是在线消息，false 表示普通消息，true 表示阅后即焚消息，默认为 false |
| message_is_peer_read                  | 消息是否被会话对方已读                                       |
| message_status                        | 消息当前状态                                                 |
| message_unique_id                     | 消息的唯一标识，推荐使用 kTIMMsgMsgId                        |
| message_msg_id                        | 消息的唯一标识                                               |
| message_rand                          | 消息的随机码                                                 |
| message_seq                           | 消息序列                                                     |
| message_custom_int                    | 自定义整数值字段（本地保存，不会发送到对端，程序卸载重装后失效） |
| message_custom_str                    | 自定义数据字段（本地保存，不会发送到对端，程序卸载重装后失效） |
| message_cloud_custom_str              | 消息自定义数据（云端保存，会发送到对端，程序卸载重装后还能拉取到） |
| message_is_excluded_from_unread_count | 消息是否不计入未读计数：默认为 NO，表明需要计入未读计数，设置为 YES，表明不需要计入未读计数 |
| message_is_forward_message            | 是否是转发消息                                               |
| message_group_at_user_array           | 群消息中被 @ 的用户 UserID 列表（即该消息都 @ 了哪些人），如果需要 @ALL ，请传入 kImSDK_MesssageAtALL 字段 |
| message_sender_profile                | 消息的发送者的用户资料                                       |
| message_sender_group_member_info      | 消息发送者在群里面的信息，只有在群会话有效。目前仅能获取字段 kTIMGroupMemberInfoIdentifier、kTIMGroupMemberInfoNameCard 其他的字段建议通过 TIMGroupGetMemberInfoList 接口获取 |
| message_offlie_push_config            | 消息的离线推送设置                                           |
| message_excluded_from_last_message    | 是否作为会话的 lasgMessage，true - 不作为，false - 作为      |

