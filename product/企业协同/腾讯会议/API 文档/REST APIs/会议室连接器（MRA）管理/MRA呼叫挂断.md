## 接口描述
- **描述**：会议中对 MRA 的进行呼叫挂断操作。
- **调用方式**：PUT
- **接口请求域名**：
```Plaintext
https://api.meeting.qq.com/v1/mra-control/meetings/{meetingId}/hangup
```



## 输入参数
HTTP 请求头公共参数请参见签名验证章节的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)。

**请求路径参数**

| 参数名称  | 必选 | 参数类型 | 参数描述                     |
| --------- | ---- | -------- | ---------------------------- |
| meetingId | 	是 | String | 会议 ID，周期性会议传总会议 ID。 |

**请求 body**

| 参数名称  | 必选 | 参数类型 | 参数描述                     |
| --------- | ---- | -------- | ---------------------------- |
| operator_id | 是   | String   | 操作者 ID。<br>operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。|
| operator_id_type | 是   | Integer   | 	操作者 ID 的类型：<br>1：userid  <br>4：ms_open_id |
| instanceid | 是   | Integer   | 用户的终端设备类型 ID。 |
| user | 是   | UserObj   | 被操作用户对象信息。 |

**被操作用户对象 UserObj**

| 参数名称  | 必选 | 参数类型 | 参数描述                     |
| --------- | ---- | -------- | ---------------------------- |
| ms_open_id | 是 | String | 被操作 MRA 设置当前会议中的临时身份 ID。 |
| instanceid | 是 | Integer | 用户的终端设备类型：<br> 9：voip、sip 设备 |



## 输出参数
成功返回空消息体，失败返回 [错误码](https://cloud.tencent.com/document/product/1095/43704) 和错误信息。

## 示例
### 输入示例

```plaintext
PUT
https://api.meeting.qq.com/v1/mra-control/meetings/100001/hangup
{
   "operator_id":"user1",
   "operator_id_type":1,
   "instanceid":1,
   "user":{
      "ms_open_id":"1234567",
      "instanceid":9
            }
}
```

### 输出示例

```
{}
```

