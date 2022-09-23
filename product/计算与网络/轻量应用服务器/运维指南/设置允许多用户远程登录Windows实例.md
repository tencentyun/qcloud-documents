## 操作场景
本文档以使用 Windows Server 2016 系统镜像的轻量应用服务器为例，指导您配置多用户远程登录 Windows 实例。

<dx-alert infotype="notice" title="">
微软提供的多用户远程登录功能试用期为120天，若未购买多用户登录授权（RDS CALs），则试用期结束后会导致无法通过远程桌面登录轻量应用服务器，只能通过 mstsc /admin 命令登录。Windows Server 默认允许2个用户同时登录，可满足多数需求。请您结合实际业务场景进行评估，若有强烈需求需配置多用户远程登录，请参考本文进行操作。
</dx-alert>


## 操作步骤

### 添加远程桌面服务
1. 参考 [使用标准方式（WebRDP）登录 Windows 实例](https://cloud.tencent.com/document/product/1207/75048)，登录 Windows 实例。
2. 在操作系统界面单击 <img src="https://qcloudimg.tencent-cloud.cn/raw/10c0728e4d194732be4eb6c1a95e0a8c.png" style="margin: -5px 0px;"/>，在弹出的界面中选择 <img src="https://qcloudimg.tencent-cloud.cn/raw/4cee830d425d629700d4569c49d3cb7c.png" style="margin: -5px 0px;"/>，打开“服务器管理器”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/721212fa585fb945139552aa7bdd1d63.png)
3. 单击**添加角色和功能**，弹出 “添加角色和功能向导” 窗口。
4. 在“添加角色和功能向导”窗口中，保持默认参数，连续单击三次**下一步**。
5. 在“选择服务器角色”界面，勾选“远程桌面服务”，单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7e33739e578ed25f780373238ef17240.png)
6. 保持默认参数，连续单击两次**下一步**。
7. 在“选择角色服务”界面，勾选**远程桌面会话主机**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e6ef6d4532a40d8684aecacd2c265f13.png)
8. 弹出“添加 远程桌面会话主机 所需的功能”提示框。在提示框中，单击**添加功能**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8f256c081e2a14770acd085297f30e79.png)
9. 在“选择角色服务”界面，勾选“远程桌面授权”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1ac8a2bf03f735cdfca28eb437bba559.png)
10. 弹出 “添加 远程桌面授权 所需的功能” 提示框。在提示框中，单击**添加功能**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ebabf7606f80930cf3800ca9bdf070b8.png)
11. 单击**下一步**。
12. 勾选“如果需要，自动重新启动目标服务器”，并在弹出的提示框中单击**是**。
13. 单击**安装**，等待远程桌面服务安装完成。


