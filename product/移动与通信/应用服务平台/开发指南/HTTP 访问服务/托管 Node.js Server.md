使用 HTTP 访问 + 云函数，可以很轻松地托管 Node.js 服务端程序。

## 准备工作

1. 准备一个基础项目目录，参考 [快速开始 - 初始化目录](https://cloud.tencent.com/document/product/876/41774#.E5.88.9D.E5.A7.8B.E5.8C.96.E7.9B.AE.E5.BD.95)

## 创建简单的 Hello World

我们在工作目录下执行以下命令，创建一个最简单的 Node.js Server：

```sh
mkdir functions/server && touch functions/server/index.js && touch functions/server/package.json
```

`functions/server/index.js` 的内容如下：

```js
// functions/server/index.js
const serverless = require("serverless-http");

exports.main = serverless((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.end("Hello World\n");
});
```

>? 我们此处使用了 [serverless-http](https://github.com/dougmoscrop/serverless-http)，把[集成请求](https://cloud.tencent.com/document/product/876/41776#.E4.BA.91.E5.87.BD.E6.95.B0.E7.9A.84.E5.85.A5.E5.8F.82)转化为 Node.js Server 能接收的 [IncommingMessage](https://nodejs.org/dist/latest-v13.x/docs/api/http.html#http_class_http_incomingmessage)，同时把返回的 [ServerResponse](https://nodejs.org/dist/latest-v13.x/docs/api/http.html#http_class_http_serverresponse) 转化为[集成请求](https://cloud.tencent.com/document/product/876/41776#.E8.BF.94.E5.9B.9E.E9.9B.86.E6.88.90.E5.93.8D.E5.BA.94)

`functions/server/package.json` 的内容如下：

```json
{
  "name": "my-serverless-server",
  "version": "1.0.0",
  "main": "index.js",
  "dependencies": {
    "serverless-http": "^2.3.0"
  }
}
```

## 发布

发布云函数：

```sh
cloudbase functions:deploy server
```

创建路由：

```sh
cloudbase service:create -p /server -f server
```

随后便可以通过 `https://${env}.service.tcloudbase.com/server` 访问到 Node.js Server：

```sh
curl https://${env}.service.tcloudbase.com/server
Hello World
```

