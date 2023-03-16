## 方案背景
Open Broadcaster Software（简称 OBS）是一款好用的第三方开源程序直播流媒体内容制作软件，为用户提供免费使用，它可支持 OS X、Windows、Linux 操作系统，适用多种直播场景，满足大部分直播行为的操作需求，您可以到 [OBS 官网下载](https://obsproject.com/download?spm=a2c4g.11186623.2.15.6aac1445JPlKR8) 最新版本软件。
以下视频将指导您在安装 OBS 工具后，如何在 PC 端进行推流配置操作。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2300-33494?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 准备工作
- 安装 [OBS](https://obsproject.com/download?spm=a2c4g.11186623.2.15.6aac1445JPlKR8) 工具。
- 已 [开通云直播服务](https://console.cloud.tencent.com/live)，并准备已备案的域名，[添加为播放域名](https://cloud.tencent.com/document/product/267/20381)（系统提供默认的推流域名可以使用，也可以添加自定义域名推流）
>? [9.9元可享100GB直播流量包](https://cloud.tencent.com/act/pro/cssall)，入门级小额体验包，低成本快速体验音视频直播服务，更多规格资源包 [立即前往选购](https://buy.cloud.tencent.com/live)。

[](id:step0)
## 获取推流地址
1. 登录云直播控制台，进入 [**地址生成器**](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)，进行如下配置：
   1. 选择生成类型为**推流域名**。
   2. 选择您已添加到域名管理里对应的域名。
   3. AppName 为区分同一个域名下多个 App 的地址路径，默认为 live。
   4. 填写自定义的流名称 StreamName，例如：`live`。
   5. 选择地址过期时间，例如：`2023-03-04 17:46:46`。
3. 单击 **生成地址** 即可获取 OBS 推流地址。

![](https://qcloudimg.tencent-cloud.cn/raw/cb590394ab312eda310cbd0693c04da1.png)

[](id:normal)
## OBS 在线推流
### 步骤一：设置推流地址[](id:step1)
1. 打开 OBS，您可通过底部工具栏的 **控件 > 设置** 按钮进入设置界面。
![](https://qcloudimg.tencent-cloud.cn/raw/33d08fc6a5efac0314566b8bab371cf6.png)
2. 单击 **直播** 进入流设置页签，选择服务类型为自定义流媒体服务器。
3. 将获取所得的 [推流地址](#step0) 填写到服务器和推流码中。
    - 服务器：对应"OBS 服务器"，即`rtmp://domain/AppName/`。
    - 推流码：对应“OBS 串流密钥”，即`StreamName?txSecret=xxxxx&txTime=5C1E5F7F`。
    ![](https://qcloudimg.tencent-cloud.cn/raw/26fa69032ad5f23e15a8e70e6f8496e8.png)
4. 单击 **确定** 保存设置信息。

### 步骤二：推流引导设置[](id:step2)
>? 若您需进行码率、录像等配置，可单击顶部工具栏，选择 **工具>自动配置向导**，按 OBS 的引导进行推流设置。

1. 查看底部工具栏的 **来源** 标签。
![](https://qcloudimg.tencent-cloud.cn/raw/acafb105ccf3fde0482f6d42cb28227a.png)
2. 单击 **+** 按钮，按需选择输入源，例如：显示器捕获。
 ![](https://qcloudimg.tencent-cloud.cn/raw/442261dc4d4d4a56739395871298ee47.png)
    **常用直播来源输入介绍**
<table>
<thead><tr><th width="20%">输入源</th><th>说明</th></tr></thead>
<tbody><tr>
<td>图像</td>
<td>适用于单张图像直播。</td>
</tr><tr><td>图像幻灯片放映</td>
<td>可循环或者顺序多张播放图片。</td>
</tr><tr><td>场景</td>
<td>实现各种强大的直播效果。此时，另一个场景是作为来源被添加进当前场景的，可以实现整个场景的插入。</td>
</tr><tr><td>媒体源</td>
<td>可上传本地视频，并本地点播视频文件进行直播化处理。</td>
</tr><tr><td>文本</td>
<td>实时添加文字在直播窗口中。</td>
</tr><tr><td>显示捕获</td>
<td>可实时动态捕捉您电脑桌面的操作，电脑桌面中所有的操作均执行直播。</td>
</tr><tr><td>游戏源</td>
<td>允许对指定来源的游戏进行直播。适用于大小游戏的实况直播。</td>
</tr><tr><td>窗口捕获</td>
<td>可根据您选择的窗口进行实时捕获，直播仅显示您当前窗口内容，其他窗口不会进行直播捕获。</td>
</tr><tr><td>色源</td>
<td>使用这个来源可以添加一个色块到您的场景中，作为一个背景色。该色块可以调节透明度，成为全屏透明色彩。</td>
</tr><tr><td>视频采集设备</td>
<td>实时动态捕捉摄像设备，可将摄像后的画面进行直播。</td>
</tr><tr><td>音频输入采集</td>
<td>用于音频直播活动（音频输入设备）。</td>
</tr><tr><td>音频输出采集</td>
<td>用于音频直播活动（音频输出设备）。</td>
</tr>
</tbody></table>

### 步骤三：开启工作室模式[](id:step3)
工作室模式下可以对当前直播的内容进行实时编辑，并在编辑过程中进行过渡动画的场景切换，从而实现在对用户体验影响最低的程度下进行直播内容的编辑。
1. 查看底部工具栏的 **控件** 标签，单击 **工作室模式**。
2. 单击 **转场特效** 即可将预览窗的直播画面过渡到输出窗口。
![](https://qcloudimg.tencent-cloud.cn/raw/f827e8514fb74f70fdc88904593963b6.png)

### 步骤四：直播推流[](id:step4)
1. 查看底部工具栏的 **控件**。
2. 单击 **开始直播**，即可将视频流推送到设置的推流地址。
![](https://qcloudimg.tencent-cloud.cn/raw/b3100da48798fc80a0d258ff453d52bb.png)

>? 
>- 底部出现![](https://qcloudimg.tencent-cloud.cn/raw/f35b2416e3bdb730565f5e817c5ebed7.png)绿灯，表示推流成功。
>- 若需停止推流，单击 **停止推流** 即可。

## 其他推流相关配置
### 影响直播延迟相关设置
1. 通过 **控件>设置>输出**。
2. 选择 **输出模式** 为 `高级`，即可对 **关键帧间隔** 等进行配置，**关键帧间隔（GOP）过大**会影响快直播体验，大小建议设置 2s。设置方法如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/cd5a40f69ba84f56410d4279b77b4923.png)
3. 同时在左侧导航栏，选择 **高级**，即可对 **直播延迟** 进行设置：
![](https://qcloudimg.tencent-cloud.cn/raw/f3e44d437ff158ca5bccc9a2f7aeb548.png)

### 关于快直播去除 B 帧设置
快直播 Web 方案**不支持 B 帧解码播放**，所以如果原始流存在 B 帧，则后台会自动进行转码去掉 B 帧，但这样会引入额外的转码延迟，并且会**产生转码费用**。建议尽量不推包含 B 帧的流，用户可以通过调整推流端软件（如 OBS）的视频编码参数来去除 B 帧。如果使用 OBS 推流，可以通过设置，关闭 B 帧。如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/77c00afcfeadd53e492bbe6354d49e27.png)

### 本地直播录制相关设置
若您有直播时进行本地录制的需求，可以选择直播时在本地进行录制备份，设置方法如下：
1. 单击 **控件>设置>输出** 进入输出设置页签。
2. 在 **录像** 设置栏中进行对应的配置，单击 **确定** 即可将录制文件进行本地保存。
![](https://qcloudimg.tencent-cloud.cn/raw/1bef3b230d6018395edfecd55bf7db58.png)
3. 单击 **视频** 设置视频分辨率与帧率信息，如下图所示：
>? 分辨率决定了观众看到的画面清晰程度，分辨率越高画面越清晰。FPS 是视频帧率，它控制观看视频的流畅，普通视频帧率有24帧 - 30帧，低于16帧画面看起来有卡顿感，而游戏对帧率要求比较高，一般小于30帧游戏会显得不连贯。
>
![](https://qcloudimg.tencent-cloud.cn/raw/da3d9793ffd64c270b456065faee7eeb.png)

### 推流转码相关设置
若您在推流过程中需要修改视频的码率，具体操作如下：
1. 通过底部的 **控件>设置** 按钮进入设置界面。
2. 单击 **输出** 页签，选择输出模式为“简单”。
3. 填写视频比特率，单击 **确定** 即可。
![](https://qcloudimg.tencent-cloud.cn/raw/8406f503a65ddfc17a004e37d009b8ef.png)




## 更多操作说明
### 纯音频推流
根据 OBS 官方论坛的解答，当前 OBS Studio 23.2.1 以及之前版本不支持纯音频推流。
为实现近似音频推流，您可以参考下面的步骤进行设置。此方法的主要思路是采用静态画布（黑屏或者图片）替代视频。如果您需要降低带宽，可以降低视频的帧率和码率，以此来逼近纯音频推流，但直播流中仍会有视频数据。
1. 参照 [推流引导设置](#step2)，添加 **音频输入采集** 输入源作为输入源，不能添加视频输入源或者添加图片作为视频输入源。
![](https://qcloudimg.tencent-cloud.cn/raw/c93d903b4183d730c4705333ac34a7b0.png)
2. 进入 **控件>设置>视频** 页面。
3. 将 **输出（缩放）分辨率** 选到最小，同时将 **常用 FPS 值（帧率）** 选到最小，单击 **确定** 保存配置。
![](https://qcloudimg.tencent-cloud.cn/raw/666e8a8e262e0c1b0028eb516de16260.png)
4. 单击 **输出** 进入输入设置页面，按下图配置，此处需将 **比特率** 设置到最低。单击 **确定** 保存配置。
![](https://qcloudimg.tencent-cloud.cn/raw/068cc1ec7fb55343ce186a9c39f0f1f6.png)
5. 参照 [OBS 推流在线推流](#normal) 中的步骤实现直播推流，这样能听到音频，视频的内容是黑屏或者一张图片。于此同时，视频的码率最低，占用的带宽显著降低。

### 视频轮播
<dx-tabs>
::: 单个文件循环播放设置方法
1. 在底部工具栏的 **来源** 标签中，单击 **+** 添加 **媒体源**，在弹出框中的 **本地文件** 选择要轮播的视频文件，勾选 **循环**，然后单击 **确定** 即可。
![](https://main.qcloudimg.com/raw/08f3d93083fe55c31e510d6069cf33d7.png)
2. 按照 [OBS 推流设置](#step1) 步骤，设置 **推流** 页面中的 **服务器** 和 **串流密钥** 项，开始推流即可实现单个文件轮播。
:::
::: 多个文件循环轮播方法
OBS本身不支持多个文件循环播放，但借助窗口捕获可以实现多个文件轮播。
1. 下载 [QQ 影音](https://player.qq.com/) 并安装。
2. 在 QQ 影音中添加需要轮播的视频文件，并设置为列表循环播放。
3. 开始播放第一个视频文件，然后隐藏右侧播放列表。
![](https://main.qcloudimg.com/raw/c1401db40457036f4a0c06e6266f03cb.png)
4. 打开 OBS，在 **来源** 中单击 **+** 添加 **窗口捕获**，在 **窗口** 选项找到 QQPlayer.exe，捕获到对应播放内容，单击 **确定**。
![](https://main.qcloudimg.com/raw/16aa802a5598db48e3e86f37f1b6c374.png)
5. 按照 [OBS 推流设置](#step1) 步骤，在 **推流** 页面中设置 **服务器** 和 **串流密钥** 完成后，开始推流。
6. 在 OBS 窗口上，调整窗口大小，上下拖动，隐藏播放器边框和按钮，即可实现多文件轮播。
![](https://main.qcloudimg.com/raw/d0b59b014734921a58b771ff9ce66391.png)
:::
</dx-tabs>

## 拉流
推流完成后，您可生成与推流地址相同的 StreamName 的播放地址，通过以下方式拉流播放来验证流是否推成功：
- PC 端：支持使用 [VLC 播放器](https://cloud.tencent.com/document/product/267/32727) 进行拉流。
- 移动端：支持通过集成 [腾讯云视立方·直播 SDK](https://cloud.tencent.com/document/product/454/) 来实现播放。
>? 腾讯云视立方·直播 SDK 是云直播服务（CSS）在移动场景的延伸。相比于主要面向云对接的直播（CSS） 服务，直播 SDK 既提供了基于 RTMP SDK 的“快速集成方案”，也提供了集标准直播（LVB）、快直播（LEB）、云点播（VOD）、即时通信（IM） 和对象存储（COS） 等多云端服务的“一体化解决方案”。
其中， [快直播](https://cloud.tencent.com/document/product/454/55880) （Live Event Broadcasting，LEB）（超低延时直播）是标准直播在超低延时播放场景下的延伸，比传统直播协议延时更低，为观众提供毫秒级的直播观看体验。 能够满足一些对延迟性能要求更高的特定场景需求，例如在线教育、体育赛事直播、在线答题等。

