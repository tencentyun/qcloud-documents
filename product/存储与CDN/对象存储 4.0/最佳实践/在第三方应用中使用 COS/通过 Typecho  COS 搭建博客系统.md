## 简介


[Typecho](https://typecho.org/) 是一个基于 PHP 的开源博客平台。本文主要介绍如何使用插件实现远程附件功能，将 Typecho 的媒体库附件存储在腾讯云 [对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/product/cos) 上。


## 前提条件

1. 已有 COS 存储桶。如无，可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 操作指引。
2. 已创建服务器。例如云服务器 CVM。相关指引可参见 [CVM 产品文档](https://cloud.tencent.com/document/product/213)。




## 实践步骤

### 安装 Typecho


您可以在 [Typecho 官方页面](http://typecho.org/download) 下载 Typecho 的最新版并查看官方安装指南进行安装。您也可以通过宝塔面板安装。宝塔面板安装指引请参见 [宝塔官网](https://www.bt.cn/)。下面以宝塔安装 Typecho 为例。

#### 安装宝塔
1. 首先准备一台 CVM 机器，然后安全组的入站规则和出站规则按照如下配置：
 - 入站规则
![](https://qcloudimg.tencent-cloud.cn/raw/e90f6a65388de747676dd894090ce158.png)
 - 出站规则
![](https://qcloudimg.tencent-cloud.cn/raw/0fd12abd0a1a729d7dc78678a8c50b94.png)
2. 执行宝塔官网提供的 Centos 安装脚本：
```
yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh ed8484bec
```
在 CVM 机器上直接执行如下图所示：
![img](https://qcloudimg.tencent-cloud.cn/raw/672aed3217d3d1cf33cd880ed4977aba.png)
3. 执行中会出现如下信息，直接输入 y 回车即可。
![img](https://qcloudimg.tencent-cloud.cn/raw/164affb276edefaad6265e0438c197ad.png)
执行成功后，会生成网站账号（需记录保存），如下所示：
![img](https://qcloudimg.tencent-cloud.cn/raw/6b12cfe7b0b28497a272ea6027cf40b3.png)

#### 通过宝塔安装 Typecho


1. 宝塔安装后，打开桌面上的浏览器，输入在 CVM 生成的宝塔外网链接：`http://43.xxx.xxx.132:16859/c2601bbd`（使用时请替换为自己的 IP）。
2. 单击添加站点，并配置相关参数，输入 CVM 的 IP，其他配置（根目录、FTP 账号、数据库账号等）保持默认。
![](https://qcloudimg.tencent-cloud.cn/raw/d2f1041e87750e292f7d0128f90fd5a7.png)
3. 站点创建完成后，进入站点。
4. 单击**文件**导航栏，在文件页面中单击**远程下载**，填入 Typecho 的 GitHub 源码地址：`https://github.com/typecho/typecho/releases/latest/download/typecho.zip`，然后单击**确认**。
![](https://qcloudimg.tencent-cloud.cn/raw/be8318b9ad5ffebb8a8955ff46009638.png)
5. Typecho 源码文件下载后，并完成解压，然后通过浏览器访问链接 `http://43.xxx.xxx.132/install.php`（使用时请替换为自己的站点 IP）。
6. 根据页面提示，填写如下信息：
![](https://qcloudimg.tencent-cloud.cn/raw/e62c6ead50e2e0ecd69f5efd17dc178a.png)
>?
>可在宝塔界面中获取数据库用户名、密码、名字。
>![](https://qcloudimg.tencent-cloud.cn/raw/c43f41c188a3c0d420a2bf7876b9f9f9.png)
7. 配置完成后输入您设置的用户名和密码即可登录成功。




### 安装 COS 插件


1. 配置完成后，在宝塔 43.xxx.xxx.132 目录下单击**远程下载**，填入以下插件链接，然后得到该插件的压缩文件。
```plaintext
https://github.com/Tencent-Cloud-Plugins/tencentcloud-typecho-plugin-cos/archive/refs/heads/master.zip
```
2. 对压缩包进行解压后，复制 TypechoCosPlugin 文件夹到 Typecho 安装路径 /usr/plugins/ 内。复制 /var/Widget/Upload.php 到 Typecho 博客源码安装路径 /var/Widget/ 内，覆盖博客源码中的 /var/Widget/Upload.php 文件。
3. 刷新 Typecho 的后台，即可看到该插件并启用插件。
4. 启用插件后，设置插件相关参数以便关联到 COS，配置信息如下：
 - 基础设置
<table>
   <tr>
      <th width="0%" >配置项</td>
      <th width="0%" >配置值</td>
   </tr>
   <tr>
      <td>SecretId</td>
      <td>访问密钥信息，可前往 <a href="https://console.cloud.tencent.com/capi">云 API 密钥</a> 中创建和获取</td>
   </tr>
   <tr>
      <td>SecretKey</td>
      <td>访问密钥信息，可前往 <a href="https://console.cloud.tencent.com/capi">云 API 密钥</a> 中创建和获取。</td>
   </tr>
   <tr>
      <td>所属地域</td>
      <td>创建存储桶时所选择的地域。</td>
   </tr>
   <tr>
      <td>存储桶名称</td>
      <td>创建存储桶时自定义的名称，例如 examplebucket-1250000000。</td>
   </tr>
   <tr>
      <td>对象存储路径</td>
      <td>文件所存储的 COS 路径，插件默认路径为 usr/uploads，可自行修改。</td>
   </tr>
</table>
<img style="width:700px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c97981a92144d65ba74dd78ab3ed6595.jpg" />
 - 高级设置
<table>
   <tr>
      <th width="0%" >配置项</td>
      <th width="0%" >配置值</td>
   </tr>
   <tr>
      <td>访问域名</td>
      <td>不填则使用默认存储桶域名。详情请参见 <a href="https://cloud.tencent.com/document/product/436/6224">地域和访问域名</a>。</td>
   </tr>
   <tr>
      <td>使用签名链接</td>
      <td>若您所创建的存储桶的访问权限为<b>私有读写</b>，则开启该项才可正常访问文件。详情可参见 <a href="https://cloud.tencent.com/document/product/436/13324#.E8.AE.BF.E9.97.AE.E6.9D.83.E9.99.90.E7.B1.BB.E5.9E.8B">访问权限类型</a>。</td>
   </tr>
   <tr>
      <td>本地删除同步删除 COS 文件</td>
      <td>当您在<b>博客后台</b>删除文件时，是否同步删除 COS 上的对应文件。</td>
   </tr>
   <tr>
      <td>在本地保存</td>
      <td>开启后，上传到 COS 的同时，自动在本地相同路径保存一份副本。建议不开启，会占用本地服务器的存储空间。</td>
   </tr>
   <tr>
      <td>删除时同步删除本地备份</td>
      <td>当您在<b>博客后台</b>删除文件时，是否同步删除本地服务器备份的文件副本（前提是已开启<b>在本地保存</b>才会生效）。</td>
   </tr>
</table>
<img style="width:700px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/6bed3fb18e64975319954b7aa06c64f9.jpg" />
5. 完成以上设置后，即可完成博客系统的搭建，上传图片即可显示该 COS 的存储桶域名。
![](https://qcloudimg.tencent-cloud.cn/raw/6c935d172d1153f3c23a6d0ef757a59d.png)


## 常见问题


1. 若在安装页面中出现以下报错，则说明 PHP 版本可能不支持，建议是将 PHP 版本替换为7.2以上。
![img](https://qcloudimg.tencent-cloud.cn/raw/ade924ec84d96fd69e7acdbcaefe62a3.png)
![img](https://qcloudimg.tencent-cloud.cn/raw/46a24d6138c8ea3d49fbbc6b507aaebb.png)

解决方法：
打开宝塔面板，单击软件商店，在 php 这里单击选择7.2以上版本即可。
![img](https://qcloudimg.tencent-cloud.cn/raw/e34844f437da44e8c9dad59fd89ec337.png)

2. 若提示**上传目录无法写入**等报错，则需要重新去 Typecho 官网下载最新安装包。
![img](https://qcloudimg.tencent-cloud.cn/raw/9107b833831b3249ccdc6451f14e4bb7.png)




## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击 [此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406) 一键启动，立即使用！

