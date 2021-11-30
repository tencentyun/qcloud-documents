[](id:que1)

### 短视频 UGSV 支持的系统版本？
- **iOS**：手机8.0以上系统，Xcode 9 或更高版本，OS X 10.10或更高版本。
- **Android**：手机4.0.3（API 15）及以上系统，注意只有（Android 4.3）API 18 以上的系统才能开启硬件编码。

[](id:que2)
### 短视频 UGSV 是否支持 X86？
- **iOS**：支持。      
- **Android**：不支持。

[](id:que3)
### 短视频 UGSV 录制是否支持防抖？
不支持。

[](id:que5)

### 接入短视频 UGSV 是否需要视听证?
不需要。

[](id:que6)

### Demo 和小视频里面的 BGM 客户是否可以使用？
不可以，Demo 和小视频里面的 BGM 仅用于功能展示用，如果您用于商业 App，会存在法律风险。

[](id:que7)
### 视频录制和编辑是否支持转 GIF？
不支持，您可以根据我们 SDK 接口（TXVideoEditer > TXVideoInfoReader > getSampleImages）获取视频采样图列表，然后自行生成 GIF。

[](id:que8)
### 短视频 UGSV 是否支持拍照功能？
支持，您可以在录制 API 里面调用拍照接口拍照（TXUGCRecord > snapshot）。

[](id:que9)
### 腾讯云视立方生成的视频是否可以直接上传到非腾讯云平台（例如微信公众号）？
腾讯云视立方生成的视频可以上传到腾讯云的点播服务器，Demo 里面也有对应的源码参考，如果您要上传到其他平台，请自行查看其他平台的上传要求。

[](id:que10)

### 短视频 UGSV 是否支持小程序？
不支持。

[](id:que11)
### 短视频 UGSV 是否支持大眼瘦脸？
暂不支持。

[](id:que12)
### 短视频 UGSV 怎么获取视频信息（如宽高之类的）？
TXVideoEditer > TXVideoInfoReader > getVideoInfo。

[](id:que13)
### 视频编辑是否支持在视频任意位置插入图片？
不支持。

[](id:que14)
### 短视频 UGSV 解压的密钥是什么？
精简版和基础版 SDK 是没有解压密钥的。 

[](id:que15)

### Demo 体验只有基础美颜功能吗？

体验 Demo 中仅支持基础美颜功能，若您需体验大眼等其他特效需要额外购买。

[](id:que16)
### 腾讯云视立方对播放人数有限制吗？

不限制播放人数。

[](id:que17)
### 短视频 UGSV 是否接入使用第三方美颜？

短视频 SDK 不支持接入第三方美颜。

[](id:que18)
### 短视频 UGSV 是否支持背景音乐功能？

支持，可选择自带声音文件或用户手机本地的 MP3 作为背景音，同时支持背景音乐的裁剪和设置音量大小。

[](id:que19)
### 为什么设置背景音乐无效？

- 精简版不支持设置背景音乐文件功能，建议查看当前集成版本。
- 若您当前 SDK 是以精简版为基础进行升级，请检查当前 SDK 包是否还是精简版。
- 请检查当前 License 是与精简版 License 包名相同。若相同，请 [提工单](https://console.cloud.tencent.com/workorder/category) 联系人员进行处理。

[](id:que20)
### 使用视频编辑功能插入音乐，可以使用什么来源的音乐？

短视频这边的音乐是需要您在代码中进行添加的，目前这边没有提供的音乐库供您使用，您可自行选择音乐路径。更多详情，请参见 [添加背景音乐](https://cloud.tencent.com/document/product/1449/57036)。

[](id:que21)
### 短视频 UGSV 是否可以在精简版的基础上试用拍照功能？

支持在腾讯云视立方短视频UGC版本功能内集成使用的拍照组件，可以集成在短视频 SDK 内使用。

[](id:que22)
### 短视频 UGSV 是否支持自定义动态贴纸？怎么实现？

支持，通过 SDK 源代码使用，详情请参见 [贴纸和字幕(iOS)](https://cloud.tencent.com/document/product/1449/57052)。

[](id:que23)

### 短视频 UGSV 是否支持滤镜？

短视频 UGSV 支持滤镜特效和视频剪辑功能，详情请参见 [类抖音特效](https://cloud.tencent.com/document/product/1449/57050)、[SDK 集成(XCode)](https://cloud.tencent.com/document/product/584/11638#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E4.BD.BF.E7.94.A8-ugckit)。

[](id:que24)
### 短视频 UGSV 的剪辑功能，能否在微信小程序使用 ？

不支持在微信小程序中集成使用。

[](id:que25)
### 短视频 UGSV 是否支持背景墙？

暂不支持。

[](id:que26)

### 是否支持使用体验 Demo 集成高级美颜功能？

Demo 仅供体验，若需在此基础上集成高级美颜功能，需先开通此功能。

[](id:que27)

### 短视频 UGSV 是否支持 H5 接入？

不支持。

[](id:que28)

### 短视频 UGSV 是否支持 Flutter 版本集成？

不支持。

[](id:que29)
### 短视频 UGSV 有没有道具编辑器？

不支持。

[](id:que30)
### 短视频 UGSV 是单线程上传，还是多线程上传？

短视频 UGSV 支持**多线程上传**。

