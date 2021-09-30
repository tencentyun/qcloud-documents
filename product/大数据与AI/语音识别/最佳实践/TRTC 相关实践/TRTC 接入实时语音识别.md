## 概述
当用户接入实时音视频（Tencent RTC）服务后，有时会有实时语音识别需求，从而实现实时会议字幕或语音弹幕等功能。本文档帮助客户端（Android/iOS）用户在已经接入 TRTC 服务后，更好的对实时语音识别进行接入。

## iOS 接入流程
1. 首先需要 [接入 TRTC](https://cloud.tencent.com/document/product/647/32221)，跑通流程。
2. 根据实时语音识别 [音频流格式要求](https://cloud.tencent.com/document/product/1093/35799)，参考 [TRTC 技术文档](http://doc.qcloudtrtc.com/group__TRTCCloud__ios.html) 设置音频流格式。
3. 在 [TRTC 接口协议](http://doc.qcloudtrtc.com/group__TRTCCloudDelegate__ios.html) 中设置音频源代理，并设置 ASR 读取音频源。

```objective-c
//1.TRTCAudioFrameDelegate 协议是 TRTC 获取音频源的协议，由于 ASR 识别16k或8k采样率的音频数据，所以需要设置 setAudioQuality 为 TRTCCloudDef#TRTC_AUDIO_QUALITY_SPEECH (流畅:采样率:16k;单声道;音频裸码率:16kbps)

- (void) onCapturedRawAudioFrame:(TRTCAudioFrame *)frame {//此方法为 TRTC 本地麦克风采集到的原始音频数据回调：

  NSUInteger readLength = [frame.data length];
  void *pcmBytes = (void *)frame.data.bytes;
  [dataSource didRecordAudioData:pcmBytes length:readLength];
}
```
4. ASR 音频源设置为第三方，并实现具体逻辑。

4.1 接入第三方音频源需要在 ASR 接入部分实现 QCloudAudioDataSource 协议。代码示例如下：
```objective-c
#import<QCloudSDK/QCloudSDK.h>

//1.使用第三方外部数据源传入语音数据，自定义 data source 需要实现 QCloudAudioDataSource 协议
QDAudioDataSource *dataSource = [[QDAudioDataSource alloc] init];

//2.创建 QCloudRealTimeRecognizer 识别实例
QCloudRealTimeRecognizer *realTimeRecognizer = [[QCloudRealTimeRecognizer alloc] initWithConfig:config dataSource:dataSource];
```
4.2 接入 ASR 的 QCloudAudioDataSource 协议如下，[协议详情](https://cloud.tencent.com/document/product/1093/35723#QCloudAudioDataSource)。代码可参考工程中 QDAudioDataSource.m 文件。

```objc
@interface QDAudioDataSource : NSObject<QCloudAudioDataSource>
@end

@implementation QDAudioDataSource
@synthesize running = _running;

//SDK 会调用此方法获取当前状态
- (BOOL)running{
    return _recording;
}

//SDK 会调用 start 方法，实现此协议的类需要初始化数据源
- (void)start:(void(^)(BOOL didStart, NSError *error))completion{
  _data = [[NSMutableData alloc] init];
}

//SDK 会调用 stop 方法，实现此协议的类需要停止提供数据
- (void)stop{
  _recording = NO;
  _data = nil;
}

//SDK 会调用实现此协议的对象的此方法读取语音数据
- (nullable NSData *)readData:(NSInteger)expectLength{
  NSData *data = nil;
  if ([_data length] >= _offset + expectLength) {
      data = [_data subdataWithRange:NSMakeRange(_offset, expectLength)];
      [_data replaceBytesInRange:NSMakeRange(_offset, expectLength) withBytes:NULL length:0];
  }
  return data;
}

//此处仅为演示，需用户自行完善音频数据源填充
- (void)didRecordAudioData:(void * const )bytes length:(NSInteger)length{
  [_data appendBytes:bytes length:length];
}
@end
```


## Android 接入流程

1. 首先需要 [接入 TRTC](https://cloud.tencent.com/document/product/647/32221)，跑通流程。
2. 根据实时语音识别 [音频流格式要求](https://cloud.tencent.com/document/product/1093/35799)，参考 [TRTC 技术文档](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html) 设置音频流格式。
3. 在 [TRTC 接口协议](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html) 里设置音频源代理，并设置 ASR 读取音频源。
4. ASR 音频源设置为第三方，并实现具体逻辑。
 - 接入第三方音频源需要在 ASR 接入部分实现 PcmAudioDataSource 接口。代码示例如下：
```java
//1.使用第三方外部数据源传入语音数据，自定义 data source 需要实现 PcmAudioDataSource 接口
AudioDataSource dataSource = new AudioDataSource(); 
//2.初始化语音识别请求
final AudioRecognizeRequest audioRecognizeRequest = new AudioRecognizeRequest.Builder()
.pcmAudioDataSource(dataSource)
.build(); 
```
 - 接入 ASR 的 PcmAudioDataSource 接口实现如下，[协议详情](https://cloud.tencent.com/document/product/1093/35722)。代码可参考工程中 AudioDataSource.java 文件。
```java
private ConcurrentLinkedDeque<Short> shortList = new ConcurrentLinkedDeque<>();
private static boolean first;

public class AudioDataSource implements PcmAudioDataSource { 
//向语音识别器添加数据，将长度为 length 的数据从下标0开始复制到 audioPcmData 数组中，并返回实际的复制的数据量的长度 
@Override
    public int read(short[] audioPcmData, int length) {
        short[] tempData = new short[length];
        try {
            if (!first) {
                first = true;
                SystemClock.sleep(1000);
            }
            ConcurrentLinkedDeque<Short> shorts;
            shorts = getDataList();
            if (shorts.size() < length) {
                SystemClock.sleep(300);
            }
            shorts = getDataList();
            for (int i = 0; i < tempData.length; i++) {
                tempData[i] = shorts.poll();
            }
            System.arraycopy(tempData, 0, audioPcmData, 0, tempData.length);
        } catch (Exception e) {
            return 0;
        }
        return tempData.length;
    } 
//启动识别时回调函数，用户可以在这里做些初始化的工作。
@Override
    public void start() {
    } 
//结束识别时回调函数，用户可以在这里进行一些清理工作
 @Override
    public void stop() {
    } 
//设置语音识别器每次最大读取数据量。 
@Override
    public int maxLengthOnceRead() {
        return 640;
    } 
//此处仅为演示，需用户自行完善音频数据源填充
public void writeByte(short[] pcmData) {
        for (short pcmDatum : pcmData) {
            shortList.add(pcmDatum);
        }
    }  
private ConcurrentLinkedDeque<Short> getDataList() {
        return shortList;
    } 
```
 - TRTC 音频源接入 ASR 协议如下，[TRTC 协议详情](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html)。
```java
//1.TRTCCloudListener.TRTCAudioFrameListener 是 TRTC 获取本地麦克风采集到的音频数据回调  由于 ASR 识别16k或8k采样率的音频数据，所以需要设置 setAudioQuality 为 TRTCCloudDef#TRTC_AUDIO_QUALITY_SPEECH （流畅：采样率：16k；单声道；音频裸码率：16kbps）
void onCapturedRawAudioFrame(TRTCCloudDef.TRTCAudioFrame trtcAudioFrame) {
dataSource.writeByte(bytesToShort(trtcAudioFrame.data));; 
} 
//以下方法为把 btyes 数组转成 short 数组
public static short[] bytesToShort(byte[] bytes) {
    if (bytes == null) {
        return null;
    }
    short[] shorts = new short[bytes.length / 2];
ByteBuffer.wrap(bytes).order(ByteOrder.LITTLE_ENDIAN).asShortBuffer().get(shorts);
    return shorts;
}
```
