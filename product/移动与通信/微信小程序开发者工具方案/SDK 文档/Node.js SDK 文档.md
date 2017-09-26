## 介绍

Wafer 服务端 SDK 是腾讯云为微信小程序开发者提供的快速开发库，SDK 封装了以下功能供小程序开发者快速调用：

- 用户登录与验证
- 信道服务
- 图片上传
- 数据库
- 客服消息

开发者只需要根据文档对 SDK 进行初始化配置，就可以获得以上能力。你还可以直接到[腾讯云小程序控制台](https://console.qcloud.com/la)购买小程序解决方案，可以得到运行本示例所需的资源和服务，其中包括已部署好的相关程序、示例代码及自动下发的 SDK 配置文件。

## 安装

```bash
npm install wafer-node-sdk --save
```
## SDK 初始化配置

### require('qcloud-weapp-server-sdk')(options)

该方法用于初始化 SDK 需要使用的各种配置项，需先于其他 API 调用。

##### 参数

- `appId` - 可选。微信小程序的 App id
- `appSecret` - 可选。微信小程序的 App secret
- `useQcloudLogin` - 必填。是否使用腾讯云代理登录小程序。会话登录需要使用小程序的 App id 和 App secret 来解密用户信息，腾讯云提供使用腾讯云 App id 和 App secret 代理请求微信进行解密。如果该项为 `false`，则需填写微信小程序 App id 和 App secret。默认为 `true`
- `mysql` - 选填。MySQL 配置。不填则使用小程序解决方案分配机器中默认的 MySQL，若使用自行部署的 MySQL 数据库，则需提供一个类型为 `object`  的配置，具体配置项如下：
  - `host` - 必填。MySQL 主机名
  - `user` - 必填。MySQL 用户名
  - `db` - 必填。MySQL 数据库名
  - `pass` - 必填。MySQL 密码，若使用了腾讯云微信小程序解决方案，开发环境下，MySQL 的初始密码为您的微信小程序 appid
  - `port` - 选填。MySQL 端口（默认：3306）
  - `char` - 选填。MySQL 编码
- `cos` - 必填。腾讯云对象存储配置信息，用于上传模块使用。
  - `region` - 必填。COS 的地域
  - `fileBucket` - 必填。COS 的 bucket 名
  - `uploadFolder` - 必填。COS 上传文件夹名
  - `maxSize` - 选填。COS 上传最大大小，默认 5M (单位：M)
  - `field` - 选填。COS 上传是 field 名称，默认为 `file`
- `serverHost` - 必填。当前服务器的 hostname
- `tunnelServerUrl` - 必填。信道服务器地址
- `tunnelSignatureKey` - 必填。信道服务签名密钥
- `qcloudAppId` - 必填。腾讯云 AppId
- `qcloudSecretId` - 必填。腾讯云 SecretId
- `qcloudSecretKey` - 必填。腾讯云 SecretKey
- `wxMessageToken` - 必填。微信客服消息通知 token
- `wxLoginExpires` - 可选。微信登录态有效期，默认 7200 秒（单位：秒）

**如果购买了腾讯云小程序解决方案，配置项中 `serverHost`, `tunnelServerUrl`, `tunnelSignatureKey`, `qcloudAppId`, `qcloudSecretId`, `qcloudSecretKey`, `wxMessageToken` 由腾讯云自动下发到您的服务器上。**

自动下发的 SDK 配置文件地址： `/data/release/sdk.config`

##### 返回值

初始化之后会返回一个 SDK 的实例，提供以下所有的 API。

## 用户登录和校验

#### qcloud.auth.authorization(req)

登录授权接口，该接口会返回登录状态和用户信息，并将用户信息和登录态储存到 MySQL 里

##### 参数

- `req` - `http.IncomingMessage` 实例化对象

##### 返回值

`Promise` 对象，`.then` 中可以得到登录状态和用户信息

##### 返回数据格式

```javascript
{
  loginState: number,  // 1表示登录成功，0表示登录失败
  userinfo: object
}
```

##### 调用示例

```javascript
// express
module.exports = (req, res) => {
  qcloud.auth.authorization(req).then(result => {
    // result : {
    //   loginState: 0  // 1表示登录成功，0表示登录失败
    //   userinfo: { // 用户信息 }
    // }
  })
}
```

#### qcloud.auth.validation(req)

登录态校验接口，该接口会从 MySQL 取出用户信息，校验登录态，返回登录状态和用户信息

##### 参数

- `req` - `http.IncomingMessage` 实例化对象

##### 返回值

`Promise` 对象，`.then` 中可以得到登录状态和用户信息

##### 返回数据格式

```javascript
{
  loginState: number,  // 1表示登录成功，0表示登录失败
  userinfo: object
}
```

##### 调用示例

```javascript
// express
module.exports = (req, res) => {
  qcloud.auth.validation(req).then(result => {
    // result : {
    //   loginState: 0  // 1表示登录成功，0表示登录失败
    //   userinfo: { // 用户信息 }
    // }
  })
}
```

#### qcloud.auth.authorizationMiddleware(ctx[, next])

用户登录的 Koa 中间件，登录信息将会被写进 `ctx.state.$wxInfo`

**参数**

- `ctx` - `Koa Context` Koa 上下文
- `next` 

**调用示例**

```javascript
const { auth: { authorizationMiddleware } } = qcloud

// 颁发登录态
router.get('/login', authorizationMiddleware, ctx => {
  console.log(ctx.state.$wxInfo)
  // {
  //   loginState: 0  // 1表示登录成功，0表示登录失败
  //   userinfo: { // 用户信息 }
  // }
})
```

#### qcloud.auth.validationMiddleware(ctx[, next])

用户登录态校验的 Koa 中间件，登录信息将会被写进 `ctx.state.$wxInfo`

**参数**

- `ctx` - `Koa Context` Koa 上下文
- `next` 

**调用示例**

```javascript
const { auth: { validationMiddleware } } = qcloud

// 校验登录态
router.get('/user', validationMiddleware, ctx => {
  console.log(ctx.state.$wxInfo)
  // {
  //   loginState: 0  // 1表示登录成功，0表示登录失败
  //   userinfo: { // 用户信息 }
  // }
})
```

## 信道服务

#### qcloud.tunnel.getTunnelUrl(req)

获取信道地址接口。调用这个接口需要用户已经登录，请查看客服端示例

**参数**

- `req` - `http.IncomingMessage` 实例化对象

##### 返回值

`Promise` 对象，`.then` 中可以获得信道服务地址

##### 返回数据格式

```javascript
{
  tunnel: {
    tunnelId: string,    // 信道ID
    connectUrl: string   // 信道连接地址
  },
  userinfo: object       // 用户信息
}
```

##### 调用示例

```javascript
// express
module.exports = (req, res) => {
  qcloud.tunnel.getTunnelUrl(req).then(result => {
    // {
    //   tunnel: {
    //     tunnelId: string,    // 信道ID
    //     connectUrl: string   // 信道连接地址
    //   },
    //   userinfo: object       // 用户信息
    // }
    // 你需要在本地维护一个信道 ID 和用户信息的对应关系
  })
}
```

#### qcloud.tunnel.onTunnelMessage(body)

解析请求体获取信道服务 post 过来的信息

**参数**

- `req` - `http.IncomingMessage` 实例化对象

##### 返回值

`Promise` 对象，`.then` 中可以获得信道服务地址

##### 返回数据格式

```javascript
{
  type: string,             // 包类型，有 connect, message, close 三种
  tunnelId: string          // 信道 ID
  content: {
    messageType: string,    // 消息类型
    messageContent: string  // 消息内容
  }
}
```

##### 调用示例

```javascript
// express
module.exports = (req, res) => {
  qcloud.tunnel.onTunnelMessage(req.body).then(packet => {
    // {
    //   type: string,             // 包类型，有 connect, message, close 三种
    //   tunnelId: string          // 信道 ID
    //   content: {
    //     messageType: string,    // 消息类型
    //     messageContent: string  // 消息内容
    //   }
    // }
  })
}
```

#### qcloud.tunnel.broadcast(tunnelIds, messageType, messageContent)

向指定的多个 `tunnelId` 广播信息

**参数**

- `tunnelIds` - 要广播的信道 ID 的列表数组
- `messageType` - 信息类型
- `messageContent` - 信息内容 

**返回数据**

`Promise` 对象

**调用示例**

```javascript
const { tunnel: { broadcast } } = qcloud

tunnel.broadcast(['abcdefghijk'], 'speak', 'hello world')
.then(result => {
    const invalidTunnelIds = result.data && result.data.invalidTunnelIds || []
    // { invalidTunnelIds: [] } // 会返回无效的信道ID
})
```

#### qcloud.tunnel.closeTunnel(tunnelId)

关闭指定的信道

**参数**

- `tunnelId` - 要关闭的信道 ID

**返回数据**

`Promise` 对象

**调用示例**

```javascript
tunnel.closeTunnel('abcdefghijk')
```

## 图片上传

#### qcloud.uploader(req)

图片上传接口，直接从请求中读取图片文件，并上传到指定的 COS 中。完全兼容直接接入微信小程序端的 `wx.upload` 接口。

**参数**

- `req` - `http.IncomingMessage` 实例化对象

**返回数据**

`Promise` 对象

**返回数据格式**

```javascript
{
  imgUrl: string,     // 图片访问地址
  size: number,       // 图片大小
  mimeType: string,   // 图片 MIME 类型
  name: string        // 图片名称
}
```

**调用示例**

```javascript
// express
module.exports = (req, res) => {
  qcloud.uploader(req).then(data => {
    console.log(data)
    // {
    //   imgUrl: 'http://test-121000000.cosgz.myqcloud.com/abcdef.jpg',
    //   size: 1048576,
    //   mimeType: 'image/jpeg',
    //   name: 'abcdef.jpg'
    // }
  })
}
```

## 数据库

由于 SDK 内部使用 [Knex.js](http://knexjs.org/) 连接数据库，SDK 暴露的 MySQL 实例就是 Knex.js 连接实例，具体使用方法可以查看 [Knex.js 文档](http://knexjs.org/)

## 客服消息

#### qcloud.message.checkSignature(signature, timestamp, nonce)

客服消息签名校验接口，具体文档可以参考微信[接入指引](https://mp.weixin.qq.com/debug/wxadoc/dev/api/custommsg/callback_help.html)

**参数**

- `signature` - 请求的 `query` 中的 `signature`
- `timestamp` - 请求的 `query` 中的 `timestamp`
- `nonce` - 请求的 `query` 中的 `nonce`

**返回数据**

`boolean` - 签名是否有效

**调用示例**

```javascript
const { message: { checkSignature } } = qcloud

/**
 * 响应 GET 请求（响应微信配置时的签名检查请求）
 */
router.get('/message', ctx => {
  const { signature, timestamp, nonce, echostr } = ctx.query
  if (checkSignature(signature, timestamp, nonce)) ctx.body = echostr
  else ctx.body = 'ERR_WHEN_CHECK_SIGNATURE'
})

// POST 请求的路由用来接收消息
router.post('/message', (ctx, next) {
    // 检查签名，确认是微信发出的请求
    const { signature, timestamp, nonce } = ctx.query
    if (!checkSignature(signature, timestamp, nonce)) ctx.body = 'ERR_WHEN_CHECK_SIGNATURE'

    /**
     * 解析微信发送过来的请求体
     * 可查看微信文档：https://mp.weixin.qq.com/debug/wxadoc/dev/api/custommsg/receive.html#接收消息和事件
     */
    const body = ctx.request.body

    ctx.body = 'success'
})
```