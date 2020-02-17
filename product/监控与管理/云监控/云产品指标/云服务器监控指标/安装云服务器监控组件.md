若用户需要使用腾讯云监控查看云服务器指标数据并且产生告警，需在腾讯云服务器上正确安装监控组件，云服务器指标数据采集依赖于监控组件。

>!
>- 为保证监控数据正常上报，用户的 CVM 操作系统内部需放通 TCP dport 80端口（由于云监控组件上报数据不依赖安全组和网络 ACL，所以无需放通安全组和网络 ACL 的 TCP dport 80端口）。
>- 下述步骤中获取 agent 安装包的命令，必须**登录到云服务器**，才可正常执行。

## Linux 安装指引
1. 用户 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436) 后，执行以下命令进行安装，操作如下：
```bash
wget http://update2.agent.tencentyun.com/update/linux_stargate_installer   //下载 agent
chmod +x linux_stargate_installer   //赋予 anent 安装脚本执行权限
./linux_stargate_installer   //安装 agent
```
2. 用户可执行以下命令查看是否安装成功。
 1. 查看 Agent 是否已添加到计划任务，执行命令如下。
```bash
crontab -l |grep stargate
```
若执行结果如下图所示，说明 Agent 已添加到计划任务。
![](https://main.qcloudimg.com/raw/dc37b46f45bdde2afd7956497ddca3bc.png)
 2. 查看 Agent 相关进程是否启动，执行命令如下。
```bash
ps ax |grep sgagent
ps ax |grep barad_agent
```
若执行结果如下图所示，说明 Agent 相关进程已正常启动，则已经成功安装 Agent。
![](https://main.qcloudimg.com/raw/78427ff35cdd80ceaeca555f1fbe7f40.png)
![](https://main.qcloudimg.com/raw/2ea6857b89a12898d26cbd0580eba213.png)

## Windows 安装指引
1. 用户 [登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435) 后，复制下载地址`http://update2.agent.tencentyun.com/update/windows-stargate-installer.exe`，并前往浏览器打开，即可下载 Agent 组件 `windows-stargate-installer.exe`。
2. 运行该程序进行自动化安装。
安装成功时如下图所示：
![](https://main.qcloudimg.com/raw/b86b053af5de987bdbf31b93715fa4ea.png)
![](https://main.qcloudimg.com/raw/c7679e1161a0891b6e65b2ba45f9106f.png)

## 常见问题
- 在用户遇到无法下载 Agent 或其它使用方面问题，可参考 [云服务器监控组件相关](https://cloud.tencent.com/document/product/248/2259) 常见问题文档进行相应的处理。
- 您也可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们寻求解决措施。
