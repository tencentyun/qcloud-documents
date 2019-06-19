# 云API

互动课堂SaaS组件为客户提供了一站式的在线教育服务。客户可以通过集成组件快速实现音视频互动，聊天，白板，课件，成员管理等课堂体验。本文档描述互动课堂后端接口，客户通过使用下述接口为组件提供必要信息，并获取组件的运行状况。


![img](https://main.qcloudimg.com/raw/4e7b38c3d8e5e10c3fb81a5f0b669f4d.png)

## 1 课堂模块
### 1.1 预约课堂
__接口__ 

| 接口名称 | `/class/create` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/class/create?公共参数` |


__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| teacher_id | string | 教师ID | 是 | - |
| class_topic | string | 课堂主题/课堂名字 | 否 | 课堂ID的字符串形式 |
| class_type | string | 课堂类型,详情参考附录 | 否 | `public` |
| start_time | int64 | 课堂预计开始时间戳 | 否 | 约课时的时间 | 
| stop_time | int64 | 课堂预计结束时间戳 | 否 | start_time+2小时 |
| record_types | Array | 字符串数组，选定录制类型，如果填写了`remote`, 在开始上课时，会自动开启服务端录制 | 否 | local | 
| members | Array | 课堂预约成员列表 | 否 |  教师ID默认在成员列表中 |
| role | string | 角色信息，本接口中全部填“student”。需要设置members时此字段必填 | 否 | - |
| user_id | string | 学生ID。需要设置members时此字段必填 | 否 | - |
| record_user_id | string | 用于录制的user_id，必须包含前缀"tic_recorduser${room_id}"，其中${room_id}为房间号，在线录制服务会使用这个user_id进房进行录制房间内的音视频与白板，为了防止进房冲突，请保证此user_id不重复，如果要云端录制，则必填 | 否 | - |
| record_user_sig | string | 用于录制的record_user_id对应的签名，如果要云端录制，则必填 | 否 | - |

__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| class_id | int | 课堂ID | 否 | - |
| teacher_url | string | 老师进房地址，成功时下发 | 否 | - |
| student_url | string | 学生进房地址，成功时下发 | 否 | - |

__举例__ 

request:
```
{
"expire_time": 1548296231,
"teacher_id":"user_00",
"class_topic": "课堂主题",
"class_type":"public",
"start_time": 1558350988,
"stop_time": 1558350988,
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
}
"record_user_id":"tic_record_user_1234_01",
"record_user_sig": "user_sig"
}
```

response:
```
{
"error_code":0,
"error_msg":"",
"class_id":100012345,
"teacher_url":"https://tedu.qcloudtrtc.com/1400127140/100012345/0",
"student_url":"https://tedu.qcloudtrtc.com/1400127140/100012345/1",
}
```

### 1.2 删除

__接口__ 

| 接口名称 | `/class/delete` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/class/delete?公共参数` |

__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| class_id | int | 课堂ID | 是 | - |

__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

__举例__ 

request

```
{
"expire_time": 1548296231,
"class_id": 100012345
}
```

response

```
{
"error_code":0,
"error_msg":""
}
```


### 1.3 修改课堂信息
__接口__ 

| 接口名称 | `/class/modify` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/class/modify?公共参数` |

__请求参数__ 

修改课堂的参数字段与创建课堂相同，需要修改哪个字段，就在请求body中设置该字段，不需要修改的字段，不要带在body中。<br> __注意__ :class_id不可修改；members 是全量修改，如果要增量修改，参考成员模块中的`添加预约成员`接口

__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

__举例__ 
修改课堂主题和课堂结束时间
request

```json
{
"expire_time": 1548296231,
"class_id": 102304,
"class_topic": "新的课堂主题",
"stop_time": 1558351000,
}
```

response

```json
{
"error_code":0,
"error_msg":"",
}
```


### 1.4 查询课堂信息
__接口__ 

| 接口名称 | `/class/info` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/class/info?公共参数` |

__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| class_id | int | 课堂ID | 否 | - |

