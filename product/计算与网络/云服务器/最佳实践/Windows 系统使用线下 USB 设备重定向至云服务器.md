## 操作场景

RemoteFx 是 Windows RDP 桌面协议升级版，RDP 8.0起可以使用 RemoteFx 来使用 USB 重定向，将本地 USB 设备通过 RDP 的数据通道重定向到远程桌面，解决云端机器无法使用 USB 设备的问题。

本文档以如下环境版本为例，为您演示如何开启 RDP 的 RemoteFx USB Redirection 功能，重定向到云服务器中：
- 客户端：Windows 10 操作系统
- 服务端：Windows Server 2016 操作系统

## 使用限制

由于 RDP 8.0及以上版本均支持 RemoteFX USB Redirection 功能，Windows 8、Windows 10、Windows Server 2016 和 Windows Server 2019 均支持 RemoteFX USB Redirection 功能。如果您的本地计算机操作系统以上版本，不需要安装 RDP 8.0 Update 补丁。如果您的本地计算机操作系统为 Windows 7 或者 Windows Vista，请前往 [微软官网](https://support.microsoft.com/en-us) 获取和安装 RDP 8.0 Update 补丁。


## 操作步骤

### 配置服务端

1. [使用 RDP 文件登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)。
2. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/ab9a3a22baf69f63a90a43476f12db94.png" style="margin: 0;"></img>，选择**服务器管理器**，打开服务器管理器。
3. 在“服务器管理器”窗口中，单击**添加角色与功能**。如下图所示：
![](https://main.qcloudimg.com/raw/518287dced9ccc1de01cbf73315f70d1.png)
4. 在弹出的“添加角色和功能向导”窗口中，单击**下一步**，进入“选择安装类型”界面。
5. 在“选择安装类型”界面中，选择**基于角色或基于功能的安装**，单击**下一步**。
6. 在“选择目标服务器”界面中，保持默认设置，单击**下一步**。
7. 在“选择服务器角色”界面中，勾选**远程桌面服务**，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/05868c877afe2e6043e34e54c023408e.png)
8. 保持默认设置，连续单击2次**下一步**。
9. 在“选择角色服务”界面，勾选“远程桌面会话主机”、“远程桌面连接代理”和“远程桌面授权”，并在弹出的窗口中单击**添加功能**。如下图所示：
![](https://main.qcloudimg.com/raw/efc41c3d8c5b54d27664772587261460.png)
10. 单击**下一步**。
11. 单击**安装**。
13. 待完成安装后，重启云服务器。
14. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/330624bafb194914948c8ebd9e47334d.png" style="margin: 0;"></img>，输入 **gpedit.msc**，按 **Enter**，打开“本地组策略编辑器”。
15. 在左侧导航树中，选择**计算机配置** > **管理模板** > **Windows 组件** > **远程桌面服务** > **远程桌面会话主机** > **设备和资源重定向**，双击打开**不允许受支持的即插即用设备重定向**。如下图所示：
![](https://main.qcloudimg.com/raw/a812e4da0f4435b2ca351b286e283b2e.png)
16. 在弹出的窗口中，选择**已禁用**，单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/e9f02b468e39d2b78365514f91cb13d1.png)
17. 重启云服务器。


### 配置客户端

1. 在本地计算机上，右键单击 <img src="https://main.qcloudimg.com/raw/6e36af2ceb4604b81de13cb42f30e859.png" style="margin: 0;"></img>，选择**运行**，打开运行对话框。
2. 在运行对话框中，输入 **gpedit.msc**，单击**确定**，打开“本地组策略编辑器”。
3. 在左侧导航树中，选择**计算机配置** > **管理模板** > **Windows 组件** > **远程桌面服务** > **远程桌面连接客户端** > **RemoteFx USB 设备重定向**，双击打开**允许此计算机中受支持的其他 RemoteFx USB 设备的 RDP 重定向**。如下图所示：
![](https://main.qcloudimg.com/raw/760b413ec2fb3aec917716556875a99f.png)
4. 在弹出的窗口中，选择**已启用**，并将 RemoteFx USB 重定向访问权限设置为**管理员和用户**。如下图所示：
![](https://main.qcloudimg.com/raw/a34da80ec13c8c041662b2c1142c931e.png)
5. 单击**确定**。
6. 重启本地计算机。

### 验证配置效果

1. 在本地计算机上，插入 USB 设备，并右键单击 <img src="https://main.qcloudimg.com/raw/6e36af2ceb4604b81de13cb42f30e859.png" style="margin: 0;"></img>，选择**运行**，打开运行对话框。
2. 在运行对话框中，输入 **mstsc**，按 **Enter**，打开远程桌面连接对话框。如下图所示：
![](https://main.qcloudimg.com/raw/107284ef6b3548585f0598f419ec7b98.png)
3. 在**计算机**后面，输入 Windows 服务器的公网 IP，单击**显示选项**。
4. 选择**本地资源**页签，单击“本地设备和资源”栏中**详细信息**，弹出本地设备和资源窗口。如下图所示：
![](https://main.qcloudimg.com/raw/ab14993dae9d7c7bf22b9443c5badc13.png)
5. 在弹出本地设备和资源窗口中，展开**其他支持的 RemoteFx USB 设备**，勾选插入的 USB 设备，单击**确定**。
![](https://main.qcloudimg.com/raw/9c86c1ad14906f4e2566a26eceaf91de.png)
6. 单击**连接**。
7. 在弹出的 “Windows 安全性” 窗口中，输入实例的管理员帐号和密码。如下图所示：
![](https://main.qcloudimg.com/raw/0a0ffbf1f09c8bac278d97adb9e5ac96.png)
8. 单击**确定**，登录 Windows 实例。
Windows 实例的操作界面上方出现 <img src="https://main.qcloudimg.com/raw/73fe2b3cfa740517e44e4596a222840a.png" style="margin: 0;"></img>，即表示配置成功。
![](https://main.qcloudimg.com/raw/751a4e2204cc38a0769116732c464789.png)


## 相关操作

Windows RDP 协议可以为常用的 USB 设备提供更优化的连接性能，即不需要开启 RemoteFx 功能便可直接映射设备，例如驱动器和摄像头等。不常用的 USB 设备则只能通过 RemoteFX USB Redirection 来实现。不常用的 USB 设备可参考如下内容，选择相应的重定向方式：
![](https://main.qcloudimg.com/raw/715de06c08753eefe6e4ff5cc3bca270.png)



