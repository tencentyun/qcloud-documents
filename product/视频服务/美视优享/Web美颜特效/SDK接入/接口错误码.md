
## SDK 内置接口错误码
如：`https://webar.qcloud.com/sdk/verify` 等 `webar.qcloud.com/sdk/xxx` 接口的错误码。
Response 返回结构：

```js
{
    "Code": xxx,
    "Message": "xxx"
}
```


### 成功 
 Code 为 0 表示成功，如果有数据，Data 会有相应数据：

```json
{
    Code: 0,
    Data:{...}
}
```


### 鉴权错误
 Code在 100 -- 104 是鉴权错误，response Status 为 401：
```json
{
  "100":{
    zh: "缺少鉴权参数"
  },
  "101":{
    zh: "signature 超时"
  },
  "102":{
    zh: "未找到此用户"
  },
  "103":{
    zh: "signature 错误"
  },
  "104":{
    zh: "referer 或者 WeChatAppId 不匹配"
  }
}
 

```

### 入参错误
Code = -2 是入参校验错误，Message 会有相应的说明：

```json

{
    "Code": -2,
    "Message": "LicenseKey字段必须是字符串"
}
```

### 业务校验错误
Code > 1000 的是业务校验错误，Message 会有相应说明：

```json
{
    "Code": 2007,
    "Message": "此项目不存在"
}
```

### 未知错误
Code = -1 是未知错误：
```json
{
    "Code": -1,
    "Message": "未知错误"
}
```
