本文档描述互动课堂后端接口，客户通过使用下述接口为组件提供必要信息，并获取组件的运行状况，在使用云 API 进行上课时请先进行账号注册。

## 账号模块
###  创建账号
####  接口
- 接口名称：`/user/register`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/user/register?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| list | Array | 需要注册的用户列表 | 是 | - |
| user_id | string | 用户 ID | 是 | - |
| password | string | 密码，长度4-18，规则：数字/大小写字母/特殊字符(!@#$%^&*()-+=.[]{}:;,?/) | 是 |-
| role | string | 用户角色 | 是 | - |
| nickname | string | 用户昵称 | 否 | 用户 ID |
| gender | string | 用户性别 | 否 | 男 |
| avatar | string | 头像的 URL 地址，头像规则参考附录 | 否 | 互动课堂后台随机选择一个头像 |
| phone_no | string | 手机号 | 否 |- |
| e_mail | string | 邮箱 | 否 | -|

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| user_list | Array |创建成功后，每个用户对应生成一个 user_token，用于唤起组件 | 是 | 空数组 |
| user_token | string | 用户票据，每个用户 ID 对应一个 user_token，等同于控制台的密码 | 是 | - |
| repeats | Array | 出现重复 ID 时，会报错，且返回重复 user_id 列表 | 是 | 空数组 |

#### 举例
请求：
```
{
  "list":[
    {
      "user_id":"xxxxx",
      "password":"12345",
      "role":"student",
      "nickname":"小明",
      "gender":"male",
      "avatar":"https://xxx/xiaoming.png", 
      "phone_no":"13033445566",
      "e_mail":"xxx@xx.com"
    }
  ]
}
```
响应：
```
{
  "error_code":0,
  "error_msg":"",
  "user_list":[
    {
      "user_id":"user1",
      "user_token":"1234578"
    }
  ],
  "repeats":["xx","yy"]
}
```

### 修改账号信息
####  接口
- 接口名称：`/user/profile/modify`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/user/profile/modify?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| user_id | string | 用户 ID | 是 | - |
| role | int | 角色 | 否 | - |
| nickname | string | 昵称 | 否 | - |
| gender | string | 用户性别 | 否 | - |
| avatar | string | 头像的 URL 地址 | 否 | - |
| phone_no | string | 手机号 | 否 | - |
| e_mail | string | 邮箱 | 否 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

#### 举例
需要修改哪个字段，就在请求体中设置该字段的值，不需要修改的字段，不要在请求体中设置。
本例修改用户昵称。
请求：
```
{
  "user_id":"xxxx",
  "nickname":"新昵称"
}
```
响应：
```
{
  "error_code":0,
  "error_msg":""
}
```


### 更新账号票据
####  接口
- 接口名称：`/user/token/update`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/user/token/update?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| user_id | string | 用户 ID | 是 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| user_token | string | 新的用户票据 | 是 | - |

#### 举例
请求：
```
{
  "user_id":"xxxx"
}
```
响应：
```
{
  "error_code":0,
  "error_msg":"",
  "user_token":"新的票据"
}
```

### 查询用户详情
####  接口
- 接口名称：`/user/info`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/user/info?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| user_id | string | 用户 ID | 是 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| user_info | Object | 用户对象 | 是 | - |
| user_id | string | 用户 ID | 是 | - |
| nickname | string | 用户昵称 | 是 | - |
| gender | string | 用户性别 | 是 | - |
| avatar | string | 用户头像 | 是 | - |
| role | string | 用户角色 | 是 | - |
| phone_no | string | 用户电话 | 是 | - |
| e_mail | string | 用户邮箱 | 是 | - |
| regist_time | string | 用户注册时间 | 是 | - |
| update_time | string | 用户信息最后一次修改时间 | 是 | - |

#### 举例
请求：
```json
{
  "user_id":"用户ID"
}
```
响应：
```json
{
  "error_code":0,
  "error_msg":"",
  "user_info":{
    "user_id":"user1",
    "nickname":"user1_nickname",
    "gender":"male",
    "avatar":"https://xxxx/head.png",
    "role":"student",
    "phone_no":"15888667799",
    "e_mail":"xx@xx.com",
    "regist_time":1554786131,
    "update_time":1554786131
  }
}
```

### 查询用户列表
####  接口
- 接口名称：`/user/list`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/user/list?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| index | int | 分段拉取分页索引 | 否 | 0
| size | int | 分段拉取分页大小（最大100） | 否 | 100
| roles | Array | 用户角色，用作过滤（不填此字段或字段为空数组均获取所有角色） | 否 | 所有角色
| prefix | string | 用户 ID 的前缀，用做模糊过滤 | 否 | 空字符串

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| finish | bool | 是否拉取完所有用户 | 是 | - |
| total | string | 用户总数 | 是 | - |
| list | Array | 用户数组 | 是 | 空数组 |
| user_id | string | 用户 ID | 是 | - |
| role | string | 用户角色 | 是 | - |
| nickname | string | 用户昵称 | 是 | - |
| gender | string | 用户性别 | 是 | - |
| avatar | string | 用户头像 URL | 是 | - |
| phone_no | string | 用户电话 | 是 | - |
| e_mail | string | 用户邮箱 | 是 | - |
| regist_time | int64 | 用户注册时间 | 是 | - |
| update_time | int64 | 用户最后一次更新时间 | 是 | - |

#### 举例

获取所有角色为老师的用户。
请求：
```json
{
  "index":0,
  "size":10,
  "roles":["teacher"],
  "prefix":""
}
```
响应：
```json
{
  "error_code":0,
  "error_msg":"",
  "total":1,
  "finish":true,
  "list":[
    {
      "user_id":"user1",
      "nickname":"user1_nickname",
      "gender":"male",
      "avatar":"https://xxxx/head.png",
      "role":"teacher",
      "phone_no":"15888667799",
      "e_mail":"xx@xx.com",
      "regist_time":1554786131,
      "update_time":1554786131
    }
  ]
}
```


本文档描述互动课堂后端接口，客户通过使用下述接口为组件提供必要信息，并获取组件的运行状况。

## 课堂模块
### 预约课堂
#### 接口
- 接口名称：`/class/create`
- 接口方法： `POST`
- Content-Type：`application/json`
- 接口 URL： `https://iclass.api.qcloud.com/paas/v1/class/create?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| teacher_id | string | 教师 ID | 是 | - |
| assistant_id | string | 助教 ID | 否 | - |
| class_topic | string | 课堂主题/课堂名字 | 否 | 课堂 ID 的字符串形式 |
| start_time | int64 | 课堂预计开始时间戳 | 否 | 约课时的时间 | 
| stop_time | int64 | 课堂预计结束时间戳 | 否 | start_time + 2小时 |
| password | string  | 进房密码 | 否 | -|
| admin_id | string | 即时通信 IM 管理员 ID，互动课堂用它来创建 IM 群组 | 否 | - |
| admin_sig | string | 即时通信 IM 管理员 Sig，互动课堂用它来创建 IM 群组 | 否 | - |
| settings | settings | 课堂配置信息 | 否 |- |
| resolution | string | 设置课堂的分辨率（320x240/800x600/1024x768）  | 否 | 1024x768 |
| fps | int | 设置课堂的帧率| 否 | 15 |
| auto_create_im | int | 是否由后台创建并管理 IM 群组，并记录 IM 历史消息（0-不创建/1-创建），若要开启服务端录制则改字段必填为1| 否 | 1 |
| record_types | Array | 字符串数组，选定录制类型，如果填写了`remote`，<br>在开始上课时，会自动开启服务端录制 | 否 | local | 
| auto_open_mic  | int | 是否自动打开麦克风（0-不打开/1-打开）| 否 | 0 |
| auto_open_camera  | int | 是否自动打开摄像头（0-不打开/1-打开）| 否 | 0 |
| enable_all_silence  | int | 是否开启了全员禁言（0-否/1-是）| 否 | 0 |
| bitrate | int | 设置课堂的码率| 否 | 850 |
| layout | int | 课堂的布局风格（具体参见 Layout 附录）| 否 | 0 |
| members | Array | 课堂预约成员列表 | 否 |  教师 ID 默认在成员列表中 |
| role | string | 角色信息，本接口中全部填“student”。需要设置 members 时此字段必填 | 否 | - |
| user_id | string | 学生 ID。需要设置 members 时此字段必填 | 否 | - |
| max_member_limit | int |最大上麦人数| 否 | - |
| max_member_num|int|课堂允许进入的最大人数，0表示无限制|否|false|
| screen_resolution |string | 设置屏幕分享的分辨率（320x240/800x600/1280x720）| 否|默认1280x720 |
| screen_fps|int |设置屏幕分享的帧率 |否 |默认15 |
| screen_bitrate| int|设置屏幕分享码率(400,900,1500) |否 | 默认1200 |
 
>?screen_resolution、screen_fps、screen_bitrate 这三个参数必须要按组填写，仅如下组合才能在控制台展示出来。
```
  '720p': {
    resolution: '1280x720',
    fps: 5,
    bitrate: 800
  },
  '720p_2': {
    resolution: '1280x720',
    fps: 10,
    bitrate: 1200
  },
  '720p_3': {
    resolution: '1280x720',
    fps: 15,
    bitrate: 1200
  },
  '1080p': {
    resolution: '1920x1080',
    fps: 5,
    bitrate: 1600
  },
  '1080p_2': {
    resolution: '1920x1080',
    fps: 10,
    bitrate: 1600
  },
  '1080p_3': {
    resolution: '1920x1080',
    fps: 15,
    bitrate: 1600
  }
```


#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| class_id | int | 课堂 ID | 否 | - |
| url | string | 进房地址，成功时下发 | 否 | - |

#### 举例

请求：
```
{
  "teacher_id":"user_00",
  "assistant_id":"user_01",
  "class_topic": "课堂主题",
  "start_time": 1558350988,
  "stop_time": 1558350988,
  "admin_id":"即时通信IM管理员ID",
  "admin_sig":"即时通信IM管理员鉴权sig",
  "max_member_limit":6,
  "max_member_num": 0,
  class_live_type:"window",
  "members": [
    {
      "role": "student",
      "user_id": "user1"
    },
    {
      "role": "student",
      "user_id": "user2"
    }
  ],
  "settings":{
    "record_types": ["local","remote"],
    "resolution": "1024x768",
    "fps": 20,
    "record_types": ["local","remote"],
    "auto_create_im": 1,
    "bitrate": 850,
    "layout": 1,
    "auto_open_mic": 0,
    "auto_open_camera": 0,
    "enable_all_silence":0

  }
}
```

响应：
```
{
  "error_code":0,
  "error_msg":"",
  "class_id":100012345,
  "url":"https://tedu.qcloudtrtc.com/#/class/100001/100012345",
}
```

###  删除
#### 接口
- 接口名称：`/class/delete`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/class/delete?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

#### 举例
请求：
```
{
  "class_id": 100012345
}
```
响应：
```
{
  "error_code":0,
  "error_msg":""
}
```

### 修改课堂信息
#### 接口
- 接口名称：`/class/modify`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/class/modify?公共参数`

#### 请求参数
修改课堂的参数字段与创建课堂相同，需要修改哪个字段，就在请求体中设置该字段。不需要修改的字段，不要带在请求体中。**class_id 不可修改；members 是全量修改，如果要增量修改，请参考成员模块中的`添加预约成员`接口**。

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

#### 举例
修改课堂主题和课堂结束时间。
请求：
```json
{
  "class_id": 102304,
  "class_topic": "新的课堂主题",
  "stop_time": 1558351000
}
```

响应：
```json
{
  "error_code":0,
  "error_msg":""
}
```


###  查询课堂信息
####  接口
- 接口名称：`/class/info`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/class/info?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 否 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| class_id | int | 课堂 ID | 是 | - |
| class_topic | string | 课堂主题/课堂名字 | 是 | - |
| class_type | string | 课堂类型 | 是 | - |
| class_status | string | 课堂状态 | 是 | - |
| teacher_id | string | 教师 ID | 是 | - |
| create_time | int64 | 课堂的创建时间 | 是 | - | 
| start_time | int64 | 课堂预计开始时间 | 是 | - | 
| stop_time | int64 | 课堂预计结束时间 | 是 | - |
| real_start_time | int64 | 课堂真正开始时间（老师开始上课时间） | 是 | 0 | 
| real_stop_time | int64 | 课堂真正结束时间（老师确认下课时间） | 是 | 0 |
| member_count | int64 | 课堂预约成员数 | 是 | - |
| chat_group_id | string | 课堂聊天群组 ID | 是 | - |
| cmd_group_id | string | 课堂信令群组 ID（如无特殊定制化需求，用户不需要使用该字段） | 是 | - |
| settings | Object | 课堂中的一些设置信息 | 是 | - |
| resolution | string | 视频分辨率 | 是 | - |
| fps | int | 视频帧率 | 是 | - |
| record_types | Array | 字符串数组，选定录制类型，如果填写了`remote`，在开始上课时，会自动开启云端录制 | 是 | - | 
| auto_open_mic  | int | 是否自动打开麦克风（0-不打开/1-打开）| 否 | 0 |
| auto_open_camera  | int | 是否自动打开摄像头（0-不打开/1-打开）| 否 | 0 |
| enable_all_silence  | int | 是否开启了全员禁言（0-否/1-是）| 否 | 0 |
| bitrate | int | 设置课堂的码率| 否 | 850 |
| layout | int | 课堂的布局风格（具体参见附录）| 否 | 0 |
| members | Array | 课堂预约成员列表 | 是 | - |
| role | string | 成员角色信息 | 是 | - |
| user_id | string | 成员 ID | 是 | - |
|max_member_limit|int|最大上麦人数|否|-|

#### 举例
请求：
```json
{
  "class_id": 100012345
}
```
响应：
```json
{
  "error_code": 0,
  "error_msg": "",
  "class_id": 100012345,
  "class_topic": "MyFirstClass",
  "class_type":"public",
  "class_status":"will",
  "teacher_id":"u1",
  "create_time": 1558350988,
  "start_time": 1558350990,
  "stop_time": 1558351000,
  "real_start_time": 1558350995,
  "real_stop_time": 1558350911,
  "member_count":30,
  "chat_group_id":"102304_chat",
  "cmd_group_id":"102304",
  "max_member_limit":6,
  "settings" : {
    "resolution": "1024x768",
    "fps": 20,
    "record_types": ["remote"],
    "bitrate": 850,
    "layout": 1,
    "auto_open_mic": 0,
    "auto_open_camera": 0
  },
  "members": [
    {
      "role": "student",
      "user_id": "user1"
    },
    {
      "role": "teacher",
      "user_id": "user2"
    }
  ]
}
```

### 查询课堂列表

####  接口
- 接口名称：`/class/list`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/class/list?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| index | int | 分段拉取分页索引 | 否 | 0 |
| size | int | 分段拉取分页大小（最大100） | 否 | 100 |
| user_id | string | 如果设置了 user_id 参数，则只查询 user_id 所在的课堂列表 | 否 | 空字符串|
| create_time_desc | bool | 是否按创建课堂时间倒序拉取 true-倒序/false-升序| 是 | true |
| class_status | Array  | 课堂的状态，默认拉取所有课堂；不传此字段或字段是空数组，也是拉取所有课堂 | 否 | ["will","ing","end"] |


#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| finish | bool | 是否拉取完所有数据 | 是 | - |
| total | int | 课堂总数 | 是 | -  |
| list | Array | 课堂信息列表 | 是 | - |

#### 举例
请求：
```json
{
  "index":0,
  "size":20,
  "user_id":"",
  "create_time_desc":true,
  "class_status": ["will","ing","end"]
}
```
响应：
```json
{
  "error_code": 0,
  "error_msg": "",
  "finish":true,
  "total":1,
  "list": [
    {
      "class_id":100012345,
      "class_topic":"职场培训",
      "class_type":"1vN",
      "class_status":"will",
      "teacher_id":"u1",
      "create_time":1558350988,
      "start_time":1558350990,
      "stop_time":1558351000
    }    
  ]
}
```
### 上课
#### 接口

- 接口名称：`/class/start` 
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL： `https://iclass.api.qcloud.com/paas/v1/class/start?公共参数` 

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| teacher_id | string | 教师 ID | 是 | - |
| class_id | int | 课堂 ID | 是 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

#### 举例

请求：

```json
{
    "teacher_id":"user",
    "class_id": 1234354
}
```

响应：

```json
{
    "error_code": 0,
    "error_msg": ""
}
```
### 下课
#### 接口

- 接口名称：`/class/stop` 
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL： `https://iclass.api.qcloud.com/paas/v1/class/stop?公共参数` 

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| teacher_id | string | 教师 ID | 是 | - |
| class_id | int | 课堂 ID | 是 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

#### 举例
请求：
```json
{
    "teacher_id":"user",
    "class_id": 1234354
}
```

响应：

```json
{
    "error_code": 0,
    "error_msg": ""
}
```

## 课件模块
### 添加课件
####  接口
- 接口名称：`/document/add`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/document/add?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| doc_url | string  | 原课件文档上传到腾讯云 COS 后，生成下载 URL | 是 | - |
| doc_name | string | 文档名（不包含扩展） | 否 | 空字符串 |
| doc_ext | string  | 文档的扩展名，如 ppt | 否 | 空字符串 |
| doc_size | int | 文档大小，单位：Byte，需填文件的真实大小，不填则认为是0| 否 | 0 |
| doc_md5 | int | 文档的 md5 | 否 | 空字符串 |
| permission | string | 文档权限 public-公开（所有人可以查看）/private-私有（只有自己可以查看）| 否 | private |
| is_transcode | bool | 是否需要 H5 转码（true-转码/false-不转码），如果需要此功能，需联系我们开通白名单，凡是需要在白板区域展示的文件都需要转码 | 否 | false|
| owner | string | 指定文档归属者（如果不填此字段，permission 会被设置为 public） | 否 | 空字符串 |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| doc_id | int | 文档 ID（互动课堂后台生成的课件唯一 ID） | 是 | - |

#### 举例
请求：
```
{
  "doc_url": "课件地址",
  "doc_name":"课件名字",
  "doc_ext": "ppt",
  "doc_size":1024,
  "doc_md5": "c4ca4238a0b923820dcc509a6f75849b",
  "permission":"private",
  "owner":"xxx",
  "is_transcode":false
}
```
响应：
```
{
  "error_code": 0,
  "error_msg": "",
  "doc_id":"sdfjdskljflkdsf"
}
```

### 删除课件
####  接口
- 接口名称：`/document/delete`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/document/delete?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| doc_ids | Array | 课件 ID 数组 | 是 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

#### 举例
请求：
```json
{
  "doc_ids": [
    "doc_id_1",
    "doc_id_2"
  ]
}
```
响应：
```json
{
  "error_code": 0,
  "error_msg": ""
}
```

### 查询课件信息
####  接口
- 接口名称：`/document/info`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/document/info?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| doc_id | string | 课件 ID | 是 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| doc_url | string  | 原课件文档上传到腾讯云 COS 后，生成下载 URL | 是 | - |
| doc_name | string | 文档名（不包含扩展） | 是 | - |
| doc_ext | string  | 文档的扩展名，如 ppt | 是 | - |
| doc_size | int | 文档大小，单位：Byte | 是 | - |
| doc_md5 | int | 文档的 md5 | 是 | - |
| permission | string | 文档权限 public-公开（所有人可以查看）/private-私有（只有自己可以查看）| 是 | private |
| owner | string | 指定文档归属者（如果不填此字段，permission 会被设置为 public） | 是 | - |
| upload_time | int64 | 文档上传时间 | 是 | - |
| is_transcode | bool | 是否需要支持动画的 H5 转码（true-转码/false-不转码），如果需要此功能，需联系我们开通白名单 | 是 | false |
| transcode_status | string | 当前转码状态 | 是 | - |
| transcode_code | int | 转码错误码；0-成功/非0-失败 | 是 | - |
| transcode_msg | string | 转码错误信息 | 是 | - |
| transcode_result | string | 转码结果（一个 H5 预览地址） | 是 | - |

#### 举例
请求：
```json
{
  "doc_id": "ywyzhohnx"
}
```
响应：
```json
{
  "error_code": 0,
  "error_msg": "",
  "doc_id": "ywyzhohnx",
  "doc_name":"课件名字",
  "doc_url":"http://xxxx.ppt",
  "doc_ext": "ppt",
  "doc_md5": "c4ca4238a0b923820dcc509a6f75849b",
  "doc_size": 204800,
  "permission":"public",
  "owner": "ownerIdentifier",
  "upload_time": 1558350990,
  "is_transcode":false,
  "transcode_status":"",
  "transcode_code":0,
  "transcode_msg":"",
  "transcode_result":""
}
```

### 查询课件列表
####  接口
- 接口名称：`/document/list`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/document/list?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| index | int | 分段拉取分页索引 | 否 | 0
| size | int | 分段拉取分页大小（最大100） | 否 | 100
| prefix | string | 课件名前缀（用来做模糊查询的） | 否 | 空字符串 |
| owner | string | 课件归属者 | 否 | 空字符串 |
| permissions | Array | 课件权限类型（如果是空数组，则获取所有类型） | 否 | 空数组 |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| finish | bool | 是否获取完所有课件 | 是 | - |
| total | int | 课件总数 | 是 | - |
| list | Array | 课件信息数组 | 是 | - |

#### 举例
请求：
```json
{
  "index":0,
  "size":10,
  "owner":"",
  "prefix":"量子",
  "permissions":["public","private"]
}
```
响应：
```json
{
  "error_code": 0,
  "error_msg": "",
  "finish":true,
  "total":100,
  "list": [
    {
      "doc_id": "doc_id_1",
      "doc_name":"量子计算导论",
      "doc_url":"http://xxxx.ppt",
      "doc_ext": "ppt",
      "doc_md5": "c4ca4238a0b923820dcc509a6f75849b",
      "doc_size": 204800,
      "permission":"public",
      "owner": "ownerIdentifier",
      "upload_time": 1558350990,
      "is_transcode":true,
      "transcode_status":"wait",
      "transcode_code":0,
      "transcode_msg":"fail",
      "transcode_result":"url"
    }
  ]
}
```

## 事件回调
用户在互动课堂后台设置接收事件的回调地址，互动课堂后台发起回调请求，用户后台必须回复响应包，响应包中 error_code 如果不为0，或者没有回复响应包，互动课堂后台会持续发送回调请求（重试10次，每次间隔1分钟）。

### 回调格式模版
####  接口
- 接口名称：`用户回调地址`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://用户回调地址?公共参数`

#### 请求参数
互动课堂后台发起的请求包体。

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| event | string | 事件名称 | 是 | - |
| data | Object | 具体回调事件对应的数据 | 是 | - |

#### 响应参数
用户业务后台返回的响应包体。

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |

#### 举例
老师开始上课回调事件。
请求：
```
{
  "event":"class_begin",
  "data":{
    "class_id":100012345,
    "real_start_time":1558350988
  }
}
```
响应：
```
{
  "error_code":0
}
```

#### 1. 老师开始上课
互动课堂客户端组件会上报老师开始上课到互动课堂后台，上报之后，互动课堂后台将此事件回调到客户后台。使用客户端互动课堂组件时，才会有“老师开始上课”事件回调；直接使用后台 API 发起老师开始上课，没有此事件回调。

**event**

```
class_begin
```
**data**

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | - |
| real_start_time | int64 | 课堂开始的真正时间 | 是 | - |

```
{
"class_id":100012345,
"real_start_time":1558350988
}
```

#### 2. 老师确认下课

互动课堂客户端组件会上报`下课事件`到互动课堂后台，上报之后，互动课堂后台将此事件回调到客户后台。使用客户端互动课堂组件时，才会有“老师开始下课”事件回调，直接使用后台 API 的，没有此事件回调。
**event**
```
class_over
```
**data**

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | - |
| real_stop_time | int64 | 课堂真正结束的时间 | 是 | - |

```
{
  "class_id":100012345,
  "real_stop_time":1558350988
}
```

#### 3. 在线录制开始

如果在约课时，录制类型设置了云端录制`remote`，则在`老师开始上课`时，会自动发起云端录制，并回调`在线录制开始`事件。
**event**
```
online_record_start
```
**data**

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| class_id | int | 课堂 ID | 是 | - |
| timestamp | int64 | 互动课堂后台时间戳 | 是 | - |

```
{
  "error_code":0,
  "error_msg":"",
  "class_id":100012345,
  "timestamp":1558350988
}
```

#### 4. 在线录制结束
**event**
```
online_record_stop
```
**data**

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
|:--------|:-----|:-------|:-------|:-------|
| error_code | int | 错误码 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| timestamp | int | 互动课堂后台，单位秒 | 是 | - |
| start_time | int | 实际开始录制时间，Unix 时间戳，单位秒 | 是 | - |
| stop_time | int | 实际停止录制时间，Unix 时间戳，单位秒 | 是 | - |
| class_id | int | 课堂 ID | 是 | - |
| video_info | []VideoInfo | 录制的视频信息 | 是 | - |

**VideoInfo 对象格式：**

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
|:--------|:-----|:------|:-------|:-------|
| video_play_time | int | 视频播放时间 | 是 | - |
| video_size | int | 文件大小（字节） | 是 | - |
| video_format | string | 文件格式（目前应该全部是 mp4） | 是 | - |
| video_duration | int | 文件播放时长（单位 s） | 是 | - |
| video_url | string | 录制文件 url | 是 | - |
| video_id | string | 点播后台返回的 fileId 字段 | 是 | - |
| video_type | int    | 视频流类型0：摄像头视频，1：屏幕分享视频，2：白板视频 | 是 | - |
| user_id | string | 视频所属用户的 ID，白板视频时，user_id 为空 | 是 | - |

```
{
  "error_code":0,
  "error_msg":"",
  "timestamp": 1529908745,
  "start_time": 1529908745,
  "stop_time": 1529908745,
  "class_id":100001234,
  "video_info":[
    {
      "video_play_time":0,
      "video_size":1200,
      "video_format":"mp4",
      "video_duration":3600,
      "video_url":"http://1253488539.vod2.myqcloud.com/oM86K7X3Ig8b.mp4",
      "video_id":"5285890781570653827",
      "video_type":0,
      "user_id":"ios_test1"
    },
    {
      "video_play_time":4000,
      "video_size":3756,
      "video_format":"mp4",
      "video_duration":5000,
      "video_url":"http://1253488539.vod2.myqcloud.com/oM86K7X3IsdfA.mp4",
      "video_id":"5285890781570653828",
      "video_type":2,
      "user_id":"pc_test1"
    }
  ]
}
```

#### 5. 转码进度回调

添加课件接口的 `is_transcode` 字段，可以控制是否进行 H5 转码，H5 转码可以将 PPT 中的动画效果，高度还原为 H5 页面，需要 H5 转码功能，需提前联系我们开通白名单。
**event**
```
transport_progress
```
**data**

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
|:--------|:-----|:-------|:-------|:-------|
| error_code | int | 错误码 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| timestamp | int | 进度发生改变的真正时间戳，单位秒 | 是 | - |
| status | string | 任务状态`queued`-正在排队/`processing`-转码中/`finished`-转码完成 | 是 | - |
| progress | int64 | 0-100的整数表示转码当前进度 | 是 | - |
| h5_url | string | 转码完成后 H5 的 URL | 是 | - |
| resolution | string | PPT 的分辨率 | 是 | - |
| pages | int | PPT 的总页数 | 是 | - |
| title | string | PPT 的文件名 | 是 | - |

```
{
  "error_code":0,
  "error_msg":"",
  "timestamp":100001234,
  "status":"finished",
  "progress": 50,
  "resolution": "1024x768",
  "pages": 20,
  "title": "PPT名字"
}
```
### 进入课堂回调



**event**

```
join_class
```

**data**

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | - |
| join_time | int64 | 进入课堂的时间 | 是 | - |
| user_id | string | 进入课堂的用户 | 是 | - |
| role | int64 | 进入课堂用户的角色 | 是 | - |


```
{
"class_id":100012345,
"join_time":1558350988,
"user_id":xxx,
"role":student,
}
```
### 退出课堂回调



**event**

```
quit_class
```

**data**

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | - |
| quit_time | int64 | 退出课堂的时间 | 是 | - |
| user_id | string | 退出课堂的用户 | 是 | - |
| role | int64 |退出入课堂用户的角色 | 是 | - |


```
{
"class_id":100012345,
"quit_time":1558350988,
"user_id":xxx,
"role":student,
}
```
### 本地录制结果回调



**event**

```
local_record_callback
```

**data**

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | - |
| class_topic | string | 课堂主题/课堂名字 | 否 | 课堂 ID 的字符串形式 |
| teacher_id | string | 教师 ID | 是 | - |
| assistant_id | string | 助教 ID | 是 | - |
| start_time | int | 视频开始时间 | 是 | - |
| stop_time | int | 视频结束时间 | 是 | - |
| class_start_time | int | 课堂开始时间 | 是 | - |
| class_stop_time | int | 课堂结束时间 | 是 | - |
| user_id | int | 录制者 id | 是 | - |
| record_type | string | 录制类型（online_record：在线录制，local_record：本地录制） | 是 | - |
| file_id | int | 视频文件 id | 是 | - |
| file_format | int | 视频文件格式 | 是 | - |
| file_size | int | 视频文件大小 | 是 | - |
| file_url | int | 视频文件地址 | 是 | - |
| duration | int | 视频文件时长 | 是 | - |


```
{
    "record_info":{
        "sdkappid":14000000,
        "class_id":1123123,
        "class_topic":"课堂",
        "teacher_id":"老师id",
        "assistant_id":"助教id",
        "start_time":12121212,
        "stop_time":13131313,
        "class_start_time":121212,
        "class_stop_time":13131313,
        "user_id":"录制者id",
        "record_type":"local_record",
        "file_id":"video id",
        "file_format":"MP4",
        "file_size":"文件大小",
        "file_url":"文件播放地址",
        "duration":123
    }
}
```
## 企业模块

### 修改企业信息
需要修改的字段填写在请求体中，不需要修改的字段不要设置，如果某个字段设置为空，则会覆盖已有数据。
#### 接口
- 接口名称：`/business/modify`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/business/modify?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| name | string | 企业名字 | 否 | - |
| contact_user | string | 企业联系人 | 否 | - |
| phone_no | string | 联系人电话 | 否 | - |
| e_mail | string | 联系人邮箱 | 否 | - |
| appid | int | 企业腾讯云账号的 appid（需要 ai 功能时才设置） | 否 | - |
| project_id | int | 企业腾讯云账号下的项目 ID（需要 ai 功能时才设置） | 否 | - |
| secret_id | string | 企业腾讯云账号下的密钥 ID（需要 ai 功能时才设置）| 否 | - |
| secret_key | string | 企业腾讯云账号下的密钥 key（需要 ai 功能时才设置） | 否 | - |
| im_admin | string | 企业腾讯云账号im的管理员账号 | 否 | - |
| private_key | string | 企业腾讯云账号im的密钥 key | 否 | - |

| call_back_url | string | 接收互动课堂的事件回调地址 | 否 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

#### 举例
修改企业名字、企业联系人、事件回调地址三项。
请求：
```
{
    "name": "新的企业名称",
    "contact_user":"新的联系人姓名",
    "call_back_url":"新的回调地址"
}
```
响应：
```
{
    "error_code": 0,
    "error_msg": "",
}
```

### 查询企业信息
#### 接口
- 接口名称：`/business/info`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/business/info?公共参数`

#### 请求参数
无
#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| enterprise_id | string | 机构 ID | 是 | - |
| sdkappid | int | 腾讯云账号下开通 TRTC 后，会得到一个唯一的项目标识 SDKAppID | 是 | - |
| busi_type | string | 业务类型 | 是 | - |
| name | string | 企业名字 | 是 | - |
| contact_user | string | 企业联系人 | 是 | - |
| phone_no | string | 企业联系人电话 | 是 | 空字符串 |
| e_mail | string | 企业联系人邮箱 | 是 | 空字符串 |
| create_time | int64 | 企业创建时间，单位秒 | 是 | - |
| valid_time | int64 | 企业账号有效时间，单位秒 | 是 | - |
| super_admin | string | 企业超级管理员（需要使用互动课堂控制台的企业需要关注此字段） | 是 | - |
| icon | string | 企业 logo | 是 | 空字符串 |
| tic_key | string | 互动课堂所有的 API 鉴权都依赖这个字段，用户需妥善`保密保存` | 是 | - |
| private_key | string | 腾讯云账号的私钥，用户需要妥善`保密保存` | 是 | - |
| bizid | int | 腾讯云账号的 BIZID | 是 | - |
| call_back_url | string | 事件回调地址 | 是 | 空字符串 |
| project_id | int | 腾讯云账号下的项目 ID（需要 ai 功能时需关注） | 是 | 0 |
| appid | int | 腾讯云账号下的 appid（需要 ai 功能时需关注） | 是 | 0 |
| secret_id | string | 腾讯云账号下的密钥对 ID（需要 ai 功能时需关注）  | 是 | 空字符串 |
| secret_key | string | 腾讯云账号下的密钥对 KEY（需要 ai 功能时需关注）  | 是 | 空字符串 |

#### 举例
请求：
```
{
}
```
响应：
```
{
    "error_code": 0,
    "error_msg": "",
    "enterprise_id": 10001,
    "sdkappid": 14000000,
    "busi_type": "saas",
    "name": "XX教育机构",
    "contact_user":"张三",
    "phone_no":"133xxxxxxxx",
    "e_mail":"xxx@xx.com",
    "create_time":1559094591,
    "valid_time":31536000,
    "super_admin":"adminid",
    "icon": "",
    "tic_key":"xxxxx",
    "private_key": "xxxxx",
    "bizid": 1234,
    "call_back_url":"https://xxx/yyy",
    "appid":0,
    "project_id":0,
    "secret_id":"",
    "secret_key":""
}
```

## 成员模块
### 添加课堂预约成员
#### 接口
- 接口名称：`/member/add`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/member/add?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | - |
| list | Array[info] | 要增加的成员数组，数组中是用户信息 | 是 | - |
| user_id | string | 用户 ID | 是 | - |
| role | string | 用户角色 | 是 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

#### 举例
请求：
```json
{
	"class_id": 1234354,
	"list": [
		{
			"user_id": "user1",
			"role": "student"
		},
		{
			"user_id": "user2",
			"role": "teacher"
		}
	]
}
```
响应：
```json
{
    "error_code": 0,
    "error_msg": ""
}
```

### 删除课堂预约成员
#### 接口
- 接口名称：`/member/delete`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/member/delete?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | - |
| list | Array[string] | 要删除的成员数组，数组中是成员 ID | 是 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

#### 举例
请求：
```json
{

	"class_id": 1234354,
	"list": [
		"user1",
		"user2"
	]
}
```
响应：
```json
{
    "error_code": 0,
    "error_msg": ""
}
```

### 成员加入课堂
#### 接口
- 接口名称：`/member/join`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/member/join?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | - |
| user_id | string | 用户 ID | 是 | - |
| password | string | 课堂密码 | 否 | - |
| camera | int | 摄像头状态1-打开/0-关闭 | 否 | 0 |
| mic | int | 麦克风状态1-打开/0-关闭 | 否 | 0 |
| speaker | int | 扬声器状态1-打开/0-关闭 | 否 | 0 |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| role | string | 成员在本课堂中的角色 | 是 | - |
|history_camera|int|用户在该课堂上一次摄像头的状态（0：关闭，1：打开，-1：未知）|是（已废弃）|-1
|history_mic|int|用户在该课堂上一次麦克风的状态（0：关闭，1：打开，-1：未知）|是（已废弃）|-1
|history_speaker|int|用户在该课堂上一次扬声器的状态（0：关闭，1：打开，-1：未知）|是（已废弃）|-1
|history_silence|int|用户在该课堂上一次禁言状态（0：未禁言，1：禁言，-1：未知）|是|-1
|history_hand_up|int|用户在该课堂上一次举手状态（0：未举手，1：举手，-1：未知）|是（已废弃）|-1
|history_enable_draw|int|用户在该课堂上一次授权状态（0：未授权，1：授权，-1：未知）|是（已废弃）|-1
|member_permission_list|int|摄像头麦克风权限列表|是|-


#### 举例
请求：
```json
{
	"class_id":12345,
	"user_id":"xxx",
	"password": "",
	"camera": 1,
	"mic": 1,
	"speaker": 1
}
```
响应：
```
{
    "error_code":0,
    "error_msg":"",
    "role":"student",
	"history_camera":0,
	"history_mic":0,
	"history_speaker":0,
	"history_silence":0,
	"history_hand_up":0,
	"member_permission_list": [
    {
      "user_id": "xkazer",
      "camera": 1,
      "mic": 1
    }
  ]
}
```

### 成员退出课堂
#### 接口
- 接口名称：`/member/quit`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/member/quit?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | - |
| user_id | string | 用户 ID | 是 | - |

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

#### 举例
请求：
```json
{
	"class_id":12345,
	"user_id":"xxx"
}
```
响应：
```
{
    "error_code":0,
    "error_msg":""
}
```

### 获取课堂实时成员列表
#### 接口
- 接口名称：`/member/runtime/list`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/member/runtime/list?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | 0
| index | int | 分段拉取分页索引 | 否 | 0
| size | int | 分段拉取分页大小（最大100） | 否 | 100

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| finish | bool | 是否拉取完所有成员 | 是 | - |
| total | string | 实时成员总数 | 是 | - |
| list | Array | 成员信息数组 | 是 | 空数组 |
| user_id | string | 用户 ID | 是 | - |
| nickname | string | 用户昵称 | 是 | - |
| gender | string | 用户性别 | 是 | - |
| avatar | string | 用户头像 URL | 是 | - |
| enter_time | int64 | 用户进房时间 | 是 | - |
| role | string | 用户角色 | 是 | - |
| Status | Object | 用户的一些状态信息 | 是 | - |
| camera | int | 用户摄像头状态1-打开/0-关闭 | 是 | - |
| mic | int | 用户麦克风状态1-打开/0-关闭 | 是 | - |
| speaker | int | 用户扬声器状态1-打开/0-关闭 | 是 | - |
| silence | int | 用户是否被禁言1-被禁言/0-未被禁言 | 是 | - |
| hand_up | int | 用户是否正在举手1-举手/0-未举手 | 是 | - |
| enable_draw | int  | 0-未授权/1-授权 | 是 | - |

#### 举例
请求：
```json
{
	"class_id":12345,
	"index":0,
	"size":20
}
```
响应：
```json
{
    "error_code":0,
    "error_msg":"",
    "finish":true,
    "total":1,
    "list":[
        {
            "user_id":"xxx",
            "nickname":"昵称",
            "gender":"male",
            "avatar":"https://xxxx/head.png",
            "enter_time": 1550546356,
            "role":"student",
            "status": {
                "camera": 1,
                "mic": 1,
                "speaker": 1,
                "silence": 0,
                "hand_up":1,
		"enable_draw":0
            }
        }
    ]
}
```

###  获取课堂实时成员总数
#### 接口
- 接口名称：`/member/runtime/total`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/member/runtime/total?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | 0

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| total | string | 实时成员总数 | 是 | - |

#### 举例
请求：
```json
{
	"class_id":1000001234
}
```
响应：
```
{
    "error_code":0,
    "error_msg":"",
    "total":20
}
```

### 获取课堂历史成员列表
历史成员与实时成员的区别：
1. 历史成员中不包含`游客`。
2. 历史成员信息中有“退房时间”。
3. 历史成员信息中**没有**“成员状态信息”。

#### 接口
- 接口名称：`/member/history/list`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/member/history/list?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | 0
| index | int | 分段拉取分页索引 | 否 | 0
| size | int | 分段拉取分页大小（最大100） | 否 | 100

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| finish | bool | 是否拉取完所有成员 | 是 | - |
| total | string | 历史成员总数 | 是 | - |
| list | Array | 成员信息数组 | 是 | 空数组 |
| user_id | string | 用户 ID | 是 | - |
| nickname | string | 用户昵称 | 是 | - |
| gender | string | 用户性别 | 是 | - |
| avatar | string | 用户头像 URL | 是 | - |
| enter_time | int64 | 用户进房时间 | 是 | - |
| quit_time | int64 | 用户退房时间 | 是 | - |
| role | string | 用户角色 | 是 | - |
|history_camera|int|用户在该课堂上一次摄像头的状态（0：关闭，1：打开，-1：未知）|是|-1
|history_mic|int|用户在该课堂上一次麦克风的状态（0：关闭，1：打开，-1：未知）|是|-1
|history_speaker|int|用户在该课堂上一次扬声器的状态（0：关闭，1：打开，-1：未知）|是|-1
|history_silence|int|用户在该课堂上一次禁言状态（0：未禁言，1：禁言，-1：未知）|是|-1
|history_hand_up|int|用户在该课堂上一次举手状态（0：未举手，1：举手，-1：未知）|是|-1
|history_enable_draw|int|用户在该课堂上一次交互授权状态（0：未授权，1：授权，-1：未知）|是|-1

#### 举例
请求：
```json
{

	"class_id":12345,
	"index":0,
	"size":20
}
```
响应：
```json
{
	"error_code":0,
	"error_msg":"",
	"finish":true,
	"total":1,
	"list":[
		{
			"user_id":"xxx",
			"nickname":"昵称",
			"gender":"male",
			"avatar":"https://xxxx/head.png",
			"enter_time": 1550546356,
			"quit_time": 1550548573,
			"role":"student",
			"history_camera":0,
			"history_mic":0,
			"history_speaker":0,
			"history_silence":0,
			"history_hand_up":0,
			"history_enable_draw":0
		}
	]
}
```

### 获取课堂历史成员总数
#### 接口
- 接口名称：`/member/history/total`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/member/history/total?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | 0

#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| total | string | 实时成员总数 | 是 | - |

#### 举例
请求：
```json
{
	"class_id":1000001234
}
```
响应：
```
{
    "error_code":0,
    "error_msg":"",
    "total":20
}
```

## 录制模块

### 获取本地录制列表
#### 接口
- 接口名称：`/localrecord/query`
- 接口方法：`POST`
- Content-Type：`application/json`
- 接口 URL：`https://iclass.api.qcloud.com/paas/v1/localrecord/query?公共参数`

#### 请求参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂 ID | 是 | 0
| user_id | string | 录制用户 ID | 否 | 0
| task_id | string | 录制任务 ID，本地录制拼接成功返回给客户端的 ID | 否 | 0
| Index | int | 分页拉取时，页面起始数据位置 | 是 | 0
| size | int | 分页拉取时，页面数据个数 | 是 | 0


#### 响应参数

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| finish | bool | 是否拉取完 | 是 | - |
| total | string | 录制文件总数 | 是 | - |
| record_info_list | array | 录制文件列表 | 是 | - |


#### 举例
请求：
```json
{
	"class_id":1212,
	"user_id":"",
	"task_id":"",
	"Index":0,
	"size":2
}
```
响应：
```
{
    "error_code": 0,
    "error_msg": "",
    "finish": true,
    "total": 1,
    "record_info_list": [
        {
            "RoomId": 1212,
            "UserId": "eric",
            "TaskId": "1257307760-EditMedia-fbd05676116bb6297f8c5162ec54ef93t0",
            "StartTime": 0,
            "SplicTime": 1574408606,
            "VideoOutputType": "mp4",
            "VideoOutputId": "5285890796076789146",
            "VideoOutputUrl": "http://1257307760.vod2.myqcloud.com/5f5371a5vodgzp1257307760/2d508f205285890796076789146/playlist.f9.mp4",
            "VideoOutputSize": 0,
            "VideoOutputDuration": 0
        }
    ]
}
```

## 附录

### 附录1：API 公共参数
| 参数名 | 类型 | 描述 |
| :------ | :--- | :---- |
| sdkappid | int | 腾讯云账号下开通 TRTC 后，会得到一个唯一的项目标识 SDKAppID |
| random | int | 一个随机数，用于区分不同的请求，过滤日志等 |
| sign | string | API 鉴权字符串 |
| expire_time | int64 | 请求签名串过期时间戳 |

**举例：**
预约课堂的完整 API：
```
https://iclass.api.qcloud.com/paas/v1/class/create?sdkappid=1400127140&random=37926&expire_time=1548247837&sign=xxxxxxx
```

### 附录2：API 鉴权算法

签名算法：`md5(tic_key+expire_time)`

|参数    |类型    | 描述|
|:---- | :---| :--- |
| tic_key | string | 创建企业时，下发的互动课堂 API 鉴权 KEY |
| expire_time    | int64 |    签名的过期时间戳：当前时间戳 + 签名有效时间；每个请求包体中都必须带此字段 |

**举例：**
1. 当前时间戳是`1548247717`。
2. 签名有效时间是120秒，则过期时间戳是`1548247717+120=1548247837`。
3. `tic_key`是`DzXpbluRsmo1JkoFxzKMNg5ifrA4GRlU`。
4. 将过期时间拼在`tic_key`后面`DzXpbluRsmo1JkoFxzKMNg5ifrA4GRlU1548247837`。
5.`sign=md5(DzXpbluRsmo1JkoFxzKMNg5ifrA4GRlU1548247837)=28374bd8cff400ac4906414780fbe387`。
6. 在请求体中，带上 expire_time 字段，值为`1548247837`。
7. 在请求 url 的参数中，带上`sign=28374bd8cff400ac4906414780fbe387`。

### 附录3：常量类型枚举值
#### 附录3.1 角色-role

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| superadmin | string | 超级管理员（申请创建企业时，设置的超级管理员） |
| admin | string | 普通管理员（需要使用腾讯云互动课堂控制台时需要关注） |
| teacher | string | 教师 |
| assistant | string | 助教 |
| student | string | 学生 |
| supervisor | string | 巡课员 |
| visitor | string | 游客 |

#### 附录3.2 录制类型-record_type

在约课时设置此字段，如果设置为 remote，在`上课`后，后台会自动发起云端录制，录制结束后，会自动发起结束录制回调。

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| local | string | 本地录制 |
| remote | string | 云端录制 |

#### 附录3.3 视频分辨率-resolution
>?当前版本不支持用互动课堂 API 设置分辨率。

| 常量值 | 类型 | 描述 |
| :-- | :-- | :-- |
| 120x120 | string | 120x120的分辨率 |
| 160x160 | string | 160x160的分辨率 |
| 270x270 | string | 270x270的分辨率 |
| 480x480 | string | 480x480的分辨率 |
| 160x120 | string | 160x12的分辨率 |
| 240x180 | string | 240x180的分辨率 |
| 280x210 | string | 280x210的分辨率 |
| 320x240 | string | 320x240的分辨率 |
| 400x300 | string | 00x300的分辨率 |
| 480x360 | string | 480x360的分辨率 |
| 640x480 | string | 640x480的分辨率 |
| 960x720 | string | 960x720的分辨率 |
| 160x90 | string | 160x90的分辨率 |
| 256x144 | string | 256x144的分辨率 |
| 320x180 | string | 320x180的分辨率 |
| 480x270 | string | 480x270的分辨率 |
| 640x360 | string | 640x360的分辨率 |
| 960x540 | string | 960x540的分辨率 |
| 1280x720 | string | 1280x720的分辨率 |
| 1920x1080 | string | 1920x1080的分辨率 |

#### 附录3.4 课堂状态-class_status

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| end | string | 已经结束的课堂|
| ing | string | 进行中的课堂|
| will | string | 未开始的课堂|


#### 附录3.5 设备开关
设备包括：camera、mic、speaker 等。

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| 0 | int | 关闭 |
| 1 | int | 打开 |

#### 附录3.6 禁言-silence

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| 0 | int | 畅聊 |
| 1 | int | 禁言 |

#### 附录3.7 性别-gender

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| male | string | 男 |
| female | string | 女 |

#### 附录3.8 事件上报-event

| 常量值 | 类型 |描述 |
| :-----  | :--- | :---- |
| camera_open | string | 打开摄像头 |
| camera_close | string | 关闭摄像头 |
| mic_open | string | 打开麦克风 |
| mic_close | string | 关闭麦克风 |
| speaker_open | string | 打开扬声器 |
| speaker_close | string | 关闭扬声器 |
| device_test | string | 设备测试 |
| speed_test | string | 测速信息上报 |
| hand_up | string | 举手 |
| hand_down | string | 取消举手 |
| enable_draw | string | 交互授权 |
| diable_draw | string | 取消交互授权 |
| reward | string | 奖励 |
| slience | string | 禁言 |
| del_silenced | string | 解除禁言 |
| all_silence | string | 全员禁言 | 
| del_all_silence | string | 解除全员禁言 |
| disable_camera | string | 禁用别人的摄像头 |
| be_disable_camera | string | 被别人的禁用了自己的摄像头 |
| disable_mic | string | 禁用别人的麦克风 |
| be_disable_mic | string | 被别人禁用了自己的麦克风 |
| disable_speaker | string | 禁用别人的扬声器 |
| be_disable_speaker | string | 被别人的禁用了自己的扬声器 |
| kick | string | 踢人 |
| be_kicked |  string | 被踢 |
| screen_share_open | string | 开启屏幕共享 |
| screen_share_close | string | 关闭屏幕共享 |
| media_open | string | 开始播片 |
| media_close | string | 停止播片 |
| packet_loss_mutation |  string | 丢包突变 |
| rate_mutation |  string | 码率突变 |

### 附录4: 用户头像规则
如果没有设置用户头像，互动课堂后台会随机设置一个默认的头像

| 格式 | 大小 |
| :-----  | :--- |
| jpg、png | 小于100KB，400x400 |

### 附录5：错误码

#### 附录5.1 公共错误码
| 错误码 | 含义说明 |
| :--- | :--- |
| 0 | 处理成功 |
| -1 | 通用错误码 |
| 10000 | 解析失败（解析 url/解析 body 字段） |
| 10001 | 序列化失败 |
| 10002 | 反序列化失败 |
| 10003 | 参数无效 |
| 10005 | 读取请求包体失败 |


#### 附录5.2 SaaS 后台通用
| 错误码 | 含义说明 |
| :--- | :--- |
| 10200 | 加密失败 |
| 10201 | 解密失败 |
| 10202 | 操作 DB 失败 |
| 10203 | 权限不足（普通用户操作了管理员的接口等） |


#### 附录5.3 用户
| 错误码 | 含义说明 |
| :--- | :--- |
| 10210 | 注册失败 |
| 10211 | 登录失败 |
| 10212 | 登出失败 |
| 10213 | 游客账号获取失败 |
| 10214 | 用户重复 |
| 10215 | 用户不存在 |
| 10216 | Token 过期 |
| 10217 | Sign 鉴权失败 |
| 10218 | 登录密码错误 |


#### 附录5.4 课堂
| 错误码 | 含义说明 |
| :--- | :--- |
| 10220 | 获取课程表失败 |
| 10221 | 没有任何课程 |
| 10222 | 生成课堂 ID 失败 |
| 10223 | 更新/删除课堂信息失败，课堂正在进行 |
| 10224 | 由于课堂已结束导致无法加入课堂 |
| 10225 | 课堂密码错误 |


#### 附录5.5 成员
| 错误码 | 含义说明 |
| :--- | :--- |
| 10230 | 课堂不存在 |


#### 附录5.6 课件
| 错误码 | 含义说明 |
| :--- | :--- |
| 10240 | 生成课件 ID 失败 |


#### 附录5.7 转码
| 错误码 | 含义说明 |
| :--- | :--- |
| 10250 | 创建转码任务失败 |


#### 附录5.8 企业
| 错误码 | 含义说明 |
| :--- | :--- |
| 10270 | 企业不存在 |


#### 附录5.9 IM 后台
| 错误码 | 含义说明 |
| :--- | :--- |
| 10280| 创建 IM 群组失败 |

### 附录6：布局类型-Layout

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| 0 | int | 未设置布局|
| 1 | int | 竖屏|
| 2 | int | 横屏 |
