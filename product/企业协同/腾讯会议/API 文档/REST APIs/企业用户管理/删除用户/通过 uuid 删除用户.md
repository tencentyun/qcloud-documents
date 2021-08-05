## 接口描述 
**描述**：使用 uuid 删除企业用户，目前暂不支持 OAuth2.0 鉴权访问。
**调用方式**：DELETE
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
无输出参数，成功返回空消息体，失败返回 [错误码](https://cloud.tencent.com/document/product/1095/43704) 和错误信息。



## 示例

#### 输入示例
```plaintext
DELETE https://api.meeting.qq.com/v1/users?uuid=WM4Fs4Th56ogU13JiK
```

#### 输出示例
删除用户成功，返回 Body 为空。
