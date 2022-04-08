## 消息的分类
腾讯云 IM 消息按照消息的发送目标可以分为：“单聊消息”（又称 “C2C 消息”）和“群聊消息” 两种：

| 消息分类 | API 关键词 | 说明 |
|---------|---------|---------|
| 单聊消息 | C2CMessage | 又称 C2C 消息，在发送时需要指定消息接收者的 UserID，只有接收者可以收到该消息。 |
| 群聊消息 | GroupMessage | 在发送时需要指定目标群组的 groupID，该群中的所有用户均能收到消息。|

按照消息承载的内容可以分为：“文本消息”、“自定义（信令）消息”，“图片消息”、“视频消息”、“语音消息”、“文件消息”、“位置消息”、“合并消息”、“群 Tips 消息”等几种类型。

| 消息分类 | API 关键词 | 说明 |
|---------|---------|---------|
| 文本消息 | TextElem | 即普通的文字消息，该类消息会经过即时通信 IM 的敏感词过滤，发送包含的敏感词消息时会报80001错误码。 |
| 自定义消息 | CustomElem | 即一段二进制 buffer，通常用于传输您应用中的自定义信令，内容不会经过敏感词过滤。 |
| 图片消息 | ImageElem | SDK 会在发送原始图片的同时，自动生成两种不同尺寸的缩略图，三张图分别被称为原图、大图、微缩图。 |
| 视频消息 | VideoElem | 一条视频消息包含一个视频文件和一张配套的缩略图。 |
| 语音消息 | SoundElem | 支持语音是否播放红点展示。 |
| 文件消息 | FileElem | 文件消息最大支持100MB。 |
| 位置消息 | LocationElem | 地理位置消息由位置描述、经度（longitude ）和纬度（latitude）三个字段组成。 |
| 合并消息 | MergerElem | 最大支持 300 条消息合并 |
| 群 Tips 消息 | GroupTipsElem | 群 Tips 消息常被用于承载群中的系统性通知消息，例如有成员进出群组，群的描述信息被修改，群成员的资料发生变化等。 |

## 收发简单消息
在 IM Flutter SDK 中有两大类消息（简单消息和富媒体消息），这里我们先介绍简单消息。在V2TIMManager.getMessageManager() 中提供了一组简单消息的收发接口，可直接用于文本消息和自定义（信令）消息的收发，但3.6.0后我们不推荐您使用。建议您也走富媒体消息流程，先 create 对应 [V2TimMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message/V2TimMessage-class.html)，再调用统一的 [sendMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/sendMessage.html) 接口。

简单消息：

在 IM Flutter SDK 中有两种简单消息 [文本消息（V2TimTextElem）](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_text_elem/V2TimTextElem-class.html) 和 [自定义消息（V2TimCustomElem）](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_custom_elem/V2TimCustomElem-class.html)，但以下简单消息发送接口在3.6.0后不推荐使用。

- [sendC2CTextMessage（3.6.0后不建议使用）](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/sendC2CTextMessage.html) 
- [sendGroupTextMessage（3.6.0后不建议使用）](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/sendGroupTextMessage.html) 
-  [sendC2CCustomMessage（3.6.0后不建议使用）](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/sendC2CCustomMessage.html) 
- [sendGroupCustomMessage（3.6.0后不建议使用）](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/sendGroupCustomMessage.html) 

### 发送消息和信令消息
推荐的消息发送方式（这里以文本消息为例）：

```dart
    V2TimValueCallback<V2TimMsgCreateInfoResult> createMessage =
        await TencentImSDKPlugin.v2TIMManager
            .getMessageManager()
            .createTextMessage(text: "您要创建的文本");
    String id = createMessage.data!.id!; // 返回的消息创建id

    V2TimValueCallback<V2TimMessage> res = await TencentImSDKPlugin.v2TIMManager
        .getMessageManager()
        .sendMessage(
            id: id, // 将消息创建id传递给
            receiver:  "您要发送给用户的userID",
            groupID:  "您要发送的groupID",
            );
```
在createMessage后，会返回一个消息创建 id，将消息创建 id 传递给 sendMessage 即可将消息发送出去。sendMessage 方法为所有消息发送的通用方法 receiver、groupID 二选一填写，另一个传递空字符串即可。

>!发送文本消息，其中文本消息会经过即时通信 IM 的敏感词过滤，包含的敏感词消息在发送时会报80001错误码。调用 createMessage 再调用 sendMessage 可以发送 C2C 自定义（信令）消息，自定义消息本质是一段二进制 buffer，通常用于传输您应用中的自定义信令，内容不会经过敏感词过滤。此外 Flutter IM SDK 额外封装了一个信令供您调用（将在下方介绍）。

