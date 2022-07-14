## 开发环境要求
微信开发者工具

## 集成说明

### TUIKit 支持以原生 js 的方式集成
从 Github 下载 TUIKit 源码。

#### 命令行执行

```
git clone https://github.com/tencentyun/TIMSDK.git
```

#### 进入小程序 TUIKit 项目
1. 进入 TUIKit  路径。
```
cd TIMSDK/MiniProgram/TUIKit
```

2.找到并打开 `TUIKit/miniprogram/debug/GenerateTestUserSig.js` 文件。
3.设置 `GenerateTestUserSig.js` 文件中的相关参数：
- SDKAPPID：默认为0，请设置为实际的 SDKAppID。
- SECRETKEY：默认为空字符串，请设置为实际的密钥信息。
![](https://main.qcloudimg.com/raw/11fd0b01fa56062c1fe93979082f8342.png)

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 TUIKit 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

4.编译运行，打开微信开发者工具，选择**小程序**，单击新建图标，选择**导入项目**。填写您微信小程序的 AppID，单击**导入**。
![](https://main.qcloudimg.com/raw/ff765eb10624d8fd4e91a3a64ea3634d.png)
>?此处应输入您微信小程序的 AppID，而非 SDKAppID。

5. 单击**预览**，生成二维码，通过手机微信扫码二维码即可进入小程序。
![](https://main.qcloudimg.com/raw/7f69e608656dcdebf54535a1097bfddf.png)

## 常见问题
### 小程序如果需要上线或者部署正式环境怎么办？
请在**微信公众平台**>**开发**>**开发设置**>**服务器域名**中进行域名配置：
将以下域名添加到 **request 合法域名**：
从v2.11.2起，SDK 支持了 WebSocket，WebSocket 版本须添加以下域名：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`wss://wss.im.qcloud.com`| Web IM 业务域名 | 必须|
|`wss://wss.tim.qq.com`| Web IM 业务域名 | 必须|
|`https://web.sdk.qcloud.com`| Web IM 业务域名 | 必须|
|`https://webim.tim.qq.com` | Web IM 业务域名 | 必须|

v2.10.2及以下版本，使用 HTTP，HTTP 版本须添加以下域名：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`https://webim.tim.qq.com` | Web IM 业务域名 | 必须|
|`https://yun.tim.qq.com` | Web IM 业务域名 | 必须|
|`https://events.tim.qq.com` | Web IM 业务域名 | 必须|
|`https://grouptalk.c2c.qq.com`| Web IM 业务域名 | 必须|
|`https://pingtas.qq.com` | Web IM 统计域名 | 必须|

将以下域名添加到 **uploadFile 合法域名**：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`https://cos.ap-shanghai.myqcloud.com` | 文件上传域名 | 必须|

将以下域名添加到 **downloadFile 合法域名**：

| 域名 | 说明 |  是否必须 |
|:-------:|---------|----|
|`https://cos.ap-shanghai.myqcloud.com` | 文件下载域名 | 必须|

## 相关文档：
- [SDK API 手册](https://web.sdk.qcloud.com/im/doc/zh-cn/SDK.html)
- [SDK 更新日志](https://cloud.tencent.com/document/product/269/38492)
