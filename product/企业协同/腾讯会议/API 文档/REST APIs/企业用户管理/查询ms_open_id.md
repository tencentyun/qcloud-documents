## 基本信息
- **描述：**
 - 查询指定会议的用户的 ms_open_id，支持在会议开始前、会议进行中、会议结束后查询。
 - 支持企业自建应用（JWT 鉴权），仅支持查询本企业创建的会议。
 - 支持 OAuth2.0 鉴权，仅支持查询该应用所创建的会议。
- **调用方式：**GET
- **接口请求域名：**
```jons
https://api.meeting.qq.com/v1/meetings/{meetingId}/ms-open-id
```

## 路径参数
| 参数名称  | 示例   | 备注       |
| --------- | ------ | ---------- |
| meetingId | 123456 | 会议唯一 ID。 |

## 请求参数

| 参数名称         | 是否必须 | 示例   | 备注                                                         |
| ---------------- | -------- | ------ | ------------------------------------------------------------ |
| operator_id      | 是       | test-1 | 操作者 ID。<br>operator_id 必须与 operator_id_type 配合使用。<br>根据 operator_id_type 的值，operator_id 代表不同类型。 |
| operator_id_type | 是       | 1      | 操作者 ID 的类型：<br> 1：userid <br>2：open_id <br>3：rooms_id          |

## 返回数据

| 名称       | 类型   | 是否必须| 备注                                                    | 
| ---------- | ------ | --------  | ------------------------------------------------------- | 
| meeting_id | string | 必须      | 会议唯一 ID。                                             |        
| ms_open_id | string | 必须        | 当场会议的用户临时 ID，可用于会控操作，适用于所有用户。 |        


## 示例
### 输入示例

```plaintext
GET
https://api.meeting.qq.com/v1/meetings/100001/ms-open-id?operator_id=user1&operator_id_type=1
```


### 输出示例

```plaintext
{
   "meeting_id":"100001",
   "ms_open_id":"12345678"
}
```
