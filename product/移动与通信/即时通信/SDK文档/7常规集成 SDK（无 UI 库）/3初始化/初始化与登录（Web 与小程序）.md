## 创建 SDK 实例

### Web 项目

<pre><code><span class="hljs-keyword">import</span> TIM <span class="hljs-keyword">from</span> <span class="hljs-string">'tim-js-sdk'</span>;
<span class="hljs-comment">// 发送图片、文件等消息需要腾讯云即时通信IM上传插件</span>
<span class="hljs-keyword">import</span> TIMUploadPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'tim-upload-plugin'</span>;

<span class="hljs-keyword">let</span> options = {
  <span class="hljs-attr">SDKAppID</span>: <span class="hljs-number">0</span> <span class="hljs-comment">// 接入时需要将0替换为您的即时通信 IM 应用的 SDKAppID</span>
};
<span class="hljs-comment">// 创建 SDK 实例，TIM.create() 方法对于同一个 SDKAppID 只会返回同一份实例</span>
<span class="hljs-keyword">let</span> tim = TIM.create(options); <span class="hljs-comment">// SDK 实例通常用 tim 表示</span>

<span class="hljs-comment">// 设置 SDK 日志输出级别，详细分级请参见 <a href="https://web.sdk.qcloud.com/im/doc/zh-cn//SDK.html#setLogLevel">setLogLevel 接口的说明</a></span>
tim.setLogLevel(<span class="hljs-number">0</span>); <span class="hljs-comment">// 普通级别，日志量较多，接入时建议使用</span>
<span class="hljs-comment">// tim.setLogLevel(1); // release 级别，SDK 输出关键信息，生产环境时建议使用</span>

<span class="hljs-comment">// 注册腾讯云即时通信IM上传插件</span>
tim.registerPlugin({<span class="hljs-string">'tim-upload-plugin'</span>: TIMUploadPlugin});</code></pre>


### 小程序项目

<pre><code><span class="hljs-keyword">import</span> TIM <span class="hljs-keyword">from</span> <span class="hljs-string">'tim-wx-sdk'</span>;
<span class="hljs-comment">// 发送图片、文件等消息需要腾讯云即时通信IM上传插件</span>
<span class="hljs-keyword">import</span> TIMUploadPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'tim-upload-plugin'</span>;


<span class="hljs-keyword">let</span> options = {
  <span class="hljs-attr">SDKAppID</span>: <span class="hljs-number">0</span> <span class="hljs-comment">// 接入时需要将0替换为您的即时通信 IM 应用的 SDKAppID</span>
};
<span class="hljs-comment">// 创建 SDK 实例，TIM.create() 方法对于同一个 SDKAppID 只会返回同一份实例</span>
<span class="hljs-keyword">let</span> tim = TIM.create(options); <span class="hljs-comment">// SDK 实例通常用 tim 表示</span>

<span class="hljs-comment">// 设置 SDK 日志输出级别，详细分级请参见 <a href="https://web.sdk.qcloud.com/im/doc/zh-cn//SDK.html#setLogLevel">setLogLevel 接口的说明</a></span>
tim.setLogLevel(<span class="hljs-number">0</span>); <span class="hljs-comment">// 普通级别，日志量较多，接入时建议使用</span>
<span class="hljs-comment">// tim.setLogLevel(1); // release 级别，SDK 输出关键信息，生产环境时建议使用</span>

<span class="hljs-comment">// 注册腾讯云即时通信IM上传插件</span>
tim.registerPlugin({<span class="hljs-string">'tim-upload-plugin'</span>: TIMUploadPlugin});</code></pre>




## 设置日志级别

<pre><code><span class="hljs-comment">// 设置 SDK 日志输出级别，详细分级请参见 <a href="https://web.sdk.qcloud.com/im/doc/zh-cn//SDK.html#setLogLevel">setLogLevel 接口的说明</a></span>
<span class="hljs-selector-tag">tim</span><span class="hljs-selector-class">.setLogLevel</span>(<span class="hljs-number">0</span>);</code></pre>



## 事件绑定


