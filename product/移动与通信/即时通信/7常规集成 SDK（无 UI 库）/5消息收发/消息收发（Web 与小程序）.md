## 发送消息

### 创建文本消息
创建文本消息的接口，此接口返回一个消息实例，可以在需要发送文本消息时调用 [发送消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 接口发送消息。


**接口名**

```javascript
tim.createTextMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description                                            |
| ------------------ | -------- | ------------------------------------------------------ |
| `to`               | `String` | 消息的接收方                                           |
| `conversationType` | `String` | 会话类型，取值`tim.TYPES.CONV_C2C`或`tim.TYPES.CONV_GROUP` |
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
  conversationType: TIM.TYPES.CONV_C2C
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
创建图片消息的接口，此接口返回一个消息实例，可以在需要发送图片消息时调用 [发送消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 接口发送消息。


**接口**

```javascript
tim.createImageMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description                                            |
| ------------------ | -------- | ------------------------------------------------------ |
| `to`               | `String` | 消息的接收方                                           |
| `conversationType` | `String` | 会话类型，取值`tim.TYPES.CONV_C2C`或`tim.TYPES.CONV_GROUP` |
| `payload`          | `Object` | 消息内容的容器                                         |

`paylaod`的描述如下表所示：

| Name | Type                        | Description                                                  |
| ---- | --------------------------- | ------------------------------------------------------------ |
| file | `HTMLInputElement 或 Object` | 用于选择图片的 DOM 节点（Web）或者微信小程序 `wx.chooseImage` 接口的 `success` 回调参数。SDK 会读取其中的数据并上传图片。 |

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



### 创建文件消息
创建文件消息的接口，此接口返回一个消息实例，可以在需要发送文件消息时调用 [发送消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 接口发送消息。

>!微信小程序目前不支持选择文件的功能，故该接口暂不支持微信小程序端。

**接口**

```javascript
tim.createFileMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description    |
| ------------------ | -------- | -------------- |
| `to`               | `String` | 消息的接收方   |
| `conversationType` | `String` | 会话类型，取值`tim.TYPES.CONV_C2C`或`tim.TYPES.CONV_GROUP` |
| `payload`          | `Object` | 消息内容的容器 |
| `onProgress`          | `function` | 获取上传进度的回调函数 |

`payload`的描述如下表所示：

| Name   | Type     | Description  |
| ------ | -------- | ------------ |
| `file` | `HTMLInputElement` | 用于选择文件的 DOM 节点，SDK 会读取其中的数据并上传文件。 |

**示例**

```javascript
// 发送文件消息
// 1. 创建文件消息实例，接口返回的实例可以上屏
let message = createFileMessage({
  to: 'user1',
  conversationType: TIM.TYPES.CONV_C2C,
  payload: {
    file: document.getElementById('filePicker'),
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

**返回**

消息实例 [Message](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Message.html)




### 创建自定义消息

创建自定义消息实例的接口，此接口返回一个消息实例，可以在需要发送自定义消息时调用 [发送消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 接口发送消息。
当 SDK 提供的能力不能满足您的需求时，可以使用自定义消息进行个性化定制，例如投骰子功能。

**接口**

```javascript
tim.createTextMessage(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Description                                            |
| ------------------ | -------- | ------------------------------------------------------ |
| `to`               | `String` | 消息的接收方                                           |
| `conversationType` | `String` | 会话类型，取值`tim.TYPES.CONV_C2C`或`tim.TYPES.CONV_GROUP` |
| `payload`          | `Object` | 消息内容的容器                                         |

`payload`的描述如下表所示：

| Name   | Type     | Description  |
| ------ | -------- | ------------ |
| `data` | `String` | 自定义消息的数据字段 |
| `description` | `String` | 自定义消息的数据字段 |
| `extension` | `String` | 自定义消息的数据字段 |


**示例**

```javascript
// 示例：利用自定义消息实现投骰子功能
// 1. 定义随机函数
function random(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
// 2. 创建消息实例，接口返回的实例可以上屏
let message = tim.createCustomMessage({
  to: 'user1',
  conversationType: TIM.TYPES.CONV_C2C,
  payload: {
    data: 'dice', // 用于标识该消息是骰子类型消息
    description: String(random(1,6)), // 获取骰子点数
    extension: ''
  }
});
// 3. 发送消息
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
- [创建文件消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createFileMessage)
- [创建自定义消息](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#createCustomMessage)

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
// 发送文本消息，Web 端与小程序端相同
// 1. 将生成的Message实例发送
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

请参考：[接收消息事件](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.MESSAGE_RECEIVED)

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
<li><b>含有 [呲牙] 内容需要解析为<img src="https://main.qcloudimg.com/raw/6be88c30a4552b5eb93d8eec243b6593.png"  style="margin:0;">的文本</b>

<pre>
const emojiMap = {         // 根据[呲牙]可匹配的路径地址
  '[微笑]': 'emoji_0.png',
  '[呲牙]': 'emoji_1.png',
  '[下雨]': 'emoji_2.png'
}

const emojiUrl = 'http://xxxxxxxx/emoji/'   // 为<img src="https://main.qcloudimg.com/raw/6be88c30a4552b5eb93d8eec243b6593.png"  style="margin:0;">图片的地址

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
// 渲染当前数组即可得到想要的 UI 结果，例如：XXX<img src="https://main.qcloudimg.com/raw/6be88c30a4552b5eb93d8eec243b6593.png"  style="margin:0;">XXX<img src="https://main.qcloudimg.com/raw/6be88c30a4552b5eb93d8eec243b6593.png"  style="margin:0;">XXX[呲牙XXX]
</pre>
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

> See:	[Conversation](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Conversation.html)

分页拉取指定会话的消息列表的接口，当用户进入会话首次渲染消息列表或者用户“下拉查看更多消息”时，需调用该接口。

**接口**

```javascript
tim.getMessageList(options)
```

**参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| Name               | Type     | Attributes | Default | Description    |
| ------------------ | -------- | -------------- | -------------- | -------------- |
| `conversationID`   | `String` |      -     |    -       | 会话 ID          |
| `nextReqMessageID`   | `String` |       -    |     -      | 用于分页续拉的消息 ID。第一次拉取时该字段可不填，每次调用该接口会返回该字段，续拉时将返回字段填入即可。          |
| `count`   | `Number` | `<optional>` | 15       | 需要拉取的消息数量，最大值为15         |

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
  const conversationList = imResponse.data.conversationList; // 会话列表，用该列表覆盖原有的会话列表。
}).catch(function(imError) {
  console.warn('getConversationList error:', imError); // 获取会话列表失败的相关信息
});
```

**返回**

该接口返回 `Promise` 对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data.groupList`中获取群组列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。



### 获取会话资料

获取会话资料的接口，当单机会话列表中的某个会话时，调用该接口获取会话的详细信息。

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

根据会话 ID 删除会话的接口。

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
