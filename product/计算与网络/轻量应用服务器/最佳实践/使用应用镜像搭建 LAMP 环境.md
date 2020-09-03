## 操作场景

LAMP（Linux+Apache+MySQL+PHP）是目前国际流行的 Web 应用框架，包括了 Linux 操作系统、Apache Web 服务器、MySQL/MariaDB 数据库和 PHP 编程语言环境以及相关组件支持。

>? LAMP 应用镜像底层基于 CentOS 7.6 64位操作系统。
>


## 操作步骤

1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)。
2. 单击【新建】，进入轻量应用服务器购买页面。
![](https://main.qcloudimg.com/raw/6591e97745bdece1b1f2244ea6615cd9.png)
 - **地域**：建议选择靠近目标客户的地域，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，地域选择 “广州”。
 - **镜像**：选择 “LAMP 7.3.15” 应用镜像。
 - **实例套餐**：按照所需的服务器配置（CPU、内存、系统盘、峰值带宽、每月流量），选择一种实例套餐。
 - **实例名称**：自定义实例名称，若不填则默认使用所选镜像名称。批量创建实例时，连续命名后缀数字自动升序。例如，填入名称为 LH，数量选择3，则创建的3个实例名称为 LH1、LH2、LH3。
 - **购买时长**：默认1个月。
 - **购买数量**：默认1台。
3. 单击【立即购买】，并根据页面提示提交订单完成支付。

## 相关操作
### 查看 LAMP 应用的各项配置信息
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)。
2. 在服务器列表中，选择并进入使用 LAMP 应用镜像创建的实例详情页。
3. 选择【应用管理】页签，进入应用管理详情页。
![](https://main.qcloudimg.com/raw/b04bd90643e1c9b50bb500d1476b259c.png)
您可以在此页面查看 LAMP 应用的各项配置信息。例如：
 - Apache 的首页地址和网站根目录。
 - MariaDB 数据的管理员账号（root）和密码、数据库地址和数据库名称。
 >? 管理员密码可通过 Webshell 方式登录实例并执行 `cat ~lighthouse/credentials.txt` 命令获取。
 >
 - Apache 、 MariaDB 和 PHP 软件在 CentOS 操作系统中的安装地址。
 >? 访问 `http://LAMP 实例的公网 IP/phpinfo.php` 可查看 PHP 配置信息。
 >


### 使用 FTP 工具上传代码并调试

1. 登录使用 LAMP 应用镜像创建的实例，并参考 [Linux 轻量应用服务器搭建 FTP 服务](https://cloud.tencent.com/document/product/1207/47638) 文档搭建 FTP 服务。
2. 在本地计算机中使用 FTP 工具（如 WinSCP ）向 LAMP 服务器上传自己的网站代码，并对网站进行测试调试。
