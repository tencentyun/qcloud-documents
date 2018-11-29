
## 1.接口描述

- **接口**
  - **Live_Channel_SetStatus**：开启或者关闭一个直播流的**可推流**状态。

- **地址**
  - API调用地址为： http://<font color='red'>fcgi.</font>video.qcloud.com/common_access

- **用途**
  - 主要用于鉴黄时的**禁播**场景，比如您如果在后台发现某个主播有涉黄或者反动内容，可以随时关闭这个直播流。

- **说明**
  - 一条直播流一旦被设置为“关闭”状态，推流链路将被腾讯云主动断开，并且后续的推流请求也会被拒绝。

## 2.输入参数

| 参数名 | 参数含义 | 类型 | 备注 | 是否必需 |
|---------|---------|---------|---------|---------|
| cmd                        | 客户ID     | int       | 即直播APPID，用于区分不同客户的身份 |  Y          | 
| interface                 | 接口名称   | string |  如：Get_LivePushStat  |  Y          | 
| t | [有效时间](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | int  | UNIX时间戳(十进制) |  Y | 
| sign | [安全签名](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | string | MD5(key+t) | Y | 
| Param.s.channel_id | 直播码 | string | | Y|
| Param.n.status | 开关状态 | int | 0:关闭； 1:开启 | Y|

> 有些早期提供的API中直播码参数被定义为channel_id，新的API则称直播码为stream_id，仅历史原因而已。

## 3.输出结果
| 参数名 | 参数含义 | 类型 | 备注            |
|---------|---------|---------|------------------|
| ret      | 返回码 |   int  |  0:成功；其他值:失败|
| message | 错误信息 |   string  |  错误信息|
 
## 4.调用示例
目标：考虑到直播码为8888_test123的直播流内容涉及违规内容，对其进行禁播操作。

| 组成部分 |   示例内容           |
|-------------|------------------|
|接口URL| http://fcgi.video.qcloud.com/common_access?|
|cmd       | 1234 |
|interface       | Live_Channel_SetStatus |
|Param.s.channel_id | 8888_test123 |
|Param.n.status | 0 |
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
// copy时请去掉美化排版用的不可见换行符，否则可能出现 “cmd is invalid” 等url拼装错误
 URL = http://fcgi.video.qcloud.com/common_access?
			cmd=1234&interface=Live_Channel_SetStatus
			&Param.s.channel_id=8888_test123
			&Param.n.status=0
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
```







