本文主要介绍如何快速地将腾讯云实时音视频 Demo(Windows) 工程运行起来，您只需参考如下步骤依次执行即可。

## 1. 创建新的应用

进入腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav)，如果您还没有任何一个应用，会出现如下提示，提醒您创建一个新的应用：
![](https://main.qcloudimg.com/raw/6ca631d8a7be7d339845645f8c9f6ab6.png)
创建完应用之后，即可获得 SDKAppid，并且可以继续下一步：
![](https://main.qcloudimg.com/raw/af782656b5042abce3dd8dc1f164791e.png)

## 2. 购买测试套餐
单击【购买6.6元测试体验包】按钮，为上一步中创建的 SDKAppid 充值一定分钟数的测试用视频通话时长。
![](https://main.qcloudimg.com/raw/f0ff77dedba7017ec05e57d834ec7f48.png)

## 3. 下载 Demo 源码
充值完体验包之后，回到实时音视频控制台页面，单击第一步新创建的应用名称，进入该应用的详情页，在页面的第一步指引中即可看到源码下载地址：
![](https://main.qcloudimg.com/raw/100be38c27d503f0cfe689d7512f0131.png)

## 4. 下载私钥文件
单击**下载公私钥**的链接，即可获得一个名为 **keys.zip** 的压缩包，解压后可以得到两个文件，即 public_key 和 private_key，用记事本打开 **private_key** 文件，并将其中的内容拷贝到控制台应用详情页的第三步**生成Demo配置文件内容**的文本输入框中。
![](https://main.qcloudimg.com/raw/75edc5d22563c32aace232543915bbff.png)


## 5. 获得配置文件
单击【生成Demo配置文件内容】按钮，即可获得一段 json 格式的文本内容，这段内容是由控制台根据您在第四步中填写的 private_key 基于非对称加密算法，生成的一组测试用的 userid 和 usersig。
![](https://main.qcloudimg.com/raw/5de8161bb72b2e19ebdb24ef6056751c.png)

复制上面的 json 内容，并粘贴到源码根目录下的 `Config.json` 文件中（如果已经存在示例内容，请覆盖之）。


## 6. 编译运行
使用 Visual Stuido（建议 VS2015）打开源码目录下的 TRTCDemo.vcxproj 工程文件，如果您已经按照上面的步骤配置过 config.json，直接单击运行按钮即可。

## 常见问题
### 1. 开发环境要求
- 操作系统： Microsoft Windows 7+
- 开发环境：Microsoft Visual Studio 2015 +

### 2. 防火墙限制
由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请将如下端口加入防火墙的安全白名单中。

| 协议 | 端口号 |
|:--------:|:--------:|
| HTTPS | 443 |
| UDP | 8000 |



