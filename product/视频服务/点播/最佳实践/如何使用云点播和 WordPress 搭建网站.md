## 简介

WordPress 是一款著名的开源博客框架和内容管理系统，使用它可以极大的降低开发者建站的难度，提高建站效率。使用 WordPress 提供的默认方案可以让一个小型的网站在几分钟的时间就运行起来，但随着网站的持续运营，图片和音视频等媒体文件的访问速度以及它们给服务器带来的带宽和存储量的增涨就会让您的站点开始表现得难堪重负。如何妥善地安置这些网站中举足轻重的媒体文件，是一个站点想要长期运营无法绕开的问题。

### 建站为何要使用云点播

使用 WordPress 默认方案搭建的网站之所以不利于长期运营，主要原因在于媒体文件是直接存放在站点的服务器上，它将带来以下问题：
<table selecttype="cells" ><colgroup><col  ><col  ></colgroup>
<tbody>
<tr  ><th style="width:10px">序号</td>
<th>详情</td>
</tr>
<tr  ><td>1</td>
<td>通过网页直接访问服务器上的媒体文件，容易出现视频卡顿和图片加载缓慢的现象。</td>
</tr>
<tr  ><td>2</td>
<td>通过网站访问媒体文件会占服务器的带宽，且很容易把带宽占满。</td>
</tr>
<tr  ><td>3</td>
<td>媒体文件的体积一般都比较大，随着网站内容不断丰富，很容易把服务器的存储空间占满。</td>
</tr>
<tr  ><td>4</td>
<td>站点服务器迁移时，媒体文件迁移困难。</td>
</tr>
</tbody>
</table>

云点播是一款为音视频和图片等媒体提供存储、转码和加速分发播放等能力的云服务，它可为您建站提供以下帮助：
<table selecttype="cells" ><colgroup><col  ><col  ></colgroup>
<tbody>
<tr  ><th style="width:10px">序号</td>
<th>详情</td>
</tr>
<tr  ><td>1</td>
<td>上传和存储。您可以使用我们提供的插件或 SDK 将文件上传到云点播，不再占用服务器的存储空间，且避免了服务器迁移、文件误删等问题。</td>
</tr>
<tr  ><td>2</td>
<td>加速访问。云点播会为您提供文件的 CDN 地址，访问音视频和图像时不再出现卡顿现象，且不占用服务器带宽。</td>
</tr>
</tbody>
</table>


除此之外，点播还提供访问控制、媒体处理和智能审核等能力，详情请参见云点播的 [功能概述](https://cloud.tencent.com/document/product/266/78037)。

### 云点播的 WordPress 插件

云点播提供了 [WordPress 插件](https://wordpress.org/plugins/tencentcloud-vod/)，您只需安装该插件，并通过简单的配置关联您的 [云点播子应用](https://cloud.tencent.com/document/product/266/14574)，即可将 WordPress 上的媒体文件托管到云点播上，并在您的网站中通过点播提供的 CDN 地址访问您的文件。该插件目前具有以下功能：

- 绑定云点播子应用。
- 在 WordPress 的管理端上传视频文件，可自动上传至云点播的子应用下。
- 在文章或页面上插入视频时，将自动使用云点播上的视频地址。

## 准备工作
### 1. 创建点播子应用

点播子应用可帮助您实现资源隔离，例如您可将不同站点的媒体文件划分到不同的子应用下，单独管理。创建方法详见 [开通子应用](https://cloud.tencent.com/document/product/266/14574#.E5.BC.80.E9.80.9A.E5.AD.90.E5.BA.94.E7.94.A8)。

### 2. 搭建 WordPress 网站
您可以根据实际情况选择一种方案来搭建 WordPress 网站：
<dx-tabs>
::: 方案一（推荐）
使用腾讯云轻量应用服务器或云服务器的 WordPress 应用镜像快速建站，详情见 [轻量应用服务器文档](https://cloud.tencent.com/document/product/1207/45117) 或 [云服务器文档](https://cloud.tencent.com/document/product/213/9740)。
:::
::: 方案二
在宝塔 Linux 面板的软件商店中，通过一键部署安装 WordPress，详情如下图：（仅服务器已 [安装宝塔面板](https://cloud.tencent.com/document/product/213/45550) 时推荐）。

![宝塔面板安装 WordPress](https://qcloudimg.tencent-cloud.cn/raw/47487a10474f6b3e49971cd0e8814fbc.png)
:::
::: 方案三
可在 [WordPress 官网](https://cn.wordpress.org/download/) 下载 WordPress 最新版，并参见 [官方安装指南](https://wordpress.org/support/article/how-to-install-wordpress/) 手动安装。
:::
</dx-tabs>


## 操作步骤

### 步骤1：安装插件

您可单击 [下载链接](https://github.com/Tencent-Cloud-Plugins/tencentcloud-wordpress-plugin-vod/releases/latest/download/tencentcloud-wordpress-plugin-vod.zip) 获取最新版插件的压缩包，然后在 WordPress 管理台的左侧边栏单击 **安装插件 > 上传插件 > 选择文件 > 立即安装 > 启用插件。**
![手动安装](https://qcloudimg.tencent-cloud.cn/raw/4577370365903872db3a97dfd02a032b.png)

### 步骤2：配置插件

如下图所示，单击 WordPress 左侧导航栏 **腾讯云设置 > [云点播](https://cloud.tencent.com/document/product/266/36702)**，可对点播插件进行配置。
![](https://qcloudimg.tencent-cloud.cn/raw/816b6e024800b7004ec0a32fa3ea86c1.png)

配置说明见下表：

| **配置项**           | **说明**                                                     |
| -------------------- | ------------------------------------------------------------ |
| 自定义密钥           | 不开启该选项时，插件会使用**腾讯云设置**中配置的密钥，即与其它腾讯云插件共用同一个密钥。开启该选项时，则会使用下方指定的密钥。 |
| SecretId、SecretKey  | 访问密钥信息，可前往 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中创建和获取。 |
| SubAppID             | 云点播的子应用 ID，填上准备工作中创建的子应用 ID 即可，也可在点播 [应用管理](https://console.cloud.tencent.com/vod/app-manage)中查询到。 |
| 是否开启转自适应码流 | 开启后，会在上传时对视频进行转自适应码流。详情见点播 [自适应码流](https://cloud.tencent.com/document/product/266/78292)。 |

配置完成后，单击 **保存设置** 即可。

### 步骤3：上传并使用点播视频
1. 开启并配置好点播插件后，在媒资库和编辑文章或页面时上传的视频文件，就会自动上传到云点播。
2. 以编辑文章时上传为例，如下图所示，在文章中插入“视频区块”，然后单击**上传**，选择视频文件并上传。接着单击文章右上角的**预览**查看文章的预览页面，通过检查视频的网址可以发现，此时使用的已经是云点播上的视频了。
![](https://qcloudimg.tencent-cloud.cn/raw/bc0511fddb87e5ad58d4e4d0c9d4f57b.png)
3. 如下图所示，左侧使用的是服务器上的视频，而右侧使了云点播。播放服务器上的本地视频会因为带宽限制和没有 CDN 加速服务而频繁卡顿，使用云点播则可以轻松地解决这些问题。
![](https://qcloudimg.tencent-cloud.cn/raw/002da7734ac65e618732036d234bf07c.gif)

## 扩展
### 使用 HTTPS

云点播默认使用 HTTP 协议，若需使用 HTTPS 可在云点播控制台选择该子应用，然后打开 **系统设置 > 分发播放设置 > 默认分发配置**，即可将**默认分发协议类型**修改为 HTTPS。
