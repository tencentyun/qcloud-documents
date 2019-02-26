若您需要使用腾讯云监控查看 **云服务器** 指标数据并且产生告警，您需在腾讯云服务器上正确安装监控组件，云服务器指标数据采集依赖于监控组件。

注：为保证监控数据正常上报，您的CVM需放通tcp dport 80端口。

## Linux安装指引
用户[登录 Linux 实例](/doc/product/213/5436)后，可执行以下命令进行安装，操作如下：
```
wget http://update2.agent.tencentyun.com/update/linux_stargate_installer
chmod +x linux_stargate_installer
./linux_stargate_installer
```

安装成功时如下图所示：
![](//mccdn.qcloud.com/img568a75015695c.png)
![](//mccdn.qcloud.com/img568a750882880.png)
![](//mccdn.qcloud.com/img568a751592aea.png)

## Windows 安装指引
1) 用户 [登录 Windows 实例](/doc/product/213/5435)后，内网访问 `http://update2.agent.tencentyun.com/update/windows-stargate-installer.exe` 下载安装包 `windows-stargate-installer.exe`。

2) 运行该程序进行自动化安装。

安装成功时如下图所示：
![](//mccdn.qcloud.com/img568a758c4c308.png)
![](//mccdn.qcloud.com/img568a75948c917.png)