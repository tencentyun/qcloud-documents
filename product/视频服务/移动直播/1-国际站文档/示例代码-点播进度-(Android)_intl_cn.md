## 如何处理进度通知
下面这段代码用来展示如何处理 RTMP SDK 点播播放器的播放进度通知：

```java
public class MyTestActivity implements ITXLivePlayListener{

@Override
public void onPlayEvent(int event, Bundle param) {
    // RTMP SDK Demo 的源码中，视频画面卡住时，会在其上绘制一个半透明的loading动画。
		// 这里的 stopLoadingAnimation 是将loading动画停止掉。
    if (event == TXLiveConstants.PLAY_EVT_PLAY_BEGIN) {
        stopLoadingAnimation();
    }
    // 如下这段代码是处理播放进度
    else if (event == TXLiveConstants.PLAY_EVT_PLAY_PROGRESS) {
        int progress = param.getInt(TXLiveConstants.EVT_PLAY_PROGRESS); //进度（秒数）
        int duration = param.getInt(TXLiveConstants.EVT_PLAY_DURATION); //时间（秒数）
        
		// UI进度进行相应的调整
		mSeekBar.setProgress(progress);
        mTextStart.setText(String.format("%2d:%2d",progress/60,progress%60));
        mTextDuration.setText(String.format("%2d:%2d",duration/60,duration%60));
        mSeekBar.setMax(duration);
        return;
    }
    // 如下这段代码是处理播放结束的事件
    else if (event == TXLiveConstants.PLAY_ERR_NET_DISCONNECT
		         || event == TXLiveConstants.PLAY_EVT_PLAY_END) {
        stopPlayRtmp();
        mVideoPlay = false;
    }
}
mLivePlayer.setPlayListener(this);
```




















