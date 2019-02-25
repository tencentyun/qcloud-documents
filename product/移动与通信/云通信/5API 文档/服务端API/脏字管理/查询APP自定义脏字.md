## 背景说明
- 脏字指云通信为 App 配置的敏感词，如果检查的内容包含脏字，将拒绝请求，并返回 [80001错误](https://cloud.tencent.com/document/product/269/1671#.E5.90.8E.E5.8F.B0.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。
- 脏字检查的内容包括群组消息（只检查文本消息 [TIMTextElem](https://cloud.tencent.com/document/product/269/2720#.E6.96.87.E6.9C.AC.E6.B6.88.E6.81.AF.E5.85.83.E7.B4.A0)，不支持对自定义消息 [TIMCustomElem](https://cloud.tencent.com/document/product/269/2720#.E8.87.AA.E5.AE.9A.E4.B9.89.E6.B6.88.E6.81.AF.E5.85.83.E7.B4.A0) 的过滤）、群组资料（群名称、群简介、群公告）和群名片。
- 云通信的脏字集已经涵盖了一批默认脏字（政治、色情等领域）。
- 如果 App 有除默认脏字集之外的自定义脏字需求，可以通过脏字管理的 REST API 进行配置。

## 功能说明
App 管理员可以通过该接口查询已设置的自定义脏字。

## 接口调用说明
### 请求 URL 示例
```
https://console.tim.qq.com/v4/openim_dirty_words/get?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```

### 请求参数说明

| 参数               | 说明                                 |
| ------------------ | ------------------------------------ |
| https              | 请求协议为 HTTPS，请求方式为 POST       |
| console.tim.qq.com | 固定域名                             |
| v4/openim_dirty_words/get  | 请求接口                     |
| usersig            | App 管理员帐号生成的签名               |
| identifier         | 必须为 App 管理员帐号                |
| sdkappid           | 创建应用时云通信控制台分配的 SdkAppid |
| random             | 32位无符号整数随机数                 |
| contenttype        | 固定值为：json                       |

### 最高调用频率
100次/秒。如需提升调用频率，请根据 [工单模板](https://cloud.tencent.com/document/product/269/3916#rest-api.E8.B0.83.E7.94.A8.E9.A2.91.E7.8E.87.E8.B0.83.E6.95.B4) 提交工单申请处理。
### 请求包示例
查询已经对 App 设置的自定义脏字。

### 应答包体示例
```
{
    "ActionStatus": "OK",
    "ErrorInfo": "",
    "ErrorCode": 0,
    "DirtyWordsList": [
        "回收金币",
        "代刷人气",
        "抽奖"
    ]
}
```

### 应答包字段说明

| 字段 | 类型 | 说明 |
|---------|---------|---------|
| ActionStatus | String | 请求处理的结果，“OK” 表示处理成功，“FAIL” 表示失败 |
| ErrorCode|	Integer	|错误码，0表示成功，非0表示失败 |
| DirtyWordsList | Array  | 返回结果是已经设置的自定义脏字  |

## 错误码说明
除非发生网络错误（例如502错误），否则该接口的 HTTP 返回码均为200。真正的错误码，错误信息是通过应答包体中的 ErrorCode、ErrorInfo 来表示的。
公共错误码（60000到79999）参见 [错误码](https://cloud.tencent.com/document/product/269/1671) 文档。
本 API 私有错误码如下：

| 错误码 | 含义说明|
|---------|---------|
| 10002 | 服务器内部错误，请重试 |
| 10003 | 请求命令字非法 |
| 10007 | 操作权限不足，比如 Public 群组中普通成员尝试执行踢人操作，但只有 App 管理员才有权限 |

## 接口调试工具
通过 [REST API 在线调试工具](https://avc.qcloud.com/im/APITester/APITester.html#v4/openim_dirty_words/get) 调试本接口。

## 参考

- 添加 App 的自定义脏字（[v4/openim_dirty_words/add](https://cloud.tencent.com/document/product/269/2397)）
- 删除 App 的自定义脏字（[v4/openim_dirty_words/delete](https://cloud.tencent.com/document/product/269/2398)）
