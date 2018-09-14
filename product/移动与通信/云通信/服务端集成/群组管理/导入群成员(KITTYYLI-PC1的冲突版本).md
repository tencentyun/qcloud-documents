## 1 功能说明 
1. 该API接口的作用是导入群组成员，不会触发回调、不会下发通知。
2. 当APP需要从其他即时通信系统迁移到云通信时，使用该协议导入存量群成员数据。
 
## 2 接口调用说明 

### 2.1 适用的群组类型

云通信中内置了私有群、公开群、聊天室、互动直播聊天室和在线成员广播大群五种群组类型，详情请见[群组形态介绍](/doc/product/269/群组系统#2-.E7.BE.A4.E7.BB.84.E5.BD.A2.E6.80.81.E4.BB.8B.E7.BB.8D)，其中：
1. 私有群、公开群和聊天室支持使用本REST API导入群成员；
2. 互动直播聊天室和在线成员广播大群不支持导入群成员，对这两种类型的群组进行操作时会返回10007错误。因为这两种类型群组所适用的场景一般不需要导入成员，所以没有提供这一功能。

### 2.2 请求URL 
```
https://console.tim.qq.com/v4/group_open_http_svc/import_group_member?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json 
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

用来向群中导入成员，一次请求最多支持添加500个成员； 
使用本接口设置的未读消息数如果大于群当前的消息数，未读消息数会设为群当前的消息总数； 
请保证导入成员的入群时间大于群的创建时间并小于当前时间，否则该成员会导入失败。 
```
{
    "GroupId": "@TGS#2J4SZEAEL",   // 要操作的群组（必填）          
    "MemberList": [  // 一次最多添加500个成员       
    {          
        "Member_Account": "tommy"  // 要添加的群成员ID（必填）
        "Role":"Admin",            // 导入成员的角色，目前只有Admin(可选)
        "JoinTime":1448357837,     // 导入的成员入群时间（选填）
        "UnreadMsgNum":5          // 该成员的未读消息数（选填）

    },        
    {           
        "Member_Account": "jared"  
        "JoinTime":1448357857,
        "UnreadMsgNum":2
    }]
}
```

### 2.8 请求包字段说明 

| 字段 | 类型 | 属性 | 说明 |
|---------|---------|---------|---------|
| GroupId | String | 必填 |操作的群ID。 |
| MemberList | Array | 必填 |待添加的群成员数组。 |
| Member_Account | String | 必填 |待导入的群成员帐号。   |
| Role | String | 选填 |待导入群成员角色。目前只支持填Admin，不填则为普通成员Member。  |
| JoinTime | Integer | 选填 |待导入群成员的入群时间。  |
| UnreadMsgNum | Integer | 选填 |待导入群成员的未读消息计数。  |

### 2.9 应答包体示例

```
{
    "ActionStatus": "OK",   
    "ErrorInfo": "",   
    "ErrorCode": 0,   
    "MemberList": [
    {
         "Member_Account": "tommy",           
         "Result": 1   // 导入结果：0为失败；1为成功；2表示已经是群成员       
    },        
    {          
         "Member_Account": "jared",           
         "Result": 1        
    }]
}
```

### 2.10 应答包字段说明 

| 字段 | 类型 | 说明 |
|---------|---------|---------|
| ActionStatus | String | 请求处理的结果，OK表示处理成功，FAIL表示失败。 |
| ErrorCode | Integer | 错误码。 |
| ErrorInfo | String | 错误信息。 |
| MemberList | Array | 返回添加的群成员结果。   |
| Member_Account | String | 返回的群成员帐号。   |
| Result | Integer | 导入结果：0为失败；1为成功；2表示已经是群成员。   |

### 2.11 错误码说明 

除非发生网络错误（例如502错误），该接口的HTTP返回码均为200。真正的错误码、错误信息是通过应答包体中的ErrorCode、ErrorInfo来表示的。 
公共错误码（60000到79999）参见[REST API公共错误码](/doc/product/269/错误码#rest-api.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 
本API私有错误码如下： 

| 错误码 | 含义说明| 
|---------|---------|
| 10002 | 系统错误，请再次尝试或联系技术客服。  | 
| 10003 | 系统错误，请再次尝试或联系技术客服。  | 
| 10004 | 参数非法。请根据应答包中的ErrorInfo字段，检查必填字段是否填充，或者字段的填充是否满足协议要求。 | 
| 10005 | 请求包体中携带的用户数量过多（超过了 500 个成员），请减少一次请求的用户数量。  | 
| 10007 | 操作权限不足。请确认操作者是否是APP管理员。| 
| 10010 | 群组不存在，或者曾经存在过，但是目前已经被解散。 | 
| 10015 | 群组ID非法，请检查群组ID是否填写正确。  | 
| 10019 | 被添加用户的帐号不存在，请检查用户帐号是否正确。  | 

## 3 接口调试工具 

### 3.1 Web调试工具 

通过[REST API在线调试工具](https://avc.cloud.tencent.com/im/APITester/APITester.html#v4/group_open_http_svc/import_group_member)调试本接口。 

### 3.2 Server调试工具 

无。
更多调试工具参见[REST API调试工具](/doc/product/269/REST%20API简介#5-rest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7)。

## 4 API集成 

### 4.1 PHP集成 

无。

## 5 可能触发的回调 

无。

## 6 参考 

REST API：删除群组成员（[v4/group_open_http_svc/delete_group_member](/doc/product/269/删除群组成员)）。 
