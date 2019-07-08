## 功能说明
 支持分页拉取所有好友。

## 接口调用说明
### 请求 URL 示例
```
https://console.tim.qq.com/v4/sns/friend_get_all?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```
### 请求参数说明
下表仅列出调用本接口时涉及修改的参数及其说明，更多参数详情请参考 [REST API 简介](https://cloud.tencent.com/document/product/269/1519)。

| 参数               | 说明                                 |
| ------------------ | ------------------------------------ |
| v4/sns/friend_get_all  | 请求接口                             |
| sdkappid           | 创建应用时云通信 IM 控制台分配的 SDKAppID |
| identifier         | 必须为 App 管理员帐号，更多详情请参见 [App 管理员](https://cloud.tencent.com/document/product/269/31999#app-.E7.AE.A1.E7.90.86.E5.91.98)                |
| usersig            | App 管理员帐号生成的签名，具体操作请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)    |
| random             | 请输入随机的32位无符号整数                 |

### 最高调用频率

100次/秒。如需提升调用频率，请根据 [工单模板](https://cloud.tencent.com/document/product/269/3916#rest-api-.E8.B0.83.E7.94.A8.E9.A2.91.E7.8E.87.E8.B0.83.E6.95.B4) 提交工单申请处理。

### 请求包示例

```
{
    "From_Account":"id",
    "TimeStamp":0,
    "StartIndex":0,
    "TagList":
    [
        "Tag_Profile_IM_Nick",
        "Tag_SNS_IM_Group",
        "Tag_SNS_IM_Remark"
    ],
    "LastStandardSequence":0,
    "GetCount":100
}
```

### 请求包字段说明

|字段|类型|属性|说明|
|-------|-------|-------|------|
| From_Account|String |必填|需要拉取该 Identifier 的好友|
| TimeStamp|Integer |选填|上次拉取的时间戳，不填或为0时表示全量拉取|
| StartIndex|Integer |必填|拉取的起始位置|
| TagList|Array |选填|指定要拉取的字段 Tag，支持拉取的字段有：<br />1. 标配资料字段，详情可参见 <a href="https://cloud.tencent.com/document/product/269/1500#.E6.A0.87.E9.85.8D.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5">标配资料字段</a>；<br />2. 自定义资料字段，详情可参见 <a href="https://cloud.tencent.com/document/product/269/1500#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5">自定义资料字段</a>；<br />3. 标配好友字段，详情可参见 <a href="https://cloud.tencent.com/document/product/269/1501#.E6.A0.87.E9.85.8D.E5.A5.BD.E5.8F.8B.E5.AD.97.E6.AE.B5">标配好友字段</a>；<br />4. 自定义好友字段，详情可参见 <a href="https://cloud.tencent.com/document/product/269/1501#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.A5.BD.E5.8F.8B.E5.AD.97.E6.AE.B5">自定义好友字段</a>|
| LastStandardSequence|Integer |选填|上次拉取标配关系链的 Sequence，仅在只拉取标配关系链字段时有用|
| GetCount|Integer |选填|每页需要拉取的好友数量：<br />1. 默认每页返回100个好友<br />2. 每页最多返回100个好友的数据<br />3. 如果拉取好友超时，请适量减少每页拉取的好友数|

### 应答包体示例

```
{
    "NeedUpdateAll":"GetAll_Type_Yes",
    "TimeStampNow":1462334521,
    "StartIndex":0,
    "InfoItem":
    [
        {
            "Info_Account":"id1",
            "SnsProfileItem":
            [
                {
                    "Tag":"Tag_Profile_IM_Nick",
                    "Value":"NickTest1"
                },
                {
                    "Tag":"Tag_SNS_IM_Group",
                    "Value":["Group1"]
                },
                {
                    "Tag":"Tag_SNS_IM_Remark",
                    "Value":"Remark1"
                }
            ]
        },
         {
            "Info_Account":"id2",
            "SnsProfileItem":
            [
                {
                    "Tag":"Tag_Profile_IM_Nick",
                    "Value":"NickTest2"
                },
                {
                    "Tag":"Tag_SNS_IM_Group",
                    "Value":["Group1","Group2"]
                },
                {
                    "Tag":"Tag_SNS_IM_Remark",
                    "Value":"Remark2"
                }
            ]
        }
    ],
    "CurrentStandardSequence": 2,
    "FriendNum": 2,
    "ActionStatus":"OK",
    "ErrorCode":0,
    "ErrorInfo":"",
    "ErrorDisplay":""
}
```

### 应答包字段说明

|字段|类型|说明|
|------|------|------|
| NeedUpdateAll|String|是否需要全量更新：<br />"GetAll_Type_YES" 表示需要全量更新；<br />"GetAll_Type_NO"表示不需要全量更新|
| TimeStampNow|Integer|本次拉取的时间戳，客户端需要保存该时间，下次请求时通过 TimeStamp 字段返回给后台|
| StartIndex|Integer|下页拉取的起始位置|
| InfoItem|Array|好友对象数组，每一个好友对象都包括了 Info_Account 和 SnsProfileItem|
| Info_Account|String|好友的 Identifier|
| SnsProfileItem|Array|好友的详细信息数组，数组每一个元素都包括 Tag 和 Value|
| Tag|String|好友的资料字段或好友字段的名称|
| Value|String/Integer/Array|好友的资料字段或好友字段的值，详情可参见 <a href="https://cloud.tencent.com/document/product/269/1501#.E5.85.B3.E7.B3.BB.E9.93.BE.E5.AD.97.E6.AE.B5">关系链字段</a> 及 <a href="https://cloud.tencent.com/document/product/269/1500#.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5">资料字段</a>|
| CurrentStandardSequence|Integer|本次拉取标配关系链的 Sequence，客户端需要保存该 Sequence，下次请求时通过 LastStandardSequence 字段返回给后台|
| FriendNum|Integer|好友总数|
| ActionStatus|String|请求处理的结果，“OK” 表示处理成功，“FAIL” 表示失败|
| ErrorCode|	Integer	|错误码，0表示成功，非0表示失败 |
| ErrorInfo|String|详细错误信息|
| ErrorDisplay|String|详细的客户端展示信息|


### 错误码说明

除非发生网络错误（例如502错误），否则该接口的 HTTP 返回码均为200。真正的错误码、错误信息是通过应答包体中的 ErrorCode、ErrorInfo 来表示的。
公共错误码（60000到79999）参见 [错误码](https://cloud.tencent.com/document/product/269/1671) 文档。
本 API 私有错误码如下：

| 错误码 | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| 30001  | 请求参数错误，请根据错误描述检查请求参数                     |
| 30003  | 请求的用户帐号不存在                                         |
| 30004  | 请求需要 App 管理员权限                                      |
| 30006  | 服务器内部错误，请重试                                       |
| 30007  | 网络超时，请稍后重试                                         |


## 接口调试工具
通过 [REST API 在线调试工具](https://avc.cloud.tencent.com/im/APITester/APITester.html#v4/sns/friend_get_all) 调试本接口。

## 参考

- 添加好友（<a href="https://cloud.tencent.com/document/product/269/1643">v4/sns/friend_add</a>）
- 删除好友（<a href="https://cloud.tencent.com/document/product/269/1644">v4/sns/friend_delete</a>）
- 删除所有好友（<a href="https://cloud.tencent.com/document/product/269/1645">v4/sns/friend_delete_all</a>）
- 校验好友（<a href="https://cloud.tencent.com/document/product/269/1646">v4/sns/friend_check</a>）
- 拉取指定好友（<a href="https://cloud.tencent.com/document/product/269/8609">v4/sns/friend_get_list</a>）
