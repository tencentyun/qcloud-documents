
腾讯云图支持用户通过自己的 API 提供实时数据，支持**浏览器端发起请求**和**服务器端发起请求**两种。

## 浏览器端发起请求
>!由浏览器端发起的请求为跨域请求，接口的实现需要满足下文的要求。

下图由接口 `http://127.0.0.1:3000/api`举例，文章后面会给出代码。

### 设置数据源
![](https://main.qcloudimg.com/raw/5cd10c18f9e4ce4c98f017fad7fd1ed1.png)

### 接口的实现
返回 HTTP 响应头以支持浏览器端跨域发起请求。
- `Access-Control-Allow-Credentials: true`：勾选**需要 Cookie**，需要返回。
- `Access-Control-Allow-Origin: http://yuntu.cloud.tencent.com`：需要按照 HTTP 请求的协议头 Origin 来源返回，如果请求`https://v.yuntus.com`页面（Origin: `https://v.yuntus.com`），则需要对应返回`Access-Control-Allow-Origin: https://v.yuntus.com`。
![](https://main.qcloudimg.com/raw/165b0e11d9eba0fe5d9084e0c159cbb0.png)

#### 返回数据
返回数据需要满足以下条件：
- JSON 格式。
- 仅包含完整数据（不包含返回码）。

![](https://main.qcloudimg.com/raw/e3d99babe5d85c4346ef9faa0de3a89c.png)
#### 示例代码：
接口`http://127.0.0.1:3000/api`的 NodeJs 示例代码（ 支持 node 8 及以上版本运行）：
```
const express = require('express')
const app = express()
const PORT = 3000
const BAR_DATA_MAX = 120
const CORS_ALLOW_ORIGIN = [
  'http://yuntu.cloud.tencent.com',
  'https://yuntu.cloud.tencent.com',
  'http://v.yuntus.com',
  'https://v.yuntus.com'
]
function randomNumber(max) {
  return parseInt(Math.random() * max, 10)
}
app.get('/api', (req, res, next) => {
  const origin = req.header('origin')
  if (CORS_ALLOW_ORIGIN.includes(origin)) {
    res.header('Access-Control-Allow-Origin', origin)
    res.header('Access-Control-Allow-Credentials', true)
  }
  res.json([
    {
      x: '一月',
      y: randomNumber(BAR_DATA_MAX),
      s: 's1'
    },
    {
      x: '二月',
      y: randomNumber(BAR_DATA_MAX),
      s: 's1'
    },
    {
      x: '三月',
      y: randomNumber(BAR_DATA_MAX),
      s: 's1'
    },
    {
      x: '四月',
      y: randomNumber(BAR_DATA_MAX),
      s: 's1'
    },
    {
      x: '五月',
      y: randomNumber(BAR_DATA_MAX),
      s: 's1'
    }
  ])
})
app.listen(PORT)
```

## 服务器端发起请求
>!接口不支持跨域，需勾选**服务器发起请求**。已勾选**服务器发起请求**时，勾选**需要 Cookie** 无效（无法传递接口域名下的 Cookie）。

由服务器端发起请求，接口响应数据格式与**浏览器端发起请求**一致，但需要接口支持外网访问，即需勾选**服务器发起请求**。
![](https://main.qcloudimg.com/raw/cb53beacb7f6280783cd108e4bb4923f.png)

## 使用访问密钥
如果 API 是公网地址，会导致 API 暴露在公网，下面有两种方法可解决其他人能调用接口查看数据的隐患。
1. 如果是**服务器端发起请求**，可以设置数据代理 IP 白名单。
2. 使用访问密钥，在 API 里实现鉴权。

### 创建密钥
登录 [腾讯云图控制台](http://yuntu.cloud.tencent.com/#/access-key)，单击**新建访问密钥**，新建成功后即可得到 SecretId 和 SecretKey。
![](https://main.qcloudimg.com/raw/43145c939ee0a226ae5712ed7b8fdf8f.png)
### 选择访问密钥
![](https://main.qcloudimg.com/raw/514a8947997b78ffb116f7371236d883.png)
### 计算并比较签名
可以通过浏览器开发工具看到，服务器使用计算出的签名向设置的 API 发起了请求。
![](https://main.qcloudimg.com/raw/6b0f6cda1fc0bafd34211f5205f41b11.png)
上图中请求签名后的 API URL 如下：

```
http://127.0.0.1:3000/api?TcvSecretId=zUYUtjPu2Kob9xxxxxxxxrbkau3FEq6pqxe6&TcvSignature=Ds3cyyhQCo%2FTvdyUi3%2BmuPj2DQKZXMpIRwTqvMXPiRE%3D&TcvTimestamp=1583399912&TcvNonce=302190
```
参数拆分如下：
- TcvSecretId
- TcvTimestamp
- TcvNonce
- TcvSignature

### 计算签名内容
将非 TcvSignature 的参数按照名称升序排列拼接，格式为 key1=value1&key2=value2&key3=value3，这里排序后如下：
```
TcvNonce=302190&TcvSecretId=zUYUtjPu2Kob9xxxxxxxxrbkau3FEq6pqxe6&TcvTimestamp=1583399912
```
### 计算签名
使用 HMAC-SHA256 算法计算签名，NodeJs 的计算代码如下：
```
const signStr='TcvNonce=302190&TcvSecretId=zUYUtjPu2Kob9xxxxxxxxrbkau3FEq6pqxe6&TcvTimestamp=1583399912' // 计算的签名内容
const secretKey = 'xrck1Mgi0IxVjS08B3HsECajxxxxxxxx'// 刚才获取的签名密钥
const signature = crypto.createHmac('sha256', SecretKey).update(signStr).digest().toString('base64’)
// 将 signature 与 TcvSignature 对比，结果一致则确认是来自云图的请求
```
### 示例代码
加上校验签名的完整 NodeJs 示例代码如下（ node 8 及以上版本运行通过）：

```
const express = require('express')
const crypto = require('crypto')
const app = express()
const PORT = 3000
const BAR_DATA_MAX = 120
const CORS_ALLOW_ORIGIN = [
  'http://yuntu.cloud.tencent.com',
  'https://yuntu.cloud.tencent.com',
  'http://v.yuntus.com',
  'https://v.yuntus.com'
]
const secretKey = 'xrck1Mgi0IxVxxxxjO01RYfGW'
function randomNumber(max) {
  return parseInt(Math.random() * max, 10)
}
function isSignatureOK(receivedSignature, query) {
  // TcvSignature 不参与签名
  delete query.TcvSignature
  const params = Object.entries(query)
  // 升序排列字段
  params.sort(([key1], [key2]) => {
    if (key1 > key2) {
      return 1
    }
    if (key1 < key2) {
      return -1
    }
    return 0
  })
  // 生成签名字符串
  const signStr = params.map(kv => kv.join('=')).join('&')
  console.log(signStr)
  // 计算签名
  const signature = crypto.createHmac('sha256', secretKey).update(signStr).digest().toString('base64')
  console.log(`signature=${signature}, receivedSignature=${receivedSignature}`)
  // 比较签名结果是否相同
  return signature === receivedSignature
}
app.get('/api', (req, res, next) => {
  if (!isSignatureOK(req.query.TcvSignature, req.query)) {
    // 签名不同，返回没有权限
    res.status(401).end()
    return
  }
  // 设置响应 CORS 头
  const origin = req.header('origin')
  if (CORS_ALLOW_ORIGIN.includes(origin)) {
    res.header('Access-Control-Allow-Origin', origin)
    res.header('Access-Control-Allow-Credentials', true)
  }
  res.json([
    {
      x: '一月',
      y: randomNumber(BAR_DATA_MAX),
      s: 's1'
    },
    {
      x: '二月',
      y: randomNumber(BAR_DATA_MAX),
      s: 's1'
    },
    {
      x: '三月',
      y: randomNumber(BAR_DATA_MAX),
      s: 's1'
    },
    {
      x: '四月',
      y: randomNumber(BAR_DATA_MAX),
      s: 's1'
    },
    {
      x: '五月',
      y: randomNumber(BAR_DATA_MAX),
      s: 's1'
    }
  ])
})
app.listen(PORT)
```

