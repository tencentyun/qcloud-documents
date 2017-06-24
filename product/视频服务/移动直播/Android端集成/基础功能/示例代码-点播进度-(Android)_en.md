## How to Handle Progress Notifications
The following codes show the way to handle playback progress notifications of the VOD player of RTMP SDK:

```java
public class MyTestActivity implements ITXLivePlayListener{

@Override
public void onPlayEvent(int event, Bundle param) {
    // In the source codes of RTMP SDK Demo, a translucent loading animation will be painted on the video screen if it stutters.
		// The stopLoadingAnimation is used to stop the loading animation.
    if (event == TXLiveConstants.PLAY_EVT_PLAY_BEGIN) {
        stopLoadingAnimation();
    }
    // The following codes are used to handle the playback progress
    else if (event == TXLiveConstants.PLAY_EVT_PLAY_PROGRESS) {
        int progress = param.getInt(TXLiveConstants.EVT_PLAY_PROGRESS); //Progress (seconds)
        int duration = param.getInt(TXLiveConstants.EVT_PLAY_DURATION); //Duration (seconds)
        
		// Accordingly, adjust UI progress
		mSeekBar.setProgress(progress);
        mTextStart.setText(String.format("%2d:%2d",progress/60,progress%60));
        mTextDuration.setText(String.format("%2d:%2d",duration/60,duration%60));
        mSeekBar.setMax(duration);
        return;
    }
    // The following codes are used to handle events related to the ending of playback
    else if (event == TXLiveConstants.PLAY_ERR_NET_DISCONNECT
		         || event == TXLiveConstants.PLAY_EVT_PLAY_END) {
        stopPlayRtmp();
        mVideoPlay = false;
    }
}
mLivePlayer.setPlayListener(this);
```





















