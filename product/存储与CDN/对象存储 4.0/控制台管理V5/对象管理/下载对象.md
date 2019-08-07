## 简介
您可以通过对象存储控制台，对存储桶中的已有对象进行下载操作，可通过控制台下载单个对象或通过 COSBrowser 工具批量下载对象。

## 前提条件
下载对象前，请您确保存储桶中已存在对象。如未上传对象，请先参见 [上传对象](https://cloud.tencent.com/document/product/436/13321) 文档进行操作。

## 下载单个对象
#### 操作步骤
1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)，单击【存储桶列表】，进入存储桶列表页。找到对象所在的存储桶，单击其存储桶名称，进入存储桶管理页。
   ![](https://main.qcloudimg.com/raw/46f3f6bcf85a1ca8f16a2f47479d0ef8.jpg)
2. 在“文件列表”页签下，找到需要下载的对象，如您只需下载单个对象，您有三种方式可选：
 1. 在所选的对象右侧直接单击【下载】即可下载。
![](https://main.qcloudimg.com/raw/45e44cdc6495cd33a477bbcf83fe6649.jpg)
 2. 选中单个对象，在【更多操作】下拉列表中单击【下载】。
![](https://main.qcloudimg.com/raw/6265db98be71116a293b929875d98365.jpg)
 3. 在对象右侧单击【详情】进入文件详情页，在文件详情页中单击【下载对象】即可下载，或单击【复制临时链接】，将链接粘贴至浏览器地址栏，回车即可下载该对象。
![](https://main.qcloudimg.com/raw/88e128e95c375e971ea5995aae7a9206.jpg)

>?
>- 若对象所属存储桶的属性为私有读写，此处复制的地址后会自动计算签名添加后缀。了解签名生成方法，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。
>- 带有签名的临时链接在**查看对象详情**起1个小时内有效，也可通过单击【刷新有效期】刷新签名的有效期。

## 批量下载对象/文件夹
>?对象存储控制台仅支持单个对象下载，如需批量下载多个对象或文件夹，建议您直接安装 [COSBrowser 客户端](https://cloud.tencent.com/document/product/436/11366) 使用。下面介绍如何通过控制台，结合**COSBrowser 客户端**批量下载对象或文件夹。
#### 操作步骤
1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)，单击【存储桶列表】，进入存储桶列表页。找到对象所在的存储桶，单击其存储桶名称，进入存储桶管理页。
![](https://main.qcloudimg.com/raw/46f3f6bcf85a1ca8f16a2f47479d0ef8.jpg)
2. 选中多个对象，在【更多操作】下拉列表中，单击【下载】。
![](https://main.qcloudimg.com/raw/a947ce302b4b81495da5d1de0ea7f71e.jpg)
3. 按照弹窗提示，安装或打开 COSBrowser 客户端并登录。
![](https://main.qcloudimg.com/raw/8139647ac37a73deed1de5a7cc235966.png)
4. 打开 COSBrowser 后已选中文件会自动进入下载队列开始下载，您可以单击【下载列表】进行查看。
![](https://main.qcloudimg.com/raw/ab3c5cd10121b5d149bc97622bf11a0a.png)
