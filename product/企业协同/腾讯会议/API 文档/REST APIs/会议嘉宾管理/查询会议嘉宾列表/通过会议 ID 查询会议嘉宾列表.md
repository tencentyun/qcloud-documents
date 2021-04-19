## 接口描述
**描述**：通过会议 ID 查询会议嘉宾列表，只有会议创建人才有权限查询。
**调用方式**：GET
**接口请求域名**：
```Plaintext
https://api.meeting.qq.com/v1/guests/{meeting_id}?userid={userid}&instanceid={instanceid}

```




## 输入参数

以下请求参数列表仅列出了接口请求参数，HTTP 请求头公共参数请参见签名验证章节的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)。

| 参数名称              | 必选 | 参数类型 | 参数描述                                                     |
| --------------------- | ---- | -------- | ------------------------------------------------------------ |
| meeting_id            | 是   | String   | 会议 ID。                                                    |
| userid                | 是   | String   | 用户的 ID（企业内部请使用企业唯一用户标识，OAuth2.0 鉴权用户请使用 openId）。 |
| instanceid            | 是   | Integer  | 用户的终端设备类型：<br/>1：PC <br/>2：Mac<br/>3：Android <br/>4：iOS <br/>5：Web <br/>6：iPad <br/>7：Android Pad <br/>8：小程序 |


## 输出参数

| 参数名称     | 参数类型  | 参数描述         |
| ------------ | --------- | ---------------- |
| meeting_id   | String    | 会议 ID。           |
| meeting_code | String    | 会议 Code。         |
| subject | String    | 会议主题。         |
| guests       | Guest 数组 | 会议嘉宾列表数组。 |

**会议嘉宾 Guest 对象**

| 参数名称     | 参数类型 | 参数描述                                           |
| ------------ | -------- | -------------------------------------------------- |
| area         | String   | 国家/地区代码（例如：中国传86，不是+86，也不是0086）。 |
| phone_number | String | 手机号。                                             |
| guest_name   | String   | 嘉宾名称。                                           |

## 示例

#### 输入示例
```plaintext
GET https://api.meeting.qq.com/v1/guests/15923312864334416762?userid=leonxsun&instanceid=1

```


#### 输出示例

```plaintext
{
    "meeting_id":"15923312864334416762",
    "meeting_code":"653202434",
    "subject":"jiabin",
    "guests":[
        {
            "area":"86",
            "phone_number":"xxxxxx",
            "guest_name":"test"
        }
    ]
}

```
