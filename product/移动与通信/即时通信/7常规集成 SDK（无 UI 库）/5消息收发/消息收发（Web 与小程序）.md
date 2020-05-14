## 发送消息

### 创建文本消息
创建文本消息的接口，此接口返回一个消息实例，可以在需要发送文本消息时调用 [发送消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 接口发送消息实例。


**接口名**

```javascript
tim.createTextMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description                                            |
| ------------------ | -------- | ------------------------------------------------------ |
| `to`               | `String` | 消息的接收方                                           |
| `conversationType` | `String` | 会话类型，取值`TIM.TYPES.CONV_C2C`或`TIM.TYPES.CONV_GROUP` |
| `payload`          | `Object` | 消息内容的容器                                         |

`payload`的描述如下表所示：

| Name   | Type     | Description  |
| ------ | -------- | ------------ |
| `text` | `String` | 消息文本内容 |



**示例**

```javascript
// 发送文本消息，Web 端与小程序端相同
// 1. 创建消息实例，接口返回的实例可以上屏
let message = tim.createTextMessage({
  to: 'user1',
  conversationType: TIM.TYPES.CONV_C2C,
  payload: {
    text: 'Hello world!'
  }
});
// 2. 发送消息
let promise = tim.sendMessage(message);
promise.then(function(imResponse) {
  // 发送成功
  console.log(imResponse);
}).catch(function(imError) {
  // 发送失败
  console.warn('sendMessage error:', imError);
});
```

**返回**

消息实例 [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html)。



### 创建图片消息
创建图片消息的接口，此接口返回一个消息实例，可以在需要发送图片消息时调用 [发送消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 接口发送消息实例。

>! v2.3.1版本开始支持传入 File 对象，使用前需要将 SDK 升级至v2.3.1或以上。


**接口**

```javascript
tim.createImageMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description                                            |
| ------------------ | -------- | ------------------------------------------------------ |
| `to`               | `String` | 消息的接收方                                           |
| `conversationType` | `String` | 会话类型，取值`TIM.TYPES.CONV_C2C`或`TIM.TYPES.CONV_GROUP` |
| `payload`          | `Object` | 消息内容的容器                                         |
| `onProgress` | `function` | 获取上传进度的回调函数 |

`paylaod`的描述如下表所示：

| Name | Type                        | Description                                                  |
| ---- | --------------------------- | ------------------------------------------------------------ |
| file | `HTMLInputElement 或 Object` | 用于选择图片的 DOM 节点（Web）或者 File 对象（Web）或者微信小程序 `wx.chooseImage` 接口的 `success` 回调参数。SDK 会读取其中的数据并上传图片 |

**Web 示例**

```javascript
// Web 端发送图片消息
// 1. 创建消息实例，接口返回的实例可以上屏
let message = tim.createImageMessage({
  to: 'user1',
  conversationType: TIM.TYPES.CONV_C2C,
  payload: {
    file: document.getElementById('imagePicker'),
  },
  onProgress: function(event) { console.log('file uploading:', event) }
});
// 2. 发送消息
let promise = tim.sendMessage(message);
promise.then(function(imResponse) {
  // 发送成功
  console.log(imResponse);
}).catch(function(imError) {
  // 发送失败
  console.warn('sendMessage error:', imError);
});
```

**小程序示例**

```javascript
// 小程序端发送图片
// 1. 选择图片
wx.chooseImage({
  sourceType: ['album'], // 从相册选择
  count: 1, // 只选一张，目前 SDK 不支持一次发送多张图片
  success: function (res) {
    // 2. 创建消息实例，接口返回的实例可以上屏
    let message = tim.createImageMessage({
      to: 'user1',
      conversationType: TIM.TYPES.CONV_C2C,
      payload: { file: res },
      onProgress: function(event) { console.log('file uploading:', event) }
    });
    // 3. 发送图片
    let promise = tim.sendMessage(message);
    promise.then(function(imResponse) {
      // 发送成功
      console.log(imResponse);
    }).catch(function(imError) {
      // 发送失败
      console.warn('sendMessage error:', imError);
    });
  }
})
```

**返回**

消息实例 [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html)。


### 创建音频消息
创建音频消息实例的接口，此接口返回一个消息实例，可以在需要发送音频消息时调用 [发送消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 接口发送消息实例。

>!
>- 使用该接口前，需要将 SDK 版本升级至v2.2.0或以上。
>- createVideoMessage 支持在微信小程序环境使用，从v2.6.0起，支持在 Web 环境使用。
>- 微信小程序录制视频或从相册选择视频文件，没有返回视频缩略图信息。为了更好的体验，SDK 在创建视频消息时会设置默认的缩略图信息。如果接入侧不想展示默认缩略图，可在渲染时忽略缩图相关信息并自行处理。
>- 全平台互通音频消息，移动端请升级使用 [最新的 TUIKit 或 SDK](https://cloud.tencent.com/document/product/269/36887)。

**接口**

```javascript
tim.createAudioMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description                                            |
| ------------------ | -------- | --------------------- |
| `to`               | `String` | 消息的接收方                                           |
| `conversationType` | `String` | 会话类型，取值`TIM.TYPES.CONV_C2C`或`TIM.TYPES.CONV_GROUP` |
| `payload`          | `Object` | 消息内容的容器                                         |

`paylaod`的描述如下表所示：

| Name | Type                        | Description                                                  |
| ---- | --------------------------- | ------------ |
| file | `Object` | 录音后得到的文件信息 |

**小程序示例**

<pre>
// 示例：使用微信官方的 RecorderManager 进行录音，参考 <a href="https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.start.html">RecorderManager.start(Object object)</a>
// 1. 获取全局唯一的录音管理器 RecorderManager
const recorderManager = wx.getRecorderManager();

// 录音部分参数
const recordOptions = {
  duration: 60000, // 录音的时长，单位 ms，最大值 600000（10 分钟）
  sampleRate: 44100, // 采样率
  numberOfChannels: 1, // 录音通道数
  encodeBitRate: 192000, // 编码码率
  format: 'aac' // 音频格式，选择此格式创建的音频消息，可以在即时通信 IM 全平台（Android、iOS、微信小程序和 Web）互通
};

// 2.1 监听录音错误事件
recorderManager.onError(function(errMsg) {
  console.warn('recorder error:', errMsg);
});
// 2.2 监听录音结束事件，录音结束后，调用 createAudioMessage 创建音频消息实例
recorderManager.onStop(function(res) {
  console.log('recorder stop', res);

  // 4. 创建消息实例，接口返回的实例可以上屏
  const message = tim.createAudioMessage({
    to: 'user1',
    conversationType: TIM.TYPES.CONV_C2C,
    payload: {
      file: res
    }
  });

  // 5. 发送消息
  let promise = tim.sendMessage(message);
  promise.then(function(imResponse) {
    // 发送成功
    console.log(imResponse);
  }).catch(function(imError) {
    // 发送失败
    console.warn('sendMessage error:', imError);
  });
});

// 3. 开始录音
recorderManager.start(recordOptions);
</pre>

**返回**

消息实例 [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html)。

### 创建文件消息
创建文件消息的接口，此接口返回一个消息实例，可以在需要发送文件消息时调用 [发送消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 接口发送消息实例。

>!
>! v2.3.1版本开始支持传入 File 对象，使用前需要将 SDK 升级至v2.3.1或以上。
>! v2.4.0版本起，上传文件大小最大值调整为100M。
>! 微信小程序目前不支持选择文件的功能，故该接口暂不支持微信小程序端。

**接口**

```javascript
tim.createFileMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description    |
| ------------------ | -------- | -------------- |
| `to`               | `String` | 消息的接收方   |
| `conversationType` | `String` | 会话类型，取值`TIM.TYPES.CONV_C2C`或`TIM.TYPES.CONV_GROUP` |
| `payload`          | `Object` | 消息内容的容器 |
| `onProgress`          | `function` | 获取上传进度的回调函数 |

`payload`的描述如下表所示：

| Name   | Type     | Description  |
| ------ | -------- | ------------ |
| `file` | `HTMLInputElement` | 用于选择文件的 DOM 节点（Web）或者 File 对象（Web），SDK 会读取其中的数据并上传文件。 |

**示例**

<pre><code class="language-javascript"><span class="hljs-comment">// 发送文件消息</span>
<span class="hljs-comment">// 1. 创建文件消息实例，接口返回的实例可以上屏</span>
<span class="hljs-keyword">let</span> message = createFileMessage({
  <span class="hljs-attr">to</span>: <span class="hljs-string">'user1'</span>,
  <span class="hljs-attr">conversationType</span>: TIM.TYPES.CONV_C2C,
  <span class="hljs-comment">// 消息优先级，用于群聊（v2.4.2起支持）。如果某个群的消息超过了频率限制，后台会优先下发高优先级的消息，详细请参考 <a href="https://cloud.tencent.com/document/product/269/3663#.E6.B6.88.E6.81.AF.E4.BC.98.E5.85.88.E7.BA.A7.E4.B8.8E.E9.A2.91.E7.8E.87.E6.8E.A7.E5.88.B6">消息优先级与频率控制</a></span>
  <span class="hljs-comment">// 支持的枚举值：TIM.TYPES.MSG_PRIORITY_HIGH, TIM.TYPES.MSG_PRIORITY_NORMAL（默认）, TIM.TYPES.MSG_PRIORITY_LOW, TIM.TYPES.MSG_PRIORITY_LOWEST</span>
  <span class="hljs-comment">// priority: TIM.TYPES.MSG_PRIORITY_NORMAL,</span>
  <span class="hljs-attr">payload</span>: {
    <span class="hljs-attr">file</span>: <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'filePicker'</span>),
  },
  <span class="hljs-attr">onProgress</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>{ <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'file uploading:'</span>, event) }
});
<span class="hljs-comment">// 2. 发送消息</span>
<span class="hljs-keyword">let</span> promise = tim.sendMessage(message);
promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">imResponse</span>) </span>{
  <span class="hljs-comment">// 发送成功</span>
  <span class="hljs-built_in">console</span>.log(imResponse);
}).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">imError</span>) </span>{
  <span class="hljs-comment">// 发送失败</span>
  <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'sendMessage error:'</span>, imError);
});
v_vyanzhu(朱焱) <span class="hljs-number">5</span><span class="hljs-number">-13</span> <span class="hljs-number">20</span>:<span class="hljs-number">45</span>:<span class="hljs-number">29</span>
<span class="hljs-comment">// Web 端发送文件消息示例2- 传入 File 对象</span>
<span class="hljs-comment">// 先在页面上添加一个 id 为 "testPasteInput" 的消息输入框，如 &lt;input type="text" id="testPasteInput" placeholder="截图后粘贴到输入框中" size="30" /&gt;</span>
<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'testPasteInput'</span>).addEventListener(<span class="hljs-string">'paste'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>{
  <span class="hljs-keyword">let</span> clipboardData = e.clipboardData;
  <span class="hljs-keyword">let</span> file;
  <span class="hljs-keyword">let</span> fileCopy;
  <span class="hljs-keyword">if</span> (clipboardData &amp;&amp; clipboardData.files &amp;&amp; clipboardData.files.length &gt; <span class="hljs-number">0</span>) {
    file = clipboardData.files[<span class="hljs-number">0</span>];
    <span class="hljs-comment">// 图片消息发送成功后，file 指向的内容可能被浏览器清空，如果接入侧有额外的渲染需求，可以提前复制一份数据</span>
    fileCopy = file.slice();
  }

  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> file === <span class="hljs-string">'undefined'</span>) {
    <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'file 是 undefined，请检查代码或浏览器兼容性！'</span>);
    <span class="hljs-keyword">return</span>;
  }

  <span class="hljs-comment">// 1. 创建消息实例，接口返回的实例可以上屏</span>
  <span class="hljs-keyword">let</span> message = tim.createFileMessage({
    <span class="hljs-attr">to</span>: <span class="hljs-string">'user1'</span>,
    <span class="hljs-attr">conversationType</span>: TIM.TYPES.CONV_C2C,
    <span class="hljs-attr">payload</span>: {
      <span class="hljs-attr">file</span>: file
    },
    <span class="hljs-attr">onProgress</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>{ <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'file uploading:'</span>, event) }
  });

  <span class="hljs-comment">// 2. 发送消息</span>
  <span class="hljs-keyword">let</span> promise = tim.sendMessage(message);
  promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">imResponse</span>) </span>{
    <span class="hljs-comment">// 发送成功</span>
    <span class="hljs-built_in">console</span>.log(imResponse);
  }).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">imError</span>) </span>{
    <span class="hljs-comment">// 发送失败</span>
    <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'sendMessage error:'</span>, imError);
  });
});
</code></pre>

