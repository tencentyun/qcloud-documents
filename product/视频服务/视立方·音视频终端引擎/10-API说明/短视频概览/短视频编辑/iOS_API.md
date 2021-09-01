## TXVideoEditer

### 构造函数

| API                          | 描述           |
| :----------------- | -------------- |
| [initWithPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a3c1008d9861aec98ac2f1e70f801c2c8) | 默认初始化方法 |

### 视频/图片设置相关方法

| API                          | 描述              |
| :----------------- | ------------ |
| [setVideoPath](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#af98d827c56a0a50893afb1ef358ef36c) | 设置视频文件路径          |
| [setVideoAsset](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a481fdf89e37b523f53bafe15e2ab3a3b) | 设置视频 AVAsset          |
| [setPictureList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#ab4a88a0f32702ee4c732d873d8804ac1) | 设置转场图片列表（ 精简版不支持） |
| [setPictureTransition](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a7a934af28bb7059f9f1e03252cd7aa71) | 设置图片转场类型（ 精简版不支持） |



### 预览逻辑相关方法

| API                          | 描述           |
| :----------------- | ---------------------- |
| [previewAtTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#ac179878f3f6c91d17bb60624a5029d56) | 渲染某一时刻的视频画面 |
| [startPlayFromTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a0a2615f86cacd81305abb2395d7f81d7) | 播放某一时间段的视频   |
| [pausePlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#af3334d06804b1d47ea3ce5be35dee73e) | 暂停播放       |
| [resumePlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a5ffa3b1cd2080af209af20b86905f22a) | 继续播放       |
| [stopPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a3d43f5cbda4c56e452cf74ec15d3d148) | 停止播放       |



### 特效相关方法

| API                          | 描述                    |
| :----------------- | ------------------ |
| [setBeautyFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#afe970c160baf293e9729455317518339) | 设置美颜，美白级别 0 - 9        |
| [setFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a05ed2f02c5b5514d7342ab50d4052d59) | 设置特效滤镜            |
| [setFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a44d7f0da7adb1aa2f62a3afd6d7c4b1c) | 设置两个滤镜效果                |
| [setSpecialRatio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a6de9ce92116926fe9b53016151d55784) | 设置滤镜效果程度                |
| [setReverse](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a3101209b2c2f5acb2dfffbcb126dd650) | 设置倒放（ 精简版不支持）       |
| [setRepeatPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a43b71deca5d9f529a12fa08cfcd71860) | 设置重复播放（ 精简版不支持）           |
| [setRenderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#aedfa7b798e073a450c2b2fbb5063955c) | 设置画面渲染角度（ 精简版不支持）       |
| [setSpeedList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a920e34fb4cd1a3818a400e02ae1c39f0) | 设置视频加速播级别（ 精简版不支持）     |
| [startEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#af6ef3fab8f2d5871c2b63571daf0f6a8) | 开始特效（ 精简版不支持）       |
| [stopEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a23fd51ba880b96b3d00fa4c5c50a0cd0) | 结束特效（ 精简版不支持）       |
| [deleteLastEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a9efcaf6c76e2fe1be9e389185768df9d) | 删除最后一个添加的特效（ 精简版不支持） |
| [deleteAllEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a002990393f8440c3c0252ed1760c7e75) | 删除所有特效（ 精简版不支持）           |



### 贴纸相关方法（ 精简版不支持）

| API                          | 描述                  |
| :----------------- | ---------------- |
| [setSubtitleList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a61765dfd460768954def11cb8f615d0f) | 设置字幕（气泡）列表（ 精简版不支持） |
| [setPasterList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a66ea4fd1f8f4170d2551ace9d7ef7e07) | 设置静态贴纸（ 精简版不支持）         |
| [setAnimatedPasterList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a979a0d339aef335525f1a7c92b6ab930) | 设置动图列表（ 精简版不支持）         |



### BGM相关方法

| API                          | 描述                        |
| :----------------- | ------------------------------ |
| [setBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a59a3956d1bdeb12a0701d48c5e85259a) | 设置背景音乐（ 精简版不支持）               |
| [setBGMAsset](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a89357b40d1c45c47a1e1ecee47d45476) | 设置背景音乐（ 精简版不支持）               |
| [setBGMStartTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a26de512c64562ba0d2eeccdde7c6c9e5) | 设置背景音乐的起始时间和结束时间（ 精简版不支持）   |
| [setBGMLoop](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#af04ec84d6367837b6a3ec009d42f3dc1) | 设置背景音乐是否循环播放（ 精简版不支持）           |
| [setBGMAtVideoTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#aef28b77ad3642c0a608887a94b155b31) | 设置背景音乐在视频的添加的起始位置（ 精简版不支持） |
| [setVideoVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a113de64447f37f924a8493e2cc2216ed) | 设置视频声音大小（ 精简版不支持）           |
| [setBGMVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a9a8155eedd2621ab628f4e503f1e8d72) | 设置背景音乐声音大小（ 精简版不支持）       |
| [setBGMFadeInDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a23e629dc5ddffaaadb994e3e9095986d) | 设置背景音淡入淡出                  |



### 水印相关方法

| API                          | 描述                  |
| :----------------- | -------- |
| [setWaterMark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a7ee69499e0ca3bd9a7c996505725c384) | 设置全局水印（ 精简版不支持） |
| [setTailWaterMark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a023510027d5c1238f61004b4309432ee) | 设置片尾水印（ 精简版不支持） |



## TXVideoPreviewListener

### 短视频预览回调接口

| API                          | 描述                   |
| :----------------- | ------------------------- |
| [onPreviewProgress](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerListener__ios.html#a80858908a27f740310ba970700624e78) | 短视频预览进度 time 视频预览的当前时间，单位 s |
| [onPreviewFinished](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerListener__ios.html#afecc9f5e883fc46fa1cb0bb138d3cb3b) | 短视频预览结束回调             |



## TXVideoCustomProcessListener

### 短视频定制处理回调接口

| API                          | 描述                   |
| :----------------- | ------------------------- |
| [onPreProcessTexture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerListener__ios.html#a291f788c080dc4fb941ff5a955e249de) | 纹理处理回调，在这里可以进行采集图像的二次处理 |
| [onTextureDestoryed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerListener__ios.html#a837386fa6d1b5614758950415132ba54) | 纹理释放回调，可以在这里释放创建的 OpenGL 资源 |



## TXVideoGenerateListener

### 短视频编辑回调接口

| API                          | 描述       |
| :----------------- | ------------------ |
| [onGenerateProgress](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerListener__ios.html#aba8d22bff87bcf57b5983943ed8e80b2) | 短视频生成进度回调 |
| [onGenerateComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerListener__ios.html#ad8b78c0c81565b6ad4b4b3cff084f21c) | 短视频生成完成回调 |



## TXVideoJoinerListener

### 短视频合成、拼接回调接口

| API                          | 描述       |
| :----------------- | ------------------ |
| [onJoinProgress](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerListener__ios.html#a36b82d985b2b1b4061d85011775ab990) | 短视频合成进度回调 |
| [onJoinComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerListener__ios.html#a697a4af42d55870db7e6e44f496b0c05) | 短视频合成完成回调 |



## TXVideoEditerTypeDef

### 视频编辑关键类型定义

| API                          | 描述           |
| :----------------- | -------------- |
| [TXVideoInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#interfaceTXVideoInfo) | 视频信息       |
| [TXPreviewParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#interfaceTXPreviewParam) | 短视频预览参数 |
| [TXGenerateResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#interfaceTXGenerateResult) | 短视频编辑结果 |
| [TXJoinerResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#interfaceTXJoinerResult) | 短视频合成结果 |
| [TXSubtitle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#interfaceTXSubtitle) | 字幕           |
| [TXPaster](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#interfaceTXPaster) | 静态贴纸       |
| [TXAnimatedPaster](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#interfaceTXAnimatedPaster) | 动态贴纸       |
| [TXSpeed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#interfaceTXSpeed) | 变速           |
| [TXRepeat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#interfaceTXRepeat) | 重复片段       |



### 枚举类型说明

| API                          | 描述           |
| :----------------- | ---------------------- |
| [TXPreviewRenderMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#gae22e497eeef02bd2932af70216cfe734) | 短视频预览参数         |
| [TXSpeedLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#ga1ba0fcb4536220e2f5bafdd02204f924) | 快慢速播放类型         |
| [TXEffectType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#gabb3a6a2a2d5ffadaf15516689f79023a) | 视频特效类型           |
| [TXTransitionType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#gad971f27e135976a5e02cbcf4683a881c) | 转场特效       |
| [TXGenerateResultCode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#gae52fdbff9ec4fc124e28000780dab967) | 生成视频结果错误码定义 |
| [TXJoinerResultCode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#ga773a8be62fe93b8e06824136e06778fe) | 视频合成结果错误码定义 |
| [TXVideoCompressed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditerTypeDef__ios.html#a8ea073944cdda7933d033d1aa74d77d7) | 短视频压缩质量         |


[](id:error)
## 错误码

### 生成视频结果错误码

| 符号                        | 值   | 含义                   |
| :--------------------- | ---- | --------- |
| GENERATE_RESULT_OK                  | 0    | 生成视频成功           |
| GENERATE_RESULT_FAILED              | -1   | 生成视频失败           |
| GENERATE_RESULT_CANCEL              | -2   | 生成视频取消           |
| GENERATE_RESULT_LICENCE_VERIFICATION_FAILED | -5   | 生成视频失败，License 校验错误 |



### 视频合成结果错误码

| 符号                      | 值   | 含义             |
| -------------------- | ---- | ---------------- |
| JOINER_RESULT_OK                  | 0    | 合成成功         |
| JOINER_RESULT_FAILED              | -1   | 合成失败         |
| JOINER_RESULT_LICENCE_VERIFICATION_FAILED | -5   | License 验证失败 |
