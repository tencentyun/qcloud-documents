## 操作场景
SRS 是一个开源的流媒体集群，主要应用在直播和 WebRTC，支持 RTMP、WebRTC、HLS、HTTP-FLV 和 SRT 等常用协议。

轻量应用服务器提供了 SRS 应用镜像，使您无需再关注繁杂的部署操作，即可通过该镜像在轻量应用服务器上一键搭建个人直播间。在本地下载推流客户端并且填写推流地址后，即可进行直播。除此之外，超清实时直播、多平台转播、直播录制等服务一应俱全，您可按需选择。


## 相关协议

<dx-accordion>
::: HTTP-FLV
HTTP-FLV 是 Adobe 公司推出的另一种视频格式（在网络上传输的流媒体数据存储容器格式），相对简单轻量，无需大量的媒体头部信息，整个 FLV 由 The FLV Header、The FLV Body 以及其他 Tag 组成，因此加载速度极快。

FLV（全称 FlashVideo）是一种网络视频格式，以体积小、加载速度极快的特性著称，采用 FLV 格式封装的文件后缀为 `.flv`。而 HTTP-FLV  即将流媒体数据封装成 FLV 格式，再通过 HTTP 协议传输给客户端。

:::
::: HLS
HLS（全称 HTTP Live Streaming）是 Apple 的动态码率自适应技术，主要应用在 PC 以及 Apple 终端的音视频服务。HLS 并不是一次请求完整的数据流，它会在服务器端将流媒体数据切割成连续的时长较短的 ts 小文件，并通过 M3U8 索引文件按序访问 ts 文件。客户端只需不停的按序播放从服务器获取到的文件，从而实现播放音视频。

相比于 HTTP-FLV，HLS 的优势如下：
 -  Apple 全系列原生支持，同时在 Android 和 PC 端也有很好的支持。
 - 给予 HTTP/HTTPS 传输，有效避免防火墙拦截。
 - 具备高性能。

但由于传输协议的特点，造成以下不足：
- 实时性较差，时延往往会大于10s。
- 由于文件切片传输的特性，会考验存储和缓存的性能。
:::
</dx-accordion>
<br>
综合两种传输协议特点，HTTP-FLV 会在互动直播（例如直播带货）的场景下发挥最优效果，而 HLS 在一些对时延不敏感的场景（例如一般直播）会更加适用。


## 操作步骤

### 使用 SRS 应用镜像创建实例
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，在 **服务器** 页面单击 **新建**。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
  - **镜像**：选择为应用模板 > 音视频场景 > SRS 音视频服务器应用模板，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。
<dx-alert infotype="explain" title="">
 - 应用模板即应用镜像。
- 查看镜像说明详情请参见 [基本概念](https://cloud.tencent.com/document/product/1207/79254)。
</dx-alert>
<dx-alert infotype="explain" title="">
- 若您想使用已创建的实例搭建直播间，则可使用 SRS 应用镜像 [重装系统](https://cloud.tencent.com/document/product/1207/44576)。
- 本文以使用应用镜像 SRS 音视频服务器 4.5 版本为例，镜像可能会进行版本升级与更新，请您以购买页实际版本为准。
</dx-alert>

### 配置实例
1. 在“服务器”页面中，选择并进入实例详情页。
2. 选择**防火墙**页签，单击**添加规则**后根据界面提示放通1935端口。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/12514c4de792b70add4f076bd25b1b86.png)
3. 选择**应用管理**页签，单击“应用内软件信息”中的“访问地址”，进入 SRS 后台管理页面。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c7cd46b518f1d1fc1ca83ab7ec9e001c.png)
4. 首次进入 SRS 后台管理页面需设置管理员密码，请根据页面提示进行设置，并妥善保管。
5. [](id:Step5)设置完成后，登录 SRS 后台管理页面，记录 OBS 推流地址及密钥。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ee31200bd5cef609aedc66d17adbb2d9.png)

