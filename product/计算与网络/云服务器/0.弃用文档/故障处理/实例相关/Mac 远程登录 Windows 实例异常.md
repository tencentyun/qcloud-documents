## 问题描述

Mac 通过 Microsoft Remote Desktop 远程连接登录 Windows 时，提示 “The certificate couldn't be verified back to a root certificate.”。如下图所示：
![Microsoft Remote Desktop](https://main.qcloudimg.com/raw/070b9c862d6928988768b266461bc816.png)
或者 Mac 远程桌面连接（Remote Desktop Connection）时，提示 “远程桌面连接无法验证您希望连接的计算机是的身份。”。如下图所示：
![Mac 远程桌面连接](https://main.qcloudimg.com/raw/32f0444a47b2e4c90f6657ec9686afcb.png)


## 解决方案

通过浏览器 VNC 方式登录实例，修改实例的本地组策略解决，详细操作步骤如下：
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在 “云主机” 页面中，选择连接异常的 CVM 实例，单击【登录】。如下图所示：
![登录](https://main.qcloudimg.com/raw/56596196a93181ac4c9467abe19c383a.png)
3. 在弹出的 “登录Windows云服务器” 窗口中，选择 “浏览器 VNC 方式登录”，单击【立即登录】。如下图所示：
![VNC登录](https://main.qcloudimg.com/raw/80b613a90328bb34a006d5988dcff18b.png)
4. 在弹出的登录窗口中，选择左上角的 “发送远程命令”，单击 **Ctrl-Alt-Delete** 进入系统登录界面。如下图所示：
![VNC界面](https://main.qcloudimg.com/raw/27daf8cc33746b195c74dfb5066addee.png)
5. 在操作系统界面，选择【开始】>【运行】，输入 **gpedit.msc**。如下图所示：
>? 也可使用 “Win+R” 快捷键打开运行界面。

 ![运行](https://main.qcloudimg.com/raw/9a0bed85a419457263f975c7c03f108d.png)

6. 按 **Enter**，打开本地组策略略编辑器。
7. 在左侧导航树中，选择【计算机配置】>【管理模板】>【windows组件】>【远程桌面服务】>【安全】，双击【远程（RDP）连接要求使用指定的安全层】。如下图所示：
![RDP](https://main.qcloudimg.com/raw/7999d6708024948b87b6739103dac208.png)
8. 在弹出的 “远程（RDP）连接要求使用指定的安全层” 窗口中，将 “远程（RDP）连接要求使用指定的安全层” 设置为 “已启用”，并将 “安全层” 选择为 “RDP”。如下图所示：
![配置修改](https://main.qcloudimg.com/raw/35b2ab9d3b34e6f39ba1a31641f66446.png)
9. 单击【应用】。
10. 单击【确认】。 
