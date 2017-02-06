**【版本说明】**
- 版本号：1.9.0.1948 @ 2017-01-20
- iOS ：支持开启Bitcode，用于减少AppStore的安装包体积；
- iOS ：软硬编美颜统一，统一使用GPU加速方案；
- iOS + Android：音频模块优化，连麦支持背景音播放；
- iOS + Android：点播多线程优化（直播在上个版本已支持多实例）
- iOS + Android：解决网络卡顿时，播放停止（stopPlay）阻塞UI线程时间较长的问题；
- iOS ： 新增耳返功能，即主播在插上耳机唱歌时，可以实时听到自己发音的效果；
- Android：由于系统API的延迟问题，暂时尚未支持，我们会继续努力。
- 历史版本功能可参看 [变更历史](https://www.qcloud.com/document/product/454/7878)。

**【版本预告】**
- 1.9.1 版本预计2月底发布
- 计划优化iOS和Android平台的美艳效果和部分机型的清晰度问题
- 计划优化音频JitterBuffer，旨在优化连麦时的声音流畅度
- 计划增加耳返时的声音混响音效

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
- 核心用例测试： 总用例数 - 43， 通过用例数 - 43，不通过用例数 - 0
- 系统用例测试： 总用例数 - 87， 通过用例数 - 87，不通过用例数 - 0
- 全部用例测试： 总用例数 - 356，通过用例数 - 332，不通过用例数 - 24

**【下载地址】**

| 操作系统 | 版本号 | 版本说明|下载链接 |
| ---- | ----------- | ---- | ---- | 
| IOS完整版  | 1.9.0.1948  | 包含推流、直播、点播、连麦、录屏 等全部特性。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKIOS1.9.0.1948.zip)  |
| IOSRename版  | 1.9.0.1948  | 在完整版的基础上，对 ffmpeg 等开源组件进行了符号重命名。<br>如果您原项目中有打包 ffmpeg 导致符号冲突或者运行时莫名其妙的崩溃，推荐使用此版本。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKIOSRename1.9.0.1948.zip)  |
| IOS精简版  | 1.9.0.1948  | 在完整版的基础上裁剪掉了非核心功能，双架构代码体积增量 800k。<br> 精简版点播功能的兼容性不及完整版；不支持iOS 7.0；iOS 10 以下系统不支持后台推流。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKIOSSimple1.9.0.1948.zip)  |
| Android完整版  | 1.9.0.1948 | 包含推流、直播、点播、连麦、录屏 等全部特性。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroid1.9.0.1948.zip)  |
| Android精简版  | 1.9.0.1948 | 在完整版的基础上裁剪掉了连麦功能。 <br> 如果您的项目中已打包互动直播SDK，推荐使用次版本。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroidSimple1.9.0.1948.zip)  |

**【联系我们】**
我们每个版本都会经过专业测试团队的测试验证，基础功能的可用性以及稳定性不成问题，但如果您在对接过程中遇到什么技术问题，欢迎[联系我们](https://www.qcloud.com/document/product/454/7998)。

