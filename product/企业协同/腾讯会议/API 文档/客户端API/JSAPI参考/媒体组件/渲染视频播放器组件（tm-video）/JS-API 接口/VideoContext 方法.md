### videoContext.load({ src: 'xxx' })
功能描述：加载需要播放的视频链接。
参数：

| 参数名称 | 参数类型  | 必填 | 参数描述 |
| --- | --- | --- |  --- |
| src | String | 否 | 视频链接。 |

```plaintext
// 加载需要播放的视频链接。
videoContext.load({ src: "https://website-1253513412.cos.ap-guangzhou.myqcloud.com/static/video/BigBuckBunny.mp4" });
```



### videoContext.play()
播放视频。

### videoContext.pause()
暂停播放。

### videoContext.stop()
停止播放。

### videoContext.mute()
静音。

### videoContext.unmute()
解除静音。

### videoContext.seek({ time: xxx })
功能描述：跳转到指定的播放时间。
参数：

| 参数名称 | 参数类型 | 必填 | 参数描述 |
| --- | --- |  --- | --- |
| time | Number  | 是 | 需要跳转的指定播放时间，单位为 ms（毫秒）。 |

```plaintext
videoContext.seek({ time: 10 * 1000 });
```

### videoContext.getSrc()
获取当前视频链接。

### videoContext.getPlaytime()
获取当前视频的播放时间点，单位 ms（毫秒）。

### videoContext.getDuration()
获取当前播放段的时长，单位 ms（毫秒）。

### videoContext.getVolume()
获取当前音量，约定取值范围是[0,1]，如果为0则是静音状态（muted）。

### videoContext.getMutedVolume()
获取静音前的音量。
