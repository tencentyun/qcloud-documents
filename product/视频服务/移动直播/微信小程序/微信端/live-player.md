
**&lt;live-player&gt;** 是小程序内部用于支持音视频下行（播放）能力的功能标签，本文主要介绍该标签的使用方法。

## 版本支持
- 微信 APP iOS 最低版本要求：6.5.21 
- 微信 APP Android 最低版本要求：6.5.19 
- 小程序基础库最低版本要求：1.7.0 

> 通过 wx.getSystemInfo 可以获取当前基础库版本信息

## 使用限制
出于政策和合规的考虑，微信暂时没有放开所有小程序对 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签的支持：

- 个人账号和企业账号的小程序暂时只开放如下表格中的类目：

<table>
  <tr align="center">
    <th width="200px">主类目</th>
    <th width="700px">子类目</th>
  </tr>
  <tr align="center">
    <td>【社交】</td>
		<td>直播</td>
  </tr>
	<tr align="center">
    <td>【教育】</td>
		<td>在线教育</td>
  </tr>
	<tr align="center">
    <td>【医疗】</td>
		<td>互联网医院，公立医院</td>
  </tr>
	<tr align="center">
    <td>【政务民生】</td>
		<td>所有二级类目</td>
  </tr>
	<tr align="center">
    <td>【金融】</td>
		<td>基金、信托、保险、银行、证券/期货、非金融机构自营小额贷款、征信业务、消费金融</td>
  </tr>
</table>

- 符合类目要求的小程序，需要在小程序管理后台的<font color='red'> “设置 - 接口设置” </font>中自助开通该组件权限，如下图所示：

