本文将为您介绍即时通信 IM 实现直播群功能的操作解析，以下为视频介绍：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2768-53360?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

即时通信 IM 的直播群（AVChatRoom）有以下特点：
- **无人数限制，可实现千万级的互动直播场景**。
- **支持针对违法违规内容以及不雅词的安全打击，满足安全监管需求**。
- 支持向全体在线用户推送消息（群系统通知）。
- Web 和微信小程序端支持以游客身份（即不登录）接收消息。
- 申请加群后，无需管理员审批，直接加入。

>?本文以 Web 和微信小程序端 SDK 为例，其他端 SDK 实现流程相同，操作略有差异。

## 适用场景

#### 直播弹幕
 AVChatRoom 支持弹幕、 送礼和点赞等多消息类型，轻松打造良好的直播聊天互动体验；提供弹幕内容审核能力，保证您的直播免受不雅信息干扰。
![](https://imgcache.qq.com/open_proj/proj_qcloud_v2/gateway/product/im-new/css/img/scenes/function2.gif)
#### 网红带货
 AVChatRoom 与商业直播相结合，通过提供点赞、询价、购物券等特定消息类型，帮助直播客户实现流量变现。
 ![](https://imgcache.qq.com/open_proj/proj_qcloud_v2/gateway/product/im-new/css/img/scenes/function3.gif)
#### 教学白板
 AVChatRoom 可提供在线课堂、文本消息、画笔轨迹等能力，轻松实现教师学生沟通、画笔轨迹保存、大班课与小班课教学等教学场景。
 ![](https://imgcache.qq.com/open_proj/proj_qcloud_v2/gateway/product/im-new/css/img/scenes/function4.gif)

## 使用限制
- 不支持 [撤回消息](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#revokeMessage)。
- 群主不可以退群，群主退群只能通过解散群组的方式。
- 不支持移除群成员。


## 相关文档
- [群组管理](https://cloud.tencent.com/document/product/269/3661)
- [群组系统](https://cloud.tencent.com/document/product/269/1502)
- [SDK 下载](https://cloud.tencent.com/document/product/269/36887)
- [更新日志（Web & 小程序）](https://cloud.tencent.com/document/product/269/38492)
- [SDK 手册](https://web.sdk.qcloud.com/im/doc/zh-cn/TIM.html)
- [集成 SDK（Web & 小程序）](https://cloud.tencent.com/document/product/269/37413)
- [初始化与登录（Web & 小程序）](https://cloud.tencent.com/document/product/269/37416)
- [消息收发（Web & 小程序）](https://cloud.tencent.com/document/product/269/37448)
- [群组管理（Web & 小程序）](https://cloud.tencent.com/document/product/269/37459)

## 使用指南
[](id:Step1)
### 步骤1：创建应用

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
>?如果您已有应用，请记录其 SDKAppID，并执行 [步骤2](#Step2)。
>同一个腾讯云帐号，最多可创建300个即时通信 IM 应用。若已有300个应用，您可以先 [停用并删除](https://cloud.tencent.com/document/product/269/32578#.E5.81.9C.E7.94.A8.2F.E5.88.A0.E9.99.A4.E5.BA.94.E7.94.A8) 无需使用的应用后再创建新的应用。**应用删除后，该 SDKAppID 对应的所有数据和服务不可恢复，请谨慎操作。**
>
2. 单击**+添加新应用**。
3. 在**创建应用**对话框中输入您的应用名称，单击**确定**。创建完成后，可在控制台总览页查看新建应用的状态、业务版本、SDKAppID、创建时间以及到期时间。
4. 记录该应用的 SDKAppID 信息。

[](id:Step2)
### 步骤2：创建 AVChatRoom
您可以通过控制台创建群组，也可以通过调用 [创建群组 API](https://cloud.tencent.com/document/product/269/1615) 创建群组。本文以通过控制台创建为例。


1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，单击目标应用卡片。
2. 在左侧导航栏选择**群组管理**，单击**添加群组**。
3. 输入群名称，选填群主 ID，选择**群类型**为**直播群**。
4. 单击**确定**，待群组创建成功后，记录其**群ID**（本文以`@TGS#aC72FIKG3`为例）。


[](id:Step3)
### 步骤3：集成 SDK
您可以通过 NPM 或 Script 集成 SDK，推荐使用 NPM 集成。本文以使用 NPM 集成为例。

-  Web 项目
```javascript
// Web 项目
npm install tim-js-sdk --save-dev
```
-  小程序项目
```javascript
// 微信小程序项目
npm install tim-wx-sdk --save-dev
```

>?若同步依赖过程中出现问题，请切换 npm 源后再次重试。
```
// 切换 cnpm 源
npm config set registry http://r.cnpmjs.org/
```

[](id:Step4)
### 步骤4：创建 SDK 实例

<pre><code><span class="hljs-comment">// 创建 SDK 实例，TIM.create() 方法对于同一个 SDKAppID 只会返回同一份实例</span>
<span class="hljs-keyword">let</span> options = {
  SDKAppID: <span class="hljs-number">0</span> <span class="hljs-comment">// 接入时需要将0替换为您的即时通信应用的 SDKAppID</span>
}
<span class="hljs-keyword">let</span> tim = TIM.create(options) <span class="hljs-comment">// SDK 实例通常用 tim 表示</span>
<span class="hljs-comment">// 设置 SDK 日志输出级别，详细分级请参考 <a href="https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html?_ga=1.43970405.1562552652.1542703643#setLogLevel">setLogLevel 接口的说明</a></span>
tim.setLogLevel(<span class="hljs-number">0</span>) <span class="hljs-comment">// 普通级别，日志量较多，接入时建议使用</span>

tim.<span class="hljs-keyword">on</span>(TIM.EVENT.SDK_READY, function (<span class="hljs-keyword">event</span>) {
  <span class="hljs-comment">// SDK ready 后接入侧才可以调用 sendMessage 等需要鉴权的接口，否则会提示失败！</span>
  <span class="hljs-comment">// event.name - TIM.EVENT.SDK_READY</span>
})

tim.<span class="hljs-keyword">on</span>(TIM.EVENT.MESSAGE_RECEIVED, function(<span class="hljs-keyword">event</span>) {
  <span class="hljs-comment">// 收到推送的单聊、群聊、群提示、群系统通知的新消息，可通过遍历 event.data 获取消息列表数据并渲染到页面</span>
  <span class="hljs-comment">// event.name - TIM.EVENT.MESSAGE_RECEIVED</span>
  <span class="hljs-comment">// event.data - 存储 Message 对象的数组 - [Message]</span>
  <span class="hljs-keyword">const</span> length = <span class="hljs-keyword">event</span>.data.<span class="hljs-function">length
  <span class="hljs-keyword">let</span> message
  <span class="hljs-title">for</span> (<span class="hljs-params"><span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i &lt; length; i++</span>)</span> {
    <span class="hljs-comment">// Message 实例的详细数据结构请参考 <a href="https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html">Message</a></span>
    <span class="hljs-comment">// 其中 type 和 payload 属性需要重点关注</span>
    <span class="hljs-comment">// 从v2.6.0起，AVChatRoom 内的群聊消息，进群退群等群提示消息，增加了 nick（昵称） 和 avatar（头像URL） 属性，便于接入侧做体验更好的展示</span>
    <span class="hljs-comment">// 前提您需要先调用 updateMyProfile 设置自己的 nick（昵称） 和 avatar（头像 URL），请参考 <a href="https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#updateMyProfile">updateMyProfile 接口的说明</a></span>
    message = <span class="hljs-keyword">event</span>.data[i]
    <span class="hljs-keyword">switch</span> (message.type) {
      <span class="hljs-keyword">case</span> TIM.TYPES.MSG_TEXT:
        <span class="hljs-comment">// 收到了文本消息</span>
        <span class="hljs-keyword">this</span>._handleTextMsg(message)
        <span class="hljs-keyword">break</span>
      <span class="hljs-keyword">case</span> TIM.TYPES.MSG_CUSTOM:
        <span class="hljs-comment">// 收到了自定义消息</span>
        <span class="hljs-keyword">this</span>._handleCustomMsg(message)
        <span class="hljs-keyword">break</span>
      <span class="hljs-keyword">case</span> TIM.TYPES.MSG_GRP_TIP:
        <span class="hljs-comment">// 收到了群提示消息，如成员进群、群成员退群</span>
        <span class="hljs-keyword">this</span>._handleGroupTip(message) 
        <span class="hljs-keyword">break</span>
      <span class="hljs-keyword">case</span> TIM.TYPES.MSG_GRP_SYS_NOTICE:
        <span class="hljs-comment">// 收到了群系统通知，通过 REST API 在群组中发送的系统通知请参考 <a href="https://cloud.tencent.com/document/product/269/1630">在群组中发送系统通知 API</a></span>
        <span class="hljs-keyword">this</span>._handleGroupSystemNotice(message)
        <span class="hljs-keyword">break</span>
      <span class="hljs-keyword">default</span>:
         <span class="hljs-keyword">break</span>
    }
  }
})

_handleTextMsg(message) {
  <span class="hljs-comment">// 详细数据结构请参考 <a href="https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.TextPayload">TextPayload 接口的说明</a></span>
  console.log(message.payload.text) <span class="hljs-comment">// 文本消息内容</span>
}

_handleCustomMsg(message) {
  <span class="hljs-comment">// 详细数据结构请参考 <a href="https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.CustomPayload">CustomPayload 接口的说明</a></span>
  console.log(message.payload)
}

_handleGroupTip(message) {
  <span class="hljs-comment">// 详细数据结构请参考 <a href="https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.GroupTipPayload">GroupTipPayload 接口的说明</a></span>
  <span class="hljs-keyword">switch</span> (message.payload.operationType) {
    <span class="hljs-keyword">case</span> TIM.TYPES.GRP_TIP_MBR_JOIN: <span class="hljs-comment">// 有成员加群</span>
      <span class="hljs-keyword">break</span>
    <span class="hljs-keyword">case</span> TIM.TYPES.GRP_TIP_MBR_QUIT: <span class="hljs-comment">// 有群成员退群</span>
      <span class="hljs-keyword">break</span>
    <span class="hljs-keyword">case</span> TIM.TYPES.GRP_TIP_MBR_KICKED_OUT: <span class="hljs-comment">// 有群成员被踢出群</span>
      <span class="hljs-keyword">break</span>
    <span class="hljs-keyword">case</span> TIM.TYPES.GRP_TIP_MBR_SET_ADMIN: <span class="hljs-comment">// 有群成员被设为管理员</span>
      <span class="hljs-keyword">break</span>
    <span class="hljs-keyword">case</span> TIM.TYPES.GRP_TIP_MBR_CANCELED_ADMIN: <span class="hljs-comment">// 有群成员被撤销管理员</span>
      <span class="hljs-keyword">break</span>
    <span class="hljs-keyword">case</span> TIM.TYPES.GRP_TIP_GRP_PROFILE_UPDATED: <span class="hljs-comment">// 群组资料变更</span>
      <span class="hljs-comment">//从v2.6.0起支持群组自定义字段变更内容</span>
      <span class="hljs-comment">// message.payload.newGroupProfile.groupCustomField </span>
      <span class="hljs-keyword">break</span>
    <span class="hljs-keyword">case</span> TIM.TYPES.GRP_TIP_MBR_PROFILE_UPDATED: <span class="hljs-comment">// 群成员资料变更，例如群成员被禁言</span>
      <span class="hljs-keyword">break</span>
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">break</span>
  }
}

_handleGroupSystemNotice(message) {
  <span class="hljs-comment">// 详细数据结构请参考  <a href="https://web.sdk.qcloud.com/im/doc/zh-cn/Message.html#.GroupSystemNoticePayload">GroupSystemNoticePayload 接口的说明</a></span>
  console.log(message.payload.userDefinedField) <span class="hljs-comment">// 用户自定义字段。使用 RESTAPI 发送群系统通知时，可在该属性值中拿到自定义通知的内容。</span>
  <span class="hljs-comment">// 用 REST API 发送群系统通知请参考 <a href="https://cloud.tencent.com/document/product/269/1630">在群组中发送系统通知 API</a></span>
}</code></pre>

[](id:Step5)
### 步骤5：登录 SDK

```javascript
let promise = tim.login({userID: 'your userID', userSig: 'your userSig'});
promise.then(function(imResponse) {
  console.log(imResponse.data); // 登录成功
}).catch(function(imError) {
  console.warn('login error:', imError); // 登录失败的相关信息
});
```

[](id:Step6)
### 步骤6：设置自己的昵称和头像
2.6.2及以上版本 SDK，AVChatRoom 内的群聊消息和群提示消息（例如进群退群等），都增加了 nick（昵称） 和 avatar（头像URL） 属性，您可以调用接口 [updateMyProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#updateMyProfile) 设置自己的 nick（昵称） 和 avatar（头像URL）。

```javascript
// 从v2.6.0起，AVChatRoom 内的群聊消息，进群退群等群提示消息，增加了 nick（昵称） 和 avatar（头像URL） 属性，便于接入侧做体验更好的展示，前提您需要先调用 updateMyProfile 设置个人资料。
// 修改个人标配资料
let promise = tim.updateMyProfile({
  nick: '我的昵称',
  avatar: 'http(s)://url/to/image.jpg'
});
promise.then(function(imResponse) {
  console.log(imResponse.data); // 更新资料成功
}).catch(function(imError) {
  console.warn('updateMyProfile error:', imError); // 更新资料失败的相关信息
});
```

[](id:Step7)
### 步骤7：加入群组
```javascript
// 匿名用户加入（无需登录，入群后仅能接收消息）
let promise = tim.joinGroup({ groupID: 'avchatroom_groupID'});
promise.then(function(imResponse) {
  switch (imResponse.data.status) {
    case TIM.TYPES.JOIN_STATUS_WAIT_APPROVAL: // 等待管理员同意
      break
    case TIM.TYPES.JOIN_STATUS_SUCCESS: // 加群成功
      console.log(imResponse.data.group) // 加入的群组资料
      break
    case TIM.TYPES.JOIN_STATUS_ALREADY_IN_GROUP: // 已经在群中
      break
    default:
      break
  }
}).catch(function(imError){
  console.warn('joinGroup error:', imError) // 申请加群失败的相关信息
});
```

### 步骤8：创建消息实例并发送
本文以发送文本消息为例。

<pre><code class="language-javascript"><span class="hljs-comment">// 发送文本消息，Web 端与小程序端相同</span>
<span class="hljs-comment">// 1. 创建消息实例，接口返回的实例可以上屏</span>
<span class="hljs-keyword">let</span> message = tim.createTextMessage({
  <span class="hljs-attr">to</span>: <span class="hljs-string">'avchatroom_groupID'</span>,
  <span class="hljs-attr">conversationType</span>: TIM.TYPES.CONV_GROUP,
  <span class="hljs-comment">// 消息优先级，用于群聊（v2.4.2起支持）。如果某个群的消息超过了频率限制，后台会优先下发高优先级的消息，详细请参考 <a href="https://cloud.tencent.com/document/product/269/3663#.E6.B6.88.E6.81.AF.E4.BC.98.E5.85.88.E7.BA.A7.E4.B8.8E.E9.A2.91.E7.8E.87.E6.8E.A7.E5.88.B6">消息优先级与频率控制</a></span>
  <span class="hljs-comment">// 支持的枚举值：TIM.TYPES.MSG_PRIORITY_HIGH, TIM.TYPES.MSG_PRIORITY_NORMAL（默认）, TIM.TYPES.MSG_PRIORITY_LOW, TIM.TYPES.MSG_PRIORITY_LOWEST</span>
  <span class="hljs-attr">priority</span>: TIM.TYPES.MSG_PRIORITY_NORMAL,
  <span class="hljs-attr">payload</span>: {
    <span class="hljs-attr">text</span>: <span class="hljs-string">'Hello world!'</span>
  }
})
<span class="hljs-comment">// 2. 发送消息</span>
<span class="hljs-keyword">let</span> promise = tim.sendMessage(message)
promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">imResponse</span>) </span>{
  <span class="hljs-comment">// 发送成功</span>
  <span class="hljs-built_in">console</span>.log(imResponse)
}).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">imError</span>) </span>{
  <span class="hljs-comment">// 发送失败</span>
  <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'sendMessage error:'</span>, imError)
})</code></pre>


## 常见问题

### 1. 自己发送的消息 `Message.nick` 和 `Message.avatar` 都是空的，该怎么处理才能在界面上正常展示昵称和头像？

可以通过调用 [getMyProfile](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#getMyProfile) 获取自己的昵称和头像。

### 2. 如何在直播群中实现禁言功能？

可以将禁言功能通过自定义消息实现，自定义消息中需包含被禁言者的 Members_Account 与禁言时间，通过 [群内发言之前回调](https://cloud.tencent.com/document/product/269/1619) 将该自定义消息抄送至业务后台，业务后台调用 [批量禁言和取消禁言](https://cloud.tencent.com/document/product/269/1627) 接口即可实现针对指定用户的禁言功能。

### 3. 如何在直播群中实现踢人功能？

可以将踢人功能通过自定义消息实现，自定义消息中需包含被踢者的 Members_Account，通过将该消息优先级设置为 High 避免因40条/秒消息限频后被后台抛弃，被踢者的 SDK 收到该消息后，调用 [退出群组](https://cloud.tencent.com/document/product/269/44498#.E7.BE.A4.E7.BB.84.E7.9B.B8.E5.85.B3.E6.8E.A5.E5.8F.A3) 接口即可在直播群中实现踢人功能。

### 4. [](id:p4)为什么在小程序/Web 端调用退出群组接口后，Android/iOS/PC 端会同步退群；但是 Android/iOS/PC 调用退出群组接口后，小程序/Web 端不会退出呢？

因为小程序/Web 端支持用户以游客模式访问，所以当 Android/iOS/PC 退群后，小程序/Web 端不会主动触发退出群组操作。

- 如果希望实现全端同步退出操作，您可以配置 [群成员离开之后](https://cloud.tencent.com/document/product/269/1668) 回调，通过 OptPlatform 字段判断当前退出平台，当退群平台为 Android/iOS/PC 时，通过 [单发单聊消息](https://cloud.tencent.com/document/product/269/2282) 接口以系统消息的方式发送一条自定义消息至退群者，前端屏蔽该会话不做 UI 层展示，小程序/Web 端收到该消息后，调用 [退出群组](https://cloud.tencent.com/document/product/269/37411#.E7.BE.A4.E7.BB.84) 接口即可。
- 如果希望实现单端独立退出操作，您可以配置 [群成员离开之后](https://cloud.tencent.com/document/product/269/1668) 回调，通过 OptPlatform 判断当前退出平台，通过 [单发单聊消息](https://cloud.tencent.com/document/product/269/2282) 接口以系统消息的方式发送一条自定义消息至退群者，前端屏蔽该会话不做 UI 层展示，非退出端收到该消息后调用 [加入群组](https://cloud.tencent.com/document/product/269/44498#.E7.BE.A4.E7.BB.84.E7.9B.B8.E5.85.B3.E6.8E.A5.E5.8F.A3) 接口再次加入该群即可，为避免多次出现加退群系统通知，可提交工单关闭加退群系统通知。

### 5. 为什么会丢消息？

出现丢消息的可能原因如下：

- 直播群有40条/秒的频率限制，可通过消息发送前回调与消息发送后回调进行判断，若丢失的消息有收到消息发送前回调，未收到消息发送后回调，则该消息被限频。
- 可参考 [常见问题4](#p4)，判断是否因为小程序/Web 端退出时，导致 Android/iOS/PC 同步退出。
- 如果是小程序/Web 出现问题，请确认您使用的 SDK 版本是否早于V2.7.6，如果是，请升级最新版。

如果您已排除以上可能性，您可以提交工单联系我们。

### 6. 如何实现点赞/关注数量统计？

先通过自定义消息构建点赞/关注消息类型，当用户在前端点击点赞/关注 icon 触发自定义消息下发后，将点赞/关注消息通过 [群内发言之前回调](https://cloud.tencent.com/document/product/269/1619) 抄送到业务侧，业务侧根据收到的点赞/关注消息数进行数量统计，每3秒 - 5秒可通过 [修改群基础资料接口](https://cloud.tencent.com/document/product/269/1620) 将该数据更新进群资料字段中，SDK 通过 [拉取群资料接口](https://cloud.tencent.com/document/product/269/44498#.E7.BE.A4.E7.BB.84.E7.9B.B8.E5.85.B3.E6.8E.A5.E5.8F.A3) 即可实现点赞/关注数量统计。

### 7. 如何设置消息优先级更为合理？

为避免重要消息被抛弃，直播间针对所有消息提供3种优先级选择，SDK 获取消息时将会优先获取高优先级消息，针对自定义消息优先级设置建议如下：

- High：红包、礼物、踢人消息。
- Normal：普通文本消息。
- Low：点赞、关注消息。

### 8. 有没有开源的直播组件，可以直接看视频和聊天互动？

有的，且代码开源，详情请参考 [腾讯云 Web 直播互动组件](https://github.com/tencentyun/TWebLive)。
您也可以直接扫码体验腾讯云 Web 直播互动组件：
<img src="https://main.qcloudimg.com/raw/7ebc3e270add5ec6d62f6f8972c61249.png" width="150">




