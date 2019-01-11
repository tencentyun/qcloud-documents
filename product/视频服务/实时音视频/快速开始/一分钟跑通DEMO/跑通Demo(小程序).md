本文主要介绍如何快速地将腾讯云实时音视频 Demo(小程序) 工程运行起来，您只需参考如下步骤依次执行即可。

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

复制上面的 json 内容，并粘贴到 `pages/webrtc-room/account.js` 文件中（如果已经存在示例内容，请覆盖之）。

>! 此处方案仅用于快速跑通 Demo 示例。
> 真实的线上环境中，需要您的业务服务器根据 userid，使用上面提到的 private_key 实时计算出 usersig，这部分内容请参考 [如何计算UserSig](https://cloud.tencent.com/document/product/647/17275)。

## 6.开通小程序类目与推拉流标签权限
出于政策和合规的考虑，微信暂时没有放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：

- 个人账号和企业账号的小程序暂时只开放如下表格中的类目：

| 主类目 | 子类目  |
|-------|----------|
| 【社交】| 直播 |
| 【教育】| 在线教育 |
| 【医疗】| 互联网医院，公立医院 |
| 【政务民生】| 所有二级类目 |
| 【金融】| 基金、信托、保险、银行、证券/期货、非金融机构自营小额贷款、征信业务、消费金融 |

- 符合类目要求的小程序，需要在【微信公众平台】-【开发】-【接口设置】中自助开通该组件权限，如下图所示：

![](https://mc.qcloudimg.com/static/img/a34df5e3e86c9b0fcdfba86f8576e06a/weixinset.png)

## 7. 编译运行
- step1：安装微信小程序 [开发者工具](https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html)，打开微信开发者工具，单击【小程序项目】按钮。

- step2： 输入您申请到的微信小程序 AppID（注意：不是上面的 SDKAppID），项目目录选择上一步下载到的代码目录（ **注意：** 目录请选择**根目录**，根目录包含有 `project.config.json`文件），单击【确定】创建小程序项目。
![](https://main.qcloudimg.com/raw/62d821ab972b8d65c5ea9d623b4f3ff5.png)
- step3： 按照上文第5步中的步骤修改 `pages/webrtc-room/account.js` 。
- step4： 使用手机进行测试，直接扫描开发者工具预览生成的二维码进入。
- step5： <font color='red'>开启调试模式</font>，体验和调试内部功能。开启调试可以跳过把这些域名加入小程序白名单的工作。

>!不同的手机进行预览体验时，要选择不同的体验 ID，因为同一个 ID 不能互相通讯。
![](https://main.qcloudimg.com/raw/9e28cb57bd7656641aec6a74b5c9dcb3.png)
	

## 常见问题
### 1. 开发环境要求
- 微信 App iOS 最低版本要求：6.5.21。
- 微信 App Android 最低版本要求：6.5.19。
- 小程序基础库最低版本要求：1.7.0。

### 2. 防火墙限制
由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请将如下端口加入防火墙的安全白名单中。

| 协议 | 端口号 |
|:--------:|:--------:|
| HTTP | 80 |
| HTTPS | 443 |
| UDP    | 443 |

### 3. 调试时为什么要开启调试模式？
开启调试可以跳过把这些域名加入小程序白名单的工作，否则可能会遇到登录失败，通话无法连接的问题。

### 4. 小程序源码会访问哪些域名？
&lt;webrtc-room&gt; 组件内部需要访问如下地址，您可以在 [微信公众平台](https://mp.weixin.qq.com)  > 开发 > 开发设置 > 服务器域名配置中进行配置：

| 域名 | 说明 | 
|:-------:|---------|
|`https://official.opensso.tencent-cloud.com` | WebRTC音视频鉴权服务域名 | 
|`https://yun.tim.qq.com` | WebRTC音视频鉴权服务域名 | 
|`https://cloud.tencent.com`| 推流域名 | 
