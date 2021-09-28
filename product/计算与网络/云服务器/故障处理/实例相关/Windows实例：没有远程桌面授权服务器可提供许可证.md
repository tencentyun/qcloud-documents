本文介绍远程连接 Windows 实例时，提示出现 “由于没有远程桌面授权服务器可以提供许可证，远程会话连接已断开” 这类告警提示的处理方法。

## 故障现象

Windows 使用远程桌面连接 Windows 实例时，提示 “由于没有远程桌面授权服务器可以提供许可证，远程会话连接已断开。请跟服务器管理员联系”。如下图所示：
![](https://main.qcloudimg.com/raw/4bfce19b16c2920adefccd123f2a021d.png)

## 故障原因

导致出现以上提示的主要原因如下（不限于以下情况，请根据实际情况进行分析）：
- 系统默认配置 RDP-Tcp 限制，每个用户只能进行一个会话。若该帐号已被登录，其他会话将无法建立。
- 系统添加了“远程桌面会话主机”角色功能，但该角色功能的授权已到期。
“远程桌面会话主机”角色功能免费使用120天，功能到期后，需要付费才能使用。

## 解决方案
### 通过 VNC 方式登录云服务器

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，找到目标云服务器实例，单击**登录**。如下图所示：
![](https://main.qcloudimg.com/raw/038fce530c6c6827796e51d896306a93.png)
3. 在弹出的 “登录Windows实例” 窗口中，选择**其它方式（VNC）**，单击**立即登录**，登录云服务器。
4. 在弹出的登录窗口中，选择左上角的 “发送远程命令”，单击 **Ctrl-Alt-Delete** 进入系统登录界面。如下图所示：
![](https://main.qcloudimg.com/raw/2dec43fa6ddb5e442da59c75f7a34b0f.png)

### 方案一：修改策略配置
1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: 0;">，打开 “Windows PowerShell” 窗口。
2. 在 “Windows PowerShell” 窗口中，输入 **gpedit.msc**，按 **Enter**，打开“本地组策略编辑器”。
3. 在左侧导航树中，选择**计算机配置** > **管理模板** > **Windows 组件** > **远程桌面服务** > **远程桌面会话主机** > **连接**，双击打开**限制连接的数量**。如下图所示：
![](https://main.qcloudimg.com/raw/5db10d892563f1492584f98ed550d67c.png)
4. 在弹出的 “限制连接的数量” 窗口中，根据实际需求，修改**允许的 RD 最大连接数**，单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/31bf2ed32474a71f1fc1c806c55111c1.png)
5. 切换至 “Windows PowerShell” 窗口。
6. 在 “Windows PowerShell” 窗口中，输入 **gpupdate**，按 **Enter**，更新策略。


### 方案二：删除“远程桌面会话主机”角色
>? 如果您不想删除“远程桌面会话主机”角色，可跳过此步骤，前往 [微软官网](https://www.microsoft.com/zh-cn/) 购买与配置相应的证书授权。
>
1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f779581f1ce3edfead8c725ce1504009.png" style="margin: 0;">，打开 “服务器管理器”。
2. 单击 “服务器管理器” 右上方的**管理**，选择**删除角色和功能**。如下图所示：
![](https://main.qcloudimg.com/raw/c50d1df5fdf65abd3f301ba904e80817.png)
3. 在 “删除角色和功能向导” 窗口中，单击**下一步**。
4. 在 “删除服务器角色” 界面，取消勾选**远程桌面服务**，并在弹出的提示框中，选择**删除功能**。如下图所示：
![](https://main.qcloudimg.com/raw/974994d5cb387ea3aa8baec6ffdc9d7f.png)
6. 单击两次**下一步**。
7. 勾选“如果需要，自动重新启动目标服务器”，并在弹出的提示框中单击**是**。如下图所示：
![](https://main.qcloudimg.com/raw/bb3b938d970a225884ec36e61e18b526.png)
8. 单击**删除**。
待云服务器重新启动即可。




