## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | &#10003;  | &#10003;                                                            | -  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 示例代码
针对开发者的接入反馈的高频问题，腾讯云视立方提供有更加简洁的 API-Example 工程，方便开发者可以快速的了解相关 API 的使用，欢迎使用。

| 所属平台 |                         GitHub 地址                          |
| :------: | :----------------------------------------------------------: |
|   iOS    | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/MLVB-API-Example) |
| Android  | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/Android/MLVB-API-Example) |


## 定制推流画面

### iOS 平台

<dx-tabs>
::: 方案一：修改\sOpenGL\s纹理
如果您有自定义图像处理的需求（例如：堆加字幕），同时又希望复用 LiteAV SDK 的整体流程，您可以按照如下攻略进行定制。
1. 首先需要调用 V2TXLivePusher 的 [enableCustomVideoProcess](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a36a27d1112103ca70954c72a5d9109ce) 开启自定义视频处理，才会收到这个回调通知。
2. 处理图像时分为两种情况。
	- **美颜组件会产生新的纹理：**
	如果您使用的美颜组件会在处理图像的过程中产生一帧全新的纹理（用于承载处理后的图像），那请您在回调函数中将 `dstFrame.textureId` 设置为新纹理的 ID。
```objectiveC
- (void) onProcessVideoFrame:(V2TXLiveVideoFrame _Nonnull)srcFrame dstFrame:(V2TXLiveVideoFrame _Nonnull)dstFrame
   {
       GLuint dstTextureId = renderItemWithTexture(srcFrame.textureId, srcFrame.width, srcFrame.height);
       dstFrame.textureId = dstTextureId;
   }
```
	- **美颜组件并不自身产生新纹理：**
如果您使用的第三方美颜模块并不生成新的纹理，而是需要您设置给该模块一个输入纹理和一个输出纹理，则可以考虑如下方案：
```objectiveC
- (void) onProcessVideoFrame:(V2TXLiveVideoFrame _Nonnull)srcFrame dstFrame:(V2TXLiveVideoFrame _Nonnull)dstFrame
   {
       thirdparty_process(srcFrame.textureId, srcFrame.width, srcFrame.height, dstFrame.textureId);
   }
```
3. 最后，对于 texture 数据的操作，需要一定的 OpenGL 基础知识，另外计算量不宜太大，因为 onProcessVideoFrame 的调用频率跟 FPS 相同，过于繁重的处理很容易造成 GPU 过热。
:::
::: 方案二：自己采集数据
如果您只希望使用 SDK 来编码和推流（例如已经对接了商汤等产品），视频采集和预处理（即美颜、滤镜这些）全部由自己的代码来控制，可以按如下步骤实现：

1. 调用 V2TXLivePusher 的 [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a35e33064526da7f360c786a63d4e33e5) 接口开启自定义采集。
这样 SDK 本身就不会再采集视频数据，而只是启动编码、流控、发送等跟推流相关的工作。
2. 通过 V2TXLivePusher 的 [sendCustomVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a70770d15cc87cf91c174df97cf45a683) 向 SDK 填充 Video 数据。
<dx-codeblock>
::: objectiveC objectiveC
/**
 * @brief 在自定义视频采集模式下，将采集的视频数据发送到SDK。<br/>
 *        在自定义视频采集模式下，SDK不再采集摄像头数据，仅保留编码和发送功能。
 *        您可以把采集到的 SampleBuffer 打包到 V2TXLiveVideoFrame 中，然后通过该API定期的发送。
 *
 * @note  需要在 [startPush](@ref V2TXLivePusher#startPush:) 之前调用 [enableCustomVideoCapture](@ref V2TXLivePusher#enableCustomVideoCapture:) 开启自定义采集。
 *
 * @param videoFrame 向 SDK 发送的 视频帧数据 {@link V2TXLiveVideoFrame}
 *
 * @return 返回值 {@link V2TXLiveCode}
 *         - V2TXLIVE_OK: 成功
 *         - V2TXLIVE_ERROR_INVALID_PARAMETER: 发送失败，视频帧数据不合法
 *         - V2TXLIVE_ERROR_REFUSED: 您必须先调用 enableCustomVideoCapture 开启自定义视频采集。
 */
- (V2TXLiveCode)sendCustomVideoFrame:(V2TXLiveVideoFrame *)videoFrame;
:::
</dx-codeblock>
:::
</dx-tabs>

