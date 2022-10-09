本文档主要介绍如何使用 TRTC SDK 实现自定义音频采集和获取，分为：音频采集、音频获取两个部分。

## 自定义音频采集

TRTC SDK 的自定义音频采集功能的开启分为两步，即：开启功能、发送音频帧给 SDK，具体 API 使用步骤见下文，同时我们也提供有对应平台的的 API-Example：

- [Android](https://github.com/LiteAVSDK/TRTC_Android/blob/main/TRTC-API-Example/Advanced/LocalVideoShare/src/main/java/com/tencent/trtc/mediashare/LocalVideoShareActivity.java)
- [iOS](https://github.com/LiteAVSDK/TRTC_iOS/blob/main/TRTC-API-Example-OC/Advanced/LocalVideoShare/LocalVideoShareViewController.m)
- [Windows](https://github.com/LiteAVSDK/TRTC_Windows/blob/main/TRTC-API-Example-C++/TRTC-API-Example-Qt/src/TestCustomCapture/test_custom_capture.cpp) 

### 开启自定义音频采集功能

首先，您需要调用 TRTCCloud 的 `enableCustomAudioCapture` 接口开启  TRTC SDK 自定义音频采集的功能，示例代码如下：

<dx-codeblock>
::: Android  Java
TRTCCloud mTRTCCloud = TRTCCloud.shareInstance();
mTRTCCloud.enableCustomAudioCapture(true);
:::
::: iOS&Mac  ObjC
self.trtcCloud = [TRTCCloud sharedInstance];
[self.trtcCloud enableCustomAudioCapture:YES];
:::
::: Windows  C++
liteav::ITRTCCloud* trtc_cloud = liteav::ITRTCCloud::getTRTCShareInstance();
trtc_cloud->enableCustomAudioCapture(true);
:::
</dx-codeblock>


### 发送自定义音频帧

然后您就可以使用 TRTCCloud 的 `sendCustomAudioData` 接口向 TRTC SDK 填充您自己的声音数据，示例代码如下：

<dx-codeblock>
::: Android  Java
TRTCCloudDef.TRTCAudioFrame trtcAudioFrame = new TRTCCloudDef.TRTCAudioFrame();
trtcAudioFrame.data = data;
trtcAudioFrame.sampleRate = sampleRate;
trtcAudioFrame.channel = channel;
trtcAudioFrame.timestamp = timestamp;
mTRTCCloud.sendCustomAudioData(trtcAudioFrame);
:::
::: iOS&Mac  ObjC
TRTCAudioFrame *audioFrame = [[TRTCAudioFrame alloc] init];
audioFrame.channels = audioChannels;
audioFrame.sampleRate = audioSampleRate;
audioFrame.data = pcmData;
    
[self.trtcCloud sendCustomAudioData:audioFrame];
:::
::: Windows  C++
liteav::TRTCAudioFrame frame;
frame.audioFormat = liteav::TRTCAudioFrameFormatPCM;
frame.length = buffer_size;
frame.data = array.data();
frame.sampleRate = 48000;
frame.channel = 1;
getTRTCShareInstance()->sendCustomAudioData(&frame);
:::
</dx-codeblock>

>! 使用 `sendCustomAudioData` 有可能会导致回声抵消（AEC）的功能失效。




## 获取音频原数据

声音模块是一个高复杂度的模块，SDK 需要严格控制声音设备的采集和播放逻辑。在某些场景下，当您需要获取远程用户的音频数据或者需要获取本地麦克风采集到的音频数据时，可以通过 TRTCCloud 对应的不同平台的接口，我们也提供有对应平台的的 API-Example：

- [Android](https://github.com/LiteAVSDK/TRTC_Android/blob/main/TRTC-API-Example/Advanced/LocalVideoShare/src/main/java/com/tencent/trtc/mediashare/LocalVideoShareActivity.java)：
- [iOS](https://github.com/LiteAVSDK/TRTC_iOS/blob/main/TRTC-API-Example-OC/Advanced/LocalVideoShare/LocalVideoShareViewController.m)
- [Windows](https://github.com/LiteAVSDK/TRTC_Windows) 


### 设置音频回调函数
<dx-codeblock>
::: Android  Java
mTRTCCloud.setAudioFrameListener(new TRTCCloudListener.TRTCAudioFrameListener() {
        @Override
        public void onCapturedRawAudioFrame(TRTCCloudDef.TRTCAudioFrame trtcAudioFrame) {

        }
    
        @Override
        public void onLocalProcessedAudioFrame(TRTCCloudDef.TRTCAudioFrame trtcAudioFrame) {
    
        }
    
        @Override
        public void onRemoteUserAudioFrame(TRTCCloudDef.TRTCAudioFrame trtcAudioFrame, String s) {
    
        }
    
        @Override
        public void onMixedPlayAudioFrame(TRTCCloudDef.TRTCAudioFrame trtcAudioFrame) {
    
        }
    
        @Override
        public void onMixedAllAudioFrame(TRTCCloudDef.TRTCAudioFrame trtcAudioFrame) {
            // 详见TRTC-API-Example 中自定义渲染的工具类：com.tencent.trtc.mediashare.helper.CustomFrameRender  
        }
    }); 
:::
::: iOS&Mac ObjC
 [self.trtcCloud setAudioFrameDelegate:self];
 // MARK: - TRTCAudioFrameDelegate
 - (void)onCapturedRawAudioFrame:(TRTCAudioFrame *)frame {
        NSLog(@"onCapturedRawAudioFrame");
}
 
- (void)onLocalProcessedAudioFrame:(TRTCAudioFrame *)frame {
        NSLog(@"onLocalProcessedAudioFrame");
}

- (void)onRemoteUserAudioFrame:(TRTCAudioFrame *)frame userId:(NSString *)userId {
        NSLog(@"onRemoteUserAudioFrame");
}
 
- (void)onMixedPlayAudioFrame:(TRTCAudioFrame *)frame {
        NSLog(@"onMixedPlayAudioFrame");
}

- (void)onMixedAllAudioFrame:(TRTCAudioFrame *)frame {
        NSLog(@"onMixedAllAudioFrame");
}
:::
::: Windows C++
// 设置音频数据自定义回调
liteav::ITRTCCloud* trtc_cloud = liteav::ITRTCCloud::getTRTCShareInstance();
trtc_cloud->setAudioFrameCallback(callback)

// 音频数据自定义回调

virtual void onCapturedRawAudioFrame(TRTCAudioFrame* frame) {
}

virtual void onLocalProcessedAudioFrame(TRTCAudioFrame* frame) {
}

virtual void onPlayAudioFrame(TRTCAudioFrame* frame, const char* userId) {
}

virtual void onMixedPlayAudioFrame(TRTCAudioFrame* frame) {
}
:::
</dx-codeblock>

>!
- 不要在上述回调函数中做任何耗时操作，建议直接拷贝，并通过另一线程进行处理，否则会导致声音断断续续或者回声抵消（AEC）失效的问题。
- 上述回调函数中回调出来的数据都只允许读取和拷贝，不能修改，否则会导致各种不确定的后果。
