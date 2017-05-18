## 1. What are the Agent installation directories?
A: Installation directories on Linux: /usr/local/qcloud/stargate and /usr/local/qcloud/monitor; installation directories on CoreOs: /var/lib/qcloud/stargate and /var/lib/qcloud/monitor, installation directories on Windows: C:\Program Files\QCloud\Stargate and C:\Program Files\QCloud\Monitor.

## 2. How to install Cloud Monitor Agent on Linux?

Install by executing the following commands:

```
1.  wget http://mirrors.tencentyun.com/install/monitor/linux_stargate_installer
2.  chmod +x linux_stargate_installer
3.  ./linux_stargate_installer
```

Once installed, you will see the following:

![img](https://mccdn.qcloud.com/img561f64c5d6e7a.png)

![img](https://mccdn.qcloud.com/img561f64d032ef0.png)

![img](https://mccdn.qcloud.com/img561f64d8a9064.png)

## 3. How to install Cloud Monitor Agent on Windows?

1) After logging in to the server, download `windows-stargate-installer.exe` from `http://mirrors.tencentyun.com/install/monitor/windows-stargate-installer.exe`.

2) Run` windows-stargate-installer.exe` to install it automatically.
Once installed, you will see the following results:

![img](https://mccdn.qcloud.com/img56259a45535ad.png)

![img](https://mccdn.qcloud.com/img561f650a18fb6.png)

## 4. Why is there no prompt after I double click the installer on Windows?

A: The installation on Windows is performed automatically, so the installer is automatically closed after installation. If you want to view the prompt during installation, you can run the installer in CMD command line.
## 5. Why can I see only "sgagent" after installation?
A: After installation, the process of "sgagent" will be started first, and then the "barad_agent". The interval between them is no more than 5 minutes. Before installation, please check whether the disk partition where the installation directory locates and the "inode"is full, whether the write permission is granted, and whether the network is running normally, etc.
## 6. How long does it take before users can view the monitoring data at frontend after installation?
A: If the network is running normally, users can view the monitoring data at frontend 5 minutes after barad_agent is started.
## 7. How to unmount Agent?
A: Execute the "uninstall" script of admin sub-directory under Agent installation directory to unmount Agent automatically.
## 8. Why is there no monitoring data after modifying the system time?
A: The collection and submission of monitoring data of Agent depends on the system time. Please make sure that the set time deviation from the actual time is less than 30 minutes and reboot Agent after setting the system time.
On Windows system:
On Server Manager -> Service List page, select QCloud BaradAgent Monitor to start and stop operations
On Linux system:
Directory of the script to be executed: /usr/local/qcloud/monitor/barad/admin; run trystart.sh to execute the script
