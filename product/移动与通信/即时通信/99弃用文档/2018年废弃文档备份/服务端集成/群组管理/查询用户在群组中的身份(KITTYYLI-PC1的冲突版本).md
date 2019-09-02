## 1 功能说明 
1. APP管理员可以通过该接口获取一批用户在群内的身份。 
 
## 2 接口调用说明

### 2.1 适用的群组类型

云通信中内置了私有群、公开群、聊天室、互动直播聊天室和在线成员广播大群五种群组类型，详情请见[群组形态介绍](/doc/product/269/群组系统#2-.E7.BE.A4.E7.BB.84.E5.BD.A2.E6.80.81.E4.BB.8B.E7.BB.8D)，其中：
1. 私有群、公开群和聊天室支持使用本REST API查询用户在群组中的身份；
2. 互动直播聊天室不支持使用该REST API查询用户在群组中的身份，如果对这种群组进行操作将返回10007错误。如果管理员希望达到查询用户身份的效果，可以通过[获取群组成员详细资料](/doc/product/269/获取群组成员详细资料)实现。
3. 在线成员广播大群不支持设置管理员和群主，全部成员都为普通成员。所以也不支持使用该REST API查询用户在群组中的身份。

### 2.2 请求URL 
```
https://console.tim.qq.com/v4/group_open_http_svc/get_role_in_group?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json 
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

用来获取用户加入的群组，群组信息包含群ID和需要查询身份的群成员ID。 
```
{
    "GroupId": "@TGS#2C5SZEAEF",
    "User_Account": [  // 最多支持500个
        "leckie",
        "peter",
        "wesley"
    ]
}
```

### 2.8 请求包字段说明 

| 字段 | 类型 | 属性 | 说明 |
|---------|---------|---------|---------|
| GroupId | String | 必填 |需要查询的群组ID。   |
| User_Account | Array | 必填 |表示需要查询的用户账号，最多支持500个账号。  |

### 2.9 应答包体示例

```
{
    "ActionStatus": "OK",
    "ErrorInfo": "",
    "ErrorCode": 0,
    "UserIdList": [  // 结果
        {
            "Member_Account": "leckie",
            "Role": "Owner"  // 身份：Owner/Admin/Member/NotMember
        },
        {
            "Member_Account": "peter",
            "Role": "Member"
        },
        {
            "Member_Account": "wesley",
            "Role": "NotMember"
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
| UserIdList | Array | 拉取到的成员在群内的身份信息，可能的身份包括Owner/Admin/Member/NotMember。    |

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

通过[REST API在线调试工具](https://avc.cloud.tencent.com/im/APITester/APITester.html#v4/group_open_http_svc/get_role_in_group)调试本接口。 

### 3.2 Server调试工具 

可以通过[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK)中的调试工具进行简单的REST API调试，命令如下： 
```
# 获取用户所加入的所有群组
./TimRestApiGear.php group_open_http_svc get_joined_group_list (account_id)
```
更多调试工具参见[REST API调试工具](/doc/product/269/REST%20API简介#5-rest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7)。

## 4 API集成 

### 4.1 PHP集成 

在云通信[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK#3-timrestapigear.php.E4.BD.BF.E7.94.A8.E8.AF.B4.E6.98.8E)中，可以通过TimRestInterface的如下成员函数快速集成该API： 
```
// 查询用户在某个群组中的身份
abstract function group_get_role_in_group($group_id, $member_id);
```

## 5 可能触发的回调 

无。  

## 6 参考 

无。

