## 用户资料

### 获取我的个人资料
获取个人资料，更多详情请参见 [Profile](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/Profile.html)。

>! v2.3.2版本开始支持自定义资料字段，使用前需要将 SDK 升级至v2.3.2或以上。

**接口名**

```js
tim.getMyProfile()
```

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data`中获取个人信息。
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



### 获取其他用户资料
此接口会同时获取标配资料和 [自定义资料](https://cloud.tencent.com/document/product/269/1500#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5)。

>!
>- v2.3.2版本开始支持自定义资料字段，使用前需要将 SDK 升级至v2.3.2或以上。
>- 如果您没有配置自定义资料字段，或者配置了自定义资料字段但未设置 value，此接口将不会返回自定义资料的内容。
>- 每次拉取的用户数不超过100，避免因回包数据量太大导致回包失败。如果传入的数组长度大于100，则只取前100个用户进行查询，其余丢弃。 

**接口名**

```js
tim.getUserProfile(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称         | 类型            | 描述                       |
| :----------- | :-------------- | :------------------------- |
| `userIDList` | `Array<String>` | 用户的帐号列表，类型为数组 |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data`中获取用户资料数组。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.getUserProfile({
  userIDList: ['user1', 'user2'] // 请注意：即使只拉取一个用户的资料，也需要用数组类型，例如：userIDList: ['user1']
});
promise.then(function(imResponse) {
  console.log(imResponse.data); // 存储用户资料的数组 - [Profile]
}).catch(function(imError) {
  console.warn('getUserProfile error:', imError); // 获取其他用户资料失败的相关信息
});
```



### 更新个人资料

>! v2.3.2版本开始支持自定义资料字段，使用前需要将 SDK 升级至v2.3.2或以上。

**接口名**

```js
tim.updateMyProfile(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称              | 类型     | 描述                                                         |
| :---------------- | :------- | :----------------------------------------------------------- |
| `nick`            | `String` | 昵称                                                         |
| `avatar`          | `String` | 头像地址                                                     |
| `gender`          | `String` | 性别<li>TIM.TYPES.GENDER_UNKNOWN 表示未设置性别<li>TIM.TYPES.GENDER_FEMALE 表示女 </li><li>TIM.TYPES.GENDER_MALE 表示男</li> |
| `selfSignature`   | `String` | 个性签名                                                     |
| `allowType`       | `String` | 当被加人加好友时是否需要验证<li>TIM.TYPES.ALLOW_TYPE_ALLOW_ANY 表示允许直接加为好友</li><li> TIM.TYPES.ALLOW_TYPE_NEED_CONFIRM 表示需要验证</li><li>TIM.TYPES.ALLOW_TYPE_DENY_ANY 表示拒绝</li> |
| `birthday`        | `Number` | 生日，推荐用法：20000101                                      |
| `location`        | `String` | 所在地，推荐用法：App 本地定义一套数字到地名的映射关系，后台实际保存的是4个 uint32_t 类型的数字：<li>第一个 uint32_t 表示国家</li><li>第二个 uint32_t 用于表示省份</li><li>第三个 uint32_t 用于表示城市</li><li>第四个 uint32_t 用于表示区县 |
| `language`        | `Number` | 语言                                                         |
| `messageSettings` | `Number` | 消息设置，0表示接收消息，1表示不接收消息                          |
| `adminForbidType` | `String` | 管理员禁止加好友标识：<li>TIM.TYPES.FORBID_TYPE_NONE 表示允许加好友，默认值</li><li>TIM.TYPES.FORBID_TYPE_SEND_OUT 表示禁止该用户发起加好友请求</li> |
| `level`           | `Number` | 等级，建议拆分以保存多种角色的等级信息                        |
| `role`            | `Number` | 角色，建议拆分以保存多种角色信息                              |
| `profileCustomField` | `Array<Object>` | [自定义资料](https://cloud.tencent.com/document/product/269/1500#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5) 键值对集合，可根据业务侧需要使用|

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data`中获取用户的新资料。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
// 修改个人标配资料
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

```js
// 修改个人自定义资料
// 自定义资料字段需要预先在控制台配置，详细请参考：https://cloud.tencent.com/document/product/269/1500#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5
let promise = tim.updateMyProfile({
  // 这里要求您已在即时通信 IM 控制台>【应用配置】>【功能配置】 申请了自定义资料字段 Tag_Profile_Custom_Test1
  // 注意：即使只有一个自定义资料字段，profileCustomField 也需要用数组类型
  profileCustomField: [
    {
      key: 'Tag_Profile_Custom_Test1',
      value: '我的自定义资料1'
    }
  ]
});
promise.then(function(imResponse) {
  console.log(imResponse.data); // 更新资料成功
}).catch(function(imError) {
  console.warn('updateMyProfile error:', imError); // 更新资料失败的相关信息
});
```

```js
// 修改个人标配资料和自定义资料
let promise = tim.updateMyProfile({
  nick: '我的昵称',
  // 这里要求您已在即时通信 IM 控制台>【应用配置】>【功能配置】 申请了自定义资料字段 Tag_Profile_Custom_Test1 和 Tag_Profile_Custom_Test2
  profileCustomField: [
    {
      key: 'Tag_Profile_Custom_Test1',
      value: '我的自定义资料1'
    },
    {
      key: 'Tag_Profile_Custom_Test2',
      value: '我的自定义资料2'
    },
  ]
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

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data`中获取黑名单列表。
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

添加用户到黑名单列表。将用户加入黑名单后可以屏蔽来自 TA 的所有消息，因此该接口可以实现“屏蔽该用户消息”的功能。

- 如果用户 A 与用户 B 之间存在好友关系，拉黑时会解除双向好友关系。
- 如果用户 A 与用户 B 之间存在黑名单关系，二者之间无法发起加好友请求。
- 如果用户 A 的黑名单中有用户 B 且用户 B 的黑名单中有用户 A，二者之间无法发起会话。
- 如果用户 A 的黑名单中有用户 B 但用户 B 的黑名单中没有用户 A，那么用户 A 可以给用户 B 发消息，用户 B 不能给用户 A 发消息。

**接口名**

```js
tim.addToBlacklist(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下：

| 名称         | 类型            | 描述                                                         |
| :----------- | :-------------- | :----------------------------------------------------------- |
| `userIDList` | `Array<String>` | 待添加为黑名单的用户 userID 列表，单次请求的 userID 数不得超过1000 |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data`中获取黑名单列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.addToBlacklist({userIDList: ['user1', 'user2']}); // 请注意：即使只添加一个用户帐号到黑名单，也需要用数组类型，例如：userIDList: ['user1']
promise.then(function(imResponse) {
  console.log(imResponse.data); // 成功添加到黑名单的帐号信息，结构为包含用户 userID 的数组 - [userID]
}).catch(function(imError) {
  console.warn('addToBlacklist error:', imError); // 添加用户到黑名单列表失败的相关信息
});
```



### 将用户从黑名单中移除

将用户从黑名单中移除。移除后，可以接收来自 TA 的所有消息。

**接口名**

```js
tim.removeFromBlacklist(options)
```

**请求参数**

参数`options`为`Object`类型，包含的属性值如下表所示：

| 名称         | 类型            | 描述                                                         |
| :----------- | :-------------- | :----------------------------------------------------------- |
| `userIDList` | `Array<String>` | 待从黑名单中移除的 userID 列表，单次请求的 userID 数不得超过1000 |

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，可在`IMResponse.data`中获取从黑名单中成功移除的帐号列表。
- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.removeFromBlacklist({userIDList: ['user1', 'user2']}); // 请注意：即使只从黑名单中移除一个用户帐号，也需要用数组类型，例如：userIDList: ['user1']
result.then(function(imResponse) {
  console.log(imResponse.data); // 从黑名单中成功移除的帐号列表，结构为包含用户 userID 的数组 - [userID]
}).catch(function(imError) {
  console.warn('removeFromBlacklist error:', imError); // 将用户从黑名单中移除失败的相关信息
});
```