**返回**

消息实例 [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html)。




### 创建自定义消息

创建自定义消息实例的接口，此接口返回一个消息实例，可以在需要发送自定义消息时调用 [发送消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 接口发送消息实例。
当 SDK 提供的能力不能满足您的需求时，可以使用自定义消息进行个性化定制，例如投骰子功能。

**接口**

```javascript
tim.createCustomMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description                                            |
| ------------------ | -------- | ------------------------------------------------------ |
| `to`               | `String` | 消息的接收方                                           |
| `conversationType` | `String` | 会话类型，取值`TIM.TYPES.CONV_C2C`或`TIM.TYPES.CONV_GROUP` |
| `payload`          | `Object` | 消息内容的容器                                         |

`payload`的描述如下表所示：

| Name   | Type     | Description  |
| ------ | -------- | ------------ |
| `data` | `String` | 自定义消息的数据字段 |
| `description` | `String` | 自定义消息的数据字段 |
| `extension` | `String` | 自定义消息的数据字段 |


**示例**

<pre><code class="language-javascript"><span class="hljs-comment">// 示例：利用自定义消息实现投骰子功能</span>
<span class="hljs-comment">// 1. 定义随机函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">random</span>(<span class="hljs-params">min, max</span>) </span>{
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * (max - min + <span class="hljs-number">1</span>) + min);
}
<span class="hljs-comment">// 2. 创建消息实例，接口返回的实例可以上屏</span>
<span class="hljs-keyword">let</span> message = tim.createCustomMessage({
  <span class="hljs-attr">to</span>: <span class="hljs-string">'user1'</span>,
  <span class="hljs-attr">conversationType</span>: TIM.TYPES.CONV_C2C,
    <span class="hljs-comment">// 消息优先级，用于群聊（v2.4.2起支持）。如果某个群的消息超过了频率限制，后台会优先下发高优先级的消息，详细请参考 <a href="https://cloud.tencent.com/document/product/269/3663#.E6.B6.88.E6.81.AF.E4.BC.98.E5.85.88.E7.BA.A7.E4.B8.8E.E9.A2.91.E7.8E.87.E6.8E.A7.E5.88.B6">消息优先级与频率控制</a></span>
  <span class="hljs-comment">// 支持的枚举值：TIM.TYPES.MSG_PRIORITY_HIGH, TIM.TYPES.MSG_PRIORITY_NORMAL（默认）, TIM.TYPES.MSG_PRIORITY_LOW, TIM.TYPES.MSG_PRIORITY_LOWEST</span>
  <span class="hljs-comment">// priority: TIM.TYPES.MSG_PRIORITY_HIGH,</span>
  <span class="hljs-attr">payload</span>: {
    <span class="hljs-attr">data</span>: <span class="hljs-string">'dice'</span>, <span class="hljs-comment">// 用于标识该消息是骰子类型消息</span>
    <span class="hljs-attr">description</span>: <span class="hljs-built_in">String</span>(random(<span class="hljs-number">1</span>,<span class="hljs-number">6</span>)), <span class="hljs-comment">// 获取骰子点数</span>
    <span class="hljs-attr">extension</span>: <span class="hljs-string">''</span>
  }
});
<span class="hljs-comment">// 3. 发送消息</span>
<span class="hljs-keyword">let</span> promise = tim.sendMessage(message);
promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">imResponse</span>) </span>{
  <span class="hljs-comment">// 发送成功</span>
  <span class="hljs-built_in">console</span>.log(imResponse);
}).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">imError</span>) </span>{
  <span class="hljs-comment">// 发送失败</span>
  <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'sendMessage error:'</span>, imError);
});</code></pre>

**返回**

消息实例 [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html)。


### 创建视频消息

创建视频消息实例的接口，此接口返回一个消息实例，可以在需要发送视频消息时调用 [发送消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 接口发送消息实例。 目前 `createVideoMessage` 只支持在微信小程序环境使用。微信小程序录制视频或从相册选择视频文件，不会返回视频缩略图信息。为了更好的体验，SDK 在创建视频消息时会设置默认的缩略图信息。如果接入侧不想展示默认的缩略图，可在渲染时忽略缩图相关信息，自主处理。

>!
>- 全平台互通视频消息，移动端请升级使用 [最新的 TUIKit 或 SDK](https://cloud.tencent.com/document/product/269/36887)。
>- 使用该接口前，需要将 SDK 版本升级至v2.2.0或以上。

**接口**

```javascript
tim.createVideoMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type       | Description                                                |
| ------------------ | ---------- | ---------------------------------------------------------- |
| `to`               | `String`   | 消息的接收方                                               |
| `conversationType` | `String`   | 会话类型，取值`TIM.TYPES.CONV_C2C`或`TIM.TYPES.CONV_GROUP` |
| `payload`          | `Object`   | 录制或从相册选择的视频文件                               |
| `onProgress`       | `function` | 获取上传进度的回调函数                                     |

**示例**

```javascript
// 1. 调用小程序接口选择视频，接口详情请查阅 https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.chooseVideo.html
wx.chooseVideo({
  sourceType: ['album', 'camera'], // 来源相册或者拍摄
  maxDuration: 60, // 设置最长时间60s
  camera: 'back', // 后置摄像头
  success (res) {
    // 2. 创建消息实例，接口返回的实例可以上屏
    let message = tim.createVideoMessage({
      to: 'user1',
      conversationType: TIM.TYPES.CONV_C2C,
      payload: {
        file: res
      },
      onProgress: function(event) { console.log('video uploading:', event) }
    })
    // 3. 发送消息
    let promise = tim.sendMessage(message);
    promise.then(function(imResponse) {
      // 发送成功
      console.log(imResponse);
    }).catch(function(imError) {
      // 发送失败
      console.warn('sendMessage error:', imError);
    });
  }
})
```

**返回**

消息实例 [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html)。

### 创建表情消息

创建表情消息实例的接口，此接口返回一个消息实例，可以在需要发送表情消息时调用 [发送消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 接口发送消息。

>! 使用该接口前，需要将 SDK 版本升级至v2.3.1或以上。

**接口**

```javascript
tim.createFaceMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description                                            |
| ------------------ | -------- | ------------------------------------------------------ |
| `to`               | `String` | 消息的接收方                                           |
| `conversationType` | `String` | 会话类型，取值`TIM.TYPES.CONV_C2C`或`TIM.TYPES.CONV_GROUP` |
| `payload`          | `Object` | 消息内容的容器                                         |

`payload`的描述如下表所示：

| Name   | Type     | Description  |
| ------ | -------- | ------------ |
| `index` | `Number` | 表情索引，用户自定义 |
| `data` | `String` | 额外数据 |

**示例**

```javascript
// 发送表情消息，Web端与小程序端相同。
// 1. 创建消息实例，接口返回的实例可以上屏
let message = tim.createFaceMessage({
  to: 'user1',
  conversationType: TIM.TYPES.CONV_C2C,
  payload: {
    index: 1, // Number 表情索引，用户自定义
    data: 'tt00' // String 额外数据
  }
});
// 2. 发送消息
let promise = tim.sendMessage(message);
promise.then(function(imResponse) {
  // 发送成功
  console.log(imResponse);
}).catch(function(imError) {
  // 发送失败
  console.warn('sendMessage error:', imError);
});
```

**返回**

消息实例 [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html)。


### 发送消息

发送消息的接口，需先调用下列的创建消息实例的接口获取消息实例后，再调用该接口发送消息实例。
- [创建文本消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createTextMessage)
- [创建图片消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createImageMessage)
- [创建音频消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createAudioMessage)
- [创建视频消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createVideoMessage)
- [创建自定义消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createCustomMessage)
- [创建表情消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createFaceVMessage)
- [创建文件消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createFileMessage)

>!调用该接口发送消息实例，需要 SDK 处于 ready 状态，否则将无法发送消息实例。SDK 状态，可通过监听以下事件得到：
- [TIM.EVENT.SDK_READY](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.SDK_READY)：SDK 处于 ready 状态时触发。
- [TIM.EVENT.SDK_NOT_READY](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.SDK_NOT_READY)：SDK 处于 not ready 状态时触发。


接收推送的单聊、群聊、群提示、群系统通知的新消息，需监听事件 [TIM.EVENT.MESSAGE_RECEIVED](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_RECEIVED)。
本实例发送的消息，不会触发事件 [TIM.EVENT.MESSAGE_RECEIVED](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_RECEIVED)。同帐号从其他端（或通过 REST API）发送的消息，会触发事件 [TIM.EVENT.MESSAGE_RECEIVED](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_RECEIVED), 离线推送仅适用于终端（Android 或 iOS)，Web 和 微信小程序不支持。 

**接口**

```javascript
tim.sendMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description    |
| ------------------ | -------- | -------------- |
| `message`               | `Message` | 消息实例   |

**示例**

```javascript
// 如果接收方不在线，则消息将存入漫游，且进行离线推送（在接收方 App 退后台或者进程被 kill 的情况下）。离线推送的标题和内容使用默认值。
// 离线推送的说明请参考 https://cloud.tencent.com/document/product/269/3604
tim.sendMessage(message);
// v2.6.4起支持消息发送选项
tim.sendMessage(message, {
  onlineUserOnly: true // 如果接收方不在线，则消息不存入漫游，且不会进行离线推送
});
// v2.6.4起支持消息发送选项
tim.sendMessage(message, {
  offlinePushInfo: {
    disablePush: true // 如果接收方不在线，则消息将存入漫游，但不进行离线推送
  }
});
// v2.6.4起支持消息发送选项
tim.sendMessage(message, {
  // 如果接收方不在线，则消息将存入漫游，且进行离线推送（在接收方 App 退后台或者进程被 kill 的情况下）。接入侧可自定义离线推送的标题及内容
  offlinePushInfo: {
    title: '', // 离线推送标题
    description: '', // 离线推送内容
    androidOPPOChannelID: '' // 离线推送设置 OPPO 手机8.0系统及以上的渠道 ID
  }
});
```

**返回**

**Type** : `Promise`

### 撤回消息

撤回单聊消息或者群聊消息。撤回成功后，消息对象的 `isRevoked` 属性值为 `true`。

>!
>- 使用该接口前，需要将 SDK 版本升级至v2.4.0或以上。
>- 消息可撤回时间默认为2分钟。可通过 [控制台](https://console.cloud.tencent.com/im-detail/login-message) 调整消息可撤回时间。
>- 被撤回的消息，可以调用 [getMessageList](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getMessageList) 接口从单聊或者群聊消息漫游中拉取到。接入侧需根据消息对象的 isRevoked 属性妥善处理被撤回消息的展示。例如，单聊会话内可展示为 "对方撤回了一条消息"，群聊会话内可展示为 "张三撤回了一条消息"。
>- 可使用 REST API [撤回单聊消息](https://cloud.tencent.com/document/product/269/38980) 或 [撤回群聊消息](https://cloud.tencent.com/document/product/269/12341)。

**接口**

```javascript
tim.revokeMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description    |
| ------------------ | -------- | -------------- |
| `message`               | `Message` | 消息实例   |

**示例**

```javascript
// 主动撤回消息
let promise = tim.revokeMessage(message);
promise.then(function(imResponse) {
  // 消息撤回成功
}).catch(function(imError) {
  // 消息撤回失败
  console.warn('revokeMessage error:', imError);
});
```

```javascript
// 收到消息被撤回的通知
tim.on(TIM.EVENT.MESSAGE_REVOKED, function(event) {
  // event.name - TIM.EVENT.MESSAGE_REVOKED
  // event.data - 存储 Message 对象的数组 - [Message] - 每个 Message 对象的 isRevoked 属性值为 true
});
```

```javascript
// 获取会话的消息列表时遇到被撤回的消息
let promise = tim.getMessageList({conversationID: 'C2Ctest', count: 15});
promise.then(function(imResponse) {
  const messageList = imResponse.data.messageList; // 消息列表
  messageList.forEach(function(message) {
    if (message.isRevoked) {
      // 处理被撤回的消息
    } else {
      // 处理普通消息
    }
  });
});
```

**返回**

**Type** : `Promise`

### 重发消息

重发消息的接口，当消息发送失败时，调用该接口进行重发。

**接口**

```javascript
tim.resendMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description    |
| ------------------ | -------- | -------------- |
| `message`               | `Message` | 消息实例   |

**示例**

```javascript
// 重发消息
let promise = tim.resendMessage(message); // 传入需要重发的消息实例
promise.then(function(imResponse) {
  // 重发成功
  console.log(imResponse.data.message);
}).catch(function(imError) {
  // 重发失败
  console.warn('resendMessage error:', imError);
});
```

**返回**

该接口返回 `Promise` 对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.groupList`中获取群组列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。



## 接收消息

### 接收消息

请参考 [接收消息事件](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_RECEIVED)。

接受消息的接口，接收消息需要通过事件监听实现：

**示例**

```javascript
let onMessageReceived = function(event) {
  // event.data - 存储 Message 对象的数组 - [Message]
};
tim.on(TIM.EVENT.MESSAGE_RECEIVED, onMessageReceived);
```



### 解析文本消息

<ul><li><b>简单版</b><br>
 如果您的文本消息只含有文字，则可以直接在 UI 上渲染出`'xxxxxxx'`文字。</li>
<li><b>含有 [呲牙] 内容需要解析为<img src="https://main.qcloudimg.com/raw/6be88c30a4552b5eb93d8eec243b6593.png"  style="margin:0;">的文本</b>

```javascript
const emojiMap = {         // 根据[呲牙]可匹配的路径地址
  '[微笑]': 'emoji_0.png',
  '[呲牙]': 'emoji_1.png',
  '[下雨]': 'emoji_2.png'
}

const emojiUrl = 'http://xxxxxxxx/emoji/'   // 为<img src="https://main.qcloudimg.com/raw/6be88c30a4552b5eb93d8eec243b6593.png"  style="margin:0;">图片的地址

function parseText (payload) {
  let renderDom = []
  // 文本消息
    let temp = payload.text
    let left = -1
    let right = -1
    while (temp !== '') {
      left = temp.indexOf('[')
      right = temp.indexOf(']')
      switch (left) {
        case 0:
          if (right === -1) {
            renderDom.push({
              name: 'text',
              text: temp
            })
            temp = ''
          } else {
            let _emoji = temp.slice(0, right + 1)
            if (emojiMap[_emoji]) {    // 如果您需要渲染表情包，需要进行匹配您对应[呲牙]的表情包地址
              renderDom.push({
                name: 'img',
                src: emojiUrl + emojiMap[_emoji]
              })
              temp = temp.substring(right + 1)
            } else {
              renderDom.push({
                name: 'text',
                text: '['
              })
              temp = temp.slice(1)
            }
          }
          break
        case -1:
          renderDom.push({
            name: 'text',
            text: temp
          })
          temp = ''
          break
        default:
          renderDom.push({
            name: 'text',
            text: temp.slice(0, left)
          })
          temp = temp.substring(left)
          break
      }
    }
  return renderDom
}


// 最后的 renderDom 结构为[{name: 'text', text: 'XXX'}, {name: 'img', src: 'http://xxx'}......]
// 渲染当前数组即可得到想要的 UI 结果，如：XXX<img src="https://main.qcloudimg.com/raw/6be88c30a4552b5eb93d8eec243b6593.png"  style="margin:0;">XXX<img src="https://main.qcloudimg.com/raw/6be88c30a4552b5eb93d8eec243b6593.png"  style="margin:0;">XXX[呲牙XXX]
```
</li></ul>


### 解析系统消息

```javascript
function parseGroupSystemNotice (payload) {
  const groupName =
      payload.groupProfile.groupName || payload.groupProfile.groupID
  switch (payload.operationType) {
    case 1:
      return `${payload.operatorID} 申请加入群组：${groupName}`
    case 2:
      return `成功加入群组：${groupName}`
    case 3:
      return `申请加入群组：${groupName}被拒绝`
    case 4:
      return `被管理员${payload.operatorID}踢出群组：${groupName}`
    case 5:
      return `群：${groupName} 已被${payload.operatorID}解散`
    case 6:
      return `${payload.operatorID}创建群：${groupName}`
    case 7:
      return `${payload.operatorID}邀请你加群：${groupName}`
    case 8:
      return `你退出群组：${groupName}`
    case 9:
      return `你被${payload.operatorID}设置为群：${groupName}的管理员`
    case 10:
      return `你被${payload.operatorID}撤销群：${groupName}的管理员身份`
    case 255:
      return '自定义群系统通知'
  }
}
```



### 解析群提示消息

```javascript
function parseGroupTipContent (payload) {
  switch (payload.operationType) {
    case this.TIM.TYPES.GRP_TIP_MBR_JOIN:
      return `群成员：${payload.userIDList.join(',')}，加入群组`
    case this.TIM.TYPES.GRP_TIP_MBR_QUIT:
      return `群成员：${payload.userIDList.join(',')}，退出群组`
    case this.TIM.TYPES.GRP_TIP_MBR_KICKED_OUT:
      return `群成员：${payload.userIDList.join(',')}，被${payload.operatorID}踢出群组`
    case this.TIM.TYPES.GRP_TIP_MBR_SET_ADMIN:
      return `群成员：${payload.userIDList.join(',')}，成为管理员`
    case this.TIM.TYPES.GRP_TIP_MBR_CANCELED_ADMIN:
      return `群成员：${payload.userIDList.join(',')}，被撤销管理员`
    default:
      return '[群提示消息]'
  }
}
```



## 会话相关

### 获取某会话的消息列表 

请参考 [Conversation](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Conversation.html)。

分页拉取指定会话的消息列表的接口，当用户进入会话首次渲染消息列表或者用户“下拉查看更多消息”时，需调用该接口。

**接口**

```javascript
tim.getMessageList(options)
```

>!该接口可用于"拉取历史消息"。

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Attributes | Default | Description    |
| ------------------ | -------- | -------------- | -------------- | -------------- |
| `conversationID`   | `String` |      -     |    -       | 会话 ID          |
| `nextReqMessageID`   | `String` |       -    |     -      | 用于分页续拉的消息 ID。第一次拉取时该字段可不填，每次调用该接口会返回该字段，续拉时将返回字段填入即可          |
| `count`   | `Number` | `<optional>` | 15       | 需要拉取的消息数量，默认值和最大值为15，即一次拉取至多返回15条消息         |

**示例**

```javascript
// 打开某个会话时，第一次拉取消息列表
let promise = tim.getMessageList({conversationID: 'C2Ctest', count: 15});
promise.then(function(imResponse) {
  const messageList = imResponse.data.messageList; // 消息列表。
  const nextReqMessageID = imResponse.data.nextReqMessageID; // 用于续拉，分页续拉时需传入该字段。
  const isCompleted = imResponse.data.isCompleted; // 表示是否已经拉完所有消息。
});
```

```javascript
// 打开某个会话时，第一次拉取消息列表
// 下拉查看更多消息
let promise = tim.getMessageList({conversationID: 'C2Ctest', nextReqMessageID, count: 15});
promise.then(function(imResponse) {
  const messageList = imResponse.data.messageList; // 消息列表。
  const nextReqMessageID = imResponse.data.nextReqMessageID; // 用于续拉，分页续拉时需传入该字段。
  const isCompleted = imResponse.data.isCompleted; // 表示是否已经拉完所有消息。
});
```

**返回**

该接口返回 `Promise` 对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.groupList`中获取群组列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

### 将会话设置为已读

将某会话下的未读消息状态设置为已读，置为已读的消息不会计入到未读统计，当打开会话或切换会话时调用该接口。如果在打开/切换会话时，不调用该接口，则对应的消息会一直是未读的状态。

**接口**

```javascript
tim.setMessageRead(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description    |
| ------------------ | -------- | -------------- |
| `conversationID` | `String` | 会话 ID |

**示例**

```javascript
// 将某会话下所有未读消息已读上报
tim.setMessageRead({conversationID: 'C2Cexample'});
```



### 获取会话列表

获取会话列表的接口，该接口拉取最近的100条会话，当需要刷新会话列表时调用该接口。

**接口**

```javascript
tim.getConversationList()
```

**示例**

```javascript
// 拉取会话列表
let promise = tim.getConversationList();
promise.then(function(imResponse) {
  const conversationList = imResponse.data.conversationList; // 会话列表，用该列表覆盖原有的会话列表
}).catch(function(imError) {
  console.warn('getConversationList error:', imError); // 获取会话列表失败的相关信息
});
```

**返回**

该接口返回 `Promise` 对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.groupList`中获取群组列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。



### 获取会话资料

获取会话资料的接口，当单击会话列表中的某个会话时，调用该接口获取会话的详细信息。

>!
>- 该接口获取的会话列表中的资料仅包括头像、昵称等，能够满足会话列表的渲染需求，若要查询详细会话资料，可参考 [getConversationProfile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#getConversationProfile)。
>- 会话保存时长跟会话最后一条消息保存时间一致。

**接口**

```javascript
tim.getConversationProfile(conversationID)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description    |
| ------------------ | -------- | -------------- |
| `conversationID` | `String` | 会话 ID |

**示例**

```javascript
let promise = tim.getConversationProfile(conversationID);
promise.then(function(imResponse) {
  // 获取成功
  console.log(imResponse.data.conversation); // 会话资料
}).catch(function(imError) {
  console.warn('getConversationProfile error:', imError); // 获取会话资料失败的相关信息
});
```

**返回**

该接口返回 `Promise` 对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.groupList`中获取群组列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。



### 删除会话

根据会话 ID 删除会话的接口，该接口只删除会话，不删除消息。例如，删除与用户 A 的会话，下次再与用户 A 发起会话时，之前的聊天信息仍在。

**接口**

```javascript
tim.deleteConversation(conversationID)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description    |
| ------------------ | -------- | -------------- |
| `conversationID` | `String` | 会话 ID |

**示例**

```javascript
let promise = tim.deleteConversation('C2CExample');
promise.then(function(imResponse) {
  //删除成功。
  const { conversationID } = imResponse.data;// 被删除的会话 ID。
}).catch(function(imError) {
  console.warn('deleteConversation error:', imError); // 删除会话失败的相关信息
});
```

**返回**

该接口返回 `Promise` 对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.groupList`中获取群组列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。
