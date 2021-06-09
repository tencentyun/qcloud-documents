## 适用场景
实时音视频 TRTC 支持接入第三方美颜特效 SDK，目前 TRTC 已与多家美颜特效 SDK 供应商紧密合作，为您在多个场景提供接入便捷、性能卓越的“TRTC+美颜特效”解决方案。

结合 TRTC 低延时、高质量、高稳定的视频通信能力和美颜、美妆、美体、AR特效、虚拟背景等美颜特效能力可以触达秀场直播、视频相亲、互动课堂、视频会议、互动游戏等业务场景，快速构建具备美颜特效能力的实时音视频应用。

>? 若您想要购买或试用**“TRTC + 美颜特效”**解决方案，请发送邮件至 ` tengxunrtc@tencent.com `。

## 原理解析
从 TRTC 8.1 版本开始，TRTC SDK 提供了新的接口 [setLocalVideoProcessListener](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a0b565dc8c77df7fb826f0c45d8ad2d85)，TRTC SDK 会在编码和渲染之前，将 TRTC SDK 采集到的图像通过该接口回调出来。您可以使用该接口，对回调出来的图像进行二次处理（例如：使用第三方美颜 SDK 进行美颜处理），并将处理后的图像通过参数传递给 TRTC SDK，TRTC SDK 后续渲染和编码都将使用二次处理后的图像。
![](https://main.qcloudimg.com/raw/5bf10ca44b2e5905c934d9ea86226283.png)


## 操作步骤

[](id:step1)
### 步骤1：集成 TRTC
您可采用**自动加载 aar** 和**手动下载 aar** 的方式集成 TRTC。具体集成操作请参见 [快速集成TRTC](https://cloud.tencent.com/document/product/647/32175)。

[](id:step2)
### 步骤2：集成美颜特效 SDK
参考您所对接的第三方特效产品集成文档，集成美颜特效 SDK。

以相芯美颜特效 SDK 为例，具体集成方法请参见 [快速集成 NAMA SDK](https://www.faceunity.com/developer-center.html)。

[](id:step3)
### 步骤3：初始化美颜特效 SDK
由于 SDK 和大部分特效产品内部都使用 OpenGL 来处理图像，因此使用 TEXTURE_2D 作为两个 SDK 对接格式，性能会最好。
以相芯为例：可以在初始化 `FURenderer` 时指定输入格式：
<dx-codeblock>
::: iOS  Objective-C 
// 初始化并对 SDK 进行授权
[[FURenderer shareRenderer] setupWithData:bundleData
                                 dataSize:bundleDataSize
                                   ardata:NULL
                              authPackage:secretKey
                                 authSize:secretKeySize];
:::
::: Android java
FURenderer mFURenderer = new FURenderer.Builder(this)
    .setInputTextureType(FURenderer.INPUT_TEXTURE_2D) // 指定输入格式为 TEXTURE_2D
    .setCameraFacing(cameraFacing)
    .setInputImageOrientation(CameraUtils.getCameraOrientation(cameraFacing))
    .build();
:::
</dx-codeblock>  

[](id:step4)
### 步骤4：设置自定义预处理回调
通过调用 `TRTCCloud` 中的 [setLocalVideoProcessDelegate ](http://doc.qcloudtrtc.com/group__TRTCCloud__ios.html#a2f73c33b1010a63bd3a06e639b3cf348) 或 [setLocalVideoProcessListener](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a0b565dc8c77df7fb826f0c45d8ad2d85) 来设置自定义美颜的回调，并指定回调的格式为 TEXTURE_2D：
<dx-codeblock>
::: iOS  Objective-C 
[[TRTCCloud sharedInstance] setLocalVideoProcessDelegete:self
                                             pixelFormat:TRTCVideoPixelFormat_NV12
                                              bufferType:TRTCVideoBufferType_PixelBuffer];
:::
::: Android java
mTRTCCloud.setLocalVideoProcessListener(TRTCCloudDef.TRTC_VIDEO_PIXEL_FORMAT_Texture_2D,
                    TRTCCloudDef.TRTC_VIDEO_BUFFER_TYPE_TEXTURE, mVideoFrameListener);
:::
</dx-codeblock>

[](id:step5)
### 步骤5：调用美颜特效 SDK 接口
自定义预处理回调接口的定义如下：
<dx-codeblock>
::: iOS  Objective-C 
@protocol TRTCVideoFrameDelegate <NSObject>
@optional

- (uint32_t)onProcessVideoFrame:(TRTCVideoFrame * _Nonnull)srcFrame
      dstFrame:(TRTCVideoFrame * _Nonnull)dstFrame;
- (void)onGLContextDestory;
  @end
  :::
  ::: Android java
  public interface TRTCVideoFrameListener {
    void onGLContextCreated();
    int onProcessVideoFrame(TRTCCloudDef.TRTCVideoFrame srcFrame, 
  	    TRTCCloudDef.TRTCVideoFrame dstFrame);
    void onGLContextDestory();
  }
  :::
</dx-codeblock>

|      接口      |      说明      |
| -------------------- | -------------------- |
| onGLContextCreated   | 在 TRTC SDK 创建 OpenGL 环境时回调，此时可以通知第三方美颜 SDK，以便它可以做一些自己的 OpenGL 资源初始化工作。 |
| onProcessVideoFrame  | 是每帧都会进行回调，其中 `srcFrame` 是 SDK 采集到的图像数据，`dstFrame` 是用来存放二次处理后的图像。回调出来时，`dstFrame` 已经分配好用来存储图像的对象（`dstFrame.texture`、`dstFrame.data`、`dstFrame.buffer`），您可以直接使用。您也可以自己分配内存，并将 `dstFrame` 中对应字段修改为您自己分配的对象。 |
| onGLContextDestory | 在 TRTC SDK 销毁 OpenGL 环境时回调，此时可以通知第三方美颜 SDK，以便它可以做一些自己的 OpenGL 资源清理工作。 |

#### 相芯接入示例
为了帮助您更好地理解和运用自定义预处理来对接第三方美颜特效 SDK，我们以相芯为例向您展示接入示例代码：
<dx-codeblock>
::: iOS  Objective-C 

- (uint32_t)onProcessVideoFrame:(TRTCVideoFrame * _Nonnull)srcFrame
      dstFrame:(TRTCVideoFrame * _Nonnull)dstFrame {
  self.frameID += 1;
  dstFrame.pixelBuffer = [[FURenderer shareRenderer] renderPixelBuffer:srcFrame.pixelBuffer
                                                           withFrameId:self.frameID
                                                                 items:self.renderItems
                                                             itemCount:self.renderItems.count];
  return 0;
  }
  :::
  ::: Android java
  private final TRTCVideoFrameListener mVideoFrameListener = new TRTCVideoFrameListener() {
  @Override
  public void onGLContextCreated() {
      // OpenGL环境创建时，需要调用相芯的onSurfaceCreated，以便其初始化OpenGL资源
      mFURenderer.onSurfaceCreated();
      mFURenderer.setUseTexAsync(true);
  }
  @Override
  public int onProcessVideoFrame(TRTCVideoFrame srcFrame, TRTCVideoFrame dstFrame) {
      // 相芯的处理接口会生成自己的纹理对象，因此通过修改 dstFrame 对应字段来将处理好后的纹理传给 TRTC SDK
      dstFrame.texture.textureId = mFURenderer.onDrawFrameSingleInput(srcFrame.texture.textureId, srcFrame.width, srcFrame.height);
      return 0;
  }
  @Override
  public void onGLContextDestory() {
      // OpenGL环境销毁时，需要调用相芯的onSurfaceDestroyed，用于销毁对应的OpenGL资源
      mFURenderer.onSurfaceDestroyed();
  }
  };
:::
</dx-codeblock>

[](id:note)
## 注意事项
- 相芯 SDK 7.2.0 版本存在兼容问题，需要更新到相芯 SDK 7.3.0 版本使用。
- 之前使用 [setLocalVideoRenderListener](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#aa3cbb7a501c3151d94473965e2538c7a) 来实现自定义预处理的客户，可以更换为新接口来实现同样的功能，新接口新增了 OpenGL 环境生命周期的回调。
