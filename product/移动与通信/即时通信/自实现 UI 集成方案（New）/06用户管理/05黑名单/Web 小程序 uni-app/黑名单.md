## 功能描述

如果您需屏蔽某人的消息，可以把该用户拉入黑名单。

## 黑名单
### 拉黑某人

添加用户到黑名单列表。将用户加入黑名单后可以屏蔽来自 TA 的所有消息，因此该接口可以实现“屏蔽该用户消息”的功能。

- 如果用户 A 与用户 B 之间存在好友关系，拉黑时会解除双向好友关系。
- 如果用户 A 与用户 B 之间存在黑名单关系，二者之间无法发起会话。
- 如果用户 A 与用户 B 之间存在黑名单关系，二者之间无法发起加好友请求。

**接口**

<dx-codeblock>
:::  js

tim.addToBlacklist(options);

:::
</dx-codeblock>

**参数**

参数 options 为 Object 类型，包含的属性值如下：

| Name               | Type     | Description                                                  |
| ------------------ | -------- | ------------------------------------------------------------ |
| userIDList | Array | 待添加为黑名单的用户 userID 列表，单次请求的 userID 数不得超过1000 |

**返回值**

`Promise` 对象。

**示例**

<dx-codeblock>
:::  js

let promise = tim.addToBlacklist({userIDList: ['user1', 'user2']}); // 请注意：即使只添加一个用户帐号到黑名单，也需要用数组类型，例如：userIDList: ['user1']
promise.then(function(imResponse) {
  console.log(imResponse.data); // 成功添加到黑名单的帐号信息，结构为包含用户 userID 的数组 - [userID]
}).catch(function(imError) {
  console.warn('addToBlacklist error:', imError); // 添加用户到黑名单列表失败的相关信息
});

:::
</dx-codeblock>

### 解除拉黑

从黑名单中移除对方后可再次接收对方的消息。

**接口**

<dx-codeblock>
:::  js

tim.removeFromBlacklist(options);

:::
</dx-codeblock>

**参数**

参数 options 为 Object 类型，包含的属性值如下：

| Name               | Type     | Description                                                  |
| ------------------ | -------- | ------------------------------------------------------------ |
| userIDList | Array | 待从黑名单中移除的 userID 列表，单次请求的 userID 数不得超过1000 |

**返回值**

`Promise` 对象。

**示例**

<dx-codeblock>
:::  js

let promise = tim.removeFromBlacklist({userIDList: ['user1', 'user2']}); // 请注意：即使只从黑名单中移除一个用户帐号，也需要用数组类型，例如：userIDList: ['user1']
promise.then(function(imResponse) {
  console.log(imResponse.data); // 从黑名单中成功移除的帐号列表，结构为包含用户 userID 的数组 - [userID]
}).catch(function(imError) {
  console.warn('removeFromBlacklist error:', imError); // 将用户从黑名单中移除失败的相关信息
});

:::
</dx-codeblock>

### 获取黑名单列表

**接口**

<dx-codeblock>
:::  js

tim.getBlacklist();

:::
</dx-codeblock>

**参数**

无

**返回值**

`Promise` 对象。

**示例**

<dx-codeblock>
:::  js

let promise = tim.getBlacklist();
promise.then(function(imResponse) {
  console.log(imResponse.data); // 我的黑名单列表，结构为包含用户 userID 的数组 - [userID]
}).catch(function(imError) {
  console.warn('getBlacklist error:', imError); // 获取黑名单列表失败的相关信息
});

:::
</dx-codeblock>
