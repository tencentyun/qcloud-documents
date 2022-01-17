## 调用应用端 API

H5 SDK 对应用端 API 的调用过程进行了封装，发送请求时会自动带上公共参数 `AccessToken` 与 `RequestId`

**接口定义**

```typescript
sdk.requestTokenApi(action, data, options) => Promise
```

**参数说明**

| 参数名  | 参数描述                                                     | 类型   | 必填 |
| ------- | ------------------------------------------------------------ | ------ | ---- |
| action  | 具体应用端 API Action 名称，如：`AppGetDeviceStatuses`       | string | 是   |
| data    | 接口调用参数                                                 | object | 否   |
| options | 请参见 [wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html) | object | 否   |

**返回值**

- 请求成功（code=0）

  返回一个 resolved 的 Promise，其值为应用端 API 响应中的 `Response` 部分数据。

- 请求失败

  返回一个 rejected 的 Promise，其值的数据结构为：`{ code, msg, ...detail }`

