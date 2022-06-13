## 获取群成员资料

>! 每次查询的用户数上限是50。如果传入的数组长度大于50，则只取前50个用户进行查询，其余丢弃。

**接口**

<dx-codeblock>
:::  js

tim.getGroupMemberProfile(options);

:::
</dx-codeblock>

**参数**

参数 options 为 Object 类型，包含的属性值如下：

| Name               | Type     | Description                                                  |
| ------------------ | -------- | ------------------------------------------------------------ |
| groupID     | String | 		群组 ID |
| userIDList | Array | 要查询的群成员用户 ID 列表 |
| memberCustomFieldFilter | Array \| undefined | 群成员自定义字段筛选。可选，若不填，则默认查询所有群成员自定义字段。 |

**返回值**

`Promise` 对象。

**示例**

<dx-codeblock>
:::  js

let promise = tim.getGroupMemberProfile({
  groupID: 'group1',
  userIDList: ['user1', 'user2'], // 请注意：即使只拉取一个群成员的资料，也需要用数组类型，例如：userIDList: ['user1']
  memberCustomFieldFilter: ['group_member_custom'], // 筛选群成员自定义字段：group_member_custom
});
promise.then(function(imResponse) {
  console.log(imResponse.data.memberList); // 群成员列表
}).catch(function(imError) {
  console.warn('getGroupMemberProfile error:', imError);
});

:::
</dx-codeblock>

## 设置群成员名片

>! 直播群不存储群成员信息，所以此接口不适用于直播群。

**接口**

<dx-codeblock>
:::  js

tim.setGroupMemberNameCard(options);

:::
</dx-codeblock>

**参数**

参数 options 为 Object 类型，包含的属性值如下：

| Name               | Type     | Description                                                  |
| ------------------ | -------- | ------------------------------------------------------------ |
| groupID     | String | 		群组 ID 或 话题 ID |
| userID | String \| undefined | 可选，默认修改自身的群名片 |
| nameCard | String | 群成员名片 |

**返回值**

`Promise` 对象。

**示例**

<dx-codeblock>
:::  js

let promise = tim.setGroupMemberNameCard({ groupID: 'group1', userID: 'user1', nameCard: '用户名片' });
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 设置后的群资料
  console.log(imResponse.data.member); // 修改后的群成员资料
}).catch(function(imError) {
  console.warn('setGroupMemberNameCard error:', imError); // 设置群成员名片失败的相关信息
});

:::
</dx-codeblock>

## 设置群成员自定义字段

>! 普通群成员只能设置自己的自定义字段。

**接口**

<dx-codeblock>
:::  js

tim.setGroupMemberCustomField(options);

:::
</dx-codeblock>

**参数**

参数 options 为 Object 类型，包含的属性值如下：

| Name               | Type     | Description                                                  |
| ------------------ | -------- | ------------------------------------------------------------ |
| groupID     | String | 		群组 ID 或 话题 ID |
| userID | String \| undefined | 可选，不填则修改自己的群成员自定义字段 |
| memberCustomField | Array | 群成员自定义字段。数组元素的结构如下：<br/><li>key --- String --- 自定义字段的 Key</li><li>value --- String --- 自定义字段的 Value</li> |

**返回值**

`Promise` 对象。

**示例**

<dx-codeblock>
:::  js

let promise = tim.setGroupMemberCustomField({ groupID: 'group1', memberCustomField: [{key: 'group_member_test', value: 'test'}]});
promise.then(function(imResponse) {
  console.log(imResponse.data.group); // 修改后的群资料
  console.log(imResponse.data.member); // 修改后的群成员资料
}).catch(function(imError) {
  console.warn('setGroupMemberCustomField error:', imError); // 设置群成员自定义字段失败的相关信息
});

:::
</dx-codeblock>