### 安装及配置 OBS 推流软件
1. 本文以选择 OBS 推流方式为例，请前往 [OBS 官网](https://obsproject.com/) 下载软件安装包，并完成安装。
2. 运行 OBS 推流软件，界面基本介绍如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a38727518482862002976269e59dea7d.png)
  1. 直播画面。
  2. 场景分类。
  3. 媒体源设置。
  4. 音频设置。
  5. 直播设置。
  如需了解 OBS 推流软件更多信息，可前往 [OBS 官网](https://obsproject.com/)。
3. 选择界面左上角的**文件** > **设置**。
4. 在“设置”页面中，选择左侧菜单中的**直播**，并进行以下设置。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6859dca114483ac366b5c84f55d597e1.png)
 - **服务**：选择下拉列表中的“自定义”。
 - **服务器**：输入 [步骤5](#Step5) 中已获取的 OBS 推流地址。
 - **推流码**：输入 [步骤5](#Step5) 中已获取的串流密钥。
5. 单击**确定**。
6.  在主界面的“媒体源设置”中，选择 <img src="https://qcloudimg.tencent-cloud.cn/raw/590204a737fb7b1c194c6b44771de307.png" style="margin:-3px 0px"/>，在弹出菜单中，根据直播的内容选择源（本文直播内容以本地视频为例，则选择**媒体源**）。
7. 在弹出的“创建或选择源”窗口中，按需创建或选择已有源，单击**确定**。
8. 在弹出“属性 '媒体源'”窗口中，选择要推流（直播）的内容，单击**确定**。本文以选择本地的视频资源为例，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1d8051c9e6382f850fd5eb52067e8c26.png)
9. 单击“直播设置”中的**开始直播**(点击后会变成**停止直播**)，画面效果如下图所示。您可在 OBS 中右键单击画面，实时调整直播画面（例如大小、方向等）。
![](https://qcloudimg.tencent-cloud.cn/raw/0ddd02cf2cef6709a3065072c0b19013.png)
此时，您已可 [观看直播](#watchLive)，若您有使用多平台转播、云录制、云点播、本地录制等需求，请参考下文继续配置。


## 相关操作

### 多平台转播
若私人直播间的流量已无法满足您的需求，可参考本步骤使用 SRS 提供的多平台转播功能。

1. 前往“服务器”页面，进入 SRS 实例详情页。
2. 选择**应用管理**页签，单击“应用内软件信息”中的“访问地址”，进入 SRS 后台管理页面。
3. 选择**多平台转播**，选择目标平台，并填写从目标平台获取的推流地址及推流密钥。如下图所示：
<dx-alert infotype="explain" title="">
您需已在目标直播平台创建直播。
</dx-alert>
<img src="https://qcloudimg.tencent-cloud.cn/raw/acf64c48e9fcc4314561ac3396ab265a.png"/>
4. 单击**更新配置**后，勾选“开启转推”即可将直播流推向目标平台。




### 本地录制
若您需将录制的直播内容存储在 SRS 实例磁盘中，可参考以下步骤使用本地录制功能。

1. 使用本地录制功能前，您需选择**组件管理**，将 **Host(主机管理)**升级到 v1.0.252 及以上版本。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/83854b39ef4a64b2db9351625d729ee4.png)
2. 在 SRS 后台管理页面中，选择**录制**页签。
2. 在**本地录制**的“设置录制规则”中，勾选“录制所有流”并单击**提交**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/148a04395e12852faf2d99bc49163f62.png)
3. 开始推流，大约等待10 - 60秒之后，可在“录制任务列表”中查看正在录制的流。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9278935682404bc0dfc175a4698b2444.png)
您可进行以下操作：
  - **录制预览**：在录制过程中可单击**预览**，实时查看录制的效果。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/afba30c0e7314ad79f349056659720e2.png)
  - **下载录制视频到本地**：录制结束后，可以在预览页面单击鼠标右键，在弹出菜单中选择下载 MP4 文件。如下图所示：
 ![](https://qcloudimg.tencent-cloud.cn/raw/41b735cfb53ea89ac270dcd36edb2d2f.png)
4. 实例保存录制视频的路径，可在“录制文件夹”中查看。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e20a4393c954de96f639605177753377.png)



