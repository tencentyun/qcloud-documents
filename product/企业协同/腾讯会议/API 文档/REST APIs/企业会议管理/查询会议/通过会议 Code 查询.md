## 接口描述
描述：用于会议 Code 查询会议详情。
调用方式：GET
接口请求域名：`https://api.meeting.qq.com/v1/meetings?meeting_code={meetingCode}&userid={userid}&instanceid={instanceid}`

## 输入参数

以下请求参数列表仅列出了接口请求参数，HTTP 请求头公共参数请参见签名验证章节的 [公共参数说明](https://cloud.tencent.com/document/product/1095/42413#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)。

| 参数名称 | 必选 | 参数类型 |参数描述 |
|---------|---------|---------|---------|
|meetingCode | 是 | String |有效的9位数字会议号码。|
|userid | 是 | String |调用方用于标示用户的唯一 ID（例如企业用户可以为企业账户英文名、个人用户可以为手机号等）。|
|instanceid | 是 | Integer |用户的终端设备类型： <br>1 - PC <br>2 - Mac<br>3 - Android <br>4 - iOS <br>5 - Web <br>6 - iPad <br>7 - Android Pad <br>8 - 小程序|

## 输出参数

| 参数名称 |参数类型 | 参数描述 |
|---------|---------|---------|
| meeting_number | integer | 会议数量。  |
|meeting_info_list  | [Array](#Array) | 会议列表。  |


<span id="Array"></span>
**会议对象**

| 参数名称 |参数类型 | 参数描述 |
|---------|---------|---------|
|subject  |String | 会议主题。  |
|meeting_id   |String| 会议的唯一标示 。  |
|meeting_code    |String| 会议 App 的呼入号码。  |
|password   |String | 会议密码。  |
|status|String|当前会议状态：<br>MEETING_STATE_INVALID：非法或未知的会议状态，错误状态<br>  MEETING_STATE_INIT：会议的初始状态，表示还没有人入会<br>  MEETING_STATE_CANCELLED：会议已取消<br> MEETING_STATE_STARTED：会议已开始，有人入会<br>MEETING_STATE_ENDED：会议已结束|
|hosts   |String 数组 | 会议主持人列表 。  |
|participants  |String数组|邀请的参会者 。|
|start_time  |String | 会议开始时间戳（单位秒）。 |
|end_time  |String | 会议结束时间戳（单位秒）。 |
|settings   |[会议媒体参数对象](#settings) |会议的配置，可为缺省配置。|

<span id="settings"></span>
**会议媒体参数对象**

| 参数名称 |参数类型 | 参数描述 |
|---------|---------|---------|
|mute_enable_join  |Bool | 加入静音状态。  |
|meeting_info_list  |Bool| 静音自解除允许 。  |

## 示例
#### 输入示例

```http
GET https://api.meeting.qq.com/v1/meetings?meeting_code=806146667&userid=tester1&instanceid=1
```

#### 输出示例

```
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
      "hosts": [        
        "tester"      
      ],      
      "participants": [        
        "test1"      
      ],      
      "join_url": "https://wemeet.qq.com/w/5NmV29k",      
      "settings": {        
        "mute_enable_join": true,        
        "allow_unmute_self": false      
      }    
    }  
  ]
}
```
