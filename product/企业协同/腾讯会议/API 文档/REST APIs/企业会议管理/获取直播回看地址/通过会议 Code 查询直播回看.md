## 接口描述
**描述**：通过会议 Code 查询直播回看信息，企业 secret 鉴权用户（会议创建者）可查看任何该企业该用户创建的会议中的直播回看，目前暂不支持 OAuth2.0 鉴权访问。
**调用方式**：GET
**接口请求域名**：
```plaintext
https://api.meeting.qq.com/v1/meetings/live_play/replays?meeting_code={meetingCode}&userid={userid}&instanceid={instanceid}
```


## 输入参数
HTTP 请求头公共参数参考签名验证章节里的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)。

| 参数名称    | 必选 | 参数类型 | 参数描述           |
| ----------- | ---- | -------- | ------------------ |
| meetingCode | 是   | String   | 有效的会议 Code。     |
| userid      | 是   | String   | 调用 API 的用户 ID。    |
| instanceid  | 是   | Integer  | 用户的终端设备类型： <br>1：PC <br>2：Mac<br>3：Android <br>4：iOS <br>5：Web <br>6：iPad <br>7：Android Pad <br>8：小程序 |

## 输出参数

| 参数名称          | 参数类型 | 参数描述 |
| ----------------- | -------- | -------- |
| meeting_number    | Integer  | 会议数量。 |
| meeting_info_list | Array    | 会议列表。 |

#### 会议对象

| 参数名称         | 参数类型     | 参数描述                               |
| ---------------- | ------------ | -------------------------------------- |
| meeting_id       | String       | 会议 ID。                                 |
| meeting_code     | String       | 会议 Code。                               |
| subject          | String       | 会议主题。                               |
| live_replay_list | 直播回看数组 | 直播回看数组（会议创建人才有权限查询）。 |

#### 直播回放对象

| 参数名称     | 参数类型 | 参数描述     |
| ------------ | -------- | ------------ |
| live_room_id | String   | 直播房间号。   |
| live_subject | String   | 直播主题。     |
| video_url    | String   | 直播回放链接。 |


## 示例
#### 输入示例
```plaintext
GET https://api.meeting.qq.com/v1/meetings/live_play/replays?meeting_code=13418515243&userid=tester&instanceid=1
```

#### 输出示例
```plaintext
{
    "meeting_number":1,
    "meeting_info_list":[
        {
            "meeting_id":"1900004128969145064",
            "meeting_code":"13418515243",
            "subject":"tester预定的会议",
            "live_replay_list":[
                {
                    "video_url":"https://meeting.tencent.com/l/xxxx",
                    "live_subject":"tester预定的会议",
                    "live_room_id":"206830819"
                },
                {
                    "video_url":"https://meeting.tencent.com/l/xxxx",
                    "live_subject":"leonxsun预定的会议",
                    "live_room_id":"112594341"
                }
            ]
        }
    ]
}

							 
```
