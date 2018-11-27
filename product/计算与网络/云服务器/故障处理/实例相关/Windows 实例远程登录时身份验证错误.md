
### 问题描述
通过远程桌面连接登录Windows实例时，出现“发生身份验证错误，给函数提供标志无效”或“发生身份验证错误。要求的函数不受支持”的报错，如下图。
![给函数提供标志无效](https://main.qcloudimg.com/raw/0c5e6df33c7de426b8e6f3a30df1e4ab.png)
![要求函数不支持](https://main.qcloudimg.com/raw/4cc667df3c13b6a255fa8be5c81c08a9.png)

### 问题分析
此问题是由于微软于2018年3月发布了一个安全更新，此更新通过更正凭据安全支持提供程序协议 (CredSSP) 在身份验证过程中验证请求的方式来修复CredSSP存在的远程执行代码漏洞。客户端和服务器都需要安装此更新，否则可能出现如问题描述中的远程桌面连接不上的情况。
![客户端服务器匹配情况](https://main.qcloudimg.com/raw/2734e664e7d72b083c37db3a4dc13647.png)
如上图说明，下述三种情况会引起远程连接失败：
情况一：客户端未修补，服务器安装了安全更新，并且策略配置为“强制更新的客户端”。
情况二：服务器未修补，客户端安装了安全更新，并且策略配置为“强制更新的客户端”。
情况三：服务器未修补，客户端安装了安全更新，并且策略配置为“缓解”。


### 解决方案
####方案一：安装安全更新（推荐）
更新未修补的客户端/服务器端，安装安全更新。不同系统对应的更新情况详见[CVE-2018-0886 | CredSSP 远程执行代码漏洞](https://portal.msrc.microsoft.com/zh-cn/security-guidance/advisory/CVE-2018-0886)。
下面详细描述服务器端（即CVM实例）进行系统更新的步骤。客户端本地的升级操作跳过VNC登录步骤从第四步开始进行即可。下面操作步骤以Windows server2016为例子。
>注意：
各操作系统进入【Windows 更新】的方法有所不同
Windows Server2012：【开始】- 【控制面板】-【系统与安全】-【Windows 更新】
Windows Server2008：【开始】- 【控制面板】-【系统与安全】-【Windows Update】
Windows10:【开始】- 【设置】-【更新与安全】
Windows7：【开始】- 【控制面板】-【系统与安全】-【Windows Update】

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，进入云主机列表页。找到目标CVM实例，点击右侧的【登录】。
![云服务器列表页](https://main.qcloudimg.com/raw/8d127ca9ff816a3ea9cf33ce8e22bf06.png)
2. 在打开的登录云服务器弹窗中，选择底部的浏览器 VNC 方式登录，点击【立即登录】。
![VNC登录入口](https://main.qcloudimg.com/raw/d5c60ee94292b84259d77208f710dc6a.png)
3. 通过在左上角单击 Ctrl-Alt-Delete 命令进入系统登录界面
![Ctrl-Alt-Delete](https://main.qcloudimg.com/raw/3ab6adc86ced2f4f7b04041af458e1c0.png)
4. 【开始】- 【设置】-【更新与安全】
![开始设置](https://main.qcloudimg.com/raw/5f93445e20f6df2b98eef4b5de9278b5.png)
![更新与安全](https://main.qcloudimg.com/raw/583bea7b453a64f704944437369ef998.png)
5. 点击【检查更新】
![检查更新](	https://main.qcloudimg.com/raw/85da2a1bf567f6518b4423ae5766c4d1.png)
6. 点击【开始安装】，等待安装完成，重启实例完成更新。
![开始安装]()


####方案二：修改策略配置
此方法通过设置已经安装安全更新的机器的【加密Oracle修正】的策略为“易受攻击”解决。
>注意：
Windows10家庭版的用户，因为系统中没有组策略编辑器，需要修改注册表来实现，请参照方案三。

1. 【开始】-【运行】，或者直接使用快捷键Win+R，打开运行界面，输入gpedit.msc，回车打开本地组策略略编辑器。
![gpedit.msc](	https://main.qcloudimg.com/raw/26f0b7056cd3949cdd42da2c5c7ac58a.png)
2. 【计算机配置】- 【管理模板】-【系统】-【凭据分配】-【加密Oracle修正】
![加密Oracle修正](https://main.qcloudimg.com/raw/5246b0a6cc5d487f62805a1002f76bd2.png)
3. 选择“已启用”，保护级别选择“易受攻击”。
![易受攻击](https://main.qcloudimg.com/raw/cd2e0719aa2aa3a406b01ab336d54b68.png)
4. 点击“应用”，完成设置。

####方案三：修改注册表
1. 【开始】-【运行】，或者直接使用快捷键Win+R，打开运行界面，输入regedit，回车打开注册表编辑器。
![注册表编辑器](https://main.qcloudimg.com/raw/fcc5dc10101186638e2f10478d865a17.png)
2. 依次打开下述文件夹路径：HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters。如果对应文件夹不存在，则手动新建。一般系统下，先新建项“CredSSP”，然后在CredSSP下新建项“Parameters”。
![Parameters](https://main.qcloudimg.com/raw/30fa16a849a9d2d103c94536577e210c.png)
3. 然后在“Parameters”下新建DWORD(32位)，名称为“AllowEncryptionOracle”，设置值为“2”。
![AllowEncryptionOracle](https://main.qcloudimg.com/raw/91b8d8d95f51feb87a9b6f50c187e159.png)
4. 重启本地计算机。


### 相关文档
[CVE-2018-0886 | CredSSP 远程执行代码漏洞](https://portal.msrc.microsoft.com/zh-cn/security-guidance/advisory/CVE-2018-0886)
[CVE-2018-0886 的 CredSSP 更新](https://support.microsoft.com/zh-cn/help/4093492/credssp-updates-for-cve-2018-0886-march-13-2018)