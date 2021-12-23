### Version 9.4 @ 2021.12.09
- iOS：修复短视频录制，开启美颜动效，录制出来的视频没有动效声音的问题。
- Android：修复短视频编辑不支持生成 1080P 视频的问题。
- Android&iOS：短视频上传更新 HTTPDNS 请求地址。

### Version 9.3 @ 2021.11.04
- iOS：修复视频录制完成后，在特效编辑场景下播放预览出现变速的问题。
- iOS：修复 TXCRenderView 的崩溃问题。
- Android：修复小米9三屏合唱视频合成卡顿崩溃的问题。

### Version 9.2 @ 2021.09.26
- Android：修复获取的缩略图只有一半的问题。
- Android：修复 MTK 天玑1200 CPU 合成视频卡住的问题。
- Android：优化视频录制 9:16 适配的问题。
- iOS：修复选择48000单声道的视频进行拼接声音异常的问题。

### Version 9.1 @ 2021.09.02
- Android：优化短视频若干稳定性问题。
- Android：优化 UGC 相关功能生成视频的清晰度问题。
- Android：修复 Android5.x 特定设备出现播放崩溃的问题。
- iOS：修复 iPhone 12 以上机型导出视频颜色饱和度失真。

### Version 9.0 @ 2021.08.06
- Android：优化短视频合唱加载耗时问题。
- Android：优化短视频 SDK 的性能问题。
- Android：优化短视频的稳定性问题。
- Andriod：修复在视频裁剪过程中偶现的裁剪不准确问题。
- iOS：修复短视频上传压缩过程中切换后来出现的压缩异常问题。

### Version 8.9 @ 2021.07.15
- iOS：修复短视频新增贴纸时，切换到静态贴纸后，返回再进入，静态贴纸显示动态贴纸的内容的问题。
- iOS：修复短视频移动位置后，再次单击已选择视频或图片会取消原位置上的文件的问题。
- Android：修复短视频在小米机型上使用图片转场功能出现图片被旋转现象的问题。

### Version 8.8 @ 2021.06.18
- iOS：修复点播播放器启停多次触发的内存泄漏问题。
- iOS&Android：修复点播暂停播放后设置进度，画面显示慢的问题。

### Version 8.7 @ 2021.05.24
iOS：修复 iOS 14.5 短视频录制模块出现电流杂音问题。

### Version 8.6 @ 2021.05.06
- iOS：修复点播播放器偶现内存异常上涨问题。
- iOS：优化 Swift 编译警告问题。
- iOS&Android：修复 UGC SDK 若干稳定性问题。
- iOS&Android：修复 UGC SDK 上传竞速导致上传失败的问题。

### Version 8.5 @ 2021.03.18
- iOS & Android：高级美颜效果优化，优化瘦脸、大眼、V脸等相关效果。
- iOS & Android：高级美颜新增窄脸接口。
- iOS & Android：高级美颜人脸特征提取优化。
- iOS & Android：高级美颜新增窄脸接口。
- iOS & Android：优化超级播放器播放部分网络串流 seek 慢的问题。
- Android: 修复超级播放器通过 fileid 方式播放出现报错问题。

### Version 8.4 @ 2021.02.07
- iOS&Android：短视频校验安全性问题 fix。
- Android：短视频支持多音轨视频预览。
- iOS：优化预处理性能，提高稳定性。
- iOS：美颜回调脸部坐标问题 fix。

### Version 8.3 @ 2021.01.15
- Android：修复片段录制时，回删片段可能导致的合成失败问题。
- Android：修复短视频多例崩溃问题。
- iOS：修复点播时减速崩溃的问题。
- iOS：修复图片转场时特定步骤下显示黑屏的问题。
- iOS：修复部分兼容性问题导致崩溃问题。

### Version 8.2 @ 2020.12.24
- Android：修复切换摄像头绿幕失效的问题。
- Android：修复短视频偶现的稳定性问题。
- iOS：修复播放器倒置旋转，偶现播放画面比例异常的问题。
- iOS：修复短视频录制设置为横屏时，继续录制的合成失败问题。
- iOS：修复超级播放器偶现的稳定性问题。

### Version 8.1 @ 2020.12.03
- Android：改善短视频的画质和清晰度。
- Android：修改美颜相关接口的参数类型从 int 到 float。
- Android：修复短视频暂停录制后返回值异常的问题。
- Android：修复部分 Crash 问题及兼容性问题。

### Version 8.0 @ 2020.11.16
- iOS：修复添加多个贴纸后偶现应用卡死的问题。
- iOS：修复气泡字幕编辑偶现闪退的问题。
- Android：上传封面兼容 9.0 以上机型。
- Android：修复三屏合拍切后台返回出现合拍视频不同步的问题。
- Android：UGCKit 修复视频压缩预览页面偶现黑屏的问题。
- Android：UGCKit 修复视频编辑音量设置不生效的问题。
- Android：UGCKit 修复动作界面撤销按钮偶现不显示的问题。

