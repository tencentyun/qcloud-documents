#TXRTMPSDK AirPlay接入指南

## AirPlay介绍

AirPlay 是苹果开发的一种无线技术，能把 iPhone 上的屏幕内容（包括系统 UI）直接投影到其它设备，因此也成为 AirPlay 镜像。

相比于 [ReplayKit](https://cloud.tencent.com/document/product/454/7883) , Airplay 的优势就是不要求目标 App 的支持，因为它可以在任何情况下获取到当前屏幕的内容，不管是一款游戏，还是系统界面。

有得必有失，如此强大的能力必然受到苹果的限制，所以使用此套方案的 APP 有可能** <font color='red'>无法通过 </font>** AppStore 的审核，如无法上架应用商店，可以考虑使用企业证书签名的方式签发 ipa 安装包。

## 版本要求
最低 iOS **9.0** 及以上系统才能支持。

## 特别说明
由于受公司内产品独占使用要求限制，带AirPlay功能的TXRTMPSDK.framework暂不提供下载，我们在努力争取尽快放开下载。需要此功能的请与商务接洽。

## 接入流程
### 1. 配置参数

初始化仅需要导入SDK，对单例TXAirPlayServerManager进行些必要的设置即可。如下:
```objective-c
_server = [TXAirPlayServerManager sharedInstance];
_server.appid = @"demo-1";
_server.serverName = @"demo-app";
_server.videoOutputType = AirPlayVideoOutputTypeH264;
_server.delegate = self;
_server.qualityWidth = 720;
_server.qualityHeight = 1280;
```

> 如果您是初次使用直播SDK，可参考 [iOS端集成](https://cloud.tencent.com/document/product/454/7876) 
>
> appid 您需要联系商务来获取；serverName 为系统AirPlay里显示的名字，可随意修改。

### 2. 启动录屏

在完成TXAirPlayServerManager的初始化设置后，只需要调用SDK提供的start方法即可开始录屏，如下:
```objective-c
[_server start:nil];
```

从AirPlay启动到连接成功，大约需要 **2～5秒** 时间。连接成功后，手机status bar的位置会出现蓝条，表示此时屏幕已被AirPlay镜像。

> 如果切换App到后台，状态栏的蓝色消失。请检查工程"Background Modes"是否有设置，建议只勾选Voice over IP即可。

### 3. 视频数据

开始录制后，视频数据流会以回调的形式返回给应用程序处理。SDK支持两种形式的视频数据：一种是AirPlay镜像传递的原始H264流，另外一种是YUV数据。


#### H264流
当设置TXAirPlayServerManager的videoOutputType属性为 AirPlayVideoOutputTypeH264 后，SDK回调的视频格式为H264原始流，回调接口为:
```
- (void)didReceivedH264Data:(unsigned char *)dataBuffer length:(uint32_t)len isIFrame:(BOOL)isIFrame timeOffset:(int64_t)timeOffset;
```

设置TXAirPlayServerManager的属性 saveH264ToFile 即可保存录制的H264视频流信息，存储在沙盒Document 录，使 VLC等工具可以查看。

#### YUV数据
当设置TXAirPlayServerManager的videoOutputType属性为 AirPlayVideoOutputTypeYUV420p 后，SDK回调的视频数据为解码后的YUV 420p数据，回调接口为:
```objective-c
- (void)didReceivedYUV420pPacket:(APYUV420pPacket)packet;
```

设置TXAirPlayServerManager的属性 saveYUVToFile 即可保存解码后的YUV数据流信息，存储在沙盒Document 录，使 YUView等工具可以查看。

__注意:YUV数据很大，保存YUV数据会占用很多磁盘空间。__

### 4. 音频数据
开始录制后，音频数据将以下面的回调返回给应用。
```
- (void)didReceivedAudioSampleBuffer:(CMSampleBufferRef)buffer;
```
对于音频SDK还提供了额外的2个能力，即静音模式和音量增强，具体请参考 TXAirPlayManager.h头文件Audio Configure部分。

### 5. 推流

#### 配置 TXLivePushConfig

TXLivePush提供多种自定义推流方式，AirPlay也属于自定义推流的一种（可以理解为AirPlay是把数据采集从摄像头换做了屏幕）。主要修改点为customModeType。

```objective-c
TXLivePushConfig* config = [[TXLivePushConfig alloc] init];
    
// video
config.homeOrientation      = [self.liveInfo homeOrientation];
config.videoFPS             = 20;
config.enableHWAcceleration = YES;
config.customModeType |= CUSTOM_MODE_VIDEO_CAPTURE;
    
config.enableAutoBitrate    = YES;
config.videoBitrateMin      = 800;
config.videoBitrateMax      = 2000;
config.videoBitratePIN      = 2000;
config.sampleBufferSize = CGSizeMake(720, 1280); // 


// Audio
config.customModeType      |= CUSTOM_MODE_AUDIO_CAPTURE; // AirPlay有自己的录音方案，必须要打开Audio自定义采集
config.audioSampleRate      = AUDIO_SAMPLE_RATE_44100;
config.audioChannels        = 1;
config.autoSampleBufferSize = YES;
```

customModeType支持TXAirPlayServerManager的两种videoOutputType方式。示例代码如下

```objective-c
double version = [[UIDevice currentDevice].systemVersion doubleValue];
if (version < 10.0) {
    _server.videoOutputType = AirPlayVideoOutputTypeH264;
  	config.customModeType |= CUSTOM_MODE_VIDEO_ENCODE_CONV;
} else {
    _server.videoOutputType = AirPlayVideoOutputTypeYUV420p;
    config.customModeType |= CUSTOM_MODE_VIDEO_CAPTURE;
}

self.txLivePublisher = [[TXLivePush alloc] initWithConfig:config]
```

iOS 10以下的系统不支持后台硬编，我们推荐TXAirPlayServerManager输出h264数据，然后由TXLivePush提供的CUSTOM_MODE_VIDEO_ENCODE_CONV转码模式进行重新编码，此模式对后台编码做了优化。

#### 开始推流

调用`[self.txLivePublisher startPush:self.rtmpUrl]`开始推流，**等到RTMP连接成功，才启动AirPlay服务**。

```objective-c
-(void)onPushEvent:(int)EvtID withParam:(NSDictionary*)param {
    if (EvtID == PUSH_EVT_CONNECT_SUCC) {
        [_server start:nil];    // RTMP连接上后再启动AirPlay
    }
    // 事件处理
}
```

> 推流事件部分参考 [推流事件监听](https://cloud.tencent.com/document/product/454/7879#1.-.E4.BA.8B.E4.BB.B6.E7.9B.91.E5.90.AC)

#### H264推流

如果TXAirPlayServerManager输出的是H264，TXLivePush提供了发送264的接口。示例代码如下

```objective-c
/// 设置 videoOutputType 为 AirPlayVideoOutputTypeH264 时，会收到这个回调
- (void)didReceivedH264Data:(unsigned char *)dataBuffer length:(uint32_t)dataLen isIFrame:(BOOL)isIFrame timeOffset:(int64_t)timestamp {
    timestamp++;
    if (isIFrame) {
        _timestamp = timestamp;
    } else {
        if (timestamp < _timestamp) {
            _timestamp += (1000 / 60);
        } else {
            _timestamp = timestamp;
        }
    }
        
    int64_t pts = _timestamp;
    EnumFrameType frameType = isIFrame ? H264_FrameType_I : H264_FrameType_P;
    
    [self.txLivePublisher sendCustomH264Data:(uint8_t *)dataBuffer
                                    dataLen: dataLen
                                  frameType: frameType
                                 frameIndex: _frameIndex++
                                        pts:(int)pts];
}
```

#### YUV推流

YUV推流需要上层将YUV420转成CMSampleBuffer格式，再通过TXLivePush提供的sendVideoSampleBuffer发送。示例代码如下

```objective-c
/// 设置 videoOutputType 为 AirPlayVideoOutputTypeYUV420p 时，会收到这个回调
- (void)didReceivedYUV420pPacket:(APYUV420pPacket)packet {
    int sYLineSize = packet.yLineSize;
    int sULineSize = packet.uLineSize;
    int sVLineSize = packet.vLineSize;
    int sYSize = sYLineSize * packet.height;
    int sUSize = sULineSize * packet.height/2;
    int sVSize = sVLineSize * packet.height/2;
    
    int dWidth = packet.width;
    int dHeight = packet.height;
    
    CVPixelBufferRef pxbuffer;
    CVReturn rc;

    rc = CVPixelBufferCreate(NULL, dWidth, dHeight, kCVPixelFormatType_420YpCbCr8PlanarFullRange, NULL, &pxbuffer);
    if (rc != 0) {
        NSLog(@"CVPixelBufferCreate failed %d", rc);
        if (pxbuffer) { CFRelease(pxbuffer); }
        return;
    }
    
    rc = CVPixelBufferLockBaseAddress(pxbuffer, 0);
    
    if (rc != 0) {
        NSLog(@"CVPixelBufferLockBaseAddress falied %d", rc);
        if (pxbuffer) { CFRelease(pxbuffer); }
        return;
    } else {
        uint8_t *y_copyBaseAddress = (uint8_t*)CVPixelBufferGetBaseAddressOfPlane(pxbuffer, 0);
        uint8_t *u_copyBaseAddress= (uint8_t*)CVPixelBufferGetBaseAddressOfPlane(pxbuffer, 1);
        uint8_t *v_copyBaseAddress= (uint8_t*)CVPixelBufferGetBaseAddressOfPlane(pxbuffer, 2);
        
        int dYLineSize = (int)CVPixelBufferGetBytesPerRowOfPlane(pxbuffer, 0);
        int dULineSize = (int)CVPixelBufferGetBytesPerRowOfPlane(pxbuffer, 1);
        int dVLineSize = (int)CVPixelBufferGetBytesPerRowOfPlane(pxbuffer, 2);
        
        memcpy(y_copyBaseAddress, packet.dataBuffer,                    sYSize);
        memcpy(u_copyBaseAddress, packet.dataBuffer + sYSize,           sUSize);
        memcpy(v_copyBaseAddress, packet.dataBuffer + sYSize + sUSize,  sVSize);

        
        rc = CVPixelBufferUnlockBaseAddress(pxbuffer, 0);
        if (rc != 0) {
            NSLog(@"CVPixelBufferUnlockBaseAddress falied %d", rc);
        }
    }
    
    CMVideoFormatDescriptionRef videoInfo = NULL;
    CMVideoFormatDescriptionCreateForImageBuffer(NULL, pxbuffer, &videoInfo);
    
    CMSampleTimingInfo timing = {kCMTimeInvalid, kCMTimeInvalid, kCMTimeInvalid};
    CMSampleBufferRef dstSampleBuffer = NULL;
    rc = CMSampleBufferCreateForImageBuffer(kCFAllocatorDefault, pxbuffer, YES, NULL, NULL, videoInfo, &timing, &dstSampleBuffer);
    
    if (rc) {
        NSLog(@"CMSampleBufferCreateForImageBuffer error: %d", rc);
    } else {
        [self.txLivePublisher sendVideoSampleBuffer:dstSampleBuffer];
    }
    
    if (pxbuffer) { CFRelease(pxbuffer); }
    if (videoInfo) { CFRelease(videoInfo); }
    if (dstSampleBuffer) { CFRelease(dstSampleBuffer); }
```

这种推流模式可参考[游戏录屏（ReplayKit）](https://cloud.tencent.com/document/product/454/7883)。

#### 声音

声音TXAirPlayServerManager和TXLivePush都支持CMSampleBufferRef，所以无需转换

```objective-c
#pragma mark - 音频回调
- (void)didReceivedAudioSampleBuffer:(CMSampleBufferRef)buffer {
    [self.txLivePublisher sendAudioSampleBuffer:buffer];
}
```

### 5. 停止服务
调用SDK接口stop即可停止AirPlay服务和录制。
```
[_server stop];
```

## 常见问题

### 1. AppStore上架

AirPlay是苹果的私有协议，因而无法通过审核，强行上架有一定风险。

### 2. 启动服务后，长时间没有收到连接成功通知

请检查网络是否异常，或提示用户手动选择AirPlay设备。自动连接随系统升级可能发生改变，请参考最新小直播代码。

### 3. 码率选择

录屏画面变化波动比摄像头要大，相同分辨率和帧率下，达到同样的清晰度往往需要更高的码率，关于码率的选择请参考[如何实现好的画质](https://cloud.tencent.com/document/product/454/7955)。

### 4. 直播出现帧率降低

SDK录屏多数时间都是在后台运行，iOS 限制了后台运行 App 的 CPU 使用率，以保证前台App的流畅。

如果当前手机配置较低，且有在运行大型游戏，有可能影响推流的流畅。您可以监听 `[TXLivePushDelegate onNetStatus:]` 的状态回调的 NET_STATUS_CODEC_CACHE 的值，理想情况 CACHE 的大小为0，如果大于100，则有必要通知用户先暂时回到App，待Cache降低后再玩。
