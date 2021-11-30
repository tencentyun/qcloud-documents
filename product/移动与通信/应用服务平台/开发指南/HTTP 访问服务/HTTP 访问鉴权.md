HTTP 访问支持鉴定云开发的用户登录凭证，开发者在开启鉴权之后，可以在 HTTP 头部中加入 `x-cloudbase-credentials: <登录凭证>` 的方式调用云函数。

## 开启 HTTP 访问鉴权

在云开发控制台的 [HTTP 访问服务管理页面](https://console.cloud.tencent.com/tcb/env/access)，左侧的路径列表中，可以为各条路径启动或关闭鉴权：

![](https://main.qcloudimg.com/raw/2e0cbbcb2d1195cf162e4c8907fe8438.png)

>? 开启访问鉴权之后，没有鉴权信息，或者鉴权信息非法的请求，都会请求失败。

## 使用 SDK 获取 HTTP 鉴权头部

以 Web 端 SDK 为例，使用云开发支持的登录方式登录后，可以使用 `Auth.getAuthHeader()` 获取鉴权头部：

```js
const cloudbase = require("@cloudbase/js-sdk");
const app = cloudbase.init({
  env: "xxxx"
});

/**
    执行登录流程，此处省略……
*/

const authHeader = cloudbase.auth().getAuthHeader();
// { 'x-cloudbase-credentials': '<credentials>' }
```

## 在请求中加入鉴权头部

我们使用 [axios](https://www.npmjs.com/package/axios) 向 HTTP 服务的 URL 发起一个 HTTP 请求，其中加入鉴权头部：

```js
const axios = require("axios");
const cloudbase = require("@cloudbase/js-sdk");
const app = cloudbase.init({
  env: "xxxx"
});

/**
    执行登录流程，此处省略……
*/

const authHeader = cloudbase.auth().getAuthHeader();

axios({
  method: "post",
  url: "https://env-id.service.tcloudbase.com/xxxx",
  data: {
    /* ... */
  },
  headers: {
    ...authHeader
  }
}).then((res) => {
  //...
});
```

HTTP 请求示例：

```
POST /aaa/bbb HTTP/1.1
Host: env-id.service.tcloudbase.com
X-Cloudbase-Credentials: <credentials>
<其它头部>: <...>

<传输体...>
```

