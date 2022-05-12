CDR 以整体会话为维度记录数据，一次客户的整体呼入或者呼出对应一条数据。CDR 的 root 层数据指标表示的是以客户为维度的会话全局信息。
会话服务中的具体细节轨迹通过 ServeParticipants 对象数组描述（如：电话转接等信息），ServeParticipants 每一条数据代表了一次服务轨迹。

呼出类型数据 QueuedSkillGroupID 字段选取策略：
1. 客服只属于一个电话技能组，则命中。
2. 客服属于多个电话技能组，优先选择外呼号码绑定的技能组（多个取第一个技能组）。
3. 不满足1、2，则取客服第一个电话技能组。

URL：`https://{custom_url}?action=cdr&version=1`
METHOD: `POST`
Content-Type: `application/json;charset=utf8`
REQUEST：

| 参数                 | 类型      | 说明                                              |
| ------------------ | ------- | ----------------------------------------------- |
| SdkAppId           | 数值(长整型） | 呼叫中心实例 ID                                        |
| SessionId          | 字符串     | 会话ID                                            |
| Direction          | 数值      | 会话整体方向，0 呼入 或 1 呼出                              |
| StartTimestamp     | 数值(长整型） | 整个会话开始时间戳（UNIX 秒级时间戳）                            |
| EndedTimestamp     | 数值(长整型） | 会话整体结束时间戳（UNIX 秒级时间戳）                            |
| QueuedSkillGroupId | 数值      | 会话进入排队技能组 ID                                     |
| Duration           | 数值      | 会话整体服务时间，单位秒 EndedTimestamp-AcceptTimestamp     |
| IVRDuration        | 数值      | IVR 阶段持续时长，单位秒，QueuedTimestamp - StartTimestamp |
| EndStatusString    | 字符串     | 会话整体结束状态，枚举值见下表。                                |
| HungUpSide         | 字符串     | 挂断方（user - 用户挂断 或 seat - 坐席挂断）                  |
| Caller             | 字符串     | 主叫方                                             |
| Callee             | 字符串     | 被叫方                                             |
| IVRKeyPressed      | 字符串数组   | IVR 按键信息 （e.g. \["1","2","3"\])                  |
| IVRKeyPressedEx    | 对象数组    | IVR 按键信息（e.g. \[{"Key":"1","Label":"非常满意"}\]）    |
| PostIVRKeyPressed  | 对象数组    | 后置 IVR 按键信息（e.g. \[{"Key":"1","Label":"非常满意"}\]）  |
| SeatUser           | 对象      | 客服信息，格式见下（如果发生转接则是最后一个客服信息)                     |
| ServeParticipants  | 对象数组    | 服务参与者列表，格式见下                                    |
| UserRemark         | 字符串     | 用户备注                                            |
| TelLocation        | Json 对象  | 号码归属地相关信息，格式见下                                  |
| Uui                | 字符串     | 随入数据（电话外呼接口客户带入的数据）                             |

EndStatusString 枚举值

| 参数              | 说明         |
| --------------- | ---------- |
| ok              | 正常结束       |
| unconnected     | 未接通        |
| seatGiveUp      | 坐席未接       |
| seatForward     | 坐席转接       |
| outboundForward | 外线转接       |
| ivrGiveUp       | IVR 期间用户放弃  |
| ivrEnd          | IVR 后直接结束   |
| waitingGiveUp   | 会话排队期间用户放弃 |
| ringingGiveUp   | 会话振铃期间用户放弃 |
| noSeatOnline    | 无坐席在线      |
| notWorkTime     | 非工作时间      |
| error           | 系统错误       |

呼出场景下特有 EndStatusString

| 参数             | 说明      |
| -------------- | ------- |
| unknown        | 未知状态    |
| notAnswer      | 未接听     |
| userReject     | 拒接挂断    |
| powerOff       | 关机      |
| numberNotExist | 空号      |
| busy           | 通话中     |
| outOfCredit    | 欠费      |
| operatorError  | 运营商线路异常 |
| callerCancel   | 主叫取消    |
| notInService   | 不在服务区   |

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

ServeParticipant 数据格式


| 参数                 | 类型      | 说明                                              |
| ------------------ | ------- | ----------------------------------------------- |
| Sequence           | 数值      | 参与者序号，从 0 开始                                    |
| Mail               | 字符串     | 坐席邮箱                                            |
| Phone              | 字符串     | 坐席电话                                            |
| StartTimestamp     | 数值(长整型） | 开始时间戳，Unix 秒级时间戳                                |
| RingTimestamp      | 数值(长整型） | 振铃时间戳，Unix 秒级时间戳                                |
| AcceptTimestamp    | 数值(长整型） | 接听时间戳，Unix 秒级时间戳                                |
| EndedTimestamp     | 数值(长整型） | 结束时间戳，Unix 秒级时间戳                                |
| Type               | 字符串     | 参与者类型，<li>staffSeat          </li><li>outboundSeat       </li><li>staffPhoneSeat     </li> |
| RecordId           | 字符串     | 录音 ID                                           |
| TransferFrom       | 字符串     | 转接来源坐席信息                                        |
| TransferTo         | 字符串     | 转接去向坐席信息                                        |
| TransferToType     | 字符串     | 转接去向参与者类型，取值与 Type 一致                           |
| SkillGroupId       | 数值      | 技能组 ID                                          |
| SkillGroupName     | 字符串     | 技能组名称                                           |
| SkillGroupPriority | 数值      | 技能组分配优先级                                        |
| EndStatusString    | 字符串     | 结束状态                                            |

TelLocation 数据格式

| 参数        | 类型  | 说明  |
| --------- | --- | --- |
| TelNumber | 字符串 | 号码  |
| Country   | 字符串 | 国家  |
| Province  | 字符串 | 省份  |
| City      | 字符串 | 城市  |
| Operator  | 字符串 | 运营商 |

RESPONSE：

| 参数      | 类型  | 说明   |
| ------- | --- | ---- |
| ErrMsg  | 字符串 | 错误说明 |
| ErrCode | 数值  | 错误码  |

数据样例：
<dx-codeblock>
:::  json
{
    "SdkAppId":1400xxx214,
    "SessionId":"e97be0ab-1ef6-4ad2-a8c4-2b2bbfb18e55",
    "QueuedSkillGroupId":1072,
    "Direction":1,
    "StartTimestamp":1608130636,
    "RingTimestamp":1608130639,
    "AcceptTimestamp":0,
    "EndedTimestamp":1608130651,
    "Duration":15,
    "Duration":0,
    "EndStatusString":"error",
    "HungUpSide":"seat",
    "Caller":"008602066247698",
    "Callee":"008618621520280",
    "IVRKeyPressed":null,
    "PostIVRKeyPressed":[
        {
            "key":"1",
            "label":"非常满意"
        }
    ],
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
    "ServeParticipants":[
        {
            "Mail":"lululing@tencent.com",
            "Phone":"",
            "RecordId":"1608130636",
            "StartTimestamp":1608130636,
            "RingTimestamp":1608130639,
            "AcceptTimestamp":0,
            "EndedTimestamp":1608130651,
            "Type":"staffSeat"
        }
    ]
}

:::
</dx-codeblock>
