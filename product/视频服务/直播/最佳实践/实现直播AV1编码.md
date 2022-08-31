AV1是一款开源、免版权费的视频压缩格式，相比上一代H.265[HEVC]编码，在相同画质下码率可以再降低30%+，这就意味着在同等带宽下可以传输更高清的画质，从而达到降低带宽成本的效果。通过阅读本文，您可以了解如何将视频转码为AV1格式的视频并进行播放。

## AV1 使用

### 前提条件

- 已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成实名认证。
- 已开通腾讯云直播服务，并添加 [推流&播放域名](https://cloud.tencent.com/document/product/267/20381)。

[](id:step1)
### 步骤1：创建转码模板
1. 登录云直播控制台，进入**功能配置** > [直播转码](https://console.cloud.tencent.com/live/config/transcode)。
2. 单击 **创建转码模板**，选择转码类型为标准转码或极速高清转码，展开高级配置。
3. 在编码方式中选择 **AV1**。
![](https://qcloudimg.tencent-cloud.cn/raw/8a2d93bbcc9154fadd96d51ac916066e.png) 
4. 填写完成后，单击 **保存** 即可。

[](id:step2)
### 步骤2：绑定域名
选择转码模板，单击**绑定域名** ，选择您需绑定的**转码模板**及**播放域名**，单击**确定**即可绑定成功。
![](https://qcloudimg.tencent-cloud.cn/raw/41575a93b7e31d1b598ae4f6570a31dc.png)

[](id:step3)
### 步骤3：生成播放地址
单击 **地址生成器** ，选择步骤2中绑定的播放域名，以及 [步骤1](#step1) 中的转码模板，生成播放地址。

[](id:step4)
### 步骤4：播放AV1视频

通过支持AV1的播放器，按播放步骤3中生成的地址进行播放即可。在播放器的选择上，可以选择已支持AV1的播放器，也可以对自有播放器进行改造。

- **已支持AV1的播放器**
	- **App 客户端**
		- [ExoPlayer](https://github.com/google/ExoPlayer) 已支持AV1，用的 libgav1
		- [ijkplayer](https://github.com/bilibili/ijkplayer) FFmpeg 版本陈旧，可以升级 FFmpeg 并集成 [dav1d](https://code.videolan.org/videolan/dav1d)
	- **Web 端**
		- [dash.js](http://cdn.dashjs.org/v2.4.0/jsdoc/index.html) 已经支持（解码取决于浏览器，Chrome 支持）
		- [shaka-player](https://github.com/shaka-project/shaka-player) 已经支持（解码取决于浏览器，Chrome 支持）
	- **PC 端**
	VLC PC 版，支持AV1 in FLV、HEVC in FLV， 可按需下载 [Windowos 版](https://share.weiyun.com/haPT1L0W) & [MacOS 版](https://share.weiyun.com/W2btBASt)
- **自有播放器改造**
如果您的播放器不具备播放AV1格式视频的能力，可参考 [AV1视频播放](https://cloud.tencent.com/document/product/267/77810) 改造播放器
