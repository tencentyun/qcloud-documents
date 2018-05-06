## 标签说明
**&lt;webrtc-room&gt;** 标签是基于 &lt;live-pusher&gt; 和 &lt;live-player&gt; 实现的用于 WebRTC 互通的自定义组件。如果您希望直接使用 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签完成对接，或者想要了解 &lt;webrtc-room&gt; 的内部原理，可以参考 [DOC](https://cloud.tencent.com/document/product/454/16915)。

## 版本要求
- 微信 6.6.6 版本开始支持。

## 效果演示
- **PC 端**
用 Chrome 浏览器打开 [体验页面](https://avc.qcloud.com/miniApp/index.html) 可以体验桌面版 WebRTC 的效果。

- **微信端**
发现=>小程序=>搜索“腾讯视频云”，点击 WebRTC 功能卡，就可以体验跟桌面版 Chrome 互通的效果了。

![](https://main.qcloudimg.com/raw/81edf044e0a40ccfd4794b91185f1f82.jpg)

## 对接资料

| 对接资料 | 说明 | 下载链接 |
|---------|---------|---------|
| 小程序源码 | 包含&lt;webrtc-room&gt;的组件源码以及demo源码 | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#XiaoChengXu) |
| PC端源码 | 基于[WebRTC API](https://sxb.qcloud.com/webrtcapi/)实现的Chrome版WebRTC接入源码（其中 component/WebRTCRoom.js 实现了一个简单的房间管理功能，component/mainwindow.js包含了对 WebRTC API 的使用代码） | [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/webRTCForChrome/WebRTC_20180428_093242.zip) |
| 后台源码 | 实现了一个简单的房间列表功能，同时包含&lt;webrtc-room&gt;几个所需参数的生成代码 | [DOWNLOAD](http://download-1252463788.file.myqcloud.com/server/java/webrtc.zip) |

## 标签详解
### 属性定义
| 属性      | 类型    | 值           | 说明       |
|:---------:|:---------:|:---------:|--------------|
| template  | String  | '1v3'             | 必要，标识组件使用的界面模版（用户如果需要自定义界面，请看[界面定制](#CustomUI)） |
| roomID    | Number  | ‘’                      | 必要，房间号                           |
| userID     | String  | ''                   |必要，用户ID |
| userSig    | String  | ‘’                      | 必要，身份签名，相当于登录密码的作用    |
| sdkAppID    | String  | ‘’                      | 必要，开通IM服务所获取到的AppID       |
| privateMapKey    | String  | ‘’                 | 必要，视频权限位，相当于进入房间的钥匙      |
| beauty    | Number  | 0~5                     | 可选，默认5, 美颜级别 0～5  |
| muted     | Boolean | true, false             | 可选，默认false，是否静音    |
| debug     | Boolean | true, false             | 可选，默认false，是否打印推流debug信息   |
| bindRoomEvent     | function |              | 必要，监听&lt;webrtc-room&gt;组件返回的事件   |
| enableIM     | Boolean | true, false             | 可选，默认false   |
| bindIMEvent     | function |             | 当IM开启时必要，监听IM返回的事件   |

### 操作接口

**&lt;webrtc-room&gt;** 组件包含如下操作接口，您需要先通过 selectComponent 获取 &lt;webrtc-room&gt; 标签的引用，之后就可以进行相应的操作了。

| 函数名                                          | 说明         |
|-------------------------------------------------|--------------|
| start()                                         | 启动     |
| pause()                                       | 暂停     |
| resume()                                     | 恢复    |
| stop()                                          | 停止     |
| switchCamera()                           | 切换摄像头   |

```
var webrtcroom = this.selectComponent("#webrtcroomid")
webrtcroom.pause();
```

### 事件通知
**&lt;webrtc-room&gt;** 标签通过 **onRoomEvent** 返回内部事件，通过 **onIMEvent** 返回IM消息事件，事件参数格式如下

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

### step1: 开通相关云服务

在腾讯云注册账号，开通 [互动直播](https://console.cloud.tencent.com/ilvb) 服务，创建一个新的应用，可以获得 SDK Appid 信息，也就是下图中红框标注的位置。

![](https://main.qcloudimg.com/raw/b376d943ae028b87eaa19a404f66334a.png)

> 小程序跟WebRTC的互通是使用互动直播服务“牵线搭桥”的，如果您之前使用的是直播服务，需要再开通一下互动直播服务。

### step2: 下载自定义组件源码

**&lt;webrtc-room&gt;** 并非微信小程序原生提供的标签，而是一个自定义组件，所以您需要额外的代码来支持这个标签。点击 [小程序源码](https://cloud.tencent.com/document/product/454/7873#XiaoChengXu) 下载源码包，您可以在 `wxlite` 文件夹下获取到所需文件。

### step3: 在工程中引入组件
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

### step4: 获取key信息
按照如下表格获取关键的key信息，这是使用腾讯云互通直播服务所必须的几个信息：

| KEY | 示例    | 作用 |获取方案 |
|:--------:|:--------:|:--------:|:--------:|
| sdkAppID | 1400087915  | 用于计费和业务区分 |  上文中有介绍 |
| userID   | xiaoming  | 用户名 | 可以由您的服务器指定，或者使用小程序的openid  |
| userSig | 加密字符串  | 相当于 userid 对应的登录密码 | 由您的服务器签发（PHP / JAVA） |
| roomID | 12345  | 房间号 | 可以由您的服务器指定 |
| privateMapKey | 加密字符串  | 进房票据：相当于是进入 roomid 的钥匙 | 由您的服务器签发（PHP / JAVA）|

下载 [sign_src.zip](http://dldir1.qq.com/hudongzhibo/mlvb/sign_src_v1.0.zip) 可以获得服务端签发 userSig 和 privateMapKey 的示例代码。

>生成 usersig 和 privMapEncrypt 的签名算法是 **ECDSA-SHA256**。

### step5: 进入房间

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