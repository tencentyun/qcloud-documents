本文档以 CentOS 7.5 操作系统的云服务器为例，介绍无法通过 SSH 登录 Linux 实例的问题排查和解决方案。

## 故障现象

[使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700) 时，提示无法连接或者连接失败。

## 故障定位及处理

1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 在操作系统界面，执行以下命令，查看是否含有 sshd 服务监听的端口。
```
netstat -tnlp | grep sshd
```
 - 若返回如下结果，即表示 sshd 进程已监听22端口，请执行 [步骤4](#step04)。
```
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1015/sshd  
```
 - 若无输出，则可能是 sshd 服务未启动，请执行 [步骤3](#step03)。
3. <span id="step03">执行以下命令，查看 sshd 服务是否启动。</span>
```
systemctl status sshd.service
```
 - 如果已启动，请执行  [步骤4](#step04)。
 - 如果未启动，请执行以下命令，启动 sshd 服务，再重新使用 SSH 登录 Linux 实例。
```
systemctl start sshd
```
4. <span id="step04">登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)。</span>
5. 在实例的管理页面，选择需要排查故障的实例，单击【更多】>【安全组】>【配置安全组】。如下图所示：
![](https://main.qcloudimg.com/raw/deff7af1803cc95cfd45036b850a9cb6.png)
6. 在弹出的 “配置安全组” 窗口中，单击已配置（已勾选）的安全组 ID。如下图所示：
进入该实例绑定的安全组页面。
![](https://main.qcloudimg.com/raw/8beddaae54897226d160c7d54c488990.png)
7. 在安全组规则的入站规则页面，单击【一键放通】。
8. 在弹出的提示框中，单击【确定】。
完成放通后，请重新使用 SSH 登录 Linux 实例。

如果进行以上操作后，您的实例仍无法连接，建议您 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行反馈。





