## 1. What is Linux server load average?
Load is used for measuring the workload of server, i.e. the length of the queue of tasks to be executed by CPU of the computer. The greater the value, the more processes that are currently running or waiting to be executed.
Reference: http://en.wikipedia.org/wiki/Load_average 

## 2. How to check Linux server load?
You can check it using w, top, uptime or procinfo commands, or from /proc/loadavg file.
Please refer to "Installing Software in Linux Environment" for the instructions on how to install procinfo tool. 

## 3. What to do when the server load is too high?
Server load/load average is displayed based on the length of process queue.
The high load of server (based on the average value over 15 minutes) may be caused by such reasons as insufficient CPU resources, I/O read/write bottleneck, insufficient memory resources, or the intensive computing that is being performed by CPU.
It is recommended to use vmstat -x, iostat and top commands to determine the reasons for the overload, and then find the processes that are taking up much of the resources for optimization. 

## 4. How to check server memory usage?
You can check this using free, top (press shift+m to sort by memory usage after the execution), vmstat, or procinfo commands, or from /proc/meminfo file. 

## 5. How to check the memory occupied by a single process?
You can check it using top -p PID, pmap -x PID, or ps aux|grep PID commands, or from /proc/$process_id (process' PID) /status file, e.g. /proc/7159/status file. 

## 6. How to check services and ports that are in use?
You can check this using netstat -tunlp, netstat -antup, or lsof -i:PORT commands. 

## 7. How to check server process information?
You can check this using ps auxww|grep PID, ps -ef, lsof v-p PID, or top -p PID commands. 

## 8. How to kill a process?
You can use kill -9 PID (process ID) and killall program name (e.g. killall cron) to kill a process.
If the process to be killed is a zombie process, then its parent process must be killed before it can be effectively killed. The command is:  kill -9 ppid (ppid is parent process ID, which can be found with ps -o ppid PID, e.g. ps -o ppid 32535). 

## 9. How to find a zombie process?
You can use top command to check the total number of zombie processes, and use ps -ef | grep defunct | grep -v grep to search for the information on specific zombie processes. 

## 10. Why can't server port be enabled?
Enabling and listen-in of server port need to be checked from operating system itself and the application. 
Port below 1024 can only be enabled by root users on the Linux operating system. This means that you need to run sudo su first to obtain root permission before enabling the server port.
For any problem with application, it is recommended to use application startup log to identify reasons for failure, for example, port conflict (port used by Tencent server system cannot be occupied, such as 36000), configuration problem, etc. 

## 11. What are the commands commonly used for checking performance of Linux server?
<table class="t">
<tbody><tr>
<th width="100"><b>Command Name </b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td>top
</td><td> Process monitoring command for monitoring the overall performance of system. <br>
<p>This command can be used to display information about system load, process, CPU, memory and paging. Shift+m and Shift+p are often used to sort processes by memory usage and CPU usage.
</p>
</td></tr>
<tr>
<td>vmstat
</td><td>System monitoring command which focuses on virtual memory but can also be used for monitoring the status information about CPU, process, memory paging and IO. <br>
<p>For example, vmstat 3 10 outputs results every 3 seconds and is executed 10 times.  
</p>
</td></tr>
<tr>
<td>iostat
</td><td>A tool used for outputting CPU and IO statuses and can display detailed IO information of system. <br>
<p>For example, iostat -dxmt 10 outputs detailed information about IO in MB every 10 seconds.
</p>
</td></tr>
<tr>
<td>df
</td><td>Used to check the disk space usage of system. <br>
<p>For example, df -m displays disk usage in MB.
</p>
</td></tr>
<tr>
<td>lsof
</td><td>List the files opened in the system. Since Linxu is based on file system, this command is very useful in system management. <br>
<p>For example: <br>
lsof -i: 36000 displays the processes using Port 36000 
<br>
lsof -u root displays the programs run by root
<br>
lsof -c php-fpm displays the files opened by php-fpm process
<br>
lsof php.ini displays the processes for which php.ini is opened.
</p>
</td></tr>
<tr>
<td>ps
</td><td>A command for viewing process. It can be used to display details of the process. <br>
<p>Commonly used command parameter combinations are ps -ef and ps aux. Ps -A -o is recommended to be used for customization of output fields. <br>
For example: <br>
ps -A -o pid,stat,uname,%cpu,%mem,rss,args,lstart,etime |sort -k6,6 -rn outputs results according to the listed fields and sorts by the 6th field
<br>
ps -A -o comm |sort -k1 |uniq -c|sort -k1 -rn|head lists the process with the largest number of running instances.
</p>
</td></tr></tbody></table>

Other often-used commands and files include free -m, du, uptime, w, /proc/stat, /proc/cpuinfo and /proc/meminfo. 
Reference: http://en.wikipedia.org/wiki/Template:Unix_commands, http://www.linuxmanpages.com/ 

## 12. What to do when Cron does not work?
The trouble-shooting procedures are as follows:

1) Verify whether crontab is running normally.
You can run crontab -e command and add the following test entry \*/1 \* \* \* \* /bin/date >> /tmp/crontest 2>&1 &, and then observe /tmp/crontest file. 
In case of any problem, it is recommended to use ps aux|grep cron to look for pid of cron and use kill -9 PID to terminate cron process, and then restart cron with /etc/init.d/cron start. 

