## 简介

图床服务提供图片存储、图片加工处理、图片全网分发等功能，为全球无数的博客网站和社区论坛提供了后端图片服务支撑。开发者们可以使用腾讯云**对象存储（Cloud Object Storage，COS）**搭建图床服务，COS 是腾讯云提供的一种存储海量文件的分布式存储服务，提供了更丰富的功能、更优越的性能、更高的可靠性保障。

COS 用于图床场景的优势有：

- **低成本：**存储单价低，按量付费，用多少算多少，还有资源包优惠。
- **不限速：**上传下载不限速，不再长时间等待 loading，访问质量也更好。
- **高可用：**有高等级的 SLA 可用性保障，存储的数据有高达99.9999999999%的持久性保障。
- **容量无限：**文件分布式存储，支持海量文件，容量按需使用。


## 实践场景

### 场景1：新增图片使用 COS 搭建图床服务

本场景使用到以下工具：
- PicGo：一款支持多种云存储配置、快捷生成图片链接的工具。
- Typora：一款轻量级 Markdown 编辑器，支持多种输出格式，支持将本地图片一键上传至图床。

### 操作步骤

1. 安装 PicGo 并设置腾讯云 COS 服务相关参数。
>?本次实践使用的是 PicGo 2.3.1版本，其他版本的配置过程可能存在一定差异，请注意相应调整。
>
在 [PicGo 官网](https://molunerfinn.com/PicGo/) 下载和安装 PicGo 后，在图床设置里找到**腾讯云 COS**，并配置以下相关参数项：
![](https://qcloudimg.tencent-cloud.cn/raw/aa84aa3d715bf44b050c8b51625bf02a.png)
  - COS 版本：选择 COS v5。
  - 设定 Secretld：开发者拥有的项目身份识别 ID，用于身份认证，可在 [API 密钥管理](https://console.cloud.tencent.com/capi) 页面中创建和获取。
  - 设定 SecretKey：开发者拥有的项目身份密钥，可在 [API 密钥管理](https://console.cloud.tencent.com/capi) 页面获取。  
  - 设定 Bucket：存储桶，COS 中用于存储数据的容器。有关存储桶的进一步说明，请参见 [存储桶概述](https://cloud.tencent.com/document/product/436/13312) 文档。
  - 设定 AppId：开发者访问 COS 服务时拥有的用户维度唯一资源标识，用以标识资源，可在 [API 密钥管理](https://console.cloud.tencent.com/capi) 页面获取。
  - 设定存储区域：存储桶所属地域信息，枚举值可参见 [可用地域](https://cloud.tencent.com/document/product/436/6224) 文档，例如 ap-beijing、ap-hongkong、eu-frankfurt 等。
  - 设定存储路径：图片存放到 COS 存储桶中的路径。
  - 设定自定义域名：可选，若您为上方的存储空间配置了自定义源站域名，则可填写。相关介绍可参见 [开启自定义源站域名](https://cloud.tencent.com/document/product/436/36638)。
  - 设定网址后缀：通过在网址后缀添加 COS 数据处理参数实现图片压缩、裁剪、格式转换等操作，相关介绍可参见 [图片处理](https://cloud.tencent.com/document/product/436/54049)。
2. 设置 typora（可选）。
>?如果您的编辑需求不是 Markdown 场景，可以忽略此步骤，仅使用上一步安装的 PicGo 作为图床工具。
>
设置指引如下：
 1. 在 typora 的偏好设置的**图像**中，进行如下配置：
![](https://qcloudimg.tencent-cloud.cn/raw/1586e34dc075d04f55fcb7a483923b09.png)
    - 在**插入图片时**，选择**上传图片**。
    - 在**上传服务设定**，选择 **PicGo(app)**，并设置刚才安装的 PicGo.exe 位置。
 2. 重启 typora，使设置生效。
 3. 进入 typora 编辑器区域，直接拖放或粘贴图片，即可上传图片并自动替换为 COS 文件链接。（如果粘贴后没有自动替换为 COS 链接，可以检查 PicGo 中的 server 设置是否已打开）。
![](https://qcloudimg.tencent-cloud.cn/raw/607852baa13b0e9b201857668059a8e3.png)


### 场景2：将原图床仓库图片快速迁移到腾讯云 COS

以某图床服务举例，您可以找到本地图床文件夹，或从线上下载完整文件夹，并将文件夹中所有图片转存到 COS 存储桶。最后再统一替换链接域名即可恢复网站。

### 操作步骤

#### 步骤1：下载原图床服务的图片

登录原图床网站页面，下载此前已上传的图片文件夹。

#### 步骤2：创建 COS 存储桶并设置防盗链

1. 注册腾讯云账号，创建一个访问权限为**公有读私有写**的存储桶，操作指引请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。
2. 创建存储桶后，在存储桶里打开防盗链设置，避免图片被盗刷，操作指引请参见 [设置防盗链](https://cloud.tencent.com/document/product/436/13319)。

#### 步骤3：上传文件夹到存储桶

在刚才已创建的存储桶里，单击上传文件夹，将刚才准备好的图片文件夹，上传到 COS 存储桶。
>?如果图片数量较多，还可以使用 [COSBrowser 客户端](https://cloud.tencent.com/document/product/436/11366) 快速上传图片。
>
![](https://qcloudimg.tencent-cloud.cn/raw/9255b169bf3bc8a41197c091133ce162.png)


#### 步骤4：全局替换链接域名

在 COS 控制台存储桶概览页，复制存储桶默认域名（也可以绑定自定义 CDN 加速域名）。使用常用代码编辑器，对项目全局搜索替换失效链接前缀为 COS 存储桶默认域名。
>?关于默认域名的说明，请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。

- vscode 搜索替换示例：
![](https://qcloudimg.tencent-cloud.cn/raw/3311b14556e9f794631a890f2a96056e.png)

- sublime text 搜索替换示例：
![](https://qcloudimg.tencent-cloud.cn/raw/d0d096590d44ed8e05c967fb0cbd41c1.png)



## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击“[此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406)”一键启动，立即使用！