### Android 平台

<dx-tabs>
::: 方案一：修改\sOpenGL\s纹理
如果您有自定义图像处理的需求（例如堆加字幕），同时又希望复用 LiteAV SDK 的整体流程，您可以按照如下攻略进行定制。
1. 首先需要调用 V2TXLivePusher 的 [enableCustomVideoProcess](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html#ab3d49118931e09d1d4954674ff8a8102) 开启自定义视频处理，才会收到这个回调通知。
2. 处理图像时分为两种情况。
	-  **美颜组件会产生新的纹理：**
	如果您使用的美颜组件会在处理图像的过程中产生一帧全新的纹理（用于承载处理后的图像），那请您在回调函数中将 `dstFrame.textureId` 设置为新纹理的 ID。
```java 
private class MyPusherObserver extends V2TXLivePusherObserver {
    @Override
    public void onGLContextCreated() {
        mFURenderer.onSurfaceCreated();
        mFURenderer.setUseTexAsync(true);
    }

    @Override
    public int onProcessVideoFrame(V2TXLiveVideoFrame srcFrame, V2TXLiveVideoFrame dstFrame) {
        dstFrame.texture.textureId = mFURenderer.onDrawFrameSingleInput(
                srcFrame.texture.textureId, srcFrame.width, srcFrame.height);
        return 0;
    }

    @Override
    public void onGLContextDestroyed() {
        mFURenderer.onSurfaceDestroyed();
    }
}
```
	-  **美颜组件并不自身产生新纹理：**
如果您使用的第三方美颜模块并不生成新的纹理，而是需要您设置给该模块一个输入纹理和一个输出纹理，则可以考虑如下方案：
```java 
@Override
    public int onProcessVideoFrame(V2TXLiveVideoFrame srcFrame, V2TXLiveVideoFrame dstFrame) {
        thirdparty_process(srcFrame.texture.textureId, srcFrame.width, srcFrame.height, dstFrame.texture.textureId);
        return 0;
}
```
3. 最后，对于 texture 数据的操作，需要一定的 OpenGL 基础知识，另外计算量不宜太大，因为 onProcessVideoFrame 的调用频率跟 FPS 相同，过于繁重的处理很容易造成 GPU 过热。
:::
::: 方案二：自己采集数据
如果您只希望使用 SDK 来编码和推流（例如已经对接了商汤等产品），视频采集预处理（即美颜、滤镜这些）全部由自己的代码来控制，可以按如下步骤实现：

1. 调用 V2TXLivePusher 的 [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html#a9d945c58c4e0ff24e55aacef1ef3090f) 接口开启自定义采集。
这样 SDK 本身就不会再采集视频数据，而只是启动编码、流控、发送等跟推流相关的工作。
2. 通过 V2TXLivePusher 的 [sendCustomVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html#a3802124d90bf00434245d2956dad1fe4) 向 SDK 填充 Video 数据。
<dx-codeblock>
::: java java
/**
 * @brief 在自定义视频采集模式下，将采集的视频数据发送到SDK。 <br/>
 *        在自定义视频采集模式下，SDK不再采集摄像头数据，仅保留编码和发送功能。
 *
 * @note  需要在 {@link V2TXLivePusher#startPush(String)} 之前调用 {@link V2TXLivePusher#enableCustomVideoCapture(boolean)} 开启自定义采集。
 *
 * @param videoFrame 向 SDK 发送的 视频帧数据 {@link V2TXLiveVideoFrame}
 *
 * @return 返回值 {@link V2TXLiveCode}
 *         - V2TXLIVE_OK: 成功
 *         - V2TXLIVE_ERROR_INVALID_PARAMETER: 发送失败，视频帧数据不合法
 *         - V2TXLIVE_ERROR_REFUSED: 发送失败，您必须先调用 enableCustomVideoCapture 开启自定义视频采集
   */
    public abstract int sendCustomVideoFrame(V2TXLiveVideoFrame videoFrame);
:::
</dx-codeblock>
:::
</dx-tabs>

## 定制播放数据

### iOS 平台
1.  设置 [V2TXLivePlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html) 的 [V2TXLivePlayerObserver](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html) 监听。
<dx-codeblock>
::: objectiveC objectiveC
@interface V2TXLivePlayer : NSObject
/**
 * @brief 设置播放器回调。<br/>
 *        通过设置回调，可以监听 V2TXLivePlayer 播放器的一些回调事件，
 *        包括播放器状态、播放音量回调、音视频首帧回调、统计数据、警告和错误信息等。
 *
 * @param observer 播放器的回调目标对象，更多信息请查看 {@link V2TXLivePlayerObserver}
 */
- (void)setObserver:(id<V2TXLivePlayerObserver>)observer;
:::
</dx-codeblock>
2.  通过 [onRenderVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html#a1ee10f163275f3b9316ce387573fcbe1) 回调捕获 Player 的图像数据。
<dx-codeblock>
::: objectiveC objectiveC
/**
 * @brief 视频帧信息。
 *        V2TXLiveVideoFrame 用来描述一帧视频画面的裸数据，它可以是一帧编码前的画面，也可以是一帧解码后的画面。
 * @note  自定义采集和自定义渲染时使用。自定义采集时，需要使用 V2TXLiveVideoFrame 来包装待发送的视频帧；自定义渲染时，会返回经过 V2TXLiveVideoFrame 包装的视频帧。
 */
    @interface V2TXLiveVideoFrame : NSObject

///【字段含义】视频帧像素格式
///【推荐取值】V2TXLivePixelFormatNV12
@property(nonatomic, assign) V2TXLivePixelFormat pixelFormat;

///【字段含义】视频数据包装格式
///【推荐取值】V2TXLiveBufferTypePixelBuffer
@property(nonatomic, assign) V2TXLiveBufferType bufferType;

///【字段含义】bufferType 为 V2TXLiveBufferTypeNSData 时的视频数据
@property(nonatomic, strong, nullable) NSData *data;

///【字段含义】bufferType 为 V2TXLiveBufferTypePixelBuffer 时的视频数据
@property(nonatomic, assign, nullable) CVPixelBufferRef pixelBuffer;

///【字段含义】视频宽度
@property(nonatomic, assign) NSUInteger width;

///【字段含义】视频高度
@property(nonatomic, assign) NSUInteger height;

///【字段含义】视频帧的顺时针旋转角度
@property(nonatomic, assign) V2TXLiveRotation rotation;

///【字段含义】视频纹理ID
@property (nonatomic, assign) GLuint textureId;

@end


@protocol V2TXLivePlayerObserver <NSObject>
@optional
/**
 * @brief 自定义视频渲染回调
 *
 * @note  调用 [enableCustomRendering](@ref V2TXLivePlayer#enableCustomRendering:pixelFormat:bufferType:) 开启自定义渲染之后，会收到这个回调通知
 *
 * @param videoFrame  视频帧数据 {@link V2TXLiveVideoFrame}
 */
- (void)onRenderVideoFrame:(id<V2TXLivePlayer>)player
                     frame:(V2TXLiveVideoFrame *)videoFrame;
                 @end
:::
</dx-codeblock>

### Android 平台
1.  设置 [V2TXLivePlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html) 的 [V2TXLivePlayerObserver](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__android.html) 监听。
<dx-codeblock>
::: java java
public abstract void setObserver(V2TXLivePlayerObserver observer)
:::
</dx-codeblock>
2.  通过 [onRenderVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__android.html#a346a3206ad4d0f38385844c1456a012f) 回调捕获 Player 的图像数据。
<dx-codeblock>
::: java java
public final static class V2TXLiveVideoFrame
{
    /// 视频像素格式
    public V2TXLivePixelFormat pixelFormat = V2TXLivePixelFormat.V2TXLivePixelFormatUnknown;
    /// 视频数据包装格式
    public V2TXLiveBufferType bufferType   = V2TXLiveBufferType.V2TXLiveBufferTypeUnknown;
    /// 视频纹理包装类
    public V2TXLiveTexture texture;
    /// 视频数据
    public byte[]       data;
    /// 视频数据
    public ByteBuffer   buffer;
    /// 视频宽度
    public int          width;
    /// 视频高度
    public int          height;
    /// 视频像素的顺时针旋转角度
    public int          rotation;
}

public abstract class V2TXLivePlayerObserver {
    /**
     * 自定义视频渲染回调
          *
          *  @param player     回调该通知的播放器对象
               *  @param videoFrame 视频帧数据 {@link V2TXLiveVideoFrame}
               */
            void onRenderVideoFrame(V2TXLivePlayer player, V2TXLiveVideoFrame videoFrame);
}
:::
</dx-codeblock>
