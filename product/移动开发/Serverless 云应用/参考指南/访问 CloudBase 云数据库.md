本文介绍如何在云托管中访问云开发 CloudBase 的数据库服务。

例如，您可以在 Node.js 中，使用 [CloudBase Node.js SDK](https://docs.cloudbase.net/api-reference/server/node-sdk/introduction.html) 调用 CloudBase 服务。

```js
const cloudbase = require("@cloudbase/node-sdk");
const app = cloudbase.init({
  env: "xxx"
});

const db = app.database();

db.collection("todos")
  .get()
  .then((result) => {
    console.log(result);
  });
```

>? 
> CloudBase 服务端 SDK 已经与云托管进行集成，无需手工填入密钥即可使用。

## 步骤 1：初始化 SDK

```js
const cloudbase = require("@cloudbase/node-sdk");
const app = cloudbase.init({
  env: "xxx"
});
```

## 步骤 2：调用云数据库

```js
const db = app.database();
db.collection("todos")
  .get()
  .then((result) => {
    console.log(result);
  });
```

## 参考文档

更多信息请参见 [Node.js SDK](https://docs.cloudbase.net/api-reference/server/node-sdk/introduction.html) 文档。
