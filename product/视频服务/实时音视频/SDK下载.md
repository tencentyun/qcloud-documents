
## SDK下载

TRTC SDK 以及附带的 Demo 源代码已经都托管到了 [Github](https://github.com/tencentyun/TRTCSDK) 上，您可以直接通过 Clone 获取之。

| 所属平台 | Github 地址 | Demo运行说明 | SDK集成指引 
|:---------:| :--------:| :--------:| :--------:|
| iOS | [GitHub](https://github.com/tencentyun/TRTCSDK/tree/master/iOS)| [DOC](https://cloud.tencent.com/document/product/647/32396)| [DOC](https://cloud.tencent.com/document/product/647/32173) |
| Android | [GitHub](https://github.com/tencentyun/TRTCSDK/tree/master/Android)| [DOC](https://cloud.tencent.com/document/product/647/32166)| [DOC](https://cloud.tencent.com/document/product/647/32175) |
| Windows| [GitHub](https://github.com/tencentyun/TRTCSDK/tree/master/Windows)| [DOC](https://cloud.tencent.com/document/product/647/32397)| [DOC](https://cloud.tencent.com/document/product/647/32178) |
| Mac| [GitHub](https://github.com/tencentyun/TRTCSDK/tree/master/Mac)| [DOC](https://cloud.tencent.com/document/product/647/32396)| [DOC](https://cloud.tencent.com/document/product/647/32176) |
| Web | [GitHub](https://github.com/tencentyun/TRTCSDK/tree/master/H5)| [DOC](https://cloud.tencent.com/document/product/647/32398)| [DOC](https://cloud.tencent.com/document/product/647/16863) |
| 微信小程序| [GitHub](https://github.com/tencentyun/TRTCSDK/tree/master/WXMini)| [DOC](https://cloud.tencent.com/document/product/647/32399)| [DOC](https://cloud.tencent.com/document/product/647/32183) |

## LiteAVSDK

![](https://main.qcloudimg.com/raw/9bcce79e250441f9aeb93756196e1a2e.png)

TRTC SDK 隶属于腾讯视频云 LiteAV 体系，LiteAV_TRTC 擅长于低延时视频通话解决方案，与此同时，LiteAV 体系还提供了其它应用场景的解决方案：

| SDK压缩包名称 | 主要用途 | 包含功能 |
|:-------:|:-------:|:-------:|
| LiteAV_TRTC | [实时音视频](https://cloud.tencent.com/product/trtc) | 视频通话 |
| LiteAV_Smart | [移动直播](https://cloud.tencent.com/product/mlvb) | 直播推流和直播播放 |
| LiteAV_Player | [超级播放器](https://cloud.tencent.com/product/player) | 直播播放器和点播播放器 |
| LiteAV_UGC | [短视频](https://cloud.tencent.com/product/ugsv) | 视频录制、视频特效、视频上传等 |

## SDK符号冲突

如果您的项目中已经使用过腾讯视频云 LiteAV 体系的相关产品，可能会出现符号冲突的问题（symbol duplicate）的问题，这是由于它们共同复用了相同的采集模块、编解码器、降噪模块、前处理等底层基础模块，所以才会出现符号重复。

您可以下载腾讯视频 LiteAV_Professional 版本，该版本集成了以上 SDK 的全部功能，而且由于 60% 以上的底层模块是复用的，所以产生的安装包体积增量远远小于集成两个独立的 SDK（音视频 SDK 中的主要体积增量源于编解码等各种基础模块）。

- [**专业版下载地址**](https://github.com/tencentyun/TRTCSDK/blob/master/SDK%E4%B8%93%E4%B8%9A%E7%89%88.md#%E4%B8%93%E4%B8%9A%E7%89%88%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80)