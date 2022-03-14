## 方法1：使用 Open API 访问 CloudBase

Cloudbase Open API 让开发者可以通过 HTTP 的方式，以管理员身份调用 CloudBase 的各项服务。以云托管中的 Node.js 服务为例：
<dx-codeblock>
:::  js
const express = require("express");
const got = require("got");
const app = express();

app.get("/", async (req, res) => {
  // 从请求头中获取凭证信息
  const authorization = req.headers["x-cloudbase-authorization"];
  const sessiontoken = req.headers["x-cloudbase-sessiontoken"];
  const timestamp = parseInt(Date.now() / 1000).toString();

  // 使用凭证向 CloudBase Open API 发起请求
  // 以查询文档为例，先拼接url
  const envId = "foo";
  const collectionName = "bar";
  const docId = "123";
  const url = `https://tcb-api.tencentcloudapi.com/api/v2/envs/${envId}/databases/${collectionName}/documents/${docId}`;

  // 发起请求，请求头中加入凭证信息
  const response = await got(url, {
    headers: {
      "X-CloudBase-Authorization": authorization,
      "X-CloudBase-TimeStamp": timestamp,
      "X-CloudBase-SessionToken": sessiontoken
    }
  });

  res.send(response.body);
});

app.listen(3000);
:::
</dx-codeblock>


更多详情请参见 [Open API 文档](https://docs.cloudbase.net/api-reference/openapi/introduction.html)。

## 方法2：使用 CloudBase 服务端 SDK

例如，您可以在 Node.js 中，使用 [CloudBase Node.js SDK](https://docs.cloudbase.net/api-reference/server/node-sdk/introduction.html) 调用 CloudBase 服务。
<dx-codeblock>
:::  js
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
:::
</dx-codeblock>

>? CloudBase 服务端 SDK 已经与云托管进行集成，无需手工填入密钥即可使用。

## 参考文档

更多信息请参见 [Node.js SDK](https://docs.cloudbase.net/api-reference/server/node-sdk/introduction.html) 文档。
