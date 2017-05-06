## 版本说明
- 版本号：2.0.2.2801 @ 2017-05-02
- iOS：新增UGC裁剪与拼接功能。
- iOS：精简版支持Bitcode。
- Android：特权版新增大眼瘦脸功能。
- Android：优化硬编效果，提升编码质量。
- Android：开发播放端数据接口，硬解数据以Surface形式提供，软解数据以buffer形式提供。
- iOS & Android：优化前置摄像头在开启P图、绿幕后的镜像表现。
- iOS & Android：优化UGC上传协议。
- 历史版本功能可参看 [变更历史](https://www.qcloud.com/document/product/454/7878)。


## 版本预告
- 2.0.3 版本预计五月中旬发布
- 预计增加 Android 端小视频编辑功能
- 预计优化 Demo 及小直播代码结构，降低对接成本
- 增加新的 setVideoQuality 类型，适用海外直播场景
- 增加新的硬件加速设置选项

## 文档索引

| 手机平台 | 文档索引 |
|:-------:|---------|
| iOS 平台 | [推流功能](https://www.qcloud.com/document/product/454/7879) &nbsp; [播放功能](https://www.qcloud.com/document/product/454/7880) &nbsp; [主播连麦](https://www.qcloud.com/document/product/454/8090) &nbsp; [进阶使用](https://www.qcloud.com/document/product/454/7884) &nbsp; [进阶使用](https://www.qcloud.com/document/product/454/7883) &nbsp; [ReplayKit](https://www.qcloud.com/document/product/454/7884)  | 
| Android 平台 | [推流功能](https://www.qcloud.com/document/product/454/7885) &nbsp; [播放功能](https://www.qcloud.com/document/product/454/7886) &nbsp; [主播连麦](https://www.qcloud.com/document/product/454/8091) &nbsp; [进阶使用](https://www.qcloud.com/document/product/454/7890) &nbsp; [手机录屏](https://www.qcloud.com/document/product/454/7889) | 

## 测试情况
- 核心测试用例： 总用例数 - 56， 通过用例数  - 56， 不通过用例数  - 0
- 系统测试用例： 总用例数 - 307，通过用例数 - 307，不通过用例数 - 0
- 全量测试用例： 总用例数 - 718，通过用例数 - 697，不通过用例数 - 21 

## 下载地址
<style>
table th:nth-of-type(1) {  width: 150px; }
table th:nth-of-type(2) {  width: 550px; }
table th:nth-of-type(3) {  width: 100px; }
</style>

- **iOS 平台（2.0.2.2801）**

| 版本类型 | 版本说明|下载链接 |
| :---------: |  ---- | :----: | 
| 完整版  |  包含推流、直播、点播、连麦、录屏 等全部特性。 | [ZIP](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOS2.0.2.2801.zip)  |
| 精简版  |  在完整版的基础上裁剪掉了非核心功能，代码体积增量 <font color='red'>900KB</font> 。播放器的兼容性逊于完整版；不支持iOS 7.0；iOS 10 以下系统不支持后台垫片推流。 | [ZIP](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOSSimple2.0.2.2801.zip)  |
| rename版  |  在完整版的基础上对 ffmpeg 等开源组件进行了符号重命名。如您的项目原来就包含有 ffmpeg 导致符号冲突，或崩溃在 ffmpeg 的内部函数里，可以使用此版本。 | [ZIP](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOSRename2.0.2.2801.zip) |

- **Android 平台 （2.0.2.2801）**

| 版本类型 | 版本说明|下载链接 |
| :---------: |  ---- | :----: | 
| 完整版  | 包含推流、直播、点播、连麦、录屏 等全部特性。 | [ZIP](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroid2.0.2.2801.zip)  |
| 精简版  | 在完整版的基础上裁剪掉了连麦功能，适合跟互动直播 iLiveSDK 一起使用。 | [ZIP](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroidSimple2.0.2.2801.zip)  |

- **商用付费版 （2.0.2.2801）**

| 操作系统 | 版本说明|下载链接 |
| :---------: |  ---- | :----: | 
| iOS平台  | 基于优图实验室的 AI 专利技术，实现了大眼、瘦脸、动效贴纸、绿幕等特效功能，使用方法见 [特效](https://www.qcloud.com/document/product/454/9018)。 | [ZIP](http://downloadfix-1252463788.cosgz.myqcloud.com/RTMPIOS%26AndroidSDKPitu.zip) |
| Android平台  | 基于优图实验室的 AI 专利技术，实现了大眼、瘦脸、动效贴纸、绿幕等特效功能，使用方法见 [特效](https://www.qcloud.com/document/product/454/9018)。 | [ZIP](http://downloadfix-1252463788.cosgz.myqcloud.com/RTMPIOS%26AndroidSDKPitu.zip) |

## 联系我们
我们每个版本都会经过专业测试团队的测试验证，基础功能的可用性以及稳定性不成问题，但如果您在对接过程中遇到什么技术问题，欢迎 [联系我们](https://www.qcloud.com/document/product/454/7998)。

