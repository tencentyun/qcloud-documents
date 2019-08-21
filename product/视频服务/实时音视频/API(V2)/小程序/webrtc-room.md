## 标签说明
**&lt;webrtc-room&gt;** 标签是基于 &lt;live-pusher&gt; 和 &lt;live-player&gt; 实现的用于 WebRTC 互通的自定义组件。如果您希望直接使用 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签完成对接，或者想要了解 &lt;webrtc-room&gt; 的内部原理，可以参考 [&lt;live-pusher&gt; 标签](https://cloud.tencent.com/document/product/454/12518)。

## 标签详解
### 属性定义
| 属性      | 类型    | 默认值           | 说明       |
|:---------:|:---------:|:---------:|--------------|
| template  | String  | 'float'             | 必要，标识组件使用的界面模版，demo 中内置 bigsmall，float 和 grid 三种布局（用户如果需要自定义界面，请看 [界面定制](#CustomUI)） |
| sdkAppID    | String  |        -              | 必要，开通实时音视频服务创建应用后分配的 sdkAppID       |
| userID     | String  |         -     |必要，用户 ID |
| userSig    | String  |        -       | 必要，身份签名，相当于登录密码的作用    |
| roomID    | Number  |        -         | 必要，房间号                           |
| privateMapKey    | String  |       -      | 可选，房间权限 key，相当于进入指定房间 roomID 的钥匙，如果 trtc 控制台开启了权限密钥，则需要传 privateMapKey（[trtc 控制台](https://console.cloud.tencent.com/rav)>选择您的应用>账号信息）      |
| beauty    | Number  | 0                     | 可选， 美颜指数，取值0 - 9，数值越大效果越明显  |
| whiteness | String | 0                      | 可选， 美白指数，取值0 - 9，数值越大效果越明显 |
| muted     | Boolean | false             | 可选，true 静音 false 不静音    |
| debug     | Boolean | false             | 可选，true 打印推流 debug 信息 fales 不打印推流 debug 信息  |
| bindRoomEvent     | Function |      -   | 必要，监听 &lt;webrtc-room&gt; 组件返回的事件   |
| enableIM     | Boolean | false        | 可选，是否启用 IM   |
| bindIMEvent     | Function |      -    | 当 IM 开启时必要，监听 IM 返回的事件   |
| aspect | String | 9:16 | 可选， 宽高比3:4，9:16 |
| minBitrate | String | 200 | 可选，最小码率，该数值决定了画面最差的清晰度表现 |
| maxBitrate | String | 400 | 可选，最大码率，该数值决定了画面最好的清晰度表现 |
| autoplay | Boolean | false | 可选，进入房间后是否自动播放房间中其他的远程画面，true：自动播放，false：不自动播放 |
| enableCamera | Boolean | true | 可选，开启/关闭摄像头 |
| pureAudioPushMod | Number | - | 可选，纯音频推流模式，需要旁路直播和录制时需要带上此参数 <br/>1 => 本次是纯音频推流,不需要录制 mp3 文件 <br/> 2 => 本次是纯音频推流,录制文件为 mp3 |
| recordId | Number | &nbsp; | 可选，自动录制时业务自定义 ID，将在录制完成后通过直播录制回调接口通知业务方（[控制台 - 直播录制回调](https://console.cloud.tencent.com/live/livecodemanage)），相关文档：[直播录制文件获取](https://cloud.tencent.com/document/product/267/32739#.E5.BD.95.E5.88.B6.E6.96.87.E4.BB.B6.E8.8E.B7.E5.8F.96)，[事件消息通知](https://cloud.tencent.com/document/product/267/32744) `注意：如果小程序与小程序或者小程序与 Web 端互通，且传了 recordId，必须保证 web 端和小程序传递的值一致` |
| smallViewLeft | String | '1vw' | 小窗口距离大画面左边的距离，只在 template 设置为 bigsmall 有效 |
| smallViewTop | String | '1vw' | 小窗口距离大画面顶部的距离，只在 template 设置为 bigsmall 有效 |
| smallViewWidth | String | '30vw' | 小窗口宽度，只在 template 设置为 bigsmall 有效 |
| smallViewHeight | String | '40vw' | 小窗口高度，只在 template 设置为 bigsmall 有效 |
| waitingImg | String | - | 当微信切到后台时的垫片图片 |
| loadingImg | String | - | 画面 loading 图片 |


>?小程序实时音视频与 WebRTC 互通只需要保证两端的 sdkAppID 与 roomID 一致。

### 操作接口

**&lt;webrtc-room&gt;** 组件包含如下操作接口，您需要先通过 selectComponent 获取 &lt;webrtc-room&gt; 标签的引用，之后就可以进行相应的操作了。

| 函数名                                          | 说明         |
|-------------------------------------------------|--------------|
| start()                                         | 启动     |
| pause()                                       | 暂停     |
| resume()                                     | 恢复    |
| stop()                                          | 停止     |
| switchCamera()                           | 切换摄像头   |
| sendC2CTextMsg(receiveUser, msg, succ, fail) | 发送 C2C 文本消息 |
| sendC2CCustomMsg(receiveUser, msgObj, succ, fail) | 发送 C2C 自定义消息 |
| sendGroupTextMsg(msg, succ, fail) | 发送群组文本消息 |
| sendGroupCustomMsg(msgObj, succ, fail) | 发送群组自定义消息 |

```
var webrtcroom = this.selectComponent("#webrtcroomid")
webrtcroom.pause();
```
#### sendC2CTextMsg

> 发送C2C文本消息

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
receiveUser | String | 是 | 接收人的 userid
msg | String | 是 | 消息内容
succ | Function | 否 | 发送成功的回调
fail | Function | 否 | 发送失败的回调

#### sendC2CCustomMsg

> 发送C2C自定义消息

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
receiveUser | String | 是 | 接收人的 userid
msgObj | Object | 是 | {data: '消息内容', ext: '', desc: ''}
succ | Function | 否 | 发送成功的回调
fail | Function | 否 | 发送失败的回调

#### sendGroupTextMsg

发送群组文本消息

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
msg | String | 是 | 消息内容
succ | Function | 否 | 发送成功的回调
fail | Function | 否 | 发送失败的回调

#### sendGroupCustomMsg

发送群组自定义消息

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
msgObj | Object | 是 | {data: '消息内容', ext: '', desc: ''}
succ | Function | 否 | 发送成功的回调
fail | Function | 否 | 发送失败的回调

### 事件通知
**&lt;webrtc-room&gt;** 标签通过 **onRoomEvent** 返回内部事件，通过 **onIMEvent** 返回 IM 消息事件，事件参数格式如下:

>?如果 enableIM 关闭了，则可以忽略 onIMEvent

```json
"detail": {
  "tag": "事件tag标识，具有唯一性",
  "code": "事件代码",
  "detail": "对应事件的详细参数"
}
```

### 示例代码
```
// Page.wxml 文件
<webrtc-room id="webrtcroom"
	roomID="{{roomID}}"
	userID="{{userID}}"
	userSig="{{userSig}}"
	sdkAppID="{{sdkAppID}}"
	privateMapKey="{{privateMapKey}}"
	template="1v3"
	beauty="{{beauty}}"
	muted="{{muted}}"
	debug="{{debug}}"
	bindRoomEvent="onRoomEvent"
	enableIM="{{enableIM}}"
	bindIMEvent="onIMEvent">
</webrtc-room>


// Page.js 文件
Page({
	data: {
		//...
		roomID: '',
		userID: '',
		userSig: '',
		sdkAppID: '',
		beauty: 3,
		muted: false,
		debug: false,
		enableIM: false
	},
    onRoomEvent: function(e){
        switch(e.detail.tag){
            case 'error': {
                //发生错误
                var code = e.detail.code;
                var detail = e.detail.detail;
                break;
            }
        }
    },
    onIMEvent: function(e){
        switch(e.detail.tag){
            case 'big_group_msg_notify': 
                //收到群组消息
                console.debug( e.detail.detail )
                break;
            case 'login_event': 
                //登录事件通知
                console.debug( e.detail.detail )
                break;
            case 'connection_event': 
                //连接状态事件
                console.debug( e.detail.detail )
                break;
            case 'join_group_event': 
                //进群事件通知
                console.debug( e.detail.detail )
                break;
        }
    },

  onLoad: function (options) {
		self.setData({
			userID: self.data.userID,
			userSig: self.data.userSig,
			sdkAppID: self.data.sdkAppID,
			roomID: self.data.roomID,
			privateMapKey: res.data.privateMapKey
		}, function() {
			var webrtcroomCom = this.selectComponent('#webrtcroom');
			if (webrtcroomCom) {
				webrtcroomCom.start();
			}
		})
	},
  	
})
```



## 使用指引

### step1: 下载自定义组件源码

**&lt;webrtc-room&gt;** 并非微信小程序原生提供的标签，而是一个自定义组件，所以您需要额外的代码来支持这个标签。单击 [小程序 Demo 源码](https://github.com/tencentyun/TRTCSDK/tree/master/WXMini) 下载源码包。

### step2: 在工程中引入组件
- 在 page 目录下的 json 配置文件内引用组件，这一步是必须的，因为 &lt;webrtc-room&gt; 并非原生标签。
```json
 "usingComponents": {
    "webrtc-room": "/pages/webrtc-room/webrtc-room"
  }
```

- 在 page 目录下的 wxml 文件中使用标签
```xml
<webrtc-room id="webrtcroomid"
    roomID="{{roomID}}"
    userID="{{userID}}"
    userSig="{{userSig}}"
    sdkAppID="{{sdkAppID}}"
    privateMapKey="{{privateMapKey}}"
    template="float"
    beauty="{{beauty}}"
    muted="{{muted}}"
    debug="{{debug}}"
    bindRoomEvent="onRoomEvent"
    enableIM="{{enableIM}}"
    bindIMEvent="onIMEvent">
</webrtc-room>
```

### step3: 获取 key 信息
按照如下表格获取关键的 key 信息，这是使用腾讯云互通直播服务所必须的几个信息：

| KEY | 示例    | 作用 |获取方案 |
|:--------:|:--------:|:--------:|:--------:|
| sdkAppID | 1400087915  | 用于计费和业务区分 |  step1 中获取 |
| userID   | xiaoming  | 用户名 | 可以由您的服务器指定，或者使用小程序的 openid  |
| userSig | 加密字符串  | 相当于 userid 对应的登录密码 | 由您的服务器 [签发](https://cloud.tencent.com/document/product/647/17275)|
| roomID | 12345  | 房间号 | 可以由您的服务器指定，数据类型为 uint32 |
| privateMapKey | 加密字符串  | 当开启权限密钥时需要传。进房票据：相当于是进入 roomid 的钥匙 | 由您的服务器 [签发](https://cloud.tencent.com/document/product/647/32240)|


### step4: 进入房间

```
self.setData({
	userID: userID,
	userSig: userSig,
	sdkAppID: sdkAppID,
	roomID: roomID,
	privateMapKey: privateMapKey
}, function() {
	var webrtcroomCom = this.selectComponent('#webrtcroomid');
	if (webrtcroomCom) {
		webrtcroomCom.start();
	}
})
```

<h2 id="CustomUI"> 界面定制 </h2>

- **创建界面模版**

```html
//第一步：新建 /pages/templates/mytemplate 文件夹，并创建 mytemplate.wxml 和 mytemplate.wxss 文件

//第二步：编写 mytemplate.wxml 和 mytemplate.wxss 文件
//mytemplate.wxml
<template name='mytemplate'>
    <view class='videoview'>
        <view class="pusher-box">
            <live-pusher
                id="rtcpusher"
                autopush
                mode="RTC"
                url="{{pushURL}}"
                aspect="{{aspect}}"
                min-bitrate="{{minBitrate}}"
                max-bitrate="{{maxBitrate}}"
                audio-quality="high"
                beauty="{{beauty}}"
                muted="{{muted}}"
                waiting-image="https://mc.qcloudimg.com/static/img/
								     daeed8616ac5df256c0591c22a65c4d3/pause_publish.jpg"
                background-mute="{{true}}"
                debug="{{debug}}"
                bindstatechange="onPush"
                binderror="onError">
                <cover-image  class='character' src="/pages/Resources/mask.png"></cover-image>
                <cover-view class='character' style='padding: 0 5px;'>我</cover-view>
            </live-pusher>
        </view>
        <view class="player-box" wx:for="{{members}}" wx:key="userID"> 
            <view class='poster'>
                <cover-image class='set'
			       src="https://miniprogram-1252463788.file.myqcloud.com/roomset_{{index + 2}}.png">
				</cover-image>
            </view>
            <live-player
                id="{{item.userID}}"
                autoplay
                mode="RTC"
                wx:if="{{item.accelerateURL}}"
                object-fit="fillCrop"
                min-cache="0.1"
                max-cache="0.3"
                src="{{item.accelerateURL}}"
                debug="{{debug}}"
                background-mute="{{true}}"
                bindstatechange="onPlay">
                <cover-view class='loading' wx:if="{{item.loading}}">
                    <cover-image src="/pages/Resources/loading_image0.png"></cover-image>
                </cover-view>
                <cover-image  class='character' src="/pages/Resources/mask.png"></cover-image>
                <cover-view class='character' style='padding: 0 5px;'>{{item.userName}}</cover-view>
            </live-player>  
        </view> 
    </view>
</template>

//mytemplate.wxss
.videoview {
  background-repeat:no-repeat;
  background-size: cover;
  width: 100%;
  height: 100%;
}

```

- **webrtc-room 组件引入模版**

```html
//为 <webrtc-room> 组件中的 webrtcroom.wxml 文件添加自定义模版
<import src='/pages/templates/mytemplate/mytemplate.wxml'/>
<view class='conponent-box'>
    <view styles="width:100%;height=100%;" wx:if="{{template=='1v3'}}">
        <template is='mytemplate' data="{{pushURL, aspect, 
				      minBitrate, maxBitrate, beauty, muted, debug, members}}"/>
    </view>
</view>

//为 <webrtc-room> 组件中的 webrtcroom.wxss 文件添加自定义样式
@import "../templates/mytemplate/mytemplate.wxss";
```