__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| class_id | int | 课堂ID | 是 | - |
| class_topic | string | 课堂主题/课堂名字 | 是 | - |
| class_type | string | 课堂类型 | 是 | - |
| class_status | string | 课堂状态 | 是 | - |
| teacher_id | string | 教师ID | 是 | - |
| create_time | int64 | 课堂的创建时间 | 是 | - | 
| start_time | int64 | 课堂预计开始时间 | 是 | - | 
| stop_time | int64 | 课堂预计结束时间 | 是 | - |
| real_start_time | int64 | 课堂真正开始时间(老师开始上课时间) | 是 | 0 | 
| real_stop_time | int64 | 课堂真正结束时间(老师确认下课时间) | 是 | 0 |
| member_count | int64 | 课堂预约成员数 | 是 | - |
| chat_group_id | string | 课堂聊天群组ID | 是 | - |
| cmd_group_id | string | 课堂信令群组ID(如无特殊定制化需求，用户不需要使用该字段) | 是 | - |
| settings | Object | 课堂中的一些设置信息 | 是 | - |
| resolution | string | 视频分辨率 | 是 | - |
| fps | int | 视频帧率 | 是 | - |
| layout | int | 客户端互动课堂组件布局模式(使用客户端组件的用户需要关注) | 是 | - |
| record_types | Array | 字符串数组，选定录制类型，如果填写了`remote`, 在开始上课时，会自动开启云端录制 | 是 | - | 
| members | Array | 课堂预约成员列表 | 是 | - |
| role | string | 成员角色信息 | 是 | - |
| user_id | string | 成员id | 是 | - |


__举例__ 

request

```json
{
"expire_time": 1548296231，
"class_id": 100012345
}
```

