

## 接口说明
**请求方式**：POST。
```shell
https://api.tpns.tencent.com/v3/push/app
```
>?广州服务接入点:
```shell
https://api.tpns.tencent.com/v3/push/app
```
香港服务接入点:
```shell
https://api.tpns.hk.tencent.com/v3/push/app
```
新加坡服务接入点:
```shell
https://api.tpns.sgp.tencent.com/v3/push/app
```


**接口功能**：Push API 是所有推送接口的统称。Push API 有多种推送目标，推送目标见下文。
所有请求参数通过 JSON 封装上传给后台，后台通过请求参数区分不同的推送目标。如有疑问请参见 [服务端错误码](https://cloud.tencent.com/document/product/548/39080)。



## 参数说明
### 请求参数

#### 必要参数

推送必要参数指一条推送消息必需携带的参数。

| 参数名           | 类型     | 是否必需 | 描述                                       |
| ------------- | ------ | ---- | ---------------------------------------- |
| audience_type | string | 是    | 推送目标：<li>all：全量推送</li><li>tag：标签推送</li><li>token：单设备推送</li><li>token_list：设备列表推送</li><li>account：单账号推送</li><li>account_list：账号列表推送</li> |
| message       | object | 是    | 消息体，请参见 [消息体类型](#消息体类型) |
| message_type  | string | 是    | 消息类型：<li>notify：通知</li><li>message：透传消息/静默消息</li> |
| environment   | string  | 是（仅 iOS 平台使用）                |  用户指定推送环境，仅限 iOS 平台推送使用：<li>product： 推送生产环境</li><li>dev： 推送开发环境</li> |
| upload_id   | int32  | 是（仅号码包推送使用）                | 号码包上传 ID  |


#### audience_type：推送目标

推送目标，表示一条推送可以被推送到哪些设备。
Push API 提供了多种推送目标的，例如全量、标签、单设备、设备列表、单账号、账号列表。

| 推送目标     | 描述         | 必需参数及使用说明                                           |
| ------------ | ------------ | ------------------------------------------------------------ |
| all          | 全量推送     | 无                                                           |
| tag          | 标签推送     | `tag_list`<li>推送 tag1 和 tag2 的设备`{"tags":["tag1","tag2"],"op":"AND"}`</li><li>推送 tag1 或 tag 的设备`{"tags":["tag1","tag2"],"op":"OR"}`</li><li> 标签列表不能超过512个字符</li> |
| token        | 单设备推送   | `token_list`<li>如果该参数包含多个 token 只会推送第一个 token</li><li>格式 eg：[“token1”]</li><li>token 字符串长度不能超过36</li> |
| token_list   | 设备列表群推 | `token_list`<li>最多1000 个token</li><li>格式 eg：["token1","token2"]</li><li>token 字符串长度不能超过36</li> |
| account      | 单账号推送   | `account_list`<li>该参数有多个账号时，仅推送第一个账号</li><li>格式 eg：["account1"] </li>|
| account_list | 账号列表群推 | `account_list`最多1000 个account2. 格式 eg：["account1","account2"] |
|package_account_push | 号码包推送 | 上传号码包推送必填 |

- 全量推送：推送给全部设备
  ```json
  {
    "audience_type": "all"
  }
```
- 标签推送：推送给同时设置了 tag1 和 tag2 标签的设备

 ```json
  {
    "audience_type": "tag",
    "tag_list": {
        "tags": [
            "tag1",
            "tag2"
        ],
        "op": "AND"
    }
  }
```

- 单设备推送：推送给 token 为 token1 的设备
  ```json
  {
    "audience_type": "token",
    "token_list": [
        "token1"
    ]
  }
```

- 设备列表推送，推送给 token 为 token1 和 token2 的设备
  ```json
  {
    "audience_type": "token_list",
    "token_list": [
        "token1",
        "token2"
    ]
  }
```
  
- 单账号推送：推送给账号为 account1 的设备
  ```json
  {
    "audience_type": "account",
    "account_list": [
        "account1"
    ]
  }
```

- 账号列表推送：推送账号为 account1 和 account2 的设备
  ```json
  {
    "audience_type": "account_list",
    "account_list": [
        "account1",
        "account2"
    ]
  }
```

<span id="消息体类型"></span>
#### message_type：消息体类型

针对不同平台，消息类型稍有不同，具体参照下表：


| 消息类型 | 描述       | 支持平台      | 特性说明       |
| -------- | ---------- | ------------- | -------------- |
| notify   | 通知栏消息 | Android & iOS | 通知栏展示消息 |
| message | 透传消息/静默消息 | Android（透传消息）<br>iOS（静默消息） | 通知栏不展示消息因厂商限制，Android 透传消息只通过自建通道下发，无法通过厂商通道下发|

#### message：消息体

消息体，即下发到客户端的消息。

Push API 对 iOS 和 Android 两个平台的消息有不同处理，需要分开来实现对应平台的推送消息，推送的消息体是 JSON 格式。

#### Android 普通消息

Android 平台具体字段如下表：

| 字段名            | 类型     |   父项目 | 默认值  | 必需   | 参数描述                                     |
| -----               | ------   | ----       |-----      |    ---- | ----------- ------------------------ |
| title                | string  |       message       | 无          | 是        | 消息标题  |                                   |
| content        | string | message       |无    | 是    | 消息内容                                     |
| accept_time    | jsonArray  | message       |无    | 否    | 消息将在哪些时间段允许推送给用户。单个元素由"start" 和"end" 组成的起止时间对组成。"start" 和 "end" 由 hour （小时）和 min（分钟）描述对应时刻，详细参考具体示例。⚠️因厂商限制， 仅对自建通道有效。                 |
| xg_media_resources    | string  | message       |无    | 否    | 图片富媒体元素地址 ⚠️因厂商限制，包含富媒体的推送不能通过厂商通道下发，全部通过自建通道下发 |
| xg_media_audio_resources    | string  | message       |无    | 否    | 音频富媒体元素地址，支持 mp3 格式音频，建议大小在5M以内<br>⚠️因厂商限制，包含富媒体的推送不能通过厂商通道下发，全部通过自建通道下发 |
| android              | JSON  | message      |无     |否    | 安卓通知高级设置结构体，可参考 Android 结构体说明|

#### Android 结构体说明

| 字段名            | 类型     |   父项目 | 默认值  | 必需   | 参数描述                                     |
| -----           | ------   | ----       |-----      |    ---- | ----------- ------------------------    |
| n_ch_id     | string    | Android      |无    | 否    | 通知渠道id（仅对自建通道生效），请参见 [创建通知渠道](https://cloud.tencent.com/document/product/548/36659#.E5.88.9B.E5.BB.BA.E9.80.9A.E7.9F.A5.E6.B8.A0.E9.81.93)                                 |
| n_ch_name     | string    | Android      |无    | 否    | 通知渠道名称 （仅对自建通道生效） ，请参见 [创建通知渠道](https://cloud.tencent.com/document/product/548/36659#.E5.88.9B.E5.BB.BA.E9.80.9A.E7.9F.A5.E6.B8.A0.E9.81.93)                                    |
| n_id           | int    | Android       |0    | 否    | 通知消息对象的唯一标识（仅对自建通道生效）<li>大于0：会覆盖先前相同 ID 的消息<li>等于0：展示本条通知且不影响其他消息<li>等于-1：将清除先前所有消息，仅展示本条消息 |
| builder_id     | int    | Android      |0    | 否    | 本地通知样式标识                                 |
| ring           | int    |Android      |1    | 否    | 是否有铃声<li>0：没有铃声<li>1：有铃声             |
| ring_raw       | string |Android     | 无    | 否    | 指定 Android 工程里 raw 目录中的铃声文件名，不需要后缀名          |
| vibrate        | int    | Android       |1    | 否    | 是否使用震动<li>0：没有震动<li>1：有震动            |
| lights         | int    |Android       |1    | 否    | 是否使用呼吸灯<li>0：不使用呼吸灯<li>1：使用呼吸灯       |
| clearable      | int    | Android      |1    | 否    | 通知栏是否可清除                                 |
| icon_type      | int    | Android      |0    | 否    | 通知栏图标是应用内图标还是上传图标<li>0：应用内图标<li>1：上传图标 |
| icon_res       | string | Android       |无    | 否    | 应用内图标文件名或者下载图标的 url 地址                     |
| style_id       | int    | Android       |1    | 否    | 设置是否覆盖指定编号的通知样式                          |
| small_icon     | string | Android      |无    | 否    | 消息在状态栏显示的图标，若不设置，则显示应用图标                 |
| action         | JSON   | Android       |有    | 否    | 设置点击通知栏之后的行为，默认为打开 App   |
| action_type| int | Action      |有    | 否    | 点击动作类型，<li>1：打开 activity 或 App 本身<li>2：打开浏览器<li>3：打开 Intent             |
| custom_content | string | Android   |无    | 否    | 用户自定义的参数， ⚠️需要序列化为 json string       |


完整的消息示例如下：

```json
{
    "title": "xxx",
    "content": "xxxxxxxxx",
    "xg_media_resources": "xxx1" , //此处填富媒体元素地址，例如https://www.xx.com/img/bd_logo1.png?qua=high
    "xg_media_audio_resources":"xxx", //此处填音频富媒体元素地址，例如http://sc1.111ttt.cn/2018/1/03/13/396131227447.mp3 

    "accept_time": [
        {
            "start": {//时间段起始时间，
                "hour": "13",//起始时间 小时值, 取值 [0:24)
                "min": "00"// 起始时间 分钟值, 取值[0:60)
            },
            "end": {//时间段结束时间
                "hour": "14",//结束时间 小时值, 取值 [0:24)
                "min": "00" //结束时间 分钟值,取值[0:60)

            }
        },
        {
            "start": {
                "hour": "00",
                "min": "00"
            },
            "end": {
                "hour": "09",
                "min": "00"
            }
        }
    ],
    "android": {
		"n_ch_id": "default_message",
		"n_ch_name": "默认通知",
        "n_id": 0,
        "builder_id": 0,
        "ring": 1,
        "ring_raw": "ring",
        "vibrate": 1,
        "lights": 1,
        "clearable": 1,
        "icon_type": 0,
        "icon_res": "xg",
        "style_id": 1,
        "small_icon": "xg",
        "action": {
            "action_type": 1,// 动作类型，1，打开activity或app本身；2，打开浏览器；3，打开Intent
            "activity": "xxx",
            "aty_attr": {// activity属性，只针对action_type=1的情况
                "if": 0, // Intent的Flag属性
                "pf": 0  // PendingIntent的Flag属性
            },
            "browser": {
                "url": "xxxx ", // 仅支持http、https
                "confirm": 1 // 是否需要用户确认
            },
            "intent": "xxx" //SDK版本需要大于等于1.0.9，然后在客户端的intent配置data标签，并设置scheme属性
        },
      "custom_content":"{\"key\":\"value\"}"
    }
}
```

#### iOS 普通消息

iOS 平台具体字段如下表：


| 字段名    | 类型          |  父项目 |默认值  | 必需   | 参数描述                                     |
| ------ | ----------- | ---- || ---- | ---------------------------------------- |
| ios    | JSON       |message  | 无    | 是    | iOS 消息结构体，请参考 iOS 字段说明  |
| xg_media_resources    | array     | message | 无    | 否    | 富媒体元素地址                          |
| xg     | string     |message | 无    | 否    | 系统保留 key，应避免使用            |



#### ios 字段说明

| 字段名    | 类型     |  父项目      | 默认值  | 必需   | 参数描述                                     |
| ------ | ----------- | |---- | ---- | ---------------------------------------- |
| aps   | JSON       |ios | 无    | 是    | 苹果推送服务（APNs）特有的消息体字段，详细介绍请参见 [Payload](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/PayloadKeyReference.html#//apple_ref/doc/uid/TP40008194-CH17-SW1)|
| alert   | JSON       |aps | 无    | 是    | 包含标题和消息内容 |
| badge_type  | int   |   aps  | 无    | 否    | App 显示的角标数 |
| category  | string    |    aps| 无    | 否    | 下拉消息时显示的操作标识 |
| mutable-content | int |     aps | 无    | 否    | 通知拓展参数，推送的时候携带 "mutable-content":1 说明是支持 iOS10 的 Service Extension，开启后，推送详情中会有抵达数据上报，使用该功能前请按照集成文档开发相应模块，如果不携带此字段则没有抵达数据上报。|
| sound  | string     | aps| 无    | 否    |sound 字段使用情况如下：<br>1：播放系统默认提示音，"sound":"default"<br>2：播放本地自定义铃声，"sound":"chime.aiff"<br>3：静音效果，"sound":"" 或者是去除 sound 字段自定义铃声说明：格式必须是 Linear PCM、MA4（IMA/ADPCM）、alaw，μLaw 的一种，将声频文件放到项目 bundle 目录中，且时长要求30s以下，否则就是系统默认的铃声。|
| custom_content | string |ios | 无    | 否    | 自定义下发的参数，需要序列化为 json string                                |


完整的消息示例如下：

```json
{
    "title": "xxx",
    "content": "xxxxxxxxx",
    "ios":{
        "aps": {
            "alert": {
                "subtitle": "my subtitle"
            },
            "badge_type": 5,
            "category": "INVITE_CATEGORY",
            "sound":"default",
            "mutable-content":1
        },
       "custom_content":"{\"key\":\"value\"}",
        "xg": "oops"
    }
}
```

#### Android 透传消息

透传消息，Android 平台特有，即不显示在手机通知栏中的消息，可以用来实现让用户无感知的向 App 下发带有控制性质的消息。

>!因厂商限制，Android 透传消息只通过自建通道下发，无法通过厂商通道下发。

Android 平台具体字段如下表：

| 字段名            | 类型    | 父项目| 默认值  | 是否必需 | 参数描述                     |
| -------------- | ------ || ---- | ---- | ------------------------ |
| title          | string |message| 无    | 是    | 命令描述                     |
| content        | string |message| 无    | 是    | 命令内容                    |
| android              | JSON  | message      |无     |否    | 安卓消息结构体|
| custom_content | string | android  | 无    | 否    | 需要序列化为 json string                    |
| accept_time    | array | message| 无    | 否    | 消息将在哪些时间段允许推送给用户。单个元素由"start" 和"end" 组成的起止时间对组成。"start" 和 "end" 由 hour （小时）和 min（分钟）描述对应时刻，详细参考具体示例。⚠️因厂商限制， 仅对自建通道有效。  |

具体完整示例：

```json
{
    "title": "this is title",
    "content": "this is content",
    "android": {
      "custom_content":"{\"key\":\"value\"}"
    },
    "accept_time": [
        {
            "start": {
                "hour": "13",
                "min": "00"
            },
            "end": {
                "hour": "14",
                "min": "00"
            }
        },
        {
            "start": {
                "hour": "00",
                "min": "00"
            },
            "end": {
                "hour": "09",
                "min": "00"
            }
        }
    ]
}
```

#### iOS 静默消息

静默消息，iOS 平台特有，类似 Android 中的透传消息，消息不展示，当静默消息到达终端时，iOS 会在后台唤醒 App 一段时间（小于30s），让 App 来处理消息逻辑。

具体字段如下表：

| 字段名    | 类型          | 父项目 | 默认值  | 是否必要 | 参数描述                                     |
| ------ | -----------| | ---- | ---- | ---------------------------------------- |
| aps    | JSON       | ios  | 无    | 是    | 苹果推送服务（APNs）特有的，其中最重要的键值对如下：<br>content-available：标识消息类型（必须为1），且不能包含 alert、sound、badge_type 字段<br>详细介绍请参见 [Payload](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/PayloadKeyReference.html#//apple_ref/doc/uid/TP40008194-CH17-SW1) |
| ios    | JSON       |message  | 无    | 是    | ios 消息结构体  |
| custom_content | String | ios| 无    | 否    | 需要序列化为 json string                                 |
| xg     | string      | ios | 无    | 否    | 系统保留 key，应避免使用                            |



具体完整示例：
```json
{
    "ios":{
        "aps": {
            "content-available": 1
        },
      "custom_content":"{\"key\":\"value\"}",
        "xg": "oops"
    }
}
```

### 可选参数

Push API 可选参数是除了 `audience_type`、`message_type`、`message` 以外，可选的高级参数。

| 参数名           | 类型    | 父项目 | 必需               | 默认值     | 描述                                       |
| ------------- | ------- || ---------------- | ------- | ---------------------------------------- |
| expire_time| int     |无| 否                | 259200（72小时） | 消息离线存储时间（单位为秒）,最长72小时<li>若 expire_time=0，则表示实时消息<li>若 expire_time大于0，且小于800s，则系统会重置为800s<li>若expire_time>=800s，按实际设置时间存储，最长72小时 <li>设置的最大值不得超过2147483647，否则会导致推送失败|
| send_time     | string| 无 | 否                | 当前系统时间  | 指定推送时间：<li>格式为 yyyy-MM-DD HH:MM:SS<li>若小于服务器当前时间，则会立即推送<li>仅全量推送和标签推送支持此字段 |
| multi_pkg     | bool   |无 | 否                | false   | 多包名推送：当 App 存在多个不同渠道包（例如应用宝、豌豆荚等），推送时如果是希望手机上安装任何一个渠道的 App 都能收到消息那么该值需要设置为 true |
| loop_param | json | 无 | 否                | 0       | 循环推送（全推，标签推）相关，详情见下文 loop_param 字段说明 |
|badge_type     |int  |  iOS  |否                 |-1        | 用户设置角标数字，仅限 iOS 平台使用，放在 aps 字段内<li> -1：角标数字不变 <li> -2：角标数字自动加1 <li> >=0：设置自定义角标数字|
|group_id     |string   | 无  |否                 |tpns_yyyymmdd，yyyymmdd 代表推送日期        | 统计标签，用于聚合统计|
| tag_list      | object | 无| 仅标签推送必需          | 无       | <li>推送 tag1 和 tag2 的设备：`{"tags":["tag1","tag2"],"op":"AND"}`<li>推送 tag1 或 tag2 的设备： `{"tags":["tag1","tag2"],"op":"OR"}` |
| account_list  | array  |无 | 单账号推送、账号列表推送时必需  | 无       | 若单账号推送：<li>要求 `audience_type=account`<li>参数格式：["account1"]<br>若账号列表推送：<li>参数格式：`["account1","account2"]`<li>最多1000 个 account |
| account_push_type  | int  |  无 | 账号推送时可选         | 0       |<li> 0：往账号的最新的 device 上推送信息<li> 1：往账号关联的所有 device 设备上推送信息|
| token_list    | array   |无| 单设备推送、设备列表推送时必需  | 无       | 若单设备推送：<li>要求 audience_type=token<li>参数格式：["token1"]<br>若设备列表推送：<li>参数格式：["token1","token2"]<li>最多1000 个 token |
| push_speed   |int |无|  仅全量推送和标签推送有效|无| 推送限速设置每秒 X 条，X 取值参数范围 1000 - 50000|

#### loop_param 参数说明
| 字段名      | 类型      | 是否必填 | 注释                                       |
| -------- | ------- | ---- | ----------------------------------------          |
| startDate      | string | 是    | 循环区间开始日期，格式YYYY-MM-DD，如2019-07-01       |
| endDate | string   | 是    | 循环区间开始日期，格式YYYY-MM-DD，如2019-07-07|                 |
| loopType | int| 是 | 循环类型，1-按天， 2-按周， 3-按月 |
| loopDayIndexs | array | 是   | 按周循环，填周几[0-6]，按天填 0，如[0, 1, 2]，表示每周的周一，周二，周三进行推送                               |
| dayTimes   | array  | 是    | 具体推送时间， 格式 HH:MM:SS，如["19:00:00", "20:00:00"]，表示每天的19点，20点进行推送 |



### 应答参数

| 字段名      | 类型      | 是否必填 | 注释                                       |
| -------- | ------- | ---- | ----------------------------------------          |
| seq      | int64_t | 是    | 与请求包一致（如果请求包是非法 json 该字段为0）        |
| push_id | string   | 是    | 推送 ID |
| ret_code | int32_t | 是    | 错误码，详细参照错误码对照表                        |
| environment | string | 是 | 用户指定推送环境，仅支持 iOS<li>product： 生产环境<li>dev： 开发环境 |
| err_msg  | string  | 否    | 请求出错时的错误信息                               |
| result   | string  | 否    | 请求正确时<li>若有额外数据要返回，则结果封装在该字段的 json 中<li>若无额外数据，则可能无此字段 |



## 示例说明

#### Android 标签推送请求消息

```json
{
    "audience_type": "tag",
    "tag_list": {
        "tags": [
            "tag1",
            "tag2"
        ],
        "op": "AND"
    },
    "message_type": "notify",
    "message": {
    "title": "测试标题",
    "content": "测试内容",
    "xg_media_resources": "xxx1" , //此处填富媒体元素地址，例如https://www.xx.com/img/bd_logo1.png?qua=high
    "xg_media_audio_resources":"xxx", //此处填音频富媒体元素地址，例如http://sc1.111ttt.cn/2018/1/03/13/396131227447.mp3 
    "accept_time": [
        {
            "start": {//时间段起始时间，
                "hour": "13",//起始时间 小时值, 取值 [0:24)
                "min": "00"// 起始时间 分钟值, 取值[0:60)
            },
            "end": {//时间段结束时间
                "hour": "14",//结束时间 小时值, 取值 [0:24)
                "min": "00" //结束时间 分钟值,取值[0:60)

            }
        },
        {
            "start": {
                "hour": "00",
                "min": "00"
            },
            "end": {
                "hour": "09",
                "min": "00"
            }
        }
    ],
    "android": {
		"n_ch_id": "default_message",
		"n_ch_name": "默认通知",
        "n_id": 0,
        "builder_id": 0,
        "ring": 1,
        "ring_raw": "ring",
        "vibrate": 1,
        "lights": 1,
        "clearable": 1,
        "icon_type": 0,
        "icon_res": "xg",
        "style_id": 1,
        "small_icon": "xg",
        "action": {
            "action_type": 1,// 动作类型，1，打开activity或app本身；2，打开浏览器；3，打开Intent
            "activity": "xxx",
            "aty_attr": {// activity属性，只针对action_type=1的情况
                "if": 0, // Intent的Flag属性
                "pf": 0  // PendingIntent的Flag属性
            },
            "browser": {
                "url": "xxxx ", // 仅支持http、https
                "confirm": 1 // 是否需要用户确认
            },
            "intent": "xxx" //SDK版本需要大于等于1.0.9，然后在客户端的intent配置data标签，并设置scheme属性
        },
      "custom_content":"{\"key\":\"value\"}"
    }
}
}
```


#### 标签推送应答消息

```json
{
    "seq": 0,
    "environment": "product",
    "ret_code": 0,
    "push_id": "3895624686"
}
```
#### iOS 单设备推送请求消息

```json
{
    "audience_type": "token",
    "environment":"dev",
    "token_list": [ "05da87c0ae5973bd2dfa9e08d884aada5bb2"],
    "message_type":"notify",
    "message":{
     "title": "推送标题",
    "content": "推送内容",
    "ios":{
        "aps": {
            "alert": {
                "subtitle": "推送副标题"
            },
            "badge_type": -2,
            "sound":"Tassel.wav",
            "category": "INVITE_CATEGORY"

        },
       "custom_content":"{\"key\":\"value\"}",
        "xg": "oops"
    }
 }
}
```
#### 单设备推送应答消息

```json
{
    "seq": 0,
    "push_id": "427184209",
    "ret_code": 0,
    "environment": "dev",
    "err_msg": "",
    "result": "[0]"
}
```


