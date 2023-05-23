## 现象描述

通过远程桌面连接登录 Windows 实例时，出现以下报错：
- **发生身份验证错误，给函数提供标志无效**，如下图所示：
![给函数提供标志无效](https://main.qcloudimg.com/raw/cbb3b5ea89ed9d3a65af8b303880b7c8.png)
- **发生身份验证错误。要求的函数不受支持**，如下图所示：
![要求函数不支持](https://main.qcloudimg.com/raw/09ff95a4f2e46e93a75d0e6ec38c1954.png)

由于微软于2018年3月发布了一个安全更新，此更新通过更正凭据安全支持提供程序协议（CredSSP），以及在身份验证过程中验证请求的方式，修复 CredSSP 存在的远程执行代码漏洞。客户端和服务器都需要安装此更新，否则可能出现问题描述中的情况。
![客户端服务器匹配情况](https://main.qcloudimg.com/raw/2734e664e7d72b083c37db3a4dc13647.png)
如上图所示，以下三种情况均会引起远程连接失败：
- 情况一：客户端未修补，服务器安装了安全更新，并且策略配置为**强制更新的客户端**。
- 情况二：服务器未修补，客户端安装了安全更新，并且策略配置为**强制更新的客户端**。
- 情况三：服务器未修补，客户端安装了安全更新，并且策略配置为**缓解**。

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
    <td>服务器或客户端未安装安全更新</td>
    <td><a href="#step4">检查服务端或客户端并安装安全更新（推荐）</a></td>
  </tr>
  <tr>
    <td>本地组策略未配置</td>
    <td><a href="#step02">检查并修改本地组策略配置</a></td>
  </tr>
  <tr>
    <td>系统中的注册表未修改</td>
    <td><a href="#Plan3">检查并修改系统中的注册表</a></td>
  </tr>
</tbody>
</table>

## 故障处理

### 通过 VNC 登录云服务器[](id:eax)
VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装或者无法使用远程登录客户端，以及通过其他方式均无法登录的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作，具体操作请参见：[使用 VNC 登录 Windows 实例](https://cloud.tencent.com/document/product/213/35704)。


### 检查服务端或客户端并安装安全更新（推荐）[](id:step4)

安装安全更新，可更新未修补的服务端或客户端。不同系统对应的更新情况可参见 [CVE-2018-0886 | CredSSP 远程执行代码漏洞](https://portal.msrc.microsoft.com/zh-cn/security-guidance/advisory/CVE-2018-0886)。本方案以 Windows Server 2016 为例。
其他操作系统可参见以下操作进入 **Windows 更新**：
- Windows Server 2012：<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;width: 22px;"></img> > **控制面板** > **系统和安全** > **Windows 更新**
- Windows Server 2008：**开始** > **控制面板** > **系统和安全** > **Windows Update**
- Windows10：<img src="https://main.qcloudimg.com/raw/6e36af2ceb4604b81de13cb42f30e859.png" style="margin:-3px 0px;"></img> > **设置** > **更新和安全**
- Windows 7：<img src="https://main.qcloudimg.com/raw/370daffec54024ee262d1e5dbcd4bde2.png" style="margin:-3px 0px;width: 28px;"></img> > **控制面板** > **系统和安全** > **Windows Update**


1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/6e36af2ceb4604b81de13cb42f30e859.png" style="margin:-3px 0px;"></img>，选择**设置**。如下图所示：
<img style="width:850px; max-width: inherit;" src="https://main.qcloudimg.com/raw/c5add12cacd642aad479bc356cec04f1.png" />
2. 在打开的**设置**窗口中，选择**更新和安全**。如下图所示：
![更新与安全](https://main.qcloudimg.com/raw/59c7b0c52eee2c5572b73b062edd3ce9.png)
3. 在**更新和安全**中，选择 **Windows 更新**，单击**检查更新**。如下图所示：
![检查更新](https://main.qcloudimg.com/raw/0aefedca7c90bcad7b39de781e9521df.png)
4. 根据界面提示，单击**开始安装**。
5. 安装完成后，重启实例，完成更新。

### 检查并修改本地组策略配置[](id:step02)

在已安装安全更新的机器中，将**加密 Oracle 数据库修正**策略设置为**易受攻击**。本方案以 Windows Server 2016 为例，其操作步骤如下：


<dx-alert infotype="notice" title="">
Windows 10 家庭版操作系统中，若没有组策略编辑器，可通过修改注册表来实现。操作步骤请参见 [检查并修改系统中的注册表](#Plan3)。
</dx-alert>


1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/330624bafb194914948c8ebd9e47334d.png" style="margin:-3px 0px;"></img>，输入 **gpedit.msc**，按 **Enter**，打开**本地组策略编辑器**。
<dx-alert infotype="explain" title="">
您也可使用 **Win+R** 快捷键打开运行界面。
</dx-alert>
3. 在左侧导航栏中，选择**计算机配置** > **管理模板** > **系统** > **凭据分配**，双击**加密 Oracle 数据库修正**。如下图所示：
![加密数据库修正](https://main.qcloudimg.com/raw/ae699fa2e997b10eab3477b6c9baf544.png)
3. 在打开的**加密 Oracle 修正**窗口中，选择**已启用**，并将**保护级别**设置为**易受攻击**。如下图所示：
![易受攻击](https://main.qcloudimg.com/raw/65135ad1ea484655953de40fa0882d06.png)
4. 单击**确定**，完成设置。


### 检查并修改系统中的注册表[](id:Plan3)

1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/330624bafb194914948c8ebd9e47334d.png" style="margin:-3px 0px;"></img>，输入 **regedit**，按 **Enter**，打开注册表编辑器。
<dx-alert infotype="explain" title="">
您也可使用 **Win+R** 快捷键打开运行界面。
</dx-alert>
2. 在左侧导航树中，依次展开**计算机** > **HKEY_LOCAL_MACHINE** > **SOFTWARE** > **Microsoft** > **Windows** > **CurrentVersion** > **Policies** > **System** > **CredSSP** > **Parameters** 目录。如下图所示：
<dx-alert infotype="explain" title="">
若该目录路径不存在，请手动创建。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/fa4c9fecefb5fc42b9055f7e6d7d36d7.png"/>
4. 右键单击 **Parameters**，选择**新建** > **DWORD(32位)值**，并将文件名称命名为 **AllowEncryptionOracle**。
5. 双击新建的 **AllowEncryptionOracle** 文件，将**数值数据**设置为**2**，单击**确定**。如下图所示：
![AllowEncryptionOracle](https://main.qcloudimg.com/raw/2355ea7ef57d01075da6d54987b6f498.png)
6. 重启实例。

## 相关参考

- [CVE-2018-0886 | CredSSP 远程执行代码漏洞](https://portal.msrc.microsoft.com/zh-cn/security-guidance/advisory/CVE-2018-0886)
- [CVE-2018-0886 的 CredSSP 更新](https://support.microsoft.com/zh-cn/help/4093492/credssp-updates-for-cve-2018-0886-march-13-2018)


