
**&lt;live-pusher&gt;** 是小程序内部用于支持音视频上行能力的功能标签，本文主要介绍该标签的使用方法。

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
| url | String |  | 用于音视频上行的推流URL|
| mode | String | RTC |  SD, HD, FHD, RTC|
| autopush | Boolean | false | 是否自动启动推流 |
| muted | Boolean | false | 是否静音 |
| enable-camera | Boolean | true | 开启\关闭摄像头  |
| auto-focus | Boolean | true | 手动\自动对焦 |
| orientation | String | vertical | vertical, horizontal |
| beauty |  Number | 0 | 美颜指数，取值 0 - 9，数值越大效果越明显 |
| whiteness  | Number | 0 | 美白指数，取值 0 - 9，数值越大效果越明显 |
| aspect | String | 9:16 | 3:4, 9:16|
| min-bitrate | Number | 200  | 最小码率，该数值决定了画面最差的清晰度表现|
| max-bitrate | Number | 1000 | 最大码率，该数值决定了画面最好的清晰度表现|
| audio-quality| String| low | low 适合语音通话, high 代表高音质 | 
| waiting-image | String |  | 当微信切到后台时的垫片图片 |
| waiting-image-hash | String |  |当微信切到后台时的垫片图片的校验值 |
| background-mute | Boolean | false | 当微信切到后台时是否禁用声音采集 |
| bindstatechange | String |  | 用于指定一个javascript函数来接收音视频事件 |
| debug | Boolean | false | 是否开启调试模式 |

## 示例代码
```html
<view id='video-box'>  
	<live-pusher
	      id="pusher"
	      mode="RTC"
	      url="{{pusher.push_url}}" 
	      autopush='true'
	      bindstatechange="onPush">
	</live-pusher>  
 </view> 
```

## 属性详解
- **url**
用于音视频上行的推流URL，以 rtmp:// 协议前缀打头，腾讯云推流 URL 的获取方法见 [DOC](https://cloud.tencent.com/document/product/454/7915)。
> 小程序内部使用的 RTMP 协议是支持 UDP 加速的版本，在同样网络条件下，UDP 版本的 RTMP 会比开源版本的有更好的上行速度和抗抖动能力。

- **mode**
SD、HD 和 FHD 主要用于直播类场景，比如赛事直播、在线教育、远程培训等等。SD、HD 和 FHD 分别对应三种默认的清晰度。该模式下，小程序会更加注重清晰度和观看的流畅性，不会过分强调低延迟，也不会为了延迟牺牲画质和流畅性。

 RTC 则主要用于双向视频通话或多人视频通话场景，比如金融开会、在线客服、车险定损、培训会议 等等。该模式下，小程序会更加注重降低点到点的时延，也会优先保证声音的质量，在必要的时候会对画面清晰度和画面的流畅性进行一定的缩水。

- **orientation 和 aspect**
横屏（horizontal）模式还是竖屏（vertical）模式，默认是竖屏模式，即 home 键朝下。这时，小程序推出的画面的宽高比是 3：4 或者 9 : 16 这两种竖屏宽高比的画面，也就是宽 < 高。如果改成横屏模式，小程序推出的画面宽高比即变为 4 : 3 或者 16 : 9 这种横屏宽高比的画面，也就是宽 > 高。

 具体的宽高比是有 aspect 决定的 ，默认是 9: 16， 也可以支持 3：4。 这是在 orientation 的属性值为 vertical 的情况下。如果 orientation 的属性值为 horizontal，那么 3：4 的效果等价于 4：3， 9：16 的效果等价于 16：9。

