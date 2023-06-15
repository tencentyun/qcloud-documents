## 现象描述

Windows 操作系统的本地计算机通过 RDP 协议（如 MSTSC 方式）远程桌面连接登录 Windows 云服务器时，出现如下报错：
您的凭据无法工作，之前用于连接到 `XXX.XXX.XXX.XXX` 的凭据无法工作。请输入新凭据。
>?如果输入新凭据，仍提示凭据不工作，请同时检查您的用户名是否拼写正确（Windows系统默认用户名为 Administrator）。
   

![](https://main.qcloudimg.com/raw/74c6302cc36d82e5add5d9ea872d4572.png)
## 可能原因
<table>
<thead>
  <tr>
    <th>可能原因</th>
    <th>处理措施</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Windows 实例网络访问策略未修改</td>
    <td ><a href="#eax">检查并修改 Windows 实例网络访问策略</a></td>
  </tr>
  <tr>
    <td>Windows 实例凭据未分配</td>
    <td><a href="#step01">检查并修改 Windows 实例凭据分配</a></td>
  </tr>
  <tr>
    <td>Windows 实例本地主机的凭据未设置</td>
    <td><a href="#step02">检查并设置 Windows 实例本地主机的凭据</a></td>
  </tr>
  <tr>
    <td>云服务器密码保护共享未关闭</td>
    <td><a href="#step03">检查并关闭云服务器密码保护共享</a></td>
  </tr>
</tbody>
</table>

## 故障处理

<dx-alert infotype="explain" title="">
- 本文以 Windows Server 2012 操作系统的腾讯云云服务器为例，根据操作系统的版本不同，详细操作步骤略有区别。
- 请按照以下步骤依次排查，并在每一个步骤执行完后重新连接 Windows 云服务器验证问题是否解决，如未生效请继续执行下一步骤。
</dx-alert>

### 检查并修改 Windows 实例网络访问策略[](id:eax)
1. [使用 VNC 登录 Windows 实例](https://cloud.tencent.com/document/product/213/35704)。
2. 在操作系统界面，单击 <img style="width:20px; max-width: inherit;" src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" />，打开 **Windows PowerShell** 窗口。
3. 在 **Windows PowerShell** 窗口中，输入 **gpedit.msc**，按 **Enter**，打开**本地组策略编辑器**。
4. 在左侧导航栏中，依次展开**计算机配置** > **Windows 设置** > **安全设置** > **本地策略** > **安全选项**目录。
5. 找到并打开**安全选项**中的**网络访问：本地帐户的共享和安全模型**。如下图所示：
![](https://main.qcloudimg.com/raw/183e8050ea081cb4634f0d3b8ef90d0a.png)
6. 选择**经典 - 对本地用户进行身份验证，不改变其本来身份**，单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/51dd491d451560dd0d963fb35335405e.png)
7. 重新连接 Windows 云服务器，验证连接是否成功。
 - 验证连接已成功，任务结束。
 - 验证连接未成功，请 [检查并修改 Windows 实例凭据分配](#step01)。

### 检查并修改 Windows 实例凭据分配[](id:step01)
1. 在**本地组策略编辑器**的左侧导航栏中，依次展开**计算机配置** > **管理模板** > **系统** > **凭据分配**目录。
2. 找到并打开**凭据分配**中的**允许分配保存的凭据用于仅 NTLM 服务器身份验证**。如下图所示：
![](https://main.qcloudimg.com/raw/10eeb0291b2a4fd91c316c39b523370d.png)
3. 在打开的窗口中，选择**已启用**，并在**选项**的**显示**中输入`TERMSRV/*`，单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/98ae861b892233e481d5c52f89ccb333.png)
4. 单击**确定**。
5. 在操作系统界面，单击 <img style="width:20px; max-width: inherit;" src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" />，打开 **Windows PowerShell** 窗口。
6. 在 **Windows PowerShell** 窗口中，输入 **gpupdate /force**，按 **Enter**，更新组策略。如下图所示：
![](https://main.qcloudimg.com/raw/077166adce1756333626312a0d3531cc.png)
7. 重新连接 Windows 云服务器，验证连接是否成功。
 - 验证连接已成功，任务结束。
 - 验证连接未成功，请 [检查并设置 Windows 实例本地主机的凭据](#step02)。

### 检查并设置 Windows 实例本地主机的凭据[](id:step02)
1. 在操作系统界面，单击 <img style="width:20px; max-width: inherit;" src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" /> >  **控制面板** > **用户帐户**，选择**凭据管理器**下的**管理 Windows 凭据**，进入 Windows 凭据界面。如下图所示：
![](https://main.qcloudimg.com/raw/32f4e4d6ec88ddea583cf452b830e597.png)
2. 查看 Windows 凭据下是否有当前登录的云服务器凭据。
 - 如果没有，请执行下一步，添加 Windows 凭据。
 - 如果有，请 [检查并关闭云服务器密码保护共享](#step03)。
3. 单击**添加 Windows 凭据**，进入添加 Windows 凭据界面。如下图所示：
![](https://main.qcloudimg.com/raw/724a1b20fe2560f2c047082c32f18161.png)
4. 输入当前登录的云服务器 IP 地址、用户名和密码，单击**确定**。
<dx-alert infotype="explain" title="">
- 云服务器 IP 地址即为云服务器公网 IP 地址，获取方式请参见 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940) 。
- Windows 实例默认用户名为 `Administrator`，密码由您在创建实例时设置。如果您忘记了登录密码，请参见 [重置实例密码](https://cloud.tencent.com/document/product/213/16566) 进行密码重置。
</dx-alert>
5. 重新连接 Windows 云服务器，验证连接是否成功。
 - 验证连接已成功，任务结束。
 - 验证连接未成功，请 [检查并关闭云服务器密码保护共享](#step03)。


### 检查并关闭云服务器密码保护共享[](id:step03)
1. 在操作系统界面，单击 <img style="width:20px; max-width: inherit;" src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" /> > **控制面板** > **网络和 Internet** > **网络和共享中心** > **更改高级共享设置**，进入高级共享设置界面。如下图所示：
![](https://main.qcloudimg.com/raw/cc6b96db18a04e3e4c16f953df362b62.png)
2. 展开**所有网络**页签，并在**密码保护的共享**下选择**关闭密码保护共享**，单击**保存更改**。
3. 重新连接 Windows 云服务器，验证连接是否成功。
 - 验证连接已成功，任务结束。
 - 验证连接未成功，请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213) 反馈。

