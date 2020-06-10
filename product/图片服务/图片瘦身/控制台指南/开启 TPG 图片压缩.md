

TPG 是腾讯推出的自研图片格式，在保证图片观感的情况下实现有效压缩，支持 JPG、PNG、webP、GIF 等格式的转换。

>! 
>- TPG 为腾讯自研图片格式，如需使用请确认图片加载环境支持 TPG 解码，腾讯云音视频实验室提供集成 TPG 解码器的[ IOS、Android、Windows 终端 SDK](https://cloud.tencent.com/document/product/875/18366)，可帮助您快速接入和使用 TPG。
>- TPG 压缩是付费服务，具体费用可查看 [计费项](https://cloud.tencent.com/document/product/1236/44811)。


## 操作步骤

您可通过控制台开通 TPG 图片压缩，开通后，对于当前存储桶中的图片资源，使用相应的图片压缩接口即可实现下载时处理。

1. 登录 [数据万象控制台](https://console.cloud.tencent.com/ci/bucket) ，在【存储桶管理】页面选择需操作的存储桶（例如 buckettest），进入存储桶管理页面。
2. 单击【样式管理】页签，进入图片样式管理页面。
3. 找到【TPG 图片压缩】配置项，单击【编辑】并打开状态按钮。
![](https://main.qcloudimg.com/raw/6283749c8192ba875ea2efb14d059a1f.jpg)
4. 单击【保存】，即可开启 TPG 图片压缩。
