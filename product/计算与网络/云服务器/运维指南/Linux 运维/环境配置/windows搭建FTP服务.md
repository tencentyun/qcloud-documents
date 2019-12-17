## 操作场景
本文档介绍如何在 Windows 操作系统的腾讯云服务器（CVM）上通过 IIS 搭建 FTP 站点。

## 示例软件版本
本文搭建 FTP 服务组成版本如下：
 - Windows 操作系统，本文以 Windows Server 2012 为例。
 - IIS：Web 服务器，本文以 IIS 8.5 为例。

## 操作步骤
### 步骤1：登录云服务器
[使用 RDP 文件登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)。
您也可以根据实际操作习惯，[使用远程桌面连接登录 Windows 实例](https://cloud.tencent.com/document/product/213/35703)。

### 步骤2：在 IIS 上安装 FTP 服务
1. 在“服务器管理器”界面中选择【添加角色与功能】。如下图所示：
![](https://main.qcloudimg.com/raw/5c7fa77df47fb39bafb9c6f39f4b1007.png)
2. 在弹出的“添加角色和功能向导”窗口中，单击【下一步】进入“选择安装类型”页面。
3. 在“选择安装类型”页面中，选择【基于角色或基于功能的安装】并单击【下一步】。
4. 在“选择目标服务器”页面中，保持默认选择并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/beec7ae5fcbdf3e413f133296e53f2df.png)
5. 在“选择服务器角色”页面中，勾选【Web 服务器(IIS)】，在弹出的窗口中单击【添加功能】，并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/f160096425be05330fc7bc39e3d81b22.png)
6. 连续单击【下一步】，进入“选择角色服务”页面。
7. 在“选择角色服务页面”，勾选【FTP 服务】及【FTP 扩展】并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/e8efaf069e2f2d2a2e632d0f2eeec4a4.png)
8. 单击【安装】，开始安装 FTP 服务。
9. 安装完成后，单击【关闭】。

### 步骤3：创建 FTP 用户名及密码
>?请按照以下步骤配置 FTP 用户名及密码，若您需使用匿名用户访问 FTP 服务，可跳过此步骤。
>
1. 在“服务器管理器”界面中，选择右上角导航栏中的【工具】>【计算机管理】。
2. 在“计算机管理”界面中，选择左侧导航栏中的【本地用户和组】>【用户】。
3. 在右侧空白处单击鼠标右键，选择【新用户】。如下图所示：
![](https://main.qcloudimg.com/raw/e59109c2d3e2bed1c05bfb6983975622.png)
4. 在“新用户”界面，按照以下提示设置用户名及密码。如下图所示：
![](https://main.qcloudimg.com/raw/5727d1a8f33bd35df02e1ec58447f23f.png)
  1. 输入用户名，本文以 `ftpuser` 为例。
  2. 输入密码，并确认密码。
密码需同时包含大写、小写字母及数字，否则不满足密码策略要求。
  3. 取消勾选【用户下次登录时须更改密码】。
  4. 勾选【密码永不过期】。
  5. 单击【创建】即可成功创建新用户。
  6. 单击【关闭】，关闭“新用户”窗口后即可在列表中查看已创建的 `ftpuser` 用户。
	
### 步骤4：设置共享文件夹权限
>?需要为 FTP 站点设置共享文件夹，本为以 `C:\test` 文件夹为例，文件夹中已包含需共享的文件 `test.txt`。
>
1. 单击云服务器界面底部任务栏中的<img src="https://main.qcloudimg.com/raw/863967bab67b6cd83ce5f0924e1b19c8.png" style="margin:-3px 0px">，进入“这台电脑”页面。
2. 进入 C 盘，选择 `test` 文件夹并单击鼠标右键，选择【属性】。
3. 在“test 属性”界面中，选择【安全】标签并单击【编辑】。如下图所示：
![](https://main.qcloudimg.com/raw/1792e5b5ff508f809091e786c229893c.png)
4. 在“test 权限”界面中，单击【添加】。
5. 在“选择用户或组”界面中，单击【高级】。
6. 在弹出的“选择用户或组”界面中，选择【立即查找】。
7. 在搜索结果中，选择 `Everyone` 并单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/3abc835b93387ef1571db5e8eea010b5.png)
8. 在“选择用户或组”界面中，单击【确定】确认添加。如下图所示：
![](https://main.qcloudimg.com/raw/6f94c003d1660597adf67cc640617407.png)
9. 在“test 的权限”界面中，勾选【完全控制】及【修改】并单击【确定】设置权限。如下图所示：
![](https://main.qcloudimg.com/raw/b32a89aee8af67bea1ad69b8838521d9.png)
10. 在“test 属性”界面中，单击【确定】完成设置。

### 步骤5：添加 FTP 站点
1. 在“服务器管理器”界面中，选择右上角导航栏中的【工具】>【Internet Information Services (IIS)管理器 】。
2. 找到【网站】并单击鼠标右键，选择【添加 FTP 站点】。如下图所示：
![](https://main.qcloudimg.com/raw/bfa4fa842a840f0f374a50de828a4615.png)
3. 在弹出的“添加 FTP 站点”窗口中，按照以下步骤设置 FTP 站点信息：
  1. 在“站点信息”界面中，填写 FTP 站点名称，本文以 `ftp` 为例。
      物理路径请选择已设置权限的共享文件，本文以 `C:\test` 为例。如下图所示：
![](https://main.qcloudimg.com/raw/21dee4172724d828f7b326f1376eae8b.png)
   2. 单击【下一步】，进入“绑定和 SSL 设置”界面。
   3. 在“绑定和 SSL 设置”界面中，绑定设置保持默认值。
   4. SSL 请按需选择，本为以【无 SSL】为例。如下图所示：
   当 SSL 选择【允许 SSL】和【需要 SSL】时，需要选择 SSL 证书。您可选择已有的 SSL 证书，也可参考 [服务器证书制作]() 步骤制作一个 SSL 证书。
	 
