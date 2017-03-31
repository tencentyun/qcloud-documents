## 版本说明
- 版本号：2.0.0.2243 @ 2017-03-31
- iOS & Android：增加 UGC 小视频的采集和发布功能，使用方法见 [iOS](https://www.qcloud.com/document/product/454/8838) & [Android](https://www.qcloud.com/document/product/454/8843)。
- iOS & Android：增加截流录制功能，观众可以在观看直播时截取一段形成 UGC 小视频，然后分享出来。
- iOS：增加了新的“美白”滤镜，适合较为偏爱映客美颜效果的客户，[setFilter](https://www.qcloud.com/document/product/454/7885#step-4.3A-.E7.BE.8E.E9.A2.9C.E6.BB.A4.E9.95.9C) 可以设置滤镜效果。
- 历史版本功能可参看 [变更历史](https://www.qcloud.com/document/product/454/7878)。


## 版本预告
- 2.0.1 版本预计4月14日发布
- 预计增加 UGC 小视频录制时的背景音功能
- 预计增加 UGC 小视频编辑器功能（由于工作量比较大，如果没有意外，该功能会完美地跳票到 4 月底）
- 预计提升 Android 硬件编码效果，减少硬件编码模式下的运动画面马赛克问题（软编码无此问题）
- 预计增加 Player 视频数据回调接口，方便 VR 等直播场景的定制

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
| IOS完整版  | 2.0.0.2243  | 包含推流、直播、点播、连麦、录屏 等全部特性。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOS1.9.2.2243.zip)  |
| IOS精简版  | 2.0.0.2243  | 裁剪掉了非核心功能，代码体积增量 <font color='red'>800K</font> 。播放器的兼容性不及完整版；不支持iOS 7.0；iOS 10 以下系统不支持后台垫片推流。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOSSimple1.9.2.2243.zip)  |
| IOSRename版  | 2.0.0.2243  | 在完整版的基础上对 ffmpeg 等开源组件进行了符号重命名。如您的项目原来就包含有 ffmpeg 导致符号冲突，或崩溃在 ffmpeg 的内部函数里，可以使用此版本。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOSRename1.9.2.2243.zip) |
| Android完整版  | 2.0.0.2243 | 包含推流、直播、点播、连麦、录屏 等全部特性。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroid1.9.2.2243.zip)  |
| Android精简版  | 2.0.0.2243 | 在完整版的基础上裁剪掉了连麦功能。如果您的项目中已打包互动直播SDK，推荐使用次版本。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroidSimple1.9.2.2243.zip)  |
| 双平台特权版  | 2.0.0.2243  | 在完整版的基础上，结合天天P图的美妆 SDK 实现了大眼、瘦脸、动效贴纸、绿幕特效等功能。 | 联系商务 |

## 联系我们
我们每个版本都会经过专业测试团队的测试验证，基础功能的可用性以及稳定性不成问题，但如果您在对接过程中遇到什么技术问题，欢迎 [联系我们](https://www.qcloud.com/document/product/454/7998)。

