
本文主要介绍如何快速地将腾讯云云通信 IM Demo(Windows) 工程运行起来，您只需参考如下步骤依次执行即可。

## 1. 创建应用
登录腾讯云通信（IM）[控制台](https://console.cloud.tencent.com/avc)，在**应用列表**页，单击【创建应用接入】，在**创建新应用**弹框中，填写新建应用的信息，单击【确认】。
![](https://main.qcloudimg.com/raw/a7769d15f050286162b0cbcdadca5f03.png)

应用创建完成后，自动生成一个应用标识：SDKAppID，如下图：
![](https://main.qcloudimg.com/raw/bf8fe4f38d782741a6e142c24648c9e0.png)

## 2. 配置应用
完成创建应用之后返回应用列表，单击对应 SDKAppID 的【应用配置】链接，在应用详情页，找到当前页面的【帐号体系集成】部分，单击【编辑】链接，配置【帐号管理员】信息，然后单击【保存】。

>?帐号管理员可以随便填写，在使用云通信后台的 REST API 发送消息时才会用到。

![](https://main.qcloudimg.com/raw/e3ce0ef527d2d4f8d0b3a0f69cefa78e.png)


## 3. 获取测试 userSig
完成帐号管理员配置后，单击【下载公私钥】的链接，即可获得一个名为 **keys.zip** 的压缩包。解压后可以得到两个文件，即 public_key 和 private_key，用记事本打开 **private_key** 文件，并将其中的内容拷贝到【开发辅助工具】的私钥文本输入框中。

其中：**identifier** 即为您的测试帐号（也就是 userId），私钥为 private_key 文件里的文本内容，生成的签名就是**userSig**。identifier 和 userSig 是一一对应的关系。
>! 可以多生成4组以上的 userid 和 usersig，方便在第5步中调试使用。

![](https://main.qcloudimg.com/raw/a1b9bb35760e1e52825c754bd3ef9a52.png)


## 4. 下载 Demo 源码
从 [Github](https://github.com/tencentyun/TIMSDK) 下载 IM SDK Windows IMApp 工程代码。

![](https://main.qcloudimg.com/raw/356319843b9560be6a9b17a679659a4b.png)

## 5. 修改源码配置
- 使用 Visual Stuido（建议 VS2015）双击源码目录下的 ImApp.sln 工程文件，打开 IMApp 工程
- 工程中默认配置了测试的 SDKAppID 以及在控制台生成的4个测试帐号，由于每个帐号同时只能有一个端登录，所以您需要按照以上第3步指引中拿到自己的4组测试帐号配置进去。
- 在文件 main.cpp 中替换您的 SDKAppID，以及替换以上第3步指引中拿到的 userId 和 userSig。
![](https://main.qcloudimg.com/raw/3440cb91cac41c6e84b584fdb2c8543f.png)

>! 这里提到的获取 userid 和 usersig 的方案仅适合本地跑通 Demo 和功能调试，userSig 正确的签发方式请参考  [登录鉴权](https://cloud.tencent.com/document/product/269/31999) 文档。

## 6. 编译运行
程序启动后，在不同的客户端上登录不同的帐号，搜索对方的 userId 创建会话，就可以体验发消息了。
