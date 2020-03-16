**GET      /v1/meetings?meeting_code={meetingCode}&userid={userid}&instanceid={instantceid}**
用会议ID查询一个会议内容
## Authorization
X-TC-Signature: {signature}
## HTTP Request Path 参数

| 参数名称 | 必选 | 参数类型 |参数描述 |
|---------|---------|---------|---------|
|meetingCode | 是 | String |有效的 9 位数字会议号码。|
|userid | 是 | String |调用 API 的用户 ID。|
|instanceid | 是 | Integer |用户的终端设备类型。|

## HTTP Request Body 参数
无
## HTTP Response 参数
HTTP Status Code: 200
和按会议ID查询相同。

## HTTP Response 示例

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
        "mumliu"      
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
