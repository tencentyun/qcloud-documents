## 简介

Discuz! 论坛可以通过配置远程附件功能将论坛的附件保存在腾讯云对象存储（Cloud Object Storage，COS）上，将论坛附件保存在 COS 上有以下好处：

- 附件将拥有更高的可靠性。
- 您的服务器无需为论坛附件准备额外的存储空间。
- 论坛用户查看图片附件时将直连 COS 服务器，不占用您服务器的下行带宽/流量，用户访问速度更快。
- 可配合腾讯云内容分发网络（Content Delivery Network，CDN）进一步提升论坛用户查看图片附件的速度。


## 前提条件

1. 已有 COS 存储桶。如无，可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 操作指引。
2. 已创建服务器。例如云服务器（Cloud Virtual Machine，CVM）。相关指引可参见 [CVM 产品文档](https://cloud.tencent.com/document/product/213)。


## 实践步骤


### 搭建 Discuz! 论坛

腾讯云市场中提供了 Discuz! 镜像，如果您不熟悉 Linux 命令的使用，建议您通过 [镜像部署 Discuz! 论坛](https://cloud.tencent.com/document/product/213/9753)。如果您对 Linux 的使用比较熟悉，并且对业务网站有较高的扩展性需求，您也可以 [手动搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/8043)。


### 准备 COS 存储桶

1. 创建一个访问权限为**公有读私有写**的存储桶，存储桶的地域建议与运行 Discuz! 论坛的 CVM 的地域相同，创建详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。
2. 在存储桶列表中找到刚刚创建的存储桶，并单击**配置管理**。
3. 在左侧导航栏中，选择**概览**页签，查看**访问域名**并记录。
![](https://main.qcloudimg.com/raw/e84d246bb9c44ac9647d4d0abae565b6.png)



### 安装 COS 插件


1. 使用管理员账号登录 Discuz! 论坛并进入**管理中心**页面。
2. 在页面上方单击**插件**。
3. 在插件页面中单击**获取更多插件**。在 Discuz! 应用中心搜索“腾讯云对象存储”，选择并单击“安装应用”。
4. 等待安装完成后，进入插件列表，即可看到已安装的 COS 插件。
![](https://qcloudimg.tencent-cloud.cn/raw/a9400929e88c4ee904100d84e7cc8904.png)
5. 单击设置，开始配置 COS 插件，配置项说明如下：
![](https://qcloudimg.tencent-cloud.cn/raw/e9a09e5c1ee366cdcfea1b12cfe87354.png)
<table>
<thead>
<tr>
<th align="left">配置项</th>
<th align="left">配置值</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">腾讯云 SecretId、腾讯云 SecretKey</td>
<td align="left">访问密钥信息，可前往 <a href="https://console.cloud.tencent.com/capi">云 API 密钥</a> 中创建和获取</td>
</tr>
<tr>
<td align="left">地域</td>
<td align="left">创建存储桶时所选择的地域，需与运行 Discuz! 论坛的 CVM 的地域相同</tdz
</tr>
<tr>
<td align="left">存储桶名称</td>
<td align="left">创建存储桶时自定义的存储桶名称，例如 examplebucket-1250000000</td>
</tr>
</tbody></table>
6. 确认配置信息无误后，单击**提交**即可。


### 发贴测试


1. 进入**默认版块**，单击 **发帖 > 发表帖子**，输入标题，在正文中添加图片，完成图片上传和验证码通过后，单击**发表帖子**。
![](https://qcloudimg.tencent-cloud.cn/raw/8334924b3da7f2762bb3578003477215.png)
2. 单击**管理中心 > 插件 > 腾讯云对象存储 1.0.2**，单击**上传图片和附件到 cos**，然后单击**开始**，等待附件上传成功后，在 COS 存储桶中的 forum 路径下即可找到已上传的图片附件。




## 使用 CDN 加速访问

您如需为已保存了 Discuz! 论坛附件的存储桶配置 CDN 加速，可参见 [CDN 加速配置](https://cloud.tencent.com/document/product/436/18670) 文档。


## 结语

当然，COS不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云COS插件，欢迎点击 [此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406) 一键启动，立即使用！
