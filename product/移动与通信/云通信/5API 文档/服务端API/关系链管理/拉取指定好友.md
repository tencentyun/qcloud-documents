## 功能说明
-  支持拉取指定好友。
-  建议每次拉取的好友数不超过100，避免因回包数据量太大导致回包失败。

## 接口调用说明
### 请求URL
```
https://console.tim.qq.com/v4/sns/friend_get_list?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```
### 请求参数说明

下表仅列出调用本接口时涉及修改的参数及其说明，更多参数详情请参考 [REST API 简介](https://cloud.tencent.com/document/product/269/1519)。

| 参数               | 说明                                 |
| ------------------ | ------------------------------------ |
| v4/sns/friend_get_list  | 请求接口                             |
| sdkappid           | 创建应用时云通信 IM 控制台分配的 SDKAppID |
| identifier         | 必须为 App 管理员帐号，更多详情请参见 [App 管理员](https://cloud.tencent.com/document/product/269/31999#app-.E7.AE.A1.E7.90.86.E5.91.98)                |
| usersig            | App 管理员帐号生成的签名，具体操作请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)    |
| random             | 请输入随机的32位无符号整数                 |

### 最高调用频率

100次/秒。如需提升调用频率，请根据 [工单模板](https://cloud.tencent.com/document/product/269/3916#rest-api-.E8.B0.83.E7.94.A8.E9.A2.91.E7.8E.87.E8.B0.83.E6.95.B4) 提交工单申请处理。

### 请求包示例
- **基础形式**
```
{
    "From_Account":"id",
    "To_Account":
    [
        "id1"
    ]
}
```
- **完整形式**
```
{
    "From_Account":"id",
    "To_Account":
    [
        "id1"
    ],
    "TagList":
    [
        "Tag_Profile_IM_Nick",
        "Tag_SNS_IM_Group",
        "Tag_SNS_IM_Remark"
    ]
}
```

- **批量拉取指定好友**
```
{
    "From_Account":"id",
    "To_Account":
    [
        "id1",
        "id2",
        "id3"
    ],
    "TagList":
    [
        "Tag_Profile_IM_Nick",
        "Tag_SNS_IM_Group",
        "Tag_SNS_IM_Remark"
    ]
}
```

### 请求包字段说明

|字段|类型|属性|说明|
|----|----|-----|-----|
| From_Account|String|必填|请求拉取该 Identifier 的好友|
| To_Account|Array|必填|请求拉取的好友的 Identifier 列表<br />注意：每次拉取的好友数不得超过100，避免因回包数据量太大以致回包失败|
|TagList|Array|选填|指定要拉取的资料字段及好友字段：<br />1. 标配资料字段<br />2. 自定义资料字段<br />3. 标配好友字段<br />4. 自定义好友字段，关于各个字段详细信息可参阅 [关系链系统](https://cloud.tencent.com/document/product/269/1501)|



### 应答包体示例
- **基础形式、完备形式**
```
{
    "InfoItem":
    [
        {
            "To_Account":"id1",
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
            ],
			"ResultCode": 0,
			"ResultInfo": ""
        }
    ],
	"ActionStatus":"OK",
	"ErrorCode":0,
	"ErrorInfo":"",
	"ErrorDisplay":""
}
```

- **批量拉取指定好友**

```
{
    "InfoItem":
    [
        {
            "To_Account":"id1",
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
            ],
			"ResultCode": 0,
			"ResultInfo": ""
        },
        {
            "To_Account":"id2",
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
            ],
			"ResultCode": 0,
			"ResultInfo": ""
        },
		{
			"To_Account": "id3",
			"ResultCode": 31211,
			"ResultInfo": "SNS_FRD_GET_LIST_FRD_NO_EXIST"
		}
    ],
	"Fail_Account":["id3"],
	"ActionStatus":"OK",
	"ErrorCode":0,
	"ErrorInfo":"",
	"ErrorDisplay":""
}
```

### 应答包字段说明

|字段|	类型|	说明|
|-----|------|-----|
| InfoItem|	Array	|好友对象数组|
| To_Account|	String|	好友的 Identifier|
| SnsProfileItem|	Array	|好友的详细信息数组，数组每一个元素都包括 Tag 和 Value|
| Tag	|String|	好友的资料字段或好友字段的名称|
| Value	|String|	好友的资料字段或好友字段的值|
| ResultCode|	Integer	|To_Account 的处理结果，0表示成功，非0表示失败|
| ResultInfo|	String|	To_Account 的错误描述信息，成功时该字段为空|
| Fail_Account|Array|返回处理失败的用户列表，仅当存在失败用户时才返回该字段|
| ActionStatus|	String	|请求处理的结果，“OK” 表示处理成功，“FAIL” 表示失败|
| ErrorCode|	Integer	|错误码，0表示成功，非0表示失败 |
| ErrorInfo|	String	|详细错误信息|
| ErrorDisplay|	String	|详细的客户端展示信息|



## 错误码说明

除非发生网络错误（例如502错误），否则该接口的 HTTP 返回码均为200；真正的错误码、错误信息是通过应答包体中的 ErrorCode、ErrorInfo 来表示的。
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
通过 [REST API 在线调试工具](https://avc.cloud.tencent.com/im/APITester/APITester.html#v4/sns/friend_get_list) 调试本接口。

## 参考

- 添加好友（<a href="https://cloud.tencent.com/document/product/269/1643">v4/sns/friend_add</a>）
- 删除好友（<a href="https://cloud.tencent.com/document/product/269/1644">v4/sns/friend_delete</a>）
- 删除所有好友（<a href="https://cloud.tencent.com/document/product/269/1645">v4/sns/friend_delete_all</a>）
- 校验好友（<a href="https://cloud.tencent.com/document/product/269/1646">v4/sns/friend_check</a>）
- 拉取指定好友（<a href="https://cloud.tencent.com/document/product/269/8609">v4/sns/friend_get_list</a>）
