## 接口描述
**描述**：通过会议 ID 查询会议详情。
- 企业 secret 鉴权用户可查询到任何该用户创建的企业下的会议，OAuth2.0 鉴权用户只能查询到通过 OAuth2.0 鉴权创建的会议。
- 本接口的邀请嘉宾限制调整至300人。

**调用方式**：GET
**接口请求域名**：
```plaintext
https://api.meeting.qq.com/v1/meetings/{meetingId}?userid={userid}&instanceid={instanceid}
```



## 输入参数

以下请求参数列表仅列出了接口请求参数，HTTP 请求头公共参数请参见签名验证章节的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)。


| 参数名称 | 必选 | 参数类型 | 参数描述 |
|---------|---------|---------|---------|
| meetingId | 是 | String| 有效的会议 ID。  |
| operator_id      | 否   | String   | 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。<br>**说明**：userid 字段和 operator_id 字段二者必填一项。若两者都填，以 operator_id 字段为准。 |
| operator_id_type | 否   | Integer  | 操作者 ID 的类型：<br>3. rooms_id<br>**说明**：当前仅支持 rooms_id。如操作者为企业内 userid 或 openId，请使用 userid 字段。 |
| userid |否 | String| 调用方用于标示用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。<br>企业唯一用户标识说明：<br>1. 企业对接 SSO 时使用的员工唯一标识 ID；<br>2. 企业调用创建用户接口时传递的 userid 参数。  |
| instanceid | 是 | Integer|用户的终端设备类型： <br>1：PC <br>2：Mac<br>3：Android <br>4：iOS <br>5：Web <br>6：iPad <br>7：Android Pad <br>8：小程序 |


               

## 输出参数
| 参数名称 |参数类型 | 参数描述 |
|---------|---------|---------|
| meeting_number | Integer | 会议数量。  |
|meeting_info_list  |Array| 会议列表。 |




**会议对象**

