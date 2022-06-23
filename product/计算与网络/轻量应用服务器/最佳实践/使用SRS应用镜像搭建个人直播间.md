## 操作场景
SRS 是一个简单高效的实时视频服务器，支持 RTMP、WebRTC、HLS、HTTP-FLV、SRT/GB28181。

轻量应用服务器提供了 SRS 应用镜像，使您无需再关注繁杂的部署操作，即可通过该镜像在轻量应用服务器上一键搭建个人直播间。


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
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，在“服务器”页面单击**新建**。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
其中，“镜像”选择为**应用镜像** > **SRS音视频服务器 4.2**，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。
<dx-alert infotype="explain" title="">
- 若您想使用已创建的实例搭建直播间，则可使用 SRS 应用镜像 [重装系统](https://cloud.tencent.com/document/product/1207/44576)。
- 本文以使用应用镜像 SRS 音视频服务器 4.2 版本为例，镜像可能会进行版本升级与更新，请您以购买页实际版本为准。
</dx-alert>

### 配置实例
1. 在“服务器”页面中，选择并进入实例详情页。
2. 选择**防火墙**页签，单击**添加规则**后根据界面提示放通1935端口。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4a3c7246c4fdbd2a6c799904c4035b8a.png)
3. 选择**应用管理**页签，单击“应用内软件信息”中的“访问地址”，进入 SRS 后台管理页面。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8bd99160e7a95d061f75c94ebb610234.png)
4. 首次进入 SRS 后台管理页面需设置管理员密码，请根据页面提示进行设置，并妥善保管。
5. [](id:Step5)设置完成后，登录 SRS 后台管理页面，记录 OBS 推流地址及密钥。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5b16713695f4d65e0d03ac34bb4fb07e.png)



### 安装及配置 OBS 推流软件
1. 本文以选择 OBS 推流方式为例，请前往 [OBS 官网](https://obsproject.com/) 下载软件安装包，并完成安装。
2. 运行 OBS 推流软件，界面基本介绍如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4b712444756153f7fee95bc832dc1104.png)
  1. 直播画面。
  2. 场景分类。
  3. 媒体源设置。
  4. 音频设置。
  5. 直播设置。
  如需了解 OBS 推流软件更多信息，可前往 [OBS 官网](https://obsproject.com/)。
3. 选择界面左上角的**文件** > **设置**。
4. 在“设置”页面中，选择左侧菜单中的**推流**，并进行以下设置。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3e29c5b1e1ecc8cc95f62d0aeff8dab8.png)
 - **服务**：选择下拉列表中的“自定义”。
 - **服务器**：输入 [步骤5](#Step5) 中已获取的 OBS 推流地址。
 - **串流密钥**：输入 [步骤5](#Step5) 中已获取的串流密钥。
5. 单击**确定**。
6. 在主界面的“媒体源设置”中选择**媒体源**，并单击“直播设置”中的**开始推流**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/415a1ca1d1e18fb1987c913d8cfe17fb.png)
7. 在弹出的“创建或选择源”窗口中，按需创建或选择已有源，单击**确定**。
8. 在弹出“属性 '媒体源'”窗口中，选择要推流（直播）的内容。本文以选择本地的视频资源为例，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1d8051c9e6382f850fd5eb52067e8c26.png)
9. 单击**确定**上传并开始推流，画面效果如下图所示。您可在 OBS 中右键单击画面，实时调整直播画面（例如大小、方向等）。
![](https://qcloudimg.tencent-cloud.cn/raw/30e383f95dbfb24db9308ff26ca32c50.png)

### 查看直播间
1. 前往“服务器”页面，进入 SRS 实例详情页。
2. 选择**应用管理**页签，单击“应用内软件信息”中的“访问地址”，进入 SRS 后台管理页面。
3. 单击 **HTTP-FLV流**或 **HLS流**，即可查看直播画面。
 ![](https://qcloudimg.tencent-cloud.cn/raw/3def08ab0d4c3cadeed714783dced090.png)
直播画面如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cd18a87b3f37189236828103728ee872.png)

