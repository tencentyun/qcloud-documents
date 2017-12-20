### 构造函数
```
qcVideo.Player(id, option, listener);
```

**ID**：String，必选参数，<span id="constructor"></span>页面放置播放器的容器 ID，可以自由定义；
**option**：Object，必选参数。
播放器的参数设置选项，具体选项有：

| 参数                                                   | 类型    | 默认值 | 参数说明                                                                                                                                                                                        |
|--------------------------------------------------------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| file_id                                               | String  | 无     | 用视频 ID 播放方式为必选参数，为该点播文件的唯一标识                                                                                                                                              |
| app_id                                                | String  | 无     | 条件同上为必选参数，同一个账户下的视频，该参数是相同的                                                                                                                                          |
| width                                                  | Number  | 无     | 必选，例如：640，设置播放器宽度，单位为像素                                                                                                                                                     |
| height                                                 | Number  | 无     | 必选，例如：480，设置播放器高度，单位为像素                                                                                                                                                     |
| auto_play                                             | Number  | 0      | 是否自动播放，0：不自动，1：自动播放  <br>备注：该选项只对 PC 平台 Flash 播放器生效                                                                                                                                                    |
| disable_full_screen                                  | Number  | 0      | 是否允许全屏播放，0：支持全屏播放，1：禁用全屏播放       <br>备注：该选项只对 PC 平台 Flash 播放器生效                                                                                                                                          |
| disable_drag                                          | Number  | 0      | 是否允许拖动时间轴，0：允许拖拽，1：禁止拖拽         <br> 备注：该选项只对 PC 平台 Flash 播放器生效                                                                                                                                              |
| stretch_full                                          | Number  | 0      | 是否等比拉伸视频至铺满播放器0：不拉伸，1：拉伸全屏          <br> 备注：该选项只对 PC 平台 Flash 播放器生效                                                                                                                                       |
| stop_time                                             | Number  | 无     | 试看功能，例如设置：60，60秒后停止播放，并且触发“playStatus”事件                                                                                                                                |
| remember                                               | Number  | 0      | 是否开启续播功能，0：关闭，1：开启，开启后将会记录这个视频上一次未看完的时间点，下一次继续播放。   <br> 备注：该选项只对 PC 平台 Flash 播放器生效                                                                                              |
| playbackRate                                           | Number  | 1      | 变速播放，例如设置 2 表示 2 倍速度播放，0.5 表示慢正常速度一倍播放。      <br> 备注：该选项暂时只对 H5 播放器生效                                                                                              |
| hide_h5_setting                                      | Boolean | false  | 是否隐藏 H5 的设置按钮，true：隐藏，false：不隐藏                                                                                                                                                 |
| hide_h5_error                                        | Boolean | false  | 是否隐藏 H5 的错误提示， <br> 备注：该选项暂时只对 H5 播放器生效                                                                                                                                              |
| WMode                                                  | String  | window | Window 模式不支持其他页面元素覆盖在 Flash 播放器上面，如需要可以修改为 opaque 或其他 flash wmode 的参数值。<br> 备注：该选项只对 PC 平台 Flash 播放器生效                                                                  |
| stretch_patch                                         | Boolean | false  | 设置为 true 时，支持将开始、暂停、结束时的图片贴片铺满播放器。                                                                                                                                    |
| definition<span id="definition"></span> | Number  | 无     | 可以指定播放视频的清晰度，首先需要视频拥有改清晰度 可选值有： 10、20、30、40、210、220、230、240，具体对应哪种视频可以参考 [third_video](#third_video) 的参数说明。                                                                             |
| videos                                                 | Array   | 无     | 开启防盗链后，可以通过设置 videos 的可访问的视频地址，支持播放器播放；清晰度类型通过 url 与后台查出的 url 前缀匹配得到，详情请查看 [防盗链功能使用指南](https://cloud.tencent.com/doc/product/266/2875)<br> 例如：[`http://xxx.myqcloud.com/xxxyy\_f220.m3u8?**sign**=xxx`，<br>...<br>]                                                                                                                                                                                               |
| third\_video <span id="third_video"></span>                  | Object  | 无     | 该选项只用于视频文件播放地址的情形<br>参数例子：{<br>‘duration’: 20 , //视频时长（单位秒），可选参数，没有传的情况下在视频加载 MetaData 后自动更新视频时长。<br>注意：如果是播放 mp4，这个时长数据是必须的<br>‘urls’ : { //(至少包含一个地址，注意对应视频格式)  <br>　　　10 : “mp4 手机视频地址”, <br>　　　20 :“mp4 标清视频地址”,<br>　　　30 : “mp4 高清视频地址”, <br>　　　40 : “mp4 超清视频地址”, <br>　　　210 : “hls 手机视频地址”, <br>　　　220 : “hls 标清视频地址”, <br>　　　230 :“hls 高清视频地址”, <br>　　　240 : “hls 超清视频地址” <br>　　}<br>}<br>备注：如果在 Chrome 等 PC 浏览器中模拟移动设备，需要有 mp4 视频地址才可以播放|

**listener**：Object，可选参数，播放状态变化回调函数列表。

| 函数名称                                                 | 类型     | 说明   |
|----------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| fullScreen                                               | function | 全屏/退出全屏时触发，回调函数的参数 isFullScreen：Boolean <br>返回值： true全屏，false 退出全屏 <br>例子：```function(isFullScreen){ ... }```  <br>备注：该事件只对 PC 平台 Flash 播放器生效  |
| playStatus<span id="playstatus" class="anchor"></span> | function | 播放状态变更时触发，回调函数的参数 status：String <br>返回值：ready：“播放器已准备就绪”，seeking：“搜索”，suspended：“暂停”，playing：“播放中” ， playEnd：“播放结束”，stop：“试看结束触发” ，error：“H5 播放出现错误时触发”  <br>例子：function(status, msg){ ... }   |
| dragPlay                                                 | function | 拖动播放位置变化时触发 ；second：Number  <br>返回值：拖动播放的位置（单位秒） <br>例子： ```function(second){ ... }```  <br> 备注：该事件只对 PC 平台 Flash 播放器生效    |


### 获取参数和状态

构造函数返回的播放器对象具有以下获取参数和状态的方法：

|   方法名              |         返回值                                                   |       说明                       |
|----------------|------------------------------------------------------------|-----------------------------|
| getVolume      | Number，取值范围（0 到 1）                                 | 获取当前音量                |
| getDuration    | Number，单位秒                                             | 获取当前视频总时长          |
| getCurrentTime | Number，单位秒                                             | 获取当前播放位置            |
| isSeeking      | Boolean，true 为”加载中”                                  | 当前播放状态是否 “加载中”   |
| isSuspended    | Boolean，true 为”暂停中”                                  | 当前播放状态是否 “暂停中”   |
| isPlaying      | Boolean，true 为”播放中”                                  | 当前播放状态是否 “播放中”   |
| isPlayEnd      | Boolean，true 为”播放结束”                                | 当前播放状态是否 “播放结束” |
| getWidth       | Number(int)                                                | 获取当前播放器宽度          |
| getHeight      | Number(int)                                                | 获取当前播放器高度          |
| getClarity     | Number(int) ( 1:”手机”, 2:“标清”, 3:“高清”, 4:“超清”)      | 获取当前视频的清晰度        |
| getAllClaritys | Array&lt;int&gt; ( 1:”手机”, 2:“标清”, 3:“高清”, 4:“超清”) | 获取当前视频全部的清晰度    |

### 设置和动作

构造函数返回的播放器对象具有以下设置方法：

| 方法                                                          | 说明                                                                                                                 |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| resize(width,height)                                          | 参数：width :int；height :int                                            <br>功能：设置当前播放器宽度高度                                         <br>返回：无                                                                                                              |
| play(second)                                                  | 参数：second：int 单位秒                                                  <br>功能：开始播放，可以设置开始播放指定时间点 <br>返回：int [返回码](#errorcode)<br>备注：在传视频地址播放的情况下，second 只能传 空值 或者 0                                                               |
| pause()                                                       | 功能：暂停当前播放的视频 <br>返回：int [返回码](#errorcode)                                                                                     |
| resume()                                                      | 功能：恢复播放视频<br>返回：int [返回码](#errorcode)                                                                                     |
| setClarity(clarity)                                           | 参数：clarity：int 清晰度 取值范围 （1：”手机”，2：”标清”，3：”高清”，4：”超清”）<br>功能：更换视频清晰度 <br>返回：int [返回码](#errorcode)                            <br>注意：clarity 指定的清晰度，请确保当前视频具备该清晰度，否则将按播放器默认规则选择一个清晰度播放                       |
| changeVideo(opt)                                              | 参数： opt Object，包含将要播放的视频的基本信息和构造函数第二个参数基本一致，具体参考 [构造函数说明](#constructor)<br>功能：动态更换视频  <br>返回：int [返回码](#errorcode) |
| addBarrage(barrage) <span id="barrage"></span>| 参数：barrage：Array 弹幕信息   <br> \[{   <br>"type":"content", //消息类型，content:普通文本（必选）  <br>"content":"hello world", //文本消息 （必选）  <br>"time":"1.101",//单位秒 ，表示距离当前调用添加字幕的时间多久后，开始显示该条字幕（必选）   <br>"style": "C64B03;35",// 分号分割，第一项颜色值，第二项字体大小（可选） <br>"postion":"center" //固定位置 <br>center: 居中，bottom: 底部， up: 顶上 (可选) }, ... \]  <br>功能：添加弹幕     <br>返回：int [返回码](#errorcode) <br> 备注：弹幕仅在前端实现，后台功能请自行开发，该功能只在 PC Flash 播放器中生效                                                                                |
| closeBarrage()                                                | 功能：关闭弹幕，关闭后重新调用 addBarrage 可开启弹幕。 <br>返回：int [返回码](#errorcode)  <br> 备注：弹幕仅在前端实现，后台功能请自行开发，该功能只在 PC Flash 播放器中生效                                                                                  |
这些设置方法的统一返回码是：
  
| 错误码<span id="errorcode"></span> | 含义 |
|---------|---------|
| 200 | 操作成功 | 
| 0  | 播放器未完全初始化 | 
| -1 | 动态更换失败视频，缺少必要参数 | 
| -2 | 未知操作命令 | 
| -3 | 播放时间超出有效播放范围 | 