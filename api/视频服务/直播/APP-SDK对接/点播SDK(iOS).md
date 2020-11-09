## 功能篇

所谓**在线点播**，是指视频文件已经存放在服务器上，在您已经获取了文件播放 URL 的情况下，可以使用本播放器实现**边下边播**的功能。

在线点播目前常用的格式为 FLV 、 MP4 和 HLS，分别介绍一下：
- **MP4**： 比较经典的文件格式，在移动终端和 PC 浏览器上的支持度都很好（在 iOS 和大部分 Android 设备上，都可以使用系统浏览器进行播放，在 PC 上可以使用 FLASH 控件进行播放）。但是 MP4 的视频文件格式比较复杂，所以处理成本高，而且由于索引表复杂度高，导致时长大于5分钟的MP4文件在线播放时加载速度会很慢。

- **HLS**： 苹果公司力推的标准，在移动终端的浏览器上的支持度较好（在 iOS 和大部分 Android 设备上，都可以使用系统浏览器进行播放），但 IE 的支持情况依赖 FLASH 的二次开发工作（例如使用腾讯视频云的 FLASH 播放器控件）。其精简的 m3u8 的索引结构可以规避 **MP4** 的索引慢问题，如果是用于点播，是非常不错的选择。

- **FLV**： Adobe 公司所推的标准，目前直播平台最常用的封装格式，在 PC 端有 FLASH 的强力支持，但在移动终端只有 App 实现播放器才有可能支持（或者使用本播放器），大部分手机端浏览器均不支持。目前腾讯视频云的直播录制，采用的就是 FLV 视频格式。
![](https://main.qcloudimg.com/raw/5f570224943c38024d67bdf6d97c500e.png)

## 基础篇
在线点播的接口依然复用直播的接口类，即 TXLivePlayer，所以使用方式上有诸多类似之处。

### step 1 : 创建 Player 对象
```objectivec
_txLivePlayer = [[TXLivePlayer alloc] init];
[_txLivePlayer setLogLevel:LOGLEVEL_INFO];
_txLivePlayer.delegate = self; //如果您需要处理播放的事件
```

### step 2: 设置显示的 View
Player 对象内部有一个渲染的 UIView，您需要提供一个 parent view，以便 Player 将自身的 UIView 添加到上面。parent view 可以是 UIViewControler 的 view，或是您自己创建的任何 view。另外，您还需要提供一个frame，指定渲染 view 在 parent view 中的位置。
```objectivec
[_txLivePlayer setupVideoWidget:_videoWidgetFrame containView:self.view insertIndex:0];
```

### step 3: 启动播放器
用下面这段代码就可以启动播放器了：
```objectivec
NSString *vodUrl = @"http://2527.vod.myqcloud.com/xxx.mp4";
[_txLivePlayer startPlay:vodUrl type:PLAY_TYPE_VOD_MP4];
```
跟直播场景中不同的是，这里的 startPlay 中的参数为 **PLAY_TYPE_VOD_MP4**，即为 MP4在线点播。

### step 4: 进度调整
能够拖动进度条调整播放进度是点播相比于直播最直观的一个差异了，除此之外，点播还可以**暂停**和**继续**，直播就没有这么好的待遇，毕竟推流端不暂停，播放端暂停了也没什么意义。
```objectivec
// 调整进度
[_txLivePlayer seek:slider.value];
// 暂停
[_txLivePlayer pause];
// 继续
[_txLivePlayer resume];
```

### step 5: 画面调整
如果您希望调整画面的显示方式，SDK 也提供了多种选择：
![](https://main.qcloudimg.com/raw/541c5eaca744f7505ae60363ab099d20.jpg)

##### setRenderMode
* RENDER_MODE_FULL_FILL_SCREEN  - 将图像等比例铺满整个屏幕，多余部分裁剪掉，此模式下画面不留黑边。
* RENDER_MODE_ADJUST_RESOLUTION - 将图像等比例缩放，缩放后的宽和高都不会超过显示区域，居中显示，可能会留有黑边。

##### setRenderRotation
* RENDER_ROTATION_PORTRAIT - 常规的竖屏显示，如果是显示人像，则最适合这种模式了。
* RENDER_ROTATION_LANDSCAPE - 横屏显示，游戏直播比较适合这种模式。

##### resetVideoWidgetFrame
此接口用于在播放中动态调整视频渲染区域的位置和大小。


## 状态篇
### 1. 播放事件
直播里的状态我们可以关心，也可以不关心，但是点播就不同了，如下三个事件是我们必然要关心的：

| 事件ID                   | 数值   | 含义说明   |
| :--------------------- | :--- | :----- |
| PLAY_EVT_PLAY_BEGIN    | 2004 | 视频播放开始 |
| PLAY_EVT_PLAY_PROGRESS | 2005 | 视频播放进度 |
| PLAY_EVT_PLAY_END      | 2006 | 视频播放结束 |

其中进度的通知稍显复杂，因为在 param 里，会带四个参数，下面是我们的一段示例代码来解释如何处理进度通知
```objectivec
-(void) onPlayEvent:(int)EvtID withParam:(NSDictionary*)param;
{
    NSDictionary* dict = param;
    
    dispatch_async(dispatch_get_main_queue(), ^{
        if (EvtID == PLAY_EVT_PLAY_BEGIN) {
            // 如下这段代码是处理播放显示的事件，言下之意：不要转菊花了
            [self stopLoadingAnimation];
        } else if (EvtID == PLAY_EVT_PLAY_PROGRESS && !_startSeek) {
           // 如下这段代码是处理播放进度
            float progress = [dict[EVT_PLAY_PROGRESS] floatValue];
            _playStart.text = [NSString stringWithFormat:@"%02d:%02d",
            (int)progress/60,(int)progress%60];
            [_playProgress setValue:progress];
            float duration = [dict[EVT_PLAY_DURATION] floatValue];
            if (duration > 0 && _playProgress.maximumValue != duration) {
                [_playProgress setMaximumValue:duration];
                _playDuration.text = [NSString stringWithFormat:@"%02d:%02d",
                (int)duration/60,(int)duration%60];
            }
            return ;
        } else if (EvtID == PLAY_ERR_NET_DISCONNECT || EvtID == PLAY_EVT_PLAY_END) {
          // 如下这段代码是处理播放结束的事件
            [self stopRtmp];
            _play_switch = NO;
            [_btnPlay setImage:[UIImage imageNamed:@"start"] forState:UIControlStateNormal];
            [[UIApplication sharedApplication] setIdleTimerDisabled:NO];
            [_playProgress setValue:0];
            _videoPause = NO;
        }
        
        long long time = [(NSNumber*)[dict valueForKey:EVT_TIME] longLongValue];
        int mil = time % 1000;
        NSDate* date = [NSDate dateWithTimeIntervalSince1970:time/1000];
        NSString* Msg = (NSString*)[dict valueForKey:EVT_MSG];
        [self appendLog:Msg time:date mills:mil];
    });
}
```

### 2. 错误通知
对于终端开发而言，我们通常会花50%以上的时间用于处理异常逻辑，不过需要您关心的异常逻辑只有网络中断比较重要。

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_ERR_NET_DISCONNECT	          |  -2301|  网络断连,且经多次重连抢救无效,可以放弃治疗,更多重试请自行重启播放|

### 3. 一般警告
如下的这些事件，您可以不用关心，我们通知出来只是告诉您内部发生了什么，如果您需要做数据上报，倒是可以用一下：

| 事件ID                           | 数值   | 含义说明                            |
| :----------------------------- | :--- | :------------------------------ |
| PLAY_WARNING_VIDEO_DECODE_FAIL | 2101 | 当前视频帧解码失败                       |
| PLAY_WARNING_AUDIO_DECODE_FAIL | 2102 | 当前音频帧解码失败                       |
| PLAY_WARNING_RECONNECT         | 2103 | 网络断连, 已启动自动重连 (自动重连连续失败超过三次会放弃) |
| PLAY_WARNING_RECV_DATA_LAG     | 2104 | 网络来包不稳：可能是下行带宽不足，或由于主播端出流不均匀    |
| PLAY_WARNING_VIDEO_PLAY_LAG    | 2105 | 当前视频播放出现卡顿（用户直观感受）              |

### 4. 连接事件
此外还有几个连接服务器的事件，您也可以不用特别关心，这里也只要是用来测定和统计服务器连接时间和服务器响应速度用的，在用户界面交互上难有什么用处：

| 事件ID                     |    数值  |  含义说明                    |   
| :-----------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC     |  2001    | 已经连接服务器                |
| PLAY_EVT_RTMP_STREAM_BEGIN|  2002    | 已经连接服务器，开始拉流（仅播放 RTMP 地址时会抛送） |
| PLAY_EVT_RCV_FIRST_I_FRAME|  2003    | 网络接收到首个可渲染的视频数据包（IDR）  |


### 5. 状态回调 
 **onNetStatus** 通知每秒都会被触发一次，目的是实时反馈当前的推流器状态，它就像汽车的仪表盘，可以告知您目前SDK内部的一些具体情况，以便您能对当前网络状况和视频质量等有所了解。
	
|   评估参数                   |  含义说明                   |   
| :------------------------  |  :------------------------ | 
|	NET_STATUS_VIDEO_BITRATE | 当前流媒体的视频码率，单位kbps|
|	NET_STATUS_AUDIO_BITRATE | 当前流媒体的音频码率，单位kbps|
|	NET_STATUS_VIDEO_FPS     | 当前流媒体的视频帧率|
|	NET_STATUS_NET_SPEED     | 当前的网络数据接收速度|
|	NET_STATUS_NET_JITTER    | 网络抖动情况，抖动越大，网络越不稳定|
|	NET_STATUS_CACHE_SIZE    | 缓冲区（jitterbuffer）大小，缓冲区当前长度为0，说明离卡顿就不远了|

















