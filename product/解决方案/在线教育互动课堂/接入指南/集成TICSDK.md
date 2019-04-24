## 接入概览

腾讯云互动课堂解决方案为用户提供强大的能力支持，用户只需完成业务层逻辑和接口调用，即可快速搭建一个全平台的在线互动课堂产品。
![](https://main.qcloudimg.com/raw/1924c82283cd5e15da0518d97154e0bb.png)

#### 业务侧登录和 userSig 生成

TICSDK 虽然有登录/登出接口，但是登录时使用的是`userId`和`userSig`，用户不能直接使用，还需实现业务层的登录逻辑，如图：

![](https://main.qcloudimg.com/raw/e5e4e33ea06db665a249844f928f0094.png)

业务终端先用业务侧的用户名密码登录开发者自己的服务器，然后开发者服务器使用腾讯云提供的工具生成登录TICSDK所需要的`userSig`（这一步相当于在腾讯云后台注册了一个账号，用户名为业务侧的用户名，密码为生成的`userSig`），并将其返回终端，终端拿到后就可以使用用户名(即`userId`)和`userSig`去调用 TICSDK 的登录接口，最后腾讯云后台负责校验登录信息的正确性，返回登录结果。

开发者需要做的就是图片`开发者服务器`上标注的，调用工具生成 userSig，并返回给终端的逻辑（通常做法为在业务侧登录接口回包中返回`userSig`）。

>?开发调试阶段，也可以使用实时音视频控制台生成`userId`和`userSig`用于测试开发，详情请参考 [生成签名](https://cloud.tencent.com/document/product/647/17275)。

#### 界面布局

用户需完成自己的产品的界面布局。

#### 课堂管理

由于课堂 ID (roomID) 从外部传入，TICSDK 无法维护 roomID，因此用户在调用 TICSDK 接口创建课堂时，需维护 roomID 的唯一性。
> ?创建重复的课堂 TICSDK 将会返回创建失败及错误信息，根据具体业务用户需维护当前的课堂列表。

## 客户端 SDK 文档

- [Windows SDK](https://cloud.tencent.com/document/product/680/17883)
- [Web SDK](https://cloud.tencent.com/document/product/680/17887)
- [Android SDK](https://cloud.tencent.com/document/product/680/17888)
- [iOS SDK](https://cloud.tencent.com/document/product/680/17891)
- [Mac SDK](https://cloud.tencent.com/document/product/680/31010)
