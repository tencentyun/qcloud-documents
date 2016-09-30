
## DEMO体验
**【界面截图】**
DEMO的整体实现力求简单易懂，适合只对接纯推流和播放服务的客户：
![](//mc.qcloudimg.com/static/img/a39eddc4b5f1ea062355ab865a845fb9/image.png)

**【功能支持】** 
- 推流：RTMP 推流
- 直播：RTMP、FLV格式的在线直播
- 点播：MP4、HLS和FLV格式的在线点播

**【APP安装】**
![](//mc.qcloudimg.com/static/img/6de577ff89bbb280dc6e3888c2724298/image.png)

**【体验地址】**
RTMP推流具有排它性：同一时间、同一URL，<font color='red'>只能有一个主播</font>在推流中。所以如果您体验推流总是断开（被后台拒绝），说明地址已经被其他的体验者占用，推荐您直接[开通腾讯云直播服务](https://console.qcloud.com/live)并创建自己的频道进行体验。

如下是3组测试地址：

```
//第一组地址：
PUSH(RTMP): rtmp://2000.livepush.myqcloud.com/live/2000_1f4652b179af11e69776e435c87f075e?bizid=2000
PLAY(FLV) : http://2000.liveplay.myqcloud.com/live/2000_1f4652b179af11e69776e435c87f075e.flv
PLAY(HLS) : http://2000.liveplay.myqcloud.com/2000_1f4652b179af11e69776e435c87f075e.m3u8
```

```
//第二组地址：
PUSH(RTMP): rtmp://2000.livepush.myqcloud.com/live/2000_44c6e64e79af11e69776e435c87f075e?bizid=2000
PLAY(FLV) : http://2000.liveplay.myqcloud.com/live/2000_44c6e64e79af11e69776e435c87f075e.flv
PLAY(HLS) : http://2000.liveplay.myqcloud.com/2000_44c6e64e79af11e69776e435c87f075e.m3u8
```

```
//第三组地址：
PUSH(RTMP): rtmp://2000.livepush.myqcloud.com/live/2000_4eb4da7079af11e69776e435c87f075e?bizid=2000
PLAY(FLV) : http://2000.liveplay.myqcloud.com/live/2000_4eb4da7079af11e69776e435c87f075e.flv
PLAY(HLS) : http://2000.liveplay.myqcloud.com/2000_4eb4da7079af11e69776e435c87f075e.m3u8
```


## 小直播体验
**【界面截图】**
小直播是基于腾讯视频云服务实现的一个直播APP的原型软件，开放终端和后台的实现源码，适合零基础的客户进行参考和评估之用：
![](//mc.qcloudimg.com/static/img/05d2e651ff6c9332211eaf7fea167cfa/image.png)

**【功能支持】** 
- 直播：支持实时直播和观看，延迟3s以内，视频秒开体验。
- 互动：支持互动消息、弹幕、点赞等互动体验。
- 回看：超过一分钟的直播内容会自动进入录播列表，提供回看能力。

**【后台服务】**
小直播的后台服务目前部署于一台普通的腾讯云虚拟主机上，基于PHP技术构建，提供源码下载和参考。

**【APP安装】**
![](//mc.qcloudimg.com/static/img/3939152d7b9a6fd0812b886ea049dc83/image.png)


## 移动端SDK

**【最新特性】**
- Android SDK 增加手机录屏功能，可以手游直播了（支持隐私模式）
- 新增背景混音能力，主播可以选择喜欢的歌曲进行伴音。
- 优化APP切后台的推流逻辑，采用贴片的方式解决主播端APP切后台之后，观众端持续重连最终断开的问题；
- 强化客户自定义采集接口能力，客户可以采集不同格式的视频数据提供给SDK发送；
- IOS点播增加静音能力 （感谢蘑菇街团队的建议）
- 修复推流播放释放错乱引起的闪屏问题，临时方案，1.6.2 会引入多实例

**【详细说明】**
- 压缩包中是可以通过编译并运行的DEMO工程，SDK位于DEMO文件夹内。
- 开发环境的工程配置请参考 [IOS平台](https://www.qcloud.com/doc/api/258/5320) & [Android平台](https://www.qcloud.com/doc/api/258/5319)。
- 每个版本的更新情况详见[历史更新记录](https://www.qcloud.com/doc/api/258/6173)

**【测试情况】**
- 总用例数：351，通过用例数：325，不通过用例数：26

【**接口变更（iOS）**】
> - IOS中 TXLivePlayer类新增接口函数 setMute:(BOOL)bEnable 用于设置静音。
> - IOS中 TXLivePush类新增接口函数 pausePush 和 resumePush 用于应对APP切后台推流被中断的问题，具体使用方式请参考demo里面的示例：
>    * 当APP切到后台之后，iOS(以及Android)系统会禁止APP继续采集摄像头的数据，此时如果什么都不做，观众端就会出现断流的情况。
>    * 当APP切到后台之后，调用pausePush会推送一张贴片图片，图片可以使用 TXLivePushConfig 中的 pauseImg 配置项进行设置。
>    * 当APP切回前台之后，调用resumePush，APP会继续采集摄像头和麦克风的数据。
>    
> - 修改自定义视频数据发送接口，原接口名称为 sendCustomYUVData 改动目的是为了兼容更多类型的数据，例如RGB等图像数据类型。
> - 新增IOS专用自定义视频数据发送接口 sendVideoSampleBuffer:(CMSampleBufferRef)sampleBuffer 
> 内含丢帧和补帧逻辑，过快和过慢的调用频率均会进行纠正
> 
> - 新增IOS专用自定义音频数据发送接口 sendAudioSampleBuffer:(CMSampleBufferRef)sampleBuffer;

> - 新增6个接口用于背景混音处理，背景音与Mic采集到的人声混合
     * (BOOL) playBGM:(NSString *)path; //playBGM 播放背景音乐
     * (BOOL) stopBGM; //停止播放背景音乐
     * (BOOL) pauseBGM;  //暂停播放背景音乐
     * (BOOL) resumeBGM; //继续播放背景音乐
     * (BOOL) setMicVolume:(float)volume;  //设置麦克风的音量大小
     * (BOOL) setBGMVolume:(float)volume;  //设置背景音乐的音量大小

【**接口变更（Android）**】
> - 新增两个接口用于录屏（录屏要求必须开启硬件加速，否则性能跟不上）
>   * public void startScreenCapture(); //开始录屏
>   * public void stopScreenCapture(); //结束录屏
>   * public void pausePusher(); //进入隐私模式
>   * public void resumePusher(); //取消隐私模式
>   * 录屏还需要在manifest里面加个activity，别忘了哦！
>   `<activity android:name="com.tencent.rtmp.video.TXScreenCapture$TXScreenCaptureAssistantActivity" android:theme="@android:style/Theme.Translucent"/>`

> - IOS中 TXLivePush类新增接口函数 pausePusher 和 resumePusher 用于应对APP切后台推流被中断的问题，具体使用方式请参考demo里面的示例：
>    * 当APP切到后台之后，Android系统会禁止APP继续采集摄像头的数据，此时如果什么都不做，观众端就会出现断流的情况。
>    * 当APP切到后台之后，调用pausePusher会推送一张贴片图片，图片可以使用 TXLivePushConfig 中的 setPauseImg 配置项进行设置。
>    * 当APP切回前台之后，调用resumePusher，APP会继续采集摄像头和麦克风的数据。

> - 修改自定义视频数据发送接口，原接口名称为 sendCustomYUVData 改动目的是为了兼容更多类型的数据，例如RGB等图像数据类型 sendCustomVideoData(byte [] buffer, int bufferType, int w, int h)；

> - 新增6个接口用于背景混音处理，背景音与Mic采集到的人声混合
>    * public boolean playBGM(String path); //playBGM 播放背景音乐
>    * public boolean stopBGM(); //停止播放背景音乐
>    * public boolean pauseBGM(); //暂停播放背景音乐
>    * public boolean resumeBGM(); //继续播放背景音乐
>    * public boolean setMicVolume(float x); //设置麦克风的音量大小
>    * public boolean setBGMVolume(float x); //设置背景音乐的音量大小

**【下载地址】**

| 操作系统 | 版本号 | 更新时间|下载链接 |
| ---- | ----------- | ---- | ---- | 
| IOS  | 1.6.1.770  | 2016-09-30 | [点击下载](http://download-10055601.cos.myqcloud.com/RTMPSDK_And_Demo__IOS_1.6.1.770.zip)  |
| Android  | 1.6.1.770 | 2016-09-30 | [点击下载](http://download-10055601.cos.myqcloud.com/RTMPSDK_And_Demo__Android_1.6.1.770.zip)  |

