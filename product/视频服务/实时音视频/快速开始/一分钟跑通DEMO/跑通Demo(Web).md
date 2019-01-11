本文主要介绍如何快速地将腾讯云实时音视频Demo工程运行起来，您只需参考如下步骤依次执行即可。

## 1. 创建新的应用

进入腾讯云实时音视频[控制台](https://console.cloud.tencent.com/rav)，如果您还没有任何一个应用，会出现如下提示，提醒您创建一个新的应用：

![](https://main.qcloudimg.com/raw/6ca631d8a7be7d339845645f8c9f6ab6.png)

创建完应用之后，即可获得 SDKAppId，并且可以继续下一步：

![](https://main.qcloudimg.com/raw/9293fa946b52904f45c8b8b6ca105d53.png)

## 2. 购买测试套餐
单击上一步中的购买**测试体验套餐包**按钮，为上一步中创建的 SDKAppId 充值一定分钟数的测试用视频通话时长。

![](https://main.qcloudimg.com/raw/6d1510cac452f74812db3eb60be3218b.png)

## 3. 下载Demo源码
充值完体验套餐包之后，就可以进入控制台的快速上手页面，在页面的第一步指引中即可看到源码下载地址：

![](https://main.qcloudimg.com/raw/a6ebb01bc2d885a8f26b9b46ca9620fc.png)


## 4. 下载私钥文件
单击**下载公私钥**的链接，即可获得一个名为 **keys.zip** 的压缩包，解压后可以得到两个文件，即 public_key 和 private_key，用记事本打开 **private_key** 文件，并将其中的内容拷贝到第三步的文本输入框中。

![](https://main.qcloudimg.com/raw/75edc5d22563c32aace232543915bbff.png)

## 5. 获得配置文件
单击**生成Demo配置文件内容**按钮，即可获得一段 json 格式的文本内容，这段内容是由控制台根据您在第四步中填写的 private_key 基于非对称加密算法，生成的一组测试用的 userid 和 usersig。

![](https://main.qcloudimg.com/raw/5de8161bb72b2e19ebdb24ef6056751c.png)

复制上面的 json 内容，打开文件 `js/config.js` ，并按代码注释指引替换对应的内容。

> 此处方案仅用于快速跑通 Demo 示例。
> 真实的线上环境中，需要您的业务服务器根据 userid，使用上面提到的 private_key 实时计算出 usersig，这部分内容请参考 [如何计算UserSig](https://cloud.tencent.com/document/product/647/17275)。

## 6. 运行Demo

- step1：使用最新版本的 Chrome 浏览器打开 index.html
> - 一般情况下体验 demo 需要部署至服务器，通过 [https://域名/xxx] 访问，或者直接在本地搭建服务器，通过 [localhost：端口] 访问，避免浏览器限制在 file 协议下进行 WebRTC 通信。
> - 目前 Chrome 浏览器较完整支持 WebRTC 的特性，因此 Chrome 浏览器的体验效果最好。

- setp2: 进入页面后，选择一个体验用户名，并输入相应的房间号，点击**我要视频通话**。
	
- step3：浏览器会提示是否允许当前页面使用摄像头和麦克风，请点击允许，然后就可以看到视频画面了。

## 常见问题

### 1. 防火墙限制
由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请联系贵司的网络管理员，将如下端口加入防火墙的安全白名单中。

| 协议 | 端口号 |
|:--------:|:--------:|
| HTTP | 80 |
| HTTPS | 443 |
| UDP    | 443 |