- **min-bitrate 和 max-bitrate**
这里首先要科普一个概念 —— 视频码率，指视频编码器每秒钟输出的视频数据的多少。在视频分辨率确定的情况下，视频码率越高，即每秒钟输出的数据越多，相应的画质也就越好。

 所以 min-bitrate 和 max-bitrate 这两个属性，分别用于决定输出画面的最低清晰度和最高清晰度。这两个数值并非越大越好，因为用户的网络上行不是无限好的。但也不是越小越好，因为实际应用场景中，清晰与否是用户衡量产品体验的一个重要指标。具体的数值设定我们会在 **“参数设置”** 部分详细介绍。
 
 小程序内部会自动处理好分辨率和码率的关系，比如 2Mbps 的码率，小程序会选择 720p 的分辨率进行匹配，而 300kbps 的码率下，小程序则会选择较低的分辨率来提高编码效率。所以您只需要关注 min-bitrate 和 max-bitrate 这一对参数就可以掌控画质了

- **waiting-image 和 waiting-image-hash**
出于用户隐私的考虑，在微信切到后台以后，小程序希望停止摄像头的画面采集。但是对于另一端的用户而言，画面会变成黑屏或者冻屏（停留在最后一帧），这种体验是非常差的。为了解决这个问题，我们引入了 waiting-image 属性，您可以设置一张有 “稍候” 含义的图片（waiting-image 是该图片的 url，waiting-image-hash 则是该图片对应的 md5 校验值）。当微信切到后台以后，小程序会使用该图片作为摄像头画面的替代，以极低的流量占用维持视频流 3 分钟时间。

