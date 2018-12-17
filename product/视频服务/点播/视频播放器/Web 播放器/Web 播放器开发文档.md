## 前言
本文档介绍腾讯云视频点播服务的 Web 播放器的相关参数以及 API，需结合 [《使用文档》](https://cloud.tencent.com/document/product/266/14424) 使用。本文档适合有一定 Javascript 语言基础的开发人员阅读。

## 初始化参数
播放器初始化需要传入两个参数，第一个为播放器容器 ID，第二个为功能参数对象。
```
var player = TCPlayer('player-container-id', options);
```

### options 参数列表
options 对象可配置的参数：

| 名称    | 类型                      | 默认值                        |说明 |
|------------|-----------------------------------|-----------------------------------|---------------------------------------|
|  appID|  String |   无 |必选|
|  fileID|  String|无|必选|  
|  width|  String / Number|  无| 播放器区域宽度，单位像素，按需设置，可通过 CSS 控制播放器尺寸。|
|  height |  String /Number|  无|  播放器区域高度，单位像素，按需设置，可通过 CSS 控制播放器尺寸。|  
|  controls|  Boolean|  true|  是否显示播放器的控制栏|  
|  poster|  String|  无|  设置封面图片完整地址|  
|  autoplay|  Boolean|  false|  是否自动播放|  
|  playbackRates|  Array| [0.5, 1, 1.25, 1.5, 2]|  设置变速播放倍率选项，仅 H5 有效|  
|  loop|Boolean|  false|  是否循环播放|  
|  muted|  Boolean|  false|  是否静音播放|  
|  preload|  String|  auto|  是否需要预加载，有 3 个属性"auto"，"meta"，"none" ，移动端由于系统限制，设置 auto 无效。|  
|  swf|  String|  无|  Flash 播放器 swf 文件的 URL|  
|  posterImage|  Boolean|  true|  是否显示封面|  
|  bigPlayButton|  Boolean|  true|  是否显示居中的播放按钮（浏览器劫持嵌入的播放按钮无法去除）|  
|  language|  String|  "zh-CN"|  设置语言|  
|  languages|  Object|  无|  设置多语言词典|  
|  controlBar|  Object|  无|  设置控制栏属性的参数组合，后面有详细介绍|  
|  plugins|  Object|  无|  设置插件功能属性的参数组合，后面有详细介绍|  
|  hlsConfig|  Object|  无|  hls.js 的启动配置，详细内容请看官方文档 [hls.js](https://github.com/video-dev/hls.js/blob/master/docs/API.md#fine-tuning)|  

#### controlBar 参数列表
controlBar 参数可以配置播放器控制栏的功能，支持的属性有：

| 名称    | 类型                      | 默认值                        |说明 |
|------------|-----------------------------------|-----------------------------------|---------------------------------------|
|  playToggle| Boolean|  true|  是否显示播放、暂停切换按钮|  
|  progressControl|  Boolean| true|  是否显示播放进度条|  
|  volumePanel|  Boolean|  true|  是否显示音量控制|  
|  currentTimeDisplay|  Boolean|  true|  是否显示视频当前时间|  
|  durationDisplay|  Boolean|  true|  是否显示视频时长|  
|  timeDivider|  Boolean|  true|  是否显示时间分割符|  
|  playbackRateMenuButton|  Boolean|  true|  是否显示播放速率选择按钮|  
|  fullscreenToggle|  Boolean|  true|  是否显示全屏按钮|  
|  QualitySwitcherMenuButton|  Boolean|  true|  是否显示清晰度切换菜单|  

>**注意事项：**
> * controlBar 参数在浏览器劫持播放的状态下将无效。[什么是劫持播放？](https://cloud.tencent.com/document/product/266/1303#.E6.B5.8F.E8.A7.88.E5.99.A8.E5.8A.AB.E6.8C.81.E8.A7.86.E9.A2.91.E6.92.AD.E6.94.BE)

#### plugins 插件参数列表
plugins 参数可以配置播放器插件的功能，支持的属性有：

| 名称    | 类型                      | 默认值                        |说明 |
|------------|-----------------------------------|-----------------------------------|---------------------------------------|
|  ContinuePlay|  Object|  无|  控制续播功能，支持的属性如下<br>auto: false, // 是否在播放时自动续播 <br>text: '上次看到 ', // 提示文案<br>btnText: '恢复播放' // 按钮文案<br>

## 对象方法
初始化播放器返回对象的方法列表：

| 名称    | 参数及类型                 | 返回值及类型                        |说明 |
|------------|-----------------------------------|-----------------------------------|---------------------------------------|
|  ready(function)|  (Function)|  无|  设置播放器初始化完成后的回调|  
|  play()|  无|  无|  播放以及恢复播放|  
|  pause()|  无|  无|  暂停播放|  
|  currentTime(seconds)|  (Number)|  (Number)|  获取当前播放时间点，或者设置播放时间点，该时间点不能超过视频时长|  
|  duration()|  无|  (Number)|  获取视频时长|  
|  volume(percent)|  (Number)[0,1][可选]|  (Number) / 设置时无返回|  获取或设置播放器音量|
|  poster(src)|  (String)|  (String) / 设置时无返回|  获取或设置播放器封面|
|  requestFullscreen()|  无|  无|  进入全屏模式|  
|  exitFullscreen()|  无|  无|  退出全屏模式|  
|  isFullscreen()|  无|  Boolean|  返回是否进入了全屏模式|  
|  on(type，listerner)|  (String, Function)|  无|  监听事件|  
|  one(type，listerner)|  (String, Function)|  无|  监听事件，事件处理函数最多只执行 1 次|  
|  off(type，listerner)|  (String, Function)|  无|  解绑事件监听|  
|  buffered()|  无|  TimeRanges|  返回视频缓冲区间|  
|  bufferedPercent()|  无|  值范围[0,1]|  返回缓冲长度占视频时长的百分比|  
|  width()|  (Number)[可选]|  (Number) / 设置时无返回|  获取或设置播放器区域宽度，如果通过 CSS 设置播放器尺寸，该方法将无效|
|  height()|  (Number)[可选]|  (Number) / 设置时无返回|  获取或设置播放器区域高度，如果通过 CSS 设置播放器尺寸，该方法将无效|
|  videoWidth()|  无|  (Number)|  获取视频分辨率的宽度|  
|  videoHeight()|  无|  (Number)|  获取视频分辨率的高度|  
|  dispose()|  无|  无|  销毁播放器|  

>**注意事项：**
> * 对象方法不能同步调用，需要在相应的事件（例如 loadedmetadata ）触发后才可以调用，除了ready、on、one、off。

## 事件
播放器可以通过初始化返回的对象进行事件监听，示例：
```
var player = TCPlayer('player-container-id', options);
player.on(type, function);
```
其中 type 为事件类型，支持的事件有：

| 名称    | 介绍                    |  
|------------|---------------------------------|
|  play|  已经开始播放，调用 play() 方法或者设置了 autuplay 为 true 且生效时触发，这时 paused 属性为 false|  
|  playing|  因缓冲而暂停或停止后恢复播放时触发，paused 属性为 false 。通常用这个事件来标记视频真正播放，play 事件只是开始播放，画面并没有开始渲染|  
|  loadstart|  开始加载数据时触发|  
|  durationchange|  视频的时长数据发生变化时触发|  
|  loadedmetadata|  已加载视频的 metadata|  
|  loadeddata|  当前帧的数据已加载，但没有足够的数据来播放视频的下一帧时，触发该事件|  
|  progress|  在获取到媒体数据时触发|  
|  canplay|  当播放器能够开始播放视频时触发|  
|  canplaythrough|  当播放器预计能够在不停下来进行缓冲的情况下持续播放指定的视频时触发|
|  error|  视频播放出现错误时触发|  
|  pause|  暂停时触发|  
|  ratechange|  播放速率变更时触发|  
|  seeked|  搜寻指定播放位置结束时触发|  
|  seeking|  搜寻指定播放位置开始时触发|  
|  timeupdate|  当前播放位置有变更，可以理解为 currentTime 有变更|  
|  volumechange|  设置音量或者 muted 属性值变更时触发|  
|  waiting|  播放停止，下一帧内容不可用时触发|  
|  ended|  视频播放已结束时触发。此时 currentTime 值等于媒体资源最大值|  
|  resolutionswitching|  清晰度切换进行中|  
|  resolutionswitched|  清晰度切换完毕|  
|  fullscreenchange| 全屏状态切换时触发|

## 错误码
当播放器触发 error 事件时，监听函数会返回错误码。错误码列表：

| 名称    | 介绍                    |  
|------------|---------------------------------|
|  -1|  没有视频地址|  
|  -2|  获取视频数据超时|  
|  1|  视频加载播放被中断|  
|  2|  由于网络问题造成加载视频失败|  
|  3|  解码时发生错误|  
|  4|  视频因格式不支持或者服务器或网络的问题无法加载|  
|  5|  解密时发生错误|  
|  10|  点播服务接口请求超时|  
|  11|  点播服务接口没有响应|  
|  12|  点播服务接口返回异常数据|  
|  13|  点播视频没有转码，需在点播控制台进行转码|
|  14|  HTML5 + hls.js 模式下播放 hls 出现网络异常，异常详情可在 event.source 中查看，详细介绍请看 hls.js 的官方文档 [Network Errors](https://github.com/video-dev/hls.js/blob/master/docs/API.md#network-errors)|  
|  15|  HTML5 + hls.js 模式下播放 hls 出现多媒体异常，异常详情可在 event.source 中查看，详细介绍请看 hls.js 的官方文档 [Media Errors](https://github.com/video-dev/hls.js/blob/master/docs/API.md#media-errors)|  
|  16|  HTML5 + hls.js 模式下播放 hls 出现多路复用异常，异常详情可在 event.source 中查看，详细介绍请看 hls.js 的官方文档 [Mux Errors](https://github.com/video-dev/hls.js/blob/master/docs/API.md#mux-errors)|  
|  17|  HTML5 + hls.js 模式下播放 hls 出现其他异常，异常详情可在 event.source 中查看，详细介绍请看 hls.js 的官方文档 [Other Errors](https://github.com/video-dev/hls.js/blob/master/docs/API.md#other-errors)|  
