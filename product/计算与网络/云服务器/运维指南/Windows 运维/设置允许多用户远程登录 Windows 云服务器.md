## 操作场景
本文档以 Windows Server 2012 R2 操作系统云服务器为例，指导您配置多用户远程登录 Windows 云服务器。

## 操作步骤
### 添加远程桌面服务
1. 登录 Windows 云服务器。
2. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f779581f1ce3edfead8c725ce1504009.png" style="margin: 0;"></img>，打开 “服务器管理器”。如下图所示：
![](https://main.qcloudimg.com/raw/4bdac63da39ed206ef3c3951d6ed5a13.png)
3. 单击【添加角色和功能】，弹出 “添加角色和功能向导” 窗口。
4. 在 “添加角色和功能向导” 窗口中，保持默认参数，连续单击三次【下一步】。
5. 在 “选择服务器角色” 界面，勾选【远程桌面服务】，单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/a395eee56ec77e729faf8b6d3217566d.png)
6. 保持默认参数，连续单击两次【下一步】。
7. 在 “选择角色服务” 界面，勾选【远程桌面会话主机】，弹出 “添加 远程桌面会话主机 所需的功能” 提示框。
8. 在 “添加 远程桌面会话主机 所需的功能” 提示框中，单击【添加功能】。如下图所示：
![](https://main.qcloudimg.com/raw/d21de386096c36baa0a4382f4d8f59e1.png)
9. 在 “选择角色服务” 界面，勾选【远程桌面授权】，弹出 “添加 远程桌面授权 所需的功能” 提示框。
10. 在 “添加 远程桌面授权 所需的功能” 提示框中，单击【添加功能】。
![](https://main.qcloudimg.com/raw/f10d21c2f28d5f49841b4aac656b9efa.png)
11. 单击【下一步】。
12. 勾选【如果需要，自动重新启动目标服务器】，并在弹出的提示框中单击【是】。如下图所示：
![](https://main.qcloudimg.com/raw/05a63b7593c57573a5c19b03ae4cd4a5.png)
13. 单击【安装】，等待远程桌面服务安装完成。
安装远程桌面服务约需3 - 5分钟。

### 配置多用户远程登录实例
1. [使用 VNC 登录 Windows 云服务器](https://cloud.tencent.com/document/product/213/35704)。
2. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: 0;"></img>，打开 Windows PowerShell 窗口。
3. 在 Windows PowerShell 窗口中，输入 gpedit.msc，按 Enter，打开 “本地组策略编辑器”。
4. 在左侧导航树中，选择【计算机配置】>【管理模板】>【Windows 组件】>【远程桌面服务】>【远程桌面会话主机】>【连接】，双击打开【限制连接的数量】。如下图所示：
![](https://main.qcloudimg.com/raw/5db10d892563f1492584f98ed550d67c.png)
5. 在弹出的 “限制连接的数量” 窗口中，选择【已启用】，并在【允许的 RD 最大连接数】中填写最大同时远程用户数。如下图所示：
![](https://main.qcloudimg.com/raw/72b16384df297cbaae5619d841e4369f.png)
6. 单击【确定】，并关闭本地组策略编辑器。
7. 重启实例。
