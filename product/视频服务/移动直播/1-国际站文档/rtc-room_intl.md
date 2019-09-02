## Tag Overview
The **&lt;rtc-room&gt;** tag implemented based on &lt;live-pusher&gt; and &lt;live-player&gt; is a custom component used for audio/video chats among two or more people. It is mainly suitable for many-to-many audio/video chat scenarios (unlike &lt;live-room&gt;).

## Demo
You can scan the following QR code or search **Tencent Video Cloud** in WeChat Mini Program to open the demo mini program. The **two-person audio/video chats** and **multi-person audio/video chats** in the demo is the typical application scenario of &lt;rtc-room&gt;.
![](https://mc.qcloudimg.com/static/img/9851dba2c86161bc9e14a08b5b82dfd2/image.png)

## Tag Description
### Attributes
| Attribute | Type | Value | Description |
|:---------:|:---------:|:---------:|--------------|
| template  | String  | '1v3','1v1'             | (Required) Identifies the UI template used by components (If you need to customize the UI, please see [UI Customization](#CustomUI)) |
| roomID    | String  | ''                      | (Optional) Room ID |
| roomName  | String  | ''                      | (Optional) Room name |
| beauty | Number | 0-5 | (Optional) Beauty filter level: 0-5. Default is 5 |
| muted     | Boolean | true, false             | (Optional) Whether to mute. Default is false |
| debug     | Boolean | true, false             | (Optional) Whether to print push debug information. Default is false |
| bindonRoomEvent     | function |              | (Required) Listens the events returned by &lt;rtc-room&gt; component |

### APIs

The **&lt;rtc-room&gt;** component contains the following APIs. You need to obtain the reference of the &lt;rtc-room&gt; tag using selectComponent before performing appropriate operations.

| Function Name | Description |
|-------------------------------------------------|--------------|
| start()                                         | Start |
| pause()                                       | Pause |
| resume()                                     | Resume |
| stop()                                          | Stop |
| switchCamera()                           | Switch camera |
| sendTextMsg(text:String)             | Send text messages |

```
var rtcroom = this.selectComponent("#rtcroomid")
rtcroom.pause();
```

### Event notification
The **&lt;rtc-room&gt;**  tag returns internal events through **onRoomEvent**. The format of the event parameters is as follows:

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
<rtc-room id="rtcroomid"
	roomID="{{roomID}}"
	roomName="{{roomName}}"
	template="1v3"
	beauty="{{beauty}}"
	muted="{{muted}}"
	debug="{{debug}}"
	bindonRoomEvent="onRoomEvent">
</rtc-room>


//Page.js file
Page({
    data: {
    	//...
        roomID: '',
        roomName: '',
        beauty: 3,
        muted: false,
        debug: false,
    },
    //...
    onRoomEvent: function(e){
        switch(e.detail.tag){
            case 'roomClosed': {
                //Room is closed
                break;
            }
            case 'error': {
                //An error occurred
                var code = e.detail.code;
                var detail = e.detail.detail;
                break;
            }
            case 'recvTextMsg': {
                //Receive a text message
                var text = e.detail.detail;
                break;
            }
        }
    },

  onShow: function () {
  },

  onHide: function () {
  },
  
  onRead: function() {
  	var rtcroom = this.selectComponent("#rtcroomid")
  	this.setData({
  		roomName: 'Test',
  	});
	rtcroom.start();
  },

})
```



## Usage Guide

### Step 1: Activate appropriate cloud service

Audio/video capability for mini programs relies on Tencent Cloud [LVB](https://console.cloud.tencent.com/live) and [IM](https://console.cloud.tencent.com/avc) services, which can be activated free of charge by clicking the link. IM service can be used immediately once activated. LVB service that has a high risk of posting pornographic and political content requires users to go through Tencent Cloud's manual audit.

### Step 2: Download custom component source code

**&lt;rtc-room&gt;** is not a native tag provided by WeChat Mini Program, but a custom component. Therefore, you need additional code to support this tag. Click [Mini Program Source Code](https://cloud.tencent.com/document/product/454/7873#XiaoChengXu) to download the source code package, and you can obtain the required files under the `wxlite` folder.

### Step 3: Log in to RoomService (Required)

Before using the **&lt;rtc-room&gt;** tag, log in first by calling `/utils/rtcroom.js` to connect to RoomService in the backend.

```
var rtcroom = require('/utils/rtcroom.js');
...
rtcroom.login({
	serverDomain: '',
	userID: '',
	userSig: '',
	sdkAppID: '',
	accType: '',
  userName: '' //Custom user nickname
});
```

For more information about how to enter parameters, please see [DOC](https://cloud.tencent.com/document/product/454/14617#Server).

### Step 4: Get room lists (optional)
If you want to use the existing room list of RoomService, rather than implementing a new one, you can obtain the list information by calling the `getRoomList` function of `/utils/rtcroom.js`.

```
var rtcroom = require('/utils/rtcroom.js');
...
rtcroom.getRoomList({
	data: {
		index: 0,  //List index number
		cnt: 20	 //Number of lists to be pulled
	},
	success: function (ret) {
		console.log('Get room lists:', ret.rooms);
	},
	fail: function (ret) {
		console.error('Failed to get room lists :', ret);
	}
});
```

### Step 5: Introduce the component into the project
- Reference the component in the JSON configuration file under the page directory. This is required because &lt;rtc-room&gt; is not a native tag.
```json
 "usingComponents": {
    "rtc-room": "/pages/rtc-room/rtc-room"
  }
```

- Use the tag in the wxml file under the page directory.
```xml
<rtc-room id="rtcroomid"
	roomID="{{roomID}}"
	roomName="{{roomName}}"
	template="1v3"
	beauty="{{beauty}}"
	muted="{{muted}}"
	debug="{{debug}}"
	bindonRoomEvent="onRoomEvent">
</rtc-room>
```

### Step 6: Create a room

- If you want to use the roomID assigned by RoomService, specify a roomName for &lt;rtc-room&gt;.

```
//Create a room (a roomID assigned by RoomService)
this.setData({
	roomName: 'Test'
});
rtcroom.start();
```

- If you want to specify a roomID, set the roomID attribute before calling the start() function.

```
//Create a room (a roomID that you specify)
this.setData({
	roomID: 12345
});
rtcroom.start();
```

- In either case, a room is created only when the **start()** function is called.

### Step 7: Join a room

- If a room with a specified roomID has already been created, calling start() will enter the created room, rather than creating a new one.

```
this.setData({
	roomID: 12345
});
rtcroom.start();
```

<h2 id="CustomUI"> UI customization </h2>

If the default "1v1" and "1v3" screen layouts do not suite your needs, you can customize the screen based on the specific project:

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

- **Introduce a template into the rtc-room component**

```html
//Add a custom template for the liveroom.wxml file in the <rtc-room> component
<import src='/pages/templates/mytemplate/mytemplate.wxml'/>
<view class='conponent-box'>
    <view styles="width:100%;height=100%;" wx:if="{{template=='1v3' || template=='1v1'}}">
        <template is='mytemplate' data="{{pushURL, aspect, 
				      minBitrate, maxBitrate, beauty, muted, debug, members}}"/>
    </view>
</view>

//Add a custom style for the liveroom.wxss file in the <rtc-room> component
@import "../templates/mytemplate/mytemplate.wxss";
```

<h2 id="PLATFORM">Other platforms</h2>

**&lt;rtc-room&gt;** can also be implemented in Windows, iOS, and Android platforms. Available references are listed in the following table. For more information about how it works, please see [Design Documentation](https://cloud.tencent.com/document/product/454/14617).

| Platform | SDK Download | API Documentation |
|:-------:|:-------:|:-------:|
| Windows(C++) | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Windows) | [API](https://cloud.tencent.com/document/product/454/13672) |
| Windows(C#) | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Windows) | [API](https://cloud.tencent.com/document/product/454/13641) |
| IE browser | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Windows) | [API](https://cloud.tencent.com/document/product/454/13651) |
| iOS | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#iOS) | [API](https://cloud.tencent.com/document/product/454/15156) |
| Android | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Android) | [API](https://cloud.tencent.com/document/product/454/15026) |

## Recording
- Step 1: [Activate](https://console.cloud.tencent.com/video) Tencent Cloud VOD service.

- Step 2: Log in to the [LVB console](https://console.cloud.tencent.com/live) (based on which the Mini Program audio/video streaming media is built), enable recording feature by going to **Access Management** -> **Access Configuration** -> **LVB Recording**. (Note: The recording fee is charged by the number of concurrent LVB recordings.)
![](https://main.qcloudimg.com/raw/6dfeba07c25151be7025dab0245398ff.jpg)

- step3: These recorded files can be found on the [Video Management](https://console.cloud.tencent.com/video/videolist) interface of VOD, or obtained by calling the [REST API](https://cloud.tencent.com/document/product/266/10688) of VOD.

