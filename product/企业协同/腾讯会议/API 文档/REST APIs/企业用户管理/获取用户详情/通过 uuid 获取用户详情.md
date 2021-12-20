## 接口描述
**描述**：使用 uuid 获取企业用户详情。企业 secret 鉴权用户可获取该用户所属企业下的用户详情，暂不支持 OAuth2.0 鉴权访问。
**调用方式**：GET
**接口请求域名**：
```Plaintext
https://api.meeting.qq.com/v1/users?uuid={uuid}
```

## 输入参数

以下请求参数列表仅列出了接口请求参数，HTTP 请求头公共参数请参见签名验证章节的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)。

| 参数名称 | 必选 | 参数类型 | 参数描述                                               |
| -------- | ---- | -------- | ------------------------------------------------------ |
| uuid     | 是   | String   | 用户身份 ID（腾讯会议颁发的用于开放平台的唯一用户 ID）。 |



## 输出参数

| 参数名称    | 参数类型 | 参数描述                   |
| ----------- | -------- | -------------------------- |
| username    | String   | 用户昵称。                   |
| update_time | String   | 更新时间，格式：yyyy-MM-dd HH:mm:ss。                 |
| status      | String   | 用户状态：<br>1：正常<br>2：注销<br>3：未激活<br>4：禁用 |
| email       | String   | 邮箱地址。                   |
| phone       | String   | 手机号码。                   |
| userid     | String   | 	调用方用于标示用户的唯一 ID（例如企业用户可以为企业账户英文名、个人用户可以为手机号等）。         |
| uuid| 	String| 	用户身份 ID（腾讯会议颁发的用于开放平台的唯一用户 ID）。| 
| area        | String   | 地区编码（国内默认86）。     |
| staff_id        | String           | 员工工号。                                               |
| job_title       | String           | 员工职位。                                               |
| entry_time      | String           | 入职时间。                                               |
| role_name       | String           | 角色名称。                                               |
| role_code       | String           | 角色类型。                                               |
| department_list | 部门信息对象数组 | 用户部门信息。                                           |

**部门对象**

| 参数名称        | 参数类型 | 参数描述 |
| --------------- | -------- | -------- |
| department_id   | String   | 部门 ID。   |
| department_name | String   | 部门名称。 |



## 示例

#### 输入示例
```plaintext
GET https://api.meeting.qq.com/v1/users?uuid=WM4Fs4Th56ogU13JiK
```



#### 输出示例
```Plaintext
{
    "area": "86",
    "update_time": "2020-04-21 18:01:29",
    "phone": "13000000000",
    "userid": "9527",
    "email": "",
    "username": "testusername",
    "status": "1",
    "uuid": "WM4Fs4Th56ogU13JiK"，
    "job_title": "developer",
	"staff_id": "6666",
	"entry_time": "2021-08-09",
	"role_name": "普通成员",
	"role_code": "NORMAL_ROLE",
	"department_list": [{
		"department_id": "e3ce085****************921fc2c2d",
		"department_name": "主部门"
	}]
}

```
