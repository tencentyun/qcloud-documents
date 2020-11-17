## 1 功能说明 
1. APP管理员可以根据群组ID获取群组中被禁言的用户列表。
 
## 2 接口调用说明 

### 2.1 适用的群组类型

云通信中内置了私有群、公开群、聊天室、互动直播聊天室和在线成员广播大群五种群组类型，详情请见[群组形态介绍](/doc/product/269/群组系统#2-.E7.BE.A4.E7.BB.84.E5.BD.A2.E6.80.81.E4.BB.8B.E7.BB.8D)，其中：

私有群、公开群、聊天室和互动直播聊天室全部支持使用本REST API获取群组被禁言用户列表。而在线成员广播大群不支持设置禁言。

### 2.2 请求URL 
```
https://console.tim.qq.com/v4/group_open_http_svc/get_group_shutted_uin?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json 
```
### 2.3 请求参数 

URL中各参数的含义以及填写方式参见[REST API简介](/doc/product/269/REST API简介)。 

### 2.4 最高调用频率 

100次/秒。如需提升调用频率，请根据[工单模板](/doc/product/269/云通信配置变更需求工单#2.15-rest-api.E8.B0.83.E7.94.A8.E9.A2.91.E7.8E.87.E8.B0.83.E6.95.B4)提交工单申请处理。 

### 2.5 HTTP请求方式 

POST 

### 2.6 HTTP请求包体格式 

JSON 

### 2.7 请求包示例

用来获取群组中被禁言的成员列表，只包含群ID。 
```
{
	 "GroupId":"@TGS#1KGZ2RAEU"
}
```

### 2.8 请求包字段说明 

| 字段 | 类型 | 属性 | 说明 |
|---------|---------|---------|---------|
| GroupId | String | 必填 |需要获取被禁言成员列表的群组ID。  |

### 2.9 应答包体示例

```
{
    "ActionStatus": "OK",
    "ErrorCode": 0,
    "GroupId": "@TGS#2FZNNRAEU",
    "ShuttedUinList": [   //群组中被禁言的用户列表
        {
            "Member_Account": "tommy",  //用户ID
            "ShuttedUntil": 1458115189  //禁言到的时间（使用UTC时间，即世界协调时间）
        },
        {
            "Member_Account": "peter",
            "ShuttedUntil": 1458115189
        }
    ]
}
```

### 2.10 应答包字段说明 

| 字段 | 类型 | 说明 |
|---------|---------|---------|
| ActionStatus | String | 请求处理的结果，OK表示处理成功，FAIL表示失败。 |
| ErrorCode | Integer | 错误码。 |
| ErrorInfo | String | 错误信息。  |
| ShuttedUinList | Array | 返回结果为禁言用户信息数组，内容包括被禁言的成员ID，及其被禁言到的时间（使用UTC时间，即世界协调时间）。 |

### 2.11 错误码说明 

除非发生网络错误（例如502错误），该接口的HTTP返回码均为200。真正的错误码、错误信息是通过应答包体中的ErrorCode、ErrorInfo来表示的。 
公共错误码（60000到79999）参见[REST API公共错误码](/doc/product/269/错误码#rest-api.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 
本API私有错误码如下： 

| 错误码 | 含义说明| 
|---------|---------|
| 10002 | 系统错误，请再次尝试或联系技术客服。  | 
| 10003 | 请求命令非法，请再次尝试或联系技术客服。 | 
| 10004 | 参数非法。请根据应答包中的ErrorInfo字段，检查必填字段是否填充，或者字段的填充是否满足协议要求。 | 
| 10007 | 操作权限不足。请确认操作者是否是APP管理员。 | 
| 10010 | 群组不存在，或者曾经存在过，但是目前已经被解散。 | 
| 10015 | 群组ID非法，请检查群组ID是否填写正确。  | 

## 3 接口调试工具 

### 3.1 Web调试工具 

通过[REST API在线调试工具](https://avc.cloud.tencent.com/im/APITester/APITester.html#v4/group_open_http_svc/get_group_shutted_uin)调试本接口。 

### 3.2 Server调试工具 

无。
更多调试工具参见[REST API调试工具](/doc/product/269/REST%20API%E7%AE%80%E4%BB%8B#5-rest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7)。

## 4 API集成 

### 4.1 PHP集成 

无。

## 5 可能触发的回调 

无。 

## 6 参考 

REST API：批量禁言和取消禁言（[v4/group_open_http_svc/forbid_send_msg](/doc/product/269/批量禁言和取消禁言)）。