```
// 监听事件，例如：
tim.on(TIM.EVENT.SDK_READY, function(event) {
  // 收到离线消息和会话列表同步完毕通知，接入侧可以调用 sendMessage 等需要鉴权的接口
  // event.name - TIM.EVENT.SDK_READY
});

tim.on(TIM.EVENT.MESSAGE_RECEIVED, function(event) {
  // 收到推送的单聊、群聊、群提示、群系统通知的新消息，可通过遍历 event.data 获取消息列表数据并渲染到页面
  // event.name - TIM.EVENT.MESSAGE_RECEIVED
  // event.data - 存储 Message 对象的数组 - [Message]
});

tim.on(TIM.EVENT.MESSAGE_REVOKED, function(event) {
  // 收到消息被撤回的通知
  // event.name - TIM.EVENT.MESSAGE_REVOKED
  // event.data - 存储 Message 对象的数组 - [Message] - 每个 Message 对象的 isRevoked 属性值为 true
});

tim.on(TIM.EVENT.MESSAGE_READ_BY_PEER, function(event) {
  // SDK 收到对端已读消息的通知，即已读回执。使用前需要将 SDK 版本升级至 v2.7.0 或以上。仅支持单聊会话。
  // event.name - TIM.EVENT.MESSAGE_READ_BY_PEER
  // event.data - event.data - 存储 Message 对象的数组 - [Message] - 每个 Message 对象的 isPeerRead 属性值为 true
});

tim.on(TIM.EVENT.CONVERSATION_LIST_UPDATED, function(event) {
  // 收到会话列表更新通知，可通过遍历 event.data 获取会话列表数据并渲染到页面
  // event.name - TIM.EVENT.CONVERSATION_LIST_UPDATED
  // event.data - 存储 Conversation 对象的数组 - [Conversation]
});

tim.on(TIM.EVENT.GROUP_LIST_UPDATED, function(event) {
  // 收到群组列表更新通知，可通过遍历 event.data 获取群组列表数据并渲染到页面
  // event.name - TIM.EVENT.GROUP_LIST_UPDATED
  // event.data - 存储 Group 对象的数组 - [Group]
});

tim.on(TIM.EVENT.PROFILE_UPDATED, function(event) {
  // 收到自己或好友的资料变更通知
  // event.name - TIM.EVENT.PROFILE_UPDATED
  // event.data - 存储 Profile 对象的数组 - [Profile]
});

tim.on(TIM.EVENT.BLACKLIST_UPDATED, function(event) {
  // 收到黑名单列表更新通知
  // event.name - TIM.EVENT.BLACKLIST_UPDATED
  // event.data - 存储 userID 的数组 - [userID]
});

tim.on(TIM.EVENT.ERROR, function(event) {
  // 收到 SDK 发生错误通知，可以获取错误码和错误信息
  // event.name - TIM.EVENT.ERROR
  // event.data.code - 错误码
  // event.data.message - 错误信息
});

tim.on(TIM.EVENT.SDK_NOT_READY, function(event) {
  // 收到 SDK 进入 not ready 状态通知，此时 SDK 无法正常工作
  // event.name - TIM.EVENT.SDK_NOT_READY
});

tim.on(TIM.EVENT.KICKED_OUT, function(event) {
  // 收到被踢下线通知
  // event.name - TIM.EVENT.KICKED_OUT
  // event.data.type - 被踢下线的原因，例如:
  //    - TIM.TYPES.KICKED_OUT_MULT_ACCOUNT 多实例登录被踢
  //    - TIM.TYPES.KICKED_OUT_MULT_DEVICE 多终端登录被踢
  //    - TIM.TYPES.KICKED_OUT_USERSIG_EXPIRED 签名过期被踢 （v2.4.0起支持）。 
});

 tim.on(TIM.EVENT.NET_STATE_CHANGE, function(event) { 
  //  网络状态发生改变（v2.5.0 起支持）。 
  // event.name - TIM.EVENT.NET_STATE_CHANGE 
  // event.data.state 当前网络状态，枚举值及说明如下： 
  //     \- TIM.TYPES.NET_STATE_CONNECTED - 已接入网络 
  //     \- TIM.TYPES.NET_STATE_CONNECTING - 连接中。很可能遇到网络抖动，SDK 在重试。接入侧可根据此状态提示“当前网络不稳定”或“连接中” 
  //    \- TIM.TYPES.NET_STATE_DISCONNECTED - 未接入网络。接入侧可根据此状态提示“当前网络不可用”。SDK 仍会继续重试，若用户网络恢复，SDK 会自动同步消息  
});

// 开始登录 
tim.login({userID: 'your userID', userSig: 'your userSig'}); 
```

参数`options`为`Object`类型：

| Name      | Type     | Description |
| --------- | -------- | ----------- |
| `options` | `Object` | 应用配置    |

