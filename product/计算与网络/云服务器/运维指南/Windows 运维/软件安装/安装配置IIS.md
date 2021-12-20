## 操作场景

本文档以 Windows Server 2012 R2 操作系统和 Windows Server 2008 操作系统为例，介绍在 Windows 云服务器上进行 IIS 角色添加与安装。

## 操作步骤
### Windows Server 2012 R2 操作系统
1. 登录 Windows 云服务器。
2. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f779581f1ce3edfead8c725ce1504009.png" style="margin: -3px 0px;"></img>，打开服务器管理器。如下图所示：
![](https://main.qcloudimg.com/raw/4bdac63da39ed206ef3c3951d6ed5a13.png)
3. 单击**添加角色和功能**，弹出 “添加角色和功能向导” 窗口。
4. 在 “添加角色和功能向导” 窗口中，单击**下一步**。
5. 在 “选择安装类型” 界面，选择**基于角色或基于功能的安装**，并连续单击2次**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/9d97da8191fddcb8c1f97ee37cced18b.png)
6. 在 “选择服务器角色” 界面，勾选“Web 服务器(IIS)”。如下图所示：
弹出 “添加 Web 服务器(IIS) 所需的功能” 提示框。
![](https://main.qcloudimg.com/raw/def5577522de9a686b2c8b71db2d86f0.png)
7. 在弹出的 “添加 Web 服务器(IIS) 所需的功能” 提示框中，单击**添加功能**。如下图所示：
![](https://main.qcloudimg.com/raw/b1647bf6ee80ddf744c03e5521e6ee46.png)
8. 单击**下一步**。
9. 在 “选择功能” 界面，勾选 “.NET Framework 3.5 功能”，并连续单击2次**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/4c1e5002e5e609242d49735add718d15.png)
10. 在 “选择角色服务” 界面，勾选 “CGI”，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/9c4077b5e2eeab6c04e01fe4b9d629e6.png)
11. 确认安装信息，单击**安装**，并等待安装完成。如下图所示：
![](https://main.qcloudimg.com/raw/b39550bd4ae3d6e4be50040a165fa417.png)
12. 安装完成后，在云服务器的浏览器中访问 `http://localhost/`，验证 IIS 是否安装成功。
若出现以下界面，即表示成功安装。
![](//mc.qcloudimg.com/static/img/e064cc1f765d68edf3dcfb0051d5dbfa/image.png)

### Windows Server 2008 操作系统

1. 登录 Windows 云服务器。
2. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/0e33f3dc1042244ab225ca32c5396296.png" style="margin:-3px 0px;"></img>，打开服务器管理界面。如下图所示：
![](https://main.qcloudimg.com/raw/62d29927e615d282e79a8278b06b5053.png)
3. 在左侧导航栏中，选择**角色**，并在右侧窗口中单击**添加角色**。如下图所示：
![](https://main.qcloudimg.com/raw/d83b0a8fd599232cdd3df72e8dd99d40.png)
4. 在打开的 “添加角色向导” 窗口中，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/1ef476b1e0f16b25f622995792cb4eca.png)
5. 在 “选择服务器角色” 界面，勾选 “Web 服务器 (IIS)”，并连续单击2次**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/11854282507a671f46ba9bf0998b7a4d.png)
6. 在 “选择角色服务” 界面，勾选 “CGI”，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/227b434e77fc922761e4d9f03e0fc465.png)
7. 确认安装信息，单击**安装**，并等待安装完成。如下图所示：
![](https://main.qcloudimg.com/raw/074a6961e17ab3d3185c3504472509e4.png)
8. 安装完成后，在云服务器的浏览器中访问 `http://localhost/`，验证 IIS 是否安装成功。
若出现以下界面，即表示成功安装。
![](https://main.qcloudimg.com/raw/b11cd8170e7646daa3b9ca904b181cf4.png)

