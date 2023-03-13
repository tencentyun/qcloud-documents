# InnerAudioContext

InnerAudioContext 实例，可通过 [wx.createInnerAudioContext](./createInnerAudioContext.md) 接口获取实例。

#### 属性

##### string src

音频资源的地址，用于直接播放。支持云文件ID

##### number startTime

开始播放的位置（单位：s），默认为 0

##### boolean autoplay

是否自动开始播放，默认为 `false`

##### boolean loop

是否循环播放，默认为 `false`


##### number volume


音量。范围 0-1。默认为 1

##### number duration

当前音频的长度（单位 s）。只有在当前有合法的 src 时返回（只读）

##### number currentTime

当前音频的播放位置（单位 s）。只有在当前有合法的 src 时返回，时间保留小数点后 6 位（只读）

##### boolean paused

当前是否是暂停或停止状态（只读）

##### number buffered

音频缓冲的时间点，仅保证当前播放时间点到此时间点内容已缓冲（只读）

#### 方法

##### [InnerAudioContext.play()](#.play)

播放

##### [InnerAudioContext.pause()](#.pause)

暂停。暂停后的音频再播放会从暂停处开始播放

##### [InnerAudioContext.stop()](#.stop)

停止。停止后的音频再播放会从头开始播放。

##### [InnerAudioContext.seek(number position)](#.seek)

跳转到指定位置

##### [InnerAudioContext.destroy()](#.destroy)

销毁当前实例

##### [InnerAudioContext.onCanplay(function callback)](#.onCanplay)

监听音频进入可以播放状态的事件。但不保证后面可以流畅播放

##### [InnerAudioContext.offCanplay(function callback)](#.offCanplay)

取消监听音频进入可以播放状态的事件

##### [InnerAudioContext.onPlay(function callback)](#.onPlay)

监听音频播放事件

##### [InnerAudioContext.offPlay(function callback)](#.offPlay)

取消监听音频播放事件

##### [InnerAudioContext.onPause(function callback)](#.onPause)

监听音频暂停事件

##### [InnerAudioContext.offPause(function callback)](#.offPause)

取消监听音频暂停事件

##### [InnerAudioContext.onStop(function callback)](#.onStop)

监听音频停止事件

##### [InnerAudioContext.offStop(function callback)](#.offStop)

取消监听音频停止事件

##### [InnerAudioContext.onEnded(function callback)](#.onEnded)

监听音频自然播放至结束的事件

##### [InnerAudioContext.offEnded(function callback)](#.offEnded)

取消监听音频自然播放至结束的事件

##### [InnerAudioContext.onTimeUpdate(function callback)](#.onTimeUpdate)

监听音频播放进度更新事件

##### [InnerAudioContext.offTimeUpdate(function callback)](#.offTimeUpdate)

取消监听音频播放进度更新事件

##### [InnerAudioContext.onError(function callback)](#.onError)

监听音频播放错误事件

##### [InnerAudioContext.offError(function callback)](#.offError)

取消监听音频播放错误事件

##### [InnerAudioContext.onWaiting(function callback)](#.onWaiting)

监听音频加载中事件。当音频因为数据不足，需要停下来加载时会触发

##### [InnerAudioContext.offWaiting(function callback)](#.offWaiting)

取消监听音频加载中事件

##### [InnerAudioContext.onSeeking(function callback)](#.onSeeking)

监听音频进行跳转操作的事件

##### [InnerAudioContext.offSeeking(function callback)](#.offSeeking)

取消监听音频进行跳转操作的事件

##### [InnerAudioContext.onSeeked(function callback)](#.onSeeked)

监听音频完成跳转操作的事件

##### [InnerAudioContext.offSeeked(function callback)](#.offSeeked)

取消监听音频完成跳转操作的事件

#### 支持格式

格式   | iOS | Android
---- | --- | -------
flac | x   | √      
m4a  | √   | √      
ogg  | x   | √      
ape  | x   | √      
amr  | x   | √      
wma  | x   | √      
wav  | √   | √      
mp3  | √   | √      
mp4  | x   | √      
aac  | √   | √      
aiff | √   | x      
caf  | √   | x      

#### 示例代码

```js
const innerAudioContext = wx.createInnerAudioContext()
innerAudioContext.autoplay = true
innerAudioContext.src = 'https://ws.stream.qqmusic.qq.com/M500001VfvsJ21xFqb.mp3?guid=ffffffff82def4af4b12b3cd9337d5e7&uin=346897220&vkey=6292F51E1E384E061FF02C31F716658E5C81F5594D561F2E88B854E81CAAB7806D5E4F103E55D33C16F3FAC506D1AB172DE8600B37E43FAD&fromtag=46'
innerAudioContext.onPlay(() => {
  console.log('开始播放')
})
innerAudioContext.onError((res) => {
  console.log(res.errMsg)
  console.log(res.errCode)
})
```

