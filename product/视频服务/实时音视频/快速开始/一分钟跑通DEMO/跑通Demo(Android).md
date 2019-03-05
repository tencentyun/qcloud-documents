本文主要介绍如何快速地将腾讯云实时音视频 Demo(Android) 工程运行起来，您只需参考如下步骤依次执行即可。

## 1. 创建新的应用
进入腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav)，如果您还没有创建过一个应用，可以先创建一个新应用，即可获得 SDKAppid，并且可以继续下一步：

![](https://main.qcloudimg.com/raw/32065cbcd4cac9d8051a045cb1ae5d63.png)

## 2. 购买测试套餐
单击【购买6.6元测试体验包】按钮，为上一步中创建的 SDKAppid 充值一定分钟数的测试用视频通话时长。

![](https://main.qcloudimg.com/raw/24ee79290d7c328ee654bdb0643c55cb.png)

## 3. 下载 Demo 源码
充值完体验包之后，回到实时音视频控制台页面，单击第一步新创建的应用名称，进入该应用的详情页，在页面的第一步指引中即可看到源码下载地址：

![](https://main.qcloudimg.com/raw/064819772bf0ef727a377a4ee23f03eb.png)


## 4. 下载私钥文件
单击**下载公私钥**的链接，即可获得一个名为 **keys.zip** 的压缩包，解压后可以得到两个文件，即 public_key 和 private_key，用记事本打开 **private_key** 文件，并将其中的内容拷贝到控制台应用详情页的第三步**生成Demo配置文件内容**的文本输入框中。
![](https://main.qcloudimg.com/raw/75edc5d22563c32aace232543915bbff.png)

## 5. 获得配置文件
单击【生成Demo配置文件内容】按钮，即可获得一段 json 格式的文本内容，这段内容是由控制台根据您在第四步中填写的 private_key 基于非对称加密算法，生成的一组测试用的 userid 和 usersig。
![](https://main.qcloudimg.com/raw/5de8161bb72b2e19ebdb24ef6056751c.png)

将这段文本另存为名叫 **config.json** 的文本文件，并放在源码工程的 `app/src/main/res/raw` 目录下（如有示例文件存在，则覆盖之）。

## 6. 编译运行
使用 Android Studio （3.2 以上的版本）  打开源码工程，如果您已经按照上面的步骤配置过 config.json，直接单击运行按钮即可。

## 常见问题
### 1. 开发环境要求
- Android SDK API Level Level ≥ 16
- Android Studio 2.0 或以上版本
- App 要求 Android 4.1 或以上设备

### 2. 防火墙限制
由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请将如下端口加入防火墙的安全白名单中。

| 协议 | 端口号 |
|:--------:|:--------:|
| HTTPS | 443 |
| UDP | 8000 |



