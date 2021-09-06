## 概述
LogListener 服务日志功能支持记录 LogListener 端运行状态和采集监控的日志数据并配置可视化视图，提供重要指标数据，便于用户观测了解 LogListener 的运行状态和日志采集统计情况。

#### 默认配置

| 默认配置项   | 配置内容                                                     |
| ------------ | ------------------------------------------------------------ |
| 日志主题     | 当 LogListener 服务日志开启时，会自动为您创建一个 cls_service_logging 日志集，将所有关联的机器组所产生的日志数据都分类保存到对应的日志主题中。默认为您创建以下3个日志主题：<li>loglistener_status：对应 LogListener 的心跳状态日志。</li><li>loglistener_alarm：对应 LogListener 的采集指标/错误类型监控日志。</li><li>loglistener_business ：对应 LogListener 的采集操作日志，每条日志对应一次请求。</li> |
| 地域         | 开启 LogListener 日志服务时，默认在同地域机器组下创建日志集和日志主题 。|
| 日志存储时间 | 默认保存7天，不支持修改存储时间。                            |
| 索引         | 默认为采集到的所有日志数据开启全文索引和键值索引。支持修改索引配置，详情请查看 [配置索引](https://cloud.tencent.com/document/product/614/50922)。 |
| 仪表盘       | 默认创建一个同地域下的仪表盘 service_log_dashboard。          |

>?
> - LogListener 服务日志专属用于 LogListener 采集监控产生的日志，不支持写入其他数据。
> - LogListener 服务日志功能产生的日志数据不产生费用。
> - cls_service_logging 为统一的 LogListener 服务日志的日志集

## 应用场景

- **查看 LogListener 状态**
开通 LogListener 服务日志功能后，您可以查看 LogListener 运行状态和采集统计情况。用户可以通过 service_log_dashboard 仪表盘，查看活跃 LogListener 数、LogListener 状态分布等统计指标。

- **采集端监控配置**
您可以按指标/错误类型，配置采集端监控指标，例如：
  - 根据 MEM、CPU、采集速度、采集延时等指标进行监控。
  - 根据 LogListener 解析错误次数的维度进行监控。

- **文件级监控**
开通 Loglistener 服务日志功能后，您可以查看文件及目录的监控日志，例如：
  - 某个 IP 上所有文件的采集统计文件。
  - 某个 IP 上某个路径下的采集日志量情况，如 app1 应用日志位于/var/log/app1/，统计这个路径下的日志采集情况。
  - 某个 topic 的采集统计情况。


## 前提条件

配置机器 IP/标识机器组仅在 LogListener 2.5.4 及以上版本支持采集监控服务日志，您可前往升级至 [最新版本](https://cloud.tencent.com/document/product/614/17414)。

## 操作步骤
### 开通服务日志

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中单击【机器组管理】，进入机器组列表页。
3. 在机器组列表页，选择目标机器组，单击![](https://main.qcloudimg.com/raw/f49ecfc95ee483de28fb0928a4ada2dd.png)，即可开启 LogListener 服务日志。
![](https://main.qcloudimg.com/raw/5dea5c8e51a0aaf92d85be9652baf59c.png)

### 关闭服务日志

1. [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中单击【机器组管理】，进入机器组列表页。
3.  在机器组列表页，选择目标机器组，单击![](https://main.qcloudimg.com/raw/b9a30517065edbe87527257fcc100184.png)，即可关闭 LogListener 服务日志。

>? 关闭服务日志功能后，日志集 cls_service_logging 中保存的日志数据不会自动删除，如果您需要删除这部分日志数据，可以手动删除保存服务日志的日志集。
>

## 服务日志仪表盘

开启 LogListener 服务日志后，日志服务系统会根据记录的日志类型自动创建可视化仪表盘 service_log_dashboard，展示 LogListener 采集监控统计。

#### 采集统计仪表盘
您可以在日志服务控制台的 [仪表盘](https://console.cloud.tencent.com/cls/dashboard) 页面，单击目标仪表盘的 ID，查看 LogListener 采集相关的统计信息，包括 LogListener 状态展示、LogListener 解析失败率、LogListener 发送成功率等指标信息。
![](https://main.qcloudimg.com/raw/a833495d8d661b5b34138fa1476720fe.png)

## 日志类型

### LogListener 状态日志
日志主题 Loglistener_status 的字段具体说明如下：
<table>
	<tr><th>字段</th><th>描述</th></tr>
	<tr><td>InstanceId</td><td>LogListener 唯一标识值</td></tr>
	<tr><td>IP</td><td>机器组 IP</td></tr>
	<tr><td>Label</td><td>机器标识数组</td></tr>
	<tr><td>Version</td><td>版本号</td></tr>
	<tr><td>MemoryUsed</td><td>组件内存使用情况</td></tr>
	<tr><td>MemMax</td><td>Agent 在该机器上设置的内存使用阈值</td></tr>
	<tr><td>CpuUsage</td><td>组件 CPU 使用率</td></tr>
	<tr><td>Status</td><td>LogListener 运行状态</td></tr>
	<tr><td>TotalSendLogSize</td><td>发送日志量大小</td></tr>
	<tr><td>SendSuccessLogSize</td><td>发送成功日志量大小</td></tr>
	<tr><td>SendFailureLogSize</td><td>发送失败日志量大小</td></tr>
	<tr><td>SendTimeoutLogSize</td><td>发送超时日志量大小</td></tr>
	<tr><td>TotalParseLogCount</td><td>解析总日志条数</td></tr>
	<tr><td>ParseFailureLogCount</td><td>解析失败日志条数</td></tr>
	<tr><td>TotalSendLogCount</td><td>总发送日志条数</td></tr>
	<tr><td>SendSuccessLogCount</td><td>发送成功日志条数</td></tr>
	<tr><td>SendFailureLogCount</td><td>发送失败日志条数</td></tr>
	<tr><td>SendTimeoutLogCount</td><td>发送超时日志条数</td></tr>
	<tr><td>TotalSendReqs</td><td>总发送请求数</td></tr>
	<tr><td>SendSuccessReqs</td><td>发送成功请求数</td></tr>
	<tr><td>SendFailureReqs</td><td>发送失败请求数</td></tr>
	<tr><td>SendTimeoutReqs</td><td>发送超时请求数</td></tr>
	<tr><td>TotalFinishRsps</td><td>收到的全部 .rsp 文件</td></tr>
	<tr><td>TotalSuccessFromStart</td><td>LogListener 启动到现在总的成功数</td></tr>
	<tr><td>AvgReqSize</td><td>平均请求包大小</td></tr>
	<tr><td>SendAvgCost	</td><td>平均发送耗时</td></tr>
	<tr><td>AvailConnNum</td><td>可用连接数</td></tr>
	<tr><td>QueueSize</td><td>排队请求大小</td></tr>
</table>





### LogListener 告警日志
日志主题 Loglistener_alarm 的字段具体说明如下：

| 监控指标分类         | 描述          |
| :----------- | :-------------------- |
| InstanceId   | LogListener 唯一标识值 |
| Label        | 机器标识数组        |
| IP           | 机器组 IP              |
| Version      | LogListener 版本      |
| AlarmType.count | 告警类型统计  |
| AlarmType.example   | 告警类型样例              |


**AlarmType ：**

| alarm type                | type ID | 描述                                      |
| :------------------------ | :------ | :---------------------------------------- |
| UnknownError           | 0       | 初始化 alarm 类型                           |
| UnknownError         | 1       | 解析失败                                  |
| CredInvalid          | 2       | 认证失败                                  |
| SendFailure          | 3       | 发送失败                                  |
| RunException         | 4       | LogListener 运行异常                             |
| MemLimited           | 5       | 触发 mem limited 限制                       |
| FileProcException         | 6       | 文件处理异常                              |
| FilePosGetError      | 7       | 获取 file pos 失败                          |
| HostIpException           | 8       | host IP 线程异常                           |
| StatException              | 9       | 获取进程相关信息异常                      |
| UpdateException            | 10      | cls update 功能异常                       |
| DoSendError            | 11      | dosend 失败                               |
| FileAddError          | 12      | 文件新增失败 |
| FileMetaError         | 13      | 元数据文件新增失败     |
| FileOpenError         | 14      | open file 失败                             |
| FileReadError         | 15      | read file 失败                             |
| FileStatError         | 16      | stat file 失败                             |
| GetTimeError           | 17      | getTimeFromLogContent 失败                |
| HandleEventError      | 18      | handle file event 异常                    |
| HandleFileCreateError | 19      | handleFileCreateEvent() 异常              |
| LineParseError         | 20      | log item 解析失败                          |
| Lz4CompressError      | 21      | 压缩失败                                  |
| ReadEventException        | 22      | readEvent 失败                             |
| ReadFileBugOn        | 23      | 触发 bugon                                 |
| ReadFileException          | 24      | procReadyFile() 异常                      |
| ReadFileInodeChange | 25      | file inode 发生变化                        |
| ReadFileTruncate     | 26      | Readfile 截断                          |
| WildCardPathException      | 27      | addWildcardPathInotify() 异常             |


###  LogListener 采集日志
日志主题 Loglistener_business 的字段具体说明如下：

<table>
	<tr><th>字段</th><th>描述</th></tr>
	<tr><td>InstanceId</td><td>LogListener 唯一标识值</td></tr>
	<tr><td>Label</td><td>机器标识数组</td></tr>
	<tr><td>IP</td><td>	机器组 IP</td></tr>
	<tr><td>Version</td><td>LogListener 版本</td></tr>
	<tr><td>TopicId</td><td>文件采集到的目标 topic</td></tr>
	<tr><td>FileName</td><td>文件路径名</td></tr>
	<tr><td>RealPath</td><td>文件实际路径</td></tr>
	<tr><td>FileInode</td><td>文件 inode</td></tr>
	<tr><td>FileSize</td><td>文件大小</td></tr>
	<tr><td>LastReadTime</td><td>上次读取文件时间</td></tr>
	<tr><td>ParseFailLines</td><td>时间窗口，解析失败日志条数</td></tr>
	<tr><td>ParseFailSize</td><td>时间窗口，解析失败日志大小</td></tr>
	<tr><td>ParseSuccessLines</td><td>时间窗口，解析成功日志条数</td></tr>
	<tr><td>ParseSuccessSize</td><td>时间窗口，解析成功日志大小</td></tr>
	<tr><td>ReadOffset</td><td>读取文件的偏移量，单位字节</td></tr>
	<tr><td>TruncateSize</td><td>时间窗口内，truncate 的文件大小</td></tr>
	<tr><td>ReadAvgDelay</td><td>时间窗口内，读取平均时延</td></tr>
	<tr><td>TimeFormatFailuresLines</td><td>时间窗口内，时间戳匹配错误次数</td></tr>
	<tr><td>SendSuccessSize</td><td>时间窗口内，发送成功日志大小</td></tr>
	<tr><td>SendSuccessCount</td><td>时间窗口内，发送成功日志条数</td></tr>
	<tr><td>SendFailureSize</td><td>时间窗口内，发送失败日志大小</td></tr>
	<tr><td>SendFailureCount</td><td>时间窗口内，发送失败日志条数</td></tr>
	<tr><td>SendTimeoutSize</td><td>时间窗口内，发送超时日志大小</td></tr>
	<tr><td>SendTimeoutCount</td><td>时间窗口内，发送超时日志条数</td></tr>
	<tr><td>DroppedLogSize</td><td>时间窗口内，丢掉日志大小</td></tr>
	<tr><td>DroppedLogCount</td><td>时间窗口内，丢掉日志条数</td></tr>
	<tr><td>ProcessBlock</td><td>标记一个统计周期内，当前文件是否触发过采集阻塞（一个文件的滑动窗口10分钟未移动过，即为触发）</td></tr>
</table>