### Version 7.9 @ 2020.10.23
- iOS：修复短视频编辑尾部音频缺失的问题。
- iOS：解决短视频录制添加 BGM 重新录制 BGM 不重置的问题。
- Android：修复短视频 SDK 若干 Crash，增强稳定性。
- Android：修复 Android 5.0 以下版本使用拍摄功能崩溃的问题。
- iOS&Android：直播播放器优化延迟控制算法，避免频繁加减速。

### Version 7.8 @ 2020.09.27
- iOS：超级播放器修复 iOS 14 兼容性问题。
- Android：更新 UGCKit 中的 VideoUploadSDK。
- Android：修复高级美颜 Android 4.4 系统 Crash 的问题。
- Android：修复短视频 SDK 录制偶现音画不同步的问题。
- Android：修复短视频 SDK 反初始化打印错误日志的问题。
- Andorid：修复短视频 SDK 结束录制回调慢的问题。
- Android：修复短视频 SDK 近期反馈的多个崩溃问题。

### Version 7.7 @ 2020.09.08
- Android：P 图基础美颜优化，新增白皙和自然两种滤镜。
- iOS：短视频 iOS14 系统兼容性问题 fix。

### Version 7.6 @ 2020.08.24
- iOS&Android：AI 美颜优化，修复唇彩遮挡问题，提高识别精确度，优化侧脸妆容效果。
- iOS&Android：SDK 事件及错误回调信息国际化。
- Android：短视频自定义预处理回调提前到添加贴纸之前。
- Android：短视频修复 bitmap 被释放导致的偶现 Crash 问题。
- Android：短视频修复特定机型合唱持续 loading 的问题。

### Version 7.5 @ 2020.07.31
iOS：解决短视频尾部水印观看闪烁的问题。

### Version 7.4 @ 2020.07.03
- iOS&Android：修复无音轨视频合并失败的问题。
- Android：优化短视频编辑生成效果，解决部分机型画面清晰度不够的问题。

### Version 7.2 @ 2020.04.17
iOS&Android：优化滤镜、绿幕等视效接口，归并到 TXBeautyManager 类下，实现统一的调用方式。

### Version 7.1 @ 2020.03.30
- Andorid：短视频编辑新增 HE-AAC 音频格式支持，更好的兼容第三方视频编辑。
- Android：短视频 UGCKit 修复偶现裁剪页面显示异常、偶现录制报错等相关问题。 

### Version 7.0 @ 2020.03.09
- Android：解决人脸动效偶现 Crash 问题。
- Android：解决频繁切换摄像头同时停止录制引起的偶现 Crash 问题。
- iOS&Android：修复若干 bug。

### Version 6.9 @ 2020.01.15
- iOS&Android：UGC TUIKit 实现，UI 组件化，支持自定义主题，方便集成与修改。
- iOS&Android：UGC 支持三屏合拍及音量调节能力。
- Android：Android 10 兼容支持。
- Android：UGC 预处理采用硬遍，提高预处理速度。
- iOS：UGC 合唱模块优化，解决音画不同步等相关问题。

### Version 6.8 @ 2019.11.15
- iOS&Android：录制支持4：3分辨率。
- iOS&Android：企业版增加 P 图新功能，包括美肤、亮眼、白牙、祛皱、美妆、手势识别等新特性。
- Android：优化短视频生成速度，提高短视频编辑生成效率。
- Android：修复对焦右下边框比左上边框粗的问题。
- Android：企业版修复部分机型大眼、瘦脸、动效无效的问题。
- iOS：短视频预览解决偶现黑屏的问题。

### Version 6.7 @ 2019.09.29
- iOS&Android：录制增加16：9分辨率支持。
- iOS&Android：重点解决上报的偶现 CRASH 问题。
- Android：短视频合成偶现杂音问题 fix。
- iOS：解决阿拉伯文兼容性问题。
- iOS：解决编辑视频使用高质量保存偶现失败的问题。

### Version 6.6 Patch @ 2019.09.10
- iOS&Android：修复若干 bug。
- Android：企业版修复内存占用及库冲突问题。
- iOS：iOS13 兼容性支持。

### Version 6.6.7458 @ 2019-08-06
- Android：企业版新增64位支持，P 图库支持动态下载。
- Android：短视频修复编辑视频页 CRASH。
- iOS：修复 TXVideoEditer 按时间点获取缩略图偶现返回数据不正确问题。
- iOS：修复设置动效切后台后无效的问题。

### Version 6.5.7272 @ 2019-06-12
- iOS&Android：新增图片上传支持。
- Android：修复短视频生成偶现 opengl 异常等问题。
- Android：修复视频编辑时 pause 后旋转方向不会刷新的问题。

