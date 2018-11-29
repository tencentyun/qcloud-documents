## 标签说明
**&lt;rtc-room&gt;** 标签是基于 &lt;live-pusher&gt; 和 &lt;live-player&gt; 实现的用于双人和多人音视频通话的自定义组件，其主要用于多对多音视频通话场景下（有别于&lt;live-room&gt;标签）。

## 效果演示
您可以扫描如下二维码，或在微信小程序里搜索“腾讯视频云”，即可打开我们的 demo 小程序，内部的 **双人音视频** 和 **多人音视频** 即为 &lt;rtc-room&gt; 的典型应用场景。
![](https://mc.qcloudimg.com/static/img/9851dba2c86161bc9e14a08b5b82dfd2/image.png)

## 标签详解
### 属性定义
| 属性      | 类型    | 值           | 说明       |
|:---------:|:---------:|:---------:|--------------|
| template  | String  | '1v3','1v1'             | 必要，标识组件使用的界面模版（用户如果需要自定义界面，请看[界面定制](#CustomUI)） |
| roomID    | String  | ‘’                      | 可选，房间号                           |
| roomName  | String  | ‘’                      | 可选，房间名  |
| beauty    | Number  | 0~5                     | 可选，默认5, 美颜级别 0～5  |
| muted     | Boolean | true, false             | 可选，默认false，是否静音    |
| debug     | Boolean | true, false             | 可选，默认false，是否打印推流debug信息   |
| bindonRoomEvent     | function |              | 必要，监听&lt;rtc-room&gt;组件返回的事件   |

### 操作接口

**&lt;rtc-room&gt;** 组件包含如下操作接口，您需要先通过 selectComponent 获取 &lt;rtc-room&gt; 标签的引用，之后就可以进行相应的操作了。

| 函数名                                          | 说明         |
|-------------------------------------------------|--------------|
| start()                                         | 启动     |
| pause()                                       | 暂停     |
| resume()                                     | 恢复    |
| stop()                                          | 停止     |
| switchCamera()                           | 切换摄像头   |
| sendTextMsg(text:String)             | 发送文本消息 |

```
var rtcroom = this.selectComponent("#rtcroomid")
rtcroom.pause();
```

### 事件通知
**&lt;rtc-room&gt;** 标签通过 **onRoomEvent** 返回内部事件，事件参数格式如下

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
<rtc-room id="rtcroomid"
	roomID="{{roomID}}"
	roomName="{{roomName}}"
	template="1v3"
	beauty="{{beauty}}"
	muted="{{muted}}"
	debug="{{debug}}"
	bindonRoomEvent="onRoomEvent">
</rtc-room>


// Page.js 文件
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
                //房间已经关闭
                break;
            }
            case 'error': {
                //发生错误
                var code = e.detail.code;
                var detail = e.detail.detail;
                break;
            }
            case 'recvTextMsg': {
                //收到文本消息
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
  		roomName: '测试',
  	});
	rtcroom.start();
  },

})
```



## 使用指引

### step1: 开通相关云服务

小程序音视频依赖腾讯云提供的直播（[LVB](https://console.cloud.tencent.com/live)）和云通讯（[IM](https://console.cloud.tencent.com/avc)）两项基础服务，您可以点击链接免费开通，其中云通讯服务开通即可使用，直播服务由于涉黄涉政风险较大，需要腾讯云人工审核开通。

### step2: 下载自定义组件源码

**&lt;rtc-room&gt;** 并非微信小程序原生提供的标签，而是一个自定义组件，所以您需要额外的代码来支持这个标签。点击 [小程序源码](https://cloud.tencent.com/document/product/454/7873#XiaoChengXu) 下载源码包，您可以在 `wxlite` 文件夹下获取到所需文件。

### step3: 登录房间服务（必需）

在使用 **&lt;rtc-room&gt;** 标签前需要先调用 `/utils/rtcroom.js` 的 `login` 方法进行登录，登录的目的是要连接后台房间服务（RoomService）。

```
var rtcroom = require('/utils/rtcroom.js');
...
rtcroom.login({
	serverDomain: '',
	userID: '',
	userSig: '',
	sdkAppID: '',
	accType: '',
  userName: '' //用户昵称，由客户自定义
});
```

参考 [DOC](https://cloud.tencent.com/document/product/454/14617#Server) 可以了解上面的这些参数应该怎么填写。

### step4: 获取房间列表（可选）
如果您不想自己实现房间列表，而是使用房间服务自带的房间列表，您可以通过调用 `/utils/rtcroom.js` 的 `getRoomList` 函数获取到列表信息。

```
var rtcroom = require('/utils/rtcroom.js');
...
rtcroom.getRoomList({
	data: {
		index: 0,  //列表索引号
		cnt: 20	 //要拉取的列表个数
	},
	success: function (ret) {
		console.log('获取房间列表:', ret.rooms);
	},
	fail: function (ret) {
		console.error('获取房间列表失败:', ret);
	}
});
```

### step5: 在工程中引入组件
- 在 page 目录下的 json 配置文件内引用组件，这一步是必须的，因为 &lt;rtc-room&gt; 并非原生标签。
```json
 "usingComponents": {
    "rtc-room": "/pages/rtc-room/rtc-room"
  }
