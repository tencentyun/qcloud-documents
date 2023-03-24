


在游戏中，即时通信需求很常见，在多人游戏中即时聊天也成为了必不可少的功能。由于游戏平台本身所涉及到的多种群组类型、自定义消息类型（如游戏内道具赠送、交易等业务）、全球接入等需求往往比较复杂，本文梳理了在搭建游戏聊天时过程中常见的需求的实现方法，以及可能遇到的问题、需要注意的细节等，希望能帮助开发者们快速的理解业务，实现需求。
![](https://qcloudimg.tencent-cloud.cn/raw/41bda125b2276c6d70bfa8de480e8748.jfif)

## 准备工作

### 使用密钥计算 UserSig

在 IM 的账号体系中，用户登录需要的密码由用户服务端使用 IM 提供的密钥计算，用户可参见 [UserSig计算](https://intl.cloud.tencent.com/document/product/1047/34385) 文档，在开发阶段，为了不阻塞客户端开发，也可在 [控制台计算 UserSig](https://console.cloud.tencent.com/im/tool-usersig) ，如下图所示：

![](https://qcloudimg.tencent-cloud.cn/raw/3ebfcc9b831fac31ad9b8b722bb7dc50.png)

### 配置管理员账号

在管理游戏内即时通信过程中，可能需要管理员向游戏发送邮件公告、管理临时组队消息等，这时就需要使用 [即时通信 IM 服务端 API](https://intl.cloud.tencent.com/document/product/1047/34621) 来进行相应的处理，调用服务端api前需要 [创建 IM 管理员账号](https://console.cloud.tencent.com/im/account-management)，IM 默认提供一个 UserID 为 administrator 的账号供开发者使用，开发者也可以根据业务的场景，创建多个管理员账号。需要注意的是，IM 最多创建五个管理员账号。

### 配置回调地址以及开通回调

在实现游戏内组队等需求时，需要用到 IM 的回调模块，即 IM 后台在某些特定的场景回调开发者业务后台。开发者只需要提供一个 HTTP 的接口并且配置在 [控制台 > 回调配置](https://console.cloud.tencent.com/im/callback-setting) 模块即可，如下图所示：

![](https://qcloudimg.tencent-cloud.cn/raw/365705a8a72a1e15ec5259e164beeb06.png)

### 集成客户端 SDK

在准备工作都完成好后，需要将即时通信 IM 客户端 SDK 集成到用户项目中去。开发者可以根据自己业务需要，选择不同的集成方案。可参见 [快速集成系列文档](https://intl.cloud.tencent.com/document/product/1047/34547)。

接下来文章梳理了游戏中集成IM时常见的功能点，提供最佳实践方案供开发者参见，并附上相关实现代码。

## 游戏聊天室各功能开发指引

### 用户资料

#### 常见用户资料
游戏业务中保存的常见用户资料可分为基本信息资料和其他信息资料。

|基本信息|其他信息|
|---|---|
|用户名，性别，生日，等级，角色，手机号等|其他游戏内需要的资料|

#### 资料存储
游戏业务内有众多的用户，而存储庞大的用户资料也是较大的难点。腾讯云 IM 开放了用户资料托管能力，提供资料相关的一套完整解决方案。下面对比保存到 腾讯云 IM 与保存到业务后台的区别。

|对比项|IM|业务后台|
|---|---|---|
|存储容量|可自动扩容/缩容|容量有限，增减容量较困难|
|用户资料|提供标配字段和自定义字段，字段的长度和命名有限制|可自行定义，更加灵活|
|资料读写|提供简单易用的服务接口和帮助指引|需自行开发|
|接口|有调用接口频率限制：最高200次/秒|接口调用等能力可按照自己需求自行开发|
|安全性|可异地容灾、多地部署|需自行维护|

综上，使用 IM 用户资料托管服务除可获得资料的存储、读写能力外还有以下优点：
1. IM 提供异地容灾、多地部署和自动扩容/缩容的能力，帮助您从服务器宕机、多拷贝主从复制和扩容缩容等复杂处理流程中得到完全地解放。
2. IM 提供业界通用的业务处理流程，帮助您在用户资料的业务逻辑上彻底地解放。
3. IM 提供专业的运营流程和运营团队，全年99.99%的稳定服务质量，帮助您为用户提供具有稳定口碑的服务。
4. IM 提供简单易用的服务接口和快捷接入的帮助指引，全程为您提供星级服务。

#### IM 存储用户资料的方式
IM 存储方案包含资料的存储和其读写能力。下面介绍 IM 存储用户资料、好友资料和拓展资料的方式。所有资料均以`Key-Value` 形式表示。其中`Key` 为`String`类型，仅支持英文大小写字母、数字、下划线。`Value`有以下几种类型：

|类型|说明|
|---|---|
|uint64_t|整数（自定义字段不支持）|
|string|字符串，长度不得超过500字节|
|bytes|一段 buffer，长度不得超过500字节|
|string 数组|字符串数组，每个字符串长度不得超过500字节，仅供好友表的 Tag_SNS_IM_Group  字段使用|

- **用户资料**：用户资料包含标配字段和自定义字段。自定义字段可见下文的拓展资料。目前即时通信 IM 支持的用户资料标配字段可参见 [用户资料标配资料字段](https://cloud.tencent.com/document/product/269/1500#.E6.A0.87.E9.85.8D.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5)。
- **好友资料**：好友资料支持标配好友字段和自定义好友字段。即时通信 IM 好友列表最多允许添加3000个好友。其中，标配好友字段如下：
<table>
<thead>
<tr>
<th>字段名称</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>Tag_SNS_IM_Group</td>
<td>Array</td>
<td>好友分组，为字符串数组</td>
</tr>
<tr>
<td>Tag_SNS_IM_Remark</td>
<td>string</td>
<td>好友备注</td>
</tr>
<tr>
<td>Tag_SNS_IM_AddSource</td>
<td>string</td>
<td>加好友来源</td>
</tr>
<tr>
<td>Tag_SNS_IM_AddWording</td>
<td>string</td>
<td>加好友附言</td>
</tr>
<tr>
<td>Tag_SNS_IM_AddTime</td>
<td>Integer</td>
<td>加好友时间戳</td>
</tr>
</tbody></table>
更详细内容请参见 <a href="https://cloud.tencent.com/document/product/269/1501#.E6.A0.87.E9.85.8D.E5.A5.BD.E5.8F.8B.E5.AD.97.E6.AE.B5">好友标配字段</a>。
- **自定义资料**：自定义资料字段可以通过即时通信 [IM 控制台](https://console.cloud.tencent.com/im) > 应用配置 > 功能配置 申请，提交申请后，自定义资料字段将在5分钟内生效。
 - 更多关于用户资料管理，请参见 [用户资料管理](https://cloud.tencent.com/document/product/269/1500)。
 - 更多关于好友关系链自定义资料管理，请参见 [好友自定义字段](https://cloud.tencent.com/document/product/269/1501#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.A5.BD.E5.8F.8B.E5.AD.97.E6.AE.B5)。

#### IM 用户资料存储限制
- **业务特性限制**
 - 存储数据：string 和 buffer 类型的恶存储长度不得超过500字节
 - 自定义字段：自定义字段的关键字必须是英文字母且长度不得超过8字节，自定义字段的值最长不能超过500字节
 - 好友关系链：单个用户支持3000个好友
- **接口相关限制**
 - 账号管理：单次最多倒入100个用户名，一次请求最多可以查询500个用户状态
 - 其他调用频率：最高200次/秒

更多关于使用限制请参见 [使用限制](https://cloud.tencent.com/document/product/269/32429)。

### 邮件系统

现在游戏中，邮件系统几乎是必备的功能。邮件包含文字消息，也可以包含游戏道具、奖励等邮件附件。邮件可以发送给一个人、也可以像发放活动奖励群发邮件 。下面从玩家接收邮件、邮件列表、邮件未读计数、全员邮件、邮件有效期等几个方面详细介绍邮件系统的功能实现。

#### 收发邮件

- **玩家接收邮件**：当系统邮件发送成功并且玩家正处联网状态时，玩家能够正确接收到系统邮件。接收到的邮件可通过获取邮件会话的消息列表取得历史/最新邮件，同时可以增加/删除接收新消息的回调监听接收所有类型的消息（包含文本、自定义、富媒体消息等）。以Unity为例的示例代码如下所示：
```javascript
// 设置接收消息事件监听器
TencentIMSDK.AddRecvNewMsgCallback((List<Message> messages, string user_data)=>{
  foreach(Message message in messages)
  {
    foreach (Elem elem in message.message_elem_array)
    {
      // 有下一个消息
      if (elem.elem_type == TIMElemType.kTIMElem_Text)
      {
         string text = elem.text_elem_content;
      }
    }
  }
})
// 监听 `RecvNewMsgCallback`回调，在其中接受消息
// 希望停止接收消息，调用 `RemoveRecvNewMsgCallback`移除监听。该步骤非必需，可按照业务需求调用。
```
关于更多有关内容请参见 [Unity-接收消息](https://cloud.tencent.com/document/product/269/76657)。
- **系统发送邮件**：系统向用户发系统邮件可以通过 服务端 API 的几种方式，下面列出不同方法的特点：
<table>
<thead>
<tr>
<th>方法</th>
<th>特点</th>
<th>应用场景</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/269/2282">单发单聊消息</a></td>
<td>向指定账号发消息，接收方看到的发送者不是管理员，而是管理员指定的账号</td>
<td>向某个特定用户发送消息，如段位赛奖励等</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/269/1612">批量发单聊消息</a></td>
<td>支持一次最多对500个用户单发消息，最高调用频率为200次/秒</td>
<td>向某些特定用户发送消息，因无需创建组使用比较灵活，但若发送用户较多则需要分批发送</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/269/1629">在群组中发送普通消息</a></td>
<td>向群组发送普通消息，需要将用户添加到同一个组内</td>
<td>向较多用户发送消息可以系统创建群组发送普通消息，群组最大人数限制为 社交群(community) 10万人</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/269/45933">全员推送服务</a></td>
<td>向 App 内全员推送消息，可指定用户标签和属性发送消息</td>
<td>向 App 内全员推送消息或人数非常多且有特征属性时可使用，如活动推送邮件等</td>
</tr>
</tbody></table>
<dx-alert infotype="explain" title="">
“全员推送” 为 IM 旗舰版功能，需 [购买旗舰版套餐包](https://buy.cloud.tencent.com/avc?from=17182) 并在 [控制台](https://console.cloud.tencent.com/im/login-message) > 功能配置 > 登录与消息 > 全员推送设置，打开开关后方可使用。
</dx-alert>
其中，在群组中发送普通消息的请求包基础形式示例如下所示：
```json
{
    "GroupId": "@TGS#2C5SZEAEF",
    "Random": 8912345, // 随机数字，五分钟数字相同认为是重复消息
    "MsgBody": [ // 消息体，由一个 element 数组组成，详见字段说明
        {
            "MsgType": "TIMTextElem", // 文本
            "MsgContent": {
            "Text": "red packet"
            }
        },
        {
            "MsgType": "TIMCustomElem", // 自定义
            "MsgContent": {
            "Data": "message",
            "Desc": "notification",
            "Ext": "url",
            "Sound":"dingdong.aiff"
            }
        }
    ],
}
```
`MsgBody`（消息体）为一个消息数组，可以将文本消息和自定义消息放入 MsgBody 中发送消息。

#### 邮件列表

历史邮件列表存储同消息存储，可分为 `C2C 单聊历史消息存储` 和 `群聊历史消息存储`。由于群聊最小人数为2人，可以将管理者指定账号与收到邮件的用户创建新的组进行存储。

>? 体验版和专业版存储时长为7天，旗舰版为 30 天。专业版和旗舰版支持延长时长。您可登录 [控制台](https://console.cloud.tencent.com/im) 修改相关配置。
> 延长历史消息存储时长是付费增值服务，具体计费说明请参见 [增值服务资费](https://www.tencentcloud.com/zh/document/product/1047/34350)。


在网络正常下会拉取最新的云端数据，若网络异常则返回本地存储的历史消息。本接口支持分页拉取。拉取历史邮件列表的 Unity 示例代码如下：
```javascript
// 拉取单聊历史消息
// 首次拉取，msg_getmsglist_param_last_msg 设置为 null
// 再次拉取时，msg_getmsglist_param_last_msg 可以使用返回的消息列表中的最后一条消息
var get_message_list_param = new MsgGetMsgListParam
{
    msg_getmsglist_param_last_msg = LastMessage
};
TIMResult res = TencentIMSDK.MsgGetMsgList(conv_id, TIMConvType.kTIMConv_C2C, get_message_list_param, (int code, string desc, string user_data) => {
// 处理回调逻辑
});
```
更多拉取历史消息内容，请参见 [历史消息-Unity](https://cloud.tencent.com/document/product/269/76658)。

#### 邮件未读计数

一个用户-系统邮件的记录相当于一个聊天中的会话。腾讯云 IM 提供会话未读计数功能，提醒用户尚未阅读消息。用户点进该会话后退回会话列表时，未读消息数会被清空。Unity示例代码如下：
```javascript
// 获取全部未读数
TIMResult res = TencentIMSDK.ConvGetTotalUnreadMessageCount((int code, string desc, GetTotalUnreadNumberResult unread, string user_data)=>{
 // 处理异步逻辑
});

// 未读计数变更通知
TencentIMSDK.SetConvTotalUnreadMessageCountChangedCallback((int total_unread_count, string user_data)=>{
 // 处理回调逻辑
});

// 清空所有会话的未读消息数
TIMResult res = TencentIMSDK.MsgMarkAllMessageAsRead((int code, string desc, string user_data)=>{
 // 处理异步逻辑
});
```
更多内容请参见 [Unity-会话未读消息数](https://cloud.tencent.com/document/product/269/76676)。

#### 全员邮件
全员邮件相当于对游戏内所有玩家发送邮件消息。腾讯云 IM 提供服务端`全员推送`功能。示例代码如下：
```
https://console.tim.qq.com/v4/all_member_push/im_push?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json
```
请求包示例如下：
```json
{
    "From_Account": "admin",
    "MsgRandom": 56512,
    "MsgLifeTime": 120, // 离线保存120s（2分钟）
    "MsgBody": [
        {
        "MsgType": "TIMTextElem",
        "MsgContent": {
            "Text": "hi, beauty"
            }
        }
    ]
}
```

全员推送可以设置消息离线存储时间，这样即便某些用户不在线，但在离线存储的时间范围内，不在线用户也能收到消息。若需要设置离线保存时间，可设置`MsgLifeTime`，单位秒，最多保存7天（604800s）。默认为0，表示不离线存储。

更多相关全员推送的内容请参见 [全员推送](https://cloud.tencent.com/document/product/269/45934)。

#### 邮件有效期
对于历史邮件，邮件存储有效期为：体验版/专业版为7天，旗舰版为30天，专业版和旗舰版支持延长时长。对于历史存储的更多内容请参见 [历史消息存储时长配置](https://cloud.tencent.com/document/product/269/38656#.E5.8E.86.E5.8F.B2.E6.B6.88.E6.81.AF.E5.AD.98.E5.82.A8.E6.97.B6.E9.95.BF.E9.85.8D.E7.BD.AE)。
此外，在服务端发送消息时，可通过在请求包内设置 `MsgLifeTime` 设置消息离线保存时长（最长为7天）。若该字段为0，则表示消息只发在线用户，不离线保存。 更多内容请参见 [服务端 API](https://cloud.tencent.com/document/product/269/2282)。

### 临时组队

多人联网游戏中临时组队必不可少。下面从组队场景和后台、队伍内成员分别所需获取的队内信息讲解临时组队的内容。

[](id:Team_scene)
#### 组队场景

组队场景一般分为如下几点：创建组队、退出临时组队、成为队长、邀请加入组队、解散组队等。下面通过一些代码示例分别解释不同场景的实现方法。

- **游戏开始前创建组队**：当第一个人进入游戏时，在服务端自动创建群组并可以设置最大群成员数量。请求时如果指定了群组或群成员，那么在创建时群主或群成员回自动加入到该群中。请求 URL 示例如下：
```
https://console.tim.qq.com/v4/group_open_http_svc/create_group?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```
请求包基础形式示例如下：
```json
{
    "Owner_Account": "leckie", // 群主的 UserId（选填）
    "Type": "Public", // 群组类型：Private/Public/ChatRoom/AVChatRoom/Community
    "Name": "TestGroup", // 群名称（必填）
    "MaxMemberCount":5 // 最大群成员数量（选填）
}
```
>? App 中 同时存在的所有群组数量最多为10万，若超过10万则需要支付一定费用。详情请参见 [价格说明](https://cloud.tencent.com/document/product/269/11673)。更多关于服务端创建群组请参见 [创建群组](https://cloud.tencent.com/document/product/269/1615)。
- **增加群成员**：创建群聊后后续有新的玩家进入游戏则需要在原来群组的基础上添加新的群成员。请求 URL 示例如下：
```
https://console.tim.qq.com/v4/group_open_http_svc/add_group_member?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```
请求包如下：
```json
{
    "GroupId": "@TGS#2J4SZEAEL", // 要操作的群组（必填）
    "MemberList": [ // 一次最多添加300个成员
        {
            "Member_Account": "tommy" // 要添加的群成员ID（必填）
        },
        {
            "Member_Account": "jared"
    }]
}
```
更多内容请参见 [增加群成员](https://cloud.tencent.com/document/product/269/1621)。
- **组队成功回调**：当在创建群组时设置了最大群成员数量，则当组队需要人数全部进群后可以开始游戏。可以通过`群组满员之后回调`感知并开始游戏。请求 URL 示例如下：
```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```
请求包示例如下：
```json
{
    "CallbackCommand": "Group.CallbackAfterGroupFull", // 回调命令
    "GroupId": "@TGS#2J4SZEAEL" // 群组 ID
}
```
更多相关内容请参见 [群组满员之后回调](https://cloud.tencent.com/document/product/269/1669)。
- **新成员入群通知**：当有新的玩家进入游戏（群聊）后，通过 `新成员入群之后回调` 可通知其他群成员入群成功。请求 URL 示例如下：
```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```
请求包示例如下：
```json
{
    "CallbackCommand": "Group.CallbackAfterNewMemberJoin", // 回调命令
    "GroupId" : "@TGS#2J4SZEAEL",
    "Type": "Public", // 群组类型
    "JoinType": "Apply", // 入群方式：Apply（申请入群）；Invited（邀请入群）
    "Operator_Account": "leckie", // 操作者成员
    "NewMemberList": [ // 新入群成员列表
        {
            "Member_Account": "jared"
        },
        {
            "Member_Account": "tommy
        }
    ]
}
```
>? 要启用回调，必须配置回调URL，并打开本条回调协议对应的开关。配置方法参见 [第三方回调配置](https://cloud.tencent.com/document/product/269/32431) 文件。更多相关内容请参见 [新成员入群之后回调](https://cloud.tencent.com/document/product/269/1667)。
>
- **游戏途中退出组队**：当玩家自主退出游戏或由于网络问题退出游戏时，服务端可以通过 `群成员离开之后回调`通知组内其他玩家有人退出群聊，也可以对因网络问题退出游戏的玩家发送消息。[群成员离开之后回调](https://cloud.tencent.com/document/product/269/1668) 的请求 URL 示例如下：
```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json&ClientIP=$ClientIP&OptPlatform=$OptPlatform
```
请求包示例如下：
```json
{
    "CallbackCommand": "Group.CallbackAfterMemberExit", // 回调命
    "GroupId": "@TGS#2J4SZEAEL", // 群组 ID
    "Type": "Public", // 群组类型
    "ExitType": "Kicked", // 成员离开方式：Kicked-被踢；Quit-主动退群
    "Operator_Account": "leckie", // 操作者
    "ExitMemberList": [ // 离开群的成员列表
        {
            "Member_Account": "jared"
        },
        {
            "Member_Account": "tommy"
        }
    ]
}
```
- **游戏结束后解散群聊**：游戏结束后，服务端可直接解散群聊。[解散群聊](https://cloud.tencent.com/document/product/269/1624) 的请求 URL 示例如下：
```
https://console.tim.qq.com/v4/group_open_http_svc/destroy_group?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```
请求包示例如下：
```json
{
    "GroupId": "@TGS#2J4SZEAEL"
}
```
对于临时组队内语音或视频聊天，内容比较复杂，下文有详细说明。

#### 后台获取队内情况

- **获取群内详细信息**：对于群内详细信息（包含当前群成员数量，群内成员基本信息等）可以通过服务端 API `获取群详细资料`获取。可以在请求包中设定Filter字段拉取置顶的信息。示例代码如下所示：
```
https://console.tim.qq.com/v4/group_open_http_svc/get_group_info?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```
请求包示例如下：
```json
{
    "GroupIdList": [ // 群组列表（必填）
        "@TGS#1NVTZEAE4",
        "@TGS#1CXTZEAET"
    ]
}
```
更多详细信息请参见 [获取群详细资料](https://cloud.tencent.com/document/product/269/1616)。
- **获取群成员详细信息**：若只需要群成员信息（包含自定义字段），则可使用`获取群成员详细资料`获取到群成员的信息。示例代码如下所示：
```
https://console.tim.qq.com/v4/group_open_http_svc/get_group_member_info?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```
请求包示例如下：
```json
{
    "GroupId":"@TGS#1NVTZEAE4"  // 群组 ID（必填）
}
```
返回字段中 `MemberNum` 可获取本群组的群成员总数，`AppMemberDefinedData` 可获取群成员自定义字段信息。
>? 该接口不支持直播群（AVChatRoom）。更多详细信息请参见 [获取群成员详细资料](https://cloud.tencent.com/document/product/269/1617)。


#### 队内成员获取队内情况

对于队内成员，可通过 `获取群成员资料` 获取到队内其他成员的资料，如成员的角色、准备状态等。示例代码如下：
```java
GroupGetMemberInfoListParam param = new GroupGetMemberInfoListParam
{
  group_get_members_info_list_param_group_id = "group_id",
  group_get_members_info_list_param_identifier_array = new List<string>
  {
    "user_id"
  }
};
TIMResult res = TencentIMSDK.GroupGetMemberInfoList(param, (int code, string desc, GroupGetMemberInfoListResult result, string user_data)=>{
 // 处理异步逻辑
});
```
>?
>- 详细内容请参见 [Unity-获取群成员资料](https://cloud.tencent.com/document/product/269/76683) 。
>- 其他关于群信息如`群满员开始游戏`、`有成员加入/退出组队`等可参见  [组队场景](#Team_scene) 并使用回调通知到群内。
>- 更多有关群组选择和关于群组的其他事项，请参见 [群组系统](https://cloud.tencent.com/document/product/269/1502) 。更多有关**群组管理的控制台指南**，请参见 [群组管理控制台指南](https://cloud.tencent.com/document/product/269/38657)。

### 敏感信息过滤
在游戏场景中，用户很可能会发送不合适的内容，特别是与敏感事件/人物相关、黄色不良内容等令人反感的内容，不仅严重损害了用户们的身心健康，更很有可能违法并导致应用被监管部门查封。

即时通信 IM 支持内容审核（反垃圾信息）功能，可针对不安全、不适宜的内容进行自动识别、处理，为您的产品体验和业务安全保驾护航。可以通过以下两种内容审核方式来实现：
- [本地审核功能](https://cloud.tencent.com/document/product/269/83795#bdsh)：在客户端本地检测在单聊、群聊、资料场景中由即时通信 SDK 发送的文本内容，支持对已配置的敏感词进行拦截或者替换处理。此功能通过在 IM 控制台开启服务并配置词库的方式实现。
- [云端审核功能](https://cloud.tencent.com/document/product/269/83795#ydsh)：在服务端检测由单聊、群聊、资料场景中产生的文本、图片、音频、视频内容，支持针对不同场景的不同内容分别配置审核策略，并对识别出的不安全内容进行拦截。此功能已提供默认预设拦截词库和审核场景，只需在 IM 控制台打开功能开关，即可直接使用。


### 自定义消息类型（如道具赠送、交易）

在游戏聊天环境中，不仅只使用文本消息、表情消息、语音消息等简单的消息类型。自定义消息类型可提供开发者自定义客制化消息内容格式的功能，可通过自定义消息类型完成游戏聊天室内游戏道具的赠送、交易等更多的聊天室功能。

腾讯云 IM 提供 9 种基本消息类型，包含文本消息、表情消息、地理位置消息、图片消息、语音消息、文件消息、短视频消息、系统通知和自定义消息。其中除了自定义消息之外的其他消息格式已经确定，只需要填入相应的信息即可。更多关于消息类型的具体描述请参见 [消息类型](https://cloud.tencent.com/document/product/269/3662)，关于消息类型的格式请参见 [消息格式描述](https://cloud.tencent.com/document/product/269/2720)。

服务端可通过 [单发单聊消息](https://cloud.tencent.com/document/product/269/2282) 、 [批量发单聊消息](https://cloud.tencent.com/document/product/269/1612) 、 [在群组中发送普通消息](https://cloud.tencent.com/document/product/269/1629) 向用户发送自定义消息。在群组中发送普通消息的基础请求包示例如下：

```json
{
    "GroupId": "@TGS#2C5SZEAEF",
    "Random": 8912345, // 随机数字，五分钟数字相同认为是重复消息
    "MsgBody": [ // 消息体，由一个 element 数组组成，详见字段说明
        {
            "MsgType": "TIMTextElem", // 文本
            "MsgContent": {
                "Text": "red packet"
            }
        },
        {
            "MsgType": "TIMFaceElem", // 表情
            "MsgContent": {
            "Index": 6,
            "Data": "abc\u0000\u0001"
            }
        }
    ],
    "CloudCustomData": "your cloud custom data",
    "SupportMessageExtension": 0,
}
```

其中，可以修改`CloudCustomData`定义消息自定义数据（云端保存），并将自定义消息填入`MsgBody` （消息体）发送。

### 组内语音/视频聊天

游戏内的语音/视频聊天也是一项很重要的功能。腾讯云 IM 提供即时通信 IM 和 [实时音视频品视频 TRTC](https://cloud.tencent.com/document/product/647) 音视频通话功能（TUICallKit），为 IM 聊天提供实时的音频通话或视频通话。

>? 
>- 为了更好的体验音视频通话功能，我们为每个 SDKAppID 提供了音视频通话能力7天体验版。您可以在 IM [控制台](https://console.cloud.tencent.com/im) 中为您的应用领取体验版进行体验使用，每个 SDKAppID 有且仅有一次领取体验版的机会。
>- 更多有关集成音视频通话能力和价格，详情请见 [音视频通话](https://cloud.tencent.com/document/product/269/82462)。更多关于 TUICallKit 的内容，请参见 [含 UI 集成方法-音视频通话](https://cloud.tencent.com/document/product/269/72445)。


### 游戏聊天室类型

游戏聊天室类型一般分为如下几种：

| 类型 | 特点 |
| --- | --- |
| 频道 | 聊天人数非常多，无固定成员列表，无需申请加入群聊，可随时加入、退出。无需发送离线消息推送。 |
| 大厅 | 聊天人数较多，可随时加入、退出。支持历史消息查询。 |
| 组队 | 聊天人数较少，聊天对象可能为陌生人，游戏结束时聊天室销毁。无需发送离线消息推送。 |
| 好友 | 为 C2C 聊天，聊天记录保存，聊天对象存在于好友列表。 |
| 私信 | 为 C2C 聊天，聊天对象可能为陌生人。 |
| 直播群 | 聊天人数无上限，可随时加入、退出。 |

IM 提供的聊天室类型分为以下几种：

| 类型 | 特点 |
| --- | --- |
| 好友工作群（work） | 类似普通微信群，创建后仅支持已在群内的好友申请加群，无需被邀请访同意或群组审批。 |
| 陌生人社交群（Public） | 类似 QQ 群，创建后群主可以指定群主管理员，用户搜索群ID发起群申请后，需要群主或管理员审批通过才能入群。 |
| 临时会议群（Meeting） | 创建后可以随意进出，且支持查看入群前消息；适合用于音视频会议场景、在线教育场景等与实时音视频产品结合的场景，同旧版本中的 ChatRoom。 |
| 直播群（AVChatRoom） | 创建后可以随意进出，没有群成员数量上限，但不支持历史消息存储；适合与直播产品结合，用于弹幕聊天场景。 |
| 社群（Community） | 创建后可以随意进出，最多支持10w人，支持历史消息存储，用户搜索群 ID 发起加群申请后，无需管理员审批即可进群。 |

根据 IM 的群特性，这里提供示例解决方案，请按照需求应用到您的游戏中：

| 类型 | 解决方案 | 特点 |
| --- | --- | --- |
| 频道、大厅 | 社群（Community） | 聊天人数较多，创建后可随意进出，无需审批 |
| 好友 | 单聊+权限控制（只允许给好友发送消息） | 支持仅好友发送消息 |
| 私信 | 单聊+权限控制（App 内任意两个用户之间发送单聊消息） | 支持任意两个陌生人发送消息 |
| 组队 | 陌生人社交群（Public）、临时会议群（Meeting） | 只有游戏内组队人员能够进入聊天群，支持音视频聊天 |
| 直播群 | 直播群（AVChatRoom） | 没有群成员上线，可随时进出群 |

>?
> - 关于好友聊天和私信聊天的单聊权限控制请参见 [单聊消息权限控制](https://cloud.tencent.com/document/product/269/3662#.E5.8D.95.E8.81.8A.E6.B6.88.E6.81.AF.E6.9D.83.E9.99.90.E6.8E.A7.E5.88.B6%EF%BC%89)。
> - 更多群组系统相关内容请参见 [群组系统](https://cloud.tencent.com/document/product/269/1502)。
