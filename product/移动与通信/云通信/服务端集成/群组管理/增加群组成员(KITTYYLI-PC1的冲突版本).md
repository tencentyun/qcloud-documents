## 1 功能说明 
1. APP管理员可以通过该接口向指定的群中添加新成员。 
 
## 2 接口调用说明 

### 2.1 适用的群组类型

云通信中内置了私有群、公开群、聊天室、互动直播聊天室和在线成员广播大群五种群组类型，详情请见[群组形态介绍](/doc/product/269/群组系统#2-.E7.BE.A4.E7.BB.84.E5.BD.A2.E6.80.81.E4.BB.8B.E7.BB.8D)，其中：
1. 私有群、公开群和聊天室支持使用本REST API增加群成员；
2. 互动直播聊天室和在线成员广播大群不支持增加群成员，对这两种类型的群组进行操作时会返回10007错误。用户加入这两种群组的唯一方式是用户申请加群。

### 2.2 请求URL 
```
https://console.tim.qq.com/v4/group_open_http_svc/add_group_member?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json 
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

#### 2.7.1 基础形式

用来向群中进行邀请加人，一次请求最多支持添加500个成员； 后台默认情况下会给群中所有成员下发加群系统通知（除没有激活的Private类型群组外）。 
```
{
    "GroupId": "@TGS#2J4SZEAEL",   // 要操作的群组（必填）          
    "MemberList": [  // 一次最多添加500个成员       
    {          
        "Member_Account": "tommy"  // 要添加的群成员ID（必填）        
    },        
    {           
        "Member_Account": "jared"       
    }]
}
```

#### 2.7.2 静默加人

当Silence为1时，成员添加成功后，不会给任何人下发系统通知。 
```
{
    "GroupId": "@TGS#2J4SZEAEL",   // 要操作的群组（必填）    
    "Silence": 1,   // 是否静默加人（选填）       
    "MemberList": [  // 一次最多添加500个成员       
    {          
        "Member_Account": "tommy"  // 要添加的群成员ID（必填）        
    },        
    {           
        "Member_Account": "jared"       
    }]
}
```

### 2.8 请求包字段说明 

| 字段 | 类型 | 属性 | 说明 |
|---------|---------|---------|---------|
| GroupId | String | 必填 |操作的群ID。  |
| Silence | Integer | 选填 |是否静默加人。0：非静默加人；1：静默加人。不填该字段默认为0。    |
| MemberList | Array | 必填 |待添加的群成员数组。  |
| Member_Account | String | 必填 |待添加的群成员帐号。  |

### 2.9 应答包体示例

```
{
    "ActionStatus": "OK",   
    "ErrorInfo": "",   
    "ErrorCode": 0,   
    "MemberList": [
    {
         "Member_Account": "tommy",           
         "Result": 1   // 加人结果：0为失败；1为成功；2为已经是群成员       
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
| ErrorInfo | String | 错误信息。  |
| MemberList | Array | 返回添加的群成员结果。  |
| Member_Account | String | 返回的群成员帐号。 |
| Result | Integer | 加人结果：0-失败；1-成功；2-已经是群成员；3-等待被邀请者确认。 |

### 2.11 错误码说明 

除非发生网络错误（例如502错误），该接口的HTTP返回码均为200。真正的错误码、错误信息是通过应答包体中的ErrorCode、ErrorInfo来表示的。 
公共错误码（60000到79999）参见[REST API公共错误码](/doc/product/269/错误码#rest-api.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 
本API私有错误码如下： 

| 错误码 | 含义说明| 
|---------|---------|
| 10002 | 系统错误，请再次尝试或联系技术客服。  | 
| 10003 | 请求命令非法，请再次尝试或联系技术客服。 | 
| 10004 | 参数非法。请根据应答包中的ErrorInfo字段，检查必填字段是否填充，或者字段的填充是否满足协议要求。 | 
| 10005 |请求包体中携带的用户数量过多（超过了 500 个成员），请减少一次请求的用户数量。 | 
| 10007 | 操作权限不足。请确认操作者是否是APP管理员。 | 
| 10010 | 群组不存在，或者曾经存在过，但是目前已经被解散。 | 
| 10015 | 群组ID非法，请检查群组ID是否填写正确。  | 
| 10016 | 该请求触发了到APP后台的“[拉人入群之前回调](/doc/product/269/拉人入群之前回调)”，云通讯后台根据回调结果拒绝增加该成员。  | 
| 10019 | 被添加用户的帐号不存在，请检查用户帐号是否正确。  | 

## 3 接口调试工具 

### 3.1 Web调试工具 

通过[REST API在线调试工具](https://avc.cloud.tencent.com/im/APITester/APITester.html#v4/group_open_http_svc/add_group_member)调试本接口。 

### 3.2 Server调试工具 

可以通过[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK)中的调试工具进行简单的REST API调试，命令如下： 
```
# 添加群组成员
./TimRestApiGear.php group_open_http_svc add_group_member (group_id) (member_id) (silence)
```
更多调试工具参见[REST API调试工具](/doc/product/269/REST%20API简介#5-rest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7)。

## 4 API集成 

### 4.1 PHP集成 

在云通信[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK#3-timrestapigear.php.E4.BD.BF.E7.94.A8.E8.AF.B4.E6.98.8E)中，可以通过TimRestInterface的如下成员函数快速集成该API： 
```
// 增加群组成员
abstract function group_add_group_member($group_id, $member_id, $silence);
```

## 5 可能触发的回调 

[拉人入群之前回调](/doc/product/269/拉人入群之前回调)；  
[新成员入群之后回调](/doc/product/269/新成员入群之后回调)；
[群组满员之后回调](/doc/product/269/群组满员之后回调)。 


## 6 参考 

REST API：删除群组成员（[v4/group_open_http_svc/delete_group_member](/doc/product/269/删除群组成员)）。 
