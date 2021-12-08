## 功能说明
 App 管理员可以通过该接口获取 App 中所有群组的 ID。

## 接口调用说明
### 适用的群组类型
即时通信 IM 内置多种群组类型，详情请参见 [群组系统](https://cloud.tencent.com/document/product/269/1502)。

### 请求 URL 示例
```
https://console.tim.qq.com/v4/group_open_http_svc/get_appid_group_list?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```
### 请求参数说明

下表仅列出调用本接口时涉及修改的参数及其说明，更多参数详情请参考 [REST API 简介](https://cloud.tencent.com/document/product/269/1519)。

| 参数               | 说明                                 |
| ------------------ | ------------------------------------ |
| v4/group_open_http_svc/get_appid_group_list  | 请求接口                             |
| sdkappid           | 创建应用时即时通信 IM 控制台分配的 SDKAppID |
| identifier         | 必须为 App 管理员帐号，更多详情请参见 [App 管理员](https://cloud.tencent.com/document/product/269/31999#app-.E7.AE.A1.E7.90.86.E5.91.98)                |
| usersig            | App 管理员帐号生成的签名，具体操作请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)    |
| random             | 请输入随机的32位无符号整数，取值范围0 - 4294967295                 |


### 最高调用频率

1次/秒。

### 请求包示例

- **基础形式**
如果 App 中的总群数量超过10000个，最多只会返回10000个群组 ID（如果需要完整获取，必须使用分页拉取的形式）。
```
{}
```
- **分页拉取**
可以使用 Limit 和 Next 两个值用于控制分页拉取：
 -  Limit 限制回包中 GroupIdList 中群组的个数，不得超过10000。
 - Next 控制分页。对于分页请求，第一次填0，后面的请求填上一次返回的 Next 字段，当返回的 Next 为0，代表所有的群都已拉取到。
   例如：假设需要分页拉取，每页展示 20 个，则第一页的请求参数应当为`{“Limit” : 20, “Next” : 0}`，第二页的请求参数应当为`{“Limit” : 20, “Next” : 上次返回的Next字段}`，依此类推。

 Limit 或者 Next 的取值不会对应答包体中的 TotalCount 造成影响。
 ```
{
    "Limit": 1000,
    "Next": 0
}
```

- **指定群组形态**
可以指定拉取的群组所属的群组形态，如 Public，Private，ChatRoom、AVChatRoom和BChatRoom。
```
{
    "GroupType" : "Public" // 拉取哪种群组形态，不填为拉取所有
}
```
- **ALL IN ONE**
```
{
    "Limit": 1000,
    "Next": 0,
    "GroupType" : "Public" // 拉取哪种群组形态，不填为拉取所有
}
```


### 请求包字段说明

| 字段 | 类型 |属性 |说明 |
|---------|---------|---------|---------|
| Limit | Integer | 选填| 本次获取的群组 ID 数量的上限，不得超过 10000。如果不填，默认为最大值 10000 |
| Next | Integer | 选填 | 群太多时分页拉取标志，第一次填0，以后填上一次返回的值，返回的 Next 为0代表拉完了 |
| GroupType | String | 选填 |如果仅需要返回特定群组形态的群组，可以通过 GroupType 进行过滤，但此时返回的 TotalCount 的含义就变成了 App 中属于该群组形态的群组总数。不填为获取所有类型的群组。<br>群组形态包括 Public（公开群），Private（即 Work，好友工作群），ChatRoom（即 Meeting，会议群），AVChatRoom（音视频聊天室），BChatRoom（在线成员广播大群）和社群（Community）|

### 应答包体示例
```
{
    "ActionStatus": "OK",
    "ErrorInfo": "",
    "ErrorCode": 0,
    "TotalCount": 2,
    "GroupIdList": [
        {
            "GroupId": "@TGS#2J4SZEAEL"
        },
        {
            "GroupId": "@TGS#2C5SZEAEF"
        }
    ],
    "Next": 4454685361
}
```

### 应答包字段说明

| 字段 | 类型| 说明 |
|---------|---------|---------|
| ActionStatus | String | 请求处理的结果，OK 表示处理成功，FAIL 表示失败 |
| ErrorCode|	Integer	|错误码，0表示成功，非0表示失败 |
| ErrorInfo | String | 错误信息  |
| TotalCount | Integer | App 当前的群组总数。如果仅需要返回特定群组形态的群组，可以通过 GroupType 进行过滤，但此时返回的 TotalCount 的含义就变成了 App 中该群组形态的群组总数；<br/>例如：假设 App 旗下总共 50000 个群组，其中有 20000 个为公开群组，如果将请求包体中的 GroupType 设置为 Public，那么不论 Limit 和 Offset 怎样设置，应答包体中的 TotalCount 都为 20000，且 GroupIdList 中的群组全部为公开群组  |
| GroupIdList | Array | 获取到的群组 ID 的集合 |
| Next | Integer | 分页拉取的标志 |

## 错误码说明

除非发生网络错误（例如502错误），否则该接口的 HTTP 返回码均为200。真正的错误码，错误信息是通过应答包体中的 ErrorCode、ErrorInfo 来表示的。
公共错误码（60000到79999）参见 [错误码](https://cloud.tencent.com/document/product/269/1671) 文档。
本 API 私有错误码如下：

| 错误码 |含义说明 |
|---------|---------|
| 10002 | 服务器内部错误，请重试 |
| 10004 | 参数错误，请根据错误信息检查请求参数是否正确，例如`GroupType` |
| 10007 | 操作权限不足，此 API 只有 App 管理员才可以调用 |
| 10018 | 应答包长度超过最大包长（1MB），请求的内容过多，请尝试减少单次请求的数据量 |

## 接口调试工具

通过 [REST API 在线调试工具](https://29294-22989-29805-29810.cdn-go.cn/api-test.html#v4/group_open_http_svc/get_appid_group_list) 调试本接口。

## 参考
获取用户所加入的群组（[v4/group_open_http_svc/get_joined_group_list](https://cloud.tencent.com/document/product/269/1625)）。

