
## 简介
本文档提供腾讯移动推送 iOS 应用快速接入指引。使用本地工具无代码集成，一键为您的iOS应用配置推送功能。

## 接入前准备
1. 接入 SDK 之前，需要您前往腾讯移动推送 [控制台](https://console.cloud.tencent.com/tpns) 创建产品和 iOS 应用，详细操作可参考 [创建产品和应用](https://cloud.tencent.com/document/product/548/37241) 文档。
![](https://main.qcloudimg.com/raw/c07fde02517072a093ac48482e92e9ea.png)
2. 应用创建完成后，您可以参考 [申请试用](https://cloud.tencent.com/document/product/548/37241#.E7.94.B3.E8.AF.B7.E8.AF.95.E7.94.A8) / [购买推送服务](https://cloud.tencent.com/document/product/548/37242) 操作文档，为您的应用申请试用或者购买推送服务。
![](https://main.qcloudimg.com/raw/c0324b24ada1e1ffc40d72aa77d3c30f.png)
3. 在【配置管理】页面上传推送证书，您可以参考 [证书获取指引](https://cloud.tencent.com/document/product/548/36664) 操作获取推送证书。
 ![](https://main.qcloudimg.com/raw/a00e9000d53aa4a3ccb0294ef9e719de.png)
![](https://main.qcloudimg.com/raw/c4eaeb3f2d9c3fbb42dbb75f2c5c12dc.png)

4. 完成以上步骤后，单击快速接入，下载快速集成工具。
![](https://main.qcloudimg.com/raw/bbe22b0a4ea25ed313c5c3785814f922.png)
5. 解压缩文件包，双击 TPNS Smart Tool。
![](https://main.qcloudimg.com/raw/b900deaadd11180abd6918e400ed55b6.png)
6. 此时会提示"无法打开TPNS Smart Tool"。
![](https://main.qcloudimg.com/raw/67334a5258eb5d879c54663d158029ee.png)
7. 前往系统偏好设置 > 安全性与隐私 > 通用中单击"仍要打开"。
![](https://main.qcloudimg.com/raw/2c5313c7d0e07ef38e231c16f056dfb2.jpg)
8. 按照系统提示输入本机密码确认操作，正确无误后再次单击"仍要打开"，此时会出现"打开"按钮。
![](https://main.qcloudimg.com/raw/9737b9509dd4beb08520ef9298136af5.png)

## 开始接入

安装并打开"TPNS Smart Tool"，执行以下操作：
1. 单击开始集成。
![](https://main.qcloudimg.com/raw/58d48d69704b096ce35e89ba54be73d5.png)
2. 输入当前应用的 AccessID 与 AccessKey（可在[产品管理](https://console.cloud.tencent.com/tpns)页面点击进入此应用的【配置管理】页面获取）。
![](https://main.qcloudimg.com/raw/fd03169088e7397cb3f35716e86e6688.png)
3. 选择您的 Xcode 工程使用的开发语言（Objective-C/Swift）。
4. 上传您的 Xcode 工程文件（.xcodeproj）。
![](https://main.qcloudimg.com/raw/eaa1c858b132cfdaab17b33b0de7de7f.jpg)
5. 单击【一键集成】按钮，等待集成结果：
 - 当开发语言选择为`Objective-C`时若出现以下提示，则表示集成成功。
![](https://main.qcloudimg.com/raw/9b1cbab5e061eb36240a08619673f639.png)
 - 当开发语言选择为`Swift`时若出现以下提示，则表示集成成功。
![](https://main.qcloudimg.com/raw/fa3e2d52ce2fdf21d4c2afaa28f1e8a6.png)

6.打开App工程配置，查看当前工程证书是否支持push，如不支持，则需要按照Xcode的提示处理证书。
![](https://main.qcloudimg.com/raw/6eca69b3e10f2525d87cd3b58c9e59c3.png)
## 接入结果验证
将 iPhone 设备连接 Xcode，安装 App 并观察控制台日志，若显示如下相似日志，表明客户端已经正确集成 SDK：
```
[TPNS] Current device token is 9298da5605c3b242261b57****376e409f826c2caf87aa0e6112f944
[TPNS] Current TPNS token is 00c30e0aeddff1270d8****dc594606dc184
```
若未搜索到 Token，请查看注册接口返回的错误码，根据 [错误码对照表](https://cloud.tencent.com/document/product/548/36669) 排查。

