## 现象描述
Windows 操作系统的本地计算机通过远程桌面登录 Windows 轻量应用服务器时，提示如下报错信息：
你的凭据无法工作，之前用于连接到 `XXX.XXX.XXX.XXX` 的凭据无法工作。请输入新凭据。
![](https://main.qcloudimg.com/raw/e19f89876a50bf177713bdae8365b0b4.png)



## 处理步骤


<dx-alert infotype="explain" title="">
- 本文以 Windows Server 2012 R2 操作系统的轻量应用服务器为例，根据操作系统的版本不同，详细操作步骤略有区别。
- 请按照以下步骤依次排查，并在每一个步骤执行完后重新登录 Windows 轻量应用服务器以验证问题是否解决，如未生效请继续执行下一步骤。
</dx-alert>



### 步骤1：修改网络访问策略
1. [使用 VNC 方式登录 Windows 实例](https://cloud.tencent.com/document/product/1207/44656)。
2. 右键单击 <img src="https://main.qcloudimg.com/raw/526d966f01c95ac39eff13f414c88ab6.png" style="margin:-3px 0px"> ，打开“运行”窗口。
3. 输入 **gpedit.msc** 并按 **Enter**，打开“本地组策略编辑器”。
4. 在“本地组策略编辑器”窗口的左侧导航栏中，依次展开**计算机配置** > **Windows 设置** > **安全设置** > **本地策略** > **安全选项**目录。
5. 选择**安全选项**，找到并双击打开**网络访问：本地帐户的共享和安全模型**。如下图所示：
![](https://main.qcloudimg.com/raw/5eb7791ae9ffb3c5cb6f897ba9c8de91.png)
6. 选择**经典 - 对本地用户进行身份验证，不改变其本来身份**，并单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/d2c8ea1d77c9926e49b30269b44482bd.png)
7. 重新登录 Windows 轻量应用服务器，验证是否可成功登录。
 - 是，任务结束。
 - 否，请执行下一步。


### 步骤2：修改凭据分配
1. 在“本地组策略编辑器”窗口的左侧导航栏中，依次展开**计算机配置** > **管理模板** > **系统** > **凭据分配**目录。
2. 选择**凭据分配**，找到并双击打开**允许分配保存的凭据用于仅 NTLM 服务器身份验证**。如下图所示：
![](https://main.qcloudimg.com/raw/7de0e8b0426a81e929543a92bcb998bb.png)
3. 在打开的窗口中，选择**已启用**，单击“选项”中的**显示**，在弹出窗口中输入 `TERMSRV/*`，并单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/6ac18ce645ca0366d02c8f1b23a324e4.png)
4. 单击**确定**。
5. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin:-3px 0px">，打开 “Windows PowerShell” 窗口。
6. 在 “Windows PowerShell” 窗口中，输入 **gpupdate /force**，并按 **Enter** 更新组策略。如下图所示：
![](https://main.qcloudimg.com/raw/13554054a53501ff53699c55b7f55da3.png)
7. 重新登录 Windows 轻量应用服务器，验证是否可成功登录。
 - 是，任务结束。
 - 否，请执行下一步。


### 步骤3：设置本地主机的凭据
1. 在操作系统界面，右键单击 <img src="https://main.qcloudimg.com/raw/526d966f01c95ac39eff13f414c88ab6.png" style="margin:-3px 0px">，在弹出的菜单中选择**控制面板**。
2. 在控制面板中，选择**用户帐户**，并单击**凭据管理器**下的**管理 Windows 凭据**，进入 Windows 凭据界面。
3. 查看 Windows 凭据下是否有当前登录的轻量应用服务器凭据。如下图所示：
![](https://main.qcloudimg.com/raw/4ffb83718a57a97177ae9980b9145654.png)
 - 无，请执行下一步，添加 Windows 凭据。
 - 有，请执行 [步骤4：关闭轻量应用服务器密码保护共享](#Step4)。
4. 单击**添加 Windows 凭据**，进入添加 Windows 凭据界面。如下图所示：
![](https://main.qcloudimg.com/raw/78a5a17c5a4d647777e0348af22e1ed9.png)
 按照以下信息配置凭据信息：
 - **Internet 地址或网络地址段**：轻量应用服务器公网 IP 地址。登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，可在服务器列表页中获取公网 IP。
 - **用户名**：Windows 实例默认用户名为 `Administrator`，您也可输入自定义用户名。
 - **密码**：登录密码由您在创建实例时设置，如忘记密码，则请 [重置密码](https://cloud.tencent.com/document/product/1207/44575)。
5. 单击**确定**。
6. 重新登录 Windows 轻量应用服务器，验证是否可成功登录。
 - 是，任务结束。
 - 否，请执行下一步。



### 步骤4：关闭轻量应用服务器密码保护共享[](id:Step4)
1. 在操作系统界面，右键单击 <img src="https://main.qcloudimg.com/raw/526d966f01c95ac39eff13f414c88ab6.png" style="margin:-3px 0px">，在弹出的菜单中选择**控制面板**。
2.  在控制面板中，选择**网络和 Internet** > **网络和共享中心** > **更改高级共享设置**，进入高级共享设置界面。
3.  展开**所有网络**页签，并在“密码保护的共享”下选择**关闭密码保护共享**。如下图所示：
![](https://main.qcloudimg.com/raw/16860f9f0a45889deab56bf9519e5029.png)
4.  单击**保存更改**。
5. 重新登录 Windows 轻量应用服务器，验证是否可成功登录。
 - 是，任务结束。
 - 否，请通过 [在线支持](https://cloud.tencent.com/act/event/Online_service?from=doc_1207) 进行反馈。

