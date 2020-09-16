

## iOS 音频相关接口

此部分接口使用 SetAdvanceParams 接口进行调用，在进房前调用。 
```
[[ITMGContext GetInstance] SetAdvanceParams:keyString value:_value]
```

| 参数      | 含义                             |
| --------- | -------------------------------- |
| keyString | 不同的 Key 代表不同的功能        |
| value     |<li> 0：代表关闭<li>1：代表开启 |

### Key 
不同的 Key 代表不同的功能，参数 Key 可填写的字段如下：
- **OptionMixWithOthers**
混音选项。开启后可以把后台播放的音乐与前台通话语音同时播放。

- **OptionDuckOthers**
压低背景音。在 OptionMixWithOthers 开启的情况下，如果开启此功能，则开启扬声器播放语音时，将会压低其他后台背景声音。

- **ReleaseAudioFoucus**
释放音频焦点。
 -  如果开启，退房之后将会释放音频焦点，系统恢复后台其他音频相关应用。例如 QQ 音乐。
 - 如果关闭，退房之后将不会恢复其他音频相关应用。