`options` 包含的属性值：

| Name       | Type     | Description             |
| ---------- | -------- | ----------------------- |
| `SDKAppID` | `Number` | 即时通信 IM 应用的 `SDKAppID` |

更详细的初始化流程和 API 使用介绍请参见 [SDK 初始化](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html)。

## 登录

用户登录 IM SDK 才能正常收发消息，登录需要用户提供 UserID、UserSig 等信息，具体含义请参见 [登录鉴权](https://cloud.tencent.com/document/product/269/31999)。登录成功后，需要先等 SDK 处于 ready 状态才能调用 [sendMessage](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html#sendMessage) 等需要鉴权的接口，您可以通过监听事件 [TIM.EVENT.SDK_READY](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.SDK_READY) 获取 SDK 状态。

>!默认情况下，不支持多实例登录，即如果此帐号已在其他页面登录，若继续在当前页面登录成功，有可能会将其他页面踢下线。用户被踢下线时会触发事件`TIM.EVENT.KICKED_OUT`，用户可在监听到事件后做相应处理。多端登录监听示例如下：

```javascript
let onKickedOut = function (event) {
  console.log(event.data.type); // mutipleAccount(同一设备，同一帐号，多页面登录被踢)
};
tim.on(TIM.EVENT.KICKED_OUT, onKickedOut);
```

如需支持多实例登录（允许在多个网页中同时登录同一帐号），请登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，找到相应 SDKAppID，选择【应用配置】>【功能配置】>【登录与消息】>【Web端实例同时在线】配置实例个数。配置将在5分钟内生效。

**接口名**

```javascript
tim.login(options);
```

**请求参数**

| 名称    | 类型   | 描述                                                         |
| ------- | ------ | ------------------------------------------------------------ |
| userID  | String | 用户 ID。                                                    |
| userSig | String | 用户登录即时通信 IM 的密码，其本质是对 UserID 等信息加密后得到的密文。<br/>具体生成方法请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)。 |

**返回值**

该接口返回 `Promise` 对象。

**示例**

```javascript
let promise = tim.login({userID: 'your userID', userSig: 'your userSig'});
promise.then(function(imResponse) {
  console.log(imResponse.data); // 登录成功
  if (imResponse.data.repeatLogin === true) {
    // 标识帐号已登录，本次登录操作为重复登录。v2.5.1 起支持
    console.log(imResponse.data.errorInfo);
  }
}).catch(function(imError) {
  console.warn('login error:', imError); // 登录失败的相关信息
});
```



## 登出

 登出即时通信 IM，通常在切换帐号的时候调用，清除登录态以及内存中的所有数据。 

>!
>- 调用此接口的实例会发布 [`SDK_NOT_READY`](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.SDK_NOT_READY) 事件，此时该实例下线，无法收、发消息。
>- 如果您在[即时通信 IM 控制台](https://console.cloud.tencent.com/im)配置的“Web端实例同时在线个数”大于 1，且同一帐号登录了`a1`和`a2`两个实例（含小程序端），当执行`a1.logout()`后，`a1`会下线，无法收、发消息。而`a2`实例不会受影响。
>- 多实例被踢：基于第 2 点，如果“Web端实例同时在线个数”配置为 2，且您的某一帐号已经登录了 `a1`，`a2`两个实例，当使用此帐号成功登录第三个实例`a3`时，`a1`或`a2`中的一个实例会被踢下线（通常是最先处在登录态的实例会触发），这种情况称之为**“多实例被踢”**。假设`a1`实例被踢下线，`a1`实例内部会执行登出流程，然后抛出[`KICKED_OUT`](https://web.sdk.qcloud.com/im/doc/zh-cn/module-EVENT.html#.KICKED_OUT)事件，接入侧可以监听此事件，并在触发时跳转到登录页。此时`a1`实例下线，而`a2`、`a3`实例可以正常运行。

**接口名**

```js
tim.logout();
```

**请求参数**

无

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://web.sdk.qcloud.com/im/doc/zh-cn/global.html#IMResponse)，`IMResponse.data`为空对象。表示成功登出。
- `catch`的回调函数参数为 [IMError](https://web.sdk.qcloud.com/im/doc/zh-cn/global.html#IMError)。

**示例**

```js
let promise = tim.logout();
promise.then(function(imResponse) {
  console.log(imResponse.data); // 登出成功
}).catch(function(imError) {
  console.warn('logout error:', imError);
});
```


