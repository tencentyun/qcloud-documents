## 事件描述
**事件名：**meeting.phone.participant-status-updated
**事件说明：**当 PSTN 外呼的状态发生变化时，触发该事件。

## 示例
```plaintext
{
    "event":"meeting.phone.participant-status-updated",// 事件名
    "trace_id":"e7aa65dd-f7e6-4b62-912c-2035173b34a9",// 事件的唯一序列值
    "payload":[       
        {
             "operate_time":1609313201465,//毫秒级别事件操作时间戳
             "operator":{ //事件操作者
                 "userid":"tester",//事件操作者id（同企业用户才返回用户id，OAuth用户返回openId,rooms返回roomsId）
                 "open_id":"KM4Ss******gUw1JiK",
                 "ms_open_id":"WMfgHRYj6m36mcDGtK",//用户会中身份ID
                 "user_name":"tester_name",//事件操作者名称
                 "instance_id":"2"//用户的终端设备类型
             },
             "meeting_info":{// 会议信息
                 "meeting_id":"13339451618278424869",// 会议ID
                 "meeting_code":"445999969",// 会议code
                 "subject":"tester-2的快速会议",// 会议主题
                 "meeting_type":0,// 会议类型(0-一次性会议，1-周期性会议，2-微信专属会议，4-rooms投屏会议，5-个人会议号会议)
                 "start_time":1608522626,//秒级别的会议开始时间戳
                 "end_time":1609415039,//秒级别的会议结束时间戳
                 "meeting_create_mode":0 //会议创建类型 0:普通会议；1:快速会议
            },
			"status":"START_ACCEPT"
        }
    ]
}
```

<table>
   <tr>
      <th width="0%" >status</td>
      <th width="0%" >含义</td>
   </tr>
   <tr>
      <td>START_INVITE</td>
      <td>开始邀请。</td>
   </tr>
   <tr>
      <td>START_ACCEPT</td>
      <td>用户接听。</td>
   </tr>
   <tr>
      <td>LEAVE_WITHOUT_ACCEPT</td>
      <td>用户无接听挂断，目前无法区分无接听挂断与拒绝，后续 PSTN 云线路支持后再考虑区分。</td>
   </tr>
   <tr>
      <td>LEAVE_WITH_ACCEPTED</td>
      <td>用户已接听挂断</td>
   </tr>
   <tr>
      <td>CANCLE_INVITE</td>
      <td>呼叫中邀请人主动取消，已接听后主持人挂断 pstn 则为 kickout 事件。</td>
   </tr>
</table>
