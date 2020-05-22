本文将指导您使用云接入+云函数托管 Node.js 服务端程序。

## 准备工作
准备一个基础项目目录，详细可参考 [快速开始](https://cloud.tencent.com/document/product/876/41774)。

## 创建简单的 Hello World
在工作目录下执行以下命令，创建一个最简单的 Node.js Server：
```sh
$ mkdir functions/server && touch functions/server/index.js && touch functions/server/package.json
```

`functions/server/index.js` 的内容如下：
```
// functions/server/index.js
const serverless = require('serverless-http');

exports.main = serverless((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World\n');
});
```

>?此处使用了 [serverless-http](https://github.com/dougmoscrop/serverless-http)，把 [集成请求](https://cloud.tencent.com/document/product/876/41776#xiangying) 转化为 Node.js Server 能接收的 [IncommingMessage](https://nodejs.org/dist/latest-v13.x/docs/api/http.html#http_class_http_incomingmessage)，同时把返回的 [ServerResponse](https://nodejs.org/dist/latest-v13.x/docs/api/http.html#http_class_http_serverresponse) 转化为集成请求。


`functions/server/package.json` 的内容如下：
```
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
$ cloudbase functions:deploy server
```
创建路由：
```sh
$ cloudbase service:create -p /server -f server
```
随后便可以通过 `https://${env}.service.tcloudbase.com/server` 访问到 Node.js Server（env 是您的环境 ID）：
```
$ curl https://${env}.service.tcloudbase.com/server
Hello World

```
