LogListener 是腾讯云日志服务 CLS 所提供的日志采集客户端，它将按照预设的采集策略实时上报日志数据，本篇文档将详细阐述 LogListener 的工作机制。

## 机制原理 
日志服务的 LogListener 成功部署之后，会对所关联的日志文件进行实时监听，主要通过文件系统修改的通知机制 Inotify 来感知目标日志文件的变化，这里的变化不仅是文件内容的变化，对于 Linux 系统而言，也包括文件 inode 发生改变。当 LogListener 感知到日志文件发生变化，就会主动采集上报新写入的日志，并记录当前位置。即使系统重启，也会从记录的位置继续采集日志。
![](https://main.qcloudimg.com/raw/db2059de9d116cf1df33ea4587af3910.png)

## 示例说明
为了更直观地说明日志服务 LogListener 采集策略，举例进行说明：
```shell
2018-01-01 10:00:01 echo log_1 >> cls.log
2018-01-01 10:00:02 start LogListener
2018-01-01 10:00:03 echo log_2 >> cls.log
2018-01-01 10:00:04 echo log_3 >> cls.log
2018-01-01 10:00:05 echo log_4 >> cls.log
......
```
在上述场景中，LogListener 将采集 log_2、log_3、log_4…… 到日志服务当中，即 LogListener 会以首次启动进程为时间点，自动监听上报该时间点之后的所有增量日志。注意，这里 LogListener 会监控到文件的 inode，若用 vim 修改日志文件 cls.log 时，由于 vim 机制会修改 inode，所以日志系统会认为是一个全新的日志文件，将会采集上报整个文件的内容。
>?
> - 机器重启后，会自动拉起 LogListener。
> - LogListener 进程挂掉重启后，会根据所记录的偏移位置继续上报日志。
> - 目前一个日志文件仅能上报到一个日志主题。若有多个日志主题关联到同一个日志文件，配置信息会覆盖，因此该日志文件实际只会上报到最后一个主题中。
