## 准备工作
请先按照 [接入准备](https://cloud.tencent.com/document/product/1214/45793) 所述流程下载好 Demo 工程文件。

## 步骤1：设置密钥
使用 xcode 打开下载好的 Demo 工程文件，在 HomeViewController 的 SECRET_ID 和 SECRET_KEY 中填入您的专属密钥。

<img src="https://main.qcloudimg.com/raw/d17501a591d0042a965204d6e7c2480b.png" alt="20200616110337" style="zoom:80%;" />

## 步骤2：更改 Bundle ID

找到 **TARGETS -> General ->Identity**，将其中 Bundle Identifier 的内容修改为申请密钥时填写的 iOS Bundle id。

![](https://main.qcloudimg.com/raw/ee60603d7b2af826eebb2ad2a294dac7.png)

## 步骤3：更改 Development Team

找到 **TARGETS -> Build Settings ->Signing**，将其中 Development Team 的内容修改为申请密钥时填写的 iOS DEVELOPMENT_TEAM。

![](https://main.qcloudimg.com/raw/4f40c89e100e8661603372516d901aee.png)

## 步骤4：运行真机调试

