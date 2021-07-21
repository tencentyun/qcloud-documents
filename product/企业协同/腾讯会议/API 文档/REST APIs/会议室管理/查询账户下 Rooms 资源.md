## 接口描述
**描述**：查询企业购买的 Rooms 资源，目前暂不支持 OAuth2.0 鉴权访问。
**调用方式**：GET
**接口请求域名**：
```Plaintext
https://api.meeting.qq.com/v1/rooms-inventory

```




## 输入参数
HTTP 请求头公共参数请参见签名验证章节的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)，无额外请求参数。



## 输出参数

| 参数名称              | 必选 | 参数类型 | 参数描述         |
| --------------------- | ---- | -------- | ---------------- |
| normal_count          | 是   | Integer  | 普通设备数。     |
| special_count         | 是   | Integer  | 专款设备数。     |
| normal_used_count     | 是   | Integer  | 普通设备使用数。 |
| special_used_count    | 是   | Integer  | 专款设备使用数。 |
| normal_expired_count  | 是   | Integer  | 普通设备过期数。 |
| special_expired_count | 是   | Integer  | 专款设备过期数。 |


## 示例

#### 输入示例
```plaintext
GET
https://api.meeting.qq.com/v1/rooms-inventory
```




#### 输出示例
```plaintext
{
    "normal_count":10,
    "special_count":2,
    "normal_used_count":2,
    "special_used_count":1,
    "normal_expired_count":0,
    "special_expired_count":0
}
```