- **debug**
 调试音视频相关功能，如果没有很好的工具会是一个噩梦，所以小程序为 live-pusher 标签支持了 debug 模式，开始 debug 模式之后，原本用于渲染视频画面的窗口上，会显示一个半透明的 log 窗口，用于展示各项音视频指标和事件，降低您调试相关功能的难度，具体使用方法我们在 [FAQ](https://cloud.tencent.com/document/product/454/7946#2.-.E5.8F.91.E7.8E.B0.E9.97.AE.E9.A2.98.E7.9A.84.E2.80.9C.E7.9C.BC.E7.9D.9B.E2.80.9D) 中有详细说明。

## 参数设置
这么多参数，具体要怎样设置才比较合适呢？我们给出如下建议值：

| 场景        | mode |  min-bitrate | max-bitrate |  audio-quality |  说明  |
|-------------|:-------:| :-------------: | :-------:| :--------: | ------------ -|
| 标清直播 | SD   | 300kbps | 800kbps  | high | 窄带场景，比如户外或者网络不稳定的情况下适用 |
| 高清直播 | HD   | 600kbps | 1200kbps | high | 目前主流的APP所采用的参数设定，普通直播场景推荐使用这一档 |
| 超清直播 | FHD  | 600kbps | 1800kbps | high | 对清晰度要求比较苛刻的场景，普通手机观看使用 HD 即可 |
| 视频客服（用户） | RTC | 200kbps | 500kbps   | high | 这是一种声音为主，画面为辅的场景，所以画质不要设置的太高 | 
| 车险定损（车主） | RTC | 200kbps | 1200kbps | high | 由于可能要看车况详情，画质上限会设置的高一些 |
| 多人会议（主讲） | RTC | 200kbps | 1000kbps | high | 主讲人画质可以适当高一些，参与的质量可以设置的低一些 |
| 多人会议（参与） | RTC | 150kbps | 300kbps   | low | 作为会议参与者，不需要太高的画质和音质 |

> 如果不是对带宽特别没有信心的应用场景，audio-quality选项请不要选择 low，其音质和延迟感都要会比 high 模式差很多。

## 对象操作
- **wx.createLivePusherContext()**
通过 wx.createLivePusherContext() 可以将 &lt;live-pusher&gt; 标签和 javascript 对象关联起来，之后即可操作该对象。

- **start** 
开始推流，如果 &lt;live-pusher&gt; 的 autopush 属性设置为 false（默认值），那么就可以使用 start 来手动开始推流。

- **stop**
停止推流。

- **pause**
暂停推流。

- **resume**
回复推流，请与 pause 操作配对使用。

- **switchCamera**
切换前后摄像头

- **snapshot**
推流截图，截图大小跟组件的大小一致。截图成功图片的临时路径为ret.tempImagePath

```javascript
var pusher = wx.createLivePusherContext('pusher');
pusher.start({
    success: function(ret){
		    console.log('start push success!')
		}
		fail: function(){
		    console.log('start push failed!')
		}
		complete: function(){
		    console.log('start push complete!')
		}
});
```

## 内部事件
通过 **&lt;live-pusher&gt;** 标签的 **bindstatechange** 属性可以绑定一个事件处理函数，该函数可以监听推流模块的内部事件和异常通知。

#### 1. 常规事件

| code                 |    事件定义  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
| 1001 | PUSH_EVT_CONNECT_SUCC | 已经成功连接到云端服务器 |
| 1002 | PUSH_EVT_PUSH_BEGIN       | 与服务器握手完毕,一切正常，准备开始上行推流 |
| 1003 | PUSH_EVT_OPEN_CAMERA_SUCC  |  已成功启动摄像头，摄像头被占用或者被限制权限的情况下无法打开 | 

#### 2. 严重错误

| code                 |    事件定义  |  含义说明                    |  
| :-------------------  |:-------- |  :------------------------ | 
| -1301 |PUSH_ERR_OPEN_CAMERA_FAIL   | 打开摄像头失败|
| -1302 |PUSH_ERR_OPEN_MIC_FAIL           | 打开麦克风失败|
| -1303 |PUSH_ERR_VIDEO_ENCODE_FAIL  | 视频编码失败|
| -1304 |PUSH_ERR_AUDIO_ENCODE_FAIL  | 音频编码失败|
| -1305 |PUSH_ERR_UNSUPPORTED_RESOLUTION  |不支持的视频分辨率|
| -1306 |PUSH_ERR_UNSUPPORTED_SAMPLERATE | 不支持的音频采样率|
| -1307 |PUSH_ERR_NET_DISCONNECT       |网络断连,且经三次抢救无效,可以放弃治疗,更多重试请自行重启推流|

#### 3. 警告事件
内部警告并非不可恢复的错误，小程序内部的音视频 SDK 会启动相应的恢复措施，警告的目的主要用于提示开发者或者最终用户，比如：

- **WARNING_NET_BUSY**
上行网速不给力，建议提示用户改善当前的网络环境，比如让用户离家里的路由器近一点，或者切到 WiFi 环境下再使用。

- <font color='red'>**WARNING_SERVER_DISCONNECT**</font>
请求被后台拒绝了，出现这个问题一般是由于 URL 里的 txSecret 计算错了，或者是 URL 被其他人占用了（跟播放不同，一个推流 URL 同时只能有一个用户使用）。

| code                 |    事件定义  |  含义说明                    | 
| :-------------------  |:-------- |  :-----------------------| 
| 1101 | PUSH_WARNING_NET_BUSY             | 上行网速不够用，建议提示用户改善当前的网络环境|
| 1102 |PUSH_WARNING_RECONNECT           | 网络断连, 已启动重连流程 (重试失败超过三次会放弃)|
| 1103 |PUSH_WARNING_HW_ACCELERATION_FAIL| 硬编码启动失败，自动切换到软编码|
| 1107 |PUSH_WARNING_SWITCH_SWENC     |  由于机器性能问题，自动切换到硬件编码|
| 3001 |PUSH_WARNING_DNS_FAIL                |  DNS解析失败，启动重试流程     |
| 3002 |PUSH_WARNING_SEVER_CONN_FAIL |  服务器连接失败，启动重试流程  |
| 3003 |PUSH_WARNING_SHAKE_FAIL            |  服务器握手失败，启动重试流程  |
| 3004 |PUSH_WARNING_SERVER_DISCONNECT   |  服务器主动断开连接，启动重试流程 |
| 3005 |PUSH_WARNING_SERVER_DISCONNECT   |  socket 链路异常断开 ，启动重试流程 |

#### 4. 示例代码
```javascript
Page({
    onPush: function(ret) {
        if(ret.detail.code == 1002) {
			    console.log('推流成功了',ret);
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

