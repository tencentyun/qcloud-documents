本文档介绍 Windows 云服务器的 PHP 配置。介绍 [PHP 5.3之后版本安装](#jump) 与 [PHP 5.3 及之前版本安装](#jump1) ，您可以根据需求查看相关内容。
## 前提条件
在Windows 云服务器中进行 PHP 配置，需要完成 IIS 角色的添加和安装，详细请见文档 [安装配置 IIS](
/doc/product/213/2755) 。

## PHP 5.3 之后版本安装
<span id="jump">  </span>
PHP 5.3 版本后取消了安装包模式，仅通过 zip 文件和 debug pack 两种方式进行安装。本例使用 Windows Server 2012 R2 环境下 zip 安装进行示例。

### 软件下载

 1. 在云服务器中下载 PHP zip 安装包（下载地址： http://windows.php.net/download/ ）。
>注意:
>在 IIS 下运行时必须选择 Non Thread Safe(NTS) 的 x86 包。若一定要在 Windows Server 32bit (x64) 下，PHP 选择 x64，则不能选择 IIS，此时可使用 Apache 作为代替选项。

	选择类似如下的安装包：
  ![](//mc.qcloudimg.com/static/img/d02eb264ae4d5fbaaf8fd01a08433c61/image.png)
  ![](//mc.qcloudimg.com/static/img/f719e6893f1addd0b260d0c740e4e0ba/image.png)
  ![](//mc.qcloudimg.com/static/img/24ca3df57de6195ad45adabad1c5dc13/image.png)

 2. PHP 5.3 以上版本的安装依赖于 Visual C++ Redistributable Update 。请根据下载的 PHP 安装包名，参考如下表格所示的对应关系下载并安装 VC Update 安装程序：

| PHP安装包名 | Visual C++ Redistributable安装包下载地址 |
|---------|---------|---------|
| php-x.x.x-nts-Win32-VC14-x86.zip | [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/zh-cn/download/details.aspx?id=48145) |
| php-x.x.x-nts-Win32-VC11-x86.zip | [Visual C++ Redistributable for Visual Studio 2012 Update 4](https://www.microsoft.com/zh-cn/download/details.aspx?id=30679) |
| php-x.x.x-nts-Win32-VC9-x86.zip | [Microsoft Visual C++ 2008 SP1 Redistributable Package (x86)](https://www.microsoft.com/zh-cn/download/details.aspx?id=5582) |

  若下载的 PHP 安装包如下图所示：
![](//mccdn.qcloud.com/static/img/974ac7192d8f10236fcc27bfd54b8aed/image.png)

则按表格第一行对应关系下载 VS 2015 版本的安装包，下载并安装如下两个`.exe`格式文件：
![](//mc.qcloudimg.com/static/img/7128c0b621f2534cecddd23b6f3efdb9/image.png)


### 安装配置
 1. 将 PHP zip 安装包解压（本例解压至 `C:\PHP`），复制`php.ini-production`并改名为`php.ini`，如下图所示：
![](//mc.qcloudimg.com/static/img/1be9b1771a93852aff909b08159a5b79/image.png)

 2. 单击【服务器管理器】-【IIS】，在本地 IIS 上右键点击选择 IIS 管理器：
![](//mc.qcloudimg.com/static/img/f0387eeb456b7d60e8a5b601cbd3c6b0/image.png)

	单击左侧 主机名(IP) 来到主页，双击【处理程序映射】：
![](//mc.qcloudimg.com/static/img/898aa0d2f61c467d333601b75c57704c/image.png)

	单击右侧【添加模块映射】按钮，在弹出框中填写如下信息并单击【确定】按钮保存：
![](//mc.qcloudimg.com/static/img/6f0fd95475a7c00a5779592d15a7753e/image.png)

	>**注意：**
	>若可执行文件选择不了 `php-cgi.exe` ，请文件后缀变为.exe：![](//mc.qcloudimg.com/static/img/d749a9fe4c77f6ea7b55afd8fd37e808/image.png)

 3. 单击左侧 主机名(IP) 回到主页，双击【默认文档】：
![](//mc.qcloudimg.com/static/img/b5861a95bf6aafd8f4bcaf1c12e9f9be/image.png)

	单击右侧【添加】按钮，添加名称为`index.php`的默认文档：
![](//mc.qcloudimg.com/static/img/6b2543227fec95d1b9bed5f4260a86bb/image.png)

 4. 单击左侧主机名(IP)回到主页，双击【 FastCGI 设置】：
![](//mc.qcloudimg.com/static/img/aa23422c038b1024354f01ed0cb3ab73/image.png)

	单击右侧【编辑】按钮，在【监视对文件所做的更改】中选择 `php.ini` 路径：
![](//mc.qcloudimg.com/static/img/b4f1ec7d39519dc7d2e89d52ed8a1a87/image.png)
![](//mc.qcloudimg.com/static/img/a2acbed50587552c6ef7ed796b82eb36/image.png)

 5. 在 `C:\inetpub\wwwroot` 目录下创建一个PHP文件 `index.php` ，写入如下内容：
```
<?php
phpinfo();
?>
```

 6. 在云服务器打开浏览器内访问 `http://localhost/index.php`  ，查看环境配置是否成功。如果页面可以显示如下，说明配置成功：
![](//mc.qcloudimg.com/static/img/46eec848975e77e770569eb5d8849d37/image.png)



## PHP 5.3 及之前版本安装
<span id="jump1">  </span>
>注意：
> http://windows.php.net/download/ 官方下载地址已不再提供 PHP 5.3 及之前版本的下载，若仍需使用 PHP 5.3 及之前版本，请在本地下载后上传文件至云服务器或在云服务器网络上搜索。上传文件详见 [这里](https://cloud.tencent.com/document/product/213/2761) 。

 1. 在云服务器中打开 PHP 安装包。

 2. 选择 Web 服务 (Web Server Setup) 时，选择 “IIS FastCGI” ，如下图所示：
![](//mc.qcloudimg.com/static/img/ef2f5959779cd733934d11ecbcb4a7f5/image.png)

 3. 按照安装界面的指引，完成PHP的安装。

 4. 在`C:/inetpub/wwwroot`目录下创建一个 PHP 文件 `hello.php` ，如下图所示：
![](//mc.qcloudimg.com/static/img/31d992849b04c1bc76c0d4ca61ab8a4b/image.png)

	`hello.php` 文件写入如下的内容：

	```
	<?php
	echo "<title>Test Page</title>";
	echo "hello world";
	?>
	```

 5. 在浏览器中访问 Windows 云服务器公网 IP ，查看环境配置是否成功。如果页面可以显示如下，说明配置成功：
![](//mc.qcloudimg.com/static/img/89cebc1127f5c76790c2a9bf3be9fd1f/image.png)


