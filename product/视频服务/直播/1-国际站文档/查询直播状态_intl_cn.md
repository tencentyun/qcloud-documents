
## 1.接口描述
- **接口**
  - **Live_Channel_GetStatus**：用于查询某条流是否处于**正在直播**的状态

- **地址**
  - API调用地址为： http://<font color='red'>fcgi.</font>video.qcloud.com/common_access

- **用途**
  - 用于查询某条流是否处于**正在直播**的状态，其内部原理是基于腾讯云对音视频流的中断检测而实现的，因此实时性上可能不如APP的主动上报这么快速和准确，但在进行直播流定时清理检查的时候，可以作为一种不错的补充手段。

- **说明**
  - 如果要查询的推流直播码从来没有推过流，会返回<font color='red'>20601</font>错误码。

## 2.输入参数

| 参数名 | 参数含义 | 类型 | 备注 | 是否必需 |
|---------|---------|---------|---------|---------|
| cmd                        | 客户ID     | int       | 即直播APPID，用于区分不同客户的身份 |  Y          | 
| interface                 | 接口名称   | string |  如：Get_LivePushStat  |  Y          | 
| t | [有效时间](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | int  | UNIX时间戳(十进制) |  Y | 
| sign | [安全签名](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | string | MD5(key+t) | Y | 
| Param.s.channel_id | 直播码      | string | 一次只能查询一条直播流      | Y           |

> 有些早期提供的API中直播码参数被定义为channel_id，新的API则称直播码为stream_id，仅历史原因而已。

## 3.输出结果
| 参数名 | 参数含义 | 类型 | 备注            |
|---------|---------|---------|------------------|
| ret      | 返回码 |   int  |  0:成功；其他值:失败|
| message | 错误信息 |   string  |  错误信息|
| output | 消息内容 |   array  |  详情见下|

output的主要内容为：

| 字段名 | 含义 | 类型 | 备注            |
|---------|---------|---------|------------------|
| rate_type      | 码率 |   int  |  0:原始码率；10:普清；20:高清|
| recv_type      | 播放协议 |   int  |  1:rtmp/flv；2:hls；3:rtmp/flv+hls|
| status            | 状态 |   int  |  0:断流；1:开启；3:关闭|
 
## 4.调用示例

目标：查询直播码为8888_test123的直播流的当前状态是否是“正在直播中”。

| 组成部分 |   示例内容           |
|-------------|------------------|
|接口URL| http://fcgi.video.qcloud.com/common_access?|
|cmd       | 1234 |
|interface       | Live_Channel_GetStatus |
|Param.s.channel_id | 8888_test123 |
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
// copy时请去掉美化排版用的不可见换行符，否则可能出现 “cmd is invalid” 等url拼装错误
 URL = http://fcgi.video.qcloud.com/common_access?
			cmd=1234&interface=Live_Channel_GetStatus
			&Param.s.channel_id=8888_test123
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
```
     





