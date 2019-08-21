目前 Cloudbase 支持的登录方式有：

* 微信授权，包括微信公众平台（公众号网页）和开放平台（普通网站应用）的网页授权
* 自定义登录

暂不支持匿名访问，因此请在**初始化资源后即调用登录授权方法**，登录成功后即可调用 Cloudbase 提供的功能性接口。

使用 JS SDK 时，您可以指定身份认证状态如何持久保留，以避免需要用户频繁登录授权。相关选项包括：

* `local`：在显式退出登录之前的30天内保留身份验证状态
* `session`：在窗口关闭时清除身份验证状态
* `none`：在页面重新加载时清除身份验证状态

## 获取登录对象

### 请求参数

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | ---
| persistence | string | 否 | 身份认证状态如何持久保留，有三个选项 `local`、`session` 和 `none`，默认为 `session`。 |

### 示例代码
```js
const tcb = require('tcb-js-sdk');

tcb.init({
  env: 'xxxx-yyy'
});

let auth = tcb.auth({
  persistence: 'local' //用户显式退出或更改密码之前的30天一直有效
})
```

## 微信授权
### 请求参数

| 字段 | 类型 | 必填 | 说明
| --- | --- | --- | ---
| appid | string | 是 | 微信公众平台（或开放平台）应用的 appid。 |
| scope | string | 是 | 网页授权类型，可选值为 `snsapi_base`（公众平台，只获取用户的 openid）、`snsapi_userinfo`（公众平台，获取用户的基本信息）和 `snsapi_login`（开放平台网页授权）。 |

### 示例代码
```javascript
tcb.init({
  env: 'xxxx-yyy'
});

tcb.auth({
  persistence: 'session'
}).weixinAuthProvider({
  appid: 'wx73932328juof23',
  scope: 'snsapi_base'
}).signIn().then(() => {
  // 登录成功
}).catch(err => {
  // 登录失败
})
```

## 自定义登录

CloudBase 允许开发者使用特定的登录凭据 Ticket 对用户进行身份认证。开发者可以使用服务端 SDK 来创建 Ticket，并且将 JWT 传入到 Web 应用内，然后调用 `signInWithTicket()` 获得 CloudBase 的登录态。

### 获取私钥文件

登录腾讯云[云开发控制台](https://console.cloud.tencent.com/tcb)，在[用户管理页面](https://console.cloud.tencent.com/tcb/user)中，点击“登录设置”，然后**生成并下载私钥**：

![云开发下载私钥](https://main.qcloudimg.com/raw/e08751567a86afceda9e3e8536d37c52.png)

### 使用私钥文件

获取私钥文件之后，在服务端 SDK 初始化时，加入私钥文件的路径：

```js
// 开发者的服务端代码
// 初始化示例
const tcb = require('tcb-admin-node');

// 1. 直接使用下载的私钥文件
tcb.init({
  // ...
  env: 'your-env-id',
  credentials: require('/path/to/your/tcb_custom_login.json')
});

// 2. 也可以直接传入私钥的内容
tcb.init({
  // ...
  env: 'your-env-id',
  credentials: {
    private_key_id: 'xxxxxxxxxxxxx',
    private_key: 'xxxxxxxxxxx'
  }
});
```

### 使用服务端 SDK 创建登录凭据 Ticket

服务端 SDK 内置了生成 Ticket 的接口，开发者需要提供一个自定义的 `customUserId` 作为用户的唯一身份标识。Ticket 有效期为 5 分钟，过期则失效。

```js
let customUserId = '123456';

const ticket = tcb.auth().createTicket(customUserId, {
  refresh: 10 * 60 * 1000 // 每十分钟刷新一次登录态， 默认为一小时
});
// 然后把 ticket 发送给 Web 端
```

### Web 端上使用 Ticket 登录

创建 Ticket 之后，开发者应将 Ticket 发送至 Web 端，然后使用 Web SDK 提供的 `signInWithTicket()` 登录 CloudBase：

```js
auth.signInWithTicket(ticket).then(() => {
  // 登录成功
})
```


## 获取用户信息

任何方式登录成功后，可以调用 `getUserInfo` 获得用户的 Cloudbase 身份信息。

### 请求参数
无

### 响应参数

| 字段 | 类型 | 是否必备 | 说明 |
|---------|---------|---------|---------|
| uid | string | 是 | 用户在云开发的唯一ID |
| appid | string | 是 | 微信(开放平台或公众平台)应用appid |
| openid | string | 是 | 当前用户在微信(开放平台或公众平台)应用的openid |
| nickName | string | 否 | 用户昵称 |
| gender | string | 否 | 用户性别，male(男)或female(女) |
| country | string | 否 | 用户所在国家 |
| province | string | 否 | 用户所在省份 |
| city | string | 否 | 用户所在城市 |
| avatarUrl | string | 否 | 用户头像链接 |


### 示例代码
```js
tcb.init({
  env: 'xxxx-yyy'
});

const auth = tcb.auth({
  persistence: 'session'
})
auth
  .weixinAuthProvider({
    appid: 'wx73932328juof23',
    scope: 'snsapi_userinfo'
  })
  // 先登录才能拿到用户信息
  .signIn()
  .then(() => {
    // 获取用户信息
    return auth.getUserInfo()
  })
  .then(userInfo => {
    //...
  })
```

## 登录授权相关事件及钩子函数

### Event: 'loginStateExpire'

当登录态失效时，会触发这个事件，开发者可以在这个事件回调内，尝试重新登录 Cloudbase。

```js
tcb.on('loginStateExpire', () => {
  // 尝试重新登录
  tcb.auth().weixinAuthProvider({
    appid: 'wx73932328juof23',
    scope: 'snsapi_base'
  }).signIn().then(() => {
    // 登录成功
  }).catch(err => {
    // 登录失败
  });
});
```

### Event: 'refreshAccessToken'

JS SDK 会在登录态生效期间，自动刷新和维护短期访问令牌（access token），每次成功刷新时会触发此事件。

对于两种登录态并存（Cloudbase、自身业务登录态）的 Web 应用，这个事件可以用于同步登录态之间的状态。

```js
tcb.on('refreshAccessToken', () => {
  // 此时 Cloudbase 短期访问令牌已经刷新，可以尝试刷新自身业务的登录态
})
```

### Auth.shouldRefreshAccessToken(callback)

`shouldRefreshAccessToken` 接收一个 `callback` 函数，并且会在刷新短期访问令牌前调用此 `callback` 函数，根据返回值决定是否要刷新短期访问令牌。

对于两种登录态并存（Cloudbase、自身业务登录态）的 Web 应用，可以在 `callback` 内判断自身业务登录态是否失效，从而决定是否续期 Cloudbase 的短期访问令牌。

```js
auth.shouldRefreshAccessToken(() => {
  if (/* 自身业务登录态还有效 */) {
    return true;
  } else {
    return false;
  }
});
```
