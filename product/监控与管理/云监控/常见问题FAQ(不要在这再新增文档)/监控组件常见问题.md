## 1. Agent 的安装目录是什么？
答：
- Linux 安装目录是`/usr/local/qcloud/stargate`和`/usr/local/qcloud/monitor`
- CoreOs 安装目录是`/var/lib/qcloud/stargate`和`/var/lib/qcloud/monitor`
- Windows 安装目录是`C:\Program Files\QCloud\Stargate`和`C:\Program Files\QCloud\Monitor`

## 2. Linux 下如何安装云监控 Agent？

[登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436) 后，执行命令进行安装，操作如下：

```
1.  wget http://update2.agent.tencentyun.com/update/linux_stargate_installer
2.  chmod +x linux_stargate_installer
3.  ./linux_stargate_installer
```

安装成功如下图所示：

![img](https://mccdn.qcloud.com/img561f64c5d6e7a.png)

![img](https://mccdn.qcloud.com/img561f64d032ef0.png)

![img](https://mccdn.qcloud.com/img561f64d8a9064.png)

## 3. Windows 下如何安装云监控 Agent？

1. [登录到Windows 实例](https://cloud.tencent.com/document/product/213/5435) 后，从`http://update2.agent.tencentyun.com/update/windows-stargate-installer.exe` ， 下载安装包 `windows-stargate-installer.exe`。请注意：  
   内网，可直接下载使用；  
   外网，进入虚拟机后才能使用。  

2. 运行 `windows-stargate-installer.exe` 进行自动化安装。
   安装成功如下图所示：
   ![img](https://mccdn.qcloud.com/img56259a45535ad.png)
   ![img](https://mccdn.qcloud.com/img561f650a18fb6.png)

## 4. Windows 双击安装包后，为何没有任何提示？

答：Windows 采用全自动化的安装，安装完成后自动退出安装包，如果想查看安装过程的提示，可以在 CMD 命令行环境下执行安装包。

## 5. 安装完成后，为何只有 sgagent 进程？
答：安装完成后会先启动 sgagent 进程，然后再启动 barad_agent 进程，中间相隔不会超过5分钟。安装之前，请先确认安装目录所在的磁盘分区是否已满、inode 是否已满、是否具有可写权限、网络是否正常等。

## 6. 安装完成后，多久可以在前台看到监控数据？
答：barad_agent 进程起来以后，如果网络没有问题，5分钟后前台可以看到监控数据。

## 7. 如何卸载 Agent？
答：执行 Agent 安装目录下 admin 子目录的 uninstall 脚本可以自动卸载 Agent。

## 8. 修改系统时间后，为何没有监控数据？
答：Agent 的监控数据采集上报依赖于系统时间，系统时间设置若偏离实际时间超过 30 分钟，则不会有监控数据。所以系统时间设置偏离实际时间须控制在 `30分钟`以内，且回退设置系统时间时请重启 Agent。
- **Windows系统**
  服务器管理器 → 服务列表页，选择`QCloud BaradAgent Monitor`进行启停操作；
- **Linux系统**
  执行脚本位置：`/usr/local/qcloud/monitor/barad/admin`，执行` trystart.sh `进行启动。

## 9. 如何重启监控agent 

1. Windows系统

   服务器管理器 → 服务列表页，选择QCloud BaradAgent Monitor进行启停操作；

2. Linux系统

   执行脚本位置：/usr/local/qcloud/monitor/barad/admin，执行stop.sh停止 ，然后执行 trystart.sh 进行启动。 


## 10.哪些情况下导致安装监控组件失败

   1.  DNS配置被修改，无法连接到后端服务

   2.  机器被入侵，`ps`被篡改，无法输出正常信息


   ​

