通过 `audioContext.on('event-name', callbackFunction)` 方法去监听 AudioContext 的回调事件。例如：
```plaintext
audioContext.on('on-play', (res) => {
    console.info(res);
});
audioContext.on('on-loaded-metadata', (res) => {
    console.info(res);
});
audioContext.on('on-ended', (res) => {
    console.info(res);
});
```

## 播放器事件列表（TmAudioPlayEvent）
### on-play
播放事件回调。

### on-pause
暂停事件回调。

### on-waiting
视频加载中事件回调。

### on-loaded-metadata
**事件描述：**视频信息事件回调。

**回调参数：**

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| width | Number | 视频内容宽 pixel。 |
| height | Number | 视频内容高 pixel。 |
| duration | Number | 媒体时长 ms（毫秒）。 |

### on-error
**事件描述：**播放错误事件回调。

**回调参数：**

| 参数名称 | 参数类型 | 
| --- | --- | 
| type | Number | 
| code | Number | 
| arg1 | Number | 
| arg2 | Number | 

### on-ended
播放完毕事件回调。

### on-time-update
**事件描述：**播放进度事件回调。

**回调参数：**

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| currentTime | Number | 当前进度 ms（毫秒）。 |
| duration | Number | 媒体时长 ms（毫秒）。 |

### on-seek
**事件描述：**跳转到指定的播放时间点事件回调。

**回调参数：**

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| to | Number | 完成 seek 的进度 ms（毫秒）。 |
