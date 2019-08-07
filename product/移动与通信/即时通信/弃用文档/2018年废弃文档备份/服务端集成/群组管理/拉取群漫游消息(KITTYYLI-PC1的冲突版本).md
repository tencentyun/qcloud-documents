## 1 背景说明

1. IM云的消息是按Seq排序的，按照server收到消息的顺序分配Seq，先发的消息Seq小，后发的Seq大。
2. 如果用户想拉取一个群的全量消息，首次拉取时不用填拉取Seq，Server会自动返回最新的消息，以后拉取时拉取Seq填上次返回的最小Seq减1。
3. 如果返回消息的IsPlaceMsg为1，表示这个Seq的消息或者过期、或者存储失败、或者被删除了。

## 2 功能说明 

1. APP管理员可以通过该接口拉取群组的漫游消息。 
 
## 3 接口调用说明 

### 3.1 适用的群组类型

云通信中内置了私有群、公开群、聊天室、互动直播聊天室和在线成员广播大群五种群组类型，详情请见[群组形态介绍](/doc/product/269/群组系统#2-.E7.BE.A4.E7.BB.84.E5.BD.A2.E6.80.81.E4.BB.8B.E7.BB.8D)，其中：
1. 私有群、公开群和聊天室支持使用本REST API拉取漫游消息；
2. 互动直播聊天室和在线成员广播大群不存储漫游消息。

### 3.2 请求URL 
```
https://console.tim.qq.com/v4/group_open_http_svc/group_msg_get_simple?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json 
```
### 3.3 请求参数 

URL中各参数的含义以及填写方式参见[REST API简介](/doc/product/269/REST API简介)。 

### 3.4 最高调用频率 

100次/秒。如需提升调用频率，请根据[工单模板](/doc/product/269/云通信配置变更需求工单#2.15-rest-api.E8.B0.83.E7.94.A8.E9.A2.91.E7.8E.87.E8.B0.83.E6.95.B4)提交工单申请处理。 

### 3.5 HTTP请求方式 

POST 

### 3.6 HTTP请求包体格式 

JSON 

### 3.7 请求包示例

#### 3.7.1 基础形式

拉取群组的漫游消息，返回群组最新的ReqMsgNumber条消息。
```
{
    "GroupId": "@TGS#15ERQPAER",    //拉取消息的群ID
    "ReqMsgNumber": 2      //需要拉取的消息条数
}
```

#### 3.7.2 按seq拉取

按指定seq拉取群组的漫游消息； 
返回消息seq小于等于ReqMsgSeq的ReqMsgNumber条消息。 
```
{
    "GroupId": "@TGS#15ERQPAER",    
    "ReqMsgSeq": 7803321,       //请求的消息最大seq，返回<=ReqMsgSeq的消息
    "ReqMsgNumber": 2     
}
```

### 3.8 请求包字段说明 

| 字段 | 类型 | 属性 | 说明 |
|---------|---------|---------|---------|
| GroupId | String | 必填 |要拉取漫游消息的群组Id。  |
| ReqMsgNumber | Integer | 必填 |拉取的漫游消息的条数，目前一次请求最多返回20条漫游消息，所以这里最好小于等于20。  |
| ReqMsgSeq | Integer | 选填 |拉取消息的最大seq。  |

### 3.9 应答包体示例

```
{
    "ActionStatus": "OK",
    "ErrorCode": 0,
    "GroupId": "@TGS#15ERQPAER",
    "IsFinished": 1,
    "RspMsgList": [
        {
            "From_Account": "144115197276518801",
            "IsPlaceMsg": 0,
            "MsgBody": [
                {
                    "MsgContent": {
                        "Data": "\b\u0001\u0010\u0006\u001A\u0006猫瞳",
                        "Desc": "MIF",
                        "Ext": ""
                    },
                    "MsgType": "TIMCustomElem"
                },
                {
                    "MsgContent": {
                        "Data": "",
                        "Index": 15
                    },
                    "MsgType": "TIMFaceElem"
                }
            ],
            "MsgRandom": 51083293,
            "MsgSeq": 7803321,
            "MsgTimeStamp": 1458721802
        },
        {
            "From_Account": "144115198339527735",
            "IsPlaceMsg": 0,
            "MsgBody": [
                {
                    "MsgContent": {
                        "Data": "\b\u0001\u0010\u0006\u001A\u000F西瓜妹妹。",
                        "Desc": "MIF",
                        "Ext": ""
                    },
                    "MsgType": "TIMCustomElem"
                },
                {
                    "MsgContent": {
                        "Text": "报上来"
                    },
                    "MsgType": "TIMTextElem"
                }
            ],
            "MsgRandom": 235168582,
            "MsgSeq": 7803320,
            "MsgTimeStamp": 1458721797
        }
    ]
}
```

### 3.10 应答包字段说明 

| 字段 | 类型 | 说明 |
|---------|---------|---------|
| ActionStatus | String | 请求处理的结果，OK表示处理成功，FAIL表示失败。 |
| ErrorCode | Integer | 错误码。 |
| GroupId | String | 请求中的群组Id。 |
| IsFinished | Integer | 是否返回了请求区间的全部消息，当消息长度太长或者区间太大（超过20）导致无法返回全部消息时值为0。 |
| RspMsgList | Array | 返回的消息列表。 |
| From_Account | String | 消息的发送者。 |
| IsPlaceMsg | Integer | 是否是空洞消息，当消息被删除或者消息过期后，MsgBody为空，这个字段为1。 |
| MsgRandom | Integer | 消息随机值，用来对消息去重，有客户端发消息时填写，如果没有填，服务端会自动生成一个。 |
| MsgSeq | Integer | 消息seq，用来标识唯一消息，值越小发送的越早。 |
| MsgTimeStamp | Integer | 消息被发送的时间戳，server的时间。 |
| MsgBody | Array | 消息内容。 |

### 3.11 错误码说明 

除非发生网络错误（例如502错误），该接口的HTTP返回码均为200。真正的错误码、错误信息是通过应答包体中的ErrorCode、ErrorInfo来表示的。 
公共错误码（60000到79999）参见[REST API公共错误码](/doc/product/269/REST%20API简介#5-rest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7)。 
本API私有错误码如下： 

| 错误码 | 含义说明| 
|---------|---------|
| 10002 | 系统错误，请再次尝试或联系技术客服。  | 
| 10004 | 参数非法。请根据应答包中的ErrorInfo字段，检查必填字段是否填充，或者字段的填充是否满足协议要求。 | 
| 10007 | 操作权限不足。请确认操作者是否是APP管理员。| 
| 10010 | 群组不存在，或者曾经存在过，但是目前已经被解散。 | 
| 10015 | 群组ID非法，请检查群组ID是否填写正确。  | 

## 4 接口调试工具 

### 4.1 Web调试工具 

通过[REST API在线调试工具](https://avc.cloud.tencent.com/im/APITester/APITester.html#v4/group_open_http_svc/group_msg_get_simple)调试本接口。 

### 4.2 Server调试工具 

无。
更多调试工具参见[REST API调试工具](/doc/product/269/REST%20API简介#5-rest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7)。

## 5 API集成 

### 5.1 PHP集成 

无。

## 6 可能触发的回调 

无。

## 7 参考 

无。