![](https://mc.qcloudimg.com/static/img/a34df5e3e86c9b0fcdfba86f8576e06a/weixinset.png)

注意：如果以上设置都正确，但小程序依然不能正常工作，可能是微信内部的缓存没更新，请删除小程序并重启微信后，再进行尝试。

## 属性定义
| 属性名 | 类型 | 默认值 | 说明 |
|:-------:|:-------:|:-------:|---------|
| src | String |  | 用于音视频下行的播放URL，支持rtmp、flv 等协议|
| mode | String | live |  live, RTC|
| autoplay | Boolean | false | 是否自动播放 |
| muted | Boolean | false | 是否静音 |
| orientation | String | vertical | vertical, horizontal |
| object-fit | String | contain | contain, fillCrop |
| background-mute | Boolean | false | 当微信切到后台时，是否关闭播放声音 |
| min-cache | Number | 1  | 最小缓冲延迟， 单位：秒|
| max-cache | Number | 3 | 最大缓冲延迟， 单位：秒|
| bindstatechange | EventHandler |  | 用于指定一个javascript函数来接受播放器事件|
| bindfullscreenchange | EventHandler |  | 用于指定一个javascript函数来接受全屏事件|
| debug | Boolean | false | 是否开启调试模式 |

## 示例代码
```html
<view id='video-box'>  
    <live-player
		wx:for="{{player}}"
		id="player_{{index}}"
		mode="RTC"
		object-fit="fillCrop"
		src="{{item.playUrl}}" 
		autoplay='true'
		bindstatechange="onPlay">
   </live-player>
 </view> 
```

## 超低时延
&lt;live-player&gt; 的 RTC 模式支持 500ms 以内的超低时延链路，可以应用在视频通话和远程遥控等场景中，要使用超低时延播放，需要注意如下几点：
（1）推流端如果是微信小程序，请使用 &lt;live-pusher&gt; 的 RTC 模式。
（2）推流端如果是 iOS 或者 Android SDK，请使用 setVideoQuality 的 MAIN_PUBLISHER 模式。
（3）推流端如果是 Windows，请不要使用 OBS，延时太高，可以使用我们的 [Windows SDK](https://cloud.tencent.com/document/product/454/7873#Windows)。
（4）&lt;live-player&gt; 的 min-cache 和 max-cache 请不要自行设置，使用默认值。
（5）播放地址请使用超低延时播放地址，也就是带了防盗链签名的 rtmp:// 地址，如下：

|  对比项目 | 示例 | 时延 |
|---------|---------| ----- |
| 普通直播 URL | rtmp://3891.liveplay.myqcloud.com/live/3891_test_clock_for_rtmpacc |  >2s |
| 超低延时 URL | rtmp://3891.liveplay.myqcloud.com/live/3891_test_clock_for_rtmpacc?bizid=bizid&txTime=5FD4431C&txSerect=20e6d865f462dff61ada209d53c71cf9 | < 500ms | 


## 属性详解
- **src**
用于音视频下行的播放 URL，支持 rtmp 协议（URL 以 “rtmp://” 打头）和 flv 协议（URL 以 “http://” 打头且以 “.flv” 结尾） ，腾讯云推流 URL 的获取方法见 [DOC](https://cloud.tencent.com/document/product/454/7915)。
> &lt;live-player&gt; 标签是不支持 HLS(m3u8) 协议的，因为 &lt;video&gt; 已经支持 HLS(m3u8) 播放协议了。但直播观看不推荐使用 HLS(m3u8) 协议，延迟要比 rtmp 和 flv 协议高一个数量级。

- **mode**
live 模式主要用于直播类场景，比如赛事直播、在线教育、远程培训等等。该模式下，小程序内部的模块会优先保证观看体验的流畅，通过调整 min-cache 和 max-cache 属性，您可以调节观众（播放）端所感受到的时间延迟的大小，文档下面会详细介绍这两个参数。

 RTC 则主要用于双向视频通话或多人视频通话场景，比如金融开会、在线客服、车险定损、培训会议 等等。在此模式下，对 min-cache 和 max-cache 的设置不会起作用，因为小程序内部会自动将延迟控制在一个很低的水平（500ms 左右）。
 
- **min-cache 和 max-cache**
这两个参数分别用于指定观看端的最小缓冲时间和最大缓冲时间。所谓**缓冲时间**，是指播放器为了缓解网络波动对观看流畅度的影响而引入的一个“蓄水池”，当来自网络的数据包出现卡顿甚至停滞的时候，“蓄水池”里的紧急用水可以让播放器还能坚持一小段时间，只要在这个短暂的时间内网速恢复正常，播放器就可以源源不断地渲染出流畅而平滑的视频画面。

 “蓄水池”里的水越多，抗网络波动的能力就越强，但代价就是观众端的延迟就越大，所以要在不同的场景下，使用不同的配置来达到体验上的平衡：
  + 码率比较低（1Mbps 左右，画面以人物为主）的直播流，min-cache = 1，max-cache = 3 较合适。
	+ 码率比较高（2-3Mbps 的高清游戏画面为主）的直播流，min-cache = 3，max-cache = 5 较合适。

 RTC 模式下这两个参数是无效的。
 
- **orientation**
画面渲染角度，horizontal 代表是原始画面方向，vertical 代表向右旋转 90度。

- **object-fit**
画面填充模式，contain 代表把画面显示完成，但如果视频画面的宽高比和 &lt;live-player&gt; 标签的宽高比不一致，那么您将看到黑边。fillCrop 代表把屏幕全部撑满，但如果视频画面的宽高比和 &lt;live-player&gt; 标签的宽高比不一致，那么画面中多余的部分会被裁剪掉。


- **background-mute**
微信切到后台以后是否继续播放声音，用于避免锁屏对于当前小程序正在播放的视频内容的影响。

- **sound-mode**  
设置播放模式，可设值为: ear与speaker，ear代表使用听筒播放， speaker代表使用扬声器。默认为扬声器

- **debug**
 调试音视频相关功能，如果没有很好的工具会是一个噩梦，所以小程序为 live-pusher 标签支持了 debug 模式，开始 debug 模式之后，原本用于渲染视频画面的窗口上，会显示一个半透明的 log 窗口，用于展示各项音视频指标和事件，降低您调试相关功能的难度，具体使用方法我们在 [FAQ](https://cloud.tencent.com/document/product/454/7946#2.-.E5.8F.91.E7.8E.B0.E9.97.AE.E9.A2.98.E7.9A.84.E2.80.9C.E7.9C.BC.E7.9D.9B.E2.80.9D) 中有详细说明。


## 对象操作
- **wx.createLivePlayerContext()**
通过 wx.createLivePlayerContext() 可以将 &lt;live-player&gt; 标签和 javascript 对象关联起来，之后即可操作该对象。

- **play** 
开始播放，如果 &lt;live-player&gt; 的 autoplay 属性设置为 false（默认值），那么就可以使用 play 来手动启动播放。

- **stop**
停止播放。

- **pause**  
暂停播放，停留在最后画面

- **resume**  
继续播放，与pause成对使用

- **mute**
设置静音。

- **requestFullScreen**
进入全屏幕。

- **exitFullScreen**
退出全屏幕。

```javascript
var player = wx.createLivePlayerContext('pusher');
player.requestFullScreen({
    success: function(){
		    console.log('enter full screen mode success!')
		}
		fail: function(){
		    console.log('enter full screen mode failed!')
		}
		complete: function(){
		    console.log('enter full screen mode complete!')
		}
});
```

## 内部事件
通过 **&lt;live-player&gt;** 标签的 **bindstatechange** 属性可以绑定一个事件处理函数，该函数可以监听推流模块的内部事件和异常通知。

#### 1. 关键事件

| code                 |   事件定义  |  含义说明            |   
| :-------------------  |:------------ |  :------------------------ | 
| 2001 | PLAY_EVT_CONNECT_SUCC           |  已经连接到云端服务器       |
| 2002 | PLAY_EVT_RTMP_STREAM_BEGIN  | 服务器开始传输音视频数据 | 
| 2003 | PLAY_EVT_RCV_FIRST_I_FRAME    | 网络接收到首段音视频数据 | 
| 2004 | PLAY_EVT_PLAY_BEGIN        | 视频播放开始，可以在收到此事件之前先用默认图片代表等待状态 |
| 2006 | PLAY_EVT_PLAY_END           | 视频播放结束                                                                   | 
| 2007 | PLAY_EVT_PLAY_LOADING    | 进入缓冲中状态，此时播放器在等待或积攒来自服务器的数据 |
| -2301 | PLAY_ERR_NET_DISCONNECT |  网络连接断开，且重新连接亦不能恢复，播放器已停止播放  | 

> 播放 HTTP:// 打头的 FLV 协议地址时，如果观众遇到播放中直播流断开的情况，小程序是不会抛出 PLAY_EVT_PLAY_END 事件的，这是因为 FLV 协议中没有定义停止事件，所以只能通过监听 PLAY_ERR_NET_DISCONNECT 来替代之。

#### 2. 警告事件
内部警告并非不可恢复的错误，小程序内部的音视频 SDK 会启动相应的恢复措施，警告的目的主要用于提示开发者或者最终用户，比如：

| code                 |    事件定义  |  含义说明           |   
| :-------------------  |:-------- |  :------------------------ | 
| 2101 | PLAY_WARNING_VIDEO_DECODE_FAIL   |   当前视频帧解码失败  |
| 2102 | PLAY_WARNING_AUDIO_DECODE_FAIL  |   当前音频帧解码失败  |
| 2103 | PLAY_WARNING_RECONNECT   | 网络断连, 已启动自动重连恢复 (重连超过三次就直接抛送 PLAY_ERR_NET_DISCONNECT 了) |
| 2104 | PLAY_WARNING_RECV_DATA_LAG        | 视频流不太稳定，可能是观看者当前网速不充裕 | 
| 2105 | PLAY_WARNING_VIDEO_PLAY_LAG       | 当前视频播放出现卡顿|
| 2106 | PLAY_WARNING_HW_ACCELERATION_FAIL  | 硬解启动失败，采用软解   |
| 2107 | PLAY_WARNING_VIDEO_DISCONTINUITY   | 当前视频帧不连续，视频源可能有丢帧，可能会导致画面花屏 |
| 3001 | PLAY_WARNING_DNS_FAIL                 | DNS解析失败（仅播放 RTMP:// 地址时会抛送）|
| 3002 | PLAY_WARNING_SEVER_CONN_FAIL  | 服务器连接失败（仅播放 RTMP:// 地址时会抛送）|
| 3003 | PLAY_WARNING_SHAKE_FAIL             | 服务器握手失败（仅播放 RTMP:// 地址时会抛送）|

#### 3. 示例代码
```javascript
Page({
    onPlay: function(ret) {
        if(ret.detail.code == 2004) {
			    console.log('视频播放开始',ret);
        }
    },
	
	/**
	 * 生命周期函数--监听页面加载
	 */
	onLoad: function (options) {
	//...
	}
})
```

## 特别说明
1. &lt;live-player&gt; 组件是由客户端创建的原生组件，它的层级是最高的，可以使用 &lt;cover-view&gt; 和 &lt;cover-image&gt; 覆盖在上面。

2. 请勿在 &lt;scroll-view&gt; 中使用 &lt;live-player&gt; 组件。

