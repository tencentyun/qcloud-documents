When users find that their instance bandwidth is used too much, they often want to locate the process that occupies the most bandwidth, and then analyze and troubleshoot it. This document describes how to use the appropriate tools to locate processes with high bandwidth usage in Linux and Windows.

## Viewing Bandwidth Usage per Progress in Linux
### NetHogs overview
NetHogs is an open source command line tool that collects bandwidth usage per process in real time in Linux. You can install NetHogs in CentOS by executing the following command:
```
yum install nethogs
```

### How to use NetHogs
Enter the following command in the terminal, and then you can see the available parameters of NetHogs and how to use it.
```
nethogs -h
```
![](https://mc.qcloudimg.com/static/img/1a5bda1babaa86e7200f7a055023c46c/image.png)
The available parameters are as follows:
- **-d**: Sets refresh interval. Default is 1 second.
- **-t**: Tracking mode.
- **-c**: Number of updates.
- **device**: Sets the ENI to monitor. Default is eth0.

When NetHogs is running, enter the following parameters to perform corresponding operations:
- **q**: Quits.
- **s**: Sorts by sent traffic.
- **r**: Sorts by received traffic.
- **m**: Switches between total (KB, B, MB) and KB/s mode. Switching sequence: KB/s > KB > B > MB.

The following figure lists the processes by sent traffic after **nethogs -d 10** runs in Linux, which provides an example for the output of NetHogs. The list of processes can be displayed either by sent traffic or by received traffic, making it easy for you to get the process that sends/receives the most traffic.
![](https://mc.qcloudimg.com/static/img/9a863640f0860a939b0a5c159522d01c/image.png)
PID: Process ID.
USER: The user who runs the process.
PROGRAM: Program name or IP port number.
DEV: Network interface to which traffic goes.
SENT: Traffic sent by a process per second.
RECEIVED: Traffic received by a process per second.

## Viewing Bandwidth Usage per Progress in Windows
### Windows Resource Monitor
Resource Monitor is a Windows utility that displays the information about the use of CPU, memory, disk, network and other resources per process.
You can launch Resource Monitor via **Task Manager** -> **Performance**.
![](https://mc.qcloudimg.com/static/img/0a70336ea3803db7edd4832ba4a1b6aa/image.png)
You can also launch Resource Monitor by executing **resmon.exe**.
![](https://mc.qcloudimg.com/static/img/05a6b6d8373f64c6dddf090ae1a7f767/image.png)
By clicking the **Network** tab in Resource Monitor, you can see the bandwidth usage of every process. By clicking **SENT** or **RECEIVED**, you can see the processes displayed by sent or received traffic respectively and locate the process that takes up the most network resources.
![](https://mc.qcloudimg.com/static/img/3a73f5d36165ad82dbacdacc449aa93a/image.png)

## Analyzing and Troubleshooting the Process
After locating the process with high CPU utilization, you need to analyze the type of the progress:
1. Analyze whether it is a normal process (system/business/Tencent Cloud process). You can search by the process name to confirm whether it is a normal one.

2. If it is an exceptional process, the instance may be poisoned. You can terminate the process, use your security software to check and kill it, or reinstall the system after data backup.

3. If it is a Tencent Cloud component process, contact us by [submitting a ticket](https://console.cloud.tencent.com/workorder/category), and we will help you locate and troubleshoot the problem.
Common Tencent Cloud components include:
 - sap00x: Security component process
 - Barad_agent: Monitoring component process
 - secu-tcs-agent: Security component process

4. If it is a normal business progress, analyze whether there is a large number of network visits, and whether you can break the resource bottleneck of network bandwidth by compressing files. Otherwise, you are advised to upgrade the instance. For how to upgrade bandwidth configurations, please see [Changing Configurations](https://cloud.tencent.com/document/product/644/12629).

