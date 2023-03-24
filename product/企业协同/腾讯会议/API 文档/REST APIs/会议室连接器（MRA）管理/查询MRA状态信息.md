## 接口描述
- **描述**：会议中查询指定 MRA 设备的当前状态信息， 包括：
 - 名称
 - 静音状态
 - 视频状态
 - 举手状态
 - 默认布局等
- **调用方式**：GET
- **接口请求域名**：
```Plaintext
https://api.meeting.qq.com/v1/meetings/{meeting_id}/query-participant
```



## 输入参数
HTTP 请求头公共参数请参见签名验证章节的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)。

| 参数名称  | 必选 | 参数类型 | 参数描述                     |
| --------- | ---- | -------- | ---------------------------- |
| meetingId | 是   | String   | 会议 ID，周期性会议传总会议 ID。 |
| operator_id | 是   | String   | 操作者 ID。<br>operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。|
| operator_id_type | 是   | Integer   | 	操作者 ID 的类型：<br>1：userid  <br>4：ms_open_id |
| instanceid | 是   | Integer   | 设备类型 ID。 |
| user_ms_open_id | 是   | String   | 	被查询用户临时身份 ID，该字段需 UrlEncode。 |
| user_instance_id | 是   | Integer   | 被查询用户设备类型 ID。 |



## 输出参数
返回查询用户的当前状态信息。

| 参数名称   | 参数类型 | 参数描述                     |
| --------- | -------- | ---------------------------- |
| ms_open_id | String | 	当场会议的用户临时 ID，可用于会控操作，适用于所有用户。 |
| instanceid | Integer | 用户的终端设备类型 ID。 |
| user_role | Integer | 	用户角色：<br>0：普通成员角色<br>1：创建者角色<br>2：主持人<br>3：创建者+主持人<br>4：游客<br>5：游客+主持人 <br>6：联席主持人 <br>7：创建者+联席主持人 |
| webinar_member_role | Integer | 	网络研讨会成员角色：<br>0：普通参会角色<br>1：内部嘉宾<br>2：外部嘉宾<br>3：邀请链接入会嘉宾<br>4：观众 |
| IP | String | 用户的 IP 地址。当用户在会中时才能返回。 |
| name | String | 用户当前显示名称。 |
| audio_state | Bool | 麦克风状态：<br>true：开启<br>false：关闭 |
| video_state | Bool | 摄像头状态：<br> true：开启<br>false：关闭 |
| screen_shared_state | Bool | 	屏幕共享状态：<br>true：开启<br>false：关闭 |
| default_layout | Integer | 	当前成员的默认分屏设置：<br>1：等分模式<br>2：全屏模式<br>3：1+N<br>**说明：**该参数仅支持 MRA 设备。 |
| raise_hands_state | Bool | 举手状态：<br>true：举手中<br>false：手放下 |


## 示例
### 输入示例
```plaintext
GET 
https://api.meeting.qq.com/v1/meetings/100001/query-participant?operator_id=user1&operator_id_type=1&instanceid=1&user_ms_open_id=12345678&user_instance_id=9
```

### 输出示例
```plaintext
{
   "ms_open_id":"",
   "instanceid":9,
   "user_role":0,
   "IP":"192.168.2.2",
   "name":"user2",
   "audio_state":true,
   "video_state":false,
   "screen_shared_state":false,
   "default_layout":1,
   "raise_hands_state":false
}
```