### 云录制及云点播指南

#### 云录制
若您的使用场景相对单一，例如希望将直播内容保存，并且后续进行剪辑等操作，建议您使用云录制。

在直播的场景下，录制同样是重要的。直播的内容在录制并存储后，可进行二次创作并再次分发。但如果将录制的内容存储在本地磁盘，则会造成空间不足或数据丢失的压力。SRS 并不直接对接云存储，而是 SRS 服务器使用 SRS 的回调 on_hls，将 HLS 切片保存在 Local Disk 或 Cloud Storage。Local Disk 指 SRS 服务器的本地磁盘。Cloud Storage 则是指对象存储 COS 或云点播 VoD。

此时可通过 SRS 近期更新的重磅功能云录制，来很好的解决该问题。云录制将直播内容以 HLS 格式存储在了 COS 中，可以认为 COS 是个无限容量的磁盘（消耗存储空间遵循 COS 计费规则），使用云录制可避免录制内容撑爆 SRS 云服务器的磁盘。


#### 云点播
如果业务场景比较丰富，建议您选择云点播。

云点播是指转换视频流到腾讯云云点播 VoD 服务，只要推送至服务器的流均可以对接云点播。除了提供基础的存储服务外，还具备媒体 AI、媒体处理以及版权保护的能力。



#### 云录制操作示例
SRS 云录制及云点播使用简单且操作步骤接近，本文以云录制为例，介绍如何在 SRS 中使用云录制功能。步骤如下：
1. 在 SRS 后台管理页面中，选择**云录制**页签，即可查看云录制场景介绍及使用说明。
2. 在“设置云密钥”中，输入 SecretId 及 SecretKey。如下图所示：
<dx-alert infotype="explain" title="">
SecretId 及 SecretKey 可前往 [API密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取。
</dx-alert>
<img src="https://qcloudimg.tencent-cloud.cn/raw/b598935206cc159c0b107ec4b149799f.png"/>
3. 单击**设置账号**。
4. 在“设置录制规则”中，勾选“录制所有流”后单击**提交**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d71892eb7cc042fb0aa86e0c22192db8.png)
5. 开始推流，大约等待10 - 60秒之后，可在“录制任务列表”中查看正在录制的流。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/47c38ba989df6af22215b55ad3e0a8fb.png)
您可进行以下操作：
  - **录制预览**：在录制过程中可单击**预览**，实时查看录制的效果。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/afba30c0e7314ad79f349056659720e2.png)
  - **录制视频管理**：录制结束后，可复制 HLS 链接，或进入存储桶进行管理。



### 观看直播[](id:watchLive)
在 SRS 后台管理页中，单击播放的流 HTTP-FLV 流或 HLS 流中的**简易**或**西瓜**，即可进入直播画面。
![](https://qcloudimg.tencent-cloud.cn/raw/7fd8f5d7550b16b5e1c55a1430eb51a9.png)
<dx-alert infotype="explain" title="">
此时您用浏览器或手机浏览器打开链接时，可能会查看“网站连接不安全”的类似提示。您可参考 [一键设置 HTTPS](#autoHTTPS) 进行处理。
</dx-alert>
将链接分享给粉丝和观众后，即可收看您的直播。画面如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/d371c2acedf073076166926442768cfe.png"/>



### 一键设置 HTTPS[](id:autoHTTPS)
此时您的 SRS 实例未设置 HTTPS，在使用浏览器或手机浏览器打开链接时，可能会查看“网站连接不安全”的类似提示。您可参考以下步骤，使用 SRS 提供的自动设置 HTTPS 功能。

<dx-alert infotype="explain" title="">
使用一键设置 HTTPS 功能前，您需具备域名，并已将域名解析至 SRS 实例。
</dx-alert>

1.  在 SRS 后台管理页面中，选择**系统配置** > **HTTPS** 页签，在“域名”中输入您的域名。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/610493f7b31c69be6ad6a889cc0de59c.png)
2. 单击**申请证书**，等待证书申请成功即可。






