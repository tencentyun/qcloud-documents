
`TUIKit` 已经在内部完成了基本消息的渲染工作，您可以很简单地通过属性设置来调节消息展示样式，也可以重新自定义消息样式。


## 基本消息类型
`TUIKit` 基本消息类型请参见 [MessageInfo.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIChat/tuichat/src/main/java/com/tencent/qcloud/tuikit/tuichat/bean/MessageInfo.java)。
<table>
     <tr>
         <th width="20%" style="text-align:center">消息类型</th>  
         <th style="text-align:center">显示效果图</th>  
     </tr>
	 <tr>      
         <td style="text-align:center">文本类消息</td>   
	 <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/6535b0a414d4dd51aabab464f0980ca3.png" width="320"/></td>   
     </tr> 
	 <tr>      
         <td style="text-align:center">图片类消息</td>   
	 <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/1f5330a92c688b6288bbd47f97202867.png" width="320"/></td>   
     </tr> 
	 <tr>      
         <td style="text-align:center">语音类消息</td>   
	 <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/5387ea2450e7fe37daa59efb163e93b6.png" width="320"/></td>   
     </tr> 
	 <tr>      
         <td style="text-align:center">视频类消息</td>   
	 <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/eb50c8cefa0decf1eef1c896c44e6188.png" width="320"/></td>   
     </tr> 
	 <tr>      
         <td style="text-align:center">文件类消息</td>   
	 <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/4be73ac319f7693916ee08b98f14c4c6.png" width="320"/></td>   
     </tr> 
</table>

## 自定义消息
>- 如果基本消息类型不能满足您的需求，您可以根据实际业务需求自定义消息。
>- 本文以发送一条可跳转至浏览器的超文本作为自定义消息为例，帮助您快速了解实现流程。**本文以 `5.7.1435` 版本为例，与之前版本有所不同。**

### 自定义欢迎消息显示效果
**在消息列表中显示自定义欢迎消息**

<img src="https://main.qcloudimg.com/raw/95467274340c18d2d22872684eed3500.png" width="500"/>

**在会话列表中显示自定义欢迎消息的消息摘要**

<img src="https://main.qcloudimg.com/raw/912ca467334d20ab3f74af756b833083.png" width="500"/>

## 实现自定义消息

### 步骤1：解析自定义消息
[MessageInfo.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIChat/tuichat/src/main/java/com/tencent/qcloud/tuikit/tuichat/bean/MessageInfo.java) 用来存储要在消息列表中渲染的消息数据。[ChatMessageInfoUtil.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIChat/tuichat/src/main/java/com/tencent/qcloud/tuikit/tuichat/util/ChatMessageInfoUtil.java) 用来把 `V2TIMMessage` 解析为 `MessageInfo`。
收到自定义消息之后，在 [ChatMessageInfoUtil.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIChat/tuichat/src/main/java/com/tencent/qcloud/tuikit/tuichat/util/ChatMessageInfoUtil.java) 的 `createCustomMessageInfo` 方法中进行解析：
```java
...

V2TIMCustomElem customElem = timMessage.getCustomElem();
if (customElem == null || customElem.getData() == null) {
    return null;
}
String data = new String(customElem.getData());

Gson gson = new Gson();
HashMap customJsonMap = null;
try {
    customJsonMap = gson.fromJson(data, HashMap.class);
} catch (JsonSyntaxException e) {
    TUIChatLog.e(TAG, " getCustomJsonMap error ");
}
String businessId = null;
if (customJsonMap != null) {
    businessIdObj = customJsonMap.get(TUIConstants.Message.CUSTOM_BUSINESS_ID_KEY);
}
if (businessIdObj instanceof String) {
    businessId = (String) businessIdObj;
}
// 欢迎消息
if (TextUtils.equals(businessId, "text_link")) {
    msgInfo.setMsgType(MessageInfo.MSG_TYPE_CUSTOM);
    msgInfo.setExtra(customJsonMap.get("text"));
}

...
```

