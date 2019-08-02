## 背景说明
- 脏字指即时通信 IM 为 App 配置的敏感词，如果检查的内容包含脏字将拒绝请求，并返回错误码 [30005](https://cloud.tencent.com/document/product/269/1671#.E5.85.B3.E7.B3.BB.E9.93.BE.E9.94.99.E8.AF.AF.E7.A0.81)、[40005](https://cloud.tencent.com/document/product/269/1671#.E8.B5.84.E6.96.99.E9.94.99.E8.AF.AF.E7.A0.81) 或 [80001](https://cloud.tencent.com/document/product/269/1671#.E5.90.8E.E5.8F.B0.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。
- 脏字检查的内容包括单聊和群组消息（只检查文本消息 [TIMTextElem](https://cloud.tencent.com/document/product/269/2720#.E6.96.87.E6.9C.AC.E6.B6.88.E6.81.AF.E5.85.83.E7.B4.A0)，不支持对自定义消息 [TIMCustomElem](https://cloud.tencent.com/document/product/269/2720#.E8.87.AA.E5.AE.9A.E4.B9.89.E6.B6.88.E6.81.AF.E5.85.83.E7.B4.A0) 的过滤）、群名片、群组资料（群名称、群简介、群公告）、用户资料和好友关系链中 bytes 类型的数据（如昵称、好友备注和好友分组等）。
- 即时通信 IM 的脏字集已经涵盖了一批默认脏字（主要是政治、色情等领域）。
- 如果 App 有除默认脏字集之外的自定义脏字需求，可以通过脏字管理的 REST API 进行配置。


## 功能说明
- App 管理员可以通过该接口添加自定义的脏字。
- 添加自定义脏字成功后，需要等待1小时才能生效。
- 单次请求添加脏字不能超过50个，如果脏字数量超过50个，需要分多次请求。累计添加的脏字，建议不要超过5000个。
- 脏字生效后，包含该脏字的请求都会返回失败，所以请务必确保脏字是经过严格谨慎的筛选的。
 

**建议：**
- 不要把常用且含有简单的词语加为脏字，比如单个字母、数字或汉字等，否则会出现大量消息发送失败。
- 不要把整句的长文本添加为脏字，这样的打击效果很差，建议筛选长文本中的关键词语添加。 



## 接口调用说明
### 请求 URL 示例
```
https://console.tim.qq.com/v4/openim_dirty_words/add?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
 ```
### 请求参数说明
 
下表仅列出调用本接口时涉及修改的参数及其说明，更多参数详情请参考 [REST API 简介](https://cloud.tencent.com/document/product/269/1519)。

| 参数               | 说明                                 |
| ------------------ | ------------------------------------ |
| v4/openim_dirty_words/add  | 请求接口                             |
| sdkappid           | 创建应用时即时通信 IM 控制台分配的 SDKAppID |
| identifier         | 必须为 App 管理员帐号，更多详情请参见 [App 管理员](https://cloud.tencent.com/document/product/269/31999#app-.E7.AE.A1.E7.90.86.E5.91.98)                |
| usersig            | App 管理员帐号生成的签名，具体操作请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)    |
| random             | 请输入随机的32位无符号整数                 |


### 最高调用频率
100次/秒。如需提升调用频率，请根据 [工单模板](https://cloud.tencent.com/document/product/269/3916#rest-api-.E8.B0.83.E7.94.A8.E9.A2.91.E7.8E.87.E8.B0.83.E6.95.B4) 提交工单申请处理。
### 请求包示例
支持批量添加 App 自定义的脏字，单次最多可以添加50个脏字。
```
{
    "DirtyWordsList": [ // 自定义脏字列表（必填），列表中的脏字不能超过50个
        "韩国代购", // 每个自定义脏字不能超过200字节
        "发票"
    ]
}
```

### 请求包字段说明

| 字段 | 类型 | 属性 | 说明 |
|---------|---------|---------|---------|
| DirtyWordsList | Array | 必填 |该字段用来指定需要添加的自定义脏字；单次最多可以添加50个脏字，每个脏字的长度不能超过200字节 |

### 应答包体示例
```
{
    "ActionStatus": "OK",
    "ErrorInfo": "",
    "ErrorCode": 0
}
```

### 应答包字段说明

| 字段 | 类型 | 说明 |
|---------|---------|---------|
| ActionStatus | String | 请求处理的结果，“OK” 表示处理成功，“FAIL” 表示失败 |
| ErrorCode|	Integer	|错误码，0表示成功，非0表示失败 |
| ErrorInfo | String  | 错误信息   |

## 错误码说明
除非发生网络错误（例如502错误），否则该接口的 HTTP 返回码均为 200。真正的错误码，错误信息是通过应答包体中的 ErrorCode、ErrorInfo 来表示的。
公共错误码（60000到79999）参见 [错误码](https://cloud.tencent.com/document/product/269/1671) 文档。
本 API 私有错误码如下：

| 错误码 | 含义说明|
|---------|---------|
| 10002 | 服务器内部错误，请重试 |
| 10003 | 请求命令字非法 |
| 10004| 参数非法，请根据错误描述检查请求是否正确 |
| 10007 | 操作权限不足，该API只有 App 管理员才有权限调用 |

## 接口调试工具
通过 [REST API 在线调试工具](https://avc.qcloud.com/im/APITester/APITester.html?_ga=1.139133813.770908707.1524645548#v4/openim_dirty_words/get) 调试本接口。

## 参考

- 查询 App 的自定义脏字（[v4/openim_dirty_words/get](https://cloud.tencent.com/document/product/269/2396)）
- 删除 App 的自定义脏字（[v4/openim_dirty_words/delete](https://cloud.tencent.com/document/product/269/2398)）
