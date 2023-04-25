该部分内容将接口中常见 ID 汇总列出，字段使用条件请详见具体接口字段描述。

| 参数 | 参数描述 | 
|---------|---------|
|AppId |腾讯会议分配给企业的企业ID。企业管理员可以登录 [腾讯会议官网](https://meeting.tencent.com/)，单击右上角**用户中心**，在左侧菜单栏中的**企业管理** > **高级** > **restApi** 中进行查看。 |
|SdkId  |用户子账号或开发的应用 ID，企业管理员可以登录 [腾讯会议官网](https://meeting.tencent.com/)，单击右上角**用户中心**，在左侧菜单栏中的**企业管理 > 高级 > restApi**中进行查看（如存在 SdkId 则必须填写，早期申请 API 且未分配 SdkId 的客户可不填写）。 |
| instanceid | 终端设备类型。目前包括以下类型：<br>1：APP - PC<br>2：APP - Mac<br>3：APP - Android<br>4：APP - iPhone<br>5：Web<br>6：APP - iPad<br>7：APP - Apad<br>8：小程序<br>9：voip、sip 设备<br>10：APP - linux<br>20：Rooms for Touch Windows<br>21：Rooms for Touch MacOS<br>22：Rooms for Touch Android<br>30：Controller for Touch Windows<br>32：Controller for Touch Android<br>33：Controller for Touch iOS  | 
| userid | 企业内用户的唯一 ID，以所属企业为维度，表示同一企业内成员的唯一标识，不同企业间的 userid 隔离。<br>企业唯一用户标识说明：<br>1. 企业对接 SSO 时使用的员工唯一标识 ID。<br>2. 企业调用创建用户接口时传递的 userid 参数。 | 
| open_id | 用户经过 OAuth2.0 授权后的唯一 ID，以所属应用为维度，表示同一应用内用户的唯一标识，不同应用间 open_id 隔离。 | 
| ms_open_id | 会议中为每个参会成员授予的临时 ID，以会议为维度，表示同一场会议内用户的唯一标识，不同会议间 ms_open_id 隔离。<br>ms_open_id 可通过 [获取参会成员列表](https://cloud.tencent.com/document/product/1095/42701)、[查询实时会中成员列表](https://cloud.tencent.com/document/product/1095/72810)、[查询等候室成员记录](https://cloud.tencent.com/document/product/1095/80579)、[查询 ms_open_id-API](https://cloud.tencent.com/document/product/1095/74998) 等接口获取，PSTN 接通的用户可通过 [查询 PSTN 的 ms_open_id](https://cloud.tencent.com/document/product/1095/80578) 接口获取。 | 
| rooms_id | 会议室的唯一 ID，对外的会议室唯一标识，可在管理平台 > 会议室管理中查看。 | 
| meeting_room_id | 会议室的唯一 ID，API 内会议室唯一标识，可通过查询设备列表接口获取。 | 
| uuid | 用户身份 ID，腾讯会议颁发的用于开放平台的唯一用户 ID（使用创建用户接口时返回的 uuid）。<br><b>注意：</b>即将废弃，推荐使用 ms_open_id | 
| operator_id_type | 接口操作者 ID 的类型。目前包括以下类型：<br>1：userid<br>2：open_id<br>3：rooms_id<br>4：ms_open_id<br>5：meeting_room_id | 
| operator_id | 接口操作者 ID，与 operator_id_type 配合使用，根据 operator_id_type 的类型不同，operator_id 表示的含义不同。 | 
| to_operator_id_type | 接口被操作者 ID 的类型。目前包括以下类型：<br>1：userid<br>2：open_id<br>3：rooms_id<br>4：ms_open_id<br>5：meeting_room_id  | 
| to_operator_id | 接口被操作者 ID，与 to_operator_id_type 配合使用，根据 to_operator_id_type 的类型不同，to_operator_id 表示的含义不同。 | 
| meeting_type   | 会议类型。    <br>0：一次性会议<br>1：周期性会议<br>2：微信专属会议<br>3：Rooms 投屏会议<br>5：个人会议号会议<br>6：网络研讨会     |
