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
- 预计增加Android端小视频编辑功能
- 预计优化Demo及小直播代码结构，降低对接成本

## 文档索引
<table class="t">
<tbody><tr>
<th style="text-align: center; width: 100px;"> 文档标题
</th><th style="text-align: center; width: 550px;"> 内容介绍
</th><th style="text-align: center; width: 85px;"> 参考文档
</th></tr>
<tr>
<td style="text-align: center;"> iOS - 推流
</td><td> 介绍推流、美颜、滤镜、水印、横屏直播、混音混响、硬件加速、后台垫片等功能，以及网络波动等情况下的应对方案。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7879">DOC</a>
</td></tr>
<tr>
<td style="text-align: center;"> iOS - 播放
</td><td> 介绍直播播放和点播播放的使用方法，同时对卡顿优化、界面处理、事件监听等问题进行了详细说明。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7880">DOC</a>
</td></tr>
<td style="text-align: center;"> iOS - 连麦
</td><td> 介绍连麦功能的使用方法，如您对原理有疑问可以阅读 <a href="https://www.qcloud.com/document/product/454/8092">连麦原理</a> 了解详情。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/8090">DOC</a>
</td></tr>
<td style="text-align: center;"> iOS - 进阶
</td><td> 介绍 RTMP SDK 的内部原理、质量监控手段、参数校调方法（FPS、GOP、分辨率、码率 ...） 以及智能控速等功能。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7884">DOC</a>
</td></tr>
<td style="text-align: center;">  iOS ReplayKit 
</td><td> 介绍如何基于 Replaykit 技术 + RTMP SDK 实现用于游戏直播场景的手机录屏功能。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7883">DOC</a>
</td></tr>
<td style="text-align: center;">   iOS AirPlay
</td><td> 介绍如何基于 AirPlay 技术 + RTMP SDK 实现用于游戏直播场景的手机录屏功能。
</td><td style="text-align: center;"> 暂不对外
</td></tr>
<td style="text-align: center;"> Android 推流
</td><td>  介绍推流、美颜、滤镜、水印、横屏直播、混音混响、硬件加速、后台垫片等功能，以及网络波动等情况下的应对方案。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7885">DOC</a>
</td></tr>
<td style="text-align: center;"> Android 播放
</td><td> 介绍直播播放和点播播放的使用方法，同时对卡顿优化、界面处理、事件监听等问题进行了详细说明。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7886">DOC</a>
</td></tr>
<td style="text-align: center;"> Android 连麦
</td><td> 介绍连麦功能的使用方法，如您对原理有疑问可以阅读 <a href="https://www.qcloud.com/document/product/454/8092">连麦原理</a> 了解详情。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/8091">DOC</a>
</td></tr>
<td style="text-align: center;">  Android 进阶
</td><td> 介绍 RTMP SDK 的内部原理、质量监控手段、参数校调方法（FPS、GOP、分辨率、码率 ...） 以及智能控速等功能。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7890">DOC</a>
</td></tr>
<td style="text-align: center;"> Android 录屏
</td><td> 介绍如何基于 RTMP SDK 实现用于游戏直播场景的手机录屏功能。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7889">DOC</a>
</td></tr>
</tbody></table>


## 测试情况
- 核心测试用例： 总用例数 - 56， 通过用例数  - 56， 不通过用例数  - 0
- 系统测试用例： 总用例数 - 307，通过用例数 - 307，不通过用例数 - 0
- 全量测试用例： 总用例数 - 718，通过用例数 - 697，不通过用例数 - 21 

## 下载地址

| 操作系统 | 版本号 | 版本说明|下载链接 |
| ---- | ----------- | ---- | ---- | 
| IOS完整版  | 2.0.2.2801  | 包含推流、直播、点播、连麦、录屏 等全部特性。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOS2.0.2.2801.zip)  |
| IOS精简版  | 2.0.2.2801   | 裁剪掉了非核心功能，代码体积增量 <font color='red'>800K</font> 。播放器的兼容性不及完整版；不支持iOS 7.0；iOS 10 以下系统不支持后台垫片推流。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOSSimple2.0.2.2801.zip)  |
| IOSRename版  | 2.0.2.2801  | 在完整版的基础上对 ffmpeg 等开源组件进行了符号重命名。如您的项目原来就包含有 ffmpeg 导致符号冲突，或崩溃在 ffmpeg 的内部函数里，可以使用此版本。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOSRename2.0.2.2801.zip) |
| Android完整版  | 2.0.2.2801 | 包含推流、直播、点播、连麦、录屏 等全部特性。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroid2.0.2.2801.zip)  |
| Android精简版  | 2.0.2.2801 | 在完整版的基础上裁剪掉了连麦功能。如果您的项目中已打包互动直播SDK，推荐使用次版本。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroidSimple2.0.2.2801.zip)  |
| 双平台特权版  | 2.0.2.2801  | 在完整版的基础上，结合天天P图的美妆 SDK 实现了大眼、瘦脸、动效贴纸、绿幕特效等功能，使用请联系商务。 | [点击下载](http://downloadfix-1252463788.cosgz.myqcloud.com/RTMPIOS%26AndroidSDKPitu.zip) |

## 联系我们
我们每个版本都会经过专业测试团队的测试验证，基础功能的可用性以及稳定性不成问题，但如果您在对接过程中遇到什么技术问题，欢迎 [联系我们](https://www.qcloud.com/document/product/454/7998)。

