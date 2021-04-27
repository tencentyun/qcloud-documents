
## 接口描述
**描述**：通过会议 ID 修改直播配置信息，目前暂不支持 OAuth2.0 鉴权访问。
**调用方式**：PUT
**接口请求域名**：
```plaintext
https://api.meeting.qq.com/v1/meetings/{meeting_id}/live_play/config
```



 
## 输入参数
HTTP 请求头公共参数参考签名验证章节里的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)。

| 参数名称    | 必选 | 参数类型 | 参数描述           |
| ----------- | ---- | -------- | ------------------ |
| userid      | 是   | String   | 用户 ID。            |
| instanceid  | 是   | integer  | 用户的终端设备类型： <br>1：PC <br>2：Mac<br>3：Android <br>4：iOS <br>5：Web <br>6：iPad <br>7：Android Pad <br>8：小程序 |
| live_config | 是   | Object   | 直播配置。           |

#### 直播配置对象

| 参数名称             | 必选 |参数类型 | 参数描述         |
| -------------------- | -------- | -------- | ---------------- |
| live_subject         | 否| String   | 直播主题。         |
| live_summary         | 否|String   | 直播简介。         |
| enable_live_password |否|Boolean   | 是否开启直播密码。<br>true：开启<br>false：不开启 |
| live_password        |否|String   | 直播密码，当设置开启直播密码时，该参数必填。         |
| enable_live_im       | 否|Boolean  | 是否开启直播互动。<br>true：开启<br>false：不开启 |
| enable_live_replay   | 否|Boolean  | 是否开启直播回放。<br>true：开启<br>false：不开启 |
| live_watermark   | 否|object  |直播水印对象信息。     |

**直播水印信息 live_watermark_info**

| **参数名称**  |  **必选** |**参数类型** | **参数描述**                              |
| ------------- | ------------ | ------------ | ----------------------------------------- |
| watermark_opt |否| integer      | 水印选项，默认为0。<br> 0：默认水印<br> 1：无水印 |

## 输出参数
无输出参数，则成功返回空消息体，失败返回 [错误码](https://cloud.tencent.com/document/product/1095/43704) 和错误信息。

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
```http
PUT https://api.meeting.qq.com/v1/meetings/{meeting_id}/live_play/config

{
    "userid": "test_userid",
    "instanceid": 1,
    "live_config": {
   	 "live_subject": "test_subject",
   	 "live_summary": "test_summary",
   	 "enable_live_password": true,
   	 "live_password": "654321",
   	 "enable_live_im": true,
   	 "enable_live_replay": true，
     "live_watermark": {
            "watermark_opt": 0
        }
    }
}

```

#### 输出示例（失败时返回）
```plaintext
{"error_info":{"error_code":200005,"message":"Json Schema validation failed!"}}
```