### 接收文本和信令消息
通过  [addSimpleMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/addSimpleMsgListener.html) 可以监听简单的文本和信令消息，复杂的图片、视频、语音消息则需要通过 v2TIMManager.getMessageManager() 中定义的 [addAdvancedMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/addAdvancedMsgListener.html) 实现。

>? [addSimpleMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/addSimpleMsgListener.html)  与 [addAdvancedMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/addAdvancedMsgListener.html) 请勿混用，以免产生逻辑 BUG。

### 经典示例：收发弹幕消息
直播场景下，在直播群中收发弹幕消息是非常普遍的交互方式，其实现方式非常简单：

1. 主播调用 [createGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/createGroup.html) 创建一个直播群（AVChatRoom），并在“正在直播”的房间列表中记录群组 ID。
2. 观众选择自己喜欢的主播，并调用 [joinGroup](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_manager/V2TIMManager/joinGroup.html) 加入该主播创建的直播群。
3. 消息的发送方可以通过 [createTextMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createTextMessage.html) 然后 [sendMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html) 群发弹幕文本消息。
4. 消息的接收方可以通过 [addSimpleMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/addSimpleMsgListener.html) 注册简单消息监听器，并通过监听回调函数  [onRecvGroupTextMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimSimpleMsgListener/V2TimSimpleMsgListener/onRecvGroupTextMessage.html) 获取文本消息。

