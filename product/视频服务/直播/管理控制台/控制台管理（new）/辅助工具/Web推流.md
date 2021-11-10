腾讯云为您提供 Web 推流功能，支持摄像头采集、屏幕分享采集和本地文件采集三种采集方式进行直播。可实现快速生成推流地址，在线推流测试直播功能。

## 前提条件
- 已登录 [云直播控制台](https://console.cloud.tencent.com/live)。
- 已添加 [推流域名](https://cloud.tencent.com/document/product/267/20381)。
- 您的设备已安装摄像头，并浏览器支持 Flash 插件调用摄像头权限。

## 操作步骤
1. 登录云直播控制台，选择 [**Web推流**](https://console.cloud.tencent.com/live/tools/webpush)。
2. **选择采集方式**。您可选择摄像头采集、屏幕分享采集和本地文件采集三种采集方式进行直播。
<dx-tabs>
::: 摄像头采集
摄像头采集是通过摄像头/麦克风（支持外接）进行视频/声音的采集。单击 **开启摄像头**/ **开启麦克风**，首次开启需授予浏览器使用摄像头和麦克风权限。
![](https://main.qcloudimg.com/raw/5b13b33c84c85587c0b9628ae6fe37c2.png)
:::
::: 屏幕分享采集
 屏幕分享采集是通过浏览器捕获对应窗口/界面进行分享采集。单击 **选择屏幕分享** 选择分享的内容，可为整个屏幕/某个窗口/浏览器标签页。
![](https://main.qcloudimg.com/raw/7d7c2150f29c0d6f0e82f48ca04ef064.png)
:::
::: 本地文件采集
本地文件采集是通过指定本地文件进行画面采集，再通过 Web 推流工具推送到云直播。单击 **选择本地文件** 选择需要推流的内容，目前仅支持 MP4 格式文件。
![](https://main.qcloudimg.com/raw/8b5902491330e4b9c6d78b45c88598f7.png)
:::
</dx-tabs>
> ! 在开启预览或选定分享屏幕内容后，不可切换采集方式，需关闭预览或取消分享屏幕后才可切换采集方式。
3. **采集配置**。设置采集配置，默认为推荐配置（不同分辨率有不同推荐配置），可在右上角单击 **编辑** 进入自定义编辑配置。（**摄像头采集和屏幕分享采集额外增加声音采样率的设置选项，本地文件采集只有分辨率和视频帧率的设置选项。**）
![](https://main.qcloudimg.com/raw/47ada859dc54bf2859ce9c76103ab7b4.png)
4. **推流配置**。设置推流配置，默认为推荐配置（不同分辨率有不同视频码率的推荐配置，音频码率不支持修改），可在右上角单击 **编辑** 进入自定义编辑配置，可自定义修改视频码率和音频码率。
> ? web 推流的音频编码方式为 opus 编码，推荐使用快直播 WebRTC 地址进行播放。若使用标准直播的播放地址（RTMP/FLV/HLS），系统会自动转换为 aac 编码才能正常播放，从而会产生音频转码费用，详见 [计费文档](https://cloud.tencent.com/document/product/267/39889#a_trans)。
> 
![](https://main.qcloudimg.com/raw/1cdda05bdee9acb361fde98d754796a6.png)
5. **推流预览**。在确定采集方式和配置以及推流配置后，开启预览，即可在右侧看到推流预览。
![](https://main.qcloudimg.com/raw/60e032cbac522fb02cd58550a10cb621.png)
6. 输入 WebRTC 推流地址或单击 **快速生成**，进行以下配置：
	- 选择您的推流域名。
	- 编辑 AppName，用于区分同一个域名下多个 App 的地址路径，默认值为 live。
	- 填写自定义的流名称 StreamName，例如：`test`。
	- 选择过期时间，例如：`2021-08-28 16:16:52`。
	- 单击 **确定**，快速自动生成 WebRTC 推流地址填入地址栏。
![](https://main.qcloudimg.com/raw/5b642ef826145e1797ebd7249546d64a.png)
7. 单击 **开始推流**，即可开始推流。您可单击![](https://main.qcloudimg.com/raw/da098f4e5ab01021e3c4704b0de41240.png)和![](https://main.qcloudimg.com/raw/aa8d8d4c9c32359a249de37ed0d723be.png)按钮来关闭/开启画面和声音，单击关闭画面或声音系统依旧正常采集，但是无法预览，推流可以正常发起但是没有画面和声音。
> ? 推流成功后，采集预览的状态不支持变更，而且推流可能会产生对应的带宽/流量或其他增值服务费用。
> 
![](https://main.qcloudimg.com/raw/1795b1d211017b79eb7ea855c7a4a276.png)
8. 推流成功后您可在下方单击 **立即查看**，快速跳转至查看直播流推流相关数据。非当前账号推流地址无法获取推流数据和播放地址，您可以通过当前账号下的推流域名生成推流地址，或者使用拉流转推功能，将直播流同时转推到当前账号下。
![](https://main.qcloudimg.com/raw/2a08d6de7da2d61cd6415456f688eb15.png)
9. 若您在 **域名管理** 中已添加播放域名，即可在下方 **选择播放域名** 快速生成的播放地址。若您需生成有转码配置的播放地址，需先将播放域名绑定转码模板，才可生成播放转码流。
![](https://main.qcloudimg.com/raw/a4dec8a211e1b2f6a7ba8432a2e89076.png)
其中，播放地址由以下4部分组成：
![](https://main.qcloudimg.com/raw/72989c8f55fe7f2ed596bd09882f5a09.png)支持 RTMP、FLV 、 HLS 和 UDP 协议，可以单击播放地址后的二维码，通过 [腾讯云工具包 App](https://cloud.tencent.com/document/product/454/6555#rtmpdemo) 扫码查看播放地址：
![](https://main.qcloudimg.com/raw/23580118a446c188d02f77a721c25691.png)
>! 当选择的播放域名已开启 HTTPS 配置时，生成的 FLV 和 HLS 地址会默认带上 HTTPS。

