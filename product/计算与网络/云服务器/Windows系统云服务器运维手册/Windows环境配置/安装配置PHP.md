本文档介绍 Windows 云服务器的 PHP 配置。介绍 [PHP 5.3之后版本安装](#jump) 与 [PHP 5.3 及之前版本安装](#jump1) ，您可以根据需求查看相关内容。
## 前提条件
在Windows 云服务器中进行 PHP 配置，需要完成 IIS 角色的添加和安装，详细请见文档 [安装配置 IIS](
//www.qcloud.com/document/product/213/10180?!preview&lang=cn) 。

## PHP 5.3 之后版本安装
<span id="jump">  </span>
PHP 5.3版本后取消了安装包模式，仅通过zip文件和debug pack两种方式进行安装。本例使用 Windows Server 2012 R2 环境下 zip 安装进行示例。

### 软件下载

 1. 在云服务器中下载 PHP zip 安装包（下载地址： http://windows.php.net/download/ ）。
>注意:
>在 IIS 下运行时必须选择 <font color="red">Non Thread Safe(NTS) 的 x86 包。</font>（若一定要在 Windows Server 32bit（x64）下，PHP 选择 x64，则不能选择 IIS，此时可使用 Apache 作为代替选项）

	选择类似如下的安装包：
	![](//mccdn.qcloud.com/static/img/46ba4886a15ee851797ec5aa92743558/image.png)
	![](//mccdn.qcloud.com/static/img/fb42955a0dbbdaf95d73469b845e4f97/image.png)
	![](//mccdn.qcloud.com/static/img/8bc781ab6611058af2b3298682481447/image.png)

 2. PHP 5.3 以上版本的安装依赖于 Visual C++ Redistributable Update 。请根据下载的 PHP 安装包名，参考如下表格所示的对应关系下载并安装 VC Update 安装程序：

| PHP安装包名 | Visual C++ Redistributable安装包下载地址 |
|---------|---------|---------|
| php-x.x.x-nts-Win32-VC14-x86.zip | [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/zh-cn/download/details.aspx?id=48145) |
| php-x.x.x-nts-Win32-VC11-x86.zip | [Visual C++ Redistributable for Visual Studio 2012 Update 4](https://www.microsoft.com/zh-cn/download/details.aspx?id=30679) |
| php-x.x.x-nts-Win32-VC9-x86.zip | [Microsoft Visual C++ 2008 SP1 Redistributable Package (x86)](https://www.microsoft.com/zh-cn/download/details.aspx?id=5582) |

  若下载的 PHP 安装包如下图所示：
	
![](//mccdn.qcloud.com/static/img/974ac7192d8f10236fcc27bfd54b8aed/image.png)

则按表格第一行对应关系下载 VS 2015 版本的安装包，下载并安装如下.exe文件：
![](//mccdn.qcloud.com/static/img/59ccf8030333b4f0af3d8239c8cb0982/image.png)
![](//mccdn.qcloud.com/static/img/2e5c06d2803f9cf41ff3a8f40fb6ca07/image.png)
![](//mccdn.qcloud.com/static/img/b20d6d5cb0303b9b21ec6d756ec87334/image.png)

### 安装配置
 1. 将 PHP zip 安装包解压（本例解压至 ```C:\PHP```），复制```php.ini-production```并改名为```php.ini```，如下图所示：
![](//mccdn.qcloud.com/static/img/40f86bb1d7f34033df856e1859a60b5c/image.png)

 2. 单击【服务器管理器】-【IIS】，在本地 IIS 上右键点击选择 IIS 管理器：
![](//mccdn.qcloud.com/static/img/e90af15beb1048b93c85d63fced74537/image.png)

	单击左侧 主机名(IP) 来到主页，双击【处理程序映射】：
![](//mccdn.qcloud.com/static/img/b5e674a20199ef56a5edd6c560ef268f/image.png)

	单击右侧【添加模块映射】按钮，在弹出框中填写如下信息并单击【确定】按钮保存：
![](//mccdn.qcloud.com/static/img/d26799e030d5367d8a1a53ee947a876a/image.png)

	>注意：
	>若可执行文件选择不了 php-cgi.exe ，请文件后缀变为.exe：![](//mccdn.qcloud.com/static/img/2a9ed2b52046528fab7658d1af8f16b1/image.png)

 3. 单击左侧 主机名(IP) 回到主页，双击【默认文档】：
![](//mccdn.qcloud.com/static/img/69bb6ccada8f8ab7fb6051c2f24b93a3/image.png)

	单击右侧【添加】按钮，添加名称为```index.php```的默认文档：
![](//mccdn.qcloud.com/static/img/52f92443370f68a599646eb37e0166d2/image.png)

 4. 单击左侧主机名(IP)回到主页，双击【 FastCGI 设置】：
![](//mccdn.qcloud.com/static/img/0d30afcb824afad36be1daa8e4d96b63/image.png)

	单击右侧【编辑】按钮，在【监视对文件所做的更改】中选择 php.ini 路径：
![](//mccdn.qcloud.com/static/img/9560607611014fe2e5742d80826c440f/image.png)
![](//mccdn.qcloud.com/static/img/16d32356d14db239ab142bfd441ce53f/image.png)

 5. 在```C:\inetpub\wwwroot```目录下创建一个PHP文件```index.php```，写入如下内容：
```
<?php
phpinfo();
?>
```

 6. 在云服务器打开浏览器内访问```http://localhost/index.php``` ，查看环境配置是否成功。如果页面可以显示如下，说明配置成功：
![](//mccdn.qcloud.com/static/img/2c71d31eeb12d5b6434d1e3df36a213f/image.png)



## PHP 5.3 及之前版本安装
<span id="jump1">  </span>
>注意：
> http://windows.php.net/download/ 官方下载地址已不再提供 PHP 5.3及之前版本的下载，若仍需使用PHP 5.3 及之前版本，请在本地下载后上传文件至云服务器或在云服务器网络上搜索。上传文件详见 [这里](https://www.qcloud.com/document/product/213/2761) 。

 1. 在云服务器中打开 PHP 安装包。

 2. 选择Web服务(Web Server Setup)时，选择 “IIS FastCGI” ，如下图所示：
![](//mccdn.qcloud.com/img56b1bdf45ec1f.png)

 3. 按照安装界面的指引，完成PHP的安装。

 4. 在```C:/inetpub/wwwroot```目录下创建一个 PHP 文件 hello.php ，如下图所示：
![](//mccdn.qcloud.com/img56b1be32d66ec.png)

	hello.php 文件写入如下的内容：

	```
	<?php
	echo "<title>Test Page</title>";
	echo "hello world";
	?>
	```

 5. 在浏览器中访问 Windows 云服务器公网 IP ，查看环境配置是否成功。如果页面可以显示如下，说明配置成功：
	![](//mccdn.qcloud.com/img56b1be73cd4cb.png)


