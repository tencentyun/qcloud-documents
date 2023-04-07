腾讯云为您提供 Web 推流功能，支持摄像头采集、屏幕分享采集和本地文件采集三种采集方式进行直播。可实现快速生成推流地址，在线推流测试直播功能。

## 前提条件
- 已登录 [云直播控制台](https://console.cloud.tencent.com/live)。
- 已添加 [推流域名](https://cloud.tencent.com/document/product/267/20381)。
- 您的设备已安装摄像头，并允许浏览器调用摄像头权限。

## 单路推流
1. 登录云直播控制台，选择 [**Web 推流**](https://console.cloud.tencent.com/live/tools/webpush)，单击单路推流。
2. **选择采集方式**。您可选择摄像头采集、屏幕分享采集和本地文件采集三种采集方式进行直播。
<dx-tabs>
::: 摄像头采集
摄像头采集是通过摄像头/麦克风（支持外接）进行视频/声音的采集。单击 **开启摄像头**/ **开启麦克风**，首次开启需授予浏览器使用摄像头和麦克风权限。
![](https://qcloudimg.tencent-cloud.cn/raw/bc954d92610673ddeb5aeecf2a1dcbf6.png)
:::
::: 屏幕分享采集
 屏幕分享采集是通过浏览器捕获对应窗口/界面进行分享采集。单击 **选择屏幕分享** 选择分享的内容，可为整个屏幕/某个窗口/浏览器标签页。屏幕分享采集支持选择音频源，目前只有 Chrome 74+ 和 Edge 79+ 支持采集声音，在 Windows 系统可以采集整个系统的声音，在 Linux 和 Mac 上面只能采集标签页的声音。
![](https://qcloudimg.tencent-cloud.cn/raw/ec67091026b7e511fea03154755fb78e.png)
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
> ? Web 推流的音频编码方式为 OPUS 编码，推荐使用快直播 WebRTC 地址进行播放。若使用标准直播的播放地址（RTMP/FLV/HLS），系统会自动转换为 AAC 编码才能正常播放，从而会产生音频转码费用，详情请参见 [计费文档](https://cloud.tencent.com/document/product/267/39889#a_trans)。
> 
![](https://main.qcloudimg.com/raw/1cdda05bdee9acb361fde98d754796a6.png)
5. **推流预览**。在确定采集方式和配置以及推流配置后，开启预览，即可在右侧看到推流预览。
![](https://qcloudimg.tencent-cloud.cn/raw/30a294ae08740005590ea4c72559cb7d.png)
6. 输入 WebRTC 推流地址或单击 **快速生成**，进行以下配置：
  - 选择您的推流域名。
  - 编辑 AppName，用于区分同一个域名下多个 App 的地址路径，默认值为 live。
  - 填写自定义的流名称 StreamName，例如：`test`。
  - 选择过期时间，例如：`2023-03-06 00:00:00`。
  - 单击 **确定**，快速自动生成 WebRTC 推流地址填入地址栏。
![](https://qcloudimg.tencent-cloud.cn/raw/78aa1679ca95466634fae126598d6067.png)
7. 单击 **开始推流**，即可开始推流。
	1. 您可单击![](https://qcloudimg.tencent-cloud.cn/raw/b2390afbbc7b72bfeee8c2c5b2ad09cf.png)和![](https://qcloudimg.tencent-cloud.cn/raw/dd90a3030e3a7421d8e4d0f5f50f5092.png)按钮来关闭/开启画面和声音，单击关闭画面或声音系统依旧正常采集，但是无法预览，推流可以正常发起但是没有画面和声音。
> ? 推流成功后，采集预览的状态不支持变更，而且推流可能会产生对应的带宽/流量或其他增值服务费用。
> 
![](https://qcloudimg.tencent-cloud.cn/raw/65ac3b98bda7bff46adf9f41ab837c85.png)
	2. 采集方式为摄像头采集时，单击**开启美颜**，即可开启美颜能力。
![](https://qcloudimg.tencent-cloud.cn/raw/eec3cddc8d84e43037d240444a74a138.png)
	3. 美颜能力模块可以对画面中人物进行美化，增加互动贴纸以及提供美妆、虚拟背景等能力。
![](https://qcloudimg.tencent-cloud.cn/raw/8192f858c2a36f3aa86a3ac98b2a6429.png)
>! 美颜能力仅提供功能体验，并不包含在云直播产品服务范围内，了解产品情况，详见[腾讯特效](https://cloud.tencent.com/document/product/616/71399)。
8. 推流成功后您可在下方单击 **立即查看**，快速跳转至查看直播流推流相关数据。非当前账号推流地址无法获取推流数据和播放地址，您可以通过当前账号下的推流域名生成推流地址，或者使用拉流转推功能，将直播流同时转推到当前账号下。
![](https://qcloudimg.tencent-cloud.cn/raw/a454fda302348b25e5c72def9cea8f2c.png)
9. 若您在 **域名管理** 中已添加播放域名，即可在下方 **选择播放域名** 快速生成的播放地址。若您需生成有转码配置的播放地址，需先将播放域名绑定转码模板，才可生成播放转码流。
![](https://qcloudimg.tencent-cloud.cn/raw/35259f25d08b4e6e572fd02049a57ad7.png)
其中，播放地址由以下4部分组成：
![](https://main.qcloudimg.com/raw/72989c8f55fe7f2ed596bd09882f5a09.png)支持 RTMP、FLV 、 HLS 和 UDP 协议，可以单击播放地址后的二维码，通过 [腾讯云工具包 App](https://cloud.tencent.com/document/product/454/6555#rtmpdemo) 扫码查看播放地址：
![](https://qcloudimg.tencent-cloud.cn/raw/dd38347d6c9c1dbfa13b734953e91fb6.png)
>! 当选择的播放域名已开启 HTTPS 配置时，生成的 FLV 和 HLS 地址会默认带上 HTTPS。



## 多路混流
### 输入配置
1. 登录云直播控制台，选择 [**Web推流**](https://console.cloud.tencent.com/live/tools/webpush)，单击多路混流。
2. 在输入配置中单击**添加**。 选择采集方式。您可选择摄像头采集、屏幕分享采集和本地文件采集三种采集方式，并且可添加文本配置进行多路混流直播。**最多可添加10个输入源**。
<dx-tabs>
::: 摄像头采集
摄像头采集是通过摄像头/麦克风（支持外接）进行视频/声音的采集。单击 **开启摄像头**/ **开启麦克风**，首次开启需授予浏览器使用摄像头和麦克风权限。
![](https://qcloudimg.tencent-cloud.cn/raw/e4e48d5ca9baa920d51b1dc3c65d392d.png)
:::
::: 屏幕分享采集
屏幕分享采集是通过浏览器捕获对应窗口/界面进行分享采集。单击 **选择屏幕分享** 选择分享的内容，可为整个屏幕/某个窗口/浏览器标签页。需选择分享屏幕后才可进行保存。
屏幕分享采集支持选择音频源，目前只有 Chrome 74+ 和 Edge 79+ 支持采集声音，在 Windows 系统可以采集整个系统的声音，在 Linux 和 Mac 上面只能采集标签页的声音。
![](https://qcloudimg.tencent-cloud.cn/raw/f9ba4e4f4ac724d4dd14565fae61803b.png)
:::
::: 本地文件采集
本地文件采集是通过指定本地文件进行画面采集，再通过 Web 推流工具推送到云直播。单击 **选择本地文件** 选择需要推流的内容，目前支持选择 MP4、MP3、JPG、PNG和BMP 格式文件。单击开启预览才可进行保存。
![](https://qcloudimg.tencent-cloud.cn/raw/5477902000bba4bed26788e137402262.png)
:::
::: 文本配置
文本配置为混流画面添加文本，再通过 Web 推流工具推送到云直播。在文本内容中输入文本。
可在画面配置中对字体、颜色、阴影、透明度、粗细、文本坐标等进行配置。文本坐标默认是页面中间。
![](https://qcloudimg.tencent-cloud.cn/raw/30874e9c1663fae7f9c7151eb576c1a7.png)
:::
</dx-tabs>
4. 可对摄像头采集、屏幕分享采集、本地文件采集设置采集配置，默认为推荐配置（不同分辨率有不同推荐配置），采集过程中不支持切换或修改配置，需在关闭预览的情况下进行修改。
5. 可对摄像头采集、屏幕分享采集、本地文件采集设置高级配置，可对画面、坐标、镜像、对比度、亮度和饱和度进行调整。
6. 单击**保存**，该输入源添加进配置中。

### 修改配置
1. 在输入配置中，可对已配置的输入源进行操作。
2. 选择您需要修改配置的输入源，单击**配置**，右侧弹窗展示该输入源的配置信息，可重新修改配置信息。采集过程中不支持切换或修改配置，需在关闭预览的情况下进行修改。
3. 输入源之间可以通过拖动输入源左侧按钮上下调节其展示层级。
4. 单击**删除**可删除该输入源。
5. 单击**关闭画面**，则关闭该输入源的预览，但是在画面编辑中可以选中画面进行编辑。
6. 有音频输入的输入源可进行调节音量，单击调节音量，拖动音量条，单击**确定**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/89e5fec4c6c2e6ae83798e557b54cf5e.png)

### 推流配置
 **推流配置**。设置推流配置，默认为推荐配置（不同分辨率有不同视频码率的推荐配置，音频码率不支持修改），可在右上角单击 **编辑** 进入自定义编辑配置，可自定义修改视频码率和音频码率。
![](https://qcloudimg.tencent-cloud.cn/raw/00e84c0fd9fae84e4436f6343bcae805.png)
> ? web 推流的音频编码方式为 opus 编码，推荐使用快直播 WebRTC 地址进行播放。若使用标准直播的播放地址（RTMP/FLV/HLS），系统会自动转换为 aac 编码才能正常播放，从而会产生音频转码费用，详情请参见 [计费文档](https://cloud.tencent.com/document/product/267/39889#a_trans)。

### 画面编辑
1. 在确定输入配置以及推流配置后，可在右侧预览框中看到预览画面，并且可对画面进行画面编辑。
2. 单击**进入画面编辑**，选中预览框中需要调整的画面，可对画面进行拖动与缩放大小。
3. 调整完成后单击**退出画面编辑**，若是处于推流中，保存后将按新画面布局继续推流。
![](https://qcloudimg.tencent-cloud.cn/raw/5ca7c92917a1fa723b05ceb9fdc1e64a.png)

> ? 进入画面编辑可以在预览框中调整画面布局，退出画面编辑可在预览框中查看推流的预览画面，编辑页面不影响实时推流，退出编辑才会保存配置。

### 推流地址
1. 在预览框下输入 WebRTC 推流地址或单击 **快速生成**，进行以下配置：
2. 选择您的推流域名。
3. 编辑 AppName，用于区分同一个域名下多个 App 的地址路径，默认值为 live。
4. 填写自定义的流名称 StreamName，例如：`test`。
5. 选择过期时间，例如：`2023-03-06 00:00:00`。
6. 单击 **确定**，快速自动生成 WebRTC 推流地址填入地址栏。
![](https://qcloudimg.tencent-cloud.cn/raw/3d26b186e774cbc5c6739e1e9e18d450.png)

### 开始推流
1. 单击 **开始推流**，即可开始推流。您可单击![](https://qcloudimg.tencent-cloud.cn/raw/b2390afbbc7b72bfeee8c2c5b2ad09cf.png)和![](https://qcloudimg.tencent-cloud.cn/raw/dd90a3030e3a7421d8e4d0f5f50f5092.png)按钮来关闭/开启画面和声音，单击关闭画面或声音系统依旧正常采集，但是无法预览，推流可以正常发起但是没有画面和声音。
2. 推流成功后您可在下方单击 **立即查看**，快速跳转至查看直播流推流相关数据。非当前账号推流地址无法获取推流数据和播放地址，您可以通过当前账号下的推流域名生成推流地址，或者使用拉流转推功能，将直播流同时转推到当前账号下。
![](https://qcloudimg.tencent-cloud.cn/raw/a2a021b2f67070abb5e3eefb5fed42ac.png)
3. 若您在 **域名管理** 中已添加播放域名，即可在下方 **选择播放域名** 快速生成的播放地址。若您需生成有转码配置的播放地址，需先将播放域名绑定转码模板，才可生成播放转码流。
![](https://qcloudimg.tencent-cloud.cn/raw/972f34258b1727a8f7a71b2c67bbbc96.png)
其中，播放地址由以下4部分组成：
![](https://main.qcloudimg.com/raw/72989c8f55fe7f2ed596bd09882f5a09.png)
支持 RTMP、FLV 、 HLS 和 UDP 协议，可以单击播放地址后的二维码，通过 [腾讯云工具包 App](https://cloud.tencent.com/document/product/454/6555#rtmpdemo) 扫码查看播放地址：
![](https://qcloudimg.tencent-cloud.cn/raw/353b82aee9d5f895106adcf49828183a.png)

>! 当选择的播放域名已开启 HTTPS 配置时，生成的 FLV 和 HLS 地址会默认带上 HTTPS。
