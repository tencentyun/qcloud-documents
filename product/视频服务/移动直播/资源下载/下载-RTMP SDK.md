**【版本说明】**
- 版本号：1.9.2.2231 @ 2017-03-18
- iOS & Android：优化了摄像头直播中的美颜效果，并增加了对滤镜的支持 ，详情请关注 [如何实现更好的画质](https://www.qcloud.com/document/product/454/7955)。
- iOS & Android：增加了对本地文件播放的支持。（startPlay 中设置 PLAY_TYPE_LOCAL_VIDEO）
- iOS & Android：重新设计了播放器中缓冲区的方案，对于低延迟链路的声音流畅性有优化。
- iOS：增加了 setReverbType 接口，可设置多种声音混响效果，详情参考 [耳返&混响](https://www.qcloud.com/document/product/454/7879#step-13.3A-.E8.80.B3.E8.BF.94.26amp.3B.E6.B7.B7.E5.93.8D)。
- iOS：优化了直播过程中添加水印的性能。
- 历史版本功能可参看 [变更历史](https://www.qcloud.com/document/product/454/7878)。

**【美颜优化】**
- **细节提升**：新版本美颜通过全新的区域识别和面部检测方案，将眼睛、眉毛、胡须、头发等细节的处理尽可能削减为零，以保证最大限度的接近真实情况。
<video style="width:830px;height:470px;"src="http://1252463788.vod2.myqcloud.com/95576ef5vodtransgzp1252463788/f2d370249031868222870425840/f0.f30.mp4" controls="controls">
抱歉，您的浏览器不支持在线播放MP4！
</video>

- **前景侧重**：通过对编码方案进行优化，突出对前景人物的侧重，尽可能保留主播的细节，忽略其它非重要部分，在同样的码率下可以呈现更加清晰亮丽的人物细节。

- **算法优化**：通过对磨皮算法的优化，在真实度上提升的同时降低了GPU的负载，解决了之前把美颜效果调高后画面细节损失严重，“宛如油画”的效果不再出现，同时耗电和发热问题也有所改善。

- **曝光改善**：通过启用新的曝光方案，解决了iOS曝光过度的问题；同时针对 Android 各机型摄像头曝光敏感度不同的现状，提供了曝光设置功能，可以让主播在曝光不理想（低端机较常见）时手动修正曝光效果。

**【版本预告】**
- 2.0.0 版本预计3月31日发布，RTMP SDK将增加小视频采集和发布功能。

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
- 核心测试用例： 总用例数 - 43， 通过用例数  - 43， 不通过用例数 - 0
- 系统测试用例： 总用例数 - 261，通过用例数 - 261，不通过用例数 - 0
- 全量测试用例： 总用例数 - 646，通过用例数 - 635，不通过用例数 - 11

**【下载地址】**

| 操作系统 | 版本号 | 版本说明|下载链接 |
| ---- | ----------- | ---- | ---- | 
| IOS完整版  | 1.9.1.2088  | 包含推流、直播、点播、连麦、录屏 等全部特性。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOS1.9.2.2231.zip)  |
| IOSRename版  | 1.9.1.2088  | 在完整版的基础上，对 ffmpeg 等开源组件进行了符号重命名。<br>如果您原项目中有打包 ffmpeg 导致符号冲突或者运行时莫名其妙的崩溃，推荐使用此版本。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOSRename1.9.2.2231.zip) |
| IOS精简版  | 1.9.1.2088  | 在完整版的基础上裁剪掉了非核心功能，双架构代码体积增量 <font color='red'>800K</font> 。<br> 精简版点播功能的兼容性不及完整版；不支持iOS 7.0；iOS 10 以下系统不支持后台推流。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKiOSSimple1.9.2.2231.zip)  |
| Android完整版  | 1.9.1.2088 | 包含推流、直播、点播、连麦、录屏 等全部特性。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroid1.9.2.2231.zip)  |
| Android精简版  | 1.9.1.2088 | 在完整版的基础上裁剪掉了连麦功能。 <br> 如果您的项目中已打包互动直播SDK，推荐使用次版本。 | [点击下载](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroidSimple1.9.2.2231.zip)  |

**【联系我们】**
我们每个版本都会经过专业测试团队的测试验证，基础功能的可用性以及稳定性不成问题，但如果您在对接过程中遇到什么技术问题，欢迎 [联系我们](https://www.qcloud.com/document/product/454/7998)。

