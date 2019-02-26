## 1 功能说明 
1. APP管理员通过接口提供关键词对群组进行模糊搜索，如果关键词与群组中的某项资料匹配则群组被搜索到。
2. 目前对模糊搜索进行匹配的资料只有群名称，未来可能支持其他类型的群组资料。 
3. 如果需要使用该功能，请根据[工单模板](/doc/product/269/云通信配置变更需求工单#2.15-rest-api.E8.B0.83.E7.94.A8.E9.A2.91.E7.8E.87.E8.B0.83.E6.95.B4)提交工单申请开通。
 
## 2 接口调用说明 

### 2.1 适用的群组类型

云通信中内置了私有群、公开群、聊天室、互动直播聊天室和在线成员广播大群五种群组类型，详情请见[群组形态介绍](/doc/product/269/群组系统#2-.E7.BE.A4.E7.BB.84.E5.BD.A2.E6.80.81.E4.BB.8B.E7.BB.8D)，其中：
1. 公开群、聊天室和互动直播聊天室默认不支持使用本REST API进行模糊搜索，并在返回结果中展示搜索到的群组资料。如需使用该服务，需要申请开通；
2. 私有群不支持模糊搜索，这种类型的群组在搜索的结果中返回10007错误；
3. 在线成员广播大群同样不支持模糊搜索。

### 2.2 请求URL 
```
https://console.tim.qq.com/v4/group_open_http_svc/search_group?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json 
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

用来获取群组信息，只包含用于搜索的关键字。
```
{
    "Content": "Test"  // 搜索关键字（目前只支持对群名称进行匹配）
}
```

#### 2.7.2 分页拉取

分页拉取搜索到的群组信息，必须同时设置PageNum和GroupPerPage字段； 
PageNum用来指定拉取第几页的群组； 
GroupPerPage用来指定每页群组个数。 
```
{
    "Content": "Test",
    "PageNum":2,       //从第2页开始拉取
    "GroupPerPage":2   //每页群组2个
}
```

#### 2.7.3 拉取指定的信息

可以指定在被搜索到的群组中，拉取哪些公开基础信息，在GroupBasePublicInfoFilter中设置。
```
{
    "Content": "Test",
    "ResponseFilter": {  
       "GroupBasePublicInfoFilter": [ //基础信息过滤器，可以通过它设置需要拉取的公开的基础信息
           "Type",
           "Name",
           "Introduction"
       ]
    }
}
```

#### 2.7.4 ALL IN ONE
```
{
    "Content": "Test",
    "PageNum": 1,       //从第1页开始拉取
    "GroupPerPage": 2,  //每页拉取2个
    "ResponseFilter": {  
       "GroupBasePublicInfoFilter": [  //基础信息过滤器，可以通过它设置需要拉取的公开的基础信息
           "Type",
           "Name",
           "Introduction"
       ]
    }
}
```

### 2.8 请求包字段说明 

| 字段 | 类型 | 属性 | 说明 |
|---------|---------|---------|---------|
| Content | String | 必填 |需要搜索的关键字。  |
| PageNum | Integer | 选填 |从第几页开始搜索。  |
| GroupPerPage | Integer | 选填 |每页有多少个群。  |
| GroupBasePublicInfoFilter | Array | 选填 |基础公开信息字段过滤器，指定需要获取的基础信息字段，基础信息字段详情参见：[群基础资料](/doc/product/269/群组系统#4.1-.E7.BE.A4.E5.9F.BA.E7.A1.80.E8.B5.84.E6.96.99)。暂时还不支持所有字段。 现在支持的公开信息有群ID、群名称、群组类型、群创建时间、群创建者、成员个数、群成员最大个数、群简介、群头像、申请加群选项、最后一条消息以及在线成员。  |

### 2.9 应答包体示例

#### 2.9.1 基础形式

```
{
    "ActionStatus": "OK",
    "ErrorCode": 0,
    "GroupInfo": [    
        {
            "ApplyJoinOption": "FreeAccess",
            "CreateTime": 1441175346,
            "ErrorCode": 0,
            "FaceUrl": "",
            "GroupId": "@TGS#3UMVKPAE2",
            "Introduction": "",
            "MaxMemberNum": 10000,
            "MemberNum": 1,
            "Name": "Test Group",
            "OnlineMemberNum": 5,
            "Owner_Account": "Testaixuetangceshi223", 
            "Type": "ChatRoom"
        },
        {
            "ApplyJoinOption": "NeedPermission",
            "CreateTime": 1436170360,
            "ErrorCode": 0,
            "FaceUrl": "",
            "GroupId": "@TGS#2IDSJPAEA",
            "Introduction": "Test",
            "MaxMemberNum": 2000,
            "MemberNum": 3,
            "Name": "Test",
            "OnlineMemberNum": 0,
            "Owner_Account": "86-18664312448",
            "Type": "Public"
        },
        {
            "ApplyJoinOption": "NeedPermission",
            "CreateTime": 1435651578,
            "ErrorCode": 0,
            "FaceUrl": "",
            "GroupId": "@TGS#23BRJPAEG",
            "Introduction": "",
            "MaxMemberNum": 200,
            "MemberNum": 3,
            "Name": "测试群Test1",   //群名称包含Test
            "OnlineMemberNum": 0,
            "Owner_Account": "86-13265568199",
            "Type": "Public"
        }
    ],
    "TotalRecord": 3
}
```

#### 2.9.2 分页拉取

```
{
    "ActionStatus": "OK",
    "ErrorCode": 0,
    "GroupInfo": [   // 因为分页指定拉取2个，所以返回2个群
        {
            "ApplyJoinOption": "FreeAccess",
            "CreateTime": 1441175346,
            "ErrorCode": 0,
            "FaceUrl": "",
            "GroupId": "@TGS#3UMVKPAE2",
            "Introduction": "Test", 
            "MaxMemberNum": 10000,
            "MemberNum": 1,
            "Name": "Test",
            "OnlineMemberNum": 0,
            "Owner_Account": "aixuetangceshi223",
            "Type": "ChatRoom"
        },
        {
            "ApplyJoinOption": "NeedPermission",
            "CreateTime": 1436170360,
            "ErrorCode": 0,
            "FaceUrl": "",
            "GroupId": "@TGS#2IDSJPAEA",
            "Introduction": "群昵称Test",
            "MaxMemberNum": 2000,
            "MemberNum": 3,
            "Name": "测试例会Test1",    //群名称包含Test
            "OnlineMemberNum": 0,
            "Owner_Account": "86-18664312448",
            "Type": "Public"
        }
    ],
    "TotalRecord": 3
}
```

#### 2.9.3 拉取指定的信息

```
{
    "ActionStatus": "OK",
    "ErrorCode": 0,     // 这里的ErrorCode无意义，需要判断每个群组的ErrorCode
    "GroupInfo": [      
        {
            "ErrorCode": 0,
            "GroupId": "@TGS#3UMVKPAE2", //任何情况均会返回
            "Introduction": "",
            "Name": "aixue1Test",    //群名称包含Test
            "Type": "ChatRoom"   //群组类型
        },
        {
            "ErrorCode": 0,
            "GroupId": "@TGS#3EMAKPAEU",
            "Introduction": "11111",
            "Name": "聊天室Test1",   //群名称包含Test
            "Type": "ChatRoom"
        },
        {
            "ErrorCode": 0,
            "GroupId": "@TGS#2IDSJPAEA",
            "Introduction": "群昵称",
            "Name": "测试例会Test1", //群名称包含Test
            "Type": "Public"
        }
    ],
    "TotalRecord": 3
}
```

#### 2.9.4 ALL IN ONE

```
{
    "ActionStatus": "OK",
    "ErrorCode": 0,     // 这里的ErrorCode无意义，需要判断每个群组的ErrorCode
    "GroupInfo": [      // 因为分页指定拉取2个，所以返回2个群
        {
            "ErrorCode": 0,
            "GroupId": "@TGS#3UMVKPAE2",
            "Introduction": "",
            "Name": "aixue1Test",    //群名称包含Test
            "Type": "ChatRoom"   //群组类型
        },
        {
            "ErrorCode": 0,
            "GroupId": "@TGS#3EMAKPAEU",
            "Introduction": "111      1111",
            "Name": "聊天室Test1", //群名称包含Test
            "Type": "ChatRoom"
        }
     ],
    "TotalRecord": 3 
}}
```

### 2.10 应答包字段说明 

| 字段 | 类型 | 说明 |
|---------|---------|---------|
| ActionStatus | String | 请求处理的结果，OK表示处理成功，FAIL表示失败。 |
| ErrorCode | Integer | 错误码。 |
| ErrorInfo | String | 错误信息。 |
| GroupInfo | Array | 返回结果为群组信息数组，内容包括[群基础资料](/doc/product/269/群组系统#4.1-.E7.BE.A4.E5.9F.BA.E7.A1.80.E8.B5.84.E6.96.99)字段，和[群成员资料](/doc/product/269/群组系统#4.2-.E7.BE.A4.E6.88.90.E5.91.98.E8.B5.84.E6.96.99)字段。 |
| TotalRecord | Array | 搜索到的群组总个数，不受分页影响。  |

### 2.11 错误码说明 

除非发生网络错误（例如502错误），该接口的HTTP返回码均为200。真正的错误码、错误信息是通过应答包体中的ErrorCode、ErrorInfo来表示的。 
公共错误码（60000到79999）参见[REST API公共错误码](/doc/product/269/错误码#rest-api.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 
本API私有错误码如下： 

| 错误码 | 含义说明| 
|---------|---------|
| 10002 | 系统错误，请再次尝试或联系技术客服。  | 
| 10003 | 请求命令非法，请再次尝试或联系技术客服。 | 
| 10004 | 参数非法。请根据应答包中的ErrorInfo字段，检查必填字段是否填充，或者字段的填充是否满足协议要求。 | 
| 10007 | 操作权限不足。请确认操作者是否是APP管理员。| 
| 10010 | 群组不存在，或者曾经存在过，但是目前已经被解散。 | 
| 10015 | 群组ID非法，请检查群组ID是否填写正确。  | 
| 10018 | 应答包长度超限。因为请求的内容过多，导致应答包超过了最大包长（1MB），请尝试减少单次请求的数据量。  | 

## 3 接口调试工具 

### 3.1 Web调试工具 

通过[REST API在线调试工具](https://avc.cloud.tencent.com/im/APITester/APITester.html#v4/group_open_http_svc/search_group)调试本接口。 

### 3.2 Server调试工具 

无。
更多调试工具参见[REST API调试工具](/doc/product/269/REST%20API简介#5-rest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7)。

## 4 API集成 

### 4.1 PHP集成 

无。

## 5 可能触发的回调 

无。

## 6 参考 

REST API：获取群成员详细资料（[v4/group_open_http_svc/search_group](/doc/product/269/获取群组成员详细资料)）； 
