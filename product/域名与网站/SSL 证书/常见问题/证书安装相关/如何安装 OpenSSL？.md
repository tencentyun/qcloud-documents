### 如何安装 OpenSSL？
OpenSSL 是用于安全通信的著名开源密码学工具包，包括主要的密码算法、常见密码和证书封装功能。

####  OpenSSL 官网

官方下载地址： [请单击此处](https://www.openssl.org/source/)。

####  Windows 安装方法

OpenSSL 官网没有提供 Windows 版本的安装包，可以选择其他开源平台提供的工具。[请单击此处](http://slproweb.com/products/Win32OpenSSL.html )， 
以该工具为例，安装步骤和使用方法如下：
1. 选择32位或者64位合适的版本下载，例如 `Win64OpenSSL_Light-1_0_2h.exe`。如下图所示：
![](https://main.qcloudimg.com/raw/d37d791cf12c0b42dddcc53a691a86d9.png)
2. 设置环境变量，例如，工具安装在 `C:\OpenSSL-Win64`，则将 `C:\OpenSSL-Win64\bin；` 复制到 Path 中。如下图所示：
![](https://main.qcloudimg.com/raw/6a2dcfbb42faab01e62fbb241e0439dc.png)
3. 打开命令行程序 cmd（以管理员身份运行），进入 `2_www.tencent.com.key`、`1_www.tencent.com_cert.crt` 文件所在目录，运行以下命令。
```
openssl pkcs12 -export -out www.tencent.com.pfx -inkey 2_www.tencent.com.key -in 1_www.tencent.com_cert.crt
```
例如 ，key 和 crt 文件保存在 D:\ ，运行情况如下：
![](https://main.qcloudimg.com/raw/121bed5ddf8e42e69a00b738046f687a.png)
>!Export Password 不需要的情况下，请直接回车不进行输入。
4. 在 D:\ 已生成的 `www.tencent.com.pfx` 文件，可以继续完成在 IIS 管理器中的证书安装。


