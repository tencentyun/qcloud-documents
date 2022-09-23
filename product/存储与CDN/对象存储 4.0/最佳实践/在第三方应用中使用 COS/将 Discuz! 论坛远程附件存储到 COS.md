## 简介

Discuz! 论坛可以通过配置远程附件功能将论坛的附件保存在腾讯云对象存储（Cloud Object Storage，COS）上，将论坛附件保存在 COS 上有以下好处：

- 附件将拥有更高的可靠性。
- 您的服务器无需为论坛附件准备额外的存储空间。
- 论坛用户查看图片附件时将直连 COS 服务器，不占用您服务器的下行带宽/流量，用户访问速度更快。
- 可配合腾讯云内容分发网络（Content Delivery Network，CDN）进一步提升论坛用户查看图片附件的速度。

## 准备工作

1. 搭建 Discuz! 论坛。
	- 您可在 [Discuz! 官方发布](https://www.discuz.net/) 页面下载 Discuz! 论坛的最新版并查看安装说明。
	- 您也可以在 [腾讯云市场](https://market.cloud.tencent.com/) 中搜索购买已经预装 Discuz! 论坛程序的云服务器（Cloud Virtual Machine，CVM）镜像。
2. 创建一个**公有读私有写**的存储桶，存储桶的地域建议与运行 Discuz! 论坛的 CVM 的地域相同，创建详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。
3. 在存储桶列表中找到刚刚创建的存储桶，并单击**配置管理**。
![](https://main.qcloudimg.com/raw/6e011a00b4646f7d465056e9c88aa78c.png)
4. 在左侧导航栏中，选择**概览**页签，查看**访问域名**并记录。
![](https://main.qcloudimg.com/raw/e84d246bb9c44ac9647d4d0abae565b6.png)
5. 在运行 Discuz! 论坛的 CVM 上，部署 COS FTP Server 工具，部署步骤可参见 [FTP Server 工具](https://cloud.tencent.com/document/product/436/7214)。
	- 在配置 FTP Server 时，FTP Server 配置中的 masquerade_address 设置为 127.0.0.1 以保证该 FTP 服务仅能被本机访问。
	- 您也可以使用独立的 CVM 单独部署 FTP Server，此时配置中的 masquerade_address 参数，您可依据实际情况配置为内网 IP 或外网 IP。


## 安装插件

### Discuz! X3.4版本通过补丁升级安装
1. 在 [GitHub](https://github.com/Tencent-Cloud-Plugins/tencentcloud-discuzx-plugin-cos)  中获取补丁包。
2. 将补丁包中的文件中修改的部分合并到源站中的对应的文件。
3. 在 ./upload 目录下新增 extend 目录及目录下的文件。合并以下文档：
 - ./upload/source/class/class_core.php
 - ./upload/source/function/function_core.php
 - ./upload/source/admincp/admincp/admincp_checktools.php
 - ./upload/source/admincp/admincp/admincp_setting.php
 - ./upload/source/admincp/language/lang_admincp.php
 - ./upload/source/module/forum/forum_attachment.php

### 补充说明

1. PHP 7.2之后已经移除了\_\_autoload()函数，如果出现告警需要注释或删除 upload/source/class/class_core.php 文件中的"\_\_autoload()"函数。
![](https://qcloudimg.tencent-cloud.cn/raw/6b510689dcbfd3fa7b244b8bee2611c3.png)
2. Discuz!X 版本更新比较频繁，可能在最新的版本中代码和本次修改的代码会有重叠部分，建议使用文件比较工具认真比较合并，且在修改代码前做好本地备份。
3. 当前扩展中不支持将历史附件上传到腾讯云的对象存储功能，如果需要同步历史附件到腾讯云存储中，需要站点维护人员手动上传历史附件。在同步历史附件前请做好全站备份。
>? 您可使用 [工具概览](https://cloud.tencent.com/document/product/436/6242) 中介绍的上传工具上传附件；或者通过对象存储控制台直接上传文件。附件存放在存储桶中的路径和附件在本地的'/upload/data/attachment/'目录下的相对路径需保持一致。
>
![](https://qcloudimg.tencent-cloud.cn/raw/2b689f80b81921c1c608874af257b90a.png)


## 配置远程附件

1. 使用管理员账号登录 Discuz! 论坛并进入**管理中心**页面。
2. 依次进入**全局 > 上传设置 > 基本设置**。
3. 在**基本设置**中选择"启用远程附件">"启用腾讯云远程附件", 在远程访问 URL 中填入腾讯云存储桶的访问域名。
![](https://qcloudimg.tencent-cloud.cn/raw/b93e681591fcff6e632e2627c5a2941c.png)
4. 在"腾讯云远程附件"配置页面中配置腾讯云对象存储的 SecretId、SecretKey、所属区域、空间名称等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/9093cb35a7f5360d3fe3068ea7bc9129.png)
配置项说明如下：
 - **SecretId**：在腾讯云云平台 API 密钥上申请的标识身份的 SecretId。可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取。
 - **SecretKey**：在腾讯云云平台 API 密钥上申请的标识身份的 SecretId 对应的 SecretKey。
 - **所属地域**：在腾讯云服务器所在地域。关于地域说明请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
 - **空间名称**：COS 服务中存储桶的名称。详情请参见 [存储桶概述](https://cloud.tencent.com/document/product/436/13312)。
 - **远程访问 URL**：存储桶的访问域名。相关说明请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
5. 填写好配置参数后，单击**测试远程附件**，如果提示“远程附件设置一切正常”，说明设置成功。然后保存配置。
6. 发帖测试。
<img src="https://main.qcloudimg.com/raw/5d984846af7d99780b21d4f1b6ca4045.png" width="90%" ></img>
7. 单击附件图片，单击右上角的**在新窗口打开**图标。
<img src="https://main.qcloudimg.com/raw/25175e71eac8738097f5c66c26489d7e.png" width="90%"></img>
8. 查看附件图片的 URL，确认附件图片的 URL 指向腾讯云 COS。
<img src="https://main.qcloudimg.com/raw/28803b68fd3cc513c5a26d8a160579fe.png" width="90%" ></img>


## 使用 CDN 加速访问

1. 您如需为已保存了 Discuz! 论坛附件的存储桶配置 CDN 加速，可参见 [CDN 加速配置](https://cloud.tencent.com/document/product/436/18670) 文档。
2. 在 Discuz! 论坛的**远程附件**设置中将**远程访问 URL**修改为默认 CDN 加速域名或自定义加速域名即可。

