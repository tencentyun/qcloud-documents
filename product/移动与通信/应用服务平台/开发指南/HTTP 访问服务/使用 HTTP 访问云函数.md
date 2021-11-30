开发者可以通过 HTTP 调用云函数，并且将云函数的返回值变为 HTTP 响应体。

## 跨域处理

HTTP 访问服务天然支持跨域请求，将域名添加至 **Web 安全域名** 中，此域名下网页便可以跨域访问 HTTP 服务。

## 云函数的入参

使用 HTTP 调用云函数时，HTTP 请求会被转化为特殊的结构体，称之为**集成请求**，结构如下：

```js
{
    path: 'HTTP请求路径，如 /hello',
    httpMethod: 'HTTP请求方法，如 GET',
    headers: {HTTP请求头},
    queryStringParameters: {HTTP请求的Query，键值对形式},
    requestContext: {云开发相关信息},
    body: 'HTTP请求体',
    isBase64Encoded: 'true or false，表示body是否为Base64编码'
}
```

下面是一个示例：

```js
{
    path: '/',
    httpMethod: 'GET',
    headers: {
        'host': 'env-id.service.tcloudbase.com',
        'connection': 'close',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
    },
    requestContext: {
        requestId: 'cdbb96328072184d19d3fcd243e8cc4d',
        envId: 'env-id',
        appId: 123456789,
        uin: 123456789
    },
    isBase64Encoded: false,
    body: ''
}
```


## 云函数的返回值

云函数可以返回 `string`、`object`、`number` 等类型的数据，或者返回 [集成响应](#.E8.BF.94.E5.9B.9E.E9.9B.86.E6.88.90.E5.93.8D.E5.BA.94)，随后返回值会被转化为正常的 HTTP 响应。

### 返回字符串或数字

云函数返回字符串，那么

```js
module.exports.main = async function () {
  return "hello gateway";
};
```

最终 HTTP 响应为：

```
HTTP/1.1 200 OK
date: Mon, 16 Dec 2019 08:35:31 GMT
content-type: text/plain; charset=utf-8
content-length: 13

hello gateway
```

### 返回 Object

返回的 `Object` 会被转换为 JSON，同时 HTTP 响应的 `content-type` 会被设置为 `application/json`）：

```js
module.exports.main = async function () {
  return {
    foo: "bar"
  };
};
```

最终 HTTP 响应为：

```
HTTP/1.1 200 OK
date: Mon, 16 Dec 2019 08:35:31 GMT
content-type: application/json; charset=utf-8
content-length: 13

{"foo":"bar"}
```

### 返回集成响应

云函数可以返回如下这样特殊结构的**集成响应**，来自由地控制响应体：

```json
{
    "isBase64Encoded": true|false,
    "statusCode": httpStatusCode,
    "headers": { "headerName": "headerValue", ... },
    "body": "..."
}
```

#### 使用集成响应返回 HTML

将 `content-type` 设置为 `text/html`，即可在 `body` 中返回 HTML，会被浏览器自动解析：

```js
module.exports.main = async function () {
  return {
    statusCode: 200,
    headers: {
      "content-type": "text/html"
    },
    body: "<h1>Hello</h1>"
  };
};
```

最终 HTTP 响应为：

```
HTTP/1.1 200 OK
date: Mon, 16 Dec 2019 08:35:31 GMT
content-type: text/html; charset=utf-8
content-length: 14

<h1>Hello</h1>
```

#### 使用集成响应返回 JS 文件

将 `content-type` 设置为 `application/javascript`，即可在 `body` 中返回 JavaScript 文件：

```js
module.exports.main = async function () {
  return {
    statusCode: 200,
    headers: {
      "content-type": "application/javascript"
    },
    body: 'console.log("Hello!")'
  };
};
```

最终 HTTP 响应为：

```
HTTP/1.1 200 OK
date: Mon, 16 Dec 2019 08:35:31 GMT
content-type: application/javascript; charset=utf-8
content-length: 21

console.log("Hello!")
```

#### 使用集成响应返回二进制文件

如果返回体是诸如图片、音视频这样的二进制文件，那么可以将 `isBase64Encoded` 设置为 `true`，并且将二进制文件内容转为 Base64 编码的字符串，例如：

```js
module.exports.main = async function () {
  return {
    isBase64Encoded: true,
    statusCode: 200,
    headers: {
      "content-type": "image/png"
    },
    body: "iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAY..."
  };
};
```

最终 HTTP 响应为一张 PNG 图片：

```
HTTP/1.1 200 OK
date: Mon, 16 Dec 2019 08:35:31 GMT
content-type: image/png
content-length: 9897

<binary payload...>
```
