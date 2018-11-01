## 背景说明
1. 脏字指云通信为 App 配置的敏感词，如果检查的内容包含脏字，将拒绝请求，并返回 [80001错误](/doc/product/269/错误码#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)；
2. 脏字检查的内容包括群组消息（只检查文本消息 [TIMTextElem](/doc/product/269/消息格式描述#.E6.96.87.E6.9C.AC.E6.B6.88.E6.81.AF.E5.85.83.E7.B4.A0)，不支持对自定义消息 [TIMCustomElem](/doc/product/269/消息格式描述#.E8.87.AA.E5.AE.9A.E4.B9.89.E6.B6.88.E6.81.AF.E5.85.83.E7.B4.A0) 的过滤）、群组资料（群名称、群简介、群公告）和群名片；
3. 云通信的脏字集中已经涵盖了一批默认脏字（政治、色情等领域）；
4. 如果 App 有除默认脏字集之外的自定义脏字需求，可以通过脏字管理的 REST API 进行配置。


## 功能说明
1. App 管理员可以通过该接口添加自定义的脏字；
2. 添加自定义脏字成功后，需要等待 5 分钟才能生效；
3. 默认 IM 添加脏字不能超过 50 个，如果超过 50 个则多次请求即可。

## 接口调用说明
#### 请求 URL
```
https://console.tim.qq.com/v4/openim_dirty_words/add?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

#### 请求参数
URL 中各参数的含义以及填写方式参见 [REST API简介](/doc/product/269/REST API简介)。

#### 最高调用频率
100次/秒。如需提升调用频率，请根据 [工单模板](/doc/product/269/云通信配置变更需求工单#2.15-rest-api.E8.B0.83.E7.94.A8.E9.A2.91.E7.8E.87.E8.B0.83.E6.95.B4) 提交工单申请处理。

### 请求
#### HTTP 请求方式
POST

#### HTTP 请求包体格式
JSON

#### 请求包示例
支持批量添加 App 自定义的脏字，添加的新脏字和已有的脏字数量之和不超过 50 个，，如果超过 50 个则需要多次请求。
```
{
    "DirtyWordsList": [  // 自定义脏字列表（必填），列表中的脏字不能超过 50 个
        "韩国代购",    //每个自定义脏字不能超过 200 字节
        "发票"
    ]
}
```

#### 请求包字段说明

| 字段 | 类型 | 属性 | 说明 |
|---------|---------|---------|---------|
| DirtyWordsList | Array | 必填 |该字段用来指定需要添加的自定义脏字。添加的新脏字和已有的脏字数量之和不超过50个，每个脏字的长度不能超过200字节。  |

### 应答
#### 应答包体示例
```
{
    "ActionStatus": "OK",
    "ErrorInfo": "",
    "ErrorCode": 0
}
```

#### 应答包字段说明

| 字段 | 类型 | 说明 |
|---------|---------|---------|
| ActionStatus | String | 请求处理的结果，“OK” 表示处理成功，“FAIL” 表示失败。 |
| ErrorCode | Integer | 错误码。  |
| ErrorInfo | String  | 错误信息。   |

### 错误码说明
除非发生网络错误（例如 502 错误），该接口的 HTTP 返回码均为 200。真正的错误码、错误信息是通过应答包体中的 ErrorCode、ErrorInfo 来表示的。
公共错误码（60000 到 79999）参见 [REST API公共错误码](/doc/product/269/错误码#rest-api.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。
本 API 私有错误码如下：

| 错误码 | 含义说明|
|---------|---------|
| 10002 | 系统错误，请再次尝试或联系技术客服。 |
| 10003 | 请求命令非法，请再次尝试或联系技术客服。 |
| 10004| 参数非法。请根据应答包中的 ErrorInfo 字段，检查必填字段是否填充，或者字段的填充是否满足协议要求。 |
| 10007 | 操作权限不足。请确认操作者是否是 [APP管理员](/doc/product/269/帐号登录集成说明#3.4-app.E7.AE.A1.E7.90.86.E5.91.98)。|

## 接口调试工具
#### Web 调试工具
通过 [REST API在线调试工具](https://avc.qcloud.com/im/APITester/APITester.html?_ga=1.139133813.770908707.1524645548#v4/openim_dirty_words/get) 调试本接口。

#### Server 调试工具
无。
更多调试工具参见 [REST API调试工具](/doc/product/269/REST%20API简介#5-rest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7)。

## API 集成
#### PHP 集成
无。

## 可能触发的回调
无。

## 参考

REST API：查询 App 的自定义脏字（[v4/openim_dirty_words/get](/doc/product/269/查询APP自定义脏字)）；
REST API：删除 App 的自定义脏字（[v4/openim_dirty_words/delete](/doc/product/269/删除APP自定义脏字)）。
