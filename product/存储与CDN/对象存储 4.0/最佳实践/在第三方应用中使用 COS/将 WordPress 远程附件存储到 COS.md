## 简介

[WordPress](https://cn.wordpress.org/) 是使用 PHP 语言开发的博客平台，用户可以在支持 PHP 和 MySQL 数据库的服务器上架设属于自己的网站，也可以把 WordPress 当作一个内容管理系统（CMS）来使用。

WordPress 功能强大、扩展性强，这主要得益于其插件众多，易于扩充功能，基本上一个完整网站该有的功能，通过其第三方插件都能实现所有功能。

这篇文章我们来介绍一下如何使用插件实现远程附件功能，将 WordPress 的媒体库附件存储在腾讯云 [对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/product/cos) 上。

COS 具有高扩展性、低成本、可靠和安全等特点，将媒体库附件保存在 COS 上有以下好处：

- 附件将拥有更高的可靠性。
- 您的服务器无需为附件准备额外的存储空间。
- 用户查看图片附件时将直连 COS 服务器，不占用您服务器的下行带宽/流量，用户访问速度更快。
- 可配合腾讯云 [内容分发网络（Content Delivery Network，CDN）](https://cloud.tencent.com/product/cdn) 进一步提升用户查看图片附件的速度，优化网站访问速度。

## 准备工作

1. 搭建 WordPress 博客平台。
 - 您可以在 [WordPress 官方页面](https://cn.wordpress.org/download/) 下载 WordPress 的最新版并查看安装指南。
 - 您也可以在安装服务器系统时在 [镜像市场](https://market.cloud.tencent.com/) 中选择预装 WordPress 博客平台的云服务器（Cloud Virtual Machine，CVM）镜像。
2. 创建一个**公有读私有写**的存储桶，存储桶的地域建议与运行 WordPress 博客平台的 CVM 的地域相同，创建详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。
3. 在**存储桶列表**中找到刚才创建的存储桶，并单击其存储桶名称，进入存储桶页面。
![](https://main.qcloudimg.com/raw/879cce343c28376f41b6561d6c73a6df.png)
4. 在左侧导航栏中，单击**概览**，查看访问域名并记录。
![](https://main.qcloudimg.com/raw/f70fd4d43e0db9faca94f5d5f4e2ac60.png)

## 安装并配置插件

### 安装插件

在 WordPress 后台，单击**插件 > 安装插件**，开始安装插件。您可通过下面两种方式获取插件并安装：

 - 后台直接搜索 **tencentcloud-cos** 进行安装（推荐使用）。
 - 您也可以从 [Github](https://github.com/Tencent-Cloud-Plugins/tencentcloud-wordpress-plugin-cos) 下载最新 releases 源码，通过 WordPress 后台上传安装，或者直接将源码上传到 WordPress 插件目录`wp-content/plugins`，然后在后台启用。

### 配置插件

1. 单击 WordPress 左侧导航栏**腾讯云设置**，然后在页面中配置 COS 的相关信息，配置说明见下表：
<table>
<thead>
<tr>
<th align="left">配置项</th>
<th align="left">配置值</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SecretId、SecretKey</td>
<td align="left">访问密钥信息，可前往 <a href="https://console.cloud.tencent.com/capi">云 API 密钥</a> 中创建和获取</td>
</tr>
<tr>
<td align="left">所属地域</td>
<td align="left">创建存储桶时所选择的地域</tdz
</tr>
<tr>
<td align="left">空间名称</td>
<td align="left">创建存储桶时自定义的存储桶名称，例如examplebucket-1250000000</td>
</tr>
<tr>
<td align="left">访问域名</td>
<td align="left">指 COS 的默认存储桶域名，用户在创建存储桶时，由系统根据存储桶名称和地域自动生成。不同地域的存储桶有不同的默认域名。您可以前往 <a href="https://console.cloud.tencent.com/cos5">对象存储控制台</a> ，在存储桶的<strong>概览 > 域名信息</strong>中查看</td>
</tr>
<tr>
<td align="left">自动重命名</td>
<td align="left">文件上传到 COS 后自动重命名，避免与已有同名文件相冲突，可按照指定格式重命名</td>
</tr>
<tr>
<td align="left">不在本地保存</td>
<td align="left">开启后，不会在本地保留源文件，建议不开启</td>
</tr>
<tr>
<td align="left">禁止缩略图</td>
<td align="left">开启后不会上传对应的缩略图文件，建议不开启</td>
</tr>
<tr>
<td align="left">数据万象</td>
<td align="left">开启数据万象服务，可对图片进行编辑、压缩、转换格式、添加水印等操作，详情可参见 <a href="https://cloud.tencent.com/product/ci">数据万象产品介绍</a></td>
</tr>
<tr>
<td align="left">调试</td>
<td align="left">记录错误、异常和警告信息，可选择开启</td>
</tr>
</tbody></table>
2. 配置完成后，单击**保存配置**即可。
3. 上传一个新文件进行测试，查看附件详情，查看附件图片的 URL，确认附件图片的 URL 指向腾讯云 COS。
![](https://main.qcloudimg.com/raw/eec09d6877cf0d573a6522146418eea2.png)
>? 如果以上测试成功，那么接下来需要同步旧资源到 COS 存储桶中（可使用 [COSCMD 工具](https://cloud.tencent.com/document/product/436/10976) 或者 [COS Migration 工具](https://cloud.tencent.com/document/product/436/15392)），**否则后台无法正常预览旧资源**。同步完成以后，可以开启回源设置，可参考下文的 [设置回源](#1)。
>

## 扩展

1. 使用 CDN 加速访问
存储桶如果需要配置 CDN 加速，可参见 [CDN 加速配置](https://cloud.tencent.com/document/product/436/18670) 文档。在插件设置中将 URL 前缀修改为默认 CDN 加速域名或自定义加速域名即可。
2. 替换数据库中的资源地址
如果不是新创建的站点，数据库当中必定是旧的资源链接地址，我们需要将资源地址进行替换，插件提供了替换功能，请在首次替换前记得备份。
 - 旧域名填写原资源域名，例如`https://example.com/`
 - 新域名填写现在的资源域名，例如`https://img.example.com/`
3. 设置跨域访问
在文章中引用对应的资源链接，控制台会提示跨域的错误`No 'Access-Control-Allow-Origin' header is present on the requested resource`。原因是没有添加 header。您需要在跨域访问 CORS 设置中添加 HTTP Header 配置。下面提供两种途径进行配置：
 - 在 COS 控制台上配置
![](https://main.qcloudimg.com/raw/ec11051c0737ca9b66710d368106cbd6.png)
>? 关于跨域配置操作步骤，请参见 [设置跨域访问](https://cloud.tencent.com/document/product/436/13318) 文档。
>
 - 在 CDN 控制台上配置
    - 如允许所有域名，则配置如下：
```plaintext
Access-Control-Allow-Origin: *
```
    - 只允许您个人的域名访问，则配置如下：
```plaintext
Access-Control-Allow-Origin: https://example.com
```
<span id=1></span>
4. 设置回源
如果您不在 WordPress 后台媒体库中上传资源，建议开启回源设置，详细步骤请参见 [设置回源](https://cloud.tencent.com/document/product/436/13310) 文档。
开启回源设置后，当客户端首次访问 COS 源文件时，COS 发现无法命中对象，对客户端返回 302 HTTP 状态码并跳转至回源地址对应的地址，此时对象由源站提供给客户端，从而保证访问。同时 COS 从源站复制该文件并保存至存储桶对应的目录中；第二次访问时，COS 直接命中对象并返回给客户端。

