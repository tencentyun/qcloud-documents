本文介绍如何设置 H5 界面风格。 
## 设置会话列表
 TUIConversation 提供会话列表功能。会话列表主要由会话列表区组成，会话列表区提供了 UI 样式可供修改。
<img src="https://qcloudimg.tencent-cloud.cn/raw/dfe7aadf60331036ba599aaa4d1915e6.png" style="zoom:50.7%;"/>

### 设置会话列表样式

登录后 TUIKit 会根据用户名从 SDK 读取该用户的会话列表。会话列表提供一些常用功能定制，例如，头像样式、背景、字体大小、点击与长按事件等。
会话列表中单个列表项展示主要在路径 `src/TUIKit/TUIComponents/container/TUIConversation/components/list-item/index.vue` 文件中。
示例代码如下：
<dx-codeblock>
:::  html
<!-- 会话列表中单个会话列表项展示 -->
<li ref="content">
	<div class="TUI-conversation-item">
		<aside class="left">
			<!-- 头像 -->
			<img class="avatar" :src="handleConversation?.avator(conversation)">
			<!-- 消息未读数/红点 -->
			<span class="num" v-if="conversation.unreadCount>0 && conversation.messageRemindType !== 'AcceptNotNotify'">
				{{conversation.unreadCount > 99 ? '99+' : conversation.unreadCount}}
			</span>
			<span class="num-notify" v-if="conversation.unreadCount>0 && conversation.messageRemindType === 'AcceptNotNotify'"></span>
		</aside>
		<div class="content">
			<div class="content-header">
				<!-- 会话名称 -->
				<label>
					<p class="name">{{handleConversation?.name(conversation)}}</p>
				</label>
				<!-- 会话最新消息展示/@提示 -->
				<div class="middle-box">
					<span class="middle-box-at"  v-if="conversation.type === 'GROUP' && conversation.groupAtInfoList.length > 0">{{handleConversation?.showAt(conversation)}}</span>
					<p>{{handleConversation?.showMessage(conversation)}}</p>
				</div>
			</div>
			<div class="content-footer">
				<!-- 会话最新消息时间 -->
				<span class="time">{{handleConversation?.time(conversation.lastMessage.lastTime)}}</span>
				<!-- 会话是否设置免打扰 -->
				<img v-if="conversation.messageRemindType === 'AcceptNotNotify'" class="mute-icon" src="../../../../assets/icon/mute.svg">
				<i></i>
			</div>
		</div>
	</div>
	<!-- 会话菜单栏 -->
	<div class="dialog dialog-item"  v-if="toggle" ref="dialog">...</div>
</li>
:::
</dx-codeblock>
您可以在在路径 `src/TUIKit/TUIComponents/container/TUIConversation/components/list-item/style/h5.scss` 下设置会话列表中列表项的样式。
设置会话列表中头像样式示例代码如下：
<dx-codeblock>
:::  scss
.TUI-conversation-item {
	.left {
		.avatar {
			width: 30px;// 设置头像的宽度
			height: 30px;// 设置头像的高度
			border: 5px;// 设置头像形状为圆角
		}
	}
}
:::
</dx-codeblock>

## 设置聊天窗口的样式
TUIChat提供聊天窗口。聊天窗口包含三个区域，从上到下为标题栏区、消息区和输入区，如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/5293586c365b7cfdc3c8c41c368e72b7.png" style="zoom:50%;"/>
聊天窗口相关配置主要在路径 `src/TUIKit/TUIComponents/container/TUIChat/index.vue` 文件中。

### 设置标题栏区样式
标题栏有左中右两个区域组成，如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/499740506a63f530dc43b7416d92df20.png" style="zoom:30%;"/> 
聊天窗口标题栏相关代码主要在路径 `src/TUIKit/TUIComponents/container/TUIChat/index.vue` 文件中。聊天窗口标题栏区提供一些常用功能定制，例如，背景、字体大小、按钮图标、点击事件、功能开关等。
示例代码如下：
<dx-codeblock>
:::  html
<header class="TUIChat-header">
	<!-- 返回按钮 -->
	<i class="icon icon-back" @click="back" v-if="env.isH5"></i>
	<!-- 聊天窗口名/【正在输入中...】状态提示 -->
	<typing-header
		:needTyping="needTyping"//【正在输入中...】状态提示开关，如需关闭此功能请传入false
		...
	/>
	<!-- 群聊天设置（仅限群聊天窗口） -->
	<aside class="setting">
		<Manage v-if="conversation.groupProfile" :conversation="conversation" :userInfo="userInfo" :isH5="env.isH5" />
	</aside>
</header>
:::
</dx-codeblock> 
您可以在 `src/TUIKit/TUIComponents/container/TUIChat/style/h5.scss` 文件中设置聊天窗口标题栏区样式。
设置聊天窗口标题栏区的字体大小和背景色示例代码如下：
<dx-codeblock>
:::  scss
.TUIChat-H5 {
  .TUIChat-header {
    background-color: #147AFF;// 设置聊天窗口标题栏背景色
    h1 {
      font-size: 16px;// 设置聊天窗口标题栏字体大小
    }
  }
}
:::
</dx-codeblock>

