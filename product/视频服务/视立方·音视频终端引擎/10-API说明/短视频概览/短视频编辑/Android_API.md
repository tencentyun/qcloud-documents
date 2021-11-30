## TXVideoEditer


### 短视频编辑基础接口
| API | 描述 |
|-----|-----|
| [TXVideoEditer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#ad0ab224b9b23eda9a60e91d7fe5f731f) | TXVideoEditer 构造函数 |
| [setVideoPath](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a3d98ae0fe0b5d77c2fe74451be48d7e4) | 设置视频路径，SDK 版本为 Android 18以上此接口有效 |
| [setCustomVideoProcessListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a5cc954ae1abd5e31bbee66f6fc108dd7) | 自定义图像处理（精简版不支持） |
| [release](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a23b477d0e2d399f75d585d154c346591) | 视频处理完或取消处理的视频，释放资源            |

### 特效相关函数

| API | 描述 |
|-----|-----|
| [setSpecialRatio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a1f6b0c14db22ca60390b271ca4295cf5) | 设置滤镜程度值（精简版不支持） |
| [setFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#ab32d5c2bd4ea611da429aa4975f62ec6) | 设置滤镜（精简版不支持） |
| [setFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a260c2d11847a0f5bb04a1048297ab193) | 设置组合滤镜特效（精简版不支持） |
| [setBeautyFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a583e0e9653f5653c0d77628cd1768e36) | 设置美颜，美白级别（精简版不支持） |
| [startEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a5c7153a4f3b01939521c111443ea3c3e) | 设置滤镜特效开始时间（精简版不支持）        |
| [stopEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a973981f257551331bf1e64d7fad3ac30) | 设置滤镜特效结束时间（精简版不支持）        |
| [deleteLastEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a9efcaf6c76e2fe1be9e389185768df9d) | 删除上一次添加的滤镜特效操作（精简版不支持） |
| [deleteAllEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a002990393f8440c3c0252ed1760c7e75) | 删除所有滤镜特效（精简版不支持）            |

### 视频生成相关函数

| API                                                          | 描述                         |
| ------------------------------------------------------------ | ---------------------------- |
| [setCutFromTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a1a7871599c714ffa06d20ea73e1ba7b5) | 设置视频剪切范围             |
| [setVideoBitrate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a58d953494573c1bd8f578f627bd4a953) | 设置生成视频码率             |
| [setAudioBitrate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a626d2ee662300262aa327828ea1e5458) | 设置生成的音频码率           |
| [setVideoGenerateListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a58218ba6d4be9ebc79f9e4f81b266b4c) | 设置编辑器生成视频监听       |
| [generateVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#af3f16bcb21f26c608c980b91671e386e) | 根据操作列表生成最终视频文件 |
| [cancel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a02d5fa6b14e221f3012a794b905be166) | 取消生成视频                 |

### 图片转视频相关函数

| API                                                          | 描述                              |
| ------------------------------------------------------------ | --------------------------------- |
| [setPictureList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#ae1305a003cc363651640cafd8dfa6f77) | 设置图片转视频参数（精简版不支持） |
| [setPictureTransition](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a13ff854740fff3897a2ee87c58525400) | 设置图片转场类型（精简版不支持）  |

### 设置时间特效相关函数

| API                                                          | 描述                            |
| ------------------------------------------------------------ | ------------------------------- |
| [setSpeedList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a4650c9432c973da02241c81bd2e9002f) | 设置多段倍速播放（精简版不支持） |
| [setRepeatPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#aa439a109f5f964b6acd2a8c25f5c85a4) | 设置多段重复片段（精简版不支持） |
| [setReverse](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a54a93c42a69b8e2c782a9b9cd3cb5ae2) | 视频倒放处理（精简版不支持）     |

### 预览逻辑相关方法

| API                                                          | 描述                                               |
| ------------------------------------------------------------ | -------------------------------------------------- |
| [setTXVideoPreviewListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#aeb200b38997fa6433d552f1480ea67d7) | 设置视频预览监听                                   |
| [initWithPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a15115ae00bfecc5fb463eb9eb72ecdcc) | 初始化预览 View                                    |
| [startPlayFromTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a41a3e3f4b9ebe7342a1ad69bc26b0ca2) | 播放某一时间段的视频                               |
| [pausePlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#af3334d06804b1d47ea3ce5be35dee73e) | 暂停播放                                           |
| [resumePlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a5ffa3b1cd2080af209af20b86905f22a) | 继续播放                                           |
| [stopPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a3d43f5cbda4c56e452cf74ec15d3d148) | 停止播放（释放资源）                               |
| [previewAtTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#aa223120c3f2b83d3a0965958d86bbf6f) | 单帧预览                                           |
| [refreshOneFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a9ae65ccf1ecda5e66f1a0ac0bd69eb30) | 用于编辑字幕界面。刷新一帧，显示不带字幕残影的图像 |
| [setRenderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a1ae55363f74a78d935d63ea7b44130a8) | 设置画面渲染角度（精简版不支持）                   |

### 短视频预处理相关函数

| API                                                          | 描述                 |
| ------------------------------------------------------------ | -------------------- |
| [setVideoProcessListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a73e2d92851802d47f78a7f7cd51a9375) | 设置短视频预处理回调 |
| [processVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#aa987a2d8cade3806e3ce06b50bf29761) | 短视频预处理         |

### 背景音乐相关函数

| API                                                          | 描述                                                  |
| ------------------------------------------------------------ | ----------------------------------------------------- |
| [setBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#adbd9b380aac0204e378b28d6bc461f01) | 设置背景音乐路径（精简版不支持）                       |
| [setBGMLoop](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a2bc4d6ff7be4d3a5be9298894ba9104a) | 设置背景音乐是否重复（精简版不支持）                   |
| [setBGMAtVideoTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a1a01fa05e3cd6b5af4f47cae951b30c1) | 设置背景音乐从视频的某个位置起开始添加（精简版不支持） |
| [setBGMStartTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#abbfc8be3c30285988e9e0cffc1d09e8c) | 可以选取音乐的起始时间和结束时间（精简版不支持）       |
| [setBGMVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a7fc2fe760afc4343afc033bb9da93a73) | 设置背景音乐声音大小（精简版不支持）                   |
| [setBGMFadeInOutDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#ad213b0abe0efee88eb4d7bcadf7a8747) | 设置背景音乐淡入淡出（精简版不支持）                   |
| [setVideoVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a274f5905b1f86da8e59a9df89f4ab418) | 设置视频声音大小（精简版不支持）                       |

### 贴纸相关方法（精简版不支持）

| API                                                          | 描述                                |
| ------------------------------------------------------------ | ----------------------------------- |
| [setPasterList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a029ea97bf271404576da7448de2c165f) | 设置静态贴纸（精简版不支持）         |
| [setAnimatedPasterList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a98a43a90684ce39cac00b26df2631316) | 设置动图列表（精简版不支持）         |
| [setSubtitleList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a95f8d9e278c5241bea021e62230abb02) | 设置字幕（气泡）列表（精简版不支持） |
| [setWaterMark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#abf5bb400f1d9d880e13ea59cd9eaadaa) | 设置水印 |
| [setTailWaterMark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a0d53a8b66fad82f05167ca4fbe7baee2) | 设置片尾水印（精简版不支持） |

### 水印相关方法

| API                                                          | 描述                        |
| ------------------------------------------------------------ | --------------------------- |
| [setWaterMark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#abf5bb400f1d9d880e13ea59cd9eaadaa) | 设置全局水印（精简版不支持） |
| [setTailWaterMark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a0d53a8b66fad82f05167ca4fbe7baee2) | 设置片尾水印（精简版不支持） |

### 缩略图相关函数

| API                                                          | 描述                     |
| ------------------------------------------------------------ | ------------------------ |
| [getThumbnail](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#aa851032ffa74d6fd94f205eaf0597366) | 获取缩略图列表           |
| [getThumbnail](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a151333765a1e2c98ea32fe13ea0cb655) | 获取缩略图列表           |
| [setThumbnail](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#ade2a9534fa3075883c551ce0163170c1) | 设置预处理输出的缩略图   |
| [setThumbnailListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a5baec0d91487fe6238f7e42879611e12) | 设置预处理输出缩略图回调 |
| [getThumbnailCount](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a5693e8dcdff926c7b840f5e49e5e47e4) | 获取缩略图数量           |

## TXVideoGenerateListener

### 短视频编辑回调接口

| API                                                          | 描述               |
| ------------------------------------------------------------ | ------------------ |
| [onGenerateProgress](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a07581798fba77eead03ff37c74065384) | 短视频生成进度回调 |
| [onGenerateComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#ae21c7177a91d25583ba6a0ad869093fe) | 短视频生成完成     |

## TXVideoPreviewListener

### 短视频预览回调接口

| API                                                          | 描述                    |
| ------------------------------------------------------------ | ----------------------- |
| [onPreviewProgress](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a35112d6d255e810bd6798ceefb5d5683) | 短视频预览进度，单位 us |
| [onPreviewFinished](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#afecc9f5e883fc46fa1cb0bb138d3cb3b) | 短视频预览结束回调      |

## TXVideoPreviewListenerEx

### 短视频预览回调接口

| API                                                          | 描述                     |
| ------------------------------------------------------------ | ------------------------ |
| [onPreviewError](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a61b3cb359e53a90564a5de1280b91223) | 短视频预览过程中发生错误 |
| [onPreviewProgress](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a35112d6d255e810bd6798ceefb5d5683) | 短视频预览进度，单位 us  |
| [onPreviewFinished](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#afecc9f5e883fc46fa1cb0bb138d3cb3b) | 短视频预览结束回调       |

## TXVideoProcessListener

### 短视频预处理回调接口

| API                                                          | 描述             |
| ------------------------------------------------------------ | ---------------- |
| [onProcessProgress](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#ac427df27a7b92aa07d84f17c9786fa1f) | 短视频预处理进度 |
| [onProcessComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#ac3343cd2111bf3b946b83fbc7149565f) | 短视频预处理完成 |

## TXVideoCustomProcessListener

### 短视频定制处理回调接口

| API                                                          | 描述                                           |
| ------------------------------------------------------------ | ---------------------------------------------- |
| [onTextureCustomProcess](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#af862bdc5a54f4097f9449bf4ef91d1d6) | 纹理处理回调，在这里可以进行采集图像的二次处理 |
| [onTextureDestroyed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#ac60f1dbbb1af39c666247c6438595de0) | 纹理释放回调，可以在这里释放创建的 OpenGL 资源 |

## TXThumbnailListener

### 获取缩略图回调接口

| API                                                          | 描述           |
| ------------------------------------------------------------ | -------------- |
| [onThumbnail](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__android.html#a2da29d316c2d34ab3977fe3f7686d5fa) | 获取缩略图回调 |

## TXVideoEditConstants

### 视频编辑关键类型定义
| API | 描述 |
|-----|-----|
| [TXVideoInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXVideoInfo) | 视频信息 |
| [TXPreviewParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXPreviewParam) | 短视频预览参数               |
| [TXGenerateResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXGenerateResult) | 短视频编辑结果               |
| [TXPreviewError](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXPreviewError) | 短视频预览错误               |
| [TXJoinerResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXJoinerResult) | 短视频合成结果               |
| [TXSubtitle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXSubtitle) | 字幕                         |
| [TXPaster](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXPaster) | 静态贴纸                     |
| [TXAnimatedPaster](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXAnimatedPaster) | 动态贴纸                     |
| [TXSpeed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXSpeed) | 变速                         |
| [TXRect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXRect) | 水印区域                     |
| [TXThumbnail](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXThumbnail) | 缩略图                       |
| [TXRepeat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXRepeat) | 重复片段                     |
| [TXAbsoluteRect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditConstants__android.html#classcom_1_1tencent_1_1ugc_1_1TXVideoEditConstants_1_1TXAbsoluteRect) | 画面合成每个视频的位置和宽高 |


[](id:error)
## 错误码

### 短视频编辑结果错误码

| 符号                                        | 值   | 含义                           |
| ------------------------------------------- | ---- | ------------------------------ |
| GENERATE_RESULT_OK                          | 0    | 生成视频成功                   |
| GENERATE_RESULT_FAILED                      | -1   | 生成视频失败                   |
| GENERATE_RESULT_LICENCE_VERIFICATION_FAILED | -5   | 生成视频失败，License 校验错误 |

### 短视频预览错误码定义

| 符号                            | 值   | 含义               |
| ------------------------------- | ---- | ------------------ |
| PREVIEW_ERROR_VIDEO_DECODE_FAIL | -1   | 预览视频，解码失败 |
