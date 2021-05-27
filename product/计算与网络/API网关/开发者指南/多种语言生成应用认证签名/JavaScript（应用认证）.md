## 操作场景

该任务指导您使用 JavaScript 语言，通过应用认证来对您的 API 进行认证管理。

## 操作步骤

1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，创建一个 API，选择鉴权类型为“应用认证”（参考 [创建 API 概述](https://cloud.tencent.com/document/product/628/11795)）。
2. 将 API 所在服务发布至发布环境（参考 [服务发布与下线](https://cloud.tencent.com/document/product/628/11809)）。
3. 在控制台 [应用管理](https://console.cloud.tencent.com/apigateway/app) 界面创建应用。
4. 在应用列表中选中已经创建好的应用，单击【绑定API】，选择服务和 API 后单击【提交】，即可将应用与 API 建立绑定关系。
5. 参考 [示例代码](#示例代码)，使用 JavaScript 语言生成签名内容。

## 环境依赖

API 网关提供 JSON 请求方式和 form 请求方式的示例代码，请您根据自己业务的实际情况合理选择。

## 注意事项

- 应用生命周期管理，以及 API 向应用授权、应用绑定 API 等操作请您参考 [应用管理](https://cloud.tencent.com/document/product/628/55087)。
- 应用生成签名过程请您参考 [应用认证方式](https://cloud.tencent.com/document/product/628/55088)。

## 示例代码[](id:示例代码)

### JSON 请求方式示例代码

<dx-codeblock>
:::  JavaScript
const https = require('https')
const crypto = require('crypto')

// 应用 ApiAppKey
const apiAppKey = 'APIDLIA6tMfqsinsadaaaaaaaapHLkQ1z0kO5n5P'
// 应用 ApiAppSecret
const apiAppSecret = 'Dc44ACV2Da3Gm9JVaaaaaaaaumYRI4CZfVG8Qiuv'

const dateTime = new Date().toUTCString()
const body = {
  arg1: 'a',
  arg2: 'b',
}
const md5 = crypto.createHash('md5').update(JSON.stringify(body), 'utf8').digest('hex')
const contentMD5 = Buffer.from(md5).toString('base64')
const options = {
  hostname: 'service-xxxxxxxx-1234567890.gz.apigw.tencentcs.com',
  port: 443,
  path: '/data',
  method: 'POST',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
    'Content-MD5': contentMD5,
    'Content-Length': JSON.stringify(body).length,
    'x-date': dateTime,
  },
}

const signingStr = [
  `x-date: ${dateTime}`,
  options.method,
  options.headers.Accept,
  options.headers['Content-Type'],
  contentMD5,
  options.path,
].join('\n')
const signing = crypto.createHmac('sha1', apiAppSecret).update(signingStr, 'utf8').digest('base64')
const sign = `hmac id="${apiAppKey}", algorithm="hmac-sha1", headers="x-date", signature="${signing}"`
options.headers.Authorization = sign

const req = https.request(options, (res) => {
  console.log(`STATUS: ${res.statusCode}`)
  res.on('data', (chunk) => {
    console.log('BODY: ' + chunk)
  })
})
req.on('error', (error) => {
  console.error(error)
})
req.write(JSON.stringify(body))
req.end()
:::
</dx-codeblock>



### form 请求方式示例代码

<dx-codeblock>
:::  JavaScript
const https = require('https')
const crypto = require('crypto')
const querystring = require('querystring')

// 应用 ApiAppKey
const apiAppKey = 'APIDLIA6tMfqsinsadaaaaaaaapHLkQ1z0kO5n5P'
// 应用 ApiAppSecret
const apiAppSecret = 'Dc44ACV2Da3Gm9JVaaaaaaaaumYRI4CZfVG8Qiuv'

const dateTime = new Date().toUTCString()
const body = {
  arg1: 'a',
  arg2: 'b',
}
const contentMD5 = ''
const options = {
  hostname: 'service-xxxxxxxx-1234567890.gz.apigw.tencentcs.com',
  port: 443,
  path: '/data',
  method: 'POST',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    'x-date': dateTime,
  },
}

const sorted_body = sortBody(body)
const signingStr = buildSignStr(sorted_body)
const signing = crypto.createHmac('sha1', apiAppSecret).update(signingStr, 'utf8').digest('base64')
const sign = `hmac id="${apiAppKey}", algorithm="hmac-sha1", headers="x-date", signature="${signing}"`

options.headers.Authorization = sign

// 发送请求
const req = https.request(options, (res) => {
  console.log(`STATUS: ${res.statusCode}`)
  res.on('data', (chunk) => {
    console.log('BODY: ' + chunk)
  })
})
req.on('error', (error) => {
  console.error(error)
})
req.write(querystring.stringify(body))
req.end()

function sortBody(body) {
  const keys = Object.keys(body).sort()
  let signKeys = []
  for (let i = 0; i < keys.length; i++) {
    signKeys.push(keys[i])
  }
  // 按字典序排序
  return signKeys.sort()
}

function buildSignStr(sorted_body) {
  const keyStr = sorted_body
    .map((item) => {
      return `${item}=${body[item]}`
    })
    .join('&')
  return [
    `x-date: ${dateTime}`,
    options.method,
    options.headers.Accept,
    options.headers['Content-Type'],
    contentMD5,
    options.path + '?' + keyStr,
  ].join('\n')
}
:::
</dx-codeblock>

