## 版本说明 
+ **版本相关信息**
  - 版本号：3.4.1757 @ 2017-09-18

+ **直播相关优化**
  - iOS & Android：引入推流加速技术，当您推流到腾讯云的 rtmp 地址时，可以开启 <font color='purple'>TXLivePushConfig::enableNearestIP</font> 开关，此时SDK会使用 **推流+** 加速后的推流通道传输主播的音视频数据，使推流质量获得较大提升，如下是 SDK 和 其他直播软件的对比效果。（推其他云商请关闭 enableNearestIP 开关）
![](//mc.qcloudimg.com/static/img/12e966a39dc5eba5701cb2e310b16ccb/image.jpg)
  - iOS & Android：大幅优化连麦时的底层网络组件的抗抖动能力，并对AEC回音消除组件进行了更好的机型适配，使连麦场景的体验更加流畅和易用。
  - iOS & Android：对美颜模块进行了彻底重构，将原有的磨皮和滤镜进行了大幅的优化和归并，在提升美颜效果的同时进一步降低了GPU使用率，缓解了发热问题。
  ![](//mc.qcloudimg.com/static/img/aac647073cf0641141900e775e929418/image.png)
  - iOS & Android：对内部音视频引擎进行了模块化重构，用于降低后续的版本的维护成本，进一步提升版本迭代速度。
  
+ **点播相关优化**
  - iOS & Android：对点播播放器进行了内部重构，支持 x2 x4 等多倍速播放，使用 <font color='purple'>TXLivePlayer::setRate</font> 接口设置播放倍速（此功能仅适用于点播）。
  - iOS & Android：对点播播放器进行了内部重构，可以使用 <font color='purple'>TXLivePlayer::setAutoPlay</font> 设置手动播放，用于播放视频前插入广告之用。

+ **短视频相关优化**
  - iOS & Android：为 TXUGCRecord 增加了 pauseRecord 和 resumeRecord 接口，用于支持多段录制。
  - iOS：提供了快速裁剪和编辑接口，1s 内完成视频裁剪和视频拼接。由 <font color='purple'>quickGenerateVideo</font> 接口 和 <font color='purple'>quickJoinVideo</font> 接口提供。
  - Android : 为编辑器增加了滤镜功能。
  - Android : 修复了部分机型视频录制、裁剪和拼接的兼容性问题。
![](//mc.qcloudimg.com/static/img/f2820e0ee0c5116b97f120a02203092f/image.png)

+ **接口变更**
  - iOS：TXLivePush 的 setBeautyFilterDepth 接口修改为 setBeautyStyle，并增加了两个参数。
  - Android：TXLivePusher 的 setBeautyFilter 接口增加了两个参数。
  - Android：TXUGCRecord、TXVideoEditer、TXVideoJoiner、TXUGCPublish 从原来的 <font color='purple'>com.tencent.rtmp</font> 移到了 <font color='purple'>com.tencent.ugc</font> 下。

+ **历史版本**
  - 上一版 SDK 下载地址为 [SDK Ver.2.0.5](https://cloud.tencent.com/document/product/454/10776)，历史版本功能说明详见 [变更历史](https://cloud.tencent.com/document/product/454/7878)。


## 下载地址
<style>
table th:nth-of-type(1) {  width: 150px; }
table th:nth-of-type(2) {  width: 150px; }
table th:nth-of-type(3) {  width: 150px; }
table th:nth-of-type(4) {  width: 150px; }
table th:nth-of-type(5) {  width: 150px; }
table th:nth-of-type(6) {  width: 150px; }
table th:nth-of-type(7) {  width: 150px; }
table td { height: 35px; }
.markdown-text-box img {
    border: 0;
    max-width: 100%;
    height: auto;
    box-sizing: content-box;
    box-shadow: 0 0 0px #ccc;
    margin: 0px 0;
}
</style>

- **iOS 平台**

|     iOS        | 直播精简版 | 独立播放器版 | 短视频功能版 | 全功能专业版 | 重命名专业版 | 商用企业版 |重命名企业版|
| :------------: | :------------: | :--------------: | :--------------: | :---------------: | :-----------: | :-----------: | :-----------: |
| RTMP推流  |![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png) | | | ![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 直播播放  |![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png) |![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)| | ![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 点播播放  |![](//mc.qcloudimg.com/static/img/2e00c5e35962f177efb87c8ed2c037dd/image.jpg) |![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png) |![](//mc.qcloudimg.com/static/img/2e00c5e35962f177efb87c8ed2c037dd/image.jpg)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 视频通话  ||||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 短视频录制  |||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 短视频编辑  |||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 多视频合并  |||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 短视频发布  |||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 动效贴纸 ||||||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 美瞳瘦脸 ||||||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 绿幕抠图 ||||||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 符号重命名 |||||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 支持BitCode |![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)||||
||[DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/3.4/TXLiteAVSDK_Smart_iOS_3.4.1757.zip)| [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/3.4/TXLiteAVSDK_Player_iOS_3.4.1757.zip) | [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/3.4/TXLiteAVSDK_UGC_iOS_3.4.1757.zip) | [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/3.4/TXLiteAVSDK_Professional_iOS_3.4.1757.zip)| [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/3.4/TXLiteAVSDK_Professional_Rename_iOS_3.4.1757.zip)| [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/3.4/TXLiteAVSDK_Enterprise_iOS_3.4.1757.zip)| [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/3.4/TXLiteAVSDK_Enterprise_Rename_iOS_3.4.1757)|

- **Android 平台**

|   Android    | 直播精简版 | 独立播放器版 | 短视频功能版 | 全功能专业版 | 商用企业版 |
| :------------: | :------------: | :--------------: | :--------------: | :---------------: | :-----------: |
| RTMP推流  |![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png) | | | ![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)| ![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 直播播放  |![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png) |![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)| | ![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)| ![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 点播播放  |![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png) |![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png) |![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 视频通话  ||||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 短视频录制  |||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 短视频编辑  |||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 多视频合并  |||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 短视频发布  |||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 动效贴纸 |||||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 美瞳瘦脸 |||||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| 绿幕抠图 |||||![](//mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png)|
| |[DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/3.4/LiteAVSDK_Smart_Android_3.4.1757.zip)| [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/3.4/LiteAVSDK_Player_Android_3.4.1757.zip) | [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/3.4/LiteAVSDK_UGC_Android_3.4.1757.zip) | [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/3.4/LiteAVSDK_Professional_Android_3.4.1757.zip)| [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/3.4/LiteAVSDK_Enterprise_Android_3.4.1757.zip) | 

- **版本说明**

> 1. 除精简版之外，SDK 各功能版本均打包有 ijkplayer，如果您的工程中已使用 ffmpeg，可能会导致符号冲突。为解决这个问题，您可以使用我们经过符号处理的 rename 版 SDK。

> 2. 商用企业版相较于专业版，增加了基于腾讯优图实验室专利技术的人脸特效功能，该版本非免费提供，需要解压密码和授权 license 才能运行，解码密码和授权 license 请联系腾讯云商务获取。使用方法见 [特效功能](https://cloud.tencent.com/document/product/454/9018)。
>  
> 3. iOS 直播精简版中没有包含软实现的编解码器，SDK 被压缩至最小（安装包体积增量 1M 左右），但此版本不支持 iOS 7.0 及以下系统。
>  
> 4. iOS 直播精简版和短视频功能版中所包含的点播播放器，主要基于系统原生接口实现，所以兼容性略逊于完整版，如果您的视频源中包含用于自己上传的视频，会遭遇部分编码制式的视频无法播放的情况。


## 联系我们
我们每个版本都会经过专业测试团队的测试验证，基础功能的可用性以及稳定性不成问题，但如果您在对接过程中遇到什么技术问题，欢迎 [联系我们](https://cloud.tencent.com/document/product/454/7998)。