| 参数名称 |参数类型 | 参数描述 |
|---------|---------|---------|
|subject  |String | 会议主题。  |
|meeting_id   |String| 会议的唯一标示。  |
|meeting_code    |String| 会议 App 的呼入号码。  |
|password   |String | 会议密码。  |
|need_password   |Boolean | 非会议创建者是否需要密码入会。<br>非会议创建者查询会议，且存在会议密码，则字段为 true；其他情况，字段不返回。  |
|status|String|当前会议状态：<br>1. MEETING_STATE_INVALID：<br> 非法或未知的会议状态，错误状态。<br>  2. MEETING_STATE_INIT：<br> 会议待开始。会议预定到预定结束时间前，会议尚无人进会。<br>  3. MEETING_STATE_CANCELLED：<br> 会议已取消。主持人主动取消会议，待开始的会议才能取消，且取消的会议无法再进入。<br> 4. MEETING_STATE_STARTED：<br> 会议已开始。会议中有人则表示会议进行中。<br>5. MEETING_STATE_ENDED：<br> 会议已删除。会议已过预定结束时间且尚无人进会时，主持人删除会议，已删除的会议无法再进入。<br>6. MEETING_STATE_NULL：<br> 会议无状态。会议已过预定结束时间，会议尚无人进会。<br>7. MEETING_STATE_RECYCLED：<br> 会议已回收。会议已过预定开始时间30天，则会议号将被后台回收，无法再进入。|
|type   |Integer  | 会议类型：<br>0：预约会议类型<br>1：快速会议类型   |
|join_url   |String  | 加入会议 URL。  |
|hosts   |用户对象数组  |指定主持人列表，仅商业版和企业版可指定主持人。|
|current_hosts  |用户对象数组  | 会议当前主持人列表。|
|current_co_hosts  |用户对象数组  | 联席主持人列表。|
|participants  |用户对象数组 |邀请的参会者，仅商业版和企业版可邀请参会用户，且只有会议创建者、邀请列表中的成员以及在会议中的成员才可以查询该字段，最多返回200个邀请者；需要查询超过200人的会议邀请者请调用 [获取会议受邀成员列表](https://cloud.tencent.com/document/product/1095/63648) 接口。    |
|start_time  |String | 会议开始时间戳（单位秒）。 |
|end_time  |String | 会议结束时间戳（单位秒）。  |
|settings   |[会议媒体参数对象](#settings) |会议的配置，可为缺省配置。|
| meeting_type           | Integer        | 会议类型：<br>0：普通会议<br>1：周期性会议<br>5：个人会议号 |
| recurring_rule         | period_meeting | 周期性会议设置。                           |
| sub_meetings           | 子会议对象数组 | 周期性子会议列表。                         |
| has_more_sub_meeting   | Integer        | 0：无更多子会议特例   <br>1：有更多子会议特例      |
| remain_sub_meetings    | Integer        | 剩余子会议场数。                           |
| current_sub_meeting_id | String         | 当前子会议 ID（进行中 / 即将开始）。     |
| enable_live | Boolean      | 是否开启直播（会议创建人才有权限查询）。   |
| live_config | 直播信息对象 | 会议的直播配置（会议创建人才有权限查询）。 |
|enable_doc_upload_permission    | Boolean       | 是否允许成员上传文档，默认为允许。                                                     |
|guests   | Guest 数组     | 会议嘉宾列表（会议创建人才有权限查询）。                                                 |
|has_vote   | Boolean     | 是否有投票（会议创建人和主持人才有权限查询）。                                                     |
|enable_enroll   | Boolean     | 是否激活报名。                                                     |




**用户对象**

| 参数名称 | 参数类型 | 参数描述 |
| -------- | -------- | -------- |
| userid   | String   | 调用方用于标示用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。<br>企业唯一用户标识说明：<br>1. 企业对接 SSO 时使用的员工唯一标识 ID；<br>2. 企业调用创建用户接口时传递的 userid 参数。   |




**会议媒体参数对象**

| 参数名称                        | 参数类型 | 参数描述                                                     |
| ------------------------------- | -------- | ------------------------------------------------------------ |
| mute_enable_join                | Bool     | 加入静音状态。                                                 |
| allow_unmute_self               | Bool     | 静音自解除允许。                                               |
| allow_in_before_host            | Bool     | 允许成员在主持人进会前加入会议。                               |
| auto_in_waiting_room            | Bool     | 开启等候室。                                                   |
| allow_screen_shared_watermark   | Bool     | 开启屏幕共享水印。                                             |
| water_mark_type | Integer | 水印样式，默认为单排：<br> 0：单排<br>  1：多排<br>  |
| only_allow_enterprise_user_join | Bool     | 是否仅企业内部成员可入会。 <br>true：仅企业内部用户可入会 <br>false：所有人可入会 |
| auto_record_type | String     | 自动录制类型，仅客户端2.7及以上版本生效。<br>none：禁用 <br>local：本地录制 <br>cloud：云录制<br> |
|participant_join_auto_record  | Boolean | 当有参会成员入会时立即开启云录制，默认值为 false 关闭，关闭时，主持人入会自动开启云录制；当设置为开启时，则有参会成员入会自动开启云录制。<br>说明：<br><li>该参数必须 auto_record_type 设置为“cloud”时才生效，该参数依赖企业账户设置，当企业强制锁定后，该参数必须与企业配置保持一致。<li>仅客户端2.7及以上版本生效。 |
|enable_host_pause_auto_record | Boolean | 允许主持人暂停或者停止云录制，默认值为 true 开启，开启时，主持人允许暂停和停止云录制；当设置为关闭时，则主持人不允许暂停和关闭云录制。<br>说明：<br><li>该参数必须将 auto_record_type 设置为“cloud”时才生效，该参数依赖企业账户设置，当企业强制锁定后，该参数必须与企业配置保持一致。<li>仅客户端2.7及以上版本生效。 |

**子会议对象**

| 参数名称       | 参数类型 | 参数描述                           |
| -------------- | -------- | ---------------------------------- |
| sub_meeting_id | String   | 子会议 ID。                           |
| status         | Integer  | 子会议状态。<br>0：默认存在<br> 1：已删除 |
| start_time     | Integer  | 子会议开始时间（UTC 秒）。            |
| end_time       | Integer  | 子会议结束时间（UTC 秒）。           |

**周期性会议 period_meeting**

| 参数名称       | 必选 | 参数类型 | 参数描述                                                     |
| -------------- | ---- | -------- | ------------------------------------------------------------ |
| recurring_type | 否   | Integer  | 周期性会议频率，默认值为0。<br>0：每天<br> 1：每周一至周五<br>2：每周<br>3：每两周<br>4：每月<br> |
| until_type     | 否   | Integer | 结束重复类型，默认值为0。<br>0：按日期结束重复<br>1：按次数结束重复 |
| until_date     | 否   | Integer | 结束日期时间戳，默认值为当前日期 + 7天。                             |
| until_count    | 否   |Integer| 限定会议次数（1-50次），默认值为7次。                              |

**直播信息对象**

| 参数名称           | 参数类型 | 参数描述         |
| ------------------ | -------- | ---------------- |
| live_subject       |  String    | 直播主题。         |
| live_summary       |  String    | 直播简介。         |
| live_password      | String   | 直播密码。         |
| enable_live_im     | Boolean  | 是否开启直播互动。 |
| enable_live_replay | Boolean  | 是否开启直播回放。 |
| live_addr          |  String   | 直播观看地址。     |
| live_watermark   | object  |直播水印对象信息。     |


**直播水印信息 live_watermark_info**

| **参数名称**  | **必选** | **参数类型** | **参数描述**                              |
| ------------- | -------- | ------------ | ----------------------------------------- |
| watermark_opt | 否       | Integer    | 水印选项，默认为0。<br> 0：默认水印<br> 1：无水印 |


**会议嘉宾 Guest 对象**

| 参数名称     | 参数类型 | 参数描述                                           |
| ------------ |-------- | -------------------------------------------------- |
| area         |  String   | 国家/地区代码（例如：中国传86，不是+86，也不是0086）。 |
| phone_number | String   | 手机号。                                             |
| guest_name   |  String   | 嘉宾名称。                                          |



## 示例
#### 输入示例

```plaintext
GET https://api.meeting.qq.com/v1/meetings/7567173273889276131?userid=tester1&instanceid=1
```

#### 输出示例（普通会议）

```plaintext
{  
  "meeting_number": 1,  
  "meeting_info_list": [    
    {      
      "subject": "tester's meeting",      
      "meeting_id": "7567173273889276131",      
      "meeting_code": "806146667",      
      "password": "1111",      
      "status": "MEETING_STATE_ENDED",      
      "start_time": "1572085800",      
      "end_time": "1572089400", 
      "type": 1,     
      "hosts": [  
      {
          "userid": "tester"
        }
      ],      
      "participants": [        
         {
          "userid": "tester"
        }     
      ],      
      "join_url": "https://wemeet.qq.com/w/5NmV29k",
      "meeting_type": 0,      
      "settings": {        
        "mute_enable_join": true,        
        "allow_unmute_self": false,
        "play_ivr_on_leave": false,
        "allow_in_before_host": true,
	    "auto_in_waiting_room": false,
	    "allow_screen_shared_watermark": true,
	    "only_allow_enterprise_user_join": false       
      },
       "enable_live":true,
        "live_config":{
            "live_subject":"test",
            "live_summary":"test",
            "live_password":"654321",
            "enable_live_im":true,
            "enable_live_replay":true,
            "live_addr":"https://meeting.tencent.com/l/xxxx",
            "live_watermark":{
                "watermark_opt":0
            }
        },
        "guests":[
            {
                "area":"86",
                "phone_number":"xxxxxxxxx",
                "guest_name":"xxxx"
            }
        ]   
    }  
  ]
}


```
#### 输出示例（周期性会议）
```plaintext
{
  "meeting_number": 1,
  "meeting_info_list": [
    {
      "subject": "tester's meeting",
      "meeting_id": "18357763596888459343",
      "meeting_code": "31380342405",
      "status": "MEETING_STATE_INIT",
      "start_time": "1599622242",
      "end_time": "1599625842",
      "hosts": [
        {
          "userid": "tester"
        }
      ],
      "join_url": "https://meeting.tencent.com/s/iY4GQ2HkQQGL",
      "settings": {
        "mute_enable_join": true,
        "allow_unmute_self": false,
        "allow_in_before_host": true,
        "auto_in_waiting_room": true,
        "allow_screen_shared_watermark": true,
        "only_enterprise_user_allowed": false
      },
      "sub_meetings": [
        {
          "sub_meeting_id": "1599622242",
          "status": 0,
          "start_time": 1599622242,
          "end_time": 1599625842
        },
        {
          "sub_meeting_id": "1599708642",
          "status": 0,
          "start_time": 1599708642,
          "end_time": 1599712242
        },
        {
          "sub_meeting_id": "1599795042",
          "status": 0,
          "start_time": 1599795042,
          "end_time": 1599798642
        },
        {
          "sub_meeting_id": "1599881442",
          "status": 0,
          "start_time": 1599881442,
          "end_time": 1599885042
        },
        {
          "sub_meeting_id": "1599967842",
          "status": 0,
          "start_time": 1599967842,
          "end_time": 1599971442
        }
      ],
      "recurring_rule": {
        "recurring_type": 0,
        "until_type": 1,
        "until_count": 7
      },
      "meeting_type": 1,
      "has_more_sub_meetings": 0,
      "remain_sub_meetings": 5,
      "current_sub_meeting_id": "1599622242",
      "enable_live":true,
      "live_config":{
            "live_subject":"test",
            "live_summary":"test", 
            "live_password":"654321",
            "enable_live_im":true,
            "enable_live_replay":true,
            "live_addr":"https://meeting.tencent.com/l/xxxx"
        }
    }
  ]
}
```
