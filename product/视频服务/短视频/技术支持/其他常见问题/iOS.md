
### 关于 license 的问题

短视频 SDK 分基础版和商业版，从 4.5 版本开始需要 Licence，基础版只需要短视频的 Licence（TXUgcSDK.licence），商业版还同时需要 Pitu 的 Licence（YTFaceSDK.licence），把 Licence 放到工程目录，并修改为对应的名字即可。

4.9 版本开始 Licence 使用方式有改变，可以选择是否把 Licence 打包到项目中。使用时需要调用 setLicenceURL: key: 接口设置 Licence 的 url 和 key。
> [注意] 4.5 ~ 4.7 版本的 SDK 不支持 Licence 自动续期，4.9 版本开始才支持自动续期。4.9 的 SDK 可以兼容之前的 Licence（url 和 key 不能传 null，可以随便传个字符串），但是新的 Licence 无法在 4.9 之前的 SDK 上使用。


### 关于 TXUGCPublish.h 的问题

从 4.5 版本开始，`TXUGCPublish` 相关的类从 SDK 上移到了 Demo 层，开发者如果需要使用，使用时直接把 `VideoUpload` 目录整个拖入自己的工程即可。



### Xcode 中直接运行 Demo 报错

需要选择对应的 Target，如下图：
![](https://main.qcloudimg.com/raw/bafe4d2c775330a29b4478be270022fc.jpg)


### 连接 Xcode 调试，短视频录制报错（此问题在4.9版本已经修复）

连接 Xcode 调试，短视频录制报错，报错信息：`Main Thread Checker: UI API called on a background thread`
![](https://main.qcloudimg.com/raw/04b272c456b0e69239c0867a8e964d7a.jpg)
原因是某些 API（一般是UI相关的）需要在主线程调用，如果在非主线程调用，同时有勾选 `Main Thread Checker` 的话，就会报错。

解决办法：`Product` -> `Scheme` -> `Edit Scheme` -> `Run` -> `Diagnostics`，取消勾选 `Main Thread Checker`。



### 使用 SDK 时报找不到头文件

- 在 `Build Settings` -> `Search Paths` -> `Header Search Paths` 中添加头文件搜索路径。
- 使用 `"TXLiteAVSDK_UGC/XXX.h"`方式引用 SDK 的头文件。
- 使用 `@import TXLiteAVSDK_UGC;`方式引用 SDK (5.0及之后的版本)。

以上几种方法选其一。



### 运行工程时报找不到类别方法或者 crash

SDK 用到了一些类别的方法，加载类别方法需要在工程配置：`Build Settings` -> `Linking` -> `Other Linker Flags` 添加 `-ObjC`。



### 录制短视频时设置背景音乐无效

1. 确定传的 BGM path 下有没有文件，以及是否可以正常播放。

2. 确定接口的调用顺序：`startCameraSimple:preview:` -> `setBGM:` -> `startRecord`。

> [注意] 很多接口调用有时序要求，不然会无效。一般在注释上会有说明。
例如短视频录制的 `setVideoResolution:`、`setVideoBitrate:`、`setAspectRatio:` 等接口都需要在 `startRecord` 之前设置才有效。


### 录制设置 BGM 不能循环播放

目前逻辑暂未支持循环播放。


### 录制设置 BGM，`endTime` 时没有完成回调

如果设置的 `endTime` 小于音乐文件总时长，4.6 及之前的版本是在 BGM 播放完后才会触发完成回调，从 4.7 版本开始在 `endTime` 时触发完成回调。


### 为什么录制时第一次打开摄像头比较慢？

苹果手机摄像头第一次打开时（冷启动）耗时相对较长，通过系统接口打开摄像头也是如此。

因为摄像头打开的操作不适合放在子线程去做，经过测试在子线程中进行打开摄像头操作耗时会更大，并且在主线程连续打开/关闭摄像头的时候，子线程的响应延迟会更高，体验不好。


### 返回继续录制怎么实现？

在第一次录制完成的时候，不要调用 `stopRecord` 和 `stopCameraPreview`（调用之后不能再继续录制，只能重新录制），可以调用`pauseRecord`，然后通过 `TXUGCPartsManager.getVideoPathList` 获取已经录取的视频片段，通过 `TXVideoJoiner.joinVideo` 合成最终视频（4.5之前版本），还可以直接调用 `TXUGCPartsManager.joinAllParts` 合成最终视频，这个方法合成速度更快（4.5 以后版本支持），这样当返回继续录制的时候，所有的录制状态都在，可以继续录制。


### 短视频录制完成时收不到完成回调

- 确定有没有调用 stopRecord，只有调用 stopRecord 后才会有完成回调。
- 确定函数的调用是否都在主线程。



### 录制过程中用其他播放器播放视频，返回继续录制，声音录制不了

iOS 中的 AudioSession 是所有音视频应用共用的，使用其他播放器播放的时候，AudioSession 会被占用，播放结束时如果 AudioSession 没有让出或者让出不及时，会导致录制模块的 AudioSession 失效，SDK 提供了 `-(void) pauseAudioSession` 和 `-(void) resumeAudioSession` 两个接口，在去其他播放器预览的时候先调用 `pauseAudioSession`，返回继续录制前调用 `resumeAudioSession`。



### 为什么录制出来的视频不清晰？

码率和分辨率不匹配，录制出来的视频就会不清晰。可以通过适当增大码率、开启B帧来提升画质。



### 视频编辑时退后台再回到前台，视频生成失败

生成视频默认采用的是硬编码（编码效率高，编码出来的图像效果好），硬编码器在程序进后台后会停止工作，从而导致视频生成失败。SDK 提供了两个接口 `pauseGenerate` 和 `resumeGenerate`，APP 进后台时可以调用 `pauseGenerate` 暂停视频生成，APP 回到前台后再调用 `resumeGenerate` 继续视频生成。

> [注意] 调用 `resumeGenerate`，SDK 将重启硬编码器，有一定的概率重启失败，或重启后前几帧数据编码失败。此时，SDK 内部会在 `TXVideoGenerateListener` 抛出错误事件，收到错误事件后需要重新生成视频。



### 文件上传失败

文件上传状态码：

![](https://main.qcloudimg.com/raw/555615a2b4ee9277d10a1258750635dc.png)
1. 确定上传的文件是否在本地沙盒，如果上传媒体库的文件，需要先 copy 到本地沙盒。
2. 返回错误码1002：签名有问题、时间戳过期、点播服务问题（未开通或停服）。
3. 返回错误码1003：请求参数问题、上传文件格式不支持。



### 短视频录制是否有拍照功能？

短视频 SDK 可以实现拍照功能，开始预览后调用 `TXUGCRecord` 类的 `snapshot` 接口获取图片即可。


