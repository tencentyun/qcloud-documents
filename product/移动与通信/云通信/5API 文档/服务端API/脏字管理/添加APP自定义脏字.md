## 背景说明
- 脏字指云通信为 App 配置的敏感词，如果检查的内容包含脏字，将拒绝请求，并返回 [80001错误](/doc/product/269/错误码#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)；
- 脏字检查的内容包括群组消息（只检查文本消息 [TIMTextElem](/doc/product/269/消息格式描述#.E6.96.87.E6.9C.AC.E6.B6.88.E6.81.AF.E5.85.83.E7.B4.A0)，不支持对自定义消息 [TIMCustomElem](/doc/product/269/消息格式描述#.E8.87.AA.E5.AE.9A.E4.B9.89.E6.B6.88.E6.81.AF.E5.85.83.E7.B4.A0) 的过滤）、群组资料（群名称、群简介、群公告）和群名片；
- 云通信的脏字集已经涵盖了一批默认脏字（政治、色情等领域）；
- 如果 App 有除默认脏字集之外的自定义脏字需求，可以通过脏字管理的 REST API 进行配置。


## 功能说明
- App 管理员可以通过该接口添加自定义的脏字；
- 添加自定义脏字成功后，需要等待 5 分钟才能生效；
- 默认 IM 添加脏字不能超过 50 个，如果超过 50 个则多次请求即可。

## 接口调用说明
### 请求 URL
```
https://console.tim.qq.com/v4/openim_dirty_words/add?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### 请求参数说明

| 参数               | 说明                                 |
| ------------------ | ------------------------------------ |
| https              | 请求协议为 HTTPS，请求方式为 POST       |
| console.tim.qq.com | 固定域名                             |
| v4/openim_dirty_words/add  | 请求接口                     |
| usersig            | App 管理员帐号生成的签名               |
| identifier         | 必须为 App 管理员帐号                |
| sdkappid           | 创建应用时云通信控制台分配的 SdkAppid |
| random             | 32位无符号整数随机数                 |
| contenttype        | 固定为：json                       |

### 最高调用频率

100次/秒。如需提升调用频率，请根据 [工单模板](/doc/product/269/云通信配置变更需求工单#2.15-rest-api.E8.B0.83.E7.94.A8.E9.A2.91.E7.8E.87.E8.B0.83.E6.95.B4)提交工单申请处理。

### 请求包示例
支持批量添加 App 自定义的脏字，添加的新脏字和已有的脏字数量之和不超过 50 个，如果超过 50 个则需要多次请求。
```
{
    "DirtyWordsList": [ // 自定义脏字列表（必填），列表中的脏字不能超过 50 个
        "韩国代购", // 每个自定义脏字不能超过 200 字节
        "发票"
    ]
}
```

### 请求包字段说明

| 字段 | 类型 | 属性 | 说明 |
|---------|---------|---------|---------|
| DirtyWordsList | Array | 必填 |该字段用来指定需要添加的自定义脏字；添加的新脏字和已有的脏字数量之和不超过50个，每个脏字的长度不能超过200字节  |

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
| ErrorCode | Integer | 错误码  |
| ErrorInfo | String  | 错误信息   |

## 错误码说明
除非发生网络错误（例如 502 错误），该接口的 HTTP 返回码均为 200。真正的错误码、错误信息是通过应答包体中的 ErrorCode、ErrorInfo 来表示的。
公共错误码（60000 到 79999）参见 [REST API公共错误码](/doc/product/269/错误码#rest-api.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。
本 API 私有错误码如下：

| 错误码 | 含义说明|
|---------|---------|
| 10002 | 服务器内部错误，请重试 |
| 10003 | 请求命令字非法 |
| 10004| 参数非法，请根据错误描述检查请求是否正确 |
| 10007 | 操作权限不足，比如 Public 群组中普通成员尝试执行踢人操作，但只有 App 管理员才有权限 |

## 接口调试工具
通过 [REST API在线调试工具](https://avc.qcloud.com/im/APITester/APITester.html?_ga=1.139133813.770908707.1524645548#v4/openim_dirty_words/get) 调试本接口。

## 参考

- 查询 App 的自定义脏字（[v4/openim_dirty_words/get](/doc/product/269/查询APP自定义脏字)）
- 删除 App 的自定义脏字（[v4/openim_dirty_words/delete](/doc/product/269/删除APP自定义脏字)）
