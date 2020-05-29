音视频聊天室（AVChatRoom）有以下特点：
- **适用于互动直播场景，群成员人数无上限**。
- **支持针对涉黄、涉政以及不雅词的安全打击，满足安全监管需求**。
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
- 不支持 [撤回消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#revokeMessage)。
- 群主不可以退群，群主退群只能通过解散群组的方式。
- 不支持移除群成员。


## 相关文档
- [群组管理](https://cloud.tencent.com/document/product/269/3661)
- [群组系统](https://cloud.tencent.com/document/product/269/1502)
- [SDK 下载](https://cloud.tencent.com/document/product/269/36887)
- [更新日志（Web & 小程序）](https://cloud.tencent.com/document/product/269/38492)
- [SDK 手册](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/TIM.html)
- [集成 SDK（Web & 小程序）](https://cloud.tencent.com/document/product/269/37413)
- [初始化（Web & 小程序）](https://cloud.tencent.com/document/product/269/37416)
- [登录（Web & 小程序）](https://cloud.tencent.com/document/product/269/37445)
- [消息收发（Web & 小程序）](https://cloud.tencent.com/document/product/269/37448)
- [群组管理（Web & 小程序）](https://cloud.tencent.com/document/product/269/37459)

## 使用指南
<span id="Step1"></span>
### 步骤1：创建应用

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
 >?如果您已有应用，请记录其 SDKAppID，并执行 [步骤2](#Step2)。
 >同一个腾讯云账号，最多可创建100个即时通信 IM 应用。若已有100个应用，您可以先 [停用并删除](https://cloud.tencent.com/document/product/269/32578#.E5.81.9C.E7.94.A8.2F.E5.88.A0.E9.99.A4.E5.BA.94.E7.94.A8) 无需使用的应用后再创建新的应用。**应用删除后，该 SDKAppID 对应的所有数据和服务不可恢复，请谨慎操作。**
 >
2. 单击【+添加新应用】。
3. 在【创建应用】对话框中输入您的应用名称，单击【确定】。创建完成后，可在控制台总览页查看新建应用的状态、业务版本、SDKAppID、创建时间以及到期时间。
4. 记录该应用的 SDKAppID 信息。

<span id="Step2"></span>
### 步骤2：创建 AVChatRoom
您可以通过控制台创建群组，也可以通过调用 [创建群组 API](https://cloud.tencent.com/document/product/269/1615) 创建群组。本文以通过控制台创建为例。


1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，单击目标应用卡片。
2. 在左侧导航栏选择【群组管理】，单击【添加群组】。
3. 输入群名称，选填群主 ID，选择【群类型】为【互动直播聊天室】。
4. 单击【确定】，待群组创建成功后，记录其【群ID】（本文以`@TGS#aC72FIKG3`为例）。


<span id="Step3"></span>
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

<span id="Step4"></span>
### 步骤4：创建 SDK 实例

<pre><code><span class="hljs-comment">// 创建 SDK 实例，TIM.create() 方法对于同一个 SDKAppID 只会返回同一份实例</span>
<span class="hljs-keyword">let</span> options = {
  SDKAppID: <span class="hljs-number">0</span> <span class="hljs-comment">// 接入时需要将0替换为您的即时通信应用的 SDKAppID</span>
}
<span class="hljs-keyword">let</span> tim = TIM.create(options) <span class="hljs-comment">// SDK 实例通常用 tim 表示</span>
<span class="hljs-comment">// 设置 SDK 日志输出级别，详细分级请参考 <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html?_ga=1.43970405.1562552652.1542703643#setLogLevel">setLogLevel 接口的说明</a></span>
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
    <span class="hljs-comment">// Message 实例的详细数据结构请参考 <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html">Message</a></span>
    <span class="hljs-comment">// 其中 type 和 payload 属性需要重点关注</span>
    <span class="hljs-comment">// 从v2.6.0起，AVChatRoom 内的群聊消息，进群退群等群提示消息，增加了 nick（昵称） 和 avatar（头像URL） 属性，便于接入侧做体验更好的展示</span>
    <span class="hljs-comment">// 前提您需要先调用 updateMyProfile 设置自己的 nick（昵称） 和 avatar（头像 URL），请参考 <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#updateMyProfile">updateMyProfile 接口的说明</a></span>
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
  <span class="hljs-comment">// 详细数据结构请参考 <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.TextPayload">TextPayload 接口的说明</a></span>
  console.log(message.payload.text) <span class="hljs-comment">// 文本消息内容</span>
}

_handleCustomMsg(message) {
  <span class="hljs-comment">// 详细数据结构请参考 <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.CustomPayload">CustomPayload 接口的说明</a></span>
  console.log(message.payload)
}

_handleGroupTip(message) {
  <span class="hljs-comment">// 详细数据结构请参考 <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupTipPayload">GroupTipPayload 接口的说明</a></span>
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
  <span class="hljs-comment">// 详细数据结构请参考  <a href="https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html#.GroupSystemNoticePayload">GroupSystemNoticePayload 接口的说明</a></span>
  console.log(message.payload.userDefinedField) <span class="hljs-comment">// 用户自定义字段。使用 RESTAPI 发送群系统通知时，可在该属性值中拿到自定义通知的内容。</span>
  <span class="hljs-comment">// 用 REST API 发送群系统通知请参考 <a href="https://cloud.tencent.com/document/product/269/1630">在群组中发送系统通知 API</a></span>
}</code></pre>

<span id="Step5"></span>
### 步骤5：登录 SDK

```javascript
let promise = tim.login({userID: 'your userID', userSig: 'your userSig'});
promise.then(function(imResponse) {
  console.log(imResponse.data); // 登录成功
}).catch(function(imError) {
  console.warn('login error:', imError); // 登录失败的相关信息
});
```

<span id="Step6"></span>
### 步骤6：设置自己的昵称和头像
2.6.2及以上版本 SDK，AVChatRoom 内的群聊消息和群提示消息（例如进群退群等），都增加了 nick（昵称） 和 avatar（头像URL） 属性，您可以调用接口 [updateMyProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#updateMyProfile) 设置自己的 nick（昵称） 和 avatar（头像URL）。

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

<span id="Step7"></span>
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



