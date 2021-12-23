## 操作场景
本文档指导您如何在 Apache 服务器中安装国密标准 SSL 证书。
>?
>- 国密标准 SSL 证书目前仅支持 Linux 环境下 Apache 服务器。
>- 本文档以证书名称 `cloud.tencent.com` 为例。
>-  Apache 版本建议使用版本 `apache-2.4.46` 或 `apache-2.4.48`，您可前往 [Apache 官网](https://httpd.apache.org/download.cgi/) 进行下载或 [单击此处](http://mirrors.tencent.com/apache/httpd/httpd-2.4.51.tar.gz) 快速下载 `apache-2.4.48`。若您需要采用其余版本，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。
>- 当前服务器的操作系统为 CentOS 7，由于操作系统的版本不同，详细操作步骤略有区别。
>- 安装 SSL 证书前，请您在 Apache 服务器上开启 “443” 端口，避免证书安装后无法启用 HTTPS。具体可参考 [服务器如何开启443端口？](https://cloud.tencent.com/document/product/400/45144)
>- SSL 证书文件上传至服务器方法可参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。

## 前提条件
- 已准备远程文件拷贝软件，例如 WinSCP（建议从官方网站获取最新版本）。
- 已准备远程登录工具，例如 PuTTY 或者 Xshell（建议从官方网站获取最新版本）。
- 已购买国密标准（SM2）SSL 证书。
- 安装 SSL 证书前需准备的数据如下：
<table>
<tr>
<th>名称</th>
<th>说明</th>
</tr>
<tr>
<td>服务器的 IP 地址</td>
<td>服务器的 IP 地址，用于 PC 连接到服务器。</td>
</tr>
<tr>
<td>用户名</td>
<td>登录服务器的用户名。</td>
</tr>
<tr>
<td>密码</td>
<td>登录服务器的密码。</td>
</tr>
</table>

>?在腾讯云官网购买的云服务器，您可以登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)  获取服务器 IP 地址、用户名及密码。

## 操作步骤
### 环境配置
>?
>- 国密标准 SSL 证书安装在 Apache 服务器上，Apache 服务器需具备相关环境支持模块。下文将指导您编译配置支持国密标准 SSL 证书的 Apache 服务器。
>- 下述步骤中的目录皆是测试环境的目录，具体路径请根据您的实际环境与需求进行确定。

1. 远程登录 Apache 服务器。例如，使用 [“PuTTY” 工具](https://cloud.tencent.com/document/product/213/35699#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4) 登录。
2. **安装编译工具**：如果您的系统是全新的，请先在服务器上安装 C++ 开发环境，为编译提供环境支持。您可以使用如下命令进行安装。
```
yum install -y gcc 
yum install -y gcc-c++ 
```
3. **下载并编译安装 apr**（以 `apr 1.7.0` 版本为例），您可以通过在服务器上输入以下命令，下载 apr 至服务器并编译安装，由于操作系统的版本不同，详细操作步骤略有区别。
```
#切换至 /usr/local/ 目录下
cd /usr/local/ 
#下载 apr 1.7.0
wget -c http://mirrors.tencent.com/apache/apr/apr-1.7.0.tar.gz
#解压已下载的 apr 1.7.0 压缩包
tar -zvxf apr-1.7.0.tar.gz
#进入解压后的 apr 1.7.0 文件夹并指定编译目录路径。
cd apr-1.7.0/
./configure --prefix=/usr/local/apr
#编译安装 apr
make && make install 
```
4. **下载并编译安装 apr-util**（推荐使用 `apr-util-1.5` 版本，以 `apr-util-1.5` 版本为例）。
```
#切换至 /usr/local/ 目录下
cd /usr/local/ 
#下载 apr-util-1.5.4
wget -c http://archive.apache.org/dist/apr/apr-util-1.5.4.tar.gz
#解压已下载的 apr-util-1.5.4 压缩包
tar -zvxf apr-util-1.5.4.tar.gz 
#进入解压后的 apr-util-1.5.4 文件夹并指定编译目录路径。
cd /usr/local/apr-util-1.5.4/
./configure --prefix=/usr/local/apr-util --with-apr=/usr/local/apr
#编译安装 apr-util
make && make install 
```
>?执行 make 命令时如果出现 `#include <expat.h> ^ compilation terminated.` 报错信息，请输入命令 `yum install -y expat-devel` 安装依赖库。 
>
5. **安装 pcre**。您可以通过以下两种方式进行安装。
 - 推荐使用 `yum` 进行安装。
```
 yum install -y pcre-devel 
```
 - 编译安装。
```
#切换至 /usr/local/ 目录下
cd /usr/local/ 
#下载 pcre-8.43
wget -c https://ftp.pcre.org/pub/pcre/pcre-8.43.tar.gz
#解压已下载的 pcre-8.43 压缩包
tar -zvxf pcre-8.43.tar.gz
#进入解压后的pcre-8.43文件夹并指定编译目录路径。
cd pcre-8.43/
./configure --prefix=/usr/local/pcre 
#编译安装 pcre
make && make install 
```
6. **Apache 服务器安装**：上述三个文件编译安装完成后，请下载 Apache 国密版和国密模块至 `/usr/local` 目录下进行编译安装。
>!
>- 国密模块文件名 `wotrus_ssl.tar.gz` 在解压与安装中请勿修改，否则可能会导致安装错误。
>- 如果在安装 Apache 的过程中找不到 pcre、apr-util 或 apr 等相关文件，请将 `/pcre/bin`、`/apr-util/bin` 或 `/apr/bin` 等文件加入系统路径。
>
```
#下载 Apache httpd-2.4.48 压缩包
wget -c http://mirrors.tencent.com/apache/httpd/httpd-2.4.48.tar.gz
#下载国密模块
wget -c https://www.wotrus.com/download/wotrus_ssl.tar.gz
#解压已下载的 wotrus_ssl 压缩包
tar -zvxf wotrus_ssl.tar.gz 
#解压已下载的 httpd-2.4.48 压缩包
tar -zvxf httpd-2.4.48.tar.gz 
#进入解压后的 httpd-2.4.48 文件夹并指定编译目录路径。
cd httpd-2.4.48/
./configure --prefix=/usr/local/httpd --enable-so --enable-ssl --enable-cgi --enable-rewrite --enable-modules=most --enable-mpms-shared=all --with-mpm=prefork --with-zlib --with-apr=/usr/local/apr --with-apr-util=/usr/local/apr-util --with-ssl=/usr/local/wotrus_ssl2.0 
#编译安装 Apache
make && make install
```

### 国密标准证书安装

1. 已在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中下载并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。 其中包含 Apache 文件夹和 CSR 文件：
 - **文件夹名称**：Apache
 - **文件夹内容**：
    - `1_root_sign_bundle.crt` 证书文件
    - `2_root_encrypt_bundle.crt` 证书文件
    - `3_cloud.tencent.com_sign.crt` 证书文件
    - `4_cloud.tencent.com_encrypt.crt` 证书文件
    - `5_cloud.tencent.com.key` 私钥文件
  - **CSR 文件内容**：
    - 	`cloud.tencent.com_sign.csr` 文件
    - 	`cloud.tencent.com_encrypt.csr` 文件

>?CSR 文件是申请证书时由您上传或系统在线生成的，提供给 CA 机构。安装时可忽略该文件。
>
2. 使用 “WinSCP”（即本地与远程计算机间的复制文件工具）登录 Apache 服务器。
3. 进入 `/usr/local/httpd/conf` 目录，新建 `cert` 目录，将已获取到的 `1_root_sign_bundle.crt` 证书文件、`2_root_encrypt_bundle.crt` 证书文件、`3_cloud.tencent.com_sign.crt` 证书文件、`4_cloud.tencent.com_encrypt.crt` 证书文件以及 `5_cloud.tencent.com.key` 私钥文件从本地目录拷贝到 Apache 服务器的 `/usr/local/httpd/conf/cert` 目录下。
4. 进入 `/usr/local/httpd/conf` 目录，按照以下步骤编辑 `httpd.conf` 文件：
   1. 请在 `#ServerName www.example.com:80` 下增加 `ServerName（您的域名）:80`。
   2. 请去掉 `LoadModule ssl_module modules/mod_ssl.so` 前的 `#`。
   3. 请在 `#Include conf/extra/httpd-ssl.conf` 下增加 `Include conf/ssl.conf` 文件内容后保存并退出。
5. 在 `/usr/local/httpd/conf` 目录下，新建一个 `ssl.conf` 文件，添加如下配置：
```
Listen 443
<VirtualHost *:443>
#填写证书名称
ServerName cloud.tencent.com
#填写网站文件路径
DocumentRoot website根目录
#启用 SSL 功能
SSLEngine on
# SM2 证书 sign 配置
SSLCertificateFile /usr/local/httpd/conf/cert/3_cloud.tencent.com_sign.crt 
SSLCertificateKeyFile /usr/local/httpd/conf/cert/5_cloud.tencent.com.key
SSLCertificateChainFile /usr/local/httpd/conf/cert/1_root_sign_bundle.crt
# SM2 证书 encrypt 配置
SSLCertificateFile /usr/local/httpd/conf/cert/4_cloud.tencent.com_encrypt.crt
SSLCertificateKeyFile /usr/local/httpd/conf/cert/5_cloud.tencent.com.key
SSLCertificateChainFile /usr/local/httpd/conf/cert/2_root_encrypt_bundle.crt
# sign 和 encrypt 配置中的 .key 为同一个
#请按照以下协议配置
SSLProtocol all -SSLv2 -SSLv3
#请按照以下套件配置，配置加密套件，写法遵循 openssl 标准。
SSLCipherSuite SM2-WITH-SMS4-SM3:ECDH:AESGCM:HIGH:MEDIUM:!RC4:!DH:!MD5:!aNULL:!eNULL
SSLHonorCipherOrder on
<Directory "website根目录">
Options -Indexes -FollowSymLinks +ExecCGI
AllowOverride None
Order allow,deny
Allow from all
Require all granted
</Directory>
</VirtualHost>
```
>?以上配置内容仅为参考，具体的证书名称，证书目录，`Directory` 等配置请根据实际环境配置。
>
6. 您通过执行以下命令验证配置文件问题。
```
/usr/local/httpd/bin/httpd -t
```
 - 若提示 `Syntax OK`，则表示配置正常，可以启动 Apache 服务器。
 - 若提示非 `Syntax OK`，请您重新配置或者根据提示修改存在问题。
7. 执行以下命令重新启动 Apache 服务器，即可使用 `https://cloud.tencent.com` 进行访问。
```
/usr/local/httpd/bin/httpd -k restart
```


### 国际标准证书与国密标准证书双安装（可选）
若您需要通过国际标准证书与国密标准证书双证书安装的方式解决浏览器兼容性问题。您可以通过以下操作设置：
>?腾讯云提供免费的 DV 型 SSL 证书以供购买了国密标准 DNSPod 证书的用户顺利解决浏览器兼容问题。申请证书请查看 [域名型（DV）免费 SSL 证书](https://cloud.tencent.com/document/product/400/8422)。
>
1. 使用 “WinSCP”（即本地与远程计算机间的复制文件工具），将已获取到的国际标准证书中的 `1_root_bundle.crt` 证书文件、`2_cloud.tencent.com.crt` 证书文件以及 `3_cloud.tencent.com.key` 私钥文件从本地目录拷贝到 Apache 服务器的 `/usr/local/httpd/conf` 目录下。 
2. 编辑 `/usr/local/httpd/conf` 目录下的 `ssl.conf` 文件。
3. 请在 `SSLEngine on` 下面换行，并添加如下内容：
```
SSLCertificateFile /usr/local/httpd/conf/cert/2_cloud.tencent.com.crt
SSLCertificateKeyFile /usr/local/httpd/conf/cert/3_cloud.tencent.com.key
SSLCertificateChainFile /usr/local/httpd/conf/cert/1_root_bundle.crt
```
>? 以上配置内容仅为参考，具体的证书名称，证书目录，请根据实际环境配置。
>
4. 您通过执行以下命令验证配置文件问题。
```
/usr/local/httpd/bin/httpd -t
```
 - 若提示 `Syntax OK` ，则表示配置正常，可以启动 Apache 服务器。
 - 若提示非 `Syntax OK` ，请您重新配置或者根据提示修改存在问题。
5. 重新启动 Apache 服务器，即可解决浏览器兼容问题。

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。


















