**【版本说明】**
- 版本号：1.9.1.xxxx @ 2017-02-28
- iOS & Android：优化了摄像头直播中的美颜效果和清晰度体验，详情请关注 [iOS平台](https://www.qcloud.com/document/product/454/7879#step-4.3A-.E7.BE.8E.E9.A2.9C.E6.BB.A4.E9.95.9C) & [Android平台](https://www.qcloud.com/document/product/454/7885#step-4.3A-.E7.BE.8E.E9.A2.9C.E6.BB.A4.E9.95.9C)。
- iOS & Android：美颜增加了滤镜功能，多种主流滤镜效果供您的主播选择，详情请关注 [iOS平台](https://www.qcloud.com/document/product/454/7879#step-4.3A-.E7.BE.8E.E9.A2.9C.E6.BB.A4.E9.95.9C) & [Android平台](https://www.qcloud.com/document/product/454/7885#step-4.3A-.E7.BE.8E.E9.A2.9C.E6.BB.A4.E9.95.9C)。
- iOS & Android：增加了 setVideoQuality 接口，画质选择更简单更声音，，详情请关注 [iOS平台](https://www.qcloud.com/document/product/454/7879#step-9.3A-.E6.8E.A8.E8.8D.90.E7.9A.84.E6.B8.85.E6.99.B0.E5.BA.A6) & [Android平台](https://www.qcloud.com/document/product/454/7885#step-9.3A-.E6.8E.A8.E8.8D.90.E7.9A.84.E6.B8.85.E6.99.B0.E5.BA.A6)。
- iOS ：解决了某些客户反馈的iOS过曝问题，在人造光源比较强的场景下会有明显差异。
- iOS：进一步优化了耳返的延迟（[混响功能](https://www.qcloud.com/document/product/454/7879#step-13.3A-.E8.80.B3.E8.BF.94.26amp.3B.E6.B7.B7.E5.93.8D) 由于还有bug没有解决完，Delay一周Release）。
- 历史版本功能可参看 [变更历史](https://www.qcloud.com/document/product/454/7878)。

**【美颜优化】**
- **细节提升**：新版本美颜通过全新的区域识别和面部检测方案，将眼睛、眉毛、胡须、头发等细节的处理尽可能削减为零，以保证最大限度的接近真实情况。

- **前景侧重**：通过对编码方案进行优化，突出对前景人物的侧重，尽可能保留主播的细节，忽略其它非重要部分，在同样的码率下可以呈现更加清晰亮丽的人物细节。

- **算法优化**：通过对磨皮算法的优化，在真实度上提升的同时降低了GPU的负载，解决了之前把美颜效果调高后画面细节损失严重，“宛如油画”的效果不再出现，同时耗电和发热问题也有所改善。

- **曝光改善**：通过启用新的曝光方案，解决了iOS曝光过度的问题；同时针对 Android 各机型摄像头曝光敏感度不同的现状，提供了曝光设置功能，可以让主播在曝光不理想（低端机较常见）时手动修正曝光效果。

- **滤镜效果**：新版本美颜还增加了色彩滤镜效果，八种自带的滤镜给主播一些个性化的风格选择，滤镜的设计和调配均出自我们专业的视觉团队，无需担心版权问题，如下是滤镜效果的展示视频（左：主播端 右：观众端）
<video style="width:830px;height:470px;"src="http://1252463788.vod2.myqcloud.com/95576ef5vodtransgzp1252463788/46dfc3109031868222871736639/f0.f30.mp4" controls="controls">
抱歉，您的浏览器不支持在线播放MP4！
</video>

- **版本对比**：新旧版本美颜效果对比（左：1.9.0 vs 右：1.9.1 ）
<video style="width:830px;height:470px;"src="http://1252463788.vod2.myqcloud.com/95576ef5vodtransgzp1252463788/f2d370249031868222870425840/f0.f30.mp4" controls="controls">
抱歉，您的浏览器不支持在线播放MP4！
</video>

- **版本对比**：与知名直播APP美颜效果对比（左：1.9.1 vs 右：某椒iOS版 ）
<video style="width:830px;height:470px;"src="http://1252463788.vod2.myqcloud.com/95576ef5vodtransgzp1252463788/f2d3e27b9031868222870426200/f0.f30.mp4" controls="controls">
抱歉，您的浏览器不支持在线播放MP4！
</video>

**【版本预告】**
- 1.9.2 版本预计3月中发布beta版，3月底发布正式版
- 计划增加观众端视频片段的录制和分享功能
- 计划增加UGC小视频采集和发布功能
- 计划增加声音混响功能

**【文档索引】**
<table class="t">
<tbody><tr>
<th style="text-align: center; width: 150px;"> 文档标题
</th><th style="text-align: center; width: 500px;"> 内容介绍
</th><th style="text-align: center; width: 85px;"> 参考文档
</th></tr>
<tr>
<td style="text-align: center;"> iOS 推流
</td><td> 介绍如何推流？如何美颜？如何打水印？如何横屏直播？如何做音乐混音？以及 APP 退后台或网络不佳等情况的应对方案。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7879">DOC</a>
</td></tr>
<tr>
<td style="text-align: center;"> iOS 播放
</td><td> 介绍直播播放和点播播放的使用方法，同时对卡顿优化、界面处理、事件监听等问题进行了详细说明。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7880">DOC</a>
</td></tr>
<td style="text-align: center;"> iOS 连麦
</td><td> 介绍连麦功能的使用方法，如您对原理有疑问可以阅读 <a href="https://www.qcloud.com/document/product/454/8092">连麦原理</a> 了解详情。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/8090">DOC</a>
</td></tr>
<td style="text-align: center;"> iOS 进阶
</td><td> 介绍 RTMP SDK 的内部原理、质量监控手段、参数校调方法（FPS、GOP、分辨率、码率 ...） 以及智能控速等功能。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7884">DOC</a>
</td></tr>
<td style="text-align: center;">  Replaykit 录屏
</td><td> 介绍如何基于 Replaykit 技术 + RTMP SDK 实现用于游戏直播场景的手机录屏功能。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7883">DOC</a>
</td></tr>
<td style="text-align: center;">  Airplay 录屏
</td><td> 介绍如何基于 Airplay 技术 + RTMP SDK 实现用于游戏直播场景的手机录屏功能。
</td><td style="text-align: center;"> <a href="https://www.qcloud.com/document/product/454/7956">DOC</a>
</td></tr>
<td style="text-align: center;"> Android 推流
</td><td>  介绍如何推流？如何美颜？如何打水印？如何横屏直播？如何做音乐混音？以及 APP 退后台或网络不佳等情况的应对方案。
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


**【测试情况】**
- 核心测试用例： 总用例数 - 43， 通过用例数 - 43， 不通过用例数 - 0
- 系统测试用例： 总用例数 - 255，通过用例数 - 255，不通过用例数 - 0
- 全量测试用例： 总用例数 - 635，通过用例数 - 621，不通过用例数 - 14

**【下载地址】**

| 操作系统 | 版本号 | 版本说明|下载链接 |
| ---- | ----------- | ---- | ---- | 
| IOS完整版  | 1.9.0.1948  | 包含推流、直播、点播、连麦、录屏 等全部特性。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKIOS1.9.0.1948.zip)  |
| IOSRename版  | 1.9.0.1948  | 在完整版的基础上，对 ffmpeg 等开源组件进行了符号重命名。<br>如果您原项目中有打包 ffmpeg 导致符号冲突或者运行时莫名其妙的崩溃，推荐使用此版本。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKIOSRename1.9.0.1948.zip)  |
| IOS精简版  | 1.9.0.1948  | 在完整版的基础上裁剪掉了非核心功能，双架构代码体积增量 800k。<br> 精简版点播功能的兼容性不及完整版；不支持iOS 7.0；iOS 10 以下系统不支持后台推流。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKIOSSimple1.9.0.1948.zip)  |
| Android完整版  | 1.9.0.1948 | 包含推流、直播、点播、连麦、录屏 等全部特性。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroid1.9.0.1948.zip)  |
| Android精简版  | 1.9.0.1948 | 在完整版的基础上裁剪掉了连麦功能。 <br> 如果您的项目中已打包互动直播SDK，推荐使用次版本。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroidSimple1.9.0.1948.zip)  |

**【联系我们】**
我们每个版本都会经过专业测试团队的测试验证，基础功能的可用性以及稳定性不成问题，但如果您在对接过程中遇到什么技术问题，欢迎 [联系我们](https://www.qcloud.com/document/product/454/7998)。

