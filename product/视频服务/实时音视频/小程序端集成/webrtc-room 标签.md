## 标签说明
**&lt;webrtc-room&gt;** 标签是基于 &lt;live-pusher&gt; 和 &lt;live-player&gt; 实现的用于 WebRTC 互通的自定义组件。如果您希望直接使用 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签完成对接，或者想要了解 &lt;webrtc-room&gt; 的内部原理，可以参考 [DOC](https://cloud.tencent.com/document/product/454/16915)。

## 版本要求
- 微信 6.6.6 版本开始支持。

## 效果演示
- **PC 端**
用 Chrome 浏览器打开 [体验页面](https://www.qcloudtrtc.com/miniApp/index.html#/) 可以体验桌面版 WebRTC 的效果。

- **Android 端**
用 Android 手机 [下载 App](http://sj.qq.com/myapp/detail.htm?apkName=com.tencent.trtc) 或者扫码下载安装 App 即可体验 Android 的效果。
<img src="https://a.app.qq.com/o/image/microQr.png?pkgName=com.tencent.trtc" width="160">

- **iOS 端**
用 iOS 手机 扫码后通过 Safari 打开并安装 App 即可体验 iOS 的效果。
<img src="https://main.qcloudimg.com/raw/87b0628665001ae24b58145d7527335d.png" width="150">


- ##### 信任证书
> 安装 App 后，还需要配置信任证书方可打开体验 (单击打开大图)
- 设置->通用->设备管理->选择证书->信任证书
![https://main.qcloudimg.com/raw/ca452ae5e382a8800dabf6679726de62.jpg](https://main.qcloudimg.com/raw/ca452ae5e382a8800dabf6679726de62.jpg)

- **微信端**
发现=>小程序=>搜索“腾讯视频云”，单击 WebRTC 功能卡，就可以体验跟桌面版 Chrome 互通的效果了。
![](https://main.qcloudimg.com/raw/36310afb4121a945d1119c51c3334c36.png)

## 对接资料

| 对接资料 | 说明 | github地址 |
|---------|---------|---------|
| 小程序源码 | 包含&lt;webrtc-room&gt;的组件源码以及 demo 源码 | [前往](https://github.com/TencentVideoCloudMLVBDev/rtcroom_wxlite) |
| PC 端源码 | 基于 [WebrtcAPI](https://cloud.tencent.com/document/product/647/16865) 实现的 Chrome 版 WebRTC 接入源码（其中 component/WebRTCRoom.js 实现了一个简单的房间管理功能，component/mainwindow.js 包含了对 WebRTC API 的使用代码） |  [前往](https://github.com/TencentVideoCloudMLVBDev/webrtc_pc)|
| 后台源码 | 实现了一个简单的房间列表功能，同时包含&lt;webrtc-room&gt;几个所需参数的生成代码 | [前往](https://github.com/TencentVideoCloudMLVBDev/webrtc_server_java) |

## 标签详解
### 属性定义
| 属性      | 类型    | 默认值           | 说明       |
|:---------:|:---------:|:---------:|--------------|
| template  | String  | '1v3'             | 必要，标识组件使用的界面模版（用户如果需要自定义界面，请看 [界面定制](#CustomUI)） |
| sdkAppID    | String  |                       | 必要，开通实时音视频服务创建应用后分配的 sdkAppID       |
| userID     | String  |                   |必要，用户 ID |
| userSig    | String  |                     | 必要，身份签名，相当于登录密码的作用    |
| roomID    | Number  |                      | 必要，房间号                           |
| privateMapKey    | String  |                 | 必要，房间权限 key，相当于进入指定房间 roomID 的钥匙      |
| beauty    | Number  | 5                     | 可选， 美颜指数，取值 0 - 9，数值越大效果越明显  |
| whiteness | String | 5                      | 可选， 美白指数，取值 0 - 9，数值越大效果越明显 |
| muted     | Boolean | false             | 可选，true 静音 false 不静音    |
| debug     | Boolean | false             | 可选，true 打印推流 debug 信息 fales 不打印推流 debug 信息  |
| bindRoomEvent     | Function |              | 必要，监听 &lt;webrtc-room&gt; 组件返回的事件   |
| enableIM     | Boolean | true             | 可选，是否启用IM, true   |
| bindIMEvent     | Function |             | 当IM开启时必要，监听 IM 返回的事件   |
| userName | String |  | 可选，IM昵称 |
| aspect | String | 9:16 | 可选， 宽高比3:4, 9:16 |
| minBitrate | String | 200 | 可选，最小码率，该数值决定了画面最差的清晰度表现 |
| maxBitrate | String | 400 | 可选，最大码率，该数值决定了画面最好的清晰度表现 |
| autoplay | Boolean | false | 可选，进入房间后是否自动播放房间中其他的远程画面 true 自动播放 false 不自动播放 |
| enableCamera | Boolean | true | 可选，开启\关闭摄像头 |
| pureAudioPushMod | Number |  | 可选，纯音频推流模式，需要旁路直播和录制时需要带上此参数 <br/>1 => 本次是纯音频推流,不需要录制mp3文件 <br/> 2 => 本次是纯音频推流,录制文件为mp3 |
| recordId | Number |  | 可选，自动录制时业务自定义id，将在录制完成后通过[直播录制回调](https://console.qcloud.com/live/livecodemanage) 接口通知业务方，`注意：如果小程序与小程序或者小程序与Web端互通，且传了recordId，必须保证web端和小程序传递的值一致` |


> 小程序实时音视频与 WebRTC 互通只需要保证两端的 sdkAppID 与 roomID 一致

### 操作接口

**&lt;webrtc-room&gt;** 组件包含如下操作接口，您需要先通过 selectComponent 获取 &lt;webrtc-room&gt; 标签的引用，之后就可以进行相应的操作了。

| 函数名                                          | 说明         |
|-------------------------------------------------|--------------|
| start()                                         | 启动     |
| pause()                                       | 暂停     |
| resume()                                     | 恢复    |
| stop()                                          | 停止     |
| switchCamera()                           | 切换摄像头   |
| enableVideo() | 打开或者关闭某一路画面 |
| enableAudio() | 打开或者关闭某一路声音 |
| sendC2CTextMsg(receiveUser, msg, succ, fail) | 发送C2C文本消息 |
| sendC2CCustomMsg(receiveUser, msgObj, succ, fail) | 发送C2C自定义消息 |
| sendGroupTextMsg(msg, succ, fail) | 发送群组文本消息 |
| sendGroupCustomMsg(msgObj, succ, fail) | 发送群组自定义消息 |

```
var webrtcroom = this.selectComponent("#webrtcroomid")
webrtcroom.pause();
```
#### enableVideo 

> 打开或者关闭某一路画面

`注意：该功能是模拟实现的，目前还不支持关闭对端的画面而只听对端的声音，这里的功能实现只是在画面上做了一层遮罩，达到一个伪效果，遮罩层的图片可以根据业务需要自行替换`

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
enable | Boolean | 是 | 打开/关闭画面
userid | Function | 是 | 要打开/关闭的画面的userid

#### enableAudio 

> 打开或者关闭某一路声音

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
enable | Boolean | 是 | 打开/关闭声音
userid | Function | 是 | 要打开/关闭的声音的userid

#### sendC2CTextMsg

> 发送C2C文本消息

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
receiveUser | String | 是 | 接收人的userid
msg | String | 是 | 消息内容
succ | Function | 否 | 发送成功的回调
fail | Function | 否 | 发送失败的回调

#### sendC2CCustomMsg

> 发送C2C自定义消息

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
receiveUser | String | 是 | 接收人的userid
msgObj | Object | 是 | {data: '消息内容', ext: '', desc: ''}
succ | Function | 否 | 发送成功的回调
fail | Function | 否 | 发送失败的回调

#### sendGroupTextMsg

> 发送群组文本消息

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
msg | String | 是 | 消息内容
succ | Function | 否 | 发送成功的回调
fail | Function | 否 | 发送失败的回调

#### sendGroupCustomMsg

> 发送群组自定义消息

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
msgObj | Object | 是 | {data: '消息内容', ext: '', desc: ''}
succ | Function | 否 | 发送成功的回调
fail | Function | 否 | 发送失败的回调


### 事件通知
**&lt;webrtc-room&gt;** 标签通过 **onRoomEvent** 返回内部事件，通过 **onIMEvent** 返回 IM 消息事件，事件参数格式如下

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

> 请确认已经参照 [Demo部署](/document/product/647/17000) 开通了相关服务和并正确的完成了配置。

### step1: 下载自定义组件源码

**&lt;webrtc-room&gt;** 并非微信小程序原生提供的标签，而是一个自定义组件，所以您需要额外的代码来支持这个标签。单击 [小程序源码](https://cloud.tencent.com/document/product/454/7873#XiaoChengXu) 下载源码包，您可以在 `wxlite` 文件夹下获取到所需文件。

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
    template="1v3"
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
| userID   | xiaoming  | 用户名 | 可以由您的服务器指定，或者使用小程序的openid  |
| userSig | 加密字符串  | 相当于 userid 对应的登录密码 | 由您的服务器签发（[PHP / JAVA](http://dldir1.qq.com/hudongzhibo/mlvb/sign_src_v1.0.zip)）|
| roomID | 12345  | 房间号 | 可以由您的服务器指定 |
| privateMapKey | 加密字符串  | 进房票据：相当于是进入 roomid 的钥匙 | 由您的服务器签发（[PHP / JAVA](http://dldir1.qq.com/hudongzhibo/mlvb/sign_src_v1.0.zip)）|

下载 [sign_src.zip](http://dldir1.qq.com/hudongzhibo/mlvb/sign_src_v1.0.zip) 可以获得服务端签发 userSig 和 privateMapKey 的计算代码（生成 userSig 和 privateMapKey 的签名算法是 **ECDSA-SHA256**）。

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


## Chrome端对接
 了解腾讯云官网的 [WebrtcAPI](https://cloud.tencent.com/document/product/647/16865) ，可以对接 Chrome 端的 H5 视频通话，因为不是本文档的重点，此处不做赘述。
