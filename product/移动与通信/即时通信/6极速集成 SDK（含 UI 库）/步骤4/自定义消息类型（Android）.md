
TUIKit 已经在内部完成了基本消息的渲染工作，您可以很简单地通过属性设置来调节消息展示样式，也可以重新自定义消息样式。

## 基本消息类型
TUIKit 基本消息类型请参见 [MessageInfo.java](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/message/MessageInfo.html)。
<table>
     <tr>
         <th width="40%" align="center">消息类型</th>  
         <th align="center">显示效果图</th>  
     </tr>
	 <tr>      
         <td align="center">文本类消息</td>   
	     <td align="center"><img src="https://main.qcloudimg.com/raw/6535b0a414d4dd51aabab464f0980ca3.png" /></td>   
     </tr> 
	 <tr>      
         <td align="center">图片类消息</td>   
	     <td align="center"><img src="https://main.qcloudimg.com/raw/1f5330a92c688b6288bbd47f97202867.png" /></td>   
     </tr> 
	 <tr>      
         <td align="center">语音类消息</td>   
	     <td align="center"><img src="https://main.qcloudimg.com/raw/5387ea2450e7fe37daa59efb163e93b6.png" /></td>   
     </tr> 
	 <tr>      
         <td align="center">视频类消息</td>   
	     <td align="center"><img src="https://main.qcloudimg.com/raw/eb50c8cefa0decf1eef1c896c44e6188.png" /></td>   
     </tr> 
	 <tr>      
         <td align="center">文件类消息</td>   
	     <td align="center"><img src="https://main.qcloudimg.com/raw/4be73ac319f7693916ee08b98f14c4c6.png" /></td>   
     </tr> 
</table>

## 自定义消息
如果基本消息类型不能满足您的需求，您可以根据实际业务需求自定义消息。
本文以发送一条可跳转至浏览器的超文本作为自定义消息为例，帮助您快速了解实现流程。

### 创建一条自定义消息

`MessageInfoUtil`类可以帮助您实现各种消息类型，包括自定义消息，例如用 JSON 串来创建一条消息：
```java
MessageInfo info = MessageInfoUtil.buildCustomMessage("{\"text\": \"欢迎加入即时通信 IM 大家庭！查看详情>>\",\"url\": \"https://cloud.tencent.com/product/im"}");
```

### 发送一条自定义消息

您可以通过`ChatLayout`的实例发送自定义消息：
```java
chatLayout.sendMessage(info)
```


### 渲染自定义消息

自定义消息的定义、解析与展示完全由您根据实际业务需求实现，通过 TUIKit 透传发送到对方，TUIKit 在渲染这条消息时也会调用您实现的回调，您的回调一般包括以下流程：
1. 解析自定义消息。
2. 根据解析结果创建显示的 View。
3. 将创建的 View 添加到 TUIKit 的父容器里。
4. 实现 View 的交互逻辑。

渲染自定义消息的流程如下图所示：
![](https://main.qcloudimg.com/raw/4c42314623c5a088cc2337da66378fec.png)

TUIKit 会在内部通过消息的类型获知该条消息是自定义消息，渲染到该条消息时会通过回调通知您，并调用您的布局以及实现逻辑，所以您只需将实现了`IOnCustomMessageDrawListener`的监听传入到 TUIKit 即可。
```java
// 设置自定义的消息渲染时的回调
messageLayout.setOnCustomMessageDrawListener(new CustomMessageDraw());
```

### 示例代码

`CustomMessageDraw`实现了`IOnCustomMessageDrawListener`，并且在`onDraw`里完成了自定义消息的解析以及 View 的创建，示例代码将呈现一个完整的`CustomMessageDraw`实现：
```java
public static class CustomMessageDraw implements IOnCustomMessageDrawListener {

    /**
         * 自定义消息渲染时，会调用该方法，本方法实现了自定义消息的创建，以及交互逻辑
         * @param parent 自定义消息显示的父 View，需要把创建的自定义消息 View 添加到 parent 里
         * @param info 消息的具体信息
         */
    @Override
    public void onDraw(ICustomMessageViewGroup parent, MessageInfo info) {
        View view = null;
        // 获取到自定义消息的 JSON 数据
        TIMCustomElem elem = (TIMCustomElem) info.getTIMMessage().getElement(0);
        // 自定义的 JSON 数据，需要解析成 bean 实例
        final CustomMessageData customMessageData = new Gson().fromJson(new String(elem.getData()), CustomMessageData.class);
        // 通过类型来创建不同的自定义消息展示 View
        switch(customMessageData.type) {
            case CustomMessageData.TYPE_HYPERLINK:
                view = LayoutInflater.from(DemoApplication.instance()).inflate(R.layout.test_custom_message_layout1, null, false);
                // 把自定义消息 View 添加到 TUIKit 内部的父容器里
                parent.addMessageContentView(view);
                break;
            case CustomMessageData.TYPE_PUSH_TEXT_VIDEO:
                view = LayoutInflater.from(DemoApplication.instance()).inflate(R.layout.test_custom_message_layout2, null, false);
                // 把自定义消息 View 添加到 TUIKit 内部的父容器里
                parent.addMessageItemView(view);
                break;
        }

        // 自定义消息 View 的实现，这里仅仅展示文本信息，并且实现超链接跳转
        TextView textView = view.findViewById(R.id.test_custom_message_tv);
        textView.setText(customMessageData.text);
        textView.setClickable(true);
        textView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent();
                intent.setAction("android.intent.action.VIEW");
                Uri content_url = Uri.parse(customMessageData.url);
                intent.setData(content_url);
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                DemoApplication.instance().startActivity(intent);
            }
        });
    }
}

/**
 * 自定义消息的 bean 实体，用来与 JSON 的相互转化
 */
public static class CustomMessageData {
    // 超文本类型，点击可以跳转到一个 Webview
    final static int TYPE_HYPERLINK = 1;
    // 视频+说明类型
    final static int TYPE_PUSH_TEXT_VIDEO = 2;
    // 自定义消息类型，根据业务可能会有很多种
    int type = TYPE_HYPERLINK;
    String text = "欢迎加入即时通信 IM 大家庭！查看详情>>";
    String url = "https://cloud.tencent.com/document/product/269";
}
```

显示效果如下图所示：
![](https://main.qcloudimg.com/raw/019fe0810738f271b61cd1d7a33c5b03.png)
