

#自定义音视频输入流
##自定义音频数据

音频本地处理流程图:

> 观众侧
![](https://zhaoyang21cn.github.io/ilivesdk_help/readme_img/audio_member.jpg)

> 主播侧
![](https://zhaoyang21cn.github.io/ilivesdk_help/readme_img/audio_host.jpg)

如上图所示，用户可以其中任意环节对数据进行拦截并作相应的处理。

这里以混音为例:

### Android

1、注册回调

接口名|接口描述
:--|:--:
registAudioDataCallbackWithByteBuffer|注册具体数据类型的回调函数

参数类型|说明
:--|:--:
int|音频数据类型(参考上图)
RegistAudioDataCompleteCallbackWithByteBuffer|指向App定义的音频数据回调函数

```java
ILiveSDK.getInstance().getAvAudioCtrl().registAudioDataCallbackWithByteBuffer(
    AVAudioCtrl.AudioDataSourceType.AUDIO_DATA_SOURCE_MIXTOSEND, mAudioDataCompleteCallbackWithByffer);
```

2、添加需要混入的音频数据

```java
private AVAudioCtrl.RegistAudioDataCompleteCallbackWithByteBuffer mAudioDataCompleteCallbackWithByffer = 
      new AVAudioCtrl.RegistAudioDataCompleteCallbackWithByteBuffer() {
        @Override
        public int onComplete(AVAudioCtrl.AudioFrameWithByteBuffer audioFrameWithByteBuffer, int srcType) {
            if (srcType==AudioDataSourceType.AUDIO_DATA_SOURCE_MIXTOSEND) {
                synchronized (obj){
                  /*************************************************
                    将要混入的音频数据写入audioFrameWithByteBuffer中
                  *************************************************/
                }
            }
            return AVError.AV_OK;
        }
    };
```

### iOS

**音频透传**，主要用于在直播中对Mic采集到的数据作再加工处理，一般用于在直播间内添加背景音等，其对透传的音频数据有格式要求，默认使用的音频格式为QAVAudioFrameDesc = {48000, 2, 16}。通常的有下面两种使用方法：<br>
1､ 麦克风透传：开麦克风端（有上行音频能力端）能听到，其他人可听到：以下代码为设置麦克风透传

```
// 设置音频处理回调
[[[ILiveSDK getInstance] getAVContext].audioCtrl setAudioDataEventDelegate:self];

// 注意为QAVAudioDataSource_MixToSend
[[[ILiveSDK getInstance] getAVContext].audioCtrl registerAudioDataCallback:QAVAudioDataSource_MixToSend];
[[[ILiveSDK getInstance] getAVContext].audioCtrl setAudioDataFormat:QAVAudioDataSource_MixToSend desc:pcmdesc];

```

2､ 扬声器透传数据：开扬声器端配置，只有自己听到，其他人听不到：以下代码为设置扬声器透传

```
 // 设置音频处理回调
 [[[ILiveSDK getInstance] getAVContext].audioCtrl setAudioDataEventDelegate:self];
 
 // 注意为QAVAudioDataSource_MixToPlay
 [[[ILiveSDK getInstance] getAVContext].audioCtrl registerAudioDataCallback:QAVAudioDataSource_MixToPlay];
 [[[ILiveSDK getInstance] getAVContext].audioCtrl setAudioDataFormat:QAVAudioDataSource_MixToPlay desc:pcmdesc];

```

3､ 音频透传处理的回调回调处理：注意三个回调中的注释

```
- (QAVResult)audioDataComes:(QAVAudioFrame *)audioFrame type:(QAVAudioDataSourceType)type
{
    // 主要用于保存直播中的音频数据
    return QAV_OK;
}

- (void)handle:(QAVAudioFrame **)frameRef withPCM:(NSData *)data offset:(NSInteger *)offset
{
	// 演示如何将透传的数据添加到QAVAudioFrame
    const QAVAudioFrame *aFrame = *frameRef;
    NSInteger off = *offset;
    NSInteger length = [aFrame.buffer length];
    if (length)
    {
        NSMutableData *pdata = [NSMutableData data];
        const Byte *btyes = [data bytes];
        
        while (pdata.length < length)
        {
            if (off + length > data.length)
            {
                const Byte *byteOff = btyes + off;
                [pdata appendBytes:byteOff length:data.length - off];
                off = 0;
            }
            else
            {
                const Byte *byteOff = btyes + off;
                [pdata appendBytes:byteOff length:length];
                off += length;
            }
        }
        
        if (pdata.length == length)
        {
            *offset = off;
            
            const void *abbytes = [aFrame.buffer bytes];
            memcpy((void *)abbytes, [pdata bytes], length);
        }
    }
}

- (QAVResult)audioDataShouInput:(QAVAudioFrame *)audioFrame type:(QAVAudioDataSourceType)type
{
    // 混音输入（Mic和Speaker）的主要回调
    
    // 麦克风透传处理
    if (type == QAVAudioDataSource_MixToSend)
    {
    	// self.micAudioTransmissionData 为要透传的音频数据，默认使用QAVAudioFrameDesc = {48000, 2, 16}，外部传入数据时，注意对应，外部传入的时候，注意相关的参数
        if (self.micAudioTransmissionData)
        {
            NSInteger off = self.micAudioOffset;
            [self handle:&audioFrame withPCM:self.micAudioTransmissionData offset:&off];
            self.micAudioOffset = off;
        }
    }
    // 扬声明器透传处理
    else if (type == QAVAudioDataSource_MixToPlay)
    {
    // self.speakerAudioTransmissionData 为要透传的音频数据，默认同样使用QAVAudioFrameDesc = {48000, 2, 16}，外部传入数据时，注意对应，外部传入的时候，注意相关的参数
        if (self.speakerAudioTransmissionData)
        {
            NSInteger off = self.speakerAudioOffset;
            [self handle:&audioFrame withPCM:self.speakerAudioTransmissionData offset:&off];
            self.speakerAudioOffset = off;
        }
    }
//    NSLog(@"%@", audioFrame.buffer);
    return QAV_OK;
}

- (QAVResult)audioDataDispose:(QAVAudioFrame *)audioFrame type:(QAVAudioDataSourceType)type
{
    // 主要用作作变声处理
    return QAV_OK;
}
```

4､ 退出直播间时，取消透传回调

```

// 取消所有音频透传处理
[[[ILiveSDK getInstance] getAVContext].audioCtrl unregisterAudioDataCallbackAll];
[[[ILiveSDK getInstance] getAVContext].audioCtrl setAudioDataEventDelegate:nil];

// 或调用AVSDK接口取消不同类型的透传
// 方法详见QAVSDK.framework中的QAVAudioCtrl
/*!
 @abstract      反注册音频数据类型的回调
 @discussion    要注册监听的音频数据源类型，具体参考QAVAudioDataSourceType。
 @param         type            要反注册监听的音频数据源类型，具体参考QAVAudioDataSourceType
 @return        成功返回QAV_OK, 其他情况请参照QAVResult。
 @see           QAVAudioDataSourceType QAVResult
 */
- (QAVResult)unregisterAudioDataCallback:(QAVAudioDataSourceType)type;

        
```









##自定义视频数据

自定义视频数据流程图:

![](https://zhaoyang21cn.github.io/ilivesdk_help/readme_img/custom_flow.png)

### Android

1、打开摄像头，同时需要调用enableExternalCapture做一些准备

接口名|接口描述
:--|:--:
enableExternalCapture|开启/关闭外部视频捕获设备

参数类型|说明
:--|:--:
boolean|true表示开启,false表示关闭
EnableExternalCaptureCompleteCallback|指向App定义的回调函数

```java
ILiveSDK.getInstance().getAvVideoCtrl().enableExternalCapture(false, 
       new AVVideoCtrl.EnableExternalCaptureCompleteCallback(){
                @Override
                protected void onComplete(boolean enable, int result) {
                    super.onComplete(enable, result);
                }
            });
```

2、获取原始视频数据，加工处理

3、上传视频数据

接口名|接口描述
:--|:--:
fillExternalCaptureFrame|输入从外部视频捕获设备获取的视频图像到SDK

参数类型|说明
:--|:--:
byte数组|图像数据
int|图像数据长度
int|图像宽度
int|图像高度
int|图像渲染角度。角度可以是0,90,180,270
int|图像颜色格式。当前仅支持COLOR_FORMAT_I420
int|视频源类型。当前仅支持VIDEO_SRC_TYPE_CAMERA

```java
// 图像需要旋转90度
ILiveSDK.getInstance().getAvVideoCtrl().fillExternalCaptureFrame(data, data.length,
    mCameraSize.width, mCameraSize.height, 270, AVVideoCtrl.COLOR_FORMAT_I420, AVView.VIDEO_SRC_TYPE_CAMERA);
```
 -----
### iOS
自定义采集画面的用途主要用于预处理原始数据，比如用户需要人脸识别，画面美化，动效处理等，如下是通过自定义采集画面后，增加动效效果图，示例图：

![](http://mc.qcloudimg.com/static/img/f532b2ba735514ed2faff41cf805a817/image.png)

**注：动效效果是用户自己增加的，和本文档无关，用户可以对原始数据做任何预处理（不仅是动效）**

1、流程说明
首先请记住，若要使用自定义采集画面，则采集画面的过程与ILiveSDK没有任何关系，完全不依赖ILiveSDK，自定义采集画面的流程中，ILiveSDK的作用是透传数据以及渲染远程数据。而本文介绍的流程是：***自定义采集画面－>画面传入ILiveSDK－>远程端收到画面帧渲染*** 的整个过程，流程图如下：
![](http://mc.qcloudimg.com/static/img/5311e0e74ef71db124c291be01f8b5da/image.png)


2、采集前准备
***进入房间之后，采集画面之前***

|接口|描述|
|---|---|
|enableExternalCapture:|打开(关闭)外部视频捕获设备,自定义采集时，需要打开.返回QAV_OK表示执行成功。用了此方法之后，***不能***再调用ILiveSDK的打开摄像头接口，且ILiveSDK的美白，美颜将失效|

|参数类型|参数名|说明|
|---|---|---|
|BOOL|isEnableExternalCapture|是否打开外部视频捕获设备，自定义采集时传YES|

* 示例：

```
    QAVVideoCtrl *videoCtrl = [[ILiveSDK getInstance] getAvVideoCtrl].videoCtrl;
    [videoCtrl enableExternalCapture:YES];
```

3、自定义采集
自定义采集使用的是系统层级接口，和ILiveSDK没有直接联系，不做过多赘述，简单列下需要用到的系统类和方法

|系统类或方法|描述|
|---|---|
|AVCaptureSession|采集画面|
|AVCaptureDeviceInput|画面输入流|
|AVCaptureVideoDataOutput|画面输出流|
|captureOutput: didOutputSampleBuffer: fromConnection:|采集画面回调函数，采集到的画面将从这里回吐，用户可在这个接口作预处理|

4、采集后处理
接收到系统回吐出的原始数据（`CMSampleBufferRef`类型数据），用户就可以对其做预处理，比如美白，美颜，人脸识别等，预处理之后的画面需要用户自己完成渲染，与ILiveSDK无直接联系。

5、ILiveSDK透传

|接口|描述|
|---|---|
|fillExternalCaptureFrame:|向音视频SDK传入捕获的视频帧，返回QAV_OK表示执行成功|

|参数类型|参数名|说明|
|---|---|---|
|QAVVideoFrame|frame|AVSDK画面帧类型，用户需将自定义采集的画面转换成QAVVideoFrame类型|
*示例：

```
    QAVVideoCtrl *videoCtrl = [[ILiveSDK getInstance] getAvVideoCtrl].videoCtrl;
    QAVResult result = [videoCtrl fillExternalCaptureFrame:frame];
```

6、远端渲染

|接口|描述|
|---|---|
|OnVideoPreview:|远程画面回调，接收远程帧数据，再使用ILiveSDK的渲染接口渲染，用户只需要添加一个渲染区域即可。渲染详情请参考[新版随心播](https://github.com/zhaoyang21cn/ILiveSDK_iOS_Demos/tree/master/TILLiveSDKShow)|

|参数类型|参数名|说明|
|---|---|---|
|QAVVideoFrame|frameData|AVSDK画面帧类型|

7、注意事项
> *1 如果渲染自定义采集的画面使用了OpenGL，则不能使用ILiveSDK中的渲染，否则会Crash。也就是说，此时界面上应该有两个view，一个渲染自定义采集的画面，另一个渲染QAVVideoFrame对象。

> *2 转换成QAVVideoFrame时，属性color_format必需填写AVCOLOR_FORMAT_NV12
srcType属性必须填写QAVVIDEO_SRC_TYPE_CAMERA
