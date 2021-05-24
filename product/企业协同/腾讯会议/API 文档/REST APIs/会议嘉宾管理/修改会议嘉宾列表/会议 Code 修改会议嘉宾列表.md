## 接口描述
**描述**：通过会议 Code 修改会议嘉宾列表，只有会议创建人才有权限修改。
**调用方式**：PUT
**接口请求域名**：
```Plaintext
https://api.meeting.qq.com/v1/guests
```




## 输入参数

以下请求参数列表仅列出了接口请求参数，HTTP 请求头公共参数请参见签名验证章节的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)。

| 参数名称     | 必选 | 参数类型      | 参数描述                                                     |
| ------------ | ---- | ------------- | ------------------------------------------------------------ |
| meeting_code | 是   | String        | 会议码。                                                       |
| userid       | 是   | String        | 用户的 ID（企业内部请使用企业唯一用户标识，OAuth2.0 鉴权用户请使用 openId）。 |
| instanceid   | 是   | Integer       | 用户的终端设备类型：<br/>1：PC <br/>2：Mac<br/>3：Android <br/>4：iOS <br/>5：Web <br/>6：iPad <br/>7：Android Pad <br/>8：小程序 |
| guests       | 是   | Guest 对象数组 | 会议嘉宾列表（传空数组会清空嘉宾列表）。                       |


**会议嘉宾 Guest 对象**

| 参数名称     | 必选 | 参数类型 | 参数描述                                           |
| ------------ | ---- | -------- | -------------------------------------------------- |
| area         | 是   | String  | 国家/地区代码（例如：中国传86，不是+86，也不是0086）。 |
| phone_number | 是   |String    | 手机号。                                             |
| guest_name   | 否   | String    | 嘉宾名称。                                           |


## 输出参数

无输出参数，成功返回空消息体，失败返回[ 错误码](https://cloud.tencent.com/document/product/1095/43704) 和错误信息。






## 示例

#### 输入示例
```plaintext
PUT https://api.meeting.qq.com/v1/guests

{
    "meeting_code":"609685458",
    "userid":"xxxxx",
    "instanceid":1,
    "guests":[
        {
            "area":"86",
            "phone_number":"xxxxx",
            "guest_name":"xxxx"
        }
    ]
}


```


#### 输出示例

更新成功，返回 body 为空。

