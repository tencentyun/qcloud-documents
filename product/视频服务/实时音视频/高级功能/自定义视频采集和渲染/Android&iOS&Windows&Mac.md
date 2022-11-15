本文档主要介绍如何使用 TRTC SDK 实现自定义视频采集和渲染，分为：视频采集、视频渲染两个部分。

## 自定义视频采集

TRTC SDK 的自定义视频采集功能的开启分为两步，即：开启功能、发送视频帧给 SDK，具体 API 使用步骤见下文，同时我们也提供有对应平台的的API-Example：

- [Android](https://github.com/LiteAVSDK/TRTC_Android/blob/main/TRTC-API-Example/Advanced/LocalVideoShare/src/main/java/com/tencent/trtc/mediashare/LocalVideoShareActivity.java)
- [iOS](https://github.com/LiteAVSDK/TRTC_iOS/blob/main/TRTC-API-Example-OC/Advanced/LocalVideoShare/LocalVideoShareViewController.m)
- [Windows](https://github.com/LiteAVSDK/TRTC_Windows/blob/main/TRTC-API-Example-C++/TRTC-API-Example-Qt/src/TestCustomCapture/test_custom_capture.cpp) 

### 开启自定义视频采集功能

首先，您需要调用 TRTCCloud 的 `enableCustomVideoCapture` 接口开启  TRTC SDK 自定义视频采集的功能，开启后会跳过 TRTC SDK 自己的摄像头采集和图像处理逻辑，仅保留编码和传输能力，示例代码如下：

<dx-codeblock>
::: Android  Java
TRTCCloud mTRTCCloud = TRTCCloud.shareInstance();
mTRTCCloud.enableCustomVideoCapture(TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, true);
:::
::: iOS&Mac  ObjC
self.trtcCloud = [TRTCCloud sharedInstance];
[self.trtcCloud enableCustomVideoCapture:TRTCVideoStreamTypeBig enable:YES];
:::
::: Windows  C++
liteav::ITRTCCloud* trtc_cloud = liteav::ITRTCCloud::getTRTCShareInstance();
trtc_cloud->enableCustomVideoCapture(TRTCVideoStreamType::TRTCVideoStreamTypeBig, true);
:::
</dx-codeblock>


### 发送自定义视频帧

然后您就可以使用 TRTCCloud 的 `sendCustomVideoData` 接口向 TRTC SDK 发送您自己的视频数据，示例代码如下：

>? 为了避免不必要的性能损失，对于输入 TRTC SDK 的视频数据，在不同平台上有不同的格式要求，更多信息，详见我们的 API 文档：[简体中文 ](https://liteav.sdk.qcloud.com/doc/api/zh-cn/index.html)、[English](https://liteav.sdk.qcloud.com/doc/api/en/md_introduction_trtc_en_TRTCSDK_Download.html)；


<dx-codeblock>
::: Android  Java
// Android 平台有 Buffer 和 Texture 两种方案，此处以 Texture 方案为例，推荐！
TRTCCloudDef.TRTCVideoFrame videoFrame = new TRTCCloudDef.TRTCVideoFrame();
videoFrame.texture = new TRTCCloudDef.TRTCTexture();
videoFrame.texture.textureId = textureId;
videoFrame.texture.eglContext14 = eglContext;
videoFrame.width = width;
videoFrame.height = height;
videoFrame.timestamp = timestamp;
videoFrame.pixelFormat = TRTCCloudDef.TRTC_VIDEO_PIXEL_FORMAT_Texture_2D;
videoFrame.bufferType = TRTCCloudDef.TRTC_VIDEO_BUFFER_TYPE_TEXTURE;
mTRTCCloud.sendCustomVideoData(TRTCCloudDef.TRTC_VIDEO_STREAM_TYPE_BIG, videoFrame);
:::
::: iOS&Mac  ObjC
// 在 iOS/Mac 平台上，摄像头原生采集的视频格式即是 NV12，原生支持且性能最佳的视频帧格式是CVPixelBufferRef，同时支持I420、OpenGL 2D纹理格式。此处以CVPixelBufferRef为例，推荐！
TRTCVideoFrame *videoFrame = [[TRTCVideoFrame alloc] init];
videoFrame.pixelFormat = TRTCVideoPixelFormat_NV12;
videoFrame.bufferType = TRTCVideoBufferType_PixelBuffer;
videoFrame.pixelBuffer = imageBuffer;
videoFrame.timestamp = timeStamp;
        
[[TRTCCloud sharedInstance] sendCustomVideoData:TRTCVideoStreamTypeBig frame:videoFrame];   
:::
::: Windows  C++
// Windows 平台目前只支持 Buffer 的方案，推荐以此方式实现功能。
liteav::TRTCVideoFrame frame;
frame.timestamp = getTRTCShareInstance()->generateCustomPTS();
frame.videoFormat = liteav::TRTCVideoPixelFormat_I420;
frame.bufferType = liteav::TRTCVideoBufferType_Buffer;
frame.length = buffer_size;
frame.data = array.data();
frame.width = YUV_WIDTH;
frame.height = YUV_HEIGHT;
getTRTCShareInstance()->sendCustomVideoData(&frame);

:::
</dx-codeblock>





## 自定义视频渲染

自定义渲染主要分为：本地预览画面的渲染、和远端用户画面的渲染，基本原理：设置本地/远端的自定义渲染回调，然后 TRTC SDK 会通过回调函数`onRenderVideoFrame`中传递出来对应的视频帧（即TRTCVideoFrame），然后就开发者可以根据收到的视频帧进行自定义渲染了，这个流程需要具备一定的OpenGL 基础，我们也提供有对应平台的的API-Example：

- [Android](https://github.com/LiteAVSDK/TRTC_Android/blob/main/TRTC-API-Example/Advanced/LocalVideoShare/src/main/java/com/tencent/trtc/mediashare/LocalVideoShareActivity.java)：
- [iOS](https://github.com/LiteAVSDK/TRTC_iOS/blob/aa3026c07baeda553aec491702382683d5486a32/TRTC-API-Example-Swift/CustomCapture/testCustomVideo/TestRenderVideoFrame.m)
- [Windows](https://github.com/LiteAVSDK/TRTC_Windows/blob/main/TRTC-API-Example-C++/TRTC-API-Example-Qt/src/TestCustomCapture/test_custom_capture.cpp) 


### 设置本地预览画面的渲染回调
<dx-codeblock>
::: Android  Java
mTRTCCloud.setLocalVideoRenderListener(TRTCCloudDef.TRTC_VIDEO_PIXEL_FORMAT_Texture_2D, TRTCCloudDef.TRTC_VIDEO_BUFFER_TYPE_TEXTURE, new TRTCCloudListener.TRTCVideoRenderListener() {
    @Override
    public void onRenderVideoFrame(String suserId int streamType, TRTCCloudDef.TRTCVideoFrame frame) {
        // 详见TRTC-API-Example 中自定义渲染的工具类：com.tencent.trtc.mediashare.helper.CustomFrameRender  
    }
});
:::
::: iOS&Mac ObjC
self.trtcCloud = [TRTCCloud sharedInstance];
[self.trtcCloud setLocalVideoRenderDelegate:self pixelFormat:TRTCVideoPixelFormat_NV12 bufferType:TRTCVideoBufferType_PixelBuffer];
:::
::: Windows C++
```
// 具体实现请参考 TRTC-API-Example-Qt 中 test_custom_render.cpp 的实现。
void TestCustomRender::onRenderVideoFrame(
    const char* userId,
    liteav::TRTCVideoStreamType streamType,
    liteav::TRTCVideoFrame* frame) {
  if (gl_yuv_widget_ == nullptr) {
    return;
  }

  if (streamType == liteav::TRTCVideoStreamType::TRTCVideoStreamTypeBig) {
    // 调整渲染窗口
    emit renderViewSize(frame->width, frame->height);
    // 绘制视频帧
    gl_yuv_widget_->slotShowYuv(reinterpret_cast<uchar*>(frame->data),
                                frame->width, frame->height);
  }
}
```
:::
</dx-codeblock>


### 设置远端用户画面的渲染回调
<dx-codeblock>
::: Android  Java
mTRTCCloud.setRemoteVideoRenderListener(userId, TRTCCloudDef.TRTC_VIDEO_PIXEL_FORMAT_I420, TRTCCloudDef.TRTC_VIDEO_BUFFER_TYPE_BYTE_ARRAY, new TRTCCloudListener.TRTCVideoRenderListener() {
    @Override
    public void onRenderVideoFrame(String userId, int streamType, TRTCCloudDef.TRTCVideoFrame frame) {
         // 详见TRTC-API-Example 中自定义渲染的工具类：com.tencent.trtc.mediashare.helper.CustomFrameRender  
    }
});
:::
::: iOS&Mac ObjC
- (void)onRenderVideoFrame:(TRTCVideoFrame *)frame 
                    userId:(NSString *)userId 
                streamType:(TRTCVideoStreamType)streamType
{
    //userId是nil时为本地画面，否则为远端画面
    CFRetain(frame.pixelBuffer);
    __weak __typeof(self) weakSelf = self;
    dispatch_async(dispatch_get_main_queue(), ^{
        TestRenderVideoFrame *strongSelf = weakSelf;
        UIImageView* videoView = nil;
        if (userId) {
            videoView = [strongSelf.userVideoViews objectForKey:userId];
        }
        else {
            videoView = strongSelf.localVideoView;
        }
        videoView.image = [UIImage imageWithCIImage:[CIImage imageWithCVImageBuffer:frame.pixelBuffer]];
        videoView.contentMode = UIViewContentModeScaleAspectFit;
        CFRelease(frame.pixelBuffer);
    });
}
:::
::: Windows C++
```
// 具体实现请参考 TRTC-API-Example-Qt 中 test_custom_render.cpp 的实现。
void TestCustomRender::onRenderVideoFrame(
    const char* userId,
    liteav::TRTCVideoStreamType streamType,
    liteav::TRTCVideoFrame* frame) {
  if (gl_yuv_widget_ == nullptr) {
    return;
  }

  if (streamType == liteav::TRTCVideoStreamType::TRTCVideoStreamTypeBig) {
    // 调整渲染窗口
    emit renderViewSize(frame->width, frame->height);
    // 绘制视频帧
    gl_yuv_widget_->slotShowYuv(reinterpret_cast<uchar*>(frame->data),
                                frame->width, frame->height);
  }
}
```
:::
</dx-codeblock>
