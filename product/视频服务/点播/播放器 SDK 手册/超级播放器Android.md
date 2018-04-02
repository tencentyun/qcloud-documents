## 功能介绍

超级播放器是基于`TXVodPlayer`实现的集视频信息拉取、横竖屏切换、清晰度选择、弹幕等功能于一体的解决方案，**且完全开源**。帮助您在短时间内，打造一个媲美市面上各种流行视频App的播放体验。

![](https://mc.qcloudimg.com/static/img/c5a7b6e6e8cba617b76fee49aa03da18/image.png)

## 接入准备

1. 下载 SDK + Demo 开发包，下载地址为([Android](https://cloud.tencent.com/document/product/454/7873#Android)).

2. 播放器的 UI 部分代码开源，开源代码位于 `app/src/main/java/com/tencent/liteav/demo/play/`文件夹中，图片资源位于`app/src/main/res/drawable-xxhdpi/`文件夹中，您需要先将这两部分拷贝的您的App工程中。

3. Demo的弹幕集成了第三方开源库`DanmakuFlameMaster`，可以自行在github获取，也可如Demo在build.gradle示例配置 
```
compile 'com.github.ctiao:DanmakuFlameMaster:0.5.3'
```

## 创建播放器

超级播放器主类为`SuperVideoPlayer`，您需求先创建它。

```objective-c
mSuperVideoPlayer = (SuperVideoPlayer) findViewById(R.id.video_player_item_1);
mSuperVideoPlayer.setVideoPlayCallback(mVideoPlayCallback);
```

## 视频信息获取

与播放普通url地址不同，获取视频信息需要通过fileId方式。

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
    Toast.makeText(mContext, "请输入正确的AppId", 0).show();
}
```

fileId在一般是在视频上传后，由服务器返回：

1. 客户端视频发布后，服务器会返回[fileId](https://cloud.tencent.com/document/product/584/9367#8..E5.8F.91.E5.B8.83.E7.BB.93.E6.9E.9C)到客户端
2. 服务端视频上传，在[确认上传](https://cloud.tencent.com/document/product/266/9757)的通知中包含对应的fileId

如果文件已存在腾讯云，则可以进入 [点播视频管理](https://console.cloud.tencent.com/video/videolist) ，找到对应的文件。点开后在右侧视频详情中，可以看到appId和fileId。

![视频管理](https://mc.qcloudimg.com/static/img/fcad44c3392b229f3a53d5f8b2c52961/image.png)

SDK在请求成功后，将视频信息将以事件的形式通知到上层

在Demo中SuperVideoPlayer中示例
```objective-c
mTXPlayerGetInfo = new TXVodPlayer(context);
mTxplayer.setVodListener(mPlayVodListener);
mTXPlayerGetInfo.setVodListener(mGetVodInfoListener);

/**
 * 获取fileId对应的视频信息
 */
private ITXVodPlayListener mGetVodInfoListener = new ITXVodPlayListener() {
    @Override
    public void onPlayEvent(TXVodPlayer player, int event, Bundle param) {
        String playEventLog = "receive event: " + event + ", " + param.getString(TXLiveConstants.EVT_DESCRIPTION);
        Log.d(TAG, playEventLog);

        if (event == TXLiveConstants.PLAY_EVT_GET_PLAYINFO_SUCC) { // 获取点播文件信息成功
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


## 切换视频

播放器播放另一个视频，调用`setPlayUrl`即可

```objective-c
String url = "http://1252463788.vod2.myqcloud.com/xxx/yyy/v.f20.mp4";
if (mSuperVideoPlayer != null) {
    mSuperVideoPlayer.updateUI("新播放的视频");
    mSuperVideoPlayer.setPlayUrl(url);
}
```

## 移除播放器

当不需要播放器时，调用onDestroy清理播放器内部状态，防止干扰下次播放。

```objective-c
if (mSuperVideoPlayer != null) {
    mSuperVideoPlayer.onDestroy();
}
```

