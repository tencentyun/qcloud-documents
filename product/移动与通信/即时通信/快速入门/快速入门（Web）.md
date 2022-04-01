本文主要介绍如何快速运行腾讯云即时通信 IM Demo (Web)。
                    

## 效果展示
![](https://qcloudimg.tencent-cloud.cn/raw/5f65b75ed5eb8ba52fc7734e8aea672c.png)


## 操作步骤
[](id:step1)
### 步骤1：创建应用
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
>?如果您已有应用，请记录其 SDKAppID 并 [获取密钥信息](#step2)。
>同一个腾讯云帐号，最多可创建300个即时通信 IM 应用。若已有300个应用，您可以先 [停用并删除](https://cloud.tencent.com/document/product/269/32578#.E5.81.9C.E7.94.A8.2F.E5.88.A0.E9.99.A4.E5.BA.94.E7.94.A8) 无需使用的应用后再创建新的应用。**应用删除后，该 SDKAppID 对应的所有数据和服务不可恢复，请谨慎操作。**
>
2. 单击**创建新应用**，在**创建应用**对话框中输入您的应用名称，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/febed2f15dee6ff09f066ba228c7fc27.png)
3. 创建完成后，可在 [控制台总览页](https://console.cloud.tencent.com/im) 查看新建应用的状态、业务版本、SDKAppID、创建时间、标签以及到期时间。请记录 SDKAppID 信息。
![](https://qcloudimg.tencent-cloud.cn/raw/853d2c3c0d5887dadc254eb0e03a215e.png)


[](id:step2)
### 步骤2：获取密钥信息
1. 单击目标应用卡片，进入应用的基础配置页面。
![](https://qcloudimg.tencent-cloud.cn/raw/e435332cda8d9ec7fea21bd95f7a0cba.png)
2. 在**基本信息**区域，单击**显示密钥**，复制并保存密钥信息。
>!请妥善保管密钥信息，谨防泄露。

[](id:step3)
### 步骤3：下载并配置 Demo 源码

1. 根据您的实际业务需求，下载 SDK 及配套的 [Demo 源码](https://cloud.tencent.com/document/product/269/36887)。
<dx-codeblock>
:::  js

# 命令行执行
git clone https://github.com/tencentyun/TIMSDK.git

# 进入 Web 项目

cd TIMSDK/Web/Demo

# 安装依赖
npm install
:::
</dx-codeblock>
2. 打开终端目录的工程，找到对应的 `GenerateTestUserSig` 文件，路径为：/public/debug/GenerateTestUserSig.js
3. 设置`GenerateTestUserSig`文件中的相关参数：
 - SDKAPPID：请设置为 [步骤1](#step1) 中获取的实际应用 SDKAppID。
 - SECRETKEY：请设置为 [步骤2](#step2) 中获取的实际密钥信息。
 ![](https://main.qcloudimg.com/raw/e7f6270bcbc68c51595371bd48c40af7.png)


>!本文提到的获取 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

[](id:step4)
### 步骤4：编译运行
在项目终端执行以下命令行，在浏览器中运行即可：
<dx-codeblock>
:::  js
# 命令行执行
npm run start
:::
</dx-codeblock>

## 参见文档

- [SDK API 手册](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html)
- [SDK 更新日志](https://cloud.tencent.com/document/product/269/38492)
- [Demo 源码](https://github.com/tencentyun/TIMSDK/tree/master/Web/Demo)