```

- 在 page 目录下的 wxml 文件中使用标签
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

### step6: 如何创建房间

- 如果您希望由后台房间服务（RoomService）自动分配一个 roomid， 那么您只需要给 &lt;rtc-room&gt; 指定 roomName 就可以。

```
//创建房间（RoomService 自动分配 roomid）
this.setData({
	roomName: '测试'
});
rtcroom.start();
```

- 如果您希望自己指定 roomid， 那么您需要先设定 roomID 属性，才可以调用 start() 函数。

```
//创建房间 (由您来指定 roomid)
this.setData({
	roomID: 12345
});
rtcroom.start();
```

- 不论哪种方案，只有 **start()** 函数被调用时，房间才会真正的被创建。

### step7: 如何加入房间

- 如果一个 roomid 对应的房间已经被创建了，那么 start() 就不再是创建房间，而是直接进入房间。

```
this.setData({
	roomID: 12345
});
rtcroom.start();
```

<h2 id="CustomUI"> 界面定制 </h2>

如果我们默认实现的 "1v1" 和 "1v3" 两种界面布局不符合您的要求，您也可以根据项目需要对界面进行定制：

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

- **rtc-room 组件引入模版**

```html
//为 <rtc-room> 组件中的 liveroom.wxml 文件添加自定义模版
<import src='/pages/templates/mytemplate/mytemplate.wxml'/>
<view class='conponent-box'>
    <view styles="width:100%;height=100%;" wx:if="{{template=='1v3' || template=='1v1'}}">
        <template is='mytemplate' data="{{pushURL, aspect, 
				      minBitrate, maxBitrate, beauty, muted, debug, members}}"/>
    </view>
</view>

//为 <rtc-room> 组件中的 liveroom.wxss 文件添加自定义样式
@import "../templates/mytemplate/mytemplate.wxss";
```

<h2 id="PLATFORM">其它平台</h2>

**&lt;rtc-room&gt;** 也有 Windows、iOS、Android 等平台下的对等实现，您可以参考下表中的资料。同时， 阅读 [设计文档](https://cloud.tencent.com/document/product/454/14617)，您可以了解该解决方案的内部设计原理。

| 所属平台 | SDK下载 | 文档指引 |
|:-------:|:-------:|:-------:|
| Windows(C++) | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Windows) | [API](https://cloud.tencent.com/document/product/454/13672) |
| Windows(C#) | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Windows) | [API](https://cloud.tencent.com/document/product/454/13641) |
| IE浏览器 | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Windows) | [API](https://cloud.tencent.com/document/product/454/13651) |
| iOS | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#iOS) | [API](https://cloud.tencent.com/document/product/454/15156) |
| Android | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Android) | [API](https://cloud.tencent.com/document/product/454/15026) |

## 录制指引
- step1： [开通](https://console.cloud.tencent.com/video) 腾讯云点播服务。

- step2：进入[直播控制台](https://console.cloud.tencent.com/live)（小程序音视频流媒体是基于直播服务构建的），在【接入管理>>接入配置>>直播录制】中，开启录制功能。（注意：这里说的录制费用是按并发收费的，不是每一路都收费）
![](https://main.qcloudimg.com/raw/6dfeba07c25151be7025dab0245398ff.jpg)

- step3：在点播的[视频管理](https://console.cloud.tencent.com/video/videolist)界面中，您可以看到这些录制的文件，您也可以通过点播服务的 [REST API](https://cloud.tencent.com/document/product/266/10688) 获取到这些文件。
