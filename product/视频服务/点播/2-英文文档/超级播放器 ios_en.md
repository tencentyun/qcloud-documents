## Feature Overview

Super Player is an **open source**, `TXVodPlayer`-based solution including video information pulling, switching between landscape/portrait modes, definition selection, on-screen comment and other features. With Super Player, you can provide a playback experience comparable to any popular video App in a short time.


![](https://mc.qcloudimg.com/static/img/c5a7b6e6e8cba617b76fee49aa03da18/image.png)

## Integration Preparations

1. Download SDK + Demo package from ([iOS](https://cloud.tencent.com/document/product/454/7873#iOS)).

2. Open source the UI-related codes of the super player. Copy the open-source codes in the `Player` folder and the image resources in the `Resource/Player` folder to your App project. You can add other dependent third-party databases with Pod or obtain them from the `Third` directory.
 - Masonry
 - SDWebImage


## Creating a Player

The main type of the super player is `ZFPlayerView`. You need to create and add it to the desired parent View.

```objective-c
_playerView = [[ZFPlayerView alloc] init];
        
[_playerView playerControlView:nil playerModel:self.playerModel];

// Set a proxy
_playerView.delegate = self;

// Play automatically after being loaded
[self.playerView autoPlayTheVideo];
```

## Obtaining Video Information

Unlike playback of an ordinary URL, fileId is required to obtain video information.

```objective-c
TXPlayerAuthParams *p = [TXPlayerAuthParams new];
p.appId = 1252463788;
p.fileId = @"4564972819220421305";

self.getInfoPlayer = [[TXVodPlayer alloc] init];
[self.getInfoPlayer setIsAutoPlay:NO];
self.getInfoPlayer.vodDelegate = self;
[self.getInfoPlayer startPlayWithParams:p];
```

fileId is generally returned by the server after the video is uploaded:

1. After the video is published from the client, the server returns [fileId](https://cloud.tencent.com/document/product/584/9367#8..E5.8F.91.E5.B8.83.E7.BB.93.E6.9E.9C) to the client.
2. If the video is uploaded from the server, the fileId is included in the [upload confirmation](https://cloud.tencent.com/document/product/266/9757) notification.

If the file already exists in Tencent Cloud, find it in the [VOD Management](https://console.cloud.tencent.com/vod/videolist) and click to view the appId and fileId in the video details at the right side.

![ ](https://mc.qcloudimg.com/static/img/fcad44c3392b229f3a53d5f8b2c52961/image.png)



If the request is successful, SDK will inform the upper layer of the video information as an event.

```objective-c
- (void)onPlayEvent:(TXVodPlayer *)player event:(int)EvtID withParam:(NSDictionary *)param
{
    
    if (EvtID == PLAY_EVT_GET_PLAYINFO_SUCC) {
        ListVideoModel *model = [ListVideoModel new];
        model.cover = param[EVT_PLAY_COVER_URL];
        model.duration = [param[EVT_PLAY_DURATION] intValue];
        model.url = param[EVT_PLAY_URL];
    }
}
```


## Switching Between Videos

To play another video, you need to recreate a `playerModel` and call resetToPlayNewVideo.

```objective-c
_playerModel.title = [cell getSource].title;
_playerModel.videoURL = [NSURL URLWithString:[cell getSource].url];
_playerModel.placeholderImage = [UIImage imageWithData:[NSData dataWithContentsOfURL:
                                [NSURL URLWithString:[cell getSource].cover]]];

[_playerView resetToPlayNewVideo:self.playerModel];
```
## Removing the Player

When the player is not needed, call "resetPlayer" to reset the player's internal status to prevent interference to the next playback.

```objective-c
[self.playerView resetPlayer];  //Very important
```


