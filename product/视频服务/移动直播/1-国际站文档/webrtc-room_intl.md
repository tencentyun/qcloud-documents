## Tag Overview
**&lt;webrtc-room&gt;** tag implemented based on &lt;live-pusher&gt; and ;live-player&gt; is a custom component used for interconnection with WebRTC. If you want to use &lt;live-pusher&gt; and &lt;live-player&gt; for integration, or to understand how the &lt;webrtc-room&gt; works, please see [DOC](https://cloud.tencent.com/document/product/454/16915)..

## Version Requirement
- Support for WeChat 6.6.6.

## Demo
- **PC**
Open the [experience page](https://sxb.qcloud.com/miniApp/) with the Chrome browser to use WebRTC for PC.

- **WeChat**
Go to **Discover** -> **Mini Programs**, then search for **Tencent Video Cloud**, and click WebRTC feature tab to experience the intercommunication with Chrome for PC.

![](https://main.qcloudimg.com/raw/00d3215b9865159429097ad7a9df4395.jpg)

## Source Code for Integration

| Source Code for Integration | Description | Github Address |
|---------|---------|---------|
| Mini Program source code | Includes component source code of &lt;webrtc-room&gt; and demo source code | [Go](https://github.com/TencentVideoCloudMLVBDev/rtcroom_wxlite) |
| PC-end source code | Source code for the integration of WebRTC for Chrome implemented based on [WebrtcAPI](https://cloud.tencent.com/document/product/647/16865) (where, component/WebRTCRoom.js implements a simple room management feature, and component/mainwindow.js contains the code for using WebRTC API) | [Go](https://github.com/TencentVideoCloudMLVBDev/webrtc_pc)|
| Backend source code | Implements a simple room list feature, and also contains the code for generating parameters required for &lt;webrtc-room&gt; | [Go](https://github.com/TencentVideoCloudMLVBDev/webrtc_server_java) |

## Tag Description
### Attributes
| Attribute | Type | Value | Description |
|:---------:|:---------:|:---------:|--------------|
| template | String | '1v3' | (Required) Identifies the UI template used by components (If you need to customize the UI, please see [UI Customization](#CustomUI)) |
| sdkAppID    | String  | '' | (Required) The AppID obtained when you activate the IM service |
| userID     | String  | '' | (Required) User ID |
| userSig    | String  | '' | (Required) Identity signature, which functions as a login password |
| roomID    | Number  | '' | (Required) Room ID |
| privateMapKey    | String  | '' | (Required) Room permission key, equivalent to the key for joining a room with the specified room ID |
| beauty    | Number   | 0-5 | (Optional) Beauty filter level: 0-5. Default is 5 |
| muted     | Boolean | true, false  | (Optional) Whether to mute. Default is false |
| debug     | Boolean | true, false | (Optional) Whether to print push debug information. Default is false |
| bindRoomEvent     | function | | (Required) Listens the events returned by &lt;webrtc-room&gt; component |
| enableIM     | Boolean | true, false  | (Optional) Default is false |
| bindIMEvent     | function | | Required when IM is enabled. It listens the events returned by IM |

### APIs

**&lt;webrtc-room&gt;** component contains the following APIs. You need to obtain the reference of the &lt;webrtc-room&gt; tag using selectComponent before performing appropriate operations.

| Function Name | Description |
|-------------------------------------------------|--------------|
| start()    | Start |
| pause()    | Pause |
| resume()  | Resume |
| stop()      | Stop |
| switchCamera()  | Switch camera |

```
var webrtcroom = this.selectComponent("#webrtcroomid")
webrtcroom.pause();
```

### Event notification
**&lt;webrtc-room&gt;** tag returns internal events through **onRoomEvent** and IM message events through **onIMEvent**. The format of the event parameters is as follows:

```json
"detail": {
  "tag": "The unique event tag ID",
  "code": "Event code",
  "detail": "Detailed parameters of the event"
}
```

### Sample Code
```
//Page.wxml file
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


//Page.js file
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
                //An error occurred
                var code = e.detail.code;
                var detail = e.detail.detail;
                break;
            }
        }
    },
    onIMEvent: function(e){
        switch(e.detail.tag){
            case 'big_group_msg_notify':
                //Receive a group message
                console.debug( e.detail.detail )
                break;
            case 'login_event':
                //Notification of login event
                console.debug( e.detail.detail )
                break;
            case 'connection_event':
                //Connection event
                console.debug( e.detail.detail )
                break;
            case 'join_group_event':
                //Notification of joining a group
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



## Usage Guide

### Step 1: Activate appropriate cloud service

The interconnection between Mini Programs and WebRTC is implemented based on the Tencent-RTC ([TRTC](https://cloud.tencent.com/product/trtc))) service which needs to be activated.

- Log in to the TRTC [console](https://console.cloud.tencent.com/rav). If you have not activated this service, click **Apply** to go to Tencent Cloud's manual audit stage. The service is activated upon the approval of your application.

- After the service is activated, log in to the [console](https://console.cloud.tencent.com/rav), then create a TRTC application, and click **OK**.
![](https://main.qcloudimg.com/raw/20d0adeadf23251f857571a65a8dd569.png)

- Get `sdkAppID, accountType, privateKey` used in Step 4 from the TRTC console:
![](https://main.qcloudimg.com/raw/9a5f341883f911cf9b65b9b5487f2f75.png)

### Step 2: Download custom component source code

**&lt;webrtc-room&gt;** is not a native tag provided by WeChat Mini Program, but a custom component. Therefore, you need additional code to support this tag. Click the link to [Mini Program source code](https://cloud.tencent.com/document/product/454/7873#XiaoChengXu)  to download the source code package, and you can obtain the required files under the `wxlite` folder.

### Step 3: Introduce the component into the project
- Reference the component in the json configuration file under the page directory. This is required because &lt;webrtc-room&gt; is not a native tag.
```json
 "usingComponents": {
    "webrtc-room": "/pages/webrtc-room/webrtc-room"
  }
```

- Use the tag in the wxml file under the page directory.
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

### Step 4: Get key information
Get the key information according to the following table. These keys are required to use Tencent Cloud ILVB service.

| KEY | Example | Role | How to Get |
|:--------:|:--------:|:--------:|:--------:|
| sdkAppID | 1400087915 | Used for billing and business differentiation | You can get it from Step 1 |
| userID | xiaoming | User ID | It can be specified by your server or you can use the openid of Mini Program |
| userSig | Encrypted string | Equivalent to the login password corresponding to the userid | Issued by your server ([PHP/JAVA](http://dldir1.qq.com/hudongzhibo/mlvb/sign_src_v1.0.zip)) |
| roomID | 12345 | Room ID | Specified by your server |
| privateMapKey | Encrypted string | Ticket for joining a room, equivalent to the key used to enter a room with the specified roomid | Issued by your server ([PHP / JAVA](http://dldir1.qq.com/hudongzhibo/mlvb/sign_src_v1.0.zip)) |

Download [sign_src.zip](http://dldir1.qq.com/hudongzhibo/mlvb/sign_src_v1.0.zip) to get the calculation code for the server to issue userSig and privateMapKey. The algorithm for generating userSig and privateMapKey signatures is **ECDSA-SHA256**.

### Step 5: Join the room

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

<h2 id="CustomUI"> UI customization </h2>

- **Create a UI template**

```html
//Step 1: Create a /pages/templates/mytemplate folder and mytemplate.wxml and mytemplate.wxss files.

//Step 2: Write the mytemplate.wxml and mytemplate.wxss files.
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
                <cover-view class='character' style='padding: 0 5px;'>Me</cover-view>
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

- **Introduce a template into the webrtc-room component**

```html
//Add a custom template for the webrtcroom.wxml file in the <webrtc-room> component
<import src='/pages/templates/mytemplate/mytemplate.wxml'/>
<view class='conponent-box'>
    <view styles="width:100%;height=100%;" wx:if="{{template=='1v3'}}">
        <template is='mytemplate' data="{{pushURL, aspect,
				      minBitrate, maxBitrate, beauty, muted, debug, members}}"/>
    </view>
</view>

//Add a custom style for the webrtcroom.wxss file in the <webrtc-room> component
@import "../templates/mytemplate/mytemplate.wxss";
```


## Integration with Chrome
 Integration of H5 video chat in Chrome by referring to the [WebrtcAPI](https://cloud.tencent.com/document/product/647/16865) , on the Tencent Cloud official website, which will not be discussed here.

