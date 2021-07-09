## 接口描述
**描述**：使用 userid 获取企业用户详情。企业 secert 鉴权用户可获取该用户所属企业下的用户详情，OAuth2.0 鉴权用户只能获取该企业下 OAuth2.0 应用的用户详情。
**调用方式**：GET
**接口请求域名**：
```Plaintext
https://api.meeting.qq.com/v1/users/{userid}
```





## 输入参数

以下请求参数列表仅列出了接口请求参数，HTTP 请求头公共参数请参见签名验证章节的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)。

| 参数名称 | 必选 | 参数类型 | 参数描述 |
| -------- | ---- | -------- | -------- |
| userid   | 是   | String   | 	调用方用于标示用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 <br>企业唯一用户标识说明：<br>1. 企业对接 SSO 时使用的员工唯一标识 ID；<br>2. 企业调用创建用户接口时传递的 userid 参数。   |



## 输出参数

| 参数名称    | 参数类型 | 参数描述                   |
| ----------- | -------- | -------------------------- |
| username    | String   | 用户昵称。                   |
| update_time | String   | 更新时间。                   |
| status      | String   | 用户状态：<br>1：正常<br>2：注销<br>3：未激活<br>4：禁用 |
| email       | String   | 邮箱地址。                   |
| phone       | String   | 手机号码。                   |
| userid     | String   | 	调用方用于标示用户的唯一 ID（例如企业用户可以为企业账户英文名、个人用户可以为手机号等）。         |
| uuid| 	String| 	用户身份 ID（腾讯会议颁发的用于开放平台的唯一用户 ID）。| 
| area        | String   | 地区编码（国内默认86）。     |




## 示例

#### 输入示例
```plaintext
GET https://api.meeting.qq.com/v1/users/9527
```



#### 输出示例
```Plaintext
{
    "area": "86",
    "update_time": "2020-04-21 18:01:29",
    "phone": "13000000000",
    "user_id": "9527",
    "email": "",
    "username": "testusername",
    "status": "1",
    "uuid": "WM4Fs4Th56ogU13JiK"
}
```
