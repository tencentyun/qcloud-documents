## 接口
### audioContext.load({ src: 'xxx' })
**功能描述：**加载需要播放的音频链接。

**参数：**

| 参数名称 | 参数类型  | 必填 | 参数描述 |
| --- | --- | ---  | --- |
| src | String  | 否 | 音频链接。 |

```plaintext
// 加载需要播放的音频链接。
audioContext.load({ src: "https://website-1253513412.cos.ap-guangzhou.myqcloud.com/static/video/test.mp3" });
```

### audioContext.play()
播放音频。

### audioContext.pause()
暂停播放。

### audioContext.stop()
停止播放。

### audioContext.mute()
静音。

### audioContext.unmute()
解除静音。

### audioContext.seek({ time: xxx })
**功能描述：**跳转到指定的播放时间。

**参数：**

| 参数名称 | 参数类型  | 必填 | 参数描述 |
| --- | --- | --- | --- |
| time | Number | 是 | 需要跳转的指定播放时间。单位为 ms（毫秒） |

```plaintext
audioContext.seek({ time: 10 * 1000 });
```


### audioContext.getSrc()
获取当前音频链接。

### audioContext.getPlaytime()
获取当前音频的播放时间点，单位 ms（毫秒）。

### audioContext.getDuration()
获取当前播放段的时长，单位 ms（毫秒）。

### audioContext.getVolume()
获取当前音量，约定取值范围是[0,1]，如果为0则是静音状态（muted）。

### audioContext.getMutedVolume()
获取静音前的音量。
