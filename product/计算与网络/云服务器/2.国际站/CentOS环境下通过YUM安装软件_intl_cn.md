为了提升用户在云服务器上的软件安装效率，减少下载和安装软件的成本，腾讯云提供了Yum下载源。在CentOS环境下，用户可通过YUM快速安装软件。

对于Yum下载源，不需要添加软件源，可以直接安装软件包。

## 1. 安装步骤

1) 在root权限下，通过以下命令来安装软件：
```
yum install [nginx][php][php-fpm][mariadb][mariadb-server][mysql][mysql-server]...
```

>注：自CentOS 7来，MariaDB成为yum源中默认的数据库安装包，在CentOS 7以上的系统中使用yum安装MySQL包将无法使用MySQL。您可以选择使用完全兼容的MariaDB，或参考[这里](https://www.linode.com/docs/databases/mysql/how-to-install-mysql-on-centos-7)进行MySQL较低版本的安装。


2) 系统会自动搜索相关的软件包和依赖关系，并且在界面中提示用户确认搜索到的软件包是否合适，如下图所示：
![](//mccdn.qcloud.com/static/img/f61a066066619f09fed1be6fa4a8a4b0/image.png)

3) 输入“y”确认后，开始安装软件，安装完成后会提示“Complete”，如下图所示：
![](//mccdn.qcloud.com/static/img/e36f74f325c00814c3c840aeda9c26a6/image.png)

## 2. 查看安装的软件信息
软件安装完成后，可通过以下命令查看软件包具体的安装目录。

```
 rpm -ql 
```
以查看nginx的安装目录为例：
![](//mccdn.qcloud.com/img56a61fa482658.png)

可通过以下命令查看软件包的版本信息。
```
 rpm -q 
```
以查看nginx的版本为例（实际的版本可能和此版本不一致，请以实际查询到的版本为准）：
![](//mccdn.qcloud.com/img56a621c372e23.png)