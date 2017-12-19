### 构造函数

```
qcVideo.Player(id, option, listener);
```

 **ID**：String，必选参数，页面放置播放器的容器 ID，可以自由定义；
  **option**：Object，必选参数，播放器的参数可设置选项，具体选项：

| 参数             | 类型   | 默认值 | 参数说明   |
|------------------|--------|--------|---------------------------------------------------------------------------------------------------|
| channel_id      | String | 无     | 用直播视频 ID 播放方式为必选参数                                                                    |
| app_id          | String | 无     | 条件同上为必选参数，同一个账户下的视频，该参数是相同的                                            |
| width            | Number | 无     | 必选，例如：640，设置播放器宽度，单位为像素                                                       |
| height           | Number | 无     | 必选，例如：480，设置播放器高度，单位为像素                                                       |
| cache_time      | Number | 0.3    | 直播画面开始播放前，最大缓存时间；这个属性可避免有效下行带宽不足导致免 rtmp 直播卡顿的情况（可选参数）<br> 备注：该选项只对 PC 平台 Flash 播放器生效 |
| h5_start_patch | Object | 无     | H5 播放，开始播放前贴片（可选参数）<br>{ <br>url : 图片地址, <br>stretch: false //是否拉伸图片铺面整个播放器，默认 false<br>}                                                                                                  |
| wording          | Object | 无     | 直播提示语自定义（可选参数，详细信息可见 [错误码](#errorcode)）<br>{	<br>	'1' 	: '数据库错误',<br> '2'		: '连接不到直播源，直播源没有推送视频内容(hls)',<br> '3'		: '直播已经结束啦(hls)',<br>'113'	: '连接超时，请稍后再试',<br>'114'	: '连接超时，请稍后再试',<br>'1000'	: 'channelID 或者 APPID 错误',<br>'1001'	: '无效参数，获取 bizid 失败',<br>'1009'	: '直播源已失效',<br>'10000'	: '请求超时，请检查网络设置',<br> '10008'	: '密码错误，请重新输入', //无效密码<br>'10020'	: '直播账户余额已不足，请及时充值',  <br>'11044'	: '无效请求',<br> '11045'	: '请求参数缺少 channelID',<br> '11046'	: '密码错误，请重新输入',<br> '20110'	: '密码错误，请重新输入',<br>'20113'	: '直播已经结束啦，请稍后再来' , //'downstream type is not exist' 拉流不存在<br>'20201'	: '直播已经结束啦，请稍后再来', //get upstream info error'  查询推流错误<br> '20301'	: '直播频道不存在，请确认频道 ID',<br>'TipReconnect'	: '重新连接中'<br>'TipRequireSafari'	: '当前浏览器不能支持视频播放，请使用 safari 打开观看'<br>'TipRequireFlash'	: '当前浏览器不能支持视频播放，可下载最新的 QQ 浏览器或者安装 Flash 即可播放'<br>'TipVideoinfoResolveError'	: '视频信息解析错误，请检查参数是否正确', //接口没有返回 json 数据，无法解析<br>'TipVideoinfoError'	: '视频信息错误，请检查参数是否正确',<br>'TipConnectError'	: '连接服务失败，请检查网络设置',<br>'TipConnectDeny'	: '连接服务被拒绝', //Flash 请求触发安全异常<br>'TipLiveEnd'		: '直播已经结束啦，请稍后再来',  // NetStream.Play.Stop 事件, <br>'TipStreamNotFound'	: '直播已经结束啦，请稍后再来' //连接不到直播源，直播源没有推送视频内容<br>}                                                                                                 |
| live_url        | String | 无     | 直播地址，支持 hls/rtmp/flv 三种格式<br>用视频地址播放方式为必选参数                                                                      |
| live_url2       | String | 无     | 直播地址，同上（可选参数）                                                                        |
| volume           | Number | 0.5    | 设置音量初始值 0 到 1，默认 0.5（可选参数）备注：该选项只对 Flash 播放器生效                                                                    |
| https             | Number | 0   | 设置对播放页的 https 支持，0：关闭，1：开启                                                                    |
| hide_volume_tips  | Number | 0   | 是否隐藏音量提示，0：显示，1：隐藏 <br>备注：该选项只对 Flash 播放器生效                                                                   |
| x5_type           | String | 无   | 通过 video 属性“x5-video-player-type”声明启用同层 H5 播放器，支持的值：H5 （该属性为 TBS 内核实验性属性，非 TBS 内核不支持，具体介绍参照 [TBS 文档](http://x5.tencent.com/guide?id=4000) ）                           |
| x5_fullscreen     | String | 无   | 视频播放时将会进入到全屏模式，支持的值： true：开启（该属性为 TBS 内核实验性属性，非 TBS 内核不支持，具体介绍参照 [TBS 文档](http://x5.tencent.com/guide?id=4000)）                                                   |
| WMode             | String  | window | Window 模式不支持其他页面元素覆盖在 Flash 播放器上面，如需要可以修改为 opaque 或其他 flash wmode 的参数值，可以在 Flash 播放器上进行覆盖其他元素。<br> 备注：该选项只对 PC 平台 Flash 播放器生效                                                                  |

**listener**：Object，可选参数，播放状态变化回调函数列表。

| 函数名称                                                 | 类型     | 说明   |
|----------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| playStatus<span id="playstatus" class="anchor"></span> | function | 播放状态变更时触发，回调函数的参数 status：String <br>返回值：<br>ready: “播放器已准备就绪”, playing:”播放中” , playEnd:”播放结束” , error: “播放异常结束或者遇到错误” //由于移动端播放事件触发条件不一致，如果监听播放结束事件建议同时监听error，以免回调不能正确执行。  <br>type：String 在遇到error时返回错误类型 <br>例子：function(status, type){ ... }   |

### 设置和动作

构造函数返回的播放器对象具有以下设置方法

| 方法                 | 说明                          |
|----------------------|-------------------------------|
| resize(width,height) | 参数：width：int；height：int <br>功能：设置当前播放器宽度高度<br>返回：无                       |
| play()                                                  | 功能：开始播放<br>返回：int（统一返回码）<br>备注：该功能仅 PC 端 Flash 播放器支持                                                           |
| stop()                                                  | 功能：停止播放<br>返回：int（统一返回码）<br>备注：该功能仅 PC 端 Flash 播放器支持                                                                    |
| pause()                                                       | 功能：暂停当前播放的视频 <br>返回：int（统一返回码)<br>备注：该功能仅 PC 端 Flash 播放器支持>                                                                                   |
| resume()                                                      | 功能：恢复播放视频<br>返回：int（统一返回码）<br>备注：该功能仅 PC 端 Flash 播放器支持       |
| addBarrage(barrage) | 参数：barrage://Array 弹幕信息   <br> \[{   <br>"type":"content", //消息类型，content：普通文本（必选）  <br>"content":"hello world", //文本消息（必选） <br>"time":"1.101",//单位秒 ，表示距离当前调用添加字幕的时间多久后，开始显示该条字幕（必选）   <br>"style": "C64B03;35",// 分号分割，第一项颜色值，第二项字体大小（可选）<br>"postion":"center" //固定位置 <br>center: 居中，bottom: 底部， up: 顶上 (可选) }, ... \]  <br>功能：添加弹幕     <br>返回：int [返回码](#errorcode) <br> 备注：弹幕仅在前端实现，后台功能请自行开发。该功能只在 PC Flash 播放器中生效                                                                                 |
| closeBarrage()                                                | 功能：关闭弹幕，关闭后重新调用 addBarrage 可开启弹幕。 <br>返回：int [返回码](#errorcode)  <br> 备注：弹幕仅在前端实现，后台功能请自行开发，该功能只在 PC Flash 播放器中生效                                                                                     |

这些设置方法的统一返回码是：
  
| 错误码<span id="errorcode"></span> | 含义 |
|---------|---------|
| 200 | 操作成功 | 
| 0  | 播放器未完全初始化 | 
| -2 | 未知操作命令 | 
