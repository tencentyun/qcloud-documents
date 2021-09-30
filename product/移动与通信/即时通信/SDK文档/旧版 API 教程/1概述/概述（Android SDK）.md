## IM SDK 基本概念
**会话：**IM SDK 中会话（Conversation）分为两种，一种是 C2C 会话，表示单聊情况自己与对方建立的对话，读取消息和发送消息都是通过会话完成；另一种是群会话，表示群聊情况下，群内成员组成的会话，群会话内发送消息群成员都可接收到。如下图所示，一个会话表示与一个好友的对话。
![](https://main.qcloudimg.com/raw/921a378c4157ad7cda2d87bfbe8ea21f.jpg)

**消息：**IM SDK 中消息(Message)表示要发送给对方的内容，消息包括若干属性，如是否自己已读，是否已经发送成功，发送人帐号，消息产生时间等；一条消息由若干 Elem 组合而成，每种 Elem 可以是文本、图片、表情等等，消息支持多种 Elem 组合发送。

![](https://main.qcloudimg.com/raw/e98740eedd17c6408c0f3cdcbdf83e8a.png)

**群组 ID：**群组 ID 唯一标识一个群，由后台生成，创建群组时返回。 

## IM SDK 对象简介[](id:dx)
IM SDK 对象主要分为通讯管理器，会话、消息，群管理，具体的含义参见下表：

| 对象 | 介绍 | 功能 |
| --- | --- | --- |
| TIMManager | 管理器类，负责 IM SDK 基本操作 | 初始化、登录、注销、创建会话等。 |
| TIMConversation | 会话，负责会话相关操作 | 如发送消息，获取会话消息缓存，获取未读计数等。 |
| TIMMessage | 消息 | 包括文本、图片等不同类型消息。 |
| TIMGroupManager | 群组管理器 | 负责创建群组、加群、退群等。 |
| TIMFriendshipManager | 资料和关系链管理器 | 负责资料获取、修改以及关系链等相关功能。 |

## 调用顺序介绍
IM SDK 调用 API 需要遵循以下顺序，其余辅助方法需要在登录成功后调用。

<table style="width:100%;">
		<tbody>
			<tr>
				<th style="text-align:center;">
					步骤<br>
				</th>
				<th style="text-align:center;">
					对应函数<br>
				</th>
				<th style="text-align:center;">
					说明<br>
				</th>
			</tr>
			<tr>
				<td rowspan="5">
					初始化<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMSdkConfig<br>
				</td>
				<td>
					设置 IM SDK 基本配置，例如 SDKAppID、日志等级等<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMManager : init<br>
				</td>
				<td>
					初始化 IM SDK<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMManager : setUserConfig<br>
				</td>
				<td>
					设置用户基本配置<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMManager  :  addMessageListener<br>
				</td>
				<td>
					设置消息监听<br>
				</td>
			</tr>
			<tr>
				<td rowspan="2">
					登录<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMManager : login<br>
				</td>
				<td>
					登录<br>
				</td>
			</tr>
			<tr>
				<td rowspan="2">
					消息收发<br>
				</td>
				<td>
					TIMManager : getConversation<br>
				</td>
				<td>
					获取会话<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMConversation : sendMessage<br>
				</td>
				<td>
					发送消息<br>
				</td>
			</tr>
			<tr>
				<td>
					群组管理<br>
				</td>
				<td>
					TIMGroupManager<br>
				</td>
				<td>
					群组管理<br>
				</td>
			</tr>
			<tr>
				<td>
					注销<br>
				</td>
				<td>
					TIMManager : logout<br>
				</td>
				<td>
					注销<br>
				</td>
			</tr>
		</tbody>
	</table>

