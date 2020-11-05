
TUIKit 已经在内部完成了基本消息的渲染工作，您可以很简单地通过属性设置来调节消息展示样式，也可以重新自定义消息样式。


## 基本消息类型
TUIKit 基本消息类型请参见 [MessageInfo.java](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/modules/message/MessageInfo.html)。
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
如果基本消息类型不能满足您的需求，您可以根据实际业务需求自定义消息。
本文以发送一条可跳转至浏览器的超文本作为自定义消息为例，帮助您快速了解实现流程。

### 创建一条自定义消息

MessageInfoUtil 类可以帮助您实现各种消息类型，包括自定义消息，例如用 JSON 串来创建一条消息：
```java
MessageInfo info = MessageInfoUtil.buildCustomMessage("{\"text\": \"欢迎加入即时通信 IM 大家庭！查看详情>>\",\"url\": \"https://cloud.tencent.com/product/im"}");
```

### 发送一条自定义消息

您可以通过 ChatLayout 的实例发送自定义消息：
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
![](https://main.qcloudimg.com/raw/644f6a44045300f48d98440ceb150bb3.png)

TUIKit 会在内部通过消息的类型获知该条消息是自定义消息，渲染到该条消息时会通过回调通知您，并调用您的布局以及实现逻辑，所以您只需将实现了`IOnCustomMessageDrawListener`的监听传入到 TUIKit 即可。
```java
// 设置自定义的消息渲染时的回调
messageLayout.setOnCustomMessageDrawListener(new CustomMessageDraw());
```

### 示例代码

下列示例代码将呈现一个完整的自定义消息解析的过程，您也可以直接 [下载](https://github.com/tencentyun/TIMSDK/blob/master/Android/app/src/main/java/com/tencent/qcloud/tim/demo/helper/ChatLayoutHelper.java) 完整的 Demo。
```java
public class CustomMessageDraw implements IOnCustomMessageDrawListener {

	/**
	 * 自定义消息渲染时，会调用该方法，本方法实现了自定义消息的创建，以及交互逻辑
	 *
	 * @param parent 自定义消息显示的父View，需要把创建的自定义消息view添加到parent里
	 * @param info   消息的具体信息
	 */
	@Override
	public void onDraw(ICustomMessageViewGroup parent, MessageInfo info) {
		// 获取到自定义消息的json数据
		if (info.getTimMessage().getElemType() != V2TIMMessage.V2TIM_ELEM_TYPE_CUSTOM) {
			return;
		}
		V2TIMCustomElem elem = info.getTimMessage().getCustomElem();
		// 自定义的json数据，需要解析成bean实例
		CustomHelloMessage data = null;
		try {
			data = new Gson().fromJson(new String(elem.getData()), CustomHelloMessage.class);
		} catch (Exception e) {
			DemoLog.w(TAG, "invalid json: " + new String(elem.getData()) + " " + e.getMessage());
		}
		if (data == null) {
			DemoLog.e(TAG, "No Custom Data: " + new String(elem.getData()));
		} else if (data.version == TUIKitConstants.JSON_VERSION_1
				|| (data.version == TUIKitConstants.JSON_VERSION_4 && data.businessID.equals("text_link"))) {
			CustomHelloTIMUIController.onDraw(parent, data);
		} else {
			DemoLog.w(TAG, "unsupported version: " + data);
		}
	}
}
```

显示效果如下图所示：
![](https://main.qcloudimg.com/raw/019fe0810738f271b61cd1d7a33c5b03.png)
