## How to Handle Progress Notifications
The following codes show the way to handle playback progress notifications of the VOD player of RTMP SDK:

```objectivec
-(void) onPlayEvent:(int)EvtID withParam:(NSDictionary*)param;
{
    NSDictionary* dict = param;

    dispatch_async(dispatch_get_main_queue(), ^{
        if (EvtID == PLAY_EVT_PLAY_BEGIN) {
            // The following codes are used to handle events related to playback display, and indicate: stop the loading animation
            [self stopLoadingAnimation];
        } else if (EvtID == PLAY_EVT_PLAY_PROGRESS && !_startSeek) {
           // The following codes are used to handle the playback progress
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
          // The following codes are used to handle events related to the ending of playback 
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





















