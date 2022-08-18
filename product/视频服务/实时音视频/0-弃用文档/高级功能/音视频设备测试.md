## 内容介绍

在进行视频通话之前，建议先进行摄像头和麦克风等设备的测试，否则等用户真正进行通话时很难发现设备问题。

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/fced7778482de4edfbe94bfcf8ec5f20.jpg" />

   
## 支持此功能的平台

| iOS | Android | Mac OS | Windows | Electron|微信小程序 | Web 端|
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|     ×  |    ×    |    &#10003;   |    &#10003;    |&#10003;  |   ×    |  &#10003;（[Web 端](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-23-advanced-support-detection.html)）    |

## 测试摄像头

使用 TRTCCloud 的 `startCameraDeviceTestInView` 接口可以进行摄像头测试，在测试过程中可以通过调用 `setCurrentCameraDevice` 函数切换摄像头。

<dx-codeblock>
::: Mac平台 Objective-C
// 显示摄像头测试界面（支持预览摄像头，切换摄像头）
- (IBAction)startCameraTest:(id)sender {
    // 开始摄像头测试, cameraPreview为macOS下的NSView或者iOS平台的UIView
    [self.trtcCloud startCameraDeviceTestInView:self.cameraPreview];
}

//关闭摄像头测试界面
- (void)windowWillClose:(NSNotification *)notification{
    // 结束摄像头测试
    [self.trtcCloud stopCameraDeviceTest];
}
:::
::: Windows平台（C++） C++
// 启动摄像头测试。传入需要渲染视频的控件句柄。
void TRTCMainViewController::startTestCameraDevice(HWND hwnd) 
{
     trtcCloud->startCameraDeviceTest(hwnd);
}

// 关闭摄像头测试
void TRTCMainViewController::stopTestCameraDevice() 
{
     trtcCloud->stopCameraDeviceTest();
}
:::
::: Windows平台（C#） c#
// 启动摄像头测试。传入需要渲染视频的控件句柄。
private void startTestCameraDevice(Intptr hwnd) 
{
     mTRTCCloud.startCameraDeviceTest(hwnd);
}

// 关闭摄像头测试
private void stopTestCameraDevice() 
{
     mTRTCCloud.stopCameraDeviceTest();
}
:::
</dx-codeblock>

## 麦克风测试

使用 TRTCCloud 的 `startMicDeviceTest` 函数可以测试麦克风音量，回调函数会返回实时的麦克风音量值。

<dx-codeblock>
::: Mac平台 Objective-C
  // 麦克风测试示例代码
  -(IBAction)micTest:(id)sender {
    NSButton *btn = (NSButton *)sender;
    if (btn.state == 1) {
		    //开始麦克风测试
        __weak __typeof(self) wself = self;
        [self.trtcCloud startMicDeviceTest:500  testEcho:^(NSInteger volume) {
            dispatch_async(dispatch_get_main_queue(), ^{
						    // 刷新麦克风音量的进度条
                [wself _updateInputVolume:volume];
            });
        }];
        btn.title = @"停止测试";
    }
    else{
		    //结束麦克风测试
        [self.trtcCloud stopMicDeviceTest];
        [self _updateInputVolume:0];
        btn.title = @"开始测试";
    }
}
:::
::: Windows平台（C++） C++
// 麦克风测试示例代码
void TRTCMainViewController::startTestMicDevice() 
{
	// 设置音量回调频率，此处500ms回调一次，在 onTestMicVolume 回调接口监听。
	uint32_t interval = 500; 
	// 开始麦克风测试
	trtcCloud->startMicDeviceTest(interval);
}

// 结束麦克风测试
void TRTCMainViewController::stopTestMicDevice() 
{
     trtcCloud->stopMicDeviceTest();
}
:::
::: Windows平台（C#） c#
// 麦克风测试示例代码
private void startTestMicDevice() 
{
	// 设置音量回调频率，此处500ms回调一次，在 onTestMicVolume 回调接口监听。
	uint interval = 500; 
	// 开始麦克风测试
	mTRTCCloud.startMicDeviceTest(interval);
}

// 结束麦克风测试
private void stopTestMicDevice() 
{
     mTRTCCloud.stopMicDeviceTest();
}
:::
</dx-codeblock>



## 扬声器测试

使用 TRTCCloud 的 `startSpeakerDeviceTest` 函数会通过播放一段默认的 mp3 音频测试扬声器是否在正常工作。

<dx-codeblock>
::: Mac平台 Objective-C
// 扬声器测试示例代码
// 以作为 NSButton 的点击事件为例, 在 xib 中设置 Button 在 On 和 Off 下的标题分别为"结束测试"和"开始测试"
- (IBAction)speakerTest:(NSButton *)btn {
    NSString *path = [[NSBundle mainBundle] pathForResource:@"test-32000-mono" ofType:@"mp3"];
    if (btn.state == NSControlStateValueOn) {
        // 单击"开始测试"
        __weak __typeof(self) wself = self;
        [self.trtcEngine startSpeakerDeviceTest:path onVolumeChanged:^(NSInteger volume, BOOL playFinished) {
            // 以下涉及 UI 操作，需要切换到 main queue 中执行
            dispatch_async(dispatch_get_main_queue(), ^{
                // 这里 _updateOutputVolume 为更新界面中的扬声器音量指示器
                [wself _updateOutputVolume:volume];
                if (playFinished) {
                    // 播放完成时将按钮状态置为"开始测试"
                    sender.state = NSControlStateValueOff;
                }
            });
        }];
    } else {
        // 单击"结束测试"
        [self.trtcEngine stopSpeakerDeviceTest];
        [self _updateOutputVolume:0];
    }
}

// 更新扬声器音量指示器
- (void)_updateOutputVolume:(NSInteger)volume {
    // speakerVolumeMeter 为 NSLevelIndicator
    self.speakerVolumeMeter.doubleValue = volume / 255.0 * 10;
}
:::
::: Windows平台（C++） C++
// 扬声器测试示例代码
void TRTCMainViewController::startTestSpeakerDevice(std::string testAudioFilePath) 
{
	// testAudioFilePath 音频文件的绝对路径，路径字符串使用 UTF-8 编码格式，支持文件格式: wav、mp3。
	// 从 onTestSpeakerVolume 回调接口监听扬声器测试音量值。
	trtcCloud->startSpeakerDeviceTest(testAudioFilePath.c_str());
}

// 结束扬声器测试
void TRTCMainViewController::stopTestSpeakerDevice() {
	trtcCloud->stopSpeakerDeviceTest();
}
:::
::: Windows平台（C#） C#
// 扬声器测试示例代码
private void startTestSpeakerDevice(string testAudioFilePath) 
{
	// testAudioFilePath 音频文件的绝对路径，路径字符串使用 UTF-8 编码格式，支持文件格式: wav、mp3。
	// 从 onTestSpeakerVolume 回调接口监听扬声器测试音量值。
	mTRTCCloud.startSpeakerDeviceTest(testAudioFilePath);
}

// 结束扬声器测试
private void stopTestSpeakerDevice() {
	mTRTCCloud.stopSpeakerDeviceTest();
}
:::
</dx-codeblock>
