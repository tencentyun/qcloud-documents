## 概述
Loglistener 服务日志功能提供采集端运行状态、工作状态、采集流量等数据的监控，支持记录 Loglistener 端运行状态和采集监控的日志数据并配置可视化视图，提供重要指标数据，便于用户观测了解 Loglistener 的运行状态和日志采集统计情况。

#### 默认配置

| 默认配置项   | 配置内容                                                     |
| ------------ | ------------------------------------------------------------ |
| 日志主题     | 当 Loglistener 服务日志开启时，会自动为您创建一个 cls_service_logging 日志集，将所有关联的机器组所产生的日志数据都分类保存到对应的日志主题中。默认为您创建以下3个日志主题：<li>loglistener_status：对应内部 Loglistener 心跳状态的日志。</li><li>loglistener_alarm：对应 Loglistener 采集指标/错误类型的监控日志。</li><li>loglistener_business ：对应 Loglistener 采集的操作日志，每条日志对应一次请求。</li> |
| 地域         | 开启 Loglistener 日志服务时，默认在同地域机器组下创建日志集和日志主题 。|
| 日志主题分区 | 每个日志主题默认创建一个主题分区，不开启自动分裂日志主题分区功能。详情请查看 [分裂主题分区](https://cloud.tencent.com/document/product/614/52204)。 |
| 日志存储时间 | 默认保存7天，不支持修改存储时间。                            |
| 索引         | 默认为采集到的所有日志数据开启全文索引和键值索引。支持修改索引配置，如果没有检索分析和监控告警等需求，可以在日志主题索引配置中关闭索引。详情请查看 [配置索引](https://cloud.tencent.com/document/product/614/50922)。 |
| 仪表盘       | 默认创建一个同地域下的仪表盘 service_log_dashboard。          |

>?
> - Loglistener 服务日志专属用于 Loglistener 采集监控产生的日志，不支持写入其他数据。
> - Loglistener 服务日志功能产生的日志数据不产生费用。
> - cls_service_logging 为统一的 Loglistener 服务日志的日志集

## 应用场景

- **查看 Loglistener 状态**
开通 Loglistener 服务日志功能后，用户可以查看 Loglistener 运行状态和采集统计情况。用户可以通过 service_log_dashboard 仪表盘，查看活跃 Loglistener 数、Loglistener 状态分布等统计指标。

- **采集端监控配置**
  用户可以按指标/错误类型，配置采集端监控指标，例如：
  - 根据 MEM、CPU、采集速度、采集延时等指标进行监控。
  - 根据 Loglistener 解析错误次数的维度进行监控。

## 前提条件

机器 IP 配置机器组仅在 LogListener 2.5.4 及以上版本支持采集监控服务日志，您可前往升级至 [最新版本](https://cloud.tencent.com/document/product/614/17414)。

## 操作步骤
### 开通服务日志

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中单击【机器组管理】，进入机器组列表页。
3. 在机器组列表页，选择目标机器组，单击![](https://main.qcloudimg.com/raw/f49ecfc95ee483de28fb0928a4ada2dd.png)，即可开启 Loglistener 服务日志。
![](https://main.qcloudimg.com/raw/5dea5c8e51a0aaf92d85be9652baf59c.png)

### 关闭服务日志

1. [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中单击【机器组管理】，进入机器组列表页。
3.  在机器组列表页，选择目标机器组，单击![](https://main.qcloudimg.com/raw/b9a30517065edbe87527257fcc100184.png)，即可关闭 Loglistener 服务日志。

>?关闭服务日志功能后，日志集 cls_service_logging 中保存的日志数据不会自动删除，如果您需要删除这部分日志数据，可以手动删除保存服务日志的日志集。

## 日志类型

### Loglistener 状态日志
日志主题 Loglistener_status 的字段具体说明如下：

| 字段                  | 描述                               |
| :-------------------- | :--------------------------------- |
| AvailConnectNum       | 当前正在工作的连接数               |
| CpuUsage              | 组件 CPU 使用率                      |
| InstanceId            | Loglistener 唯一标识值              |
| Label                 | 机器标示 Array                     |
| IP                    | 机器组 IP                           |
| MemUsed               | 组件内存使用情况                   |
| MemMax                | agent 在该机器上设置的内存使用阈值  |
| QueueSize             | 当前排队请求总数                   |
| SendAvgCost           | 发送成功请求的平均耗时           |
| SendAvgReqSize        | 发送成功请求的平均传输日志量     |
| SendFailedLogEntry    | 发送失败日志总条数（non-200 rsp） |
| SendFailedLogSize     | 发送失败日志量大小（non-200 rsp） |
| SendFailedReqs        | 发送失败请求数（non-200 rsp）    |
| SendSuccessReqs       | 发送成功的请求数                  |
| SendSuccessLogEntry   | 发送成功日志总条数               |
| SendSuccessAllTime    | 发送成功请求总耗时                |
| SendSuccessLogSize    | 发送成功日志量大小               |
| SendTimeoutLogSize    | 发送超时日志量大小                |
| SendTimeoutReqs       | 发送超时请求数                   |
| SendTimeoutLogEntry   | 发送超时日志总条数               |
| Status                | loglistener 运行状态                |
| TotalFiniRsp          | 收到的 rsq 总数                      |
| TotalParseEntry       | 解析日志总条数                     |
| TotalParseFailedEntry | 解析日志失败总条数                 |
| TotalSendLogSize      | 发送日志量大小                     |
| TotalSendReq          | 发送总请求数                       |
| TotalSendLogEntry     | 发送日志总条数                     |
| Version               | 版本号                             |
| TimeFormatFailed      | 时间窗口内，时间戳匹配错误次数     |


### Loglistener 告警日志
日志主题 Loglistener_alarm 的字段具体说明如下：

| 字段         | 监控指标分类          |
| :----------- | :-------------------- |
| InstanceId   | Loglistener 唯一标识值 |
| Label        | 机器标示 Array        |
| IP           | 机器组 IP              |
| Version      | Loglistener 版本      |
| AlarmMessage | 触发告警原始日志采样  |
| Alarmcount   | 告警次数              |
| HostName     | 主机 hostname          |
| AlarmType    | 告警类型              |

**AlarmType ：**

| alarm type                | type ID | 描述                                      |
| :------------------------ | :------ | :---------------------------------------- |
| CLS_UNKNOWN_ERR           | 0       | 初始化 alarm 类型                           |
| CLS_PARSE_FAILURE         | 1       | 解析失败                                  |
| CLS_CRED_INVALID          | 2       | 认证失败                                  |
| CLS_SEND_FAILURE          | 3       | 发送失败                                  |
| CLS_RUN_EXCEPTION         | 4       | agent 运行异常                             |
| CLS_MEM_LIMITED           | 5       | 触发 mem limited 限制                       |
| CLS_FILE_PROC_EXP         | 6       | 文件处理异常                              |
| CLS_FILE_POS_GET_ERR      | 7       | 获取 file pos 失败                          |
| CLS_HOST_IP_EXP           | 8       | host ip 线程异常                           |
| CLS_STAT_EXP              | 9       | 获取进程相关信息异常                      |
| CLS_UPDATE_EXP            | 10      | cls update 功能异常                       |
| CLS_DOSEND_ERR            | 11      | dosend 失败                               |
| CLS_FILE_ADD_ERR          | 12      | addFileToReadyList get file realpath fail |
| CLS_FILE_META_ERR         | 13      | addFileToReadyList metadata not found     |
| CLS_FILE_OPEN_ERR         | 14      | open file 失败                             |
| CLS_FILE_READ_ERR         | 15      | read file 失败                             |
| CLS_FILE_STAT_ERR         | 16      | stat file 失败                             |
| CLS_GETTIME_ERR           | 17      | getTimeFromLogContent 失败                |
| CLS_HANDLE_EVENT_EXP      | 18      | handle file event 异常                    |
| CLS_HANDLE_FILECREATE_ERR | 19      | handleFileCreateEvent() 异常              |
| CLS_LINEPARSE_ERR         | 20      | log item 解析失败                          |
| CLS_LZ4_COMPRESS_ERR      | 21      | 压缩失败                                  |
| CLS_READ_EVENT_EXP        | 22      | readEvent 失败                             |
| CLS_READFILE_BUGON        | 23      | 触发 bugon                                 |
| CLS_READFILE_EXP          | 24      | procReadyFile() 异常                      |
| CLS_READFILE_INODE_CHANGE | 25      | file inode changed                        |
| CLS_READFILE_TRUNCATE     | 26      | file truncated                            |
| CLS_WILDCARDPATH_EXP      | 27      | addWildcardPathInotify() 异常             |
| CLS_ALARM_MAX             | 28      |                                           |

###  Loglistener 采集日志
日志主题 Loglistener_business 的字段具体说明如下：

| 字段             | 描述                                                         |
| :--------------- | :----------------------------------------------------------- |
| InstanceId       | Loglistener 唯一标识值                                        |
| Label            | 机器标示 Array                                               |
| IP               | 机器组 IP                                                    |
| Version          | Loglistener 版本                                             |
| ConfigName       | Loglistener 采集配置名称（暂时没有）                         |
| FileInode        | 文件 inode                                                    |
| FileName         | 文件路径名                                                   |
| FileSize         | 文件大小                                                     |
| LastReadTime     | 上次读取文件的时间（unix时间戳）                             |
| TopicID          | 文件采集到的目标 topic                                        |
| Version          | Loglistener 版本                                             |
| ParseFailedCount | 时间窗口解析失败条数                                         |
| ReadAvgDelay     | 时间窗口内，平均每次读取日志数据时，当前偏移量与文件大小差值的平均值 |
| ReadCount        | 时间窗口内读日志的条数                                       |
| ReadSize         | 时间窗口内，读取的总数据大小                                 |
| ReadOffset       | 读取文件的偏移量，单位字节                                   |
| SendFailedReq    | 时间窗口内，发送失败的次数                                   |
| SendCountReq     | 时间窗口内，发送的次数                                       |
| SendSuccessReq   | 时间窗口内，发送成功的次数                                   |
| SendCountEntry   | 时间窗口内，发送的日志条数                                   |
| SendSuccessEntry | 时间窗口内，发送成功的日志条数                               |
| TimeFormatFailed | 时间窗口内，时间戳匹配错误次数                               |
| TotalErrorCount  | 时间窗口内，各种采集错误的总次数                             |



## 服务日志仪表盘

开启 Loglistener 服务日志后，日志服务系统会根据记录的日志类型自动创建可视化仪表盘 search_log_dashboard，展示 Loglistener 采集监控统计。

#### 采集统计仪表盘
您可以在日志服务控制台的 [仪表盘](https://console.cloud.tencent.com/cls/dashboard) 页面，单击目标仪表盘的 ID，查看 Loglistener 采集相关的统计信息，包括 Loglistener 状态展示、Loglistener 解析失败率、Loglistener 发送成功率等指标信息。
![](https://main.qcloudimg.com/raw/a833495d8d661b5b34138fa1476720fe.png)


