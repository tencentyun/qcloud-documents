
本文主要介绍如何快速地将腾讯云即时通信 Demo(Android) 工程运行起来，您只需参考如下步骤依次执行即可。

## 1. 创建应用
登录腾讯云通讯（IM）[控制台](https://console.cloud.tencent.com/avc)，在**应用列表**页，单击【创建应用接入】，在**创建新应用**弹框中，填写新建应用的信息，单击【确认】：
![](https://main.qcloudimg.com/raw/a7769d15f050286162b0cbcdadca5f03.png)

应用创建完成后，自动生成一个应用标识：SdkAppId，如下图：
![](https://main.qcloudimg.com/raw/bf8fe4f38d782741a6e142c24648c9e0.png)

## 2. 配置应用
完成创建应用之后返回应用列表，单击对应 SdkAppId 的**应用配置**链接，在应用详情页，找到当前页面的**帐号体系集成**部分，单击**编辑**链接，配置**账号管理员**信息，然后单击【保存】：

>?账号管理员可以随便填写，在使用云通讯后台的 REST API 发送消息时才会用到。

![](https://main.qcloudimg.com/raw/e3ce0ef527d2d4f8d0b3a0f69cefa78e.png)


## 3. 获取测试 userSig
完成账号管理员配置后，单击**下载公私钥**的链接，即可获得一个名为 **keys.zip** 的压缩包。解压后可以得到两个文件，即 public_key 和 private_key，用记事本打开 **private_key** 文件，并将其中的内容拷贝到**开发辅助工具**的私钥文本输入框中。

其中：**identifier** 即为你的测试账号（也就是 userId），私钥为 private_key 文件里的文本内容，生成的签名就是**userSig**。identifier 和 userSig 是一一对应的关系。
>! 可以多生成4组以上的 userid 和 usersig，方便在第5步中调试使用。

![](https://main.qcloudimg.com/raw/a1b9bb35760e1e52825c754bd3ef9a52.png)


## 4. 下载 Demo 源码
从 [Github](https://github.com/tencentyun/TIMSDK/tree/master/Android) 下载 ImSDK Android 开发包，打开 tuikit 工程。

## 5. 修改源码配置
- 使用 Android Studio （3.0 以上的版本）  打开源码工程。
- 工程中默认配置了测试的 SdkAppId 以及在控制台生成的四个测试账号，由于每个账号同时只能有一个端登录，所以您需要按照 step 3 中指引拿到自己的四组测试账号配置进去。
- 在 com.tencent.qcloud.uipojo.utils.Constants 中替换您的 SdkAppId。
![](https://main.qcloudimg.com/raw/b6cec2fd99c8350f4781304d96d28653.png)

- 在 com.tencent.qcloud.uipojo.login.view.LoginActivity 中替换以上第三步在 IM 控制台中获得的 userId 和 userSig 。
![](https://main.qcloudimg.com/raw/976f87fe676546bfc93fc3dcb04bc97e.png)

>! 这里提到的获取 userid 和 usersig 的方案仅适合本地跑通 demo 和功能调试，userSig 正确的签发方式请参考 [帐号登录集成说明](https://cloud.tencent.com/document/product/269/1507)。

## 6. 编译运行
App 启动后，在不同的手机上登录不同的账号，就可以搜索对方的 userId 体验发消息了。
