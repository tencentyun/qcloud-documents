
`TUIKit` 已经在内部完成了基本消息的渲染工作，您可以很简单地通过属性设置来调节消息展示样式，也可以重新自定义消息样式。


## 基本消息类型
`TUIKit` 基本消息类型请参见 [MessageInfo.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/tuikit/src/main/java/com/tencent/qcloud/tim/uikit/modules/message/MessageInfo.java)。
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
>- 本文以发送一条可跳转至浏览器的超文本作为自定义消息为例，帮助您快速了解实现流程。**本文以 `5.4.666` 版本为例，与之前版本有所不同。**
>- 可以参考 [自定义欢迎消息实现](https://github.com/tencentyun/TIMSDK/blob/master/Android/app/src/main/java/com/tencent/qcloud/tim/demo/helper/HelloChatController.java) 和 [自定义群直播消息实现](https://github.com/tencentyun/TIMSDK/blob/master/Android/tuikit-live/src/main/java/com/tencent/qcloud/tim/tuikit/live/helper/TUIKitLiveChatController.java) 。

### 实现自定义消息的流程
自定义消息流程
<img src="https://main.qcloudimg.com/raw/47d8393a4fb6620102bc618b6c35623a.png" width="1000"/>
如图所示，自定义消息需要实现 `TUIChatControllerListener` 和 `TUIConversationControllerListener`；其中 `TUIChatControllerListener` 用来解析消息生成自定义的 `MessageInfo`、创建和填充要在聊天页面显示的自定义的 `ViewHolder`；`TUIConversationControllerListener` 用来生成要在会话页面显示的消息摘要。
>- `TUIKit 使用` `RecyclerView` 来展示消息，要想显示自定义消息，需要创建自定义消息的 `ViewHolder` 来存放展示消息内容的 `View`。
>- 需要尽早把自己的 `TUIChatControllerListener` 和 `TUIConversationControllerListener` 注册到 `TUIKitListenerManager` 中。
### 创建一条自定义欢迎消息
自定义 `MessageInfo`，并实现自定义消息的解析方法。
```java
public class HelloChatController implements TUIChatControllerListener {
    // 定义 HelloMessageInfo 继承自 MessageInfo
    static class HelloMessageInfo extends MessageInfo {
        // 消息类型 ID ，不可重复，包括不能与内置消息类型重复，建议使用大于 100002 的数字
        public static final int MSG_TYPE_HELLO = 100002;
    }

    // 实现 TUIChatControllerListener 的 createCommonInfoFromTimMessage 方法来解析生成 MessageInfo
    // 如果是自己定义的消息，则生成自定义的 MessageInfo 并返回，否则返回 null 表示无法处理
    @Override
    public IBaseInfo createCommonInfoFromTimMessage(V2TIMMessage timMessage) {
        if (timMessage.getElemType() == V2TIMMessage.V2TIM_ELEM_TYPE_CUSTOM) {
            V2TIMCustomElem customElem = timMessage.getCustomElem();
            if (customElem == null || customElem.getData() == null) {
                return null;
            }
            CustomHelloMessage helloMessage = null;
            try {
                helloMessage = new Gson().fromJson(new String(customElem.getData()), CustomHelloMessage.class);
            } catch (Exception e) {
                DemoLog.w(TAG, "invalid json: " + new String(customElem.getData()) + " " + e.getMessage());
            }
            if (helloMessage != null && TextUtils.equals(helloMessage.businessID, TUIKitConstants.BUSINESS_ID_CUSTOM_HELLO)) {
                MessageInfo messageInfo = new HelloMessageInfo();
                // 设置消息类型 ID， 必须设置
                messageInfo.setMsgType(HelloMessageInfo.MSG_TYPE_HELLO);
                // 设置
                MessageInfoUtil.setMessageInfoCommonAttributes(messageInfo, timMessage);
                Context context = TUIKit.getAppContext();
                if (context != null) {
                    messageInfo.setExtra(context.getString(R.string.custom_msg));
                }
                return messageInfo;
            }
        }
        return null;
    }

    ......

}
```
尽可能早地注册到 `TUIKitListenerManager` 中
```java
TUIKitListenerManager.getInstance().addChatListener(new HelloChatController());
```
可以由 JSON 字符串创建自定义消息
```java
Gson gson = new Gson();
CustomHelloMessage customHelloMessage = new CustomHelloMessage();
customHelloMessage.version = TUIKitConstants.version;
customHelloMessage.text = DemoApplication.instance().getString(R.string.welcome_tip);
customHelloMessage.link = "https://cloud.tencent.com/document/product/269/3794";

String data = gson.toJson(customHelloMessage); // data = {"businessID":"text_link","link":"https://cloud.tencent.com/document/product/269/3794","text":"欢迎加入云通信IM大家庭！","version":4}
// 根据 JSON 创建自定义消息，会调用上面重写的 createCommonInfoFromTimMessage 方法解析出 MessageInfo
MessageInfo info = MessageInfoUtil.buildCustomMessage(data);
```
### 发送一条自定义消息

您可以通过 `ChatLayout` 的实例发送自定义消息：
```java
MessageInfo info = MessageInfoUtil.buildCustomMessage(data);
chatLayout.sendMessage(info)
```
也可以使用 `MessageSender` 发送消息
```java
MessageInfo info = MessageInfoUtil.buildCustomMessage(data);
IBaseMessageSender messageSender = TUIKitListenerManager.getInstance().getMessageSender();
if (messageSender != null) {
    // 发送消息
    messageSender.sendMessage(info, null, chatInfoId,
            chatType == V2TIMConversation.V2TIM_GROUP, false, new IUIKitCallBack() {
                @Override
                public void onSuccess(Object data) {
                    Log.i("CustomChatController", "send success");
                }

                @Override
                public void onError(String module, int errCode, String errMsg) {
                    Log.i("CustomChatController", "send failed");
                }
            });
}
```

### 把自定义消息显示在聊天框里

#### 创建 ViewHolder
`TUIKit` 使用 `RecyclerView` 来展示消息，要想显示自定义消息，需要创建自定义消息的 `ViewHolder` 来存放展示消息内容的 `View`。
自定义消息的 `ViewHolder` 可以继承自 [基础消息 ViewHolder](https://github.com/tencentyun/TIMSDK/tree/master/Android/tuikit/src/main/java/com/tencent/qcloud/tim/uikit/modules/chat/layout/message/holder)。
```java
// 定义 HelloViewHolder 继承自 MessageCustomHolder
class HelloViewHolder extends MessageCustomHolder{

    public HelloViewHolder(View itemView) {
        super(itemView);
    }
}

// 实现 TUIChatControllerListener 的 createCommonViewHolder 方法来创建 ViewHolder
// 根据 viewType 创建自定义的 ViewHolder，如果不是自定义消息类型则返回 null
@Override
public IBaseViewHolder createCommonViewHolder(ViewGroup parent, int viewType) {
    if (viewType != HelloMessageInfo.MSG_TYPE_HELLO) {
        return null;
    }
    if (parent == null) {
        return null;
    }
    LayoutInflater inflater = LayoutInflater.from(TUIKit.getAppContext());
    View contentView = inflater.inflate(R.layout.message_adapter_item_content, parent, false);
    return new HelloViewHolder(contentView);
}
```
#### 设置自定义消息要显示的内容
`TUIKit` 展示消息时会调用 `bindCommonViewHolder` 方法，在 `bindCommonViewHolder` 中完成自定义消息内容的设置。
```java
// 实现 TUIChatControllerListener 的 bindCommonViewHolder 方法来填充 ViewHolder
// 如果是自定义 ViewHolder 则去设置显示内容并且返回 true 表示已经处理，否则返回 false
@Override
public boolean bindCommonViewHolder(IBaseViewHolder baseViewHolder, IBaseInfo baseInfo, int position) {
    if (baseViewHolder instanceof ICustomMessageViewGroup && baseInfo instanceof HelloMessageInfo) {
        ICustomMessageViewGroup customHolder = (ICustomMessageViewGroup) baseViewHolder;
        MessageInfo msg = (MessageInfo) baseInfo;
        new CustomMessageDraw().onDraw(customHolder, msg, position);
        return true;
    }
    return false;
}
```

### 把自定义消息摘要显示在会话列表中
```java
// 定义 HelloConversationController 实现 TUIConversationControllerListener 接口
public static class HelloConversationController implements TUIConversationControllerListener {
    // 获取要显示到会话列表的摘要字符串，如果不是自己的消息返回 null 表示不处理
    @Override
    public CharSequence getConversationDisplayString(IBaseInfo baseInfo) {
        if (baseInfo instanceof HelloChatController.HelloMessageInfo) {
            return DemoApplication.instance().getString(R.string.welcome_tip);
        }
        return null;
    }
}
// 尽可能早地注册到 TUIKitListenerManager 中，以便打开会话列表就能正确显示自定义消息摘要
TUIKitListenerManager.getInstance().addConversationListener(new HelloChatController.HelloConversationController());
```

### 自定义欢迎消息显示效果
**在消息列表中显示自定义欢迎消息**
<img src="https://main.qcloudimg.com/raw/95467274340c18d2d22872684eed3500.png" width="500"/>

**在会话列表中显示自定义欢迎消息的消息摘要**
<img src="https://main.qcloudimg.com/raw/912ca467334d20ab3f74af756b833083.png" width="500"/>


