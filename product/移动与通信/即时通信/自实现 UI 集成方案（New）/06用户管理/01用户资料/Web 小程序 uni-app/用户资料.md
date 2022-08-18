## 功能描述

用户可以设置和获取个人的昵称、头像、签名等资料信息，也可以获取到陌生人的资料信息。

## 用户资料管理

### 查询自己的资料

**接口**

<dx-codeblock>
:::  js

tim.getMyProfile();

:::
</dx-codeblock>

**参数**

无

**返回值**

`Promise` 对象。

**示例**

<dx-codeblock>
:::  js

let promise = tim.getMyProfile();
promise.then(function(imResponse) {
  console.log(imResponse.data); // 个人资料 - Profile 实例
}).catch(function(imError) {
  console.warn('getMyProfile error:', imError); // 获取个人资料失败的相关信息
});

:::
</dx-codeblock>

### 查询其他用户资料

>!
>- 如果您没有配置自定义资料字段，或者配置了自定义资料字段，但是没有设置 value，此接口将不会返回自定义资料的内容。
>- 每次拉取的用户数不超过100，避免因回包数据量太大导致回包失败。如果传入的数组长度大于100，则只取前100个用户进行查询，其余丢弃。

**接口**

<dx-codeblock>
:::  js

tim.getUserProfile(options);

:::
</dx-codeblock>

**参数**

参数 options 为 Object 类型，包含的属性值如下：

| Name               | Type     | Description                                                  |
| ------------------ | -------- | ------------------------------------------------------------ |
| userIDList     | Array | 		用户的帐号列表，类型为数组 |

**返回值**

`Promise` 对象。

**示例**

<dx-codeblock>
:::  js

let promise = tim.getUserProfile({
  userIDList: ['user1', 'user2'] // 请注意：即使只拉取一个用户的资料，也需要用数组类型，例如：userIDList: ['user1']
});
promise.then(function(imResponse) {
  console.log(imResponse.data); // 存储用户资料的数组 - [Profile]
}).catch(function(imError) {
  console.warn('getUserProfile error:', imError); // 获取其他用户资料失败的相关信息
});

:::
</dx-codeblock>

### 更新个人资料

**接口**

<dx-codeblock>
:::  js

tim.updateMyProfile(options);

:::
</dx-codeblock>

**参数**

参数 options 为 Object 类型，包含的属性值如下：

| Name               | Type     | Description                                                  |
| ------------------ | -------- | ------------------------------------------------------------ |
| nick     | String \| undefined | 		昵称 |
| avatar | String \| undefined | 头像地址 |
| gender | String \| undefined | 性别：<br/><li>TIM.TYPES.GENDER_UNKNOWN（未设置性别）</li><li>TIM.TYPES.GENDER_FEMALE（女）</li><li>TIM.TYPES.GENDER_MALE（男）</li> |
| selfSignature | String \| undefined | 个性签名 |
| allowType | String \| undefined | 当被加人加好友时：<br/><li>TIM.TYPES.ALLOW_TYPE_ALLOW_ANY（允许直接加为好友）</li><li>TIM.TYPES.ALLOW_TYPE_NEED_CONFIRM（需要验证）</li><li>TIM.TYPES.ALLOW_TYPE_DENY_ANY（拒绝）</li> |
| birthday | Number \| undefined | 生日，推荐用法：20000101 |
| location | String \| undefined | 所在地 推荐用法：App 本地定义一套数字到地名的映射关系 后台实际保存的是4个 uint32_t 类型的数字： 其中第一个 uint32_t 表示国家； 第二个 uint32_t 用于表示省份； 第三个 uint32_t 用于表示城市； 第四个 uint32_t 用于表示区县 |
| language | Number \| undefined | 语言 |
| messageSettings | Number \| undefined | 消息设置，0：接收消息，1：不接收消息 |
| adminForbidType | String \| undefined | 管理员禁止加好友标识：<br/><li>TIM.TYPES.FORBID_TYPE_NONE（默认值，允许加好友）</li><li>TIM.TYPES.FORBID_TYPE_SEND_OUT（禁止该用户发起加好友请求）</li> |
| level | Number \| undefined | 等级，建议拆分以保存多种角色的等级信息 |
| role | Number \| undefined | 角色，建议拆分以保存多种角色信息 |
| profileCustomField | Array \| undefined | 自定义资料键值对集合，可根据业务侧需要使用，详细请参考: https://cloud.tencent.com/document/product/269/1500#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5 |

**返回值**

`Promise` 对象。

**示例**

<dx-codeblock>
:::  js

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

:::
</dx-codeblock>

<dx-codeblock>
:::  js

// 修改个人自定义资料
// 自定义资料字段需要预先在控制台配置，详细请参考：https://cloud.tencent.com/document/product/269/1500#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5
let promise = tim.updateMyProfile({
  // 这里要求您已在即时通信 IM 控制台>【应用配置】>【功能配置】 申请了自定义资料字段 Tag_Profile_Custom_Test1
  // 注意！即使只有一个自定义资料字段，profileCustomField 也需要用数组类型
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

:::
</dx-codeblock>

<dx-codeblock>
:::  js

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

:::
</dx-codeblock>