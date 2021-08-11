本文介绍您的 Mac 通过 Microsoft Remote Desktop 远程连接登录 Windows 时遇到的常见故障现象以及解决方法。
## 故障现象

- Mac 通过 Microsoft Remote Desktop 远程连接登录 Windows 时，提示 “The certificate couldn't be verified back to a root certificate.”。
<img src="https://main.qcloudimg.com/raw/070b9c862d6928988768b266461bc816.png" data-nonescope="true">
- Mac 远程桌面连接（Remote Desktop Connection）时，提示 “远程桌面连接无法验证您希望连接的计算机的身份”。
<img src="https://main.qcloudimg.com/raw/32f0444a47b2e4c90f6657ec9686afcb.png" data-nonescope="true">

## 故障处理
>? 以下操作以 Windows Server 2016 为例。
>

### 通过 VNC 方式登录云服务器

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，找到目标云服务器实例，单击【登录】。如下图所示：
![登录](https://main.qcloudimg.com/raw/038fce530c6c6827796e51d896306a93.png)
3. 在弹出的 “登录Windows实例” 窗口中，选择【其它方式（VNC）】，单击【立即登录】，登录云服务器。
4. 在弹出的登录窗口中，选择左上角的 “发送远程命令”，单击 **Ctrl-Alt-Delete** 进入系统登录界面。如下图所示：
![](https://main.qcloudimg.com/raw/2dec43fa6ddb5e442da59c75f7a34b0f.png)

### 修改实例本地组策略

1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/330624bafb194914948c8ebd9e47334d.png" style="margin: 0;">，输入 **gpedit.msc**，按 **Enter**，打开 “本地组策略编辑器”。
>? 也可使用 “Win+R” 快捷键打开运行界面。
>
2. 在左侧导航树中，选择【计算机配置】>【管理模板】>【Windows组件】>【远程桌面服务】>【远程桌面会话主机】>【安全】，双击【远程（RDP）连接要求使用指定的安全层】。如下图所示：
![](https://main.qcloudimg.com/raw/cfcb737815f047d5542ced1658eb354f.png)
3. 在打开的 “远程（RDP）连接要求使用指定的安全层” 窗口中，选择【已启用】，并将【安全层】设置为【RDP】。如下图所示：
![](https://main.qcloudimg.com/raw/25245ed985e5317078c80fa82d375a59.png)
4. 单击【确定】，完成设置。
5. 重启实例，重新尝试连接是否成功。
如果还是无法成功，请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213
) 进行反馈。
