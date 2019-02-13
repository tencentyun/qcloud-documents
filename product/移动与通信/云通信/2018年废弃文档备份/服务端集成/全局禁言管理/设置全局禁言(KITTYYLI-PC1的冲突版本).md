## 1 功能说明 

1. 设置账户的单聊消息全局禁言。如果账户被设置单聊消息全局禁言，在单聊消息禁言时间未到期时间内所有的单聊消息发送失败，发送者接收到错误码20012（参见[错误码](/doc/product/269/1671)），不会触发发单聊消息之前回调(参加[发单聊消息之前回调](/doc/product/269/1632))。禁言时间到期后IM云通信后台自动解除单聊消息禁言，解除后所有单聊消息就能发送正常；对于永久全局单聊禁言，全局单聊消息禁言时间一直不过期。帐号默认未设置单聊消息全局禁言。
2. 设置账户的群组消息全局禁言。如果账户被设置群组消息全局禁言，在群组消息禁言时间内所有的群组消息发送失败，发送者接收到错误码10017（参见[错误码](/doc/product/269/1671)），不会触发群内发言之前回调(参加[群内发言之前回调](/doc/product/269/1619))。禁言时间到期后IM通信后台自动解除群组消息禁言，解除后所有群组消息就能发送正常；对于永久全局群组消息禁言，全局群组消息禁言时间一直不过期。帐号默认未设置群组消息全局禁言。


## 2 接口调用说明 

### 2.1 请求URL 
```
https://console.tim.qq.com/v4/openconfigsvr/setnospeaking?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```
### 2.2 请求参数 

URL中各参数的含义以及填写方式参见[REST API简介](/doc/product/269/REST API简介)。 

### 2.3 最高调用频率 

100次/秒。如需提升调用频率，请根据[工单模板](/doc/product/269/云通信配置变更需求工单#2.15-rest-api.E8.B0.83.E7.94.A8.E9.A2.91.E7.8E.87.E8.B0.83.E6.95.B4)提交工单申请处理。

### 2.4 HTTP请求方式 

POST 

### 2.5 HTTP请求包体格式 

JSON 

### 2.6 请求包示例 

```
{
    "Set_Account": "lumotuwe", 
    "C2CmsgNospeakingTime": 4294967295, //C2CmsgNospeakingTime和GroupmsgNospeakingTime是选填字段，但不能两个都不填
    "GroupmsgNospeakingTime": 7200
}
```



### 2.7 请求包字段说明 

| 字段 | 类型 |属性 |说明 |
|---------|---------|---------|---------|---------|
| Set_Account | String |必填 |设置禁言配置的帐号。  |
| C2CmsgNospeakingTime | Number |选填| 单聊消息禁言时间，秒为单位，非负整数，最大值为4294967295(十六进制0xFFFFFFFF)。等于0代表取消账户禁言；等于最大值4294967295(十六进制0xFFFFFFFF)代表账户永久被设置禁言；其它代表该账户禁言时间。  |
| GroupmsgNospeakingTime | Number | 选填|群组消息禁言时间，秒为单位，非负整数，最大值为4294967295(十六进制0xFFFFFFFF)。0代表取消帐号禁言；最大值4294967295(0xFFFFFFFF)代表账户永久禁言；其它代表该账户禁言时间。  |

### 2.8 应答包体示例 

```
{
    "ErrorCode": 0, 
    "ErrorInfo": "", 
}
```

### 2.9 应答包字段说明 

| 字段 | 类型  |说明 |
|---------|---------|---------|
| ErrorCode | Number | 请求错误码。  |
| ErrorInfo | String | 错误相关信息。  |


### 3 错误码说明 

除非发生网络错误(例如502错误),该接口的HTTP返回码均为200。真正的错误码、错误信息是通过应答包体中的ErrorCode、ErrorInfo来表示的。 
公共错误码（60000到79999）参见[公共错误码](/doc/product/269/错误码)。 
本API私有错误码如下： 

| 错误码 |含义说明 | 
|---------|---------|
| 130001 |Json格式解析失败,请检查请求包是否符合JSON规范。| 
| 130004 |Json格式请求包中没有Set_Account字段。|
| 130005 |Json格式请求包中没有Set_Account字段不是String类型。| 
| 130006 |Json格式请求包中C2CmsgNospeakingTime不是String类型。| 
| 130007 |Json格式请求包中GroupmsgNospeakingTime不是String类型。| 
| 130008 |Json格式请求包中GroupmsgNospeakingTime和C2CmsgNospeakingTime这两个字段都没有填写。| 
## 4 接口调试工具 

### 4.1 Web调试工具 

通过[REST API在线调试工具](https://avc.qcloud.com/im/APITester/APITester.html#v4/openconfigsvr/setnospeaking)调试本接口。 

### 4.2 Server调试工具 

无。

更多调试工具参见[REST API调试工具](/doc/product/269/REST API简介#5-rest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7)。 

## 5 API集成 

无。


## 6 参考 
查询全局禁言（[v4/openconfigsvr/setnospeaking](/doc/product/269/4229)）.


