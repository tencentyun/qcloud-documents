## 前言
平时写博客记笔记大都是使用 Markdown 编辑器 ，插入图片时默认保存在电脑本地磁盘。如果需要在多个平台上发布文章，就要分别多次上传图片，非常繁琐。所以需要一种更好的图片管理方案，就是使用图床服务。将图片文件上传到图床并得到一个 URL 地址，就可以方便的分享图片了。

市面上有一些免费的图床服务。如果仅仅是临时分享，可以使用。如果有大量的图片资源需要保存，最好还是购买图床服务，或者自建图床。本文将以腾讯云对象存储 COS 为例，结合 PicGo，演示如何搭建一个属于自己的图床服务。

## 环境准备
- PicGo：用于压缩、上传图片。
- 腾讯云对象存储 COS：用于存储图片并提供在线访问。

## 操作步骤
### 安装 PicGo
- PicGo 是一个用于快速上传图片并获取图片 URL 链接的工具，支持腾讯云COS、七牛图床、Github 图床、又拍云图床等。
- 我们以 Windows 为例，首先访问 Github 仓库去 [下载](https://github.com/Molunerfinn/PicGo/releases) 客户端安装包，找到 2.3.0 正式版，找到对应平台的安装包，单击下载。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0055fd83ed41dbc2880cf8f7e0de9ae8.jfif)
- 下载完成之后，正常安装即可。 

### 安装 webp 插件
- PicGo 有一系列好用的插件，帮助扩展功能，例如压缩图片、添加水印等等。本文将以 **webp** 插件为例，演示如何在 PicGo 中使用插件。
- webp 插件会在图片上传前将图片转为 .webp 格式，它相比于传统的 .jpg、.png 等格式，同等体积质量更高，同等质量体积更小。图片经过压缩之后再上传至 COS，对于节省存储空间，节省流量都很有帮助。如果对图片格式有特殊要求，不希望转换格式，可以省略这一步。
- 打开 PicGo，进入**插件设置**，在搜索栏输入插件名字即可搜索并安装，非常方便。如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/f8b7b3956b4d61fbcde451a899c3e04d.jfif)

## COS 对象存储
- COS（Cloud Object Storage，对象存储）是由腾讯云推出的一种分布式存储服务。它的特点是无目录层次结构、无数据格式限制，可容纳海量数据，支持 HTTP/HTTPS 协议访问。
- 腾讯云 COS 的存储桶空间无容量上限，无需分区管理，适用于 CDN 数据分发、[数据万象](https://cloud.tencent.com/product/ci?from=10680) 处理或大数据计算与分析的数据湖等多种场景。
- 对于 [实名认证](https://cloud.tencent.com/solution/face-recognition?from=10680) 的新用户，腾讯云 COS 提供了六个月的**免费体验服务**（50GB 存储空间），[单击此处访问](https://cloud.tencent.com/act/free?from=10680)。
![](https://qcloudimg.tencent-cloud.cn/raw/15751362b0e98d8e7fd10300afba81be.jfif)


### 开通 COS
官网提供了非常友好的新手引导服务，可根据引导快捷开通和使用存储服务。
![](https://qcloudimg.tencent-cloud.cn/raw/fcfcc1c5b3e955ed431591365b9d33d1.jfif)
### 创建存储桶
1. 按需要填写各项即可，需要注意的地方是访问权限的选择，默认是**私有读写**，适合**存储隐私机密文件**；本文选择了**公有读私有写**，是因为这个存储桶主要是做图床服务，用来**存储图片，并能对外提供公开访问**。
![](https://qcloudimg.tencent-cloud.cn/raw/7938b0bfd221b3a88fb4640a7fd06387.jfif)
2. 单击**下一步**创建即可。
3. 创建成功后，来到**存储桶列表**，记录下**存储桶名称**，和**所属地域**的代号，如图示例，也就是 ap-beijing。
![](https://qcloudimg.tencent-cloud.cn/raw/61a91029c34f2e222903ab063570fbee.jfif)

### 创建 API 密钥
1. 进入 **访问管理** - **访问密钥** - [**API 密钥管理**](https://console.cloud.tencent.com/cam/capi)，会提示是否使用子账号管理，可根据实际需要进行选择，这里我们直接使用主账号进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/ed5a357845ffbc36919919ee3ba4ba2a.jfif)
2. 创建成功，将 **APPID**，**SecretId**，**SecretKey** 保存下来，非常重要，谨防外泄。
![](https://qcloudimg.tencent-cloud.cn/raw/2028b6934b743d007b781e1df51fb386.jfif)
### 答题领流量
新手有一次答题 [领取流量](https://console.cloud.tencent.com/cos) 的机会。题目很简单，全部回答正确以后，可以免费领取3个月的流量包。
![](https://qcloudimg.tencent-cloud.cn/raw/3962bf73ccc45e08c9b66a7257d1dbd0.jfif)

## 配置 PicGo 图床服务
1. 打开安装好的 PicGo 客户端，进入**图床设置** - **腾讯云 COS**，将上面保存的内容填写到配置中：
![](https://qcloudimg.tencent-cloud.cn/raw/24357488e9042eab84699e4085779176.jfif)
2. 存储路径，也就是图片上传后在存储桶内的目录结构，可根据需要填写。如果填写，存储桶会自动创建出对应的目录结构。注意要以 / 结尾。然后单击**确定**，并**设为默认图床**。
3. 进入**PicGo 设置**，将**上传前重命名**、**时间戳重命名**打开，这样可以防止图片重名。
![](https://qcloudimg.tencent-cloud.cn/raw/240e185c08ee5cd83b91bf5fa630d393.jfif)

## 测试
1. 打开 PicGo 上传区，选择本地的一张图片，然后上传。上传前会自动根据时间戳进行重命名，也可以自己修改：
![](https://qcloudimg.tencent-cloud.cn/raw/42b703bce00f7372e09f245dd095b024.jfif)
2. 单击**确定**，图片就会进行上传了。
3. PicGo 的相册功能，会展示已经上传的图片，并提供了复制图片 url，编辑图片 url 和移除相册的基础操作。需要注意的是，仅仅是删除本地的数据，云端的图片不会受影响。
![](https://qcloudimg.tencent-cloud.cn/raw/ebb42a8dc7749cc1afb31337685ddbdc.jfif)
4. 来到 [腾讯云 COS 控制台](https://console.cloud.tencent.com/cos5)，进入对应的存储桶中，可以发现图片已经上传成功了：
![](https://qcloudimg.tencent-cloud.cn/raw/80b8da463adfb89ccae1ba5f0f43b38d.jfif)
5. 存储桶内的每个文件都会有一个唯一的访问地址，单击**详情**查看：
![](https://qcloudimg.tencent-cloud.cn/raw/6bd850708beb5bb1a15b0ab682a2d662.png)
使用图床：在 Typora 粘贴图片时自动上传。
打开 Typora ，进入**文件**- **偏好设置**- **图像设置**，进行三个设置：
 1. 插入图片时，执行**上传图片**操作
 2. 上传服务采用 **PicGo(app)**
 3. 设置 PicGo 程序的安装**路径**
![](https://qcloudimg.tencent-cloud.cn/raw/b5083516ccfe46410c188fa3bdd91c25.jfif)

之后，当我们使用 typora 编写 md 文档，在插入图片时，会自动唤起 PicGo 客户端，并上传图片到目标平台。
