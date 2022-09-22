## 简介
[Typecho](https://typecho.org/) 是一个基于 PHP 的开源博客平台。本文主要介绍如何使用插件实现远程附件功能，将 Typecho 的媒体库附件存储在腾讯云 [对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/product/cos) 上。


## 前提条件
1. 已有 COS 存储桶。如无，可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 操作指引。
2. 已创建服务器。例如云服务器 CVM。相关指引可参见 [CVM 产品文档](https://cloud.tencent.com/document/product/213)。




## 实践步骤

### 安装 Typecho
1. 您可以在 [Typecho 官方页面](http://typecho.org/download) 下载 Typecho 的最新版并查看安装指南。您也可以通过宝塔面板安装。宝塔面板安装指引请参见 [宝塔官网](https://www.bt.cn/)。下面以宝塔安装 Typecho 为例。
2. 宝塔安装后，添加站点，并配置相关参数，输入服务器的域名 IP、根目录、FTP 账号、数据库账号等。
![](https://qcloudimg.tencent-cloud.cn/raw/d2f1041e87750e292f7d0128f90fd5a7.png)
3. 站点创建完成后，进入站点。
4. 单击**文件**导航栏，在文件页面中单击**远程下载**，填入 Typecho 的 GitHub 源码地址：`https://github.com/typecho/typecho/releases/latest/download/typecho.zip`，然后单击**确认**。
![](https://qcloudimg.tencent-cloud.cn/raw/be8318b9ad5ffebb8a8955ff46009638.png)
5. Typecho 源码文件下载后，并完成解压，然后通过浏览器访问链接`http://43.xxx.xxx.132/install.php`（使用时请替换为自己的站点 IP），根据页面提示，即可完成 Typecho 的安装。

### 安装 COS 插件
1. 执行以下命令下载插件：
```
git clone https://github.com/cnhongv/typecho-cos-plugin
```
2. 复制 TypechoCosPlugin 文件夹到 Typecho 安装路径 /usr/plugins/ 内。
3. 在 Typecho 的后台页面启用插件。
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
<img style="width:700px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/bcd04f122386c569cfeac1779572dab9.png" />
 - 高级设置（可选）
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
<img style="width:700px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/d18236891f7b60bcb21915949f5d975c.png" />
5. 完成以上设置后，即可完成博客系统的搭建。

