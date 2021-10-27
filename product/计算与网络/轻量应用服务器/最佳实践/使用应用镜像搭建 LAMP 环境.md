## 操作场景

LAMP（Linux+Apache+MySQL+PHP）是目前国际流行的 Web 应用框架，包括了 Linux 操作系统、Apache Web 服务器、MySQL/MariaDB 数据库和 PHP 编程语言环境以及相关组件支持。



<dx-alert infotype="explain" title="">
LAMP 应用镜像底层基于 CentOS 7.6 64位操作系统。
</dx-alert>



## 操作步骤

1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)。
![](https://main.qcloudimg.com/raw/b7f0f2d6423cce18e14e309a3d52c2e3.png)
 - **地域**：建议选择靠近目标客户的地域，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，地域选择 “广州”。
 - **镜像**：选择 “LAMP 7.3.15” 应用镜像。
 - **实例套餐**：按照所需的服务器配置（CPU、内存、系统盘、峰值带宽、每月流量），选择一种实例套餐。
 - **实例名称**：自定义实例名称，若不填则默认使用所选镜像名称。批量创建实例时，连续命名后缀数字自动升序。例如，填入名称为 LH，数量选择3，则创建的3个实例名称为 LH1、LH2、LH3。
 - **购买时长**：默认1个月。
 - **购买数量**：默认1台。
3. 单击**立即购买**，并根据页面提示提交订单完成支付。

## 相关操作
### 查看 LAMP 应用的各项配置信息
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)。
2. 在服务器列表中，选择并进入使用 LAMP 应用镜像创建的实例详情页。
3. 选择**应用管理**页签，进入应用管理详情页。
![](https://main.qcloudimg.com/raw/b04bd90643e1c9b50bb500d1476b259c.png)
您可以在此页面查看 LAMP 应用的各项配置信息。例如：
 - Apache 的首页地址和网站根目录。
 - MariaDB 数据的管理员账号（root）和密码、数据库地址和数据库名称。
<dx-alert infotype="explain" title="">
管理员密码可通过 Webshell 方式登录实例并执行 `cat ~lighthouse/credentials.txt` 命令获取。
</dx-alert>
 - Apache 、 MariaDB 和 PHP 软件在 CentOS 操作系统中的安装地址。
<dx-alert infotype="explain" title="">
访问 `http://LAMP 实例的公网 IP/phpinfo.php` 可查看 PHP 配置信息。
</dx-alert>



### 使用 FTP 工具上传代码并调试

1. 登录使用 LAMP 应用镜像创建的实例，并参考 [Linux 轻量应用服务器搭建 FTP 服务](https://cloud.tencent.com/document/product/1207/47638) 文档搭建 FTP 服务。
2. 在本地计算机中使用 FTP 工具（如 WinSCP ）向 LAMP 服务器上传自己的网站代码，并对网站进行测试调试。

### 域名与 DNS 解析设置
您可以给自己的 LAMP 实例设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

### 开启 HTTPS 访问
可参考 [Apache 服务器证书安装](https://cloud.tencent.com/document/product/1207/50330) 文档为您的 LAMP 实例安装 SSL 证书并开启 HTTPS 访问。
