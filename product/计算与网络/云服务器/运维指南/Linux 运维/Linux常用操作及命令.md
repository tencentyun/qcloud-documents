## 1. 什么是 Linux 服务器 Load Average？

Load 是用来度量服务器工作量的大小，即计算机 CPU 任务执行队列的长度，值越大，表明包括正在运行和待运行的进程数越多。

## 2. 如何查看 Linux 服务器负载？

您可以通过执行 `w`，`top`，`uptime`，`procinfo` 命令，或者访问 `/proc/loadavg` 文件进行查看。
procinfo 工具安装请参考 Linux 环境下安装软件的相关文档。 

## 3. 服务器负载高怎么办？

服务器负载（Load/Load Average）是根据进程队列的长度来显示的。当服务器出现负载高的现象时（建议以15分钟平均值为参考），可能由于 CPU 资源不足，I/O 读写瓶颈，内存资源不足，CPU 正在进行密集型计算等原因造成。建议使用 `vmstat`，`iostat`，`top` 命令判断负载过高的原因，并找到具体占用大量资源的进程进行优化处理。 

## 4. 如何查看服务器内存使用率？

您可以通过执行 `free`，`top`（执行后可通过 `shift+m` 对内存排序），`vmstat`，`procinfo` 命令，或者访问 `/proc/meminfo` 文件进行查看。 

## 5. 如何查看单个进程占用的内存大小？

您可以通过执行 `top -p PID`，`pmap -x PID`，`ps aux|grep PID` 命令，或者访问 `/proc/$process_id（进程的 PID）/status` 文件进行查看，例如 /proc/7159/status 文件。 

## 6. 如何查看正在使用的服务和端口？

您可以通过执行 `netstat -tunlp`，`netstat -antup`，`lsof -i:PORT` 命令进行查看。 

## 7. 如何查看服务器进程信息？

您可以通过执行 `ps auxww|grep PID`，`ps -ef`，`lsof -p PID`，`top -p PID` 命令进行查看。 

## 8. 如何停止进程？

您可以通过执行 `kill -9 PID`（PID 表示进程号），`killall 程序名`（例如 killall cron）来停止进程。
如果需要停止僵尸进程，则需要杀掉进程的父进程，执行的命令为： `kill -9 ppid`（ppid 为父进程 ID 号，可以通过 `ps -o ppid PID` 命令进行查找，例如 ps -o ppid 32535）。 

## 9. 如何查找僵尸进程？

您可以通过执行 `top` 命令查看僵尸进程（zombie）的总数，通过执行 `ps -ef | grep defunct | grep -v grep` 查找具体僵尸进程的信息。 

## 10. 为什么启动不了服务器端口？

服务器端口的启动监听，需要从操作系统本身以及应用程序查看。
Linux 操作系统1024以下的端口只能由 root 用户启动，即需要先运行 `sudo su –` 获取 root 权限后再启用服务端口。
应用程序问题，建议通过应用程序启动日志来排查失败原因，例如端口冲突（腾讯服务器系统使用端口36000不能占用），配置问题等。 

## 11. 常用的 Linux 服务器性能查看命令有哪些？
<table class="t">
<tbody><tr>
<th width="100"><b>命令名称</b>
</th><th> <b>说明</b>
</th></tr>
<tr>
<td>top
</td><td>进程监控命令，用来监控系统的整体性能。<br>
<p>可以显示系统负载，进程，CPU，内存，分页等信息，常用 shift+m 和 shift+p 来按 memory 和 CPU 使用对进程进行排序。
</p>
</td></tr>
<tr>
<td>vmstat
</td><td>系统监控命令，重点侧重于虚拟内存，也可以监控 CPU，进程，内存分页以及 IO 的状态信息。<br>
<p>例如，vmstat 3 10，每隔3秒输出结果，执行10次。
</p>
</td></tr>
<tr>
<td>iostat
</td><td>用于输出 CPU 状态和 IO 状态的工具，可以详细展示系统的 IO 信息。<br>
<p>例如 iostat -dxmt 10，每10秒以 MB 的格式输出 IO 的详细信息。
</p>
</td></tr>
<tr>
<td>df
</td><td>用来检查系统的磁盘空间占用状况。<br>
<p>例如：df -m，以 MB 为单位展现磁盘使用状况。
</p>
</td></tr>
<tr>
<td>lsof
</td><td>列举系统中被打开的文件，由于 Linux 是以文件系统为基础，此命令在系统管理中很有帮助。<br>
<p>例如：<br>
lsof -i：36000，显示使用36000端口的进程
<br>
lsof -u root，显示以 root 运行的程序
<br>
lsof -c php-fpm，显示 php-fpm 进程打开的文件
<br>
lsof php.ini，显示打开 php.ini 的进程。
</p>
</td></tr>
<tr>
<td>ps
</td><td>进程查看命令，可以用来显示进程的详细信息。<br>
<p>常用命令参数组合为，ps -ef，ps aux，推荐使用 ps -A -o 来自定义输出字段。<br>
例如：<br>
ps -A -o pid,stat,uname,%cpu,%mem,rss,args,lstart,etime |sort -k6,6 -rn，按所列字段输出并以第六个字段进行排序
<br>
ps -A -o comm |sort -k1 |uniq -c|sort -k1 -rn|head，列出运行实例最多的进程。
</p>
</td></tr></tbody></table>

其他常用的命令和文件：`free -m`，`du`，`uptime`，`w`，`/proc/stat`，`/proc/cpuinfo`，`/proc/meminfo`。 