### 步骤2：在消息列表中渲染自定义消息
[MessageCustomHolder.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIChat/tuichat/src/main/java/com/tencent/qcloud/tuikit/tuichat/ui/view/message/viewholder/MessageCustomHolder.java) 用来渲染各种自定义消息。收到自定义消息之后，[MessageCustomHolder.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIChat/tuichat/src/main/java/com/tencent/qcloud/tuikit/tuichat/ui/view/message/viewholder/MessageCustomHolder.java)  根据解析出的 `MessageInfo` 在 `layoutViews` 方法中进行自定义消息的渲染：
```java
...

String data = new String(msg.getCustomElemData());
Gson gson = new Gson();
HashMap customJsonMap = null;
try {
    customJsonMap = gson.fromJson(data, HashMap.class);
} catch (JsonSyntaxException e) {
    TUIChatLog.e("MessageCustomHolder", " getCustomJsonMap error ");
}
String businessId = null;
Object businessIdObj = null;
if (customJsonMap != null) {
    businessIdObj = customJsonMap.get(TUIConstants.Message.CUSTOM_BUSINESS_ID_KEY);
}
if (businessIdObj instanceof String) {
    businessId = (String) businessIdObj;
}

// 渲染欢迎消息
if (TextUtils.equals(businessId, TUIChatConstants.BUSINESS_ID_CUSTOM_HELLO)) {
    drawCustomHelloMessage(msg, position);
} 

...
```
### 步骤3: 在会话列表中渲染自定义消息
[ConversationMessageInfo.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIConversation/tuiconversation/src/main/java/com/tencent/qcloud/tuikit/tuiconversation/bean/ConversationMessageInfo.java) 用来存储要在会话列表中渲染的消息数据。
[ConversationMessageInfoUtil.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIConversation/tuiconversation/src/main/java/com/tencent/qcloud/tuikit/tuiconversation/util/ConversationMessageInfoUtil.java) 用来把 `V2TIMMessage` 解析为 `ConversationMessageInfo`。
收到自定义消息之后，在 [ConversationMessageInfoUtil.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIConversation/tuiconversation/src/main/java/com/tencent/qcloud/tuikit/tuiconversation/util/ConversationMessageInfoUtil.java)  的 `createCustomMessageInfo` 方法中进行解析：
```java
// 欢迎消息
if (TextUtils.equals(businessId, "text_link")) {
    msgInfo.setMsgType(MessageInfo.MSG_TYPE_CUSTOM);
    msgInfo.setExtra(customJsonMap.get("text"));
}
```
## 发送自定义消息
 <img src="https://main.qcloudimg.com/raw/80ff0af0e44bde79d099cd5296b3136f.jpg" width = "400" height = "400" align=center />

 [ChatLayoutSetting.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIChat/tuichat/src/main/java/com/tencent/qcloud/tuikit/tuichat/setting/ChatLayoutSetting.java) 用来设置聊天界面的控件和样式，在  [ChatLayoutSetting.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIChat/tuichat/src/main/java/com/tencent/qcloud/tuikit/tuichat/setting/ChatLayoutSetting.java) 的 `customizeChatLayout` 方法中添加以下代码，用来添加自定义消息发送按钮和发送按钮点击后的发送消息事件： 
 ```java
InputMoreActionUnit unit = new InputMoreActionUnit() {};
unit.setIconResId(R.drawable.custom);
unit.setTitleId(R.string.test_custom_action);
unit.setActionId(CustomHelloMessage.CUSTOM_HELLO_ACTION_ID);
unit.setPriority(10);
unit.setOnClickListener(unit.new OnActionClickListener() {
    @Override
    public void onClick() {
        CustomHelloMessage customHelloMessage = new CustomHelloMessage();
        customHelloMessage.version = TUIChatConstants.version;
        Gson gson = new Gson();
        String data = gson.toJson(customHelloMessage);
        MessageInfo info = ChatMessageInfoUtil.buildCustomMessage(data, customHelloMessage.text, customHelloMessage.text.getBytes());
        layout.sendMessage(info, false);
    }
});
inputView.addAction(unit);
// 消息内容为
// data = {"businessID":"text_link","link":"https://cloud.tencent.com/document/product/269/3794","text":"欢迎加入云通信IM大家庭！","version":4}
```
