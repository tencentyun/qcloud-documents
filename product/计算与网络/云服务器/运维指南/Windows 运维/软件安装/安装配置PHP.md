## 操作场景

本文档以 Windows Server 2012 R2 操作系统云服务器为例，介绍在 Windows 云服务器中配置 PHP 5.3 及之前版本与 PHP 5.3 之后版本的 PHP。


## 前提条件

- 已登录 Windows 云服务器，并已在该云服务器中完成 IIS 角色的添加和安装。详情请参见 [安装 IIS 服务](https://cloud.tencent.com/document/product/213/2755)。
- 已获取 Windows 云服务器的公网 IP。详情请参见 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940)。

## 操作步骤


### PHP 5.3 及之前版本安装[](id:jump1)

<dx-alert infotype="notice" title="">
[PHP 官网](http://windows.php.net/download/) 已不再提供 PHP 5.2 之前版本的安装包下载，若仍需使用 PHP 5.2 之前版本，可在云服务器中自行搜索和下载。也可在本地自行下载，再将其安装包上传至云服务器中。如何将文件上传到 Windows 云服务器，请参考 [上传文件到 Windows 云服务器](https://cloud.tencent.com/document/product/213/2761)。以下操作步骤以 PHP 5.2.13 版本为例。
</dx-alert>


1. 在云服务器中，双击 `php-xxxxx.msi` 打开 PHP 安装包。
2. 按照安装界面的指引，单击 **Next**。
3. 在 “Web Server Setup” 界面，选择 **IIS FastCGI**，单击 **Next**。如下图所示：
![](https://main.qcloudimg.com/raw/c5fc89547b020e6ec943732d16186a7b.png)
4. 按照安装界面的指引，完成 PHP 的安装。
4. 在 `C:/inetpub/wwwroot` 目录下，创建一个 PHP 文件。例如创建一个 `hello.php` 文件，如下图所示：
![](https://main.qcloudimg.com/raw/bd064531274bf38dc1ddaa1ec3f27a61.png)
5. 在新创建的 `hello.php` 文件中，填写以下内容并保存。
```
<?php
echo "<title>Test Page</title>";
echo "hello world";
?>
```
6. 在操作系统界面，打开浏览器并访问 `http://Windows云服务器的公网IP/hello.php`，查看环境配置是否成功。
如果打开的页面如下所示，则表示配置成功：
![](https://main.qcloudimg.com/raw/0cdefc8707c4402e9ae5f9e6fa523ae1.png)


### PHP 5.3 之后版本安装[](id:jump)

PHP 5.3 版本后取消了安装包模式，仅通过 zip 文件和 debug pack 两种方式进行安装。以下操作以使用 zip 文件方式在 Windows Server 2012 R2 环境下安装 PHP 为例。

#### 软件下载

1. 在云服务器中，访问 [PHP 官网](http://windows.php.net/download/)，下载 PHP zip 安装包。如下图所示：
<dx-alert infotype="notice" title="">
- 如果您的服务器是 Windows Server 64bit (x64) 操作系统，则在 IIS 下运行 PHP 时，需选择 Non Thread Safe 版本的 x86 安装包。
- 如果您的服务器是 Windows Server 32bit (x86) 操作系统，则需要将 IIS 替换成 Apache，并选择 Thread Safe 版本的 x86 安装包。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/b54dcb237ae24673cd592561ffc91bc0.png"/>
2.  根据下载的 PHP 安装包名称，下载并安装 Visual C++ Redistributable 安装包。
PHP 安装包对应需下载和安装的 Visual C++ Redistributable 安装包如下表所示：
<table>
<tr><th>PHP 安装包名</th><th>Visual C++ Redistributable 安装包下载地址</th></tr>
<tr><td>php-x.x.x-nts-Win32-VC16-x86.zip</td><td><a href="https://visualstudio.microsoft.com/zh-hans/downloads/">Microsoft Visual C++ Redistributable for Visual Studio 2019</a> x86版本</td></tr>
<tr><td>php-x.x.x-nts-Win32-VC15-x86.zip</td><td><a href="https://visualstudio.microsoft.com/zh-hans/vs/older-downloads/">Microsoft Visual C++ Redistributable for Visual Studio 2017</a> x86版本</td></tr>
<tr><td>php-x.x.x-nts-Win32-VC14-x86.zip</td><td><a href="https://www.microsoft.com/zh-cn/download/details.aspx?id=48145">Microsoft Visual C++ Redistributable for Visual Studio 2015</a> x86版本</td></tr>
</table>
 例如，下载的 PHP 安装包名称为 <code>PHP-7.1.30-nts-Win32-VC14-x86.zip</code>，则需下载和安装 Microsoft Visual C++ Redistributable for Visual Studio 2015 x86版本的安装包。

#### 安装配置
1. 将已下载的 PHP zip 安装包解压缩。例如，解压缩至 `C:\PHP` 目录下。
2. 复制 `C:\PHP` 目录下的 `php.ini-production` 文件，并将该文件的后缀修改为 `.ini`（即重命名为`php.ini`文件）。如下图所示：
![](https://main.qcloudimg.com/raw/ba62cb859993ee25f372bc4ea969b4cf.png)
3. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f779581f1ce3edfead8c725ce1504009.png" style="margin: -3px 0px"></img>，打开服务器管理器。
4. 在服务器管理器的左侧导航栏中，单击 **IIS**。
5. 在右侧 IIS 管理窗口中，右键单击**服务器**栏中的服务器名称，选择 **Internet Information Sevices (IIS)管理器**。如下图所示：
![](https://main.qcloudimg.com/raw/e10681a1bee2850f0f9e31832cc9be65.png)
6. 在打开的 “Internet Information Sevices (IIS)管理器” 窗口中，单击左侧导航栏的服务器名称，进入服务器的主页。如下图所示：
例如，单击 10_141_9_72 服务器名称，进入 10_141_9_72 主页。
![](https://main.qcloudimg.com/raw/249468f27268512b8766df5f00d4ae24.png)
7. 在**10_141_9_72 主页**中，双击**处理程序映射**，进入 “处理程序映射” 管理界面。如下图所示：
![](https://main.qcloudimg.com/raw/9daf2155892a72526ecada93b03018a7.png)
8. 在右侧的**操作**栏中，单击**添加模块映射**，打开 “添加模块映射” 窗口。
9. 在打开的 “添加模块映射” 窗口中，填写以下信息，并单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/ec6ded20a961ff3acaf955221a1a68a4.png)
主要的参数信息如下：
 - 请求路径：填写 `*.php`。
 - 模块：选择 “FastCgiModule”。
 - 可执行文件：选择 PHP zip 安装包中的 php-cgi.exe 文件，即 `C:\PHP\php-cgi.exe`。
 - 名称：自定义，例如输入 FastCGI。
10.  在弹出的提示框中，单击**是**。 
11.  单击左侧导航栏的 10_141_9_72 服务器名称，返回 10_141_9_72 主页。
12.  在**10_141_9_72 主页**中，双击**默认文档**，进入 “默认文档” 管理界面。如下图所示：
![](https://main.qcloudimg.com/raw/bb5924fa455f89bb83f66a115dcd2f7b.png)
13.  在右侧的**操作**栏中，单击**添加**，打开 “添加默认文档” 窗口。
14.  在打开的 “添加默认文档” 窗口中，将**名称**填写为 `index.php`，单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/e8f4aeea428c8adee1573b2df30c5355.png)
15.  单击左侧导航栏的 10_141_9_72 服务器名称，返回 10_141_9_72 主页。
16.  在**10_141_9_72 主页**中，双击 **FastCGI 设置**，进入 “FastCGI 设置” 管理界面。如下图所示：
![](https://main.qcloudimg.com/raw/82a739a387fd82fb392b56595316c299.png)
17.  在 “FastCGI 设置” 管理界面，选择 FastCGI 应用程序，单击**编辑**。如下图所示：
![](https://main.qcloudimg.com/raw/9c1382da5600121741ecfa4560623997.png)
18.  在打开的 “编辑  FastCGI 应用程序” 窗口中，将**监视对文件所做的更改**设置为 `php.ini` 文件的路径。如下图所示：
![](https://main.qcloudimg.com/raw/c167f15bb6cabe35cce2650133ac63e2.png)
19. 在 `C:\inetpub\wwwroot` 目录下，创建一个 PHP 文件。例如创建一个 `index.php` 文件。
20. 在新创建的 `index.php` 文件中，填写以下内容并保存。
```
<?php
phpinfo();
?>
```
21. 在操作系统界面，打开浏览器并访问 `http://localhost/index.php`，查看环境配置是否成功。
如果打开的页面如下显示，则表示配置成功：
![](https://main.qcloudimg.com/raw/ccd08fd9af6afe4ee2c3bf38f9e581b9.png)

