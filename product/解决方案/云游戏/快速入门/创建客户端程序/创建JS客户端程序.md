腾讯云云游戏提供 JS SDK，可支持包括 PC 浏览器、移动端 H5 页面以及小程序内嵌 WebView 等多种落地场景。本文将通过 Web 端程序入门 Demo 演示如何快速搭建 Web Demo 并部署运行。

## 步骤1：下载 Demo[](id:step1)
单击 [下载](https://github.com/tencentyun/cloudgame-js-sdk/tree/master/demo) Web 端程序 Demo 工程。

## 步骤2：配置文件[](id:step2)
解压 Demo 工程文件，打开 `demo` 目录下 `demo.html` 文件。
- 请求 **url**：修改为您后台程序中的对应后台接口地址。
- **GameId**：修改为您在 [接入准备 - 步骤4](https://cloud.tencent.com/document/product/1162/46135#step4) 中部署后会在**云游戏控制台** > **游戏管理**中生成对应的 GameID。
- **UserId**：修改为用户唯一标识（由业务方自定义），ClientSession 修改为云游戏 Web 端 Session。

![](https://qcloudimg.tencent-cloud.cn/raw/fb3decdca3d69ee5d528639ff02835b0.png)

## 步骤3：部署（可选）[](id:step3)
部署一个静态网站，这里可使用腾讯云对象存储（COS）来托管。

1. 进入 **COS 控制台** > [**存储桶列表**](https://console.cloud.tencent.com/cos5) 单击**创建存储桶**，并将**访问权限**设置为“公有读私有写”，具体操作请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。
![](https://qcloudimg.tencent-cloud.cn/raw/97688cb27984e35953f673a34dd354e7.png)
2. 存储桶创建完成后，进入存储桶详情页的**文件列表**，单击**上传文件**，将已修改配置的 Demo 工程文件上传到 COS 存储桶。
![](https://qcloudimg.tencent-cloud.cn/raw/f4d4c3cdb29c3595c77a835bf5d6dec7.png)
3. 进入**基础配置** > **静态网站**，单击**编辑** [开启静态网站](https://cloud.tencent.com/document/product/436/14984) 功能。成功开启后，静态网站页面下的的“访问节点”即是网站的访问地址，在浏览器中访问即可体验 Demo。
![](https://qcloudimg.tencent-cloud.cn/raw/526d55a337a37180beaf6ad0f606987f.png)

经过以上步骤，您的 JS 入门 Demo 就搭建完成了。
