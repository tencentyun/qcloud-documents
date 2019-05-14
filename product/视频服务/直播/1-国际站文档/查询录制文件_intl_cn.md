
## 1.接口描述

- **接口**
  - **Live_Tape_GetFilelist**：用于查询某条直播流截止到调用时间为止已经生成的录制文件。

- **地址**
  - API调用地址为： http://<font color='red'>fcgi.</font>video.qcloud.com/common_access

- **说明**
  - 由于文件的落地时间对您不可知，所以这种主动查询接口在调用时机上并不是特别好掌握，更推荐使用[被动事件通知](https://cloud.tencent.com/doc/api/258/5957)（event_type = 100）机制。

## 2.输入参数

| 参数名 | 参数含义 | 类型 | 备注 | 是否必需 |
|---------|---------|---------|---------|---------|
| cmd                        | 客户ID     | int       | 即直播APPID，用于区分不同客户的身份 |  Y          | 
| interface                 | 接口名称   | string |  如：Get_LivePushStat  |  Y          | 
| t | [有效时间](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | int  | UNIX时间戳(十进制) |  Y | 
| sign | [安全签名](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | string | MD5(key+t) | Y | 
| Param.s.channel_id | 直播码 | string | | Y|
| Param.n.page_no   | 分页页码  | int  | 从1开始，默认为1 | N |
| Param.n.page_size | 分页大小 | int   |1~100，默认为10  | N |
|Param.s.sort_type  | 排序方式| string| asc表示升序，desc表示降序,默认arc|N|

> 有些早期提供的API中直播码参数被定义为channel_id，新的API则称直播码为stream_id，仅历史原因而已。

## 3.输出结果
| 参数名 | 参数含义 | 类型 | 备注            |
|---------|---------|---------|------------------|
| ret      | 返回码 |   int  |  0:成功；其他值:失败|
| message | 错误信息 |   string  |  错误信息|
| output | 消息内容 |   array  |  详情见下|

其中output的主要内容为：

| 字段名 | 含义 | 类型 | 备注                 |
|---------|---------|---------|------------------|
| all_count | 分片总个数    |   int      |    |
| file_list    | 分片文件信息 |   array  | 详情见下  |

其中file_list的主要内容为：

| 字段名 | 含义 | 类型 | 备注                 |
|---------|---------|---------|------------------|
| vid | 分片总个数    |  string      | 如果为空，则使用record_file_url |
| start_time   | 分片开始时间|   string  |   由于I帧位置原因，并不能精确到秒 |
| end_time    | 分片结束时间 |   string  |  由于I帧位置原因，并不能精确到秒  |
| file_id        | 点播file_id     |   string  |  需要用点播API换取播放URL|
| record_file_url | 播放地址|string | 如果不为空，则使用该地址  |

 
## 4.调用示例
目标：查询直播码为8888_test123的直播流在整个直播过程中所录制的文件列表。

| 组成部分 |   示例内容           |
|-------------|------------------|
|接口URL| http://fcgi.video.qcloud.com/common_access?|
|cmd       | 1234 |
|interface       | Live_Tape_GetFilelist |
|Param.s.channel_id | 8888_test123 |
|Param.n.page_no | 1 |
|Param.n.page_size | 20 |
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
// copy时请去掉美化排版用的不可见换行符，否则可能出现 “cmd is invalid” 等url拼装错误
URL = http://fcgi.video.qcloud.com/common_access?
			cmd=1234&interface=Live_Tape_GetFilelist
			&Param.s.channel_id=8888_test123
			&Param.n.page_no=1
			&Param.n.page_size=20
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
```
			