为直播间增加“点赞飘心”的功能，“点赞飘心”属于一条指令，操作步骤如下：
1. 定义一个的自定义消息类型，例如一个 JSON 字符串：` { "command": "favor", "value": 101 }`。
2. 通过 [createCustomMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createCustomMessage.html) 和
[sendMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html) 接口进行消息的发送，并通过  [onRecvGroupCustomMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSimpleMsgListener.html#a46b48869e411b41c25a98211d951335c) 进行接收。

## 收发富媒体消息
图片、视频、语音、文件、地理位置等类型的消息称为“富媒体消息”。
- 在发送时，富媒体消息需要先用对应的 `create` 函数创建一个  [V2TimMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message/V2TimMessage-class.html) 对象，再调用对应的 `send` 接口发送。
- 在接收时，富媒体消息要先判断 `elemType`，并根据 `elemType` 获取对应的 `Elem` 进行二次解析。

### 发送富媒体消息
本文以图片消息为例，介绍发送一条富媒体消息的过程：
1. 发送方调用 [createImageMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createImageMessage.html) 创建一条图片消息，拿到消息对象 [V2TimMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message/V2TimMessage-class.html)的id(注意此id不是messageId)。
2. 发送方调用 [sendMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html) 接口将刚才创建的消息对象的id传递进去消息便会发送。

### 接收富媒体消息
1. 接收方调用 [addAdvancedMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/addAdvancedMsgListener.html) 接口设置高级消息监听。
2. 接收方通过监听回调 [onRecvNewMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimAdvancedMsgListener/V2TimAdvancedMsgListener/onRecvNewMessage.html) 获取图片消息 [V2TIMMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message/V2TimMessage-class.html)。
3. 接收方解析  [V2TIMMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message/V2TimMessage-class.html) 消息中的 `elemType` 属性，并根据其类型进行二次解析，获取消息内部 Elem 中的具体内容。

### 经典示例：收发图片
发送方创建一条图片消息并发送：
```dart
// 创建图片消息
    V2TimValueCallback<V2TimMsgCreateInfoResult> createMessage =
        await TencentImSDKPlugin.v2TIMManager
            .getMessageManager()
            .createImageMessage(
              imagePath: image.path,
              fileName: 'test.png',
              fileContent: fileContent, // web端需要
            );
// 拿到返回的id
    String id = createMessage.data!.id!;
// 传递id发送消息
    V2TimValueCallback<V2TimMessage> res = await TencentImSDKPlugin.v2TIMManager
        .getMessageManager()
        .sendMessage(
            id: id,
            receiver: "您需要发送给谁的userID",
            groupID: "您需要发送给哪个group",
         );
```

接收方识别一条 [图片消息](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_image_elem/V2TimImageElem-class.html) 并将解析其中包含的原图、大图和微缩图：
```dart
  // 3.9.0后 可以引入V2TIM_IMAGE_TYPE来获取枚举值
  static const V2_TIM_IMAGE_TYPES = {
    'ORIGINAL': 0,
    'BIG': 1,
    'SMALL': 2,
  };


 void onRecvNewMessage(V2TimMessage message) {
	int elemType = message.elemType;
	 V2TimImage? img;
    // 缩略图优先，大图次之，最后是原图
    img = message.imageElem!.imageList?.firstWhere(
        (e) => e!.type == V2_TIM_IMAGE_TYPES['ORIGINAL'],
        orElse: () => null);
    img = message.imageElem!.imageList?.firstWhere(
        (e) => e!.type == V2_TIM_IMAGE_TYPES['BIG'],
        orElse: () => null);
    img = message.imageElem!.imageList?.firstWhere(
        (e) => e!.type == V2_TIM_IMAGE_TYPES['SMALL'],
        orElse: () => null);
    if (img == null) {
     // ....
    }
    // ....
}
```


## 收发群 @ 消息
群 @ 消息，发送方可以在输入栏监听 @ 字符输入，调用到群成员选择界面，选择完成后以 `“@A @B @C......”` 形式显示在输入框，并可以继续编辑消息内容，完成消息发送。接收方会在会话界面的群聊天列表，重点显示 `“有人@我”` 或者 `“@所有人”` 标识，提醒用户有人在群里 @ 自己了。
>?目前仅支持文本 @ 消息。


### 发送群 @ 消息
1. 发送方监听聊天界面的文本输入框，启动群成员选择界面，选择完成后回传选择群成员的 ID 和昵称信息，ID 用来构建消息对象 [V2TimMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message/V2TimMessage-class.html)，昵称用来在文本框显示。
2. 发送方调用 v2TIMManager.getMessageManager() 的 [createTextAtMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createTextAtMessage.html) 创建一条 @ 文本消息，拿到消息对象 [V2TimMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message/V2TimMessage-class.html)。
3. 发送方调用 [sendMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html) 接口将刚才创建的 @ 消息对象发送出去。

### 接收群 @ 消息
1. 在加载和更新会话处，需要监听 [V2TIMConversation](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_conversation/V2TimConversation-class.html) 的 [OnConversationChangedCallback](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_callbacks/OnConversationChangedCallback.html) 回调来获取会话的@列表，将来会提供方法`getGroupAtInfoList`手动获取 atInfoList。
2. 在返回列表中找到 [V2TIMGroupAtInfo](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_group_at_info/V2TimGroupAtInfo-class.html) 对象，其中有一个 [atType](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_group_at_info/V2TimGroupAtInfo/atType.html) 字段来获取 @ 数据类型，并更新到当前会话的 @ 信息。

### 经典示例：收发群 @ 消息
- **发送群 @ 消息**：
发送方创建一条群 @ 消息并发送：
```dart
// 获取群成员ID数据
List<String> atUserList = ['AT_ALL_TAG',"何大佬的userID"]; // 既 @全体又@何大佬
// 创建群@消息

    V2TimValueCallback<V2TimMsgCreateInfoResult> createMessage =
        await TencentImSDKPlugin.v2TIMManager
            .getMessageManager()
            .createTextAtMessage(
              text: text,
              atUserList: atUserList,
            );
    String id = createMessage.data!.id!;
    V2TimValueCallback<V2TimMessage> res = await TencentImSDKPlugin.v2TIMManager
        .getMessageManager()
        .sendMessage(
            id: id,
            receiver: "发送给谁",
            groupID: "需要发送给哪个Group",
           );
```

- **接收群 @ 消息**：
  加载和更新会话处，即 [OnConversationChangedCallback](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_callbacks/OnConversationChangedCallback.html) 处，获取群 @ 数据列表：
```dart
   // 3.9.0版本后可以使用枚举 V2TIM_IMAGE_TYPE
    var arInfoType = {
      "TIM_AT_UNKNOWN": 0, 	//错误状态
      "TIM_AT_ME": 1,  		// @ 我
      "TIM_AT_ALL": 2,		// @ 群里所有人
      "TIM_AT_ALL_AT_ME": 3 // @ 群里所有人并且单独 @ 我
    };

		//获取群@数据列表
     getInfoList(V2TimConversation conversation) {
        List<V2TimGroupAtInfo?>? atInfoList =
           conversation.groupAtInfoList;
           if (atInfoList == null || atInfoList.isNotEmpty) {
              return [];
            } else {
                  return atInfoList;
            }
        }

```

## 收发合并转发消息
要实现类似于微信的合并转发功能，首先需要根据原始消息列表创建一条合并消息，然后把合并消息发送到对端，对端收到合并消息后再解析出原始消息列表，合并消息的展示还需要标题和摘要信息，如下图所示：

<table>
   <tr>
      <th width="0px" style="text-align:center">合并转发</td>
      <th width="0px" style="text-align:center">合并消息展示</td>
      <th width="0px"  style="text-align:center">单击合并消息下载合并消息列表展示</td>
   </tr>
   <tr>
      <td style="text-align:center"><img style="width:190px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/ca62239bbab545665df617c928960d5a.jpg" /></td>
      <td style="text-align:center"><img style="width:190px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/ae0bbf431eee95aa1b0be04b2346837f.jpg" /></td>
      <td style="text-align:center"><img style="width:190px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/b145e9c869fc84ead6477f9fa9012d72.jpg" /></td>
   </tr>
</table>

- **发送合并转发消息：**
通常我们在收到一条合并消息的时候，会在聊天界面这样显示：

| vinson 和 lynx 的聊天记录 | title         （标题） |
|---------|---------|
| vinson：新版本 SDK 计划什么时候上线呢？ | abstract1     （摘要信息1） |
| lynx：计划下周一，具体时间要看下这两天的系统测试情况..| abstract2     （摘要信息2） |
| vinson：好的 | abstract3     （摘要信息3） |

聊天界面只会显示合并消息的标题和摘要信息，只有用户单击合并消息的时候才会展示合并消息列表，我们在创建一条合并消息的时候不仅要设置合并消息列表，还要设置标题和摘要信息，实现流程如下：
1、调用 [createMergerMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/createMergerMessage.html) 接口创建一条合并消息。
2、调用 [sendMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/sendMessage.html) 接口发送合并消息。

- **接收合并转发消息：**
当我们收到一条合并消息 [V2TIMMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message/V2TimMessage-class.html)，可以先通过合并消息元素 [V2TIMMergerElem](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMergerElem.html) 获取 [title](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMergerElem.html#a864916a91d453e2124c12e0ccbb66550) 和  [abstractList](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_merger_elem/V2TimMergerElem/abstractList.html)  UI 展示，当用户单击合并消息的时候再调用 [downloadMergerMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMergerElem.html#af34d8228a9842875652a726f24ac3d30) 接口下载合并消息列表 UI 展示。


### 经典示例：收发合并转发消息
- **发送合并转发消息：**
发送方创建一条合并消息并发送。
```dart
  /// 合并转发
  sendMergerMessage(
      {required List<V2TimConversation> conversationList, // 为了支持一次转发多个会话
      required String title,
      required List<String> abstractList,
      required List<String> multiSelectedMessageList}) async {
    for (var conversation in conversationList) {
      final convID = conversation.groupID ?? conversation.userID ?? "";
      final convType = conversation.type;
      // 要发送的信息msgId列表
      final List<String> msgIDList = multiSelectedMessageList;

      final mergerMessageInfo = await _messageService.createMergerMessage(
          msgIDList: msgIDList,
          title: title,
          abstractList: abstractList,
          compatibleText: "该版本不支持此消息");
      final messageInfo = mergerMessageInfo!.messageInfo;
      if (messageInfo != null) {
        // 发送mergeMessage
        V2TimValueCallback<V2TimMessage> res = await TencentImSDKPlugin
            .v2TIMManager
            .getMessageManager()
            .sendMessage(
              id: mergerMessageInfo.id!,
              receiver: convType == ConvType.c2c ? convID : "",
              groupID: convType == ConvType.group ? convID : "",
            );
      }
    }
  }
```

- **接收合并转发消息：**
接收方收到一条合并消息并解析：
```dart

 void onRecvNewMessage(V2TIMMessage msg) {
	if (msg.elemType == MessageElemType.V2TIM_ELEM_TYPE_MERGER) {
		// 获取合并消息 elem
		V2TimMergerElem mergerElem = messageItem.mergerElem!,
		// 获取 title
		String title = mergerElem.title;
		// 获取摘要列表
		List<String> abstractList = mergerElem.abstractList;
		// 用户单击合并消息的时候下载合并消息列表
		// ...
		};
}

	// 单击mergeMessage下载mergeMessage
  handleTap(BuildContext context, String msgID) async {
    final res = await TencentImSDKPlugin.v2TIMManager
        .getMessageManager()
        .downloadMergerMessage(msgID: msgID);
    final mergerMessageList = res.data;
    if (mergerMessageList != null) {
   // ....
    }
  }
```

## 发送不计入未读数的消息
正常情况下，无论是发送 C2C 单聊消息还是发送 Group 群消息，都会计入未读消息数（通过会话对象 [V2TIMConversation](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_conversation/V2TimConversation-class.html) 的 [unreadCount](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_conversation/V2TimConversation/unreadCount.html) 接口，可以拿到一个会话的未读消息数）。当您希望发送一些不计入未读计数的消息时，例如提示类或者控制类的消息，可以按照下面的方式来发送：

```dart
    V2TimValueCallback<V2TimMsgCreateInfoResult> createMessage =
        await TencentImSDKPlugin.v2TIMManager
            .getMessageManager()
            .createTextMessage(text: "text");
    String id = createMessage.data!.id!;
	// 设置不计入未读消息的标记
    createMessage.data?.messageInfo?.isExcludedFromUnreadCount = true;
    V2TimValueCallback<V2TimMessage> res = await TencentImSDKPlugin.v2TIMManager
        .getMessageManager()
        .sendMessage(
            id: id,
            receiver:  "userID",
            groupID:  "groupID",
            );
```


## 发送不更新会话的消息

某些场景下，不希望一些提示类型的消息显示为会话的最新消息，可以按照下面的方式来发送：

```dart
// 创建消息对象
    V2TimValueCallback<V2TimMsgCreateInfoResult> createMessage =
        await TencentImSDKPlugin.v2TIMManager
            .getMessageManager()
            .createTextMessage(text: "你的Text");
    String id = createMessage.data!.id!;
	// 设置不计入未读消息的标记
    createMessage.data?.messageInfo?.setExcludedFromLastMessage = true; // 设置更改标记
    V2TimValueCallback<V2TimMessage> res = await TencentImSDKPlugin.v2TIMManager
        .getMessageManager()
        .sendMessage(
            id: id,
            receiver:  "userID",
            groupID: "groupID",
            );
```

## 发送群内定向消息


定向消息是指向群内部分成员发送消息，而其他群成员无法收到该消息，可以按照下面的方式实现：

> ?3.9.0后会支持该方法：
>
>- 该功能需要购买旗舰版套餐包。
>- 创建定向群消息的原始消息对象不支持群 @ 消息。
>- 社群（Community）和直播群（AVChatRoom）不支持发送定向群消息。
>- 定向群消息默认不计入群会话的未读计数。

## 设置离线推送
当接收方的 App 被 kill 时，IM SDK 无法通过正常的网络连接收取新消息。如需实现在此场景下接收方仍能感知到新消息，需要使用各个手机厂商提供的离线推送服务，新用户推荐使用 TPNS 推送（详情请参见 [离线推送部分](https://cloud.tencent.com/document/product/269/68720)。)

### 设置离线推送的标题和内容
您可以在发送消息时，通过 [sendMessage](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/sendMessage.html) 接口中的 **offlinePushInfo** 字段，设置离线推送的标题和内容。

```dart
// 创建一条文本消息发送给 groupA，并且自定义推送 Title、推送内容
    V2TimValueCallback<V2TimMsgCreateInfoResult> createMessage =
        await TencentImSDKPlugin.v2TIMManager
            .getMessageManager()
            .createTextMessage(text: text);
    String id = createMessage.data!.id!;
    createMessage.data?.messageInfo?.isExcludedFromUnreadCount = true;
    // 设置通知标题和通知栏内容
    OfflinePushInfo offlinePushInfo =
        OfflinePushInfo(title: "offline_title", desc: "offline_desc");
    V2TimValueCallback<V2TimMessage> res =
        await TencentImSDKPlugin.v2TIMManager.getMessageManager().sendMessage(
              id: id,
              receiver: receiver.length > 0 ? receiver.first : "",
              groupID: groupID.length > 0 ? groupID.first : "",
              offlinePushInfo: offlinePushInfo
            );
```

### 单击推送消息跳转到对应的聊天窗口
如需实现该功能，发送消息时需设置离线推送对象 `offlinePushInfo` 的扩展字段 `ext`，收到消息的用户打开 App 时可以通过不同厂商提供的获取自定义内容的方式拿到这个扩展字段 `ext`，然后根据 `ext` 内容跳转到对应的聊天界面。

本文以 `“denny 给 vinson 发送消息”` 的场景为例。
发送方：denny 要在发送消息的时候设置推送扩展字段 ext：

```dart
// denny 在发送消息时设置 offlinePushInfo，并指定 ext 字段
    V2TimValueCallback<V2TimMsgCreateInfoResult> createMessage =
        await TencentImSDKPlugin.v2TIMManager
            .getMessageManager()
            .createTextMessage(text: text);
    String id = createMessage.data!.id!;
    
    // 设置通知标题和通知栏内容以及ext
    OfflinePushInfo offlinePushInfo =
        OfflinePushInfo(title: "offline_title", 
		desc: "offline_desc", 
		ext: json.encode({"action": "jump to denny"})
		);
    
	V2TimValueCallback<V2TimMessage> res = await TencentImSDKPlugin.v2TIMManager
        .getMessageManager()
        .sendMessage(
            id: id,
            receiver:  "userID",
            groupID:  "groupID",
            offlinePushInfo: offlinePushInfo);
```


## 设置消息为只能在线接收
某些场景下，您可能希望发出去的消息只被在线用户接收，即当接收者不在线时就不会感知到该消息。您只需在 [sendMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html) 时，将参数 `onlineUserOnly` 设置为 `true`，此时发送出去的消息跟普通消息相比，会有如下差异点：
- 不支持离线存储，即如果接收方不在线就无法收到。
- 不支持多端漫游，即如果接收方在一台终端设备上一旦接收过该消息，无论是否已读，都不会在另一台终端上再次收到。
- 不支持本地存储，即本地的云端的历史消息中均无法找回。

>?此参数可以用来完成用户正在输入场景。

## 设置接收消息免打扰
SDK 支持三种类型的消息接收选项：

- V2TIM_RECEIVE_MESSAGE：在线时正常接收消息，离线时接收离线推送通知
- V2TIM_NOT_RECEIVE_MESSAGE：在线和离线都不接收消息
- V2TIM_RECEIVE_NOT_NOTIFY_MESSAGE：在线时正常接收消息，离线时不接收离线推送通知

您可以调用 [setC2CReceiveMessageOpt](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/setC2CReceiveMessageOpt.html) 接口设置单聊消息免打扰，调用 [setGroupReceiveMessageOpt](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/setGroupReceiveMessageOpt.html) 接口设置群聊消息免打扰。


## 撤回消息

发送方通过  [revokeMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/revokeMessage.html) 接口可以撤回一条已经发送成功的消息。默认情况下，发送者只能撤回2分钟以内的消息，您可以按需更改消息撤回时间限制，具体操作请参见 [消息撤回设置](https://cloud.tencent.com/document/product/269/38656#.E6.B6.88.E6.81.AF.E6.92.A4.E5.9B.9E.E8.AE.BE.E7.BD.AE)。
消息撤回同时需要接收方 UI 代码的配合：当发送方撤回一条消息后，接收方会收到消息撤回通知 [onRecvMessageRevoked](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_callbacks/OnRecvMessageRevokedCallback.html)，通知中包含了撤回消息的 `msgID`，您可以根据这个 `msgID` 判断 UI 层是哪一条消息撤回了，然后把对应的消息气泡切换成 "消息已被撤回" 状态。

### 发送方撤回一条消息

 ```dart
 V2TimCallback res =
        await TencentImSDKPlugin.v2TIMManager.getMessageManager().revokeMessage(msgID: msgID,);
 ```

### 接收方感知消息被撤回

1. 调用 [addAdvancedMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/addAdvancedMsgListener.html) 设置高级消息监听。
2. 通过 [onRecvMessageRevoked](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimAdvancedMsgListener/V2TimAdvancedMsgListener/onRecvMessageRevoked.html) 接收消息撤回通知。

```dart

 void onRecvMessageRevoked(String msgID) {
	// msgList 为当前聊天界面的消息列表
	for (V2TIMMessage msg in msgList) {
		if (msg.msgID == msgID) {
				// msg 即为被撤回的消息，您需要修改 UI 上相应的消息气泡的状态
		}
	}
}
```

## 清空未读消息数
### 清空单个会话的未读数
接收方调用 [markC2CMessageAsRead](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/markC2CMessageAsRead.html) 和 [markGroupMessageAsRead](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/markGroupMessageAsRead.html) 可以分别清空某个 C2C 单聊会话或者群聊会话的未读数，并会回调 [onConversationChanged](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimConversationListener/V2TimConversationListener/onConversationChanged.html) 方法通知界面更新。
### 一键清空所有会话的未读数
接收方调用 [markAllMessageAsRead](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/markAllMessageAsRead.html) 可以实现一键清空所有会话的未读数，并会回调 [onConversationChanged](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimConversationListener/V2TimConversationListener/onConversationChanged.html) 方法通知界面更新。

## 给消息增加已读回执
在 C2C 单聊场景下，当接收方通过 [markC2CMessageAsRead](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/markC2CMessageAsRead.html) 接口将来自某人的消息标记为已读时，消息的发送方将会收到“已读回执”，表示“xxx 已经读过我的消息了”。

>?目前仅 C2C 单聊消息支持已读回执，群聊场景暂不支持。虽然群聊消息也有对应的 [markGroupMessageAsRead](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/markGroupMessageAsRead.html) 接口，但群消息的发送者目前无法收到已读回执。

### 接收方标记消息已读

 ```dart
 //将来自 haven 的消息均标记为已读
    V2TimCallback res = await TencentImSDKPlugin.v2TIMManager
        .getMessageManager()
        .markC2CMessageAsRead(
          userID: "haven_userID",
        );
 ```

### 发送方感知消息已读
消息已读回执的事件通知位于高级消息监听器 [V2TimAdvancedMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimAdvancedMsgListener/V2TimAdvancedMsgListener-class.html) 中，如需支持感知消息已读，需要先通过 [addAdvancedMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/addAdvancedMsgListener.html) 设置监听器，然后通过 [onRecvC2CReadReceipt](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/enum_V2TimAdvancedMsgListener/V2TimAdvancedMsgListener/onRecvC2CReadReceipt.html) 回调即可感知接收方的已读确认。

```dart
void onRecvC2CReadReceipt(List<V2TimMessageReceipt> receiptList) {
	// 由于发送方一次性可能会收到多个已读回执，所以这里采用了数组的回调形式
	for (V2TimMessageReceipt  receipt in receiptList) {
		// 消息接收者 receiver
		String userID = receipt.userID;
		// 已读回执时间，聊天窗口中时间戳小于或等于 timestamp 的消息都可以被认为已读
		int timestamp = receipt.timestamp;
	}
}
```

## 查看历史消息
您可以调用 [getC2CHistoryMessageList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getC2CHistoryMessageList.html) 获取单聊历史消息，调用 [getGroupHistoryMessageList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getGroupHistoryMessageList.html) 获取群聊历史消息。如果当前设备网络连接正常，SDK 会默认从服务器拉取历史消息；如果没有网络连接，SDK 会直接从本地数据库中读取历史消息。

### 分页拉取历史消息
SDK 支持分页拉取历史消息，一次分页拉取的消息数量不宜太大，否则会影响拉取速度，建议一次最多拉取20条。
本文以分页拉取名为 `groupA` 的群的历史消息，每次分页拉取20条为例，示例代码如下：

```dart
// 第一次拉取 lastMsg 传 null，表示从最新的消息开始拉取 20 条消息
    V2TimValueCallback<List<V2TimMessage>> res = await TencentImSDKPlugin
        .v2TIMManager
        .getMessageManager()
        .getGroupHistoryMessageList(
          groupID: "groupID",
          count: 20,
        );
    List<V2TimMessage> msgList = res.data ?? [];
    if (msgList.isNotEmpty) {
      lastMsgID = msgList[msgList.length - 1].msgID;
      V2TimValueCallback<List<V2TimMessage>> nextRes = await TencentImSDKPlugin
          .v2TIMManager
          .getMessageManager()
          .getGroupHistoryMessageList(
            groupID: "groupID",
            count: 20,
            lastMsgID: lastMsgID,
          );
		  // ...
    }
```

现实场景中的分页拉取，通常由用户的滑动操作触发的，用户每下拉一次消息列表就触发一次分页拉取。但原理上跟上述示例代码类似，都是以 `lastMsg` 作为分页的标记，以 `count` 控制每次拉取的消息条数。

### 历史消息的注意事项
- 历史消息存储时长如下：<ul style="margin:0;"><li>体验版：免费存储7天，不支持延长</li><li>专业版：免费存储7天，支持延长</li><li>旗舰版：免费存储30天，支持延长</li></ul>延长历史消息存储时长是增值服务，您可以登录 <a href="https://console.cloud.tencent.com/im">即时通信 IM 控制台</a> 修改相关配置，具体计费说明请参见 <a href="https://cloud.tencent.com/document/product/269/11673#zz">增值服务资费</a>。
- 只有会议群（Meeting）（对应老版本的 ChatRoom 群）才支持拉取到用户**入群之前**的历史消息。
- 直播群（AVChatRoom）中的消息均不支持本地存储和多终端漫游，因此对直播群调用 [getGroupHistoryMessageList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/getGroupHistoryMessageList.html) 接口是无效的。

## 删除消息
对于历史消息，您可以调用 [deleteMessages](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/deleteMessages.html) 接口删除历史消息，消息删除后，无法再恢复。

## 设置消息权限
### 只允许好友间收发消息
SDK 默认不限制非好友之间收发消息。如果您希望仅允许好友之间发送单聊消息，您可以在 [**即时通信 IM 控制台**](https://console.cloud.tencent.com/im) > **功能配置** > **登录与消息** > **好友关系检查** 中开启"发送单聊消息检查关系链"。开启后，用户只能给好友发送消息，当用户给非好友发消息时，SDK 会报20009错误码。

### 不接收某人的消息
不接收某人消息可以选择拉黑某人或则设置某人消息免打扰，拉黑某人后再也收不到对方的任何消息，设置消息免打扰后可以更改消息 [免打扰状态](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessage.html#a90a89f5b4855dad72b784101667998c5)，flutter IM SDK中请使用ReceiveMsgOptEnum枚举来进行获取
**拉黑某人：**
调用 [addToBlackList](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/addToBlackList.html) 接口把该用户加入黑名单，即拉黑该用户。
当消息发送者被拉黑后，发送者默认不会感知到“被拉黑”的状态，即发送消息后仍展示发送成功（实际上此时接收方不会收到消息）。如果需要被拉黑的发送者收到消息发送失败的提示，请在 [**即时通信 IM 控制台**](https://console.cloud.tencent.com/im) > **功能配置** > **登录与消息** > **黑名单检查** 中关闭"发送消息后展示发送成功"，关闭后，被拉黑的发送者在发送消息时，SDK 会报20007错误码。
**设置某人消息免打扰：**
调用 [setC2CReceiveMessageOpt](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/setC2CReceiveMessageOpt.html) 接口，设置消息接收选项为 `ReceiveMsgOptEnum.V2TIM_NOT_RECEIVE_MESSAGE` 状态。

### 不接收某个群组的消息

调用 [setGroupReceiveMessageOpt](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/setGroupReceiveMessageOpt.html) 接口，设置消息接收选项为 `ReceiveMsgOptEnum.V2TIM_NOT_RECEIVE_MESSAGE` 状态。
其他 SDK 版本，请调用 `setReceiveMessageOpt` 接口，设置群消息接收选项为 `ReceiveMsgOptEnum.V2TIM_GROUP_NOT_RECEIVE_MESSAGE` 状态。

## 敏感词过滤
SDK 发送的文本消息默认会经过即时通信 IM 的敏感词过滤，如果发送者在发送的文本消息中包含敏感词，SDK 会报 80001 错误码。
![](https://main.qcloudimg.com/raw/63625c5252348205993ec5f33b087dec.png)

## 常见问题
### 1. 为什么会收到重复的消息？
请检查以下逻辑是否正确：
- 请检查 [addSimpleMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/addSimpleMsgListener.html) 与 [addAdvancedMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/addAdvancedMsgListener.html) 是否混用。如果混用，当收到文本消息或自定义消息时，两个监听都会回调，会导致收到重复消息。
- 请检查同一个监听对象是否重复 `add`（现在支持重复监听），如果监听对象不再使用，请主动调用对应的 [removeSimpleMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/removeSimpleMsgListener.html) 或 [removeAdvancedMsgListener](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/removeAdvancedMsgListener.html) 接口移除多余的监听器。

### 2. App 卸载重装后已读回执为什么失效了？
在单聊场景下，接收方如果调用 [markC2CMessageAsRead](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/im_flutter_plugin_platform_interface/ImFlutterPlatform/markC2CMessageAsRead.html) 设置消息已读，发送方收到的已读回执里面包含了对方已读的时间戳 `timestamp`，SDK 内部会根据 `timestamp` 判断消息对方是否已读， `timestamp` 目前只在本地保存，程序卸载重装后会丢失。

### 3. 如何解析多个 Elem 的消息？
1. 通过 `Message` 对象正常解析出第一个 `Elem` 对象。
2. 通过第一个 `Elem` 对象的 [nextElem](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_elem/V2TIMElem/nextElem.html) 方法获取下一个 `Elem` 对象。如果下一个 `Elem` 对象存在，会返回 `Elem` 对象实例，如果不存在，会返回 `null`。
```dart

 onRecvNewMessage(V2TimMessage msg) {
	// 查看第一个 Elem
	int elemType = msg.elemType;
	if (elemType == MessageElemType.V2TIM_ELEM_TYPE_TEXT) {
		// 文本消息
		V2TIMTextElem v2TIMTextElem = msg.textElem;
		String text = v2TIMTextElem.text;
		// 查看 v2TIMTextElem 后面还有没有更多 elem
		V2TIMElem elem = v2TIMTextElem.nextElem;
		while (elem != null) {
			// 判断 elem 类型，以 V2TIMCustomElem 为例
			if (elem is V2TIMCustomElem) {
				
				String? data = customElem?.data;
			}
			// 继续查看当前 elem 后面还有没更多 elem
			elem = nextElem;
		}
		// elem 如果为 null，表示所有 elem 都已经解析完
	}
}
```

[](id:msgAnalyze)
### 4. 各种不同类型的消息应该如何解析？
解析消息相对复杂，我们提供了各种类型消息解析的 [示例代码](https://github.com/tencentyun/TIMSDK/blob/master/Flutter/Demo/im_discuss/lib/pages/conversion/component/common_content.dart)，您可以直接把相关代码拷贝到您的工程，然后根据实际需求进行二次开发。