### .destroy

#### InnerAudioContext.destroy()

销毁当前实例

### .offCanplay

#### InnerAudioContext.offCanplay(function callback)


取消监听音频进入可以播放状态的事件

#### 参数

##### function callback

音频进入可以播放状态的事件的回调函数

### .offEnded

#### InnerAudioContext.offEnded(function callback)


取消监听音频自然播放至结束的事件

#### 参数

##### function callback

音频自然播放至结束的事件的回调函数

### .offError

#### InnerAudioContext.offError(function callback)


取消监听音频播放错误事件

#### 参数

##### function callback

音频播放错误事件的回调函数

### .offPause

#### InnerAudioContext.offPause(function callback)


取消监听音频暂停事件

#### 参数

##### function callback

音频暂停事件的回调函数

### .offPlay

#### InnerAudioContext.offPlay(function callback)


取消监听音频播放事件

#### 参数

##### function callback

音频播放事件的回调函数

### .offSeeked

#### InnerAudioContext.offSeeked(function callback)


取消监听音频完成跳转操作的事件

#### 参数

##### function callback

音频完成跳转操作的事件的回调函数

### .offSeeking

#### InnerAudioContext.offSeeking(function callback)


取消监听音频进行跳转操作的事件

#### 参数

##### function callback

音频进行跳转操作的事件的回调函数

### .offStop

#### InnerAudioContext.offStop(function callback)


取消监听音频停止事件

#### 参数

##### function callback

音频停止事件的回调函数

### .offTimeUpdate

#### InnerAudioContext.offTimeUpdate(function callback)


取消监听音频播放进度更新事件

#### 参数

##### function callback

音频播放进度更新事件的回调函数

### .offWaiting

#### InnerAudioContext.offWaiting(function callback)


取消监听音频加载中事件

#### 参数

##### function callback

音频加载中事件的回调函数

### .onCanplay

#### InnerAudioContext.onCanplay(function callback)

监听音频进入可以播放状态的事件。但不保证后面可以流畅播放

#### 参数

##### function callback

音频进入可以播放状态的事件的回调函数

### .onEnded

#### InnerAudioContext.onEnded(function callback)

监听音频自然播放至结束的事件

#### 参数

##### function callback

音频自然播放至结束的事件的回调函数

### .onError

#### InnerAudioContext.onError(function callback)

监听音频播放错误事件

#### 参数

##### function callback

音频播放错误事件的回调函数

###### 参数

**Object res**

属性      | 类型     | 说明
------- | ------ | --
errCode | number |   

**errCode 的合法值**

值     | 说明  
----- | ----
10001 | 系统错误
10002 | 网络错误
10003 | 文件错误
10004 | 格式错误
-1    | 未知错误

### .onPause

#### InnerAudioContext.onPause(function callback)

监听音频暂停事件

#### 参数

##### function callback

音频暂停事件的回调函数

### .onPlay

#### InnerAudioContext.onPlay(function callback)

监听音频播放事件

#### 参数

##### function callback

音频播放事件的回调函数

### .onSeeked

#### InnerAudioContext.onSeeked(function callback)

监听音频完成跳转操作的事件

#### 参数

##### function callback

音频完成跳转操作的事件的回调函数

### .onSeeking

#### InnerAudioContext.onSeeking(function callback)

监听音频进行跳转操作的事件

#### 参数

##### function callback

音频进行跳转操作的事件的回调函数

### .onStop

#### InnerAudioContext.onStop(function callback)

监听音频停止事件

#### 参数

##### function callback

音频停止事件的回调函数

### .onTimeUpdate

#### InnerAudioContext.onTimeUpdate(function callback)

监听音频播放进度更新事件

#### 参数

##### function callback

音频播放进度更新事件的回调函数

### .onWaiting

#### InnerAudioContext.onWaiting(function callback)

监听音频加载中事件。当音频因为数据不足，需要停下来加载时会触发

#### 参数

##### function callback

音频加载中事件的回调函数

### .pause

#### InnerAudioContext.pause()

暂停。暂停后的音频再播放会从暂停处开始播放

### .play

#### InnerAudioContext.play()

播放

### .seek

#### InnerAudioContext.seek(number position)

跳转到指定位置

#### 参数

##### number position

跳转的时间，单位 s。精确到小数点后 3 位，即支持 ms 级别精确度

### .stop

#### InnerAudioContext.stop()

停止。停止后的音频再播放会从头开始播放。
