>注：请勿在Windows云服务器上安装个人PC类的杀毒软件，此类软件可能会封云服务器的远程登录端口，导致云服务器无法登录。 

## 1. 安装配置IIS
### 1.1. Windows2012R2版本示例
1) 点击Windows云服务器左下角【开始(Start)】，选择【服务器管理器(Server Manager)】，打开服务器管理界面，如下图所示：
![](//mccdn.qcloud.com/static/img/d27f493d5613aa2d87a9bbd9dba59387/image.png)

2) 选择【添加角色和功能】，在弹出的添加角色和功能向导弹出框”开始之前“中点击【下一步】按钮，在”安装类型“中选择【基于角色或基于功能的安装】，点击【下一步】按钮。
![](//mccdn.qcloud.com/static/img/36ab9d6b144c5eff7fe2b468268155f2/image.png)
![](//mccdn.qcloud.com/static/img/0375764474b419976b13b594ea328e88/image.png)
![](//mccdn.qcloud.com/static/img/b6341e1fff569f1d7fffb5b66bc14c98/image.png)

3) 窗口左侧选择”服务器角色“选项卡，勾选【Web服务器（IIS）】，在弹出框中点击【添加功能】按钮后点击【下一步】按钮。
![](//mccdn.qcloud.com/static/img/d516d053aca89ddc0a27ebe68a8f5882/image.png)
![](//mccdn.qcloud.com/static/img/702065dfb3620e7aa7e81a94ff87a79b/image.png)

4) 在”功能“选项卡中点击【下一步】按钮后，在”Web服务器角色（IIS）“选项卡也点击【下一步】。
![](//mccdn.qcloud.com/static/img/6e436524609ccd6e38b7440ebb881278/image.png)
![](//mccdn.qcloud.com/static/img/b003e403fe4e8e86bb0655199bb75a19/image.png)

5) 在”角色服务“选项卡中勾选【CGI】选项，点击下一步。
![](//mccdn.qcloud.com/static/img/d13a9e02730018041342ecafa1b471af/image.png)

6) 确认安装并等待安装完成。
![](//mccdn.qcloud.com/static/img/7e295431db7ef4a43b4136c860b32b19/image.png)

7) 安装完成后在云服务器的浏览器中访问localhost验证是否安装成功，出现以下界面即为成功安装。
![](//mccdn.qcloud.com/static/img/dfa6725c4358e1a4214dcceb03e87028/image.png)
### 1.2. Windows2008版本示例
1) 点击Windows云服务器左下角【开始(Start)】菜单中的【管理工具】中的【服务器管理器(Server Manager)】按钮，打开服务器管理界面，如下图所示：
![](//mccdn.qcloud.com/img56b1bc701ec41.png)

2) 点击“添加角色和功能Add Roles”添加服务器角色，在这里选择Web Server（IIS），如下图所示：

![](//mccdn.qcloud.com/img56b1bb12831b3.png)
![](//mccdn.qcloud.com/img56b1bcee2d9e8.png)

3) 点击【下一步】，在选择角色服务时，勾选“CGI”，如下图所示：

![](//mccdn.qcloud.com/img56b1bd1b8f220.png)

4) 设置完成后，点击【安装(install)】，进行安装：

![](//mccdn.qcloud.com/img56b1bd4f18f1a.png)

5) 浏览器访问Windows云服务器公网IP查看IIS服务是否正常运行。如果显示如下，说明IIS安装配置成功。

![](//mccdn.qcloud.com/img56b1bd7c5b0be.png)

## 2. 安装配置PHP
### 2.1. PHP 5.3及之前版本安装
1) 下载PHP安装包（下载地址： http://windows.php.net/download/ ），选择如下图对应的安装包：

![](//mccdn.qcloud.com/img56b1bdc4dbec6.png)


2) 下载完成后，安装PHP，需要选择Web服务时，选择“IIS FastCGI”，如下图所示：

![](//mccdn.qcloud.com/img56b1bdf45ec1f.png)

3) 按照安装界面的指引，完成PHP的安装。

4) 在C:/inetpub/wwwroot目录下创建一个PHP文件hello.php，如下图所示：
![](//mccdn.qcloud.com/img56b1be32d66ec.png)

hello.php文件写入如下的内容：

```
<?php
echo "<title>Test Page</title>";
echo "hello world";
?>
```

在浏览器中访问Windows云服务器公网IP查看环境配置是否成功。如果页面可以显示如下，说明配置成功：
![](//mccdn.qcloud.com/img56b1be73cd4cb.png)

### 2.2. PHP 5.3之后版本安装
PHP 5.3版本后取消了安装包(installer)模式，仅通过zip文件和debug pack两种方式进行安装。本例使用Windows Server 2012R2 环境下zip安装进行示例。

1) 下载PHP zip安装包，请注意在IIS下运行时必须选择<font color="red">Non Thread Safe(NTS)的x86包。</font>（若一定要在Windows Server 32bit（x64）下，PHP选择x64，则不能选择IIS，此时可使用Apache作为代替选项）

选择类似如下的安装包：

![](//mccdn.qcloud.com/static/img/46ba4886a15ee851797ec5aa92743558/image.png)
![](//mccdn.qcloud.com/static/img/fb42955a0dbbdaf95d73469b845e4f97/image.png)
![](//mccdn.qcloud.com/static/img/8bc781ab6611058af2b3298682481447/image.png)

2) PHP5.3以上版本的安装依赖于Visual C++ Redistributable Update。请根据下载的PHP安装包名，参考如下表格所示的对应关系下载并安装VC Update安装程序：

| PHP安装包名 | Visual C++ Redistributable安装包下载地址 |
|---------|---------|---------|
| php-x.x.x-nts-Win32-VC14-x86.zip | [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/zh-cn/download/details.aspx?id=48145) |
| php-x.x.x-nts-Win32-VC11-x86.zip | [Visual C++ Redistributable for Visual Studio 2012 Update 4](https://www.microsoft.com/zh-cn/download/details.aspx?id=30679) |
| php-x.x.x-nts-Win32-VC9-x86.zip | [Microsoft Visual C++ 2008 SP1 Redistributable Package (x86)](https://www.microsoft.com/zh-cn/download/details.aspx?id=5582) |

比如，下载的PHP安装包如下图所示：
![](//mccdn.qcloud.com/static/img/974ac7192d8f10236fcc27bfd54b8aed/image.png)

则按第一行对应关系下载VS2015版本的安装包，下载并安装如下.exe文件：
![](//mccdn.qcloud.com/static/img/59ccf8030333b4f0af3d8239c8cb0982/image.png)
![](//mccdn.qcloud.com/static/img/2e5c06d2803f9cf41ff3a8f40fb6ca07/image.png)
![](//mccdn.qcloud.com/static/img/b20d6d5cb0303b9b21ec6d756ec87334/image.png)

3) 将PHP zip安装包解压（本例解压至C:\PHP），复制php.ini-production并改名为php.ini，如下图所示：
![](//mccdn.qcloud.com/static/img/40f86bb1d7f34033df856e1859a60b5c/image.png)

4) 点击【服务器管理器】-【IIS】，在本地IIS上右键点击选择IIS管理器：
![](//mccdn.qcloud.com/static/img/e90af15beb1048b93c85d63fced74537/image.png)

点击左侧主机名(IP)来到主页，双击【处理程序映射】：
![](//mccdn.qcloud.com/static/img/b5e674a20199ef56a5edd6c560ef268f/image.png)

点击右侧【添加模块映射】按钮，在弹出框中填写如下信息并点击【确定】按钮保存：
![](//mccdn.qcloud.com/static/img/d26799e030d5367d8a1a53ee947a876a/image.png)

若可执行文件选择不了php-cgi.exe，请注意将选择文件处的文件后缀变为.exe：
![](//mccdn.qcloud.com/static/img/2a9ed2b52046528fab7658d1af8f16b1/image.png)

5) 点击左侧主机名(IP)回到主页，双击【默认文档】：
![](//mccdn.qcloud.com/static/img/69bb6ccada8f8ab7fb6051c2f24b93a3/image.png)

点击右侧【添加】按钮，添加名称为index.php的默认文档：
![](//mccdn.qcloud.com/static/img/52f92443370f68a599646eb37e0166d2/image.png)

6) 点击左侧主机名(IP)回到主页，双击【FastCGI设置】：
![](//mccdn.qcloud.com/static/img/0d30afcb824afad36be1daa8e4d96b63/image.png)

选中路径点击右侧【编辑】按钮，在【监视对文件所做的更改】中选择php.ini路径：
![](//mccdn.qcloud.com/static/img/9560607611014fe2e5742d80826c440f/image.png)
![](//mccdn.qcloud.com/static/img/16d32356d14db239ab142bfd441ce53f/image.png)

6) 在C:\inetpub\wwwroot目录下创建一个PHP文件index.php，写入如下内容：

```
<?php

phpinfo();

?>
```

保存，在云服务器内访问http://localhost/index.php ，可验证PHP是否安装成功：
![](//mccdn.qcloud.com/static/img/2c71d31eeb12d5b6434d1e3df36a213f/image.png)


