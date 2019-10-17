## Feature Overview

Super Player is an **open source**, `TXVodPlayer`-based solution including video information pulling, switching between landscape/portrait modes, definition selection, on-screen comment and other features. With Super Player, you can provide a playback experience comparable to any popular video App in a short time.

![](https://mc.qcloudimg.com/static/img/c5a7b6e6e8cba617b76fee49aa03da18/image.png)

## Integration Preparations

1. Download SDK + Demo package from [Android](https://cloud.tencent.com/document/product/454/7873#Android).

2. Open source the UI-related codes of the player. Copy the open-source codes in the `app/src/main/java/com/tencent/liteav/demo/play/` folder and the image resources in the `app/src/main/res/drawable-xxhdpi/` folder to your App project.

3. The on-screen comment in Demo integrates a third-party open source library `DanmakuFlameMaster`, which is available on github. You can also obtain it by configuring the build.gradle as in the Demo. 
```
compile 'com.github.ctiao:DanmakuFlameMaster:0.5.3'
```

## Creating a Player

The main type of the super player is `SuperVideoPlayer`. You need to create it first.

```objective-c
mSuperVideoPlayer = (SuperVideoPlayer) findViewById(R.id.video_player_item_1);
mSuperVideoPlayer.setVideoPlayCallback(mVideoPlayCallback);
```

## Obtaining Video Information

Unlike playback of an ordinary URL, fileId is required to obtain video information.

```objective-c
TXPlayerAuthParams *p = [TXPlayerAuthParams new];
p.appId = 1252463788;
p.fileId = @"4564972819220421305";

TXPlayerAuthBuilder authBuilder = new TXPlayerAuthBuilder();
try {
    authBuilder.setAppId(Integer.parseInt(playerAuthParam.appId));
    authBuilder.setFileId(playerAuthParam.fileId);
    mTXPlayerGetInfo.startPlay(authBuilder);
} catch (NumberFormatException e) {
    Toast.makeText(mContext, "Enter the correct AppId", 0).show();
}
```

fileId is generally returned by the server after the video is uploaded:

1. After the video is published from the client, the server returns [fileId](https://cloud.tencent.com/document/product/584/9367#8..E5.8F.91.E5.B8.83.E7.BB.93.E6.9E.9C) to the client.
2. If the video is uploaded from the server, the fileId is included in the [upload confirmation](https://cloud.tencent.com/document/product/266/9757) notification.

If the file already exists in Tencent Cloud, find it in the [VOD Management](https://console.cloud.tencent.com/vod/videolist) and click to view the appId and fileId in the video details at the right side.

![](https://mc.qcloudimg.com/static/img/fcad44c3392b229f3a53d5f8b2c52961/image.png)

If the request is successful, SDK will inform the upper layer of the video information as an event.

The example of SuperVideoPlayer in Demo
```objective-c
mTXPlayerGetInfo = new TXVodPlayer(context);
mTxplayer.setVodListener(mPlayVodListener);
mTXPlayerGetInfo.setVodListener(mGetVodInfoListener);

/**
 * Obtain the information of the video corresponding to fileId
 */
private ITXVodPlayListener mGetVodInfoListener = new ITXVodPlayListener() {
    @Override
    public void onPlayEvent(TXVodPlayer player, int event, Bundle param) {
        String playEventLog = "receive event: " + event + ", " + param.getString(TXLiveConstants.EVT_DESCRIPTION);
        Log.d(TAG, playEventLog);

        if (event == TXLiveConstants.PLAY_EVT_GET_PLAYINFO_SUCC) { // VOD file information obtained successfully
            VodRspData data = new VodRspData();
            data.cover = param.getString(TXLiveConstants.EVT_PLAY_COVER_URL);
            data.duration = param.getInt(TXLiveConstants.EVT_PLAY_DURATION);
            data.url = param.getString(TXLiveConstants.EVT_PLAY_URL);
            if (mVideoPlayCallback != null) {
                mVideoPlayCallback.onLoadVideoInfo(data);
            }
        }
    }
};
```


## Switching Between Videos

You can call `setPlayUrl` to play another video in the player

```objective-c
String url = "http://1252463788.vod2.myqcloud.com/xxx/yyy/v.f20.mp4";
if (mSuperVideoPlayer != null) {
    mSuperVideoPlayer.updateUI("New video");
    mSuperVideoPlayer.setPlayUrl(url);
}
```

## Removing the Player

When the player is not needed, call "resetPlayer" to reset the player's internal status to prevent interference to the next playback.

```objective-c
if (mSuperVideoPlayer != null) {
    mSuperVideoPlayer.onDestroy();
}
```


