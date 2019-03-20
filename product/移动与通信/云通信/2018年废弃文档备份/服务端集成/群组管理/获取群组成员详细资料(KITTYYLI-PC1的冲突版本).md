## 1 功能说明 
1. APP管理员可以根据群组ID获取群组成员的资料。 
 
## 2 接口调用说明 

### 2.1 适用的群组类型

云通信中内置了私有群、公开群、聊天室、互动直播聊天室和在线成员广播大群五种群组类型，详情请见[群组形态介绍](/doc/product/269/群组系统#2-.E7.BE.A4.E7.BB.84.E5.BD.A2.E6.80.81.E4.BB.8B.E7.BB.8D)，其中：
1. 私有群、公开群和聊天室支持使用本REST API获取群组成员的详细资料；
2. 因为内部实现的差异，互动直播聊天室只能获取1000人以内的群成员资料，群人数达到1000后加入的群成员的成员资料无法被获取；而在线成员广播大群则无法获取群成员资料。

### 2.2 请求URL 
```
https://console.tim.qq.com/v4/group_open_http_svc/get_group_member_info?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json 
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

用来获取群成员详细信息（群成员资料和群成员维度自定义字段），请求中只包含群ID。 
```
{
    "GroupId":"@TGS#1NVTZEAE4"  // 群组ID（必填）
}
```

#### 2.7.2 分页获取 

可以使用Limit和Offset两个值用于控制分页拉取； 
Limit限制回包中MemberList数组中成员的个数，不得超过10000；
Offset控制从群成员中的第多少个成员开始拉取信息。对于分页请求（页码数字从1开始），每一页的Offset值应当为：`（页码数– 1）×每页展示的群成员数量`； 
例如：假设需要分页拉取，每页展示20个，则第一页的请求参数应当为：`{“Limit” : 20, “Offset” : 0}`，第二页的请求参数应当为`{“Limit” : 20, “Offset” : 20}`，依此类推；
Limit或者Offset的取值不会对应答包体中的TotalCount造成影响。 
```
{
    "GroupId":"@TGS#1NVTZEAE4", // 群组ID（必填）
    "Limit": 100,   // 最多获取多少个成员的资料
    "Offset": 0   // 从第多少个成员开始获取资料
}
```

#### 2.7.3 指定拉取的信息

通过MemberInfoFilter过滤器字段选择需要拉取的字段。没有在过滤器中指明的字段将不被拉取。 
```
{
    "GroupId":"@TGS#1NVTZEAE4", // 群组ID（必填）
    "MemberInfoFilter": [   // 需要获取哪些信息（Member_Account被默认包含在其中），如果没有该字段则为群成员全部资料
        "Role",
        "JoinTime",
        "MsgSeq",
        "MsgFlag",
        "LastSendMsgTime",
        "ShutUpUntil",
        "NameCard"
    ] 
}
```

#### 2.7.4 拉取指定身份成员

通过MemberRoleFilter过滤器字段选择需要拉取资料的成员身份。没有在过滤器中指明则代表拉取任何身份的成员的资料。 
```
{
    "GroupId":"@TGS#37AB3PAEC",  // 群组ID（必填）
    "MemberRoleFilter":[  //群成员身份过滤器
        "Owner",
        "Member"
    ]
}
```

#### 2.7.5 拉取群成员自定义字段

通过AppDefinedDataFilter_GroupMember过滤器选取需要拉取的成员自定义字段。没有在过滤器中指明的字段将不被拉取。
```
{
    "GroupId":"@TGS#37AB3PAEC",  // 群组ID（必填）
    "AppDefinedDataFilter_GroupMember": [  //群成员自定义字段过滤器
        "MemberDefined2"    //群成员自定义字段Key
    ]
}
```

#### 2.7.6 ALL IN ONE

```
{
    "GroupId":"@TGS#1NVTZEAE4",  // 群组ID（必填）
    "MemberInfoFilter": [  // 需要获取哪些信息，如果没有该字段则为群成员全部资料
        "Role",
        "JoinTime",
        "MsgSeq",
        "MsgFlag",
        "LastSendMsgTime",
        "ShutUpUntil",
        "NameCard"
    ],
   "MemberRoleFilter":[  //群成员身份过滤器
        "Owner",
        "Member"
    ],
   "AppDefinedDataFilter_GroupMember": [  //群成员自定义字段过滤器
        "MemberDefined2",    //群成员自定义字段Key
        "MemberDefined1"
    ],
    "Limit": 100,   // 最多获取多少个成员的资料
    "Offset": 0   // 从第多少个成员开始获取
}
```

### 2.8 请求包字段说明 

| 字段 | 类型 | 属性 | 说明 |
|---------|---------|---------|---------|
| GroupId | String | 必填 |需要拉取成员信息的群组的ID。   |
| MemberInfoFilter | Array | 选填 |需要获取哪些信息， 如果没有该字段则为群成员全部资料，成员信息字段详情参见：[群成员资料](/doc/product/269/群组系统#4.2-.E7.BE.A4.E6.88.90.E5.91.98.E8.B5.84.E6.96.99)。 |
| MemberRoleFilter | Array | 选填 |拉取指定身份的群成员资料。如没有填写该字段，默认为所有身份成员资料，成员身份可以为：“Owner”，“Admin”，“Member”。  |
| AppDefinedDataFilter_GroupMember | Array | 选填| 默认情况是没有的。该字段用来群成员维度的自定义字段过滤器，指定需要获取的群成员维度的自定义字段，群成员维度的自定义字段详情参见：[自定义字段](/doc/product/269/群组系统#6-.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)。 |
| Limit | Integer | 选填 |一次最多获取多少个成员的资料，不得超过10000。如果不填，则获取群内全部成员的信息。 |
| Offset | Integer | 选填 |从第几个成员开始获取，如果不填则默认为0，表示从第一个成员开始获取。 |

### 2.9 应答包体示例

#### 2.9.1 基本形式和分页拉取

```
{
    "ActionStatus": "OK", 
    "ErrorInfo": "", 
    "ErrorCode": 0, 
    "MemberNum": 2, // 本群组的群成员总数
    "MemberList": [  // 群成员列表
        {
            "Member_Account": "bob", 
            "Role": "Owner", 
            "JoinTime": 1425976500, // 入群时间
            "MsgSeq": 1233, 
            "MsgFlag": "AcceptAndNotify", 
            "LastSendMsgTime": 1425976500, // 最后一次发消息的时间
            "ShutUpUntil": 1431069882, // 禁言截至时间（秒数）
            "AppMemberDefinedData": [ //群成员自定义字段
                {
                   "Key": "MemberDefined1",
                   "Value": "ModifyDefined1"
                },
                {
                    "Key": "MemberDefined2",
                    "Value": "ModifyDefined2"
                }
             ]
        }, 
        {
            "Member_Account": "peter", 
            "Role": "Member ", 
            "JoinTime": 1425976500, 
            "MsgSeq": 1233, 
            "MsgFlag": "AcceptAndNotify", 
            "LastSendMsgTime": 1425976500,
            "ShutUpUntil": 0, // 0表示未被禁言，否则为禁言的截止时间
            "AppMemberDefinedData": [ //群成员自定义字段
                {
                   "Key": "MemberDefined1",
                   "Value": "ModifyDefined1"
                },
                {
                    "Key": "MemberDefined2",
                    "Value": "ModifyDefined2"
                }
             ]
        }
    ]
}
```

#### 2.9.2 拉取指定字段

```
{
    "ActionStatus": "OK", 
    "ErrorInfo": "", 
    "ErrorCode": 0, 
    "MemberNum": 2, // 本群组的群成员总数
    "MemberList": [  // 群成员列表
        {
            "Member_Account": "bob", 
            "Role": "Owner", 
            "JoinTime": 1425976500, // 入群时间
            "MsgSeq": 1233, 
            "MsgFlag": "AcceptAndNotify", 
            "LastSendMsgTime": 1425976500, // 最后一次发消息的时间
            "ShutUpUntil": 1431069882, // 禁言截至时间（秒数）
        }, 
        {	
            "Member_Account": "peter", 
            "Role": "Member ", 
            "JoinTime": 1425976500, 
            "MsgSeq": 1233, 
            "MsgFlag": "AcceptAndNotify", 
            "LastSendMsgTime": 1425976500,
            "ShutUpUntil": 0, // 0表示未被禁言，否则为禁言的截止时间
        }
    ]
}
```

#### 2.9.3 拉取指定身份成员

```
{
    "ActionStatus": "OK",   //返回成功
    "ErrorCode": 0,   //返回码
    "MemberList": [        
        {   
            "JoinTime": 1450680436, //成员加入时间
            "LastSendMsgTime": 0,   //成员最后发消息时间
            "Member_Account": "Test_1",   //成员帐号
            "MsgFlag": "AcceptNotNotify",  //成员消息屏蔽类型
            "MsgSeq": 1,    //成员已读消息seq
            "NameCard": "",  //成员名片
            "Role": "Owner", // 成员身份
            "ShutUpUntil": 0  // 0表示未被禁言，否则为禁言的截止时间
        },
        {
            "JoinTime": 1450680436,
            "LastSendMsgTime": 0,          
            "Member_Account": "Test_6",           
            "MsgFlag": "AcceptNotNotify",          
            "MsgSeq": 1,        
            "NameCard": "",
            "Role": "Admin",
            "ShutUpUntil": 0
        }
    ],
    "MemberNum": 8    //本群组，群成员总数
}
```

#### 2.9.4 拉取群成员自定义字段

```
{
    "ActionStatus": "OK", 
    "ErrorInfo": "", 
    "ErrorCode": 0, 
    "MemberNum": 2, // 本群组的群成员总数
    "MemberList": [  // 群成员列表
        {
            "Member_Account": "bob", 
            "Role": "Owner", 
            "JoinTime": 1425976500, // 入群时间
            "MsgSeq": 1233, 
            "MsgFlag": "AcceptAndNotify", 
            "LastSendMsgTime": 1425976500, // 最后一次发消息的时间
            "ShutUpUntil": 1431069882, // 禁言截至时间（秒数）
             "AppMemberDefinedData": [ //群成员自定义字段
                {
                    "Key": "MemberDefined2",
                    "Value": "ModifyDefined2"
                }
             ]
        }, 
        {
            "Member_Account": "peter", 
            "Role": "Member", 
            "JoinTime": 1425976500, 
            "MsgSeq": 1233, 
            "MsgFlag": "AcceptAndNotify", 
            "LastSendMsgTime": 1425976500,
            "ShutUpUntil": 0, // 0表示未被禁言，否则为禁言的截止时间
            "AppMemberDefinedData": [ //群成员自定义字段
                {
                    "Key": "MemberDefined2",
                    "Value": "ModifyDefined2"
                }
             ]
        }
    ]
}
```

#### 2.9.5 ALL IN ONE

```
{
    "ActionStatus": "OK", 
    "ErrorInfo": "", 
    "ErrorCode": 0, 
    "MemberNum": 2, // 本群组的群成员总数
    "MemberList": [  // 群成员列表
        {
            "Member_Account": "bob", 
            "Role": "Owner", 
            "JoinTime": 1425976500, // 入群时间
            "MsgSeq": 1233, 
            "MsgFlag": "AcceptAndNotify", 
            "LastSendMsgTime": 1425976500, // 最后一次发消息的时间
            "ShutUpUntil": 1431069882, // 禁言截至时间（秒数）
            "AppMemberDefinedData":[ //群成员自定义字段
                {
                   "Key":"MemberDefined1",
                   "Value":"ModifyDefined1"
                },
                {
                    "Key":"MemberDefined2",
                    "Value":"ModifyDefined2"
                }
             ]
        }, 
        {
            "Member_Account": "peter", 
            "Role": "Member", 
            "JoinTime": 1425976500, 
            "MsgSeq": 1233, 
            "MsgFlag": "AcceptAndNotify", 
            "LastSendMsgTime": 1425976500,
            "ShutUpUntil": 0, // 0表示未被禁言，否则为禁言的截止时间
            "AppMemberDefinedData": [ //群成员自定义字段
                {
                   "Key": "MemberDefined1",
                   "Value": "ModifyDefined1"
                },
                {
                    "Key": "MemberDefined2",
                    "Value": "ModifyDefined2"
                }
             ]
        }
    ]
}
```

### 2.10 应答包字段说明 

| 字段 | 类型 | 说明 |
|---------|---------|---------|
| ActionStatus | String | 请求处理的结果，OK表示处理成功，FAIL表示失败。 |
| ErrorCode | Integer | 错误码。  |
| ErrorInfo | String | 错误信息。  |
| MemberNum | Integer | 本群组的群成员总数。 |
| MemberList | Array | 获取到的群成员列表，其中包含了全部或者指定的群成员信息，成员信息字段详情参见：[群成员资料数据结构](/doc/product/269/1502#4.2-.E7.BE.A4.E6.88.90.E5.91.98.E8.B5.84.E6.96.99)。 |
| AppMemberDefinedData | Array | 返回的群成员自定义字段信息。   |

### 2.11 错误码说明 

除非发生网络错误（例如502错误），该接口的HTTP返回码均为200。真正的错误码、错误信息是通过应答包体中的ErrorCode、ErrorInfo来表示的。 
公共错误码（60000到79999）参见[REST API公共错误码](/doc/product/269/错误码#rest-api.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 
本API私有错误码如下： 

| 错误码 | 含义说明| 
|---------|---------|
| 10002 | 系统错误，请再次尝试或联系技术客服。  | 
| 10003 | 请求命令非法，请再次尝试或联系技术客服。 | 
| 10004 | 参数非法。请根据应答包中的ErrorInfo字段，检查必填字段是否填充，或者字段的填充是否满足协议要求。 | 
| 10005 |请求包体中携带的用户数量过多（超过了 50 个成员），请减少一次请求的用户数量。 | 
| 10007 | 操作权限不足。请确认操作者是否是APP管理员。 | 
| 10010 | 群组不存在，或者曾经存在过，但是目前已经被解散。 | 
| 10015 | 群组ID非法，请检查群组ID是否填写正确。  | 
| 10018 | 应答包长度超限。因为请求的内容过多，导致应答包超过了最大包长（1MB），请尝试减少单次请求的数据量。  | 

## 3 接口调试工具 

### 3.1 Web调试工具 

通过[REST API在线调试工具](https://avc.cloud.tencent.com/im/APITester/APITester.html#v4/group_open_http_svc/get_group_member_info)调试本接口。 

### 3.2 Server调试工具 

可以通过[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK)中的调试工具进行简单的REST API调试，命令如下： 
```
# 获取群组成员详细信息
./TimRestApiGear.php group_open_http_svc get_group_member_info (group_id) (limit) (offset)
```
更多调试工具参见[REST API调试工具](/doc/product/269/REST%20API简介#5-rest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7)。

## 4 API集成 

### 4.1 PHP集成 

在云通信[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK#3-timrestapigear.php.E4.BD.BF.E7.94.A8.E8.AF.B4.E6.98.8E)中，可以通过TimRestInterface的如下成员函数快速集成该API： 
```
// 获取群组成员详细信息
abstract function group_get_group_member_info($group_id, $limit, $offset);
```

## 5 可能触发的回调 

无。 

## 6 参考 

REST API：修改群成员资料（[v4/group_open_http_svc/modify_group_member_info](/doc/product/269/修改群成员资料)）。 
