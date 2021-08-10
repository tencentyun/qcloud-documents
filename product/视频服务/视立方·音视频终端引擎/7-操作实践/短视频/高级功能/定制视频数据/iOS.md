## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。



## 录制预处理回调 

<dx-codeblock>
::: objc objc
/**

 * 在 OpenGL 线程中回调，在这里可以进行采集图像的二次处理
 * @param texture    纹理 ID
 * @param width      纹理的宽度
 * @param height     纹理的高度
 * @return           返回给 SDK 的纹理
 * 说明：SDK 回调出来的纹理类型是 GL_TEXTURE_2D，接口返回给 SDK 的纹理类型也必须是 GL_TEXTURE_2D; 该回调在 SDK 美颜之后. 纹理格式为 GL_RGBA
 */
- (GLuint)onPreProcessTexture:(GLuint)texture width:(CGFloat)width height:(CGFloat)height;

/**
 * 五官位置回调（企业版接口）
 * @prama points 五官坐标
 * 说明：使用了挂件的相关功能如动效贴纸、大眼或者瘦脸等。此回调在 onPreProcessTexture:width:height: 之前会被调用
 */
- (void)onDetectFacePoints:(NSArray *)points;

/**
 * 在 OpenGL 线程中回调，可以在这里释放创建的 OpenGL 资源
 */
- (void)onTextureDestoryed;
:::
</dx-codeblock>


## 编辑预处理回调
<dx-codeblock>
::: objc objc
/** 
 在 OpenGL 线程中回调，在这里可以进行采集图像的二次处理
 @param texture    纹理 ID
 @param width      纹理的宽度
 @param height     纹理的高度
 @param timestamp        纹理 timestamp 单位 ms
 @return           返回给 SDK 的纹理
 说明：SDK 回调出来的纹理类型是 GL_TEXTURE_2D，接口返回给 SDK 的纹理类型也必须是 GL_TEXTURE_2D; 该回调在 SDK 美颜之后. 纹理格式为 GL_RGBA
 timestamp 为当前视频帧的 pts ，单位是 ms ，客户可以根据自己的需求自定义滤镜特效
 */
- (GLuint)onPreProcessTexture:(GLuint)texture width:(CGFloat)width height:(CGFloat)height timestamp:(UInt64)timestamp;

/**
 * 在 OpenGL 线程中回调，可以在这里释放创建的 OpenGL 资源
 */
- (void)onTextureDestoryed;
:::
</dx-codeblock>