### 设置消息区样式
#### 设置聊天窗口的背景
您可以在路径 `src/TUIKit/TUIComponents/container/TUIChat/style/h5.scss` 下自定义设置聊天背景色或背景图片。
设置聊天窗口消息区的背景色的示例代码如下：
<dx-codeblock>
:::  scss
.TUIChat-H5 
	.TUIChat-main {
		.TUI-message-list {
			background-color: #006EFF;// 设置聊天窗口消息区的背景色
		}
	}
}
:::
</dx-codeblock>
设置聊天窗口消息区的背景图片的示例代码如下：
<dx-codeblock>
:::  scss
.TUIChat-H5 
	.TUIChat-main {
		.TUI-message-list {
			 // 设置聊天窗口消息区的背景图片
			background-image: url(https://im.sdk.qcloud.com/download/tuikit-resource/avatar/avatar_6.png);
		}
	}
}
:::
</dx-codeblock>

#### 设置发送者的头像样式
消息区中的头像相关代码主要在路径 `src/TUIKit/TUIComponents/container/TUIChat/components/message-bubble.vue` 文件中。如果用户没有设置头像会显示默认头像，您可以自定义设置默认头像、头像是否圆角以及头像大小等。
设置默认头像示例代码如下：
<dx-codeblock>
:::  html
<!-- 设置默认头像路径为https://web.sdk.qcloud.com/component/TUIKit/assets/avatar_21.png  -->
<img
	class="avatar"
	:src="message?.avatar || 'https://web.sdk.qcloud.com/component/TUIKit/assets/avatar_21.png'"
	onerror="this.src='https://web.sdk.qcloud.com/component/TUIKit/assets/avatar_21.png'"
/>
:::
</dx-codeblock>
设置头像形状、大小示例代码如下：
<dx-codeblock>
:::  scss
.avatar {
	width: 36px;// 设置头像宽度
	height: 36px;// 设置头像高度
	border-radius: 5px; // 设置头像为圆角
}
:::
</dx-codeblock>

#### 设置气泡的背景色
消息区中单条消息包括 avatar 头像、messageArea 内容区以及 messageLabel 标签区组成。结构如图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/ca91179dcfec41166e0960d1991cc94f.png" style="zoom:30%;"/>
聊天窗口消息区中，左边为对方的气泡，右边为自己的气泡，你可以在路径  `src/TUIKit/TUIComponents/container/TUIChat/components/message-bubble.vue` 文件中自定义设置双方的气泡背景。
设置消息气泡颜色示例代码如下：
<dx-codeblock>
:::  scss
.message-area {
	.content {
		&-in {
			background: #fbfbfb;// 设置左边接收对方消息气泡颜色
			border-radius: 0px 10px 10px 10px;
		}
		&-out {
			background: #dceafd;// 设置右边本人发送消息气泡颜色
			border-radius: 10px 0px 10px 10px;
		}
	}
}
:::
</dx-codeblock>

#### 设置发送者的昵称样式
你可以在路径 `src/TUIKit/TUIComponents/container/TUIChat/components/message-bubble.vue` 文件中自定义设置昵称的字体大小与颜色等。
<dx-codeblock>
:::  scss
.message-area {
	.name {
		font-weight: 400;// 设置发送者昵称字体粗细
		font-size: 0.8rem; // 设置发送者昵称字体大小
		color: #999999;// 设置发送者昵称字体颜色
	}
}
:::
</dx-codeblock>

#### 设置聊天内容样式
您可以在路径 `src/TUIKit/TUIComponents/container/TUIChat/components/message-text.vue` 文件中自定义设置聊天内容的字体大小、双方字体颜色、emoji表情大小等。
设置聊天内容样式示例代码如下：
<dx-codeblock>
:::  scss
.text-img {
	width: 20px;// 设置聊天内容中emoji表情宽度
	height: 20px;// 设置聊天内容中emoji表情高度
}
.text-box {
	white-space: pre-wrap;
	font-size: 14px;// 设置聊天内容中字体大小
	color: #999999;// 设置聊天内容中字体颜色
}
:::
</dx-codeblock>

#### 设置聊天的提示信息样式

您可以在路径 `src/TUIKit/TUIComponents/container/TUIChat/components/message-tip.vue` 文件中自定义设置提示信息的背景、字体大小以及字体颜色等。
示例代码如下：
<dx-codeblock>
:::  scss
.message-tip {
	margin: 0 auto;
	color: #999999;// 设置提示信息字体颜色
	font-size: 14px;// 设置提示信息字体大小
	background: red;// 设置提示信息背景颜色
}
:::
</dx-codeblock>


### 设置输入区域 InputView
输入区域包含文字输入、表情输入、图片发送、视频发送、文件发送、评价发送、常用语发送等功能。
<img src="https://qcloudimg.tencent-cloud.cn/raw/4c3e91f5e5a4146a404713516f0e4dcb.png" style="zoom:30%;"/>

#### 隐藏不需要的功能
您可以自定义隐藏功能模块的发送图片、发送文件以及发送评价等功能。
输入区功能模块通过获取sendComponents中注册的功能模块来加载各项功能，sendComponents在路径  `src/TUIKit/TUIComponents/container/TUIChat/index.ts` 文件中进行注册，您可以在该文件中删除您不需要的功能。
示例代码如下：
<dx-codeblock>
:::  typescript
let sendComponents: any = {
	Face,// 发送表情功能
	Image,// 发送图片功能
	Video,// 发送视频功能
	File,// 发送文件功能
	Evaluate,// 发送评价功能
	Words,// 发送常用语功能
};
:::
</dx-codeblock>
