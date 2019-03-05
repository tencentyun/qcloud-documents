
本文档介绍 Linux 云服务器因 CPU 与内存占用率高导致无法登录等问题的排查方法和解决方案。

## 登录与查看系统负载

 1. 登录云服务器。
	- 通过第三方软件远程登录 Linux 云服务器（ Linux 云服务器处于 CPU 高负荷状态时，可能出现无法登录状态）。

	- 通过 [控制台](https://console.cloud.tencent.com/cvm) 登录云服务器（ Linux 云服务器处于 CPU 高负荷状态时，控制台能正常登录）。

 2. 查看系统负载。
 输入 ` top ` 命令，查看 `%CPU` 列与 `%MEM` 列，确定占用较多资源的进程。

## 终止进程操作

 1. 分析列出资源占用情况，记录需要终止的进程 PID 。

 2. 输入` k `，再输入需要终止进程的 PID ，回车终止。此处以终止 PID 为 23 的进程为例。
![](//mc.qcloudimg.com/static/img/61cd74354cf2b4d2a80a83528a500f5c/image.png)
 >**注意:**
 >若回车后出现`kill PID 23 with signal [15]:`，则继续回车使用默认设定即可。

 3. 操作成功后，界面会出现` Send pid 23 signal [15/sigterm] ` 的提示信息。按回车确认即可。

## CPU 空闲但高负载情况处理
** 问题描述：**
&nbsp;&nbsp;&nbsp;&nbsp;load average 是 CPU 负载的评估，其值越高，说明其任务队列越长，处于等待执行的任务越多。
&nbsp;&nbsp;&nbsp;&nbsp;通过 top 观察，类似如下图所示，CPU 很空闲，但是 load average 却非常高。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](//mc.qcloudimg.com/static/img/4ddf663a68ee602d8cf8075d88edccf6/image.png)
 
** 处理办法：**
 
 1. 输入` ps -axjf `指令查看进程状态。查看是否存在 D 状态进程。（D 状态是指不可中断的睡眠状态。该状态进程无法被杀死，也无法自行退出。）
![](//mc.qcloudimg.com/static/img/32420d3fe022b57d85120c941705dbf6/image.png)

 2. 若出现较多 D 状态进程，通过恢复该进程依赖资源或重启系统解决。


## kswapd0 进程占用 CPU 较高处理
** 问题描述： **
Linux 系统通过分页机制管理内存的同时，将磁盘的一部分划出来作为虚拟内存。而 kswapd0 是 Linux 系统虚拟内存管理中负责换页的进程。当系统内存不足时，kswapd0 会频繁的进行换页操作。换页操作非常消耗 CPU 资源，导致该进程持续占用高 CPU 资源。
 
** 处理办法： **
 1. 输入` top `指令，找到 kswapd0 进程。

 2. 观察 kswapd0 进程状态。若持续处于非睡眠状态，且运行时间较长并持续占用较高 CPU 资源。可将问题转向内存不足来排查。

 3. 输入` free`，`ps `等指令，查询系统内进程的内存占用情况，做进一步排查分析。

 4. 根据内存占用情况，考虑 重启系统 或 终止不需要且安全的进程 。
