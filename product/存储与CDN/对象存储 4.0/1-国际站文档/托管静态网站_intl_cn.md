在此实践中，用户可以在腾讯云对象存储（以下简称 COS）上托管静态网站，访客可以通过自定义域名（例如 www.example.com ）访问托管的静态网站。无论您是想在 COS 上托管已有静态网站还是从零开始建站，此实践可帮助您在 COS 上托管静态网站。以下是具体步骤：

**步骤预览**
![流程图](//mc.qcloudimg.com/static/img/33e1c857baf9bf191b1b668ae3c1f514/image.png)
## 事前准备
以下是实践过程中，将会用到的相关服务：

**域名注册**：如果还未注册域名，则需要先注册一个域名，例如 www.example.com 。可通过腾讯云 [域名注册](https://dnspod.cloud.tencent.com/?from=qcloud) 申请域名。通常，只需少量费用，即可拥有一个域名。

**COS**：您将使用 COS 创建存储桶 ，配置权限以允许每个人查看内容，然后上传网页内容。

**内容分发网络**：内容分发网络（以下简称 CDN）和云解析服务将共同作用，使域名和网站内容绑定，同时为静态网站加速，降低访问延迟，提高可用性。

**云解析**：利用云解析，可将域名和网站内容绑定在一起，实现使用自定义域名访问静态网站的目的。

> 本指南中的所有步骤都使用`www.example.com` 作为示例域名。实际操作中请使用您的自有域名替换此域名。

## 一、注册域名与备案
域名注册是在互联网上建立任何服务的基础。注册域名之后，还需要进行备案，网站才能正常访问。请根据您的具体情况进行操作：
- 已注册域名并备案，可跳过本步骤，进行 [步骤二](#创建存储桶)。
- 已注册域名但未备案，请进行 [域名备案](https://cloud.tencent.com/product/ba)。
- 未注册域名，请先 [注册域名](https://dnspod.cloud.tencent.com/?from=qcloud)，再进行 [域名备案](https://cloud.tencent.com/product/ba)。

<span id="创建存储桶"></span>
## 二、创建存储桶并上传内容
在完成域名注册及备案后，您需要在 COS 控制台中执行以下任务，以创建和配置网站内容：
2.1 为您的网站内容创建存储桶。
2.2 配置存储桶并上传内容。

### 2.1 创建存储桶
请使用腾讯云账号登陆[ COS 控制台](https://console.cloud.tencent.com/cos4)，为您的网站创建相应的存储桶。存储桶在 COS 中用于存储数据，您可以将网站内容存储在一个存储桶中。可通过 COS 概览页或 Bucket 列表快速创建存储桶，详细设置可参考 [创建存储桶](https://cloud.tencent.com/document/product/436/6232)：
-  **通过概览页**
 1. 登录对象存储控制台后，当您首次创建存储桶时，请单击概览页上的【创建 Bucket】，弹出创建 Bucket 对话框。
![概览页](//mc.qcloudimg.com/static/img/598d047d08b5f990e0efe0943b3bf74d/image.png)
 2. 请填写存储桶名称（如 example），选定存储桶所属地域（请参阅 [可用地域](https://cloud.tencent.com/document/product/436/6224)），点击【确定】即可快速创建一个存储桶。
![创建Bucket3](//mc.qcloudimg.com/static/img/c092210dcbeb9781297bfdd3a2306521/image.png)

- **通过 Bucket 列表** 
 1. 登录对象存储控制台后，请点击左侧导航【 Bucket 列表】，进入 Bucket 列表。
![bucket列表](//mc.qcloudimg.com/static/img/915383ea2a680d7b09088579ee4ac021/image.png)
 2. 单击【+ 创建 Bucket】，弹出创建 Bucket 对话框。
 3. 请填写存储桶名称（如 example），选定存储桶所属地域（请参阅 [可用地域](https://cloud.tencent.com/document/product/436/6224)），点击【确定】即可快速创建一个存储桶。
![创建Bucket3](//mc.qcloudimg.com/static/img/c092210dcbeb9781297bfdd3a2306521/image.png)


### 2.2 配置存储桶并上传内容
1. 将存储桶的访问权限设置为**公有读私有写**，使网站内容可被公开访问。
 1. 在 COS 控制台，单击已创建好的存储桶。
 2. 进入存储桶后，单击【基础配置】>基本信息的【编辑】按钮。
 3. 修改存储桶的访问权限为公有读私有写，保存即可。
![权限修改](//mc.qcloudimg.com/static/img/dbe9b445af96bb13b6b84598b68a56e9/image.png)
2. 将您的网站内容上传到已创建好的存储桶。
单击【文件列表】，在文件列表页面上传网站内容。详细说明请参考 [上传对象](https://cloud.tencent.com/document/product/436/6233)。
![upload](//mc.qcloudimg.com/static/img/6dcf9bd44e00b393555c5f683f7544da/image.png)

> 公有读私有写：任何人（包括匿名访问者）都对该存储桶中的对象有读权限，但只有存储桶创建者及有相应权限的账号才对该存储桶中的对象有写权限。
私有读写：只有该存储桶的创建者及有相应权限的账号才对该存储桶中的文件有读写权限，其他任何人对该存储桶中的对象都没有读写权限。

在存储桶中托管的内容可以是文本文件、照片、视频——任何您想要托管的内容。如果还未构建网站，则只需为此实践创建一个文件。
例如，您可使用以下 HTML 创建文件，并将其上传到存储桶。网站主页的文件名通常为 index.html。在后续步骤中，您将提供此文件作为网站的索引文档。
```
<!DOCTYPE html>
<html>
    <head>
        <title>Hello COS!</title>
        <meta charset="utf-8">
    </head>
    <body>
        <p>欢迎使用&nbspCOS&nbsp的静态网站功能。</p>
        <p>这是首页！</p>
    </body>
</html>
```
> 开启静态网站功能后，当用户访问任何不带文件指向的一级目录时，COS 默认优先匹配对应存储桶目录下 index.html，其次为 index.htm，若无此文件，则返回 404。

##  三、绑定自定义域名
> 用户只有绑定自定义域名并开启静态网站功能后，才可以直接在浏览器中打开资源。使用默认提供的域名（CDN 加速域名和 COS 默认域名）访问资源时将始终弹出下载框。

可设置自定义域名直接指向存储桶，并开通静态网站功能，达到通过浏览器直接访问网站的目的（存储桶中的内容）。同时为降低网站访问延迟，提高可用性。在此实践中，在绑定自定义域名的同时，为自定义域名开启 CDN 加速（不开启 CDN 加速的配置请参考 [域名管理-配置自定义域名](https://cloud.tencent.com/document/product/436/6252#.E9.85.8D.E7.BD.AE.E8.87.AA.E5.AE.9A.E4.B9.89.E5.9F.9F.E5.90.8D)），使网站访客获取更好的浏览体验。
### 3.1 域名添加
在进行自定义域名添加时，有两种途径供您选择：
- [通过 CDN 控制台添加](#通过CDN控制台)
- [通过 COS 控制台添加](#通过COS控制台)

如果您想在添加自定义域名的同时，进行 CDN 高级管理和配置，可优先选择 CDN 控制台添加域名。本实践中不涉及 CDN 高级管理和配置，如需帮助，请参考 [CDN 配置管理](https://cloud.tencent.com/document/product/228/6288)。
如果您只需要先添加自定义域名，不进行其他配置，COS 控制台添加将节省时间。
<span id="通过CDN控制台"></span>
- **通过 CDN 控制台添加** 
 1. 请登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，从左侧导航进入域名管理页面。
 2. 单击【+添加域名】，进入域名配置界面。
![CDN 添加1](//mc.qcloudimg.com/static/img/d8738549ff278dde2702e3e2414240db/image.png)
 3. 请输入自有域名，源站类型选择**对象存储（COS ）**，并为源站选择托管网站内容的对应存储桶默认域名。业务类型选择静态加速，其他保持默认配置，提交即可。
![CDN添加2](//mc.qcloudimg.com/static/img/83505f18ad572e90c40d1f1e7bc24e90/image.png)
 4. 域名添加完成。
     1. 请关闭弹窗，耐心等待域名配置下发至全网节点（约 15 分钟）。
![CDN添加3](//mc.qcloudimg.com/static/img/9ed0be361b2cd3bde8a0e4b557dafaba/image.png)
     2. 获取系统分配的 CNAME 记录，再进行步骤 3.2。
![CDN添加4](//mc.qcloudimg.com/static/img/3922bf529760e262316381936e40e26c/image.png)

<span id="通过COS控制台"></span>
- **通过 COS 控制台添加**
 1. 登录 [COS 控制台](https://console.cloud.tencent.com/cos4/index) ，进入左侧菜单栏【 Bucket 列表】，单击存储网站内容的存储桶（如 example），进入存储桶。
![COS添加域名1](//mc.qcloudimg.com/static/img/d9334338a1fb26670997ca716500a5a6/image.png)
 2. 单击【域名管理】，进入域名管理页面，单击自定义域名下的【+ 添加域名】按钮，进入可配置状态。
 3. 输入待绑定的自定义域名（如 www.example.com ），选择开启 CDN 加速，单击【保存】即可完成添加。
![域名管理6](//mc.qcloudimg.com/static/img/0f961cc797d90a2d59ce73c1d688385a/image.png)
 4. 请稍等几分钟，等待域名上线。获取对应的 CNAME 记录，再进行步骤 3.2。
![COS添加域名3](//mc.qcloudimg.com/static/img/6950a8955b4544e33bb9a4a5b05924c6/image.png)

### 3.2 域名解析
1. 添加自定义域名后，还需进行域名解析。请登录 [域名管理控制台](https://console.cloud.tencent.com/cns/domains)，单击左侧菜单栏【云解析】>【一级域名】，进入一级域名菜单。单击【+添加域名】，弹出添加域名对话框。
![域名管理7](//mc.qcloudimg.com/static/img/6ac3a93bda882224cbd6c2f591397042/image.png)
2. 输入自定义域名，选择所属项目，单击【确定】保存即可。
![域名管理8](//mc.qcloudimg.com/static/img/8364ae1f871077a2755c4ea9c8071041/image.png)
3. 域名添加成功后，点击域名，进入解析记录管理页面。单击【+ 添加记录】，弹出添加记录对话框。
![域名管理9](//mc.qcloudimg.com/static/img/34997fe3c0fa5ccf275997ae6a63a0bd/image.png)
4. 记录类型选择 CNAME，主机记录留空，线路类型选择默认，填入 [步骤 3](#步骤3) 获取的 CNAME 记录，TTL 保持默认，单击【确定】保存即可。完成解析添加后，大约需 15 分钟左右生效，请耐心等待。
![域名管理10](//mc.qcloudimg.com/static/img/8d0fdde4ff83ae50fdfea421935dc93d/image.png)

## 四、设置静态网站托管
将网站内容与自定义域名绑定之后，需要开启 COS 的静态网站功能，才能通过浏览器直接访问网站内容。具体步骤如下：
1. 登录 [ COS 控制台](https://console.cloud.tencent.com/cos4/index) ，进入左侧菜单栏【 Bucket 列表】，单击存储网站内容的存储桶（如 example），进入存储桶。
  ![访问权限1](//mc.qcloudimg.com/static/img/b51d5a77d53c3416324ea3eb283c788c/image.png)
2. 单击【基础配置】，找到静态网站设置，单击【编辑】按钮，进入可编辑状态。
  ![静态网站1](//mc.qcloudimg.com/static/img/682188854dabd038d34a452569feefa3/image.png)
3. 修改当前状态为开启，开启 Index 索引，开启指定的 Http 状态码并设置指向文件（可选），设置完成单击【保存】即可。
![开通静态网站托管](//mc.qcloudimg.com/static/img/ac355b7e26479983790382c25c0ecb42/image.png)

> 静态网站设置的具体配置及相关参数说明，请参考 [静态网站设置](https://cloud.tencent.com/document/product/436/6249)。

## 五、测试验证
在完成上述步骤后，可通过在浏览器地址栏输入网站域名进行访问，来验证实践结果，以 `www.example.com` 为例：

- `http://www.example.com` ——返回名为 example 的存储桶中的索引页面（index.html）。
- `http://www.example.com/test.html`（不存在的文件） ——返回名为 example 的存储桶中的 404 文档（error.html）。

> 在某些情况下，您可能需要清除缓存才能看到预期结果。
