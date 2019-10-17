
## 1.接口描述

- **接口**
  - **Live_Queue_Get**：查询直播中的频道新产生的截图文件。

- **地址**
  - API调用地址为： http://<font color='red'>fcgi.</font>video.qcloud.com/common_access

- **用途**
  - 腾讯云提供针对视频直播的定时截图服务，您在开启此服务后，可以每隔几秒获得一张直播流的截图文件。
  - 我们的客户经常会使用这套服务进行鉴黄，或者游戏直播客户用其定时更新网页上的直播封面。

- **说明**
  - 截图文件有生成频率高、文件数量多的特点，尤其是当直播频道很多的时候，所以腾讯云以消息队列的形式对客户提供查询服务。
  - **消息队列**是一个截图文件队列，您的直播频道每产生一个新的截图图片，图片ID和对应的直播码会以消息的形式塞入您的专属消息队列中，您可以定时地调用该API，每次调用都可以把最新产生的截图消息取走。
  - <font color='red'>截图服务非全开放服务</font>，仅为大客户提供接口支持，未开通截图相关服务前此API调用无效。

- **历史**
  - Live_Queue_Get 原计划用于取走各种类型的消息，但后来随着[通知机制](https://cloud.tencent.com/doc/api/258/5957)渐渐被很多客户接受，这种方式并没有太多的拓展出去，目前使用该服务主要用于为截图这种高频事件服务。


## 2.输入参数

| 参数名 | 参数含义 | 类型 | 备注 | 是否必需 |
|---------|---------|---------|---------|---------|
| cmd                        | 客户ID     | int       | 即直播APPID，用于区分不同客户的身份 |  Y          | 
| interface                 | 接口名称   | string |  如：Get_LivePushStat  |  Y          | 
| t | [有效时间](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | int  | UNIX时间戳(十进制) |  Y | 
| sign | [安全签名](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | string | MD5(key+t) | Y | 
| Param.n.bid   | 消息队列id  | int  | 100：为截图的专属队列id | Y |
| Param.n.count | 一次获取的消息数量 | int   |1~100，默认为1 | N |

## 3.输出结果
| 参数名 | 参数含义 | 类型 | 备注            |
|---------|---------|---------|------------------|
| ret      | 返回码 |   int  |  0:成功；其他值:失败|
| message | 错误信息 |   string  |  错误信息|
| output | 消息内容 |   array  |  详情见下|

其中output的主要内容为：

| 字段名 | 含义 | 类型 | 备注                 |
|---------|---------|---------|------------------|
| count | 数量    |   int      |    |
| data    | 截图URL列表 |   array  | 详情见下  |

其中data部分的主要内容为：

| 字段名 | 含义 | 类型 | 备注                 |
|---------|---------|---------|------------------|
| stream_id | 直播码    |   string      |            |
| pic_url   | 截图URL|   string  |   完整的url为: http://(cos_bucketname)-(cos_appid).file.myqcloud.com/文件名|
| create_time | 截图时间 |   int  |  由于I帧位置原因，并不能精确到秒  |

## 4.调用示例

目标：查询您当前账户下所有直播频道新生成的截图文件

| 组成部分 |   示例内容      |
|-------------|------------------|
|接口URL| http://fcgi.video.qcloud.com/common_access?|
|cmd       | 1234 |
|interface       | Live_Queue_Get |
|Param.n.bid | 100 |
|Param.n.count | 10 |
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
// copy时请去掉美化排版用的不可见换行符，否则可能出现 “cmd is invalid” 等url拼装错误
URL = http://fcgi.video.qcloud.com/common_access?
			cmd=1234&interface=Live_Queue_Get
			&Param.n.bid=100
			&Param.n.count=10
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
```
			
			






