本课程讲解自定采集视频数据相关问题

## 效果图

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。 点击[下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/Demo_CustomVideo.zip)
## 相关概念

本课程中使用系统组件，自定义采集摄像头视频，并渲染到AVCaptureVideoPreviewLayer中，自定义采集的类封装到一个单独的类CameraManager中，如果用户对系统组件不熟悉，可以不用理解这个类。用户应该有自己的采集画面的类，而本课程主要讲解从开始采集数据，到把数据传输出去的整个流程。

## 流程图

![](https://main.qcloudimg.com/raw/0cca183352be2824682136be4d86be9f.png)

## 具体实现

### 流程说明
首先请记住，若要使用自定义采集画面，则采集画面的过程与ILiveSDK没有任何关系，完全不依赖ILiveSDK，自定义采集画面的流程中，ILiveSDK的作用是透传数据以及渲染远程数据。而本文介绍的流程是：***自定义采集画面－>画面传入ILiveSDK－>远程端收到画面帧渲染*** 的整个过程

### 采集前准备
***进入房间之后，采集画面之前***

|接口|描述|
|---|---|
|enableExternalCapture:shouldRender:|打开(关闭)外部视频捕获设备,自定义采集时，需要打开.返回QAV_OK表示执行成功。用了此方法之后，**不能**再调用ILiveSDK的打开摄像头接口，且ILiveSDK的美白，美颜将失效|

|参数类型|参数名|说明|
|---|---|---|
|BOOL|isEnableExternalCapture|是否打开外部视频捕获设备，自定义采集时传YES|
|BOOL|shouldRender|SDK是否渲染输入流视频数据，YES表示会，NO表示不会|

```
[[[ILiveSDK getInstance] getAVContext].videoCtrl enableExternalCapture:YES shouldRender:NO];
```

### 自定义采集
自定义采集使用的是系统层级接口，和ILiveSDK没有直接联系，不做过多赘述(用户应该有自己的采集模块)，简单列下Demo中需要用到的系统类和方法

|系统类或方法|描述|
|---|---|
|AVCaptureSession|采集画面|
|AVCaptureDeviceInput|画面输入流|
|AVCaptureVideoDataOutput|画面输出流|
|captureOutput: didOutputSampleBuffer: fromConnection:|采集画面回调函数，采集到的画面将从这里回吐，用户可在这个接口作预处理|

### 采集后处理
接收到系统回吐出的原始数据（`CMSampleBufferRef`类型数据），用户就可以对其做预处理，例如美白，美颜，人脸识别等，预处理之后的画面需要用户自己完成渲染，与ILiveSDK无直接联系，ILiveSDK提供接口，可将 `CMSampleBufferRef` 转换为 SDK所需的QAVFrame类型，再将QAVFrame类型传入SDK中，SDK完成数据传输

```
//ilivesdk提供接口，将CMSampleBufferRef转为QAVVideoFrame对象
    ILiveFrameDispatcher *dispatch = [[ILiveRoomManager getInstance] getFrameDispatcher];
    QAVVideoFrame *frame = [dispatch getVideoFrameFromSampleBuffer:sampleBuffer];

    //将QAVVideoFrame传入SDK
    [[[ILiveSDK getInstance] getAVContext].videoCtrl fillExternalCaptureFrame:frame];
```

### 观众端观看
观众端观看与普通进房无任何区别，请参见基础教程或本Demo中的JoinViewController类。在本Demo中，用主播端登录自定义采集，观众端登录观看自定义采集的画面

## 常见问题
* 1 如果渲染自定义采集的画面使用了OpenGL，则不能使用ILiveSDK中的渲染，否则会Crash。也就是说，此时界面上应该有两个view，一个渲染自定义采集的画面，另一个渲染QAVVideoFrame对象。

* 2 如果有其它自定义采集数据格式，推荐使用[libyuv库](https://github.com/asynnestvedt/libyuv-ios)进行转换，再构造QAVVideoFrame结构。

## 联系邮箱
如果对上述文档有不明白的地方，请反馈到trtcfb@qq.com
