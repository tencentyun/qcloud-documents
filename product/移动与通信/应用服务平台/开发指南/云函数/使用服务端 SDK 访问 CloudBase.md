如需在云函数中访问 CloudBase 的各项服务，例如操作数据库、管理云文件等，可使用 CloudBase 服务端 SDK。

例如，您可以在 Node.js 云函数中，使用 [CloudBase Node.js SDK](https://docs.cloudbase.net/api-reference/server/node-sdk/introduction) 调用 CloudBase 服务。

```js
const cloudbase = require("@cloudbase/node-sdk");
const app = cloudbase.init({
  env: cloudbase.SYMBOL_CURRENT_ENV
});

const db = app.database();

exports.main = async (event, context) => {
  return db.collection("todos").get();
};
```

>? CloudBase 服务端 SDK 已经与云函数进行集成，无需手工填入密钥即可使用。

## 初始化 SDK
<dx-codeblock>
::: Node.js
const cloudbase = require("@cloudbase/node-sdk");
const app = cloudbase.init({
  env: cloudbase.SYMBOL_CURRENT_ENV
});
:::
</dx-codeblock>

## 调用云数据库
<dx-codeblock>
::: Node.js
const db = app.database();
exports.main = async (event, context) => {
  return db.collection("todos").get();
};
:::
</dx-codeblock>

## 调用云存储
<dx-codeblock>
::: Node.js
exports.main = async (event, context) => {
  const fileStream = fs.createReadStream(path.join(__dirname, "demo.jpg"));
  return await app.uploadFile({
    cloudPath: "demo.jpg",
    fileContent: fileStream
  });
};
:::
</dx-codeblock>

## 调用其它云函数
<dx-codeblock>
::: Node.js
exports.main = async (event, context) => {
  return await cloud.callFunction({
    name: "sum",
    data: {
      x: 1,
      y: 2
    }
  });
};
:::
</dx-codeblock>

## 获取用户信息

当从客户端调用云函数时，如在小程序中或者 web 端使用微信登录授权，云函数的传入参数中会被注入用户的 `openid`，开发者无需校验 `openid` 的正确性，可以直接使用该 `openid`。与 `openid` 一起注入云函数的还有其它相关的用户身份信息。

<dx-tabs>
::: Node.js
<dx-codeblock>
::: Node.js
//引用SDK
const tcb = require("@cloudbase/node-sdk");
//初始化SDK
const app = tcb.init();
//获取用户信息
const userInfo = await app.auth().getUserInfo();
const {
  openId, //微信openId，非微信授权登录则空
  appId, //微信appId，非微信授权登录则空
  uid, //用户唯一ID
  customUserId //开发者自定义的用户唯一id，非自定义登录则空
} = userInfo;
:::
</dx-codeblock>

:::
::: 小程序·云开发

从小程序端调用云函数时，开发者可以在云函数内使用 [wx-server-sdk](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/guide/functions/wx-server-sdk.html) 提供的 [getWXContext](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/reference-sdk-api/utils/Cloud.getWXContext.html) 方法获取到每次调用的上下文（`appid`、`openid` 等），无需维护复杂的鉴权机制，即可获取可信任的用户登录态（`openid`）。

示例代码
<dx-codeblock>
:::  js
// index.js
const cloud = require("wx-server-sdk");
exports.main = async (event, context) => {
  // 这里获取到的 openId、 appId 和 unionId 是可信的，注意 unionId 仅在满足 unionId 获取条件时返回
  const { OPENID, APPID, UNIONID } = cloud.getWXContext();

  return {
    OPENID,
    APPID,
    UNIONID
  };
};
:::
</dx-codeblock>

:::
</dx-tabs>

## 参考

更多详细信息请参见：

- [Node.js SDK 文档](https://docs.cloudbase.net/api-reference/server/node-sdk/introduction)
- [wx-server-sdk](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/reference-sdk-api/init/server.init.html)