response

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
"settings" : {
"resolution": "1024x768",
"fps": 20,
"layout": 1,
"record_types": ["remote"]
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

### 1.5 查询课堂列表
__接口__ 

| 接口名称 | `/class/list` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/class/list?公共参数` |

__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| index | int | 分段拉取分页索引 | 否 | 0 |
| size | int | 分段拉取分页大小(最大100) | 否 | 100 |
| user_id | string | 如果设置了user_id参数，则只查询user_id所在的课堂列表 | 否 | 空字符串|
| create_time_desc | bool | 是否按创建课堂时间倒序拉取 true-倒序/false-升序| 是 | true |
| class_status | Array  | 课堂的状态,默认拉取所有课堂；不传此字段或字段是空数组，也是拉取所有课堂 | 否 | ["will","ing","end"] |
| class_type | Array  | 课堂的类型,默认拉取所有课堂；不传此字段或字段是空数组，也是拉取所有课堂 | 否 | ["public","1v1","1vN"] |


__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| finish | bool | 是否拉取完所有数据 | 是 | - |
| total | int | 课堂总数 | 是 | -  |
| list | Array | 课堂信息列表 | 是 | - |

__举例__ 

request
```json
{
"expire_time": 1548296231,
"index":0,
"size":20,
"user_id":"",
"create_time_desc":true,
"class_status": ["will","ing","end"],
"class_type":["1vN"]
}
```

response

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
"stop_time":1558351000,
}    
]
}
```

## 2 账号模块
### 2.1 创建账号
__接口__ 

| 接口名称 | `/user/register` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/user/register?公共参数` |

__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| list | Array | 需要注册的用户列表 | 是 | - |
| user_id | string | 用户ID | 是 | - |
| role | string | 用户角色 | 是 | - |
| nickname | string | 用户昵称 | 否 | 用户ID |
| gender | string | 用户性别 | 否 | 男 |
| avatar | string | 头像的URL地址，头像规则参考附录 | 否 | 互动课堂后台随机选择一个头像 |
| phone_no | string | 手机号 | 否 | |
| e_mail | string | 邮箱 | 否 | |

__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| user_list | Array |创建成功后，每个用户对应生成一个user_token, 用于唤起组件 | 是 | 空数组 |
| user_token | string | 用户票据, 每个用户ID对应一个user_token | 是 | - |
| repeats | Array | 出现重复id时，会报错，且返回重复user_id列表 | 是 | 空数组 |

__举例__ 

request:

```
{
"expire_time": 1548296231,
"list":[
{
"user_id":"xxxxx",
"role":"student",
"nickname":"小明",
“gender”:"male",
"avatar":"https://xxx/xiaoming.png", 
"phone_no":"13033445566",
"e_mail":"xxx@xx.com"
}
]
}
```

response:

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

### 2.2 修改账号信息
__接口__ 

| 接口名称 | `/user/profile/modify` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/user/profile/modify?公共参数` |

__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| user_id | string | 用户ID | 是 | - |
| role | int | 角色 | 否 | - |
| nickname | string | 昵称 | 否 | - |
| gender | string | 用户性别 | 否 | - |
| avatar | string | 头像的URL地址 | 否 | - |
| phone_no | string | 手机号 | 否 | - |
| e_mail | string | 邮箱 | 否 | - |

__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

__举例__ 

需要修改哪个字段，就在请求body中设置该字段的值，不需要修改的字段，不要在body中设置。
本例修改用户昵称
request

```
{
"expire_time": 1548296231,
"user_id":"xxxx",
"nickname":"新昵称"
}
```

response

```
{
"error_code":0,
"error_msg":"",
}
```


### 2.3 更新账号票据
__接口__ 

| 接口名称 | `/user/token/update` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/user/token/update?公共参数` |

__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| user_id | string | 用户ID | 是 | - |

__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| user_token | string | 新的用户票据 | 是 | - |

__举例__ 

request

```
{
"expire_time": 1548296231,
"user_id":"xxxx"
}
```

response

```
{
"error_code":0,
"error_msg":"",
"user_token":"新的票据"
}
```

### 2.4 查询用户详情
__接口__ 

| 接口名称 | `/user/info` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/user/info?公共参数` |

__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| user_id | string | 用户ID | 是 | - |

__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| user_info | Object | 用户对象 | 是 | - |
| user_id | string | 用户ID | 是 | - |
| nickname | string | 用户昵称 | 是 | - |
| gender | string | 用户性别 | 是 | - |
| avatar | string | 用户头像 | 是 | - |
| role | string | 用户角色 | 是 | - |
| phone_no | string | 用户电话 | 是 | - |
| e_mail | string | 用户邮箱 | 是 | - |
| regist_time | string | 用户注册时间 | 是 | - |
| update_time | string | 用户信息最后一次修改时间 | 是 | - |

__举例__ 

request

```json
{
"expire_time": 1548296231,
"user_id":"用户ID"
}
```

response

```json
{
"error_code":0,
"error_msg":"",
"user_info":{
"user_id":"user1",
"nickname":"user1_nickname",
"gender":"male",
"avatar":"https://xxxx/head.png",
"role":"stduent",
"phone_no":"15888667799",
"e_mail":"xx@xx.com",
"regist_time":1554786131,
"update_time":1554786131
}
}
```

### 2.5 查询用户列表
__接口__ 

| 接口名称 | `/user/list` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/user/list?公共参数` |

__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| index | int | 分段拉取分页索引 | 否 | 0
| size | int | 分段拉取分页大小(最大100) | 否 | 100
| roles | Array | 用户角色，用作过滤(不填此字段或字段为空数组均获取所有角色) | 否 | 所有角色
| prefix | string | 用户ID的前缀，用做模糊过滤 | 否 | 空字符串

__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| finish | bool | 是否拉取完所有用户 | 是 | - |
| total | string | 用户总数 | 是 | - |
| list | Array | 用户数组 | 是 | 空数组 |
| user_id | string | 用户ID | 是 | - |
| role | string | 用户角色 | 是 | - |
| nickname | string | 用户昵称 | 是 | - |
| gender | string | 用户性别 | 是 | - |
| avatar | string | 用户头像URL | 是 | - |
| phone_no | string | 用户电话 | 是 | - |
| e_mail | string | 用户邮箱 | 是 | - |
| regist_time | int64 | 用户注册时间 | 是 | - |
| update_time | int64 | 用户最后一次更新时间 | 是 | - |


__举例__ 

获取所有角色为老师的用户

request

```json
{
"expire_time": 1548296231,
"index":0,
"size":10,
"roles":["teacher"],
"prefix":""
}
```

response

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

## 3 课件模块
### 3.1 添加课件
__接口__ 

| 接口名称 | `/document/add` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/document/add?公共参数` |

__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| doc_url | string  | 原课件文档上传到腾讯云COS后，生成下载URL | 是 | - |
| doc_name | string | 文档名(不包含扩展) | 否 | 空字符串 |
| doc_ext | string  | 文档的扩展名，如：ppt | 否 | 空字符串 |
| doc_size | int | 文档大小，单位：Byte | 否 | 0 |
| doc_md5 | int | 文档的md5 | 否 | 空字符串 |
| permission | string | 文档权限 public-公开(所有人可以查看)/private-私有(只有自己可以查看)| 否 | private |
| is_transcode | bool | 是否需要H5转码(true-转码/false-不转码),如果需要此功能，需联系我们开通白名单 | 否 | false|
| owner | string | 指定文档归属者(如果不填此字段，permission会被设置为public) | 否 | 空字符串 |

__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| doc_id | int | 文档id(互动课堂后台生成的课件唯一ID) | 是 | - |

__举例__ 

request

```
{
"expire_time": 1548296231,
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

response

```
{
"error_code": 0,
"error_msg": "",
"doc_id":"sdfjdskljflkdsf"
}
```

### 3.2 删除课件
__接口__ 

| 接口名称 | `/document/delete` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/document/delete?公共参数` |

__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| doc_ids | Array | 课件ID数组 | 是 | - |

__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |

__举例__ 
request

```json
{
"expire_time": 1548296231,
"doc_ids": [
"doc_id_1",
"doc_id_2"
]
}
```

response

```json
{
"error_code": 0,
"error_msg": ""
}
```

### 3.3 查询课件信息
__接口__ 

| 接口名称 | `/document/info` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/document/info?公共参数` |

__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| doc_id | string | 课件ID | 是 | - |

__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| doc_url | string  | 原课件文档上传到腾讯云COS后，生成下载URL | 是 | - |
| doc_name | string | 文档名(不包含扩展) | 是 | - |
| doc_ext | string  | 文档的扩展名，如：ppt | 是 | - |
| doc_size | int | 文档大小，单位：Byte | 是 | - |
| doc_md5 | int | 文档的md5 | 是 | - |
| permission | string | 文档权限 public-公开(所有人可以查看)/private-私有(只有自己可以查看)| 是 | private |
| owner | string | 指定文档归属者(如果不填此字段，permission会被设置为public) | 是 | - |
| upload_time | int64 | 文档上传时间 | 是 | - |
| is_transcode | bool | 是否需要支持动画的H5转码(true-转码/false-不转码),如果需要此功能，需联系我们开通白名单 | 是 | false |
| transcode_status | string | 当前转码状态 | 是 | - |
| transcode_code | int | 转码错误码；0-成功/ 非0-失败 | 是 | - |
| transcode_msg | string | 转码错误信息 | 是 | - |
| transcode_result | string | 转码结果(一个H5预览地址) | 是 | - |


__举例__ 

request

```json
{
"expire_time": 1548296231,
"doc_id": “ywyzhohnx”
}
```

response

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

### 3.4 查询课件列表
__接口__ 

| 接口名称 | `/document/list` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://iclass.api.qcloud.com/paas/v1/document/list?公共参数` |

__请求参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| index | int | 分段拉取分页索引 | 否 | 0
| size | int | 分段拉取分页大小(最大100) | 否 | 100
| prefix | string | 课件名前缀(用来做模糊查询的) | 否 | 空字符串 |
| owner | string | 课件归属者 | 否 | 空字符串 |
| permissions | Array | 课件权限类型(如果是空数组，则获取所有类型) | 否 | 空数组 |


__响应参数__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| finish | bool | 是否获取完所有课件 | 是 | - |
| total | int | 课件总数 | 是 | - |
| list | Array | 课件信息数组 | 是 | - |

__举例__ 

request

```json
{
"expire_time": 1548296231,
"index":0,
"size":10,
"owner":"",
"prefix":"量子",
"permissions":["public","private"]

}
```

response

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

## 4 事件回调
用户在互动课堂后台设置接收事件的回调地址，互动课堂后台发起回调请求，用户后台必须回复响应包，响应包中error_code 如果不为0，或者没有回复响应包，互动课堂后台会持续发送回调请求(重试10次，每次间隔1分钟)

### 4.1 回调格式模版

__接口__ 

| 接口名称 | `用户回调地址` |
| :---------| :---------------|
| 接口方法 | `POST` |
| Content-Type | `application/json` |
| 接口URL | `https://用户回调地址?公共参数` |

__请求参数__ 

互动课堂后台发起的请求包体

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| expire_time | int64 | 请求签名串过期时间戳，鉴权时使用 | 是 | - |
| event | string | 事件名称 | 是 | - |
| data | Object | 具体回调事件对应的的数据 | 是 | - |

__响应参数__ 

用户业务后台返回的响应包体

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码，0-成功/ 非0-失败 | 是 | - |

__举例__ 

老师开始上课回调事件

回调请求格式如下：
```
{
"expire_time":1548296231,
"event":"class_begin",
"data":{
"class_id":100012345,
"real_start_time":1558350988
}
}
```

响应包格式如下：
```
{
"error_code":0,
}
```

### 4.2 老师开始上课

互动课堂客户端组件会上报老师开始上课到互动课堂后台，上报之后，互动课堂后台将此事件回调到客户后台
使用客户端互动课堂组件时，才会有“老师开始上课”事件回调；直接使用后台API发起老师开始上课，没有此事件回调

__event__

```
class_begin
```

__data__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂ID | 是 | - |
| real_start_time | int64 | 课堂开始的真正时间 | 是 | - |

```
{
"class_id":100012345,
"real_start_time":1558350988
}
```

### 4.3 老师确认下课

互动课堂客户端组件会上报`下课事件`到互动课堂后台，上报之后，互动课堂后台将此事件回调到客户后台
使用客户端互动课堂组件时，才会有“老师开始下课”事件回调，直接使用后台API的，没有此事件回调

__event__

```
class_over
```

__data__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| class_id | int | 课堂ID | 是 | - |
| real_stop_time | int64 | 课堂真正结束的时间 | 是 | - |

```
{
"class_id":100012345,
"real_stop_time":1558350988
}
```

### 4.4 在线录制开始

如果在约课时，录制类型设置了云端录制`remote`, 则在`老师开始上课`时，会自动发起云端录制，并回调`在线录制开始`事件

__event__

```
online_record_start
```

__data__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
| :------ | :--- | :---- | :--------: | :-----: |
| error_code | int | 错误码 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| class_id | int | 课堂ID | 是 | - |
| timestamp | int64 | 互动课堂后台时间戳 | 是 | - |

```
{
"error_code":0,
"error_msg":"",
"class_id":100012345,
"timestamp":1558350988
}
```

### 4.5 在线录制结束

__event__

```
online_record_stop
```

__data__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
|:--------|:-----|:-------|:-------|:-------|
| error_code | int | 错误码 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| timestamp | int | 互动课堂后台，单位秒 | 是 | - |
| start_time | int | 实际开始录制时间，Unix时间戳，单位秒 | 是 | - |
| stop_time | int | 实际停止录制时间，Unix时间戳，单位秒 | 是 | - |
| class_id | int | 课堂ID | 是 | - |
| video_info | []VideoInfo | 录制的视频信息 | 是 | - |

VideoInfo对象格式

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
|:--------|:-----|:------|:-------|:-------|
| video_play_time | int | 视频播放时间 | 是 | - |
| video_size | int | 文件大小(字节) | 是 | - |
| video_format | string | 文件格式(目前应该全部是mp4) | 是 | - |
| video_duration | int | 文件播放时长(单位s) | 是 | - |
| video_url | string | 录制文件url | 是 | - |
| video_id | string | 点播后台返回的fileId字段 | 是 | - |
| video_type | int    | 视频流类型 0:摄像头视频 1:屏幕分享视频 2:白板视频 | 是 | - |
| user_id | string | 视频所属用户的id，白板视频时，user_id为空 | 是 | - |

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
"video_play_time":0
"video_size":1200,
"video_format":"mp4",
"video_duration":3600
"video_url":"http://1253488539.vod2.myqcloud.com/oM86K7X3Ig8b.mp4",
"video_id":"5285890781570653827",
"video_type":0,
"user_id":"ios_test1"
},
{
"video_play_time":4000
"video_size":3756,
"video_format":"mp4",
"video_duration":5000
"video_url":"http://1253488539.vod2.myqcloud.com/oM86K7X3IsdfA.mp4",
"video_id":"5285890781570653828",
"video_type":2,
"user_id":"pc_test1"
}
]
}
```

### 4.6 H5转码进度回调

添加课件接口的 `is_transcode` 字段，可以控制是否进行H5转码，H5转码可以将PPT中的动画效果，高度还原为H5页面，需要H5转码功能，需提前联系我们开通白名单

__event__

```
transport_progress
```

__data__ 

| 参数名 | 类型 | 描述 | 是否必填 | 默认值 |
|:--------|:-----|:-------|:-------|:-------|
| error_code | int | 错误码 | 是 | - |
| error_msg | string | 错误信息 | 是 | - |
| timestamp | int | 进度发生改变的真正时间戳，单位秒 | 是 | - |
| status | string | 任务状态 `queued`-正在排队/`processing`-转码中/`finished`-转码完成 | 是 | - |
| progress | int64 | 0-100的整数表示转码当前进度 | 是 | - |
| h5_url | string | 转码完成后H5的URL | 是 | - |
| resolution | string | PPT的分辨率 | 是 | - |
| pages | int | PPT的总页数 | 是 | - |
| title | string | PPT的文件名 | 是 | - |

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

## 附录

### 附录1: API公共参数
| 参数名 | 类型 | 描述 |
| :------ | :--- | :---- |
| sdkappid | int | 腾讯云账号下开通TRTC后，会得到一个唯一的项目标识sdkappid |
| random | int | 一个随机数，用于区分不同的请求,过滤日志等 |
| sign | string | API鉴权字符串 |

__举例__ 

预约课堂的完整API:

```
https://iclass.api.qcloud.com/paas/v1/class/create?sdkappid=1400127140&random=37926&sign=xxxxxxx
```

### 附录2: API鉴权算法

签名算法：md5(tic_key+expire_time)

|参数    |类型    | 描述|
|:---- | :---| :--- |
| tic_key | string | 创建企业时，下发的互动课堂API鉴权KEY |
| expire_time    | int64 |    签名的过期时间戳:当前时间戳+签名有效时间；每个请求包体中都必须带此字段 |

举例：
```
1. 当前时间戳是 1548247717
2. 签名有效时间是 120 秒，则过期时间戳是 1548247717+120=1548247837
3. tic_key是DzXpbluRsmo1JkoFxzKMNg5ifrA4GRlU
4. sign=md5(DzXpbluRsmo1JkoFxzKMNg5ifrA4GRlU1548247837)=28374bd8cff400ac4906414780fbe387
5. 在请求body中，带上expire_time字段，值为1548247837
6. 在请求url的参数中，带上sign=28374bd8cff400ac4906414780fbe387
```

### 附录3: 常量类型枚举值
#### 附录3.1 角色-role

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| superadmin | string | 超级管理员(申请创建企业时，设置的超级管理员) |
| admin | string | 普通管理员(需要使用腾讯云互动课堂控制台时需要关注) |
| teacher | string | 教师 |
| assistant | string | 助教 |
| student | string | 学生 |
| supervisor | string | 巡课员 |
| visitor | string | 游客 |

#### 附录3.2 录制类型-record_type

在约课时设置此字段，如果设置为remote，在`上课`后，后台会自动发起云端录制，录制结束后，会自动发起结束录制回调

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| local | string | 本地录制 |
| remote | string | 云端录制 |

#### 附录3.3 ~~视频分辨率-resolution~~
<font color=red>todo:当前版本不支持用互动课堂API设置分辨率</font>

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

#### 附录3.5 课堂类型-class_type

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| public | string | 公开课(所有人都可以进入) |
| 1v1 | string | 1v1课堂(只有指定的预约成员可以进入) |
| 1vN | string | 1vN小班课(只有指定的预约成员可以进入) |

#### 附录3.6 设备开关
设别包括：camera、mic、speaker等

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| 0 | int | 关闭 |
| 1 | int | 打开 |

#### 附录3.7 禁言-silence

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| 0 | int | 畅聊 |
| 1 | int | 禁言 |

#### 附录3.8 性别-gender

| 常量值 | 类型 | 描述 |
| -- | -- | -- |
| male | string | 男 |
| female | string | 女 |

#### 附录3.9 事件上报-event

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
| reward | string | 奖励 |
| slience | string | 禁言 |
| be_silenced | string | 被禁言 |
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
| jpg、png | 小于100KB,400x400 |