### Version 6.4.7328 @ 2019-05-15
修复近期反馈的 bug，进一步提升稳定性。  

### Version 5.4 @ 2019-01-04
- iOS&Android：优化了短视频上传的成功率。
- iOS：图片转场合成功能的一些 CRASH 问题。

### Version 5.3 @ 2018-10-25
- iOS&Android：编辑 BGM 支持淡入淡出。
- iOS&Android：支持 1080P 视频录制。
- iOS&Android：支持无音频视频拼接。
- Android：修复录制进度回调不及时问题。
- Android：解决部分视频缩略图方向不对问题。
- Android：解决预处理卡顿问题。
- iOS：录制 BGM 支持设置是否循环播放。
- iOS：短视频上传优化。
- iOS：Demo 增加生成原视频的 GIF 功能。

### Version 5.2 @ 2018-09-14
- iOS&Android：支持 4K 大视频编辑，缩略图提取支持指定分辨率。
- iOS&Android：新增草稿箱功能使用示例，具体请参见小视频 App。
- iOS&Android：编辑支持动态旋转画面角度。
- Android：视频编辑新增缩略图快速获取接口。
- Android：修复动态贴纸角度设置不生效问题。
- Android：解决多视频合成偶现音画不同步问题，提升视频合成画质。
- iOS：修复快速频繁切换 BGM 引起的线程安全问题。
- iOS：解决视频录制和预览 BGM 声音大小不一致的问题。
- iOS：修复视频编辑添加重复特效导致片尾水印 PTS 异常的问题。

### Version 5.1 @ 2018-08-18
- iOS&Android：短视频增加多个版本：精简版，基础版，企业版，企业版 Pro，以满足不同客户的需求，不同版本需申请对应的 License。
- iOS&Android：优化美颜滤镜，重新设计增加多种滤镜效果。
- iOS&Android：录制、编辑滤镜增加手势滑动切换效果。
- iOS&Android：优化双人合唱功能。
- iOS&Android：小视频 App 增加长按录制、单击录制、单击拍照等功能，合唱增加倒计时功能，录制界面新增混响和变声选择。
- iOS&Android：小视频 App 支持国际化，已支持中文、英文两种语言。
- iOS&Android：Demo 主界面重新设计，更清晰易用。
- Android：增加快速导入能力，适合大视频快速导入。
- Android：编辑增加滤镜程度设置接口。
- iOS：视频编辑支持 Two-pass 编码，生成更好的质量。
- iOS：解决录制非正常退出进入编辑导致 CPU 高的问题。
- iOS：解决 iOS12 短视频录制花屏的问题。

### Version 5.0 @ 2018-07-18
- iOS&Android：视频左右画面合成支持双人合唱。
- iOS&Android：编辑生成视频支持双声道。
- iOS&Android：录制支持设置音频采样率及渲染模式。
- Android：优化录制和编辑生成画质，生成文件更小。
- Android：优化编辑预处理速度和视频生成速度。
- Android：解决录制横竖屏切换黑屏问题。
- Android：修复录制快速单击开始结束报错的问题。
- iOS：优化编辑视频的加载速度。
- iOS：解决编辑生成视频偶现画面撕裂的问题。
- iOS：解决编辑生成视频末尾偶现黑帧的问题。
- iOS：修复编辑预览视频设置慢速播放，音频播放会提前结束的问题。
- iOS：iOS Demo 界面适配 iPhoneX。
- iOS：iOS 修复内存泄漏，提升稳定性，增加 module 定义更好的支持 swift 集成。

### Version 4.9 @ 2018-06-14
- Android&iOS：优化短视频 License 集成方式，支持自动续期。
- Android：短视频新增图片转视频能力，图片之间切换支持多种转场动画，包括上下左右滑动、放大、缩小、旋转缩放、淡入淡出等。
- Android：优化短视频编辑生成速度，解决内存泄漏等问题。
- iOS：优化短视频本地 BGM、微缩图加载速度及 videoInfo 获取速度。
- iOS：优化短视频编辑生成视频画质。
- iOS：解决短视频录制偶现卡顿和黑帧、片尾水印偶现闪烁、内存泄漏等问题

### Version 4.7 @ 2018-05-25
- iOS&Android：短视频增加新的滤镜特效，包括百叶窗、幻影、闪电、镜像、幻觉等。
- Android：自定义数据新增纹理支持。
- Android：优化短视频编辑合成内存占用，降低编辑生成期间内存使用峰值。
- iOS：短视频新增图片转视频能力，图片之间切换支持多种转场动画，包括上下左右滑动、放大、缩小、旋转缩放、淡入淡出等。
- iOS：短视频解决短视频 BGM 需要播放完才能回调的问题。

