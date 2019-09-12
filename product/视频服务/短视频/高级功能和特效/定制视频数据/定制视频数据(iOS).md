## 录制预处理回调
```objc
/**
 * 在OpenGL线程中回调，在这里可以进行采集图像的二次处理
 * @param texture    纹理ID
 * @param width      纹理的宽度
 * @param height     纹理的高度
 * @return           返回给SDK的纹理
 * 说明：SDK回调出来的纹理类型是GL_TEXTURE_2D，接口返回给SDK的纹理类型也必须是GL_TEXTURE_2D; 该回调在SDK美颜之后. 纹理格式为GL_RGBA
 */
- (GLuint)onPreProcessTexture:(GLuint)texture width:(CGFloat)width height:(CGFloat)height;

/**
 * 人脸数据回调（商业版接口）
 * @prama points 人脸坐标
 *  说明：使用了人脸识别的相关功能如人脸识别贴纸、大眼或者瘦脸等。此回调在onPreProcessTexture:width:height:之前会被调用
 */
- (void)onDetectFacePoints:(NSArray *)points;

/**
 * 在OpenGL线程中回调，可以在这里释放创建的OpenGL资源
 */
- (void)onTextureDestoryed;
```
## 编辑预处理回调
```objc
/** 
 在OpenGL线程中回调，在这里可以进行采集图像的二次处理
 @param texture    纹理ID
 @param width      纹理的宽度
 @param height     纹理的高度
 @param timestamp        纹理timestamp 单位ms
 @return           返回给SDK的纹理
 说明：SDK回调出来的纹理类型是GL_TEXTURE_2D，接口返回给SDK的纹理类型也必须是GL_TEXTURE_2D; 该回调在SDK美颜之后. 纹理格式为GL_RGBA
 timestamp 为当前视频帧的 pts ，单位是ms ，客户可以根据自己的需求自定义滤镜特效
 */
- (GLuint)onPreProcessTexture:(GLuint)texture width:(CGFloat)width height:(CGFloat)height timestamp:(UInt64)timestamp;

/**
 * 在OpenGL线程中回调，可以在这里释放创建的OpenGL资源
 */
- (void)onTextureDestoryed;
```
