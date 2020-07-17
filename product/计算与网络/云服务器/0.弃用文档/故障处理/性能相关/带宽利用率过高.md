当发现实例带宽利用率过高时，往往希望能够具体定位出是哪一个进程占用了带宽，进而进行相应的分析处理。本文将介绍 Linux 和 Windows 系统下如何使用对应的工具进行定位处带宽使用高的进程。

## Linux下查看进程的带宽使用情况
### NetHogs 介绍
NetHogs 是 Linux 平台下的一个开源命令行工具，用来实时统计各进程的带宽使用情况。在 CentOS 下可以使用如下命令进行安装：
```
yum install nethogs
```

### NetHogs 使用方法
终端输入以下命令可以看到 NetHogs 的可用参数以及具体用法。
```
nethogs -h
```
![](https://mc.qcloudimg.com/static/img/1a5bda1babaa86e7200f7a055023c46c/image.png)
下面介绍下常用的参数：
- **-d**：设置刷新的时间间隔，默认为 1s。
- **-t**：跟踪模式。
- **-c**：更新次数。
- **device**：设置要监控的网卡，默认是 eth0。

运行时可以输入以下参数完成相应的操作：
- **q**：退出。
- **s**：按发送流量进行排序。
- **r**：按接收流量进行排序。
- **m**：切换是显示各进程使用的网络速率亦或是使用的流量，或者使用流量的计量单位。切换顺序为 KB/s > KB > B > MB。

下图展示了在 Linux 实例上运行 **nethogs -d 10** 并按发送数据量进行排序的结果，以此为示例，介绍 NetHogs 的输出。通过切换按发送/接收流量排序，可以很方便的获取占用发送/接收流量较多的进程。
![](https://mc.qcloudimg.com/static/img/9a863640f0860a939b0a5c159522d01c/image.png)
PID：进程 ID。
USER：运行该进程的用户。
PROGRAM：程序名或IP端口号。
DEV：流量要去往的网络接口。
SENT：进程每秒发送的数据量。
RECEIVED：进程每秒接收的数据量。

## Windows下查看进程的带宽使用情况
### Windows 资源监视器
资源监视器是 Windows下以进程为单位了解 CPU、内存、磁盘、网络等资源的使用情况的工具。
可以在任务管理器，性能 tab 单击打开资源监视器打开。
![](https://mc.qcloudimg.com/static/img/0a70336ea3803db7edd4832ba4a1b6aa/image.png)
或者在运行中输入 **resmon.exe**，确定打开
![](https://mc.qcloudimg.com/static/img/05a6b6d8373f64c6dddf090ae1a7f767/image.png)
单击资源监视器的网络 tab，就可以看到每个进程的带宽使用情况。单击发送，按发送数据量进行排序，单击接收按照接收数据量进行排序。排序后，可以方便的看到具体是哪个进程占用了网络资源。
![](https://mc.qcloudimg.com/static/img/3a73f5d36165ad82dbacdacc449aa93a/image.png)

## 结果分析及处理
知道占用资源较多的进程后，需要分析进程所属的类型，然后进行：
1. 分析是否正常进程（系统进程/业务进程/腾讯云的常见进程）起。如果无法完全确认，建议使用进程名进程搜索确认。

2. 如果是异常进程，实例可能中毒，可以自行终止进程、使用安全软件进行查杀或者进行数据备份后，重装系统。

3. 如果为腾讯云组件进程，请 [发起工单](https://console.cloud.tencent.com/workorder/category) 联系我们进行进一步定位处理。
常见的腾讯云组件有：
 - sap00x：安全组件进程
 - Barad_agent：监控组件进程
 - secu-tcs-agent：安全组件进程

4. 正常的业务进程，分析是否有大量的网络访问行为，是否通过压缩文件解决网络带宽的资源瓶颈。否则建议升级实例配置。带宽配置升级详情见 [变更配置](https://cloud.tencent.com/document/product/644/12629)。