### Version 4.6 @ 2018-05-04
- iOS&Android：短视频录制新增会堂、磁性等混响效果，和萝莉、大叔等变声效果。
- iOS&Android：短视频录制的新增分片存储目录外部设置接口。
- iOS&Android：短视频编辑添加 BGM 支持纯视频流。
- iOS&Android：短视频合成新增分屏合成接口。
- iOS&Android：短视频录制取消上限码率限制。
- Android：优化小文件上传，提升成功率。
- Android：解决动效路径错误导致的 CRASH 问题。
- iOS：短视频支持 Bitcode。

### Version 4.5 @ 2018-04-13
- iOS&Android：Demo 新增上传功能的 Demo 代码，与点播服务进行整合，提供从拍摄到特效制作、上传、转码、鉴黄、分发、播放的一体化解决方案。
- iOS&Android：封面：上传封面支持 GIF 格式，新增片段合成功能。
- iOS&Android：短视频特效：新增两个特殊功能，支持去除动效背景音以及支持一键取消所有滤镜特效。
- Android: 对短视频制作过程进行优化，解决大文件上传后无法播放、获取缩略图偶现黑帧、某些视频音画不同步等问题。
- Android: 进行短视频编辑时允许对码率进行自定义设置。
- Android: 支持对无音轨的视频文件进行编辑。

### Version 4.2
iOS&Android：提升企业版 SDK 性能，开启 P 图动效，iOS 帧率显著提升，Android GPU 消耗降低。

### Version 4.1
- iOS&Android：短视频录制新增分辨率与码率切换接口。
- iOS&Android：短视频录制新增拍照接口。
- iOS&Android：短视频编辑 BGM 支持设置播放开始时间与循环播放能力。

### Version 3.9
- iOS&Android：动效贴纸大升级，新增 HDR 和高分辨率贴纸特效，贴纸更靓丽。
- iOS&Android：新增 AI 智能抠背景能力。
- iOS&Android：推出慢动作、重复播放、时光倒流三种时间特效。
- iOS&Android：新增多种滤镜，更多效果供您选择。
- iOS&Android：新增多种动态与静态贴纸，支持定制更多贴纸。
- iOS&Android：可以在视频中添加气泡字幕了。
- iOS&Android：支持静音拍摄，方便后期制作。
- iOS&Android：支持在拍摄时进行横竖屏切换。
- iOS&Android：修复若干 bug。
- Android：UGCPublish 接入全新 cos 架构，优化短视频上传处理流程。

### Version 3.4
- iOS&Android：短视频录制新增回删、多比例切换、焦距调节等功能。
- iOS&Android：短视频编辑新增片尾水印功能。
- iOS：解决 iOS11 兼容性问题。

### Version 3.3
- iOS&Android：修复过去一周客户提出的部分 bug。
- Android：解决 Android 在某些机型上录制绿屏及播放黑屏的问题。

### Version 3.1
- iOS&Android：企业版新增 V 脸、瘦鼻、瘦下巴等特性。
- iOS&Android：美颜算法优化，新增红润效果及多套美颜风格。
- Android：新增光滑、自然、朦胧三种美颜风格。
- Android：短视频编辑新增变速、背景音、字幕功能。
- iOS：新增光滑与自然两种美颜风格。

### Version 3.0
- iOS&Android：重构美颜模块，提升美颜效果同时降低 GPU 使用率。
- iOS&Android：TXUGCRecord 增加了 pauseRecord 和 resumeRecord 接口，用于支持多段录制。
- iOS：提供了快速裁剪和编辑接口。

### Version 2.0.5
- Android：短视频编辑添加水印功能。
- Android：短视频录制新增多段录制功能。
- iOS&Android：修复若干 bug。

### Version 2.0.4
- iOS&Android：UGC 录制增加美颜回调预处理接口。
- iOS&Android：短视频上传增加断点续传能力。
- Android：优化短视频裁剪、拼接功能，新增编辑滤镜功能。
- iOS：短视频编辑添加滤镜、水印、背景音、字幕、变速等功能。

### Version 2.0.3
- iOS&Android：优化 Demo 目录及代码结构，降低接入成本，新增小视频录制、裁剪、拼接 Demo，简单易用。
- Android：新增 UGC 裁剪与拼接功能。
- iOS：优化 iOS 过曝问题，曝光更自然。

### Version 2.0.2
- iOS&Android：优化 UGC 上传协议。
- Android：特权版新增大眼瘦脸功能。
- Android：优化硬编效果，提升编码质量。
- iOS：新增 UGC 裁剪与拼接功能。
- iOS：精简版支持 Bitcode。

### Version 2.0.1
- iOS&Android：增加 UGC 小视频添加背景音乐功能。
- Android：特权版新增绿幕功能。

### Version 2.0.0
iOS&Android：增加 UGC 小视频的采集和发布功能。


