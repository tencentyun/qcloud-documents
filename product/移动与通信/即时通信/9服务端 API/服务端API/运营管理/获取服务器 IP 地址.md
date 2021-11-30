## 功能说明
基于安全等考虑，您可能需要获知服务器的 IP 地址列表，以便进行相关限制。App 管理员可以通过该接口获得 SDK、第三方回调所使用到的服务器 IP 地址列表或 IP 网段信息。  
>!此接口仅支持获取中国大陆地区的所有 IM 接入方式的 IP 地址或 IP 网段信息。（如需获取国外 IP 或者指定接入方式 IP，您可 [联系我们](https://cloud.tencent.com/document/product/269/59590) 申请开通该功能，申请后我们将对您的需求进行评估，需求评估合理后您方可使用该功能）。

## 接口调用说明
### 请求 URL 示例
```
https://console.tim.qq.com/v4/ConfigSvc/GetIPList?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```
 
### 请求参数说明
 
下表仅列出调用本接口时涉及修改的参数及其说明，更多参数详情请参考 [REST API 简介](https://cloud.tencent.com/document/product/269/1519)。

| 参数               | 说明                                 |
| ------------------ | ------------------------------------ |
| v4/ConfigSvc/GetIPList | 请求接口                             |
| sdkappid           | 创建应用时即时通信 IM 控制台分配的 SDKAppID |
| identifier         | 必须为 App 管理员帐号，更多详情请参见 [App 管理员](https://cloud.tencent.com/document/product/269/31999#app-.E7.AE.A1.E7.90.86.E5.91.98)                |
| usersig            | App 管理员帐号生成的签名，具体操作请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)    |
| random             | 请输入随机的32位无符号整数，取值范围0 - 4294967295                 |


### 最高调用频率
200次/秒。

### 请求包示例

```
{}
```


### 应答包体示例

```
{
    "ActionStatus": "OK",
    "ErrorCode": 0,
    "IPList": [ "127.0.0.2",   "183.192.202.0/25" ]
}
```

### 应答包字段说明

| 字段 | 类型 | 说明 |
|---------|---------|---------|
| IPList | Array | 	服务器 IP 列表 |
| ErrorCode|	Integer	|错误码，0表示成功，非0表示失败 |
| ErrorInfo | String  | 错误信息   |

## 错误码说明
除非发生网络错误（例如502错误），否则该接口的 HTTP 返回码均为200。真正的错误码，错误信息是通过应答包体中的 ErrorCode、ErrorInfo 来表示的。
公共错误码（60000到79999）参见 [错误码](https://cloud.tencent.com/document/product/269/1671) 文档。


## 接口调试工具

通过 [REST API 在线调试工具](https://29294-22989-29805-29810.cdn-go.cn/api-test.html#v4/ConfigSvc/GetIPList)调试本接口。


