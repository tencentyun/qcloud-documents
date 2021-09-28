本文主要介绍如何快速地运行即时通信 IM Demo（Windows）工程。

<span id="step1"></span>
## 创建应用
1. 登录即时通信 IM [控制台](https://console.cloud.tencent.com/avc)。
 >?如果您已有应用，请记录其 SDKAppID 并 [配置应用](#step2)。
 >
2. 在【应用列表】页，单击【创建应用接入】。
3. 在【创建新应用】对话框中，填写新建应用的信息，单击【确认】。
 应用创建完成后，自动生成一个应用标识 SDKAppID，请记录 SDKAppID 信息。
 
<span id="step2"></span>
## 配置应用
1. 单击目标应用所在行的【应用配置】，进入应用详情页面。
 ![](https://main.qcloudimg.com/raw/e41602a50754be9d478b9db84c0bcff2.png)
2. 单击【帐号体系集成】右侧的【编辑】，配置**帐号管理员**信息，单击【保存】。
 ![](https://main.qcloudimg.com/raw/2ad153a77fe6f838633d23a0c6a4dde1.png)

<span id="step3"></span>
## 下载公私钥

1. 在控制台应用详情页面，单击【下载公私钥】，保存 **keys.zip** 压缩文件。
 ![](https://main.qcloudimg.com/raw/e11d958bc43b09fb41c7064ee2b09722.png)
2. 解压 **keys.zip** 文件 ，获得 **private_key.txt** 和 **public_key.txt** 文件，其中 **private_key.txt** 即为私钥文件。
 ![](https://main.qcloudimg.com/raw/ec89f5bb93d57de1acffa4e15786da11.png)

## 下载 Demo 源码
从 [Github](https://github.com/tencentyun/TIMSDK/tree/master/Windows) 下载即时通信 IM Demo（Windows）IMApp 工程代码。

## 修改源码配置
>!本文提到的获取 UserID 和 UserSig 的方案仅适合本地跑通 Demo 和功能调试，正确的 UserSig 签发方式请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)。

1. 使用 Microsoft Visual Studio（建议 VS2015）双击源码目录下的 ImApp.sln 工程文件，打开 IMApp 工程后，打开 TestUserSigGenerator.h 文件。
2. 在工程中配置 [创建应用](#step1) 中获取的测试 SDKAppID。
 ![](https://main.qcloudimg.com/raw/2285708c13c47687832697c9c6af6c53.png)
3. 在工程中配置  [下载公私钥](#step3) 中获得的测试私钥 ，用于生成 UserSig。
 ![](https://main.qcloudimg.com/raw/0a3e2c4f1b1a0fd07b3510fbf0eff848.png)
4. 在文件 main.cpp 中查看您测试的 UserID。
 ![](https://main.qcloudimg.com/raw/33834ecf83cf6e1976df2418afe826f1.png)

## 编译运行
程序启动后，在不同的客户端上登录不同的帐号，搜索对方的 UserID 创建会话，即可体验发送消息等功能。
