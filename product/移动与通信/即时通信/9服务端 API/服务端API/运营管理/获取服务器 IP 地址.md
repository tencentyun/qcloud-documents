## 功能说明
基于安全等考虑，您可能需要获知服务器的 IP 地址列表，以便进行相关限制。App 管理员可以通过该接口获得 SDK、第三方回调所使用到的服务器 IP 地址列表或 IP 网段信息。  
>!此接口仅支持获取中国大陆地区的所有 IM 接入方式的 IP 地址或 IP 网段信息。（如需获取国外 IP 或者指定接入方式 IP，您可 [联系我们](https://cloud.tencent.com/document/product/269/59590) 申请开通该功能，申请后我们将对您的需求进行评估，需求评估合理后您方可使用该功能）。

## 接口调用说明
### 请求 URL 示例
```
https://xxxxxx/v4/ConfigSvc/GetIPList?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json&nettype=0
```
 
### 请求参数说明
 
下表仅列出调用本接口时涉及修改的参数及其说明，更多参数详情请参考 [REST API 简介](https://cloud.tencent.com/document/product/269/1519)。

| 参数               | 说明                                 |
| ------------------ | ------------------------------------ |
| xxxxxx | SDKAppID 所在国家/地区对应的专属域名：<br><li>中国：`console.tim.qq.com`</li><li>新加坡：`adminapisgp.im.qcloud.com`</li><li>首尔： `adminapikr.im.qcloud.com`</li><li>法兰克福：`adminapiger.im.qcloud.com`</li><li>孟买：`adminapiind.im.qcloud.com`</li><li>硅谷：`adminapiusa.im.qcloud.com`</li>|
| v4/ConfigSvc/GetIPList | 请求接口                             |
| sdkappid           | 创建应用时即时通信 IM 控制台分配的 SDKAppID |
| identifier         | 必须为 App 管理员帐号，更多详情请参见 [App 管理员](https://cloud.tencent.com/document/product/269/31999#app-.E7.AE.A1.E7.90.86.E5.91.98)                |
| usersig            | App 管理员帐号生成的签名，具体操作请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)    |
| random             | 请输入随机的32位无符号整数，取值范围0 - 4294967295                 |
|contenttype|请求格式固定值为`json`|
|nettype|请求指定类型的服务器 IP 地址列表：<br><li>nettype=0:所有的服务器 IP 地址列表；<br><li>nettype=1:native SDK 访问的中国地区(包括中国香港)服务器 IP 地址列表；<br><li>nettype=2:native SDK 访问的海外地区服务器地址列表；<br><li>nettype=3:web SDK 访问的中国地区(包括中国香港)服务器 IP 地址列表；<br><li>nettype=4:web SDK  访问的海外地区服务器地址列表；<br><li>nettype=5: IM 回调中国地区(包括中国香港)的出口地址列表；<br><li>nettype=6:IM 回调海外地区的出口地址列表。|

>?针对回调业务，业务服务器需要针对 IM 出口加白，可以根据业务服务器地址归属，通过指定 nettype=5(或6) 来获取 IM 出口地址列表。

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

通过 [REST API 在线调试工具](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/ConfigSvc/GetIPList)调试本接口。
