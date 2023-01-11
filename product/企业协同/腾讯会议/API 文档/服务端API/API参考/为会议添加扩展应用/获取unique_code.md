## 接口描述
- **描述：**
 - 绑定扩展应用到某一个会议，可给应用传入 unique_code，该接口可以让应用查询到对应的 unique_code。
 - 若未绑定应用，或未设定 unique_code，接口返回为空。
- **调用方法：**GET
- **接口请求域名：**
```plaintext
https://api.meeting.qq.com/v1/app/unique-code
```



## 输入参数

| 参数名称 | 是否必须 | 参数类型 | 备注 |
| --- | --- | --- | --- |
| userid | 是 | String | 调用方用于标示用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId） 企业唯一用户标识说明： <br>3：企业对接 SSO 时使用的员工唯一标识 ID <br>4：企业调用创建用户接口时传递的 userid 参数 |
| instanceid | 是 | Integer | 用户的终端设备类型： <br>1：PC <br>2：Mac <br>3：Android <br>4：iOS <br>5：Web <br>6：iPad <br>7：Android Pad <br>8：小程序 |
| meeting_id | 是 | String | 会议 ID |

## 输出参数

| 参数名称 | 是否必须 | 参数类型 | 备注 |
| --- | --- | --- | --- |
| unique_code | 否 | String | 调用方业务相关字段，最大128个字符 |


## 示例
### 输入示例
```plaintext
GET https://api.meeting.qq.com/v1/app/unique-code?instanceid=1&userid=1593602****427&meeting_id=1201116****699152359
```

### 输出示例
```plaintext
{"unique_code":"test"}
```
