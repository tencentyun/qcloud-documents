登录**音视频终端 SDK控制台** > [Web License 管理](https://console.cloud.tencent.com/vcube/web)，该页面提供了密钥 Token 以及 Web License & 项目的管理，您可在此查看并创建项目以及对应的 Web License。

## 管理 Web License 
目前我们提供两个版本的 Web License，分别为正式版 Web License 和测试版 Web License。一个项目对应一个字符串形式的 License Key，接入 SDK 使用时需要使用 License Key。
- [测试版 Web License](https://tcloud-doc.isd.com/document/product/616/71368?!preview&!editLang=zh#test) 可以直接创建，有效期 14 天，**仅可续期一次**，共28天。
- [正式版 Web License](https://tcloud-doc.isd.com/document/product/616/71368?!preview&!editLang=zh#formal) 需要绑定 Web License 资源，有效期时为一年。
> ! 目前暂无计费购买的资源，创建并使用正式版 Web License，需先 [申请领取 License 资源](https://cloud.tencent.com/apply/p/9fuh8sv6fl?!preview)。

## 创建项目
Web 美颜特效 SDK 支持 Web 端和微信小程序使用，创建项目时需填写要部署的 Web 网站域名或微信小程序 APPID，如您同时在两种场景下使用该项目，则都需填写。

1. 单击**创建并绑定 License**（绑定正式 License），进入填写**项目名称**及业务部署场景信息等参数。
![](https://qcloudimg.tencent-cloud.cn/raw/ae3d8c5ac8dd95f3b814555662ed9b34.png)
> !
> - 域名必须完全匹配，不支持其子域名。
> - 进入 [**微信公众平台**](https://mp.weixin.qq.com/)，登录小程序账号，打开**设置** > **帐号信息**，即可获得小程序 APPID 。
2. 单击**下一步**，选择 License 资源（没有 License 资源时可 [提交申请](https://cloud.tencent.com/apply/p/9fuh8sv6fl?!preview)），单击**确定**即可完成创建。
![](https://qcloudimg.tencent-cloud.cn/raw/d1be5a9ce87d136646ae462c01b89995.png)
3. 创建成功后即可生成正式版 Web License。
![](https://qcloudimg.tencent-cloud.cn/raw/7ed8ac6c394a8610dbddc7de16c6b2cf.png)
> ! 若您是单击**创建测试项目**创建 Web License，则不需要绑定 License 资源，创建完成得到的即是测试版 Web License。

![](https://qcloudimg.tencent-cloud.cn/raw/5da5d13014fb540b478aab164d7d758a.png)

## 续期 License
测试版 Web License 默认有效期为**14天**，期满后您可续期1次（仅可续期一次），单击测试版 License 右侧的**续期**即可完成续期，增加**14天**有效期。

![](https://qcloudimg.tencent-cloud.cn/raw/378863a7fffcebac23c0edc4bbc90f17.png)


## 编辑项目
若您的业务应用部署信息需要更改或增添。
1. 进入 [Web License 管理](https://console.cloud.tencent.com/vcube/web)， 单击需修改的项目，单击右上角的**编辑**，进入项目基本信息编辑页。
![](https://qcloudimg.tencent-cloud.cn/raw/ae54ae6fc7c5ce7b6aa18a732f1507cd.png)
2. 支持编辑修改当前项目的项目名称、使用场景及对应的信息，单击**确定**即可更新当前项目。
![](https://qcloudimg.tencent-cloud.cn/raw/b857974619044fe3dd7232046ba7851e.png)



