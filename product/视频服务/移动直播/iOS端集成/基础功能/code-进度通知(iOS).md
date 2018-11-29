## 如何处理进度通知
下面这段代码用来展示如何处理 RTMP SDK 点播播放器的播放进度通知：

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




















