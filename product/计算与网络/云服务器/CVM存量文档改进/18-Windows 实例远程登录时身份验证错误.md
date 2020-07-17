## 故障现象

通过远程桌面连接登录 Windows 实例时，出现 “**发生身份验证错误，给函数提供标志无效**” 或 “**发生身份验证错误。要求的函数不受支持**” 的报错，如下图所示：
![给函数提供标志无效](https://main.qcloudimg.com/raw/cbb3b5ea89ed9d3a65af8b303880b7c8.png)
![要求函数不支持](https://main.qcloudimg.com/raw/09ff95a4f2e46e93a75d0e6ec38c1954.png)

## 问题分析

由于微软于2018年3月发布了一个安全更新，此更新通过更正凭据安全支持提供程序协议（CredSSP）在身份验证过程中验证请求的方式来修复 CredSSP 存在的远程执行代码漏洞。
**客户端和服务器都需要安装此更新，否则可能出现问题描述中的情况**。
![客户端服务器匹配情况](https://main.qcloudimg.com/raw/2734e664e7d72b083c37db3a4dc13647.png)
如上图所示，以下三种情况会引起远程连接失败：
- 情况一：客户端未修补，服务器安装了安全更新，并且策略配置为 “强制更新的客户端”。
- 情况二：服务器未修补，客户端安装了安全更新，并且策略配置为 “强制更新的客户端”。
- 情况三：服务器未修补，客户端安装了安全更新，并且策略配置为 “缓解”。


## 解决方案

### 方案一：客户端和服务器端均安装安全更新（推荐）

安装安全更新，更新未修补的客户端/服务器端。不同系统对应的更新情况可参见 [CVE-2018-0886 | CredSSP 远程执行代码漏洞](https://portal.msrc.microsoft.com/zh-cn/security-guidance/advisory/CVE-2018-0886)。
>! 各操作系统进入【Windows 更新】的方法有所不同。本方案以 Windows server 2016 为例。
> - Windows Server 2012：【开始】- 【控制面板】-【系统与安全】-【Windows 更新】
> - Windows Server 2008：【开始】- 【控制面板】-【系统与安全】-【Windows Update】
> - Windows10：【开始】- 【设置】-【更新与安全】
> - Windows 7：【开始】- 【控制面板】-【系统与安全】-【Windows Update】

服务器端（即 CVM 实例）进行系统更新的操作步骤如下：
>? 客户端本地的升级操作，请直接执行 [步骤5](#step5)。

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在 “云服务器” 页面中，找到目标 CVM 实例，单击【登录】。如下图所示：
![云服务器列表页](https://main.qcloudimg.com/raw/56596196a93181ac4c9467abe19c383a.png)
3. 在弹出的 “登录Windows云服务器” 窗口中，选择 “浏览器 VNC 方式登录”，单击【立即登录】。如下图所示：
![VNC登录入口](https://main.qcloudimg.com/raw/80b613a90328bb34a006d5988dcff18b.png)
4. 在弹出的登录窗口中，选择左上角的 “发送远程命令”，单击 **Ctrl-Alt-Delete** 进入系统登录界面。如下图所示：
![Ctrl-Alt-Delete](https://main.qcloudimg.com/raw/27daf8cc33746b195c74dfb5066addee.png)
<span id="step5"></span>
5. 在操作系统界面，选择【开始】> 【设置】。如下图所示：
<img src="https://main.qcloudimg.com/raw/50ff10420a966a5baca6f24344fac7ac.png"  width="500" height="400" />

6. 在弹出的 “设置” 窗口中，选择【更新与安全】。如下图所示：
<img src="https://main.qcloudimg.com/raw/fc366907a454ca9eb484097241fb5d59.png"  width="420" height="400" />

7. 在 “更新和安全” 中，选择 “Windows 更新”，单击【检查更新】。如下图所示：
![检查更新](https://main.qcloudimg.com/raw/b687c689b78124df4c26a11050da6ad4.png)
8. 根据界面提示，单击【开始安装】。
9. 安装完成后，重启实例，完成更新。

### 方案二：修改策略配置

在已安装安全更新的机器中，将【加密 Oracle 修正】策略设置为 “易受攻击” 。
操作步骤如下：
>! Windows 10 家庭版操作系统中，没有组策略编辑器，可通过修改注册表来实现。操作步骤请参见 [方案三](#Plan3)。

1. 在操作系统界面，选择【开始】>【运行】，输入 **gpedit.msc**。如下图所示：
>? 也可使用 “Win+R” 快捷键打开运行界面。
 
 ![gpedit.msc](https://main.qcloudimg.com/raw/9a0bed85a419457263f975c7c03f108d.png)
2. 按 **Enter**，打开本地组策略略编辑器。
3. 在左侧导航树中，选择【计算机配置】>【管理模板】>【系统】>【凭据分配】，双击【Endcryption Oracle Remediation】。如下图所示：
![加密Oracle修正](https://main.qcloudimg.com/raw/bf26bc8269f9ca350bd5d3d13fa65de4.png)
3. 在 “Endcryption Oracle Remediation” 窗口中，选择 “已启用”，并将 “Protection Level” 设置为 “Vulnerable”。如下图所示：
![易受攻击](https://main.qcloudimg.com/raw/d097fc88a5b554197f803c1323dd008a.png)
4. 单击【确定】，完成设置。

<span id="Plan3"></span>
### 方案三：修改注册表

1. 在操作系统界面，选择【开始】>【运行】，输入 **regedit**。如下图所示：
>? 也可使用 “Win+R” 快捷键打开运行界面。 

 ![注册表编辑器](https://main.qcloudimg.com/raw/49391d1423537fcd6f54c4e763d5f616.png)
2. 按 **Enter**，打开注册表编辑器。
3. 在左侧导航树中，选择 “计算机 > HKEY_LOCAL_MACHINE > SOFTWARE > Microsoft > Windows > CurrentVersion > Policies > System > CredSSP > Parameters”。如下图所示：
>? 若该文件夹路径不存在，请手动创建。

 ![Parameters](https://main.qcloudimg.com/raw/9b3cfbb05ba279aed2bb0172e1c98254.png)
4. 右键单击 “Parameters”，选择【新建】>【DWORD(32位)】，并将文件名称命名为 “AllowEncryptionOracle”。
5. 双击新建的 “AllowEncryptionOracle” 文件，将 “数值数据” 设置为 “2”，单击【确定】。如下图所示：
![AllowEncryptionOracle](https://main.qcloudimg.com/raw/91b8d8d95f51feb87a9b6f50c187e159.png)
6. 重启本地计算机。

## 相关文档
[CVE-2018-0886 | CredSSP 远程执行代码漏洞](https://portal.msrc.microsoft.com/zh-cn/security-guidance/advisory/CVE-2018-0886)
[CVE-2018-0886 的 CredSSP 更新](https://support.microsoft.com/zh-cn/help/4093492/credssp-updates-for-cve-2018-0886-march-13-2018)