## 12. Cron 不生效怎么办？
排查步骤如下：
1. 确认 crontab 是否正常运行。
 1. 执行 `crontab -e` 命令，添加如下测试条目。
```
 \*/1 \* \* \* \* /bin/date >> /tmp/crontest 2>&1 &
```
 2. 观察 `/tmp/crontest` 文件。 
如果有问题，建议使用 `ps aux|grep cron` 查找 cron 的 pid，`kill -9 PID` 结束 cron 进程，并通过执行 `/etc/init.d/cron start` 命令重新启动 cron。 
2. 确认 cron 条目中的脚本路径为绝对路径。
3. 查看运行 cron 的用户帐号是否正确，同时查看 `/etc/cron.deny` 中是否包含此帐号。
4. 检查脚本的执行权限，脚本目录以及日志的文件权限。
5. 建议通过后台方式运行脚本，在脚本条目后添加 “&”。例如 `\*/1 \* \* \* \* /bin/date >> /tmp/crontest 2>&1 &` 。

## 13. 如何设置云服务器开机任务？

Linux 内核启动顺序为：
1. 启动 `/sbin/init` 进程。
2. 依次执行 init 初始脚本。
3. 运行级别脚本 `/etc/rc.d/rc\*.d`，\*号值等于运行模式。您可以在 `/etc/inittab` 中查看。
4. 执行 `/etc/rc.d/rc.local`。

>? 如果需要配置开机任务，您可以在 `/etc/rc.d/rc\*.d` 中的 `S\*\*rclocal` 文件配置，也可以在 `/etc/rc.d/rc.local` 中配置。 

## 14. 为什么服务器硬盘只读？

硬盘只读的常见原因如下：
- 磁盘空间满
可以通过 `df -m` 命令查看磁盘使用情况，然后删除多余的文件释放磁盘空间（非第三方文件不建议删除，如果需要请确认）。 
- 磁盘 inode 资源占用完。
您可以通过执行 `df -i` 命令进行查看和确认相关的进程。 
-  硬件故障。

如果 hosting 应用通过上述方式仍无法确认原因，请拨打咨询热线4009100100或通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213
) 协助定位。 

## 15. 如何查看 Linux 系统日志？

- 系统级别的日志文件存放路径为 `/var/log`。
- 常用的系统日志为 `/var/log/messages`。

## 16. 如何查找文件系统大文件？

您可以通过执行以下步骤进行查找：
1. 执行 `df` 命令，查看磁盘分区使用情况，例如 df -m。
2. 执行 `du` 命令，查看具体文件夹的大小。例如 du -sh ./\*，du -h --max-depth=1|head -10。
3. 执行 `ls` 命令，列出文件和文件大小，例如 ls -lSh。
您也可以通过 `find` 命令直接查看特定目录下的文件大小，例如 find / -type f -size +10M -exec ls -lrt {} \。

## 17. 如何查看服务器操作系统版本？

您可以通过执行以下命令查看系统版本：
- uname -a
- cat /proc/version
- cat /etc/issue 

## 18. 为什么 Linux 终端显示中文会出现乱码？

服务器本身不对显示语言进行限制，如果终端软件影响中文的显示，您可以尝试调整【选项】>【会话选项】>【外观】（secureCRT 设置，其他版本软件请查找相关设置）。
如果是纯 Linux shell 出现乱码，请使用 export 命令查看用户环境变量，LANG，LC_CTYPE 等环境变量设置。

## 19. 如何设置通过 SecureCRT 连接云服务器的超时时间？

当 SecureCRT 连接云服务器时，您可以通过以下设置不断开连接：
1. 打开【SecureCRT 选项（Options）】。
2. 选择【会话选项（Session Opetions）】，单击【终端（Terminal）】。
3. 在右侧反空闲（Anti-idle）的框中，勾选【发送协议 NO-OP（Send protocol NO-OP）】，并将时间设置为每120秒(every 120 seconds)。 

## 20. 为什么删除 Linux 服务器上的文件，硬盘空间不释放？

**原因：**

登录 Linux 服务器并执行 `rm` 命令删除文件后，执行 `df` 命令查看硬盘空间，可能会发现删除文件后可用的硬盘空间没有增加。其原因为，当通过 `rm` 命令删除文件时，有其它进程正在访问该文件，若通过执行 `df` 命令进行查看，删除的文件占用的空间将为没有立即释放的状态。

**解决方法：**

1. 使用 root 权限执行 `lsof |grep deleted` 命令，查看正在使用被删除文件的进程的 PID。
2. 通过命令 `kill -9 PID` 杀掉对应的进程即可。 


## 21. 如何删除 Linux 服务器上的文件？
您可通过 `rm` 命令进行文件删除，但通过此命令删除的文件无法恢复，请谨慎使用。
`rm` 命令格式为 `rm （选项）（参数）`。
- 选项：
**-d**：直接将需删除的目录的硬连接数据删除为0，再删除该目录。
**-f**：强制删除文件或目录。
**-i**：删除已有文件或目录之前先询问用户。
**-r** 或 **-R**：递归处理，将指定目录下的所有文件与子目录一并处理。
**--preserve-root**：不对根目录进行递归操作。
**-v**：显示指令的详细执行过程。
- 参数：文件，指定被删除的文件列表，如果参数中含有目录，则需加上 -r 或者 -R 选项。
- 示例：
	- 删除文件 `test.txt`，请执行 `rm test.txt`。
	- 删除目录 `test`，请执行 `rm -r test`。
	- 删除当前目录下的所有文件及子目录，请执行 `rm -r *`。
