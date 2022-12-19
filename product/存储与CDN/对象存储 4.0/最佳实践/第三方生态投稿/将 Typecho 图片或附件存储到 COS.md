Typecho 是使用 PHP 语言开发的博客平台，用户可以在支持 PHP 和 [MySQL 数据库 ](https://cloud.tencent.com/product/cdb?from=10680)的服务器上架设属于自己的网站。

Typecho 原生支持 Markdown 排版语法，易读更易写。支持各类云主机，即使面对突如其来的高访问量，也能轻松应对。

本文将介绍如何使用插件实现远程存储图片、附件功能，将 Typecho 的静态资源存储在腾讯云 [对象存储](https://cloud.tencent.com/product/cos?from=10680)（Cloud Object Storage，COS） 上。

## 准备工作
### 搭建博客
1. 您可从[ Typecho官网 ](https://typecho.org/)下载完整源码并按提示安装。
2. 如果您是轻量应用服务器用户，也可以选择安装/重装官方提供的 Typecho 应用镜像。
![](https://qcloudimg.tencent-cloud.cn/raw/a47dee62b4c4636fe0309c8731b9c377.png)

### 创建存储桶
可根据需要，创建一个私有读写或公有读私有写的存储桶（推荐创建私有读写存储桶），存储桶的地域建议选择与 Typecho 博客平台服务器相同的地域，体验更佳。创建详情参见 [创建存储桶文档](https://cloud.tencent.com/document/product/436/13309?from=10680)。


## 安装并设置插件
### 安装腾讯云对象存储插件（Typecho 版）
“腾讯云对象存储插件（Typecho版）”是苏苏编写的个人项目，您可从 [github](https://github.com/cnhongv/typecho-cos-plugin/) 下载最新的 [release 版](https://github.com/cnhongv/typecho-cos-plugin/releases/)本。下载完成后，将“TypechoCosPlugin”文件夹上传至 Typecho 博客的插件路径（/usr/plugins/），并在后台启用插件。
![](https://qcloudimg.tencent-cloud.cn/raw/c058bd6ddaed93b97822592e2cc6af37.png)

### 设置腾讯云对象存储插件（Typecho 版）
1. 点击**设置**，填写配置信息。
![](https://qcloudimg.tencent-cloud.cn/raw/0b41383c2e27f457c365bff29b77ebb6.png)
- 以下为基础设置（必填信息）
![](https://qcloudimg.tencent-cloud.cn/raw/2455bbda12ea32e624371ad3b173e9d1.png)

| 设置项       | 注释                                                                                   |
| --------- | ------------------------------------------------------------------------------------ |
| SecretId  | 用于标识 API 调用者身份，可以简单类比为用户名。可从 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取。 |
	| SecretKey | 用于验证 API 调用者的身份，可以简单类比为密码。可从 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取。 |
| 所属地域      | 腾讯云 COS 存储桶所在地域。详情参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。     |
| 存储桶名称     | 腾讯云 COS 服务中存储桶的名称。详情参见 [存储桶概述](https://cloud.tencent.com/document/product/436/13312)。    |
| 对象存储路径    | 文件存储的前缀，为更接近 Typecho 默认设置，本插件默认为 `usr/uploads`，可根据实际情况自行修改。                              |

>?用户必须严格保管 SecretId、SecretKey 安全凭证，避免泄露，否则将危及财产安全。如已泄漏，请立刻禁用该安全凭证。

- 以下为高级设置（可选信息）
![](https://qcloudimg.tencent-cloud.cn/raw/60e524bcb9d41b2b5bce1cebb2279b3e.png)

| 设置项           | 注释                                                                                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 访问域名          | 对象文件对外访问的域名，若设置不正确，图片、附件将无法正常访问，如无特殊要求可留空，使用默认域名。详情参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) 。                                                |
| 使用签名链接        | 若您创建的存储桶/对象存储路径的为**私有读写**，必须开启本项设置，才可正常访问。详情参见 [访问权限类型](https://cloud.tencent.com/document/product/436/13324#.E8.AE.BF.E9.97.AE.E6.9D.83.E9.99.90.E7.B1.BB.E5.9E.8B)。 |
| 本地删除同步删除 COS 文件 | 在**博客后台-管理-文件**删除文件时，是否同步删除 COS 上的对应文件。                                                                                                                               |
| 在本地保存         | 开启后，上传到 COS 的同时，自动在本地相同路径保存一份副本，会占用本地服务器的存储空间。                                                                                                                        |
| 删除时同步删除本地备份   | 在**博客后台-管理-文件**删除文件时，是否同步删除本地服务器备份的文件副本（须开启**在本地保存**才会生效）。                                                                                                          |

2. 配置填写完成后，单击**保存**即可。

## 使用插件
1. 在博客后台撰写-撰写文章，通过上传附件/Ctrl+V粘贴上传图片/文件，检查插入的附件地址是否为COS域名（默认域名的后缀为myqcloud.com）。若为COS域名，则配置成功。
![](https://qcloudimg.tencent-cloud.cn/raw/b8aa182f1deac2ebd7244a5b130d50fa.png)
2. 还可前往腾讯云控制台 [COS 存储桶](https://console.cloud.tencent.com/cos/bucket) 对应路径，查看是否存在对应文件。
![](https://qcloudimg.tencent-cloud.cn/raw/66b3b4a01a548e9035f6eb326fc06764.png)

以上便是腾讯云对象存储插件（Typecho版）的介绍，如有变动请以最新版插件为准。
