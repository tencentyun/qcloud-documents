## 接口描述
描述：用会议 Code 修改直播信息。
调用方式：PUT
接口请求域名：`https://api.meeting.qq.com/v1/meetings/live_play/config`

## 输入参数
HTTP 请求头公共参数参考签名验证章节里的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)。

| 参数名称     | 必选 | 参数类型 | 参数描述           |
| ------------ | ---- | -------- | ------------------ |
| meeting_code | 是   | String   | 会议号码。           |
| userid       | 是   | String   | 调用API的用户 ID。    |
| instanceid   | 是   | Integer  | 用户的终端设备类型： <br>1：PC <br>2：Mac<br>3：Android <br>4：iOS <br>5：Web <br>6：iPad <br>7：Android Pad <br>8：小程序。 |
| live_config  | 是   | Object   | 直播配置。           |

#### 直播配置对象
| 参数名称             | 参数类型 | 参数描述         |
| -------------------- | -------- | ---------------- |
| live_subject         | String   | 直播主题。         |
| live_summary         | String   | 直播简介。         |
| enable_live_password | Boolean   | 是否开启直播密码。 |
| live_password        | string   | 直播密码。         |
| enable_live_im       | Boolean  | 是否开启直播互动。 |
| enable_live_replay   | Boolean  | 是否开启直播回放。 |

## 输出参数
成功则返回空消息体，失败则返回 [错误码](https://tcloud-doc.isd.com/document/product/1095/43704) 和错误信息。

| 参数名称   | 必选 | 参数类型 | 参数描述                 |
| ---------- | ---- | -------- | ------------------------ |
| error_info | 否   | Object   | 错误信息对象（失败时返回）。 |

#### 错误信息对象定义

| 参数名称   | 参数类型 | 参数描述 |
| ---------- | -------- | -------- |
| error_code | Integer  | 错误码。   |
| message    | String   | 错误描述。 |

## 示例
#### 输入示例
```Plaintext
PUT https://api.meeting.qq.com/v1/meetings/live_play/config

{
    "userid": "test_userid",
    "instanceid": 1,
    "meeting_code": "33291296584",
    "live_config": {
   	 "live_subject": "test_subject",
   	 "live_summary": "test_subject",
   	 "enable_live_password": true,
   	 "live_password": "654322",
   	 "enable_live_im": true,
   	 "enable_live_replay": true
    }
}
```

#### 输出示例（失败时返回）
```
{"error_info":{"error_code":200005,"message":"Json Schema validation failed!"}}
```