2) Verify whether the script path in the cron entry is an absolute path.

3) Check whether the user account for cron execution is correct, and check whether the account is included in /etc/cron.deny.

4) Check the execution permission of the script, script directory and log file permission.

5) It is recommended to run the script in background. Append a "&" to the script entry, for example, \*/1 \* \* \* \* /bin/date >> /tmp/crontest 2>&1 & 

## 13. How to set startup task for CVM?
Linux kernel startup procedure is as follows:

Start /sbin/init process,
then execute init initial script,
run level script/etc/rc.d/rc\*.d, where value of \* means running mode which can be viewed in /etc/inittab, and finally execute /etc/rc.d/rc.local.

The configuration of startup task can be made in S\*\*rclocal file under /etc/rc.d/rc\*.d, or in /etc/rc.d/rc.local. 

## 14. Why is server hard drive read-only?
Common reasons for read-only hard disk are as follows:
1) Disk space is full
You can use df-m command to check the disk usage, and then delete unnecessary files to free disk space (Deletion of non-third party files is not recommended. Please verify it if required); 
2) Disk inode resources are all occupied
You can use df-i command to check and verify related processes; 
3) Hard disk failure 

If hosting application is still unable to identify the reason using the above methods, please call the hot-line 4009100100 or submit ticket for assistance in locating. 

## 15. How to view Linux system logs?
The storage path for system-level log files is /var/log.
The commonly used system log is /var/log/messages.

## 16. How to find large files in file system?
First, check disk partition usage with df commands, for example, df-m;
Then check the size of specific folder with du commands, for example, du -sh ./\*, du -h --max-depth=1|head -10;
List files and their sizes using ls commands, for example, ls -lSh;
In addition, you can also directly check the size of files under specific directory by using find commands, for example, find / -type f -size +10M -exec ls -lrt {} \; 

## 17. How to check the version of server's operating system?
You can use the following command to check system version:
uname -a, cat /proc/version, cat /etc/issue 

## 18. Why are there unreadable codes in the Chinese displayed by Linux terminal?
The server itself does not impose restrictions on the display language. If the display of Chinese is affected by the terminal software, you can try to adjust "Options" - "Session Options" - "Appearance" (secureCRT settings; please search for relevant settings for software of other versions.)
If the unreadable codes appear in pure Linux shell, please use export command to check settings for user environment variables and such environment variables as LANG and LC_CTYPE.

## 19. How to set up time-out for connection to CVM through SecureCRT?
It can be set as follows so that the connection is not broken when connecting to CVM through SecureCRT:
Open secureCRT Options, choose "Session Options", click "Terminal", then check "Send protocol NO-OP" in the Anti-idle box on the right, and set the time to "every 120 seconds". 

## 20. Why isn't disk space freed after a file on Linux server is deleted?
Sometimes, after logging in to Linux server and executing rm command to delete a file on it, you may find that available disk space does not increase when you execute df command to check disk space. This is because when the file is deleted with rm command, if another process happens to be assessing the file, the space occupied by the deleted file will not be immediately freed at the time you check the disk space using df command.

Solution:
Use root permission to execute lsof |grep deleted, view the PID of the process which is using the deleted file, and then kill the process with kill -9 PID command. 