### 申请多用户登录授权许可证
1. 在操作系统界面单击 <img src="https://qcloudimg.tencent-cloud.cn/raw/10c0728e4d194732be4eb6c1a95e0a8c.png" style="margin: -5px 0px;"/>，在弹出的界面中选择 <img src="https://qcloudimg.tencent-cloud.cn/raw/4cee830d425d629700d4569c49d3cb7c.png" style="margin: -5px 0px;"/>，打开“服务器管理器”。
2. 在“服务器管理器”窗口中，选择右上角的**工具** > **Remote Desktop Services** > **远程桌面授权管理器**。
3. 在弹出的 “RD 授权管理器”窗口中，右键单击服务器所在行，并选择**激活服务器**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/862ee285c4eca41f300ef4d516eae8ba.png)
4. 在弹出的“服务器激活向导”窗口中，单击**下一步**。
5. 在“连接方法”设置中，本文选择 “Web 浏览器”，并单击**下一步**。如下图所示：
您也可以结合实际情况选择其他连接方式。
![](https://qcloudimg.tencent-cloud.cn/raw/0884f8fab22d476a2d07e1e60b65f515.png)
6. [](id:Step6)在“许可证服务器激活”中，记录产品 ID 并访问 [远程桌面授权网站](https://activate.microsoft.com/)。
7. 在远程桌面授权网站中，选择“启用许可证服务器”，并单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/93faa607f0fdd76eaadba989876a3dc4.png)
8. 输入 [步骤6](#Step6) 获取的产品 ID，并根据实际情况填写公司信息后，单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/32c16ece864ab55e3988caced1cdeeaf.png)
9. 确认输入信息无误后，单击**下一步**。
10. [](id:Step10)记录许可证服务器 ID，并单击**是**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a06aeb049e55d4137791b3c52014dddd.png)
11. 输入上一步获取的许可证服务器 ID，并按需选择授信息，填写公司信息后单击**下一步**。如下图所示：
本文授权信息以选择“企业协议”为例。
![](https://qcloudimg.tencent-cloud.cn/raw/162cbea63445b30a8e53776ae8d06ce0.png)
12. 选择产品类型，并输入数量及许可证授权信息。如下图所示：
<dx-alert infotype="explain" title="">
您可前往 [微软官网](https://www.microsoftstore.com.cn/software/software)，联系客服购买 RDS CALs 授权。
</dx-alert>
<img src="https://qcloudimg.tencent-cloud.cn/raw/f7c35e9f47806167746a9a2e58078bc3.png"/>
13. 确认信息无误后，单击**下一步**。
14. [](id:Step14)获取并记录密钥包 ID。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c865378c5da3531f10511a535a9d600f.png)
15. 单击**结束**。


### 激活远程桌面服务许可证服务器
1. 在操作系统界面单击 <img src="https://qcloudimg.tencent-cloud.cn/raw/10c0728e4d194732be4eb6c1a95e0a8c.png" style="margin: -5px 0px;"/>，在弹出的界面中选择 <img src="https://qcloudimg.tencent-cloud.cn/raw/4cee830d425d629700d4569c49d3cb7c.png" style="margin: -5px 0px;"/>，打开“服务器管理器”。
2. 在“服务器管理器”窗口中，选择右上角的**工具** > **Remote Desktop Services** > **远程桌面授权管理器**。
3. 在弹出的 “RD 授权管理器”窗口中，右键单击服务器所在行，并选择**激活服务器**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/862ee285c4eca41f300ef4d516eae8ba.png)
4. 在弹出的“服务器激活向导”窗口中，单击**下一步**。
5. 在“连接方法”设置中，本文选择 “Web 浏览器”，并单击**下一步**。如下图所示：
您也可以结合实际情况选择其他连接方式。
![](https://qcloudimg.tencent-cloud.cn/raw/0884f8fab22d476a2d07e1e60b65f515.png)
6. 在“许可证服务器激活”中，输入 [步骤10](#Step10) 获取的许可证服务器 ID，并单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/895e7b811fc170b870416f9aef7693ee.png)
12. “服务器激活向导”窗口中提示“你已完成服务器激活向导”时，单击**下一步**进入许可证安装步骤。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f50d694cf5f2000585b7851545649caf.png)


### 安装 RDS 客户端访问许可证
1. 在“许可证安装向导”页面中，确认许可证服务器信息，并单击**下一步**。
2. 在“获取客户端许可证密钥包”中，输入 [步骤14](#Step14) 获取的许可证服务器 ID，并单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d92e9fd24c481ac6ee3c0189fd1ebe20.png)
3. “许可证安装向导”窗口中提示“你已完成许可证安装向导”即表示已成功安装许可证。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e5d6e9522af714a4fa30ba182c45c40e.png)


### 配置远程桌面会话主机授权服务器
1. 在操作系统界面单击 <img src="https://qcloudimg.tencent-cloud.cn/raw/10c0728e4d194732be4eb6c1a95e0a8c.png" style="margin: -5px 0px;"/>，在弹出的界面中选择 <img src="https://qcloudimg.tencent-cloud.cn/raw/4cee830d425d629700d4569c49d3cb7c.png" style="margin: -5px 0px;"/>，打开“服务器管理器”。
2. 在“服务器管理器”窗口中，选择右上角的**工具** > **Remote Desktop Services** > **远程桌面授权诊断程序**。查看当前服务器状态，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/49243ae49a97444dbabd8aac844cd38b.png)
3. 在操作系统界面右键单击 <img src="https://qcloudimg.tencent-cloud.cn/raw/10c0728e4d194732be4eb6c1a95e0a8c.png" style="margin: -5px 0px;"/>，在弹出菜单中选择**运行**。
4. 在“运行”窗口中输入 **gpedit.msc**，并按 **Enter** 打开计算机本地组策略。
5. 在左侧导航树中，选择**计算机配置** > **管理模板** > **Windows 组件** > **远程桌面服务** > **远程桌面会话主机** > **授权**，双击打开“使用指定的远程桌面许可服务器”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/22b21ae6075aaa7c2ddc0dbcf010b5f0.png)
6. 在弹出的“使用指定的远程桌面许可证服务器”窗口中，选择“已启用”，并在选项中输入“要使用的许可证服务器”，可输入轻量应用服务器公网 IP 或主机名。设置完成后单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2bbb91952f87121ee7a6ef6860783120.png)
7. 双击打开“设置远程桌面授权模式”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/aad3343e9fe40636cd1a8c40a3abfab1.png)
8. 在弹出的“设置远程桌面授权模式”窗口中，选择“已启用”，并指定 RD 会话主机服务器的授权模式为“按用户”。设置完成后单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/666c093b280a2706dc70c060b336d106.png)
9. 重启轻量应用服务器。


### 配置用户使用远程桌面服务时不限数量连接
1. 在操作系统界面右键单击 <img src="https://qcloudimg.tencent-cloud.cn/raw/10c0728e4d194732be4eb6c1a95e0a8c.png" style="margin: -5px 0px;"/>，在弹出菜单中选择**运行**。
2. 在“运行”窗口中输入 **gpedit.msc**，并按 **Enter** 打开计算机本地组策略。
3. 在左侧导航树中，选择**计算机配置** > **管理模板** > **Windows 组件** > **远程桌面服务** > **远程桌面会话主机** > **连接**，双击打开“将远程桌面服务用户限制到单独的远程桌面服务会话”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0bc74ee837eb345af313e48fd0f24aba.png)
4. 在弹出的“使用指定的远程桌面许可证服务器”窗口中，选择“已禁用”，以允许用户通过使用远程桌面服务进行不限数量的同时远程连接。设置完成后单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0db425f63fb7dd9b6ae46623d9008986.png)
5. 双击打开“限制连接的数量”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f0d3627dc01901e789d01f0b81bddc50.png)
3. 在弹出的“限制连接的数量”窗口中，选择“已启用”，并根据实际需求填写允许 RD 最大连接数。设置完成后单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a05d039bc7c0f2d21262c9c89a0490d8.png)


至此您已完成多用户远程登录配置。

## 参考资料
- [License your RDS deployment with client access licenses (CALs)](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-client-access-license)
- [Activate the Remote Desktop Services license server](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-activate-license-server)
- [Install RDS client access licenses on the Remote Desktop license server](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-install-cals)


