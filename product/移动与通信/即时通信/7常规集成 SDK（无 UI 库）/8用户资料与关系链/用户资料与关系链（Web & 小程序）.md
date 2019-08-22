## 用户资料

### 获取我的个人资料

> 参考：[Profile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Profile.html)

获取个人资料

**接口名**

```js
tim.getMyProfile()
```

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data`中拿到个人信息。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.getMyProfile();
promise.then(function(imResponse) {
  console.log(imResponse.data); // 个人资料 - Profile 实例
}).catch(function(imError) {
  console.warn('getMyProfile error:', imError); // 获取个人资料失败的相关信息
});
```



### 获取用户资料

**接口名**

```js
tim.getUserProfile(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称         | 类型            | 描述                       |
| :----------- | :-------------- | :------------------------- |
| `userIDList` | `Array<String>` | 用户的账号列表，类型为数组 |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data`中拿到用户资料数组。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.getUserProfile({
  userIDList: ['user1', 'user2'] // 请注意：即使只拉取一个用户的资料，也需要用数组类型，如：userIDList: ['user1']
});
promise.then(function(imResponse) {
  console.log(imResponse.data); // 存储用户资料的数组 - [Profile]
}).catch(function(imError) {
  console.warn('getUserProfile error:', imError); // 获取其他用户资料失败的相关信息
});
```



### 更新个人资料

**接口名**

```js
tim.updateMyProfile(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称              | 类型     | 描述                                                         |
| :---------------- | :------- | :----------------------------------------------------------- |
| `nick`            | `String` | 昵称                                                         |
| `avatar`          | `String` | 头像地址                                                     |
| `gender`          | `String` | 性别：<br>TIM.TYPES.GENDER_UNKNOWN(未设置性别)<br/>TIM.TYPES.GENDER_FEMALE(女) <br/>TIM.TYPES.GENDER_MALE(男) |
| `selfSignature`   | `String` | 个性签名                                                     |
| `allowType`       | `String` | 当被加人加好友时：<br/>TIM.TYPES.ALLOW_TYPE_ALLOW_ANY(允许直接加为好友)<br/> TIM.TYPES.ALLOW_TYPE_NEED_CONFIRM(需要验证)<br/> TIM.TYPES.ALLOW_TYPE_DENY_ANY(拒绝) |
| `birthday`        | `Number` | 生日 推荐用法：20000101                                      |
| `location`        | `String` | 所在地 推荐用法：App 本地定义一套数字到地名的映射关系 后台实际保存的是4个 uint32_t 类型的数字： 其中第一个 uint32_t 表示国家； 第二个 uint32_t 用于表示省份； 第三个 uint32_t 用于表示城市； 第四个 uint32_t 用于表示区县 |
| `language`        | `Number` | 语言                                                         |
| `messageSettings` | `Number` | 消息设置 0：接收消息，1：不接收消息                          |
| `adminForbidType` | `String` | 管理员禁止加好友标识：<br>TIM.TYPES.FORBID_TYPE_NONE(默认值，允许加好友)<br/> TIM.TYPES.FORBID_TYPE_SEND_OUT(禁止该用户发起加好友请求) |
| `level`           | `Number` | 等级 建议拆分以保存多种角色的等级信息                        |
| `role`            | `Number` | 角色 建议拆分以保存多种角色信息                              |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data`中拿到用户的新资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.updateMyProfile({
  nick: '我的昵称',
  avatar: 'http(s)://url/to/image.jpg',
  gender: TIM.TYPES.GENDER_MALE,
  selfSignature: '我的个性签名',
  allowType: TIM.TYPES.ALLOW_TYPE_ALLOW_ANY
});
promise.then(function(imResponse) {
  console.log(imResponse.data); // 更新资料成功
}).catch(function(imError) {
  console.warn('updateMyProfile error:', imError); // 更新资料失败的相关信息
});
```



## 黑名单

### 获取我的黑名单列表

**接口名**

```js
tim.getBlacklist()
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data`中拿到黑名单列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.getBlacklist();
promise.then(function(imResponse) {
  console.log(imResponse.data); // 我的黑名单列表，结构为包含用户 userID 的数组 - [userID]
}).catch(function(imError) {
  console.warn('getBlacklist error:', imError); // 获取黑名单列表失败的相关信息
});
```



### 添加用户到黑名单列表

添加用户到黑名单列表。将用户加入黑名单后可以屏蔽来自TA的所有消息，因此该接口可以实现“屏蔽该用户消息”的功能

- 如果用户 A 与用户 B 之间存在好友关系，拉黑时会解除双向好友关系
- 如果用户 A 与用户 B 之间存在黑名单关系，二者之间无法发起会话
- 如果用户 A 与用户 B 之间存在黑名单关系，二者之间无法发起加好友请求

**接口名**

```js
tim.addToBlacklist(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称         | 类型            | 描述                                                         |
| :----------- | :-------------- | :----------------------------------------------------------- |
| `userIDList` | `Array<String>` | 待添加为黑名单的用户 userID 列表，单次请求的 userID 数不得超过 1000 |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data`中拿到黑名单列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.addToBlacklist({userIDList: ['user1', 'user2']}); // 请注意：即使只添加一个用户账号到黑名单，也需要用数组类型，如：userIDList: ['user1']
promise.then(function(imResponse) {
  console.log(imResponse.data); // 成功添加到黑名单的账号信息，结构为包含用户 userID 的数组 - [userID]
}).catch(function(imError) {
  console.warn('addToBlacklist error:', imError); // 添加用户到黑名单列表失败的相关信息
});
```



### 将用户从黑名单中移除

将用户从黑名单中移除。移除后，可以接收来自TA的所有消息

**接口名**

```js
tim.removeFromBlacklist(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称         | 类型            | 描述                                                         |
| :----------- | :-------------- | :----------------------------------------------------------- |
| `userIDList` | `Array<String>` | 待从黑名单中移除的 userID 列表，单次请求的 userID 数不得超过1000 |

**返回值**

该接口返回 `Promise` 对象

- `then` 的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data`中拿到从黑名单中成功移除的账号列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.removeFromBlacklist({userIDList: ['user1', 'user2']}); // 请注意：即使只从黑名单中移除一个用户账号，也需要用数组类型，如：userIDList: ['user1']
result.then(function(imResponse) {
  console.log(imResponse.data); // 从黑名单中成功移除的账号列表，结构为包含用户 userID 的数组 - [userID]
}).catch(function(imError) {
  console.warn('removeFromBlacklist error:', imError); // 将用户从黑名单中移除失败的相关信息
});
```



## 好友与关系链相关

开发中，敬请期待