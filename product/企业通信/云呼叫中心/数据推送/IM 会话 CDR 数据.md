URL：`https://{custom_url}?action=imcdr&version=1`
METHOD: `POST`
Content-Type: `application/json;charset=utf8`
REQUEST:

| 参数                   | 类型      | 说明                                              |
| -------------------- | ------- | ----------------------------------------------- |
| SdkAppId             | 数值(长整型） | 呼叫中心实例 ID                                        |
| SessionId            | 字符串     | 会话 ID                                            |
| StartTimestamp       | 数值(长整型） | 整个会话开始时间戳（UNIX 秒级时间戳）                            |
| QueuedTimestamp      | 数值(长整型） | 会话进入排队时间戳（UNIX 秒级时间戳）                            |
| RingTimestamp        | 数值(长整型） | 会话首次振铃时间戳（UNIX 秒级时间戳）                            |
| AcceptTimestamp      | 数值(长整型） | 会话首次应答时间戳（UNIX 秒级时间戳）                            |
| EndedTimestamp       | 数值(长整型） | 会话整体结束时间戳（UNIX 秒级时间戳）                            |
| QueuedSkillGroupId   | 数值      | 会话进入排队技能组 ID                                     |
| QueuedSkillGroupName | 字符串     | 会话进入排队的技能组名称                                    |
| Duration             | 数值      | 会话整体服务时间，单位秒 EndedTimestamp-AcceptTimestamp     |
| IVRDuration          | 数值      | IVR 阶段持续时长，单位秒，QueuedTimestamp - StartTimestamp |
| EndStatusString      | 字符串     | 结束状态，枚举值见下表                                    |
| UserId               | 字符串     | 用户 ID                                           |
| UserNickName         | 字符串     | 用户昵称                                            |
| IVRKeyPressed        | 字符串数组   | IVR 按键信息 （e.g. \["1","2","3"\])                  |
| SeatUser             | 对象      | 客服信息，格式见下                                       |
| UserRemark           | 字符串     | 用户备注                                            |
| Satisfaction         | 对象      | 满意度信息{"id":"104","content":"满意"}                |
| ClientData           | 字符串     | 客户端关联数据                                         |

EndStatusString 枚举值

| 参数            | 说明         |
| ------------- | ---------- |
| ok            | 正常结束       |
| seatGiveUp    | 坐席未接       |
| seatForward   | 坐席转接       |
| ivrGiveUp     | IVR 期间用户放弃  |
| ivrEnd        | IVR 后直接结束   |
| autoFinished  | 用户回答超时自动结束 |
| ringingGiveUp | 会话振铃期间用户放弃 |
| noSeatOnline  | 无坐席在线      |
| notWorkTime   | 非工作时间      |
| error         | 系统错误       |

SeatUser 数据格式

| 参数                 | 类型    | 说明        |
| ------------------ | ----- | --------- |
| Mail               | 字符串   | 坐席邮箱      |
| Name               | 字符串   | 坐席名称      |
| Nick               | 字符串   | 坐席昵称      |
| Phone              | 字符串   | 坐席电话号码    |
| UserId             | 字符串   | 用户 ID      |
| StaffNumber        | 字符串   | 坐席工号      |
| SkillGroupNameList | 字符串数组 | 坐席所属技能组列表 |

RESPONSE：

| 参数      | 类型  | 说明   |
| ------- | --- | ---- |
| ErrMsg  | 字符串 | 错误说明 |
| ErrCode | 数值  | 错误码  |

<dx-codeblock>
:::  json
{
    "SdkAppId":1400xx214,
    "SessionId":"e97be0ab-1ef6-4ad2-a8c4-2b2bbfb18e55",
    "QueuedSkillGroupId":1072,
    "StartTimestamp":1608130636,
    "QueuedTimestamp":1608130638,
    "RingTimestamp":1608130639,
    "AcceptTimestamp":0,
    "EndedTimestamp":1608130651,
    "Duration":15,
    "EndStatusString":"error",
    "UserId":"oZB6q5c-tuMEz-ZiHOAkhW59a4AI",
    "UserNickName":"小君君",
    "IVRKeyPressed":null,
    "Satisfaction":{"id":"104","content":"满意"},
    "SeatUser":{
        "Mail":"lululing@tencent.com",
        "Name":"lululing",
        "Nick":"璐璐",
        "Phone":"",
        "UserId":"lululing@tencent.com",
        "StaffNumber":"007",
        "SkillGroupNameList":[
            "lulu"
        ]
    },
    "ClientData":"dGhpcyBpcyBhIGV4YW1wbGVhZGZhc2RmYXNkZg=="
}

:::
</dx-codeblock>
