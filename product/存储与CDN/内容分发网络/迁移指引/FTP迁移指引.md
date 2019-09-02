#### 迁移须知

迁移前，您需要登录 FTP 服务器，将所有的在 FTP 上的资源同步至本地。迁移过程中，请勿向 FTP 中新增资源。

#### 1 创建 Bucket

登录 [COS 控制台](https://console.cloud.tencent.com/cos)，若未开通，请单击开通 COS 对象存储服务，在左侧单击【Bucket 列表】：
![](https://mc.qcloudimg.com/static/img/b87d5d718cf5c7e8b6d93cd2acc78783/cos-1.png)

单击页面上【创建Bucket】按钮，填充如下项：

选择【所属项目】: 您可以根据需要对该源站进行分项目管理

填写 Bucket 名称：为bucket命名，示例中填写APPID

填写所属地域：根据需要选择COS所在园区

访问权限：选择【公有读私有写】

CDN加速：选择【关闭】![](https://mc.qcloudimg.com/static/img/e765dd971cb4a4ce2bae8d670e2a4e43/create_bucket.png)

此时可以看到该 bucket 对应默认域名：

![](https://mc.qcloudimg.com/static/img/448abcbf4f9f0ec86dac6449d7fbc184/domain-name.png)

选择【基础配置】，在下方开启该 bucket 的【静态网站】功能：

![](https://mc.qcloudimg.com/static/img/e7d6f2f605c3504efa713b2997f0f347/open_static_web.png)



#### 2  同步资源

利用COS本地同步工具，将资源同步至指定 bucket，使用方式可参考：
https://cloud.tencent.com/document/product/436/7133



#### 3 源站切换

请保证 COS 中的资源路径与原有 FTP 中资源路径一致，然后通过工单系统提交加速域名与要切换的 COS bucket 域名，我们会协助您进行切换。

切换成功后，所有资源均从 COS 中获取，文件管理操作可通过 COS 进行，更多操作指南请参考 [对象存储服务](https://cloud.tencent.com/document/product/436)。

