本文为您介绍小程序云直播插件解决方案的制定。

## 注册腾讯云账号
注册 [腾讯云账号](https://cloud.tencent.com/document/product/378/17985)，并完成 [企业实名认证](https://cloud.tencent.com/document/product/378/10496)。注册完成后，提供腾讯云账号 APPID 和 bizname。bziname 为您的唯一品牌标识，将会在域名前缀等被使用。bziname 一旦确定不可变更。

## 注册小程序
在 [微信公众平台](https://mp.weixin.qq.com) 注册并登录小程序。小程序类目请根据您的实际场景选择。

## 安装微信小程序开发工具
下载并安装最新版本的 [微信开发者工具](https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html)，使用小程序绑定的微信号扫码登录开发者工具。
![](https://main.qcloudimg.com/raw/366e52aa9cc84949271b87a4678da636.png)

## 推流及拉流
1. 配置防盗链
直播防盗链用于对推流端/播放端身份的权限鉴定，通过使用加密算法对推流 URL 或者播放 URL 进行加密，防止非法用户恶意盗推或者盗播。您可以提供推流密钥/播放密钥到腾讯云为您配置推流防盗链/播放防盗链。默认情况下，为您自动开启推流防盗链配置。
2. 生成推流/播放地址
打开`https://bizlive.myqcloud.com/tools/address.html?bizname=bizname`工具页面（URL 中的 bizname 参数为您的 bizname），您可以在工具页面中填写流名称和鉴权密钥，自动生成推流和播放地址。

## 什么是小程序插件？
 使用前，请先阅读微信小程序提供的 [插件文档](https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/)，了解插件的使用范围和限制。

## 如何使用插件？
### 申请插件使用权限
在小程序管理后台的"设置-第三方设置"中选择"添加插件"，在弹出的面板中搜索"腾讯云直播助手"，选中插件并添加。

### 在小程序中引入插件代码
在小程序中引入插件代码，可参考 [demo 源码](https://bizlive-1258550678.cos.ap-chengdu.myqcloud.com/plugin-demo.zip)。使用插件前需在小程序工程的`app.json`中声明要使用的插件，例如：
```
{
  ……
  "plugins": {
      "liveRoomPlugin": {
          "version": "1.1.3",
          "provider": "wx95a7d2b78cf30f98"
      }
  }
}
```

### 小程序使用插件中的播放组件
####  播放组件
在 page 的`.json`文件中定义需要引入的`live-room-play`组件，使用`plugin://`协议。
```js
{
    "usingComponents": {
        "live-room-play": "plugin://liveRoomPlugin/live-room-play"    //播放组件
    }
}
```
在 page 的`.wxml`文件加载上一步引入的`live-room-play`组件。
```xml
<view class="container-box">
<view class="player-view">
  <live-room-play liveAppID="1258550678" playUrl="{{playUrl}}" orientation="{{orientation}}" objectFit="{{objectFit}}"
    minCache="{{minCache}}" maxCache="{{maxCache}}" mode="{{mode}}" muted="{{muted}}" debug="{{debug}}" bindPlayEvent="onPlayEvent" >
  </live-room-play>
</view>
</view>
```
#### 推流组件
在 page 的`.json`文件中定义需要引入的`live-room-push`组件，使用`plugin://`协议。
```
{
    "usingComponents": {
        "live-room-push": "plugin://liveRoomPlugin/live-room-push"    //推流组件
    }
}
```
在 page 的`.wxml`文件加载上一步引入的`live-room-push`组件。
```xml
<live-room-push liveAppID="{{liveAppID}}" pushUrl="{{pushUrl}}" orientation="{{orientation}}" muted="{{muted}}" mode="{{mode}}" waitingImage="{{waitingImage}}" enableCamera="{{enableCamera}}" beauty="{{beauty}}" whiteness="{{whiteness}}" backgroundMute="{{backgroundMute}}"
  debug="{{debug}}" autoFocus="{{autoFocus}}" aspect="{{aspect}}" minBitrate="{{minBitrate}}" maxBitrate="{{maxBitrate}}" zoom="{{zoom}}" devicePosition="{{devicePosition}}" sdkAppID="{{sdkAppID}}" accountType="{{accountType}}" userID="{{userID}}" userSig="{{userSig}}"
  roomID="{{roomID}}" nickName="{{nickName}}" avatar="{{avatar}}" bindPushEvent="onPushEvent" bindIMEvent="onIMEvent">
```
#### PPT 及电子白板组件
在 page 的`.json`文件中定义需要引入的`tic-component`组件，使用`plugin://`协议。
```js
{
    "usingComponents": {
        "tic-component": "plugin://liveRoomPlugin/tic-component"    //PPT及电子白板组件
    }
}
```
在 page 的`.wxml`文件加载上一步引入的`tic-component`组件。
```xml
<tic-coxmlmponent userId="{{userId}}" sdkAppId="{{sdkAppId}}" userSig="{{userSig}}">
<!--内嵌HTML代码-->
</tic-component>
```
#### 直播播放组件相关的属性说明

| 属性                      | 类型        | 默认值     | 必填 | 说明                                                         |
| :------------------------ | :---------- | :--------- | :--- | :----------------------------------------------------------- |
| liveAppID                 | Number      | 0          | 是   | 用户的腾讯云 appid                                            |
| playUrl                   | String      | ""         | 是   | 通过使用`https://bizlive.myqcloud.com/tools/address.html?bizname=bizname`工具页面获取 |
| mode                      | String      | "live"     | 否   | live（直播），RTC（实时通话，该模式延时更低）                |
| orientation               | String      | "vertical" | 否   | 画面方向，可选值有 vertical，horizontal                      |
| objectFit                 | String      | "contain"  | 否   | 填充模式，可选值有 contain，fillCrop                         |
| minCache                  | Number      | 1          | 否   | 最小缓冲区，单位 s                                            |
| maxCache                  | Number      | 3          | 否   | 最大缓冲区，单位 s                                            |
| muted                     | Boolean     | false      | 否   | 是否静音                                                     |
| debug                     | Boolean     | false      | 否   | 是否显示日志                                                 |
| soundMode                 | String      | 'speaker'  | 否   | 声音输出设备，'speaker'或者'ear'，代表扬声器或听筒           |
| autoplay                  | Boolean     | false      | 否   | 是否自动播放                                                 |
| autopause                 | Boolean     | true       | 否   | 页面跳转时是否自动暂停                                       |
| sdkAppId                  | String      | ""         | 否   | IM 应用的 appid，如果不需要启用内置 IM，可以不填                |
| userID                    | String      | "not set"  | 否   | 用户在 IM 内的唯一 ID                                           |
| userSig                   | String      | "not set"  | 否   | 用户的 IM 登录签名，签名一般由服务端根据 IM 应用的公私钥生成     |
| roomID                    | String      | "not set"  | 否   | 房间 ID                                                       |
| nickName                  | String      | "not set"  | 否   | 用户在 IM 里的昵称                                             |
| avatar                    | String      | "not set"  | 否   | 用户在 IM 里的头像 url                                          |
| bindPlayEvent             | EventHandle | null       | 否   | 播放状态变化事件回调                                         |
| bindfullscreenChangeEvent | EventHandle | null       | 否   | 全屏状态变化事件回调                                         |
| bindNetStatus             | EventHandle | null       | 否   | 网络状态变化回调                                             |
| bindAttachedEvent         | EventHandle | null       | 否   | 插件加载完成回调                                             |
| bindIMEvent               | EventHandle | null       | 否   | 播放组件内置的 IM 事件回调                                     |

#### 直播推流组件相关属性说明

| 属性              | 类型        | 默认值     | 必填 | 说明                                                         |
| :---------------- | :---------- | :--------- | :--- | :----------------------------------------------------------- |
| liveAppID         | Number      | 0          | 是   | 直播 appid                                                    |
| pushUrl           | String      | ""         | 是   | 直播推流地址                                                 |
| orientation       | String      | "vertical" | 否   | 推流画面方向，可选值有 vertical，horizontal                  |
| muted             | Boolean     | false      | 否   | 是否静音                                                     |
| mode              | String      | "SD"       | 否   | 清晰度，可选值：SD（标清），HD（高清），FHD（超清），RTC（实时通话） |
| waitingImage      | String      | ""         | 否   | 进入后台推流时候的垫片图片                                   |
| enableCamera      | Boolean     | true       | 否   | 是否开启摄像头                                               |
| beauty            | Number      | 0          | 否   | 美颜指数，取值0 - 9，数值越大效果越明显                     |
| whiteness         | Number      | 0          | 否   | 美白指数，取值0 - 9，数值越大效果越明显                     |
| backgroundMute    | Boolean     | false      | 否   | 进入后台时是否静音，初始化设置生效                           |
| debug             | Boolean     | false      | 否   | 是否显示日志                                                 |
| autoFocus         | Boolean     | true       | 否   | 自动聚焦，初始化设置生效                                     |
| aspect            | String      | "9:16"     | 否   | 宽高比，可选值有3:4，9:16                                   |
| minBitrate        | Number      | 200        | 否   | 最小码率，仅在 mode 为"RTC"的时候生效                          |
| maxBitrate        | Number      | 1000       | 否   | 最大码率，仅在 mode 为"RTC"的时候生效                          |
| zoom              | Boolean     | false      | 否   | 自动调整焦距，初始化设置生效                                 |
| devicePosition    | String      | "front"    | 否   | 摄像头前置或后置，值为 front，back。注意这个值只是在组件初始化时生效，不能动态修改。动态切换摄像头用接口 switchCamera |
| audioQuality      | String      | 'high'     | 否   | 录音质量，'high'或者'low'                                    |
| mirror            | Boolean     | false      | 否   | 是否镜像反转                                                 |
| autopush          | Boolean     | true       | 否   | 是否自动推流                                                 |
| sdkAppId          | String      | ""         | 否   | IM 应用的 appid，如果不需要启用内置 IM，可以不填                |
| userID            | String      | "not set"  | 否   | 用户在 IM 内的唯一 ID                                           |
| userSig           | String      | "not set"  | 否   | 用户的 IM 登录签名，签名一般由服务端根据 IM 应用的公私钥生成     |
| roomID            | String      | "not set"  | 否   | 房间 ID                                                       |
| nickName          | String      | "not set"  | 否   | 用户在 IM 里的昵称                                             |
| avatar            | String      | "not set"  | 否   | 用户在 IM 里的头像 url                                          |
| bindPushEvent     | EventHandle | null       | 否   | 推流状态变化事件回调                                         |
| bindNetStatus     | EventHandle | null       | 否   | 网络状态变化事件回调                                         |
| bindError         | EventHandle | null       | 否   | 推流错误回调                                                 |
| bindBgmStart      | EventHandle | null       | 否   | 背景音乐开始播放回调                                         |
| bindBgmProgress   | EventHandle | null       | 否   | 背景音乐进度回调                                             |
| bindBgmComplete   | EventHandle | null       | 否   | 背景音乐播放完成回调                                         |
| bindAttachedEvent | EventHandle | null       | 否   | 插件加载完成回调                                             |

#### PPT 及电子白板组件属性列表

| 属性     | 类型   | 默认值 | 必填 | 说明                 |
| :------- | :----- | :----- | :--- | :------------------- |
| sdkAppId | Number | -1     | 是   | 用户申请 IM 的 SDKAppID |
| userId   | String | ""     | 是   | 用户登录 IM 的唯一标识 |
| userSig  | String | ""     | 是   | 用户登录 IM 所需的签名 |

### 在播放区域叠加额外展示信息
组件提供了一个`<slot>`节点，用于承载组件引用时提供的子节点。本功能受限于微信，只能在组件上叠加`cover-image`、`cover-view`和`canvas`。

## 组件实例化

### 获取 live-room-play 组件实例
#### 为什么要获取 live-room-play 组件实例？
 live-room 组件支持播放、停止播放、全屏等接口，要调用这些接口需要先获取到 live-room-play 的实例。

#### 怎么获取 live-room-play 组件实例？
live-room-play 是腾讯视频云直播插件中的一个组件，在腾讯视频云直播插件中暴露了获取 live-room-play 组件实例的接口，您只需要先在 page 的`.js`文件中，将插件加载进来，即可获取到 live-room-play 组件实例。
```js
// 加载插件
var plugin = requirePlugin("liveRoomPlugin")
// 获取live-room组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
```

### 获取 live-room-push 组件实例
具体步骤同上 [获取 live-room-play 组件实例](#.E8.8E.B7.E5.8F.96-live-room-play-.E7.BB.84.E4.BB.B6.E5.AE.9E.E4.BE.8B)。

## 组件接口
### live-room-play 组件提供如下接口
- start
开始播放。调用之后会启动播放。在开始播放之前，`playUrl`也要保证已经设置到组件属性中。
```
// 获取live-room-play组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.start();
```
- stop
结束播放。
```
// 获取live-room-play组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.stop();
```
- requestFullScreen
全屏播放。
```
// 获取live-room-play组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.requestFullScreen(true);        //全屏播放
//liveRoomComponent.requestFullScreen(false);    //退出全屏
```
- pause
暂停播放。
```
// 获取live-room-play组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.pause();        //暂停播放
```
- resume
恢复播放。
```
// 获取live-room-play组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.resume();        //恢复播放
```
- mute
静音。
```
// 获取live-room-play组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.mute();        //静音
```
- 如果小程序需要后台播放纯音频流，可以使用纯音频的转码流进行播放，示例代码如下：
```
this.audio = wx.getBackgroundAudioManager();
this.audio.protocol = 'hls';// 这个属性设置为hls才支持m3u8类型的直播流
this.audio.title = '后台音乐';// 显示在状态栏的标题
this.audio.src = "http://domain/live/streamName_pureAudio.m3u8?txSecret=xxxx&txTime=xxxxx"; 
// 注：domain是PaaS插件申请时我方提供的，streamName是指定的流名称，
// 后面加_pureAudio就是纯音频转码流，后台播放时可以节省流量 。
```

### live-room-push 组件提供如下接口
- start
开始推流。调用之后会启动推流。在开始推流之前，`pushUrl`也要保证已经设置到组件属性中。
```
// 获取live-room-push组件实例
var liveRoomPushComponent = plugin.instance.getLiveRoomPushInstance();
liveRoomPushComponent.start();
```
- stop
结束推流。
```
// 获取live-room-push组件实例
var liveRoomPushComponent = plugin.instance.getLiveRoomPushInstance();
liveRoomPushComponent.stop();
```
- snapshot
截图。
```
liveRoomPushComponent.snapshot({
    success: function (res){
       wx.saveImageToPhotosAlbum({
           filePath: {{imagepath}}
       })
    },
    fail:function(res) {
    }
});
```
- switchCamera
 切换前后摄像头。
```
liveRoomComponent.switchCamera();
```
- toggleTorch
打开/关闭手电筒。
```
liveRoomComponent.toggleTorch();
```
- playBGM
播放背景音乐。
```
liveRoomComponent.playBGM({
    url: media_url,
    success: function(res){},
    fail: function(err){},
    complete: function(res){}
});
```
- stopBGM
停止背景音乐。
```
liveRoomComponent.stopBGM();
```
- pauseBGM
暂停背景音乐。
```
liveRoomComponent.pauseBGM();
```
- resumeBGM
恢复背景音乐。
```
liveRoomComponent.resumeBGM();
```
- setBGMVolume
设置背景音量。
```
liveRoomComponent.setBGMVolume({
    volume: "0.5",// 0-1之间的浮点数字符串
    success: function(ers){},
    fail: function(err){},
    complete: function(res){}
});
```
- startPreview
开启摄像头预览。
```
liveRoomComponent.startPreview();
```
- stopPreview
关闭摄像头预览。
```
liveRoomComponent.stopPreview();
```

### tic-component 组件提供如下接口
- 获取插件实例：
 - 给组件标签定义个 id 或者 class，<tic-component id="tx_board" />
 - 通过`wx.selectComponent`获取组件实例：
```
var tx_board = wx.selectComponent('#tx_board');
```
- init(callback)
初始化演示白板。
```
tx_board.init(function(){...})
```
- createClassroom(roomId, callback)
创建演示房间。
```
tx_board.createClassroom(roomId, function(){...})
```
- joinClassroom(roomId, callback)
加入已存在的演示房间，如不存在，会返回失败。
```
tx_board.joinClassroom(roomId, function(){...})
```
- quitClassroom(callback)
退出演示房间。
```
tx_board.quitClassroom(function(){...})
```
- destroyClassroom(roomId, callback)
销毁演示房间，只能是创建者调用。
```
tx_board.destroyClassroom(roomId, function(){...})
```
- setOrientation(orientation)
设置白板的方向，horizontal 为全屏（横屏），vertical 为小屏（竖屏的一部分区域）。
```
tx_board.setOrientation('horizontal')
```
- sendCustomMessage(userId, data, callback)
发送 C2C 自定义消息。
```
tx_board.sendCustomMessage('hello', {type:1, data: '112233'}, function(){...})
```
- sendTextMessage(userId, text, callback)
发送 C2C 文本消息。
```
tx_board.sendTextMessage('hello', 'welcome', function(){...})
```
- sendGroupTextMessage(text, callback)
发送群组文本消息。
```
tx_board.sendGroupTextMessage('welcome', function(){...})
```
- sendGroupCustomMessage(data, callback)
发送群组自定义消息。
```
tx_board.sendGroupCustomMessage({foo:'foo', bar:'bar'}, function(){...})
```
- addTICMessageListener(listener)
添加 IM 消息回调。
```
tx_board.addTICMessageListener(this)
```
- removeTICMessageListener(listener)
移除 IM 消息回调。
```
tx_board.removeTICMessageListener(this)
```

## 组件事件

### 播放事件
播放事件分为：
1. 普通的播放事件，tag 是 playEvent，code 含义见 [状态码](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html)。
2. 错误事件，tag 是 error。现在只有白名单校验出错时会抛出，code 是-1，具体的错误原因在 detail 中给出。

| code | 含义           | 具体错误信息                 |
| :--- | :------------- | :--------------------------- |
| -1   | 白名单校验出错 | 具体的错误原因在 detail 中给出 |

### 推流事件
推流事件分为：
1. 普通的推流事件，tag 是 pushEvent，code 含义见 [状态码](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html)。
2. 错误事件，tag 是 error。现在只有白名单校验出错时会抛出，code 是-1，具体的错误原因在 detail 中给出。
