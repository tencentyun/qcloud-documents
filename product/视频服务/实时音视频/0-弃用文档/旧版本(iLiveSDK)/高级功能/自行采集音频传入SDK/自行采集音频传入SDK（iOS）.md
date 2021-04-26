本课程讲解伴奏，音频透传相关问题

## 效果图

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。 点击[下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/iOS/Demo_CustomAudio.zip)
## 相关概念

** 伴奏 **
主播说话的过程中附带背景音乐

** 麦克风纯音频透传 **
主播说话的同时，还有其它模块在采集另外的音频数据，将这些自定义采集的音频数据和主播的声音混流后一起传输出去(主播端听不到，观众端能听到)

** 扬声器纯音频透传 **
主播说话的同时，还有其它模块在采集另外的音频数据，将这些自定义采集的音频数据和主播的声音混流后一起传输出去(主播端能听到，观众端能听到)

## 流程图
伴奏流程图
![](https://main.qcloudimg.com/raw/06f21699dcc9be582e7390211cdafddc.png)

纯音频透传流程图
![](https://main.qcloudimg.com/raw/e4dfa85ce847b3916543108ff4368d2b.png)

## 伴奏实现
伴奏的实现非常简单，只需调用一个接口即可
在**创建房间成功后**，将准备好的伴奏音频文件路径，传入伴奏接口中，调用示例：
```
//filePath：伴奏文件路径，目前支持wav aac mp3 m4a格式
//loopBack: 是否混音发送，一般都设置为true
//loopCount:循环次数，-1为无限循环
//duckerTimeMs：淡出效果，结尾时的淡出时间
//block: 播放结束时的回调
NSString *path = [[NSBundle mainBundle] pathForResource:@"love" ofType:@"mp3"];
QAVAudioEffectCtrl *audioEfftCtl = [[ILiveSDK getInstance] getAVContext].audioEffectCtrl;
QAVResult result = [audioEfftCtl startAccompany:path loopBack:YES loopCount:-1 duckerTimeMs:10 complete:^(int result, NSString *filePath) {
    NSLog(@"complete");
}];
NSLog(@"resul:%ld",result);
```

## 纯音频透传实现

### 设置音频数据回调
```
//创建房间前设置
[[[ILiveSDK getInstance] getAVContext].audioCtrl setAudioDataEventDelegate:self];
```

### 开启外部设备采集功能

```
//进入房间后设置
[[[ILiveSDK getInstance] getAVContext].audioCtrl enableExternalAudioDataInput:YES];
```

### 注册音频数据类型回调
```
//按需注册回调，Demo中注册了QAVAudioDataSource_MixToSend和QAVAudioDataSource_MixToPlay事件的回调
[[[ILiveSDK getInstance] getAVContext].audioCtrl registerAudioDataCallback:QAVAudioDataSource_MixToSend];
[[[ILiveSDK getInstance] getAVContext].audioCtrl registerAudioDataCallback:QAVAudioDataSource_MixToPlay];
```

### 注册音频数据回调中的处理

```
- (QAVResult)audioDataShouInput:(QAVAudioFrame *)audioFrame type:(QAVAudioDataSourceType)type {
    // 演示如何将透传的数据添加到QAVAudioFrame
    // 混音输入（Mic和Speaker）的主要回调
    // 麦克风透传处理
    // 主要场景：主播端除了需要传输主播说的话，还需要传输一个背景音乐
    if (type == QAVAudioDataSource_MixToSend)
    {
        // self.testData 为要透传的音频数据，默认使用QAVAudioFrameDesc = {48000, 2, 16}，外部传入数据时，注意对应，外部传入的时候，注意相关的参数
        if (self.testData)
        {
            NSInteger off = self.testOffset;
            [self handle:&audioFrame withPCM:self.testData offset:&off];
            self.testOffset = off;
        }
    }
    // 扬声明器透传处理
    // 主要场景：主播端的音频，在主播本地再发播放一次，主播本人能知道这个音频是什么效果
    else if (type == QAVAudioDataSource_MixToPlay)
    {
        // self.speakerAudioTransmissionData 为要透传的音频数据，默认同样使用QAVAudioFrameDesc = {48000, 2, 16}，外部传入数据时，注意对应，外部传入的时候，注意相关的参数
        if (self.testData)
        {
            NSInteger off = self.testOffset;
            [self handle:&audioFrame withPCM:self.testData offset:&off];
            self.testOffset = off;
        }
    }
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
```

## 常见问题
* 1 实现纯音频透传时，声音无法正确播放，一般是因为音频数据格式不正确导致，自定义采集的音频数据的采样率，通道数，音频位宽，必须与回调中QAVAudioFrame数据的一致
