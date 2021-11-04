## 操作场景
为了提升您在云服务器上的软件安装效率，减少下载和安装软件的成本，腾讯云提供了 zypper 下载源。openSUSE 操作系统和部分 SLES 的云服务器用户可通过 zypper 快速安装软件。本文档以 openSUSE 操作系统为例，指导您通过 zypper 快速安装软件。

## 操作步骤
### 查看软件源

1. 使用 root 帐号登录 openSUSE 操作系统的云服务器。
2. 执行 `zypper service-list` 或 `zypper sl` 命令，列出软件源。
例如，执行 `zypper sl` 命令，返回类似如下信息：
![](https://main.qcloudimg.com/raw/ee336605784eca333f10777ccb7cf5ed.png)



### 安装软件包[](id:SearchPackage)

1. 执行 `zypper search` 或 `zypper se` 命令，搜索软件包。
例如，搜索 Nginx 软件包，则可执行以下命令：
```
zypper se nginx
```
返回类似如下结果：
![](https://main.qcloudimg.com/raw/292106a01b048171007247cb9cdf00c0.png)
2. 根据搜索到的软件包名，执行 `zypper install` 或 `zypper in` 命令，安装软件。
<dx-alert infotype="explain" title="">
如果您需要安装多个软件，软件包名之间用空格隔开。安装软件时，如果该软件需要依赖包，会自动下载安装，无需自己安装依赖包。
</dx-alert>
例如，安装 Nginx，则可执行以下命令：
```
zypper install nginx
```
例如，安装 PHP 和 PHP-FPM 等软件，则可执行以下命令：
```
zypper install MySQL-server-community php5-mysql php5 php5-fpm
```


### 查看已安装软件的信息

1. 待软件安装完成后，执行以下命令，查看软件包具体的安装目录。
```
rpm -ql
```
例如，查看 Nginx 软件包具体的安装目录，则执行以下命令：
```
rpm -ql nginx
```
返回类似如下信息：
![](https://main.qcloudimg.com/raw/b4ad19a8735041bf78942f5ea351dc2e.png)
2. 执行以下命令，查看软件包的版本信息。
```
rpm -q
```
例如，查看 Nginx 软件包的版本信息，则执行以下命令：
```
rpm -q nginx
```
返回类似如下信息：
![](https://main.qcloudimg.com/raw/9950192d2cf51c7ab30c2109b3e52d14.png)

