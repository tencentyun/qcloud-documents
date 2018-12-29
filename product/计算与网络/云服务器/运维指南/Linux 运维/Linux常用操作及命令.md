## 1. 什么是 Linux 服务器 Load Average？
Load 是用来度量服务器工作量的大小，即计算机 CPU 任务执行队列的长度，值越大，表明包括正在运行和待运行的进程数越多。
参考文档：[点此获取](http://en.wikipedia.org/wiki/Load_average)。

## 2. 如何查看 Linux 服务器负载？
您可以通过执行 w，top，uptime，procinfo 命令，或者访问 /proc/loadavg 文件进行查看。
procinfo 工具安装请参考 Linux 环境下安装软件。 

## 3. 服务器负载高怎么办？
服务器负载（load/load average）是根据进程队列的长度来显示的。
当服务器出现负载高的现象时（建议以15分钟平均值为参考），可能是由于 CPU 资源不足，I/O 读写瓶颈，内存资源不足等原因造成，也可能是由于 CPU 正在进行密集型计算。
建议使用 vmstat -x，iostat，top 命令判断负载过高的原因，并找到具体占用大量资源的进程进行优化处理。 

## 4. 如何查看服务器内存使用率？
可以通过 free，top（执行后可通过shitf+m对内存排序），vmstat，procinfo 命令，也可以通过 /proc/meminfo 文件查看。 

## 5. 如何查看单个进程占用的内存大小？
可以使用 top -p PID，pmap -x PID，ps aux|grep PID 命令，也可以通过 /proc/$process_id（进程的PID）/status 文件查看，例如 /proc/7159/status 文件。 

## 6. 如何查看正在使用的服务和端口？
可以使用 netstat -tunlp，netstat -antup，lsof -i:PORT 命令查看。 

## 7. 如何查看服务器进程信息？
可以使用 ps auxww|grep PID，ps -ef，lsof -p PID，top -p PID 命令查看。 

## 8. 如何停止进程？
可以使用 `kill -9 PID`（进程号），killall 程序名（比如killall cron）来停止进程。
如果要停止的是僵尸进程，则需要杀掉进程的父进程才有效果，命令为： kill -9 ppid（ppid 为父进程 ID 号，可以通过 ps -o ppid PID 查找，例如 ps -o ppid 32535）。 

## 9. 如何查找僵尸进程？
可以使用 top 命令查看僵尸进程（zombie）的总数，使用 `ps -ef | grep defunct | grep -v grep` 查找具体僵尸进程的信息。 

## 10. 为什么启动不了服务器端口？
服务器端口的启动监听，需要从操作系统本身以及应用程序查看。
Linux 操作系统1024以下的端口只能由 root 用户启动，即需要先运行 `sudo su –` 获取 root 权限后再启用服务端口。
应用程序问题，建议通过应用程序启动日志来排查失败原因，例如端口冲突（腾讯服务器系统使用端口不能占用，比如36000），配置问题等。 

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

其他常用的命令和文件，free -m，du，uptime，w，/proc/stat，/proc/cpuinfo，/proc/meminfo。 
参考文档：[点此获取](http://en.wikipedia.org/wiki/Template:Unix_commands)。

## 12. Cron不生效怎么办？
排查步骤如下：
1) 确认 crontab 是否正常运行。
可以运行命令 crontab -e 添加如下测试条目 \*/1 \* \* \* \* /bin/date >> /tmp/crontest 2>&1 &，然后观察 /tmp/crontest文件。 
如果有问题，建议使用 ps aux|grep cron 查找 cron 的 pid，kill -9 PID 结束 cron 进程，然后通过 /etc/init.d/cron start 重新启动 cron。 

2) 确认 cron 条目中的脚本路径为绝对路径。

3) 查看运行 cron 的用户帐号是否正确，同时查看 /etc/cron.deny 中是否包含此账户。

4) 检查脚本的执行权限，脚本目录以及日志的文件权限。

5) 建议通过后台方式运行脚本，在脚本条目后添加“&”，例如，\*/1 \* \* \* \* /bin/date >> /tmp/crontest 2>&1 & 

## 13. 如何设置云服务器开机任务？
Linux 内核启动顺序为：
/sbin/init 进程启动，
然后依次执行 init 初始脚本，
运行级别脚本/etc/rc.d/rc\*.d，\*号值等于运行模式，可以在 /etc/inittab 中查看，最后执行 /etc/rc.d/rc.local。

如果需要配置开机任务，可以在 /etc/rc.d/rc\*.d 中的 S\*\*rclocal 文件配置，也可以在 /etc/rc.d/rc.local 中配置。 

## 14. 为什么服务器硬盘只读？
硬盘只读的常见原因如下：
1) 磁盘空间满
可以通过df -m命令查看磁盘使用情况，然后删除多余的文件释放磁盘空间（非第三方文件不建议删除，如果需要请确认）； 
2) 磁盘inode资源占用完
可以通过df -i命令查看，确认相关的进程； 
3) 硬件故障

如果 hosting 应用通过上述方式仍无法确认原因，请拨打咨询热线4009-100-100或提交工单协助定位。 

## 15. 如何查看linux系统日志？
系统级别的日志文件存放路径为 /var/log。
常用的系统日志为 /var/log/messages 。

## 16. 如何查找文件系统大文件？
可以首先通过 df 命令查看磁盘分区使用情况，比如 df -m；
然后通过 du 命令查看具体文件夹的大小，比如 du -sh ./\*，du -h --max-depth=1|head -10；
使用 ls 命令列出文件以及大小，比如 ls -lSh；
另外，也可以通过find命令直接查看特定目录下的文件大小，比如find / -type f -size +10M -exec ls -lrt {} \; 

## 17. 如何查看服务器操作系统版本？
可以通过下列命令查看系统版本：
uname -a，cat /proc/version，cat /etc/issue 

## 18. 为什么linux终端显示中文会出现乱码？
服务器本身没有对显示语言有限制，如果是终端软件的影响中文的显示，可以尝试调整【选项】-【会话选项】-【外观】（secureCRT设置，其他版本软件请查找相关设置）；
如果是纯Linux shell出现乱码，请使用export命令查看用户环境变量，查看LANG，LC_CTYPE等环境变量设置。

## 19. 如何设置通过SecureCRT连接云服务器的超时时间？
可以通过如下设置，使SecureCRT连接云服务器时，不断开连接：
打开secureCRT选项(Options)，选择会话选项（Session Opetions），单击终端（Terminal），在右侧反空闲（Anti-idle）的框中勾选发送协议NO-OP（Send protocol NO-OP），时间设置为每120秒(every 120 seconds)。 

## 20. 为什么删除linux服务器上的文件，硬盘空间不释放？
有时，登录linux服务器执行 rm 命令删除文件后，用 df 命令查看硬盘空间，发现删除文件后可用的硬盘空间没有增加。原因是通过 rm 命令删除文件的时候，如果正好有其它进程在访问该文件，通过 df 命令查看，删除的文件占用的空间是没有立即释放的。

解决方法：
使用 root 权限执行 `lsof |grep deleted` ，查看正在使用被删除文件的进程的 PID，通过命令 `kill -9 PID` 杀掉对应的进程即可。 
