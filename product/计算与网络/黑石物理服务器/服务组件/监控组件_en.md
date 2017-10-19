## Purpose of Monitoring Component
The monitoring component should be installed in the CPM in advance in order to provide __performance monitoring, hardware failure monitoring, exception monitoring__.
## Configuration of Monitoring Information
You can customize the alarm policy for CPM monitoring metrics in [Cloud Monitor Console](https://console.cloud.tencent.com/monitor/policylist), to associate with (apply to) alarm object (CPM) and manage alarm receiver group.
<br  />
Metrics that support custom alarm threshold include (__performance monitoring__): _CPU utilization, CPU average load, MEM memory usage, application memory usage, virtual memory usage, memory utilization, disk IO read traffic, disk IO write traffic, disk IO waiting time, disk IO CPU utilization, disk IO service time, disk space utilization, ENI outbound bandwidth, ENI inbound bandwidth, ENI outbound packets, ENI inbound packets, public network outbound bandwidth, public network inbound bandwidth, public network outbound packets, public network inbound packets, public network outbound traffic_ .
<br  />
The alarm that is triggered when an exception occurs include (__exception monitoring__): _Disk read-only alarm (data cannot be written into a certain logic disk probably because the disk is full or file system failed)_ .
<br  />
Alarms on hardware failure with clear reasons include (__hardware failure monitoring__): _Disk failure (with redundancy), RAID card battery failure, RAID card cache failure, disk failure (without redundancy), impending failure of disk (with redundancy), disk failure (with redundancy, slot unknown), power failure (with redundancy), fan failure, disk failure (without redundancy, online replacement of disk), SSD disk failure (without redundancy), ENI failure, memory failure, SSD disk is running out of service life (shut down and replace disk) [it means you need to shut the CPM down and replace the disk, otherwise the CPM may suffer great risks], higher SSD disk bad block rate (shut down and replace disk), HBA card failure, operating system disk failure (without redundancy), motherboard failure, CPU failure, power failure (without redundancy), impending failure of disk (without redundancy)_ .
<br  />
Note: For hardware failure alarms, even though users have not configured alarms in cloud console, when Tencent Cloud BM platform identifies any failure, users are notified of such failure through after-sales services (generally the after-sales group), which makes sure that the hardware failure is followed-up and solved in time. The other two types of alarms should be configured by users in cloud monitor console.

## Guide on Installation (Repair) of Monitoring Component

### Linux Operating System
- Download:
wget http://mirrors.tencentyun.com/install/monitor_bm/AgentInstall.tgz
- Decompress:
tar zxvf AgentInstall.tgz
- Install:
cd AgentInstall;./setupagent.sh
- Verify:
Execute ps -ef |grep agenttools, and 5 related processes are shown.
```
[root@centos ~]# ps -ef |grep agenttools
root      3900     1  0 Jul10 ?        00:00:03 /usr/local/agenttools/agent/agent -c /usr/local/agenttools/agent/client.conf
root      3907     1  0 Jul10 ?        00:00:00 /usr/local/agenttools/agent/agentPlugInD
root      3915     1  0 Jul10 ?        00:01:05 /usr/local/agenttools/agent/base -d5 -c1 -m4 -s /usr/local/agenttools/agent/base.conf
root      3921     1  0 Jul10 ?        00:00:00 /usr/local/agenttools/agent/tcvmstat
root      3935     1  0 Jul10 ?        00:00:06 /usr/local/agenttools/agent/sysddd
root     41565 41419  0 15:50 pts/0    00:00:00 grep agenttools
```

### Windows Operating System
- Download:
In the operating system of CPM, download the component via browser:
http://mirrors.tencentyun.com/install/monitor_bm/AgentInstall_win64.zip
- Decompress:
Decompress the installation package into the folder win-agent under the root directory of C drive. The directory structure is:
``` 
c:\win-agent\
    |--adssensor.dll
    |--agentplugin.dll
    |--agentRepNum.exe
    |--agentRepStr.exe
    ......
``` 

- Install
Execute c:\win-agent\uninstall.bat and c:\win-agent\setup.bat.
 
- Verify:
Open "My Computer", enter "cmd" in address bar and press Enter.
![](https://mc.qcloudimg.com/static/img/a04a39f2b78d0d98e3df65c073e2ddf4/001.png)
Enter command netstat -ano, press Enter, and the remote connection port 9922 is shown.
![](https://mc.qcloudimg.com/static/img/5aa69ae7ffcea1a3b6775fec1fde3576/002.png)

