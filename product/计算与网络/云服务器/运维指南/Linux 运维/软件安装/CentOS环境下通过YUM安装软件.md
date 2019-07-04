为提升用户在云服务器上的软件安装效率，减少下载和安装软件的成本，腾讯云提供了 Yum 下载源。在 CentOS 环境下，用户可通过 Yum 快速安装软件。对于 Yum 下载源，用户不需要添加软件源，可以直接安装软件包。

### 安装步骤 
>? 该步骤需要超级管理员帐号才能操作，此处root默认为超级管理员权限。

1. 在 root 权限下，通过以下命令来安装软件：
```
yum install 软件名称
``` 
>**注意：**
>从 CentOS 7 系统开始，MariaDB 成为 yum 源中默认的数据库安装包。在 CentOS 7 及以上的系统中使用 yum 安装 MySQL 包将无法使用 MySQL。您可以选择使用完全兼容的 MariaDB，或单击 [参阅此处](https://www.linode.com/docs/databases/mysql/how-to-install-mysql-on-centos-7) 进行较低版本的 MySQL 的安装。

2. 输入上述命令后，系统将自动搜索相关的软件包和依赖关系，并且在界面中提示用户确认搜索到的软件包是否合适。
例如，键入`yum install PHP`之后，界面显示如图：
![](https://mc.qcloudimg.com/static/img/cdf81bb49022aa8924968864571922ed/39.png)
3. 确认软件包合适无误后，键入`y`，开始安装软件。界面提示`Complete`即安装完成。
![](https://mc.qcloudimg.com/static/img/c98bda7d1f3f42156f9015e3c9d00295/40.png)

### 查看已安装软件信息
软件安装完成后：
- 可通过命令` rpm -ql 软件名`查看软件包具体的安装目录。
- 可通过命令` rpm -q 软件名`查看软件包的版本信息。

以 PHP 为例：
![](https://mc.qcloudimg.com/static/img/d8b9e21cc801da16b76011b3886e1351/42.png)


