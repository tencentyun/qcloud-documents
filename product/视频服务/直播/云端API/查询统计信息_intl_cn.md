
## 1.接口描述
- **接口**
   - **Get_LiveStat**：查询指定直播流的推流和播放信息
   - **Get_LivePushStat** ：仅返回推流统计信息以提高查询效率
   - **Get_LivePlayStat** ：仅返回播放统计信息以提高查询效率
- **地址**
   - API调用地址为： http://<font color='red'>statcgi.</font>video.qcloud.com/common_access
- **用途**
   - 查询某条直播流的统计信息（如观看人数、带宽、码率、帧率等等）
   - 查询当前正在直播状态中的若干条直播流的统计信息（建议采用分页查询避免单次回包数据过大）
- **说明**
   - 统计数据均为查询时间点的瞬时统计数据，而并非历史累计数据。
   - <font color='red'>如果目标流不在直播中，则返回结果中的output字段为空。</font>
   - 推流信息的统计数据每**5秒钟**更新一次，也就是快于5秒的查询频率是浪费的。
   - 播放信息的统计数据每**1分钟**更新一次，也就是快于60秒的查询频率是浪费的。
- **BETA**
   - 统计接口目前尚处于Beta阶段，并未全员放开，未开通即调用此接口会收到“<font color='red'>cmd is invalid </font>”提示，如您急需请联系我们。


## 2.输入参数

|        参数名        | 参数含义                                     | 类型     | 备注                                       | 是否必需 |
| :---------------: | ---------------------------------------- | ------ | ---------------------------------------- | :--: |
|        cmd        | 客户ID                                     | int    | 即直播APPID，用于区分不同客户的身份                     |  Y   |
|     interface     | 接口名称                                     | string | 如：Get_LivePushStat                       |  Y   |
|         t         | [有效时间](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | int    | UNIX时间戳(十进制)                             |  Y   |
|       sign        | [安全签名](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | string | MD5(key+t)                               |  Y   |
|  Param.n.page_no  | 分页页码                                     | int    | 从1开始，默认为1                                |  N   |
| Param.n.page_size | 分页大小                                     | int    | 1~300，默认为300                             |  N   |
| Param.s.stream_id | 直播码                                      | string | <font color='red'>如不设置stream_id：查询所有正在直播中的流</font> |  N   |


## 3.输出结果
### Get_LiveStat
| 参数名     | 参数含义 | 类型     | 备注          |
| ------- | ---- | ------ | ----------- |
| ret     | 返回码  | int    | 0:成功；其他值:失败 |
| message | 错误信息 | string | 错误信息        |
| output  | 消息内容 | array  | 详情见下        |

其中output的主要内容为：

| 字段名             | 含义               | 类型     | 备注                 |
| --------------- | ---------------- | ------ | ------------------ |
| stream_count    | 所有在线的直播流数量       | int    | 请求中指定stream_id时返回1 |
| stream_info     | 直播流统计信息          | array  | 详情见下               |
| total_bandwidth | 当前账号在查询时间点的总带宽   | double | 单位：Mbps            |
| total_online    | 当前账号在查询时间点的总在线人数 | int    | 单位：人               |

其中stream_info的主要内容为：

| 字段名         | 含义          | 类型     | 备注      |
| ----------- | ----------- | ------ | ------- |
| stream_name | 直播码         | string | -       |
| bandwidth   | 该直播流的瞬时带宽占用 | double | 单位：Mbps |
| online      | 该直播流的瞬时在线人数 | int    | 单位：人    |
| client_ip   | 推流客户端IP     | string | -       |
| server_ip   | 接流服务器IP     | string | -       |
| fps         | 瞬时推流帧率      | int    | -       |
| speed       | 瞬时推流码率      | int    | bps     |

### Get_LivePushStat
Get_LivePushStat 的 output 部分是 Get_LiveStat 的一个子集：

| 字段名          | 含义         | 类型    | 备注                 |
| ------------ | ---------- | ----- | ------------------ |
| stream_count | 所有在线的直播流数量 | int   | 请求中指定stream_id时返回1 |
| stream_info  | 直播流统计信息    | array | 详情见下               |

其中stream_info的主要内容为：

| 字段名         | 含义      | 类型     | 备注   |
| ----------- | ------- | ------ | ---- |
| stream_name | 直播码     | string | -    |
| client_ip   | 推流客户端IP | string | -    |
| server_ip   | 接流服务器IP | string | -    |
| fps         | 瞬时推流帧率  | int    | -    |
| speed       | 瞬时推流码率  | int    | bps  |

### Get_LivePlayStat
Get_LivePushStat 的 output 部分是 Get_LiveStat 的另一个子集：

| 字段名             | 含义               | 类型     | 备注                 |
| --------------- | ---------------- | ------ | ------------------ |
| stream_count    | 所有在线的直播流数量       | int    | 请求中指定stream_id时返回1 |
| stream_info     | 直播流统计信息          | array  | 详情见下               |
| total_bandwidth | 当前账号在查询时间点的总带宽   | double | 单位：Mbps            |
| total_online    | 当前账号在查询时间点的总在线人数 | int    | 单位：人               |

其中stream_info的主要内容为：

| 字段名         | 含义          | 类型     | 备注      |
| ----------- | ----------- | ------ | ------- |
| stream_name | 直播码         | string | -       |
| bandwidth   | 该直播流的瞬时带宽占用 | double | 单位：Mbps |
| online      | 该直播流的瞬时在线人数 | int    | 单位：人    |

## 4.调用示例

目标：查询当前账户名下所有正在直播的视频流的推流和播放信息

| 组成部分              | 示例内容                                     |
| ----------------- | ---------------------------------------- |
| 接口URL             | http://statcgi.video.qcloud.com/common_access? |
| cmd               | 1234                                     |
| interface         | Get_LiveStat                             |
| Param.n.page_no   | 1                                        |
| Param.n.page_size | 20                                       |
| t                 | 1471850187                               |
| sign              | b17971b51ba0fe5916ddcd96692e9fb3         |

```
// copy时请去掉美化排版用的不可见换行符，否则可能出现 “cmd is invalid” 等url拼装错误
URL = http://statcgi.video.qcloud.com/common_access?
			cmd=1234&interface=Get_LiveStat
			&Param.n.page_no=1
			&Param.n.page_size=20
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
```






