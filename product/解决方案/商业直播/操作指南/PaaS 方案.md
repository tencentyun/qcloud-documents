在正式接入前，请先阅读微信小程序提供的 [插件文档](https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/)，了解插件的使用范围和限制。

## 版本支持
- 最新插件版本：1.3.0。新增小窗功能，包体缩减。需在云直播控制台添加插件，使用小程序直播域名才能调用，无需通过 version 标识方案（即与旧版本不兼容，需要在云直播控制台接入插件）。
- 最低插件版本限制：1.2.4。仍支持旧方案，但是新功能暂时不支持，需要通过 version 2 来标识新方案。

## 准备工作
1. 在 [微信公众平台](https://mp.weixin.qq.com) 注册并登录小程序。
2. 符合接入要求，申请插件并购买小程序·云直播服务，详见 [小程序·云直播插件](https://cloud.tencent.com/document/product/1078/42916)。
3. 开通小程序·云直播服务后，登录 [云直播控制台](https://console.cloud.tencent.com/live)，在 **域名管理** 中添加小程序直播域名，然后 [自助拼接直播地址](https://cloud.tencent.com/document/product/267/32720)。
4. 下载并安装最新版本的 [微信开发者工具](https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html)，使用小程序绑定的微信号扫码登录开发者工具。
   ![](https://main.qcloudimg.com/raw/366e52aa9cc84949271b87a4678da636.png)
 
## 引入插件代码
在小程序中引入插件代码，可参考 [Demo 源码](https://bizlive-1258550678.cos.ap-chengdu.myqcloud.com/plugin-demo.zip)。使用插件前需在小程序工程的`app.json`中声明要使用的插件，例如：
```
{
  ……
  "plugins": {
      "liveRoomPlugin": {
          "version": "1.3.0",
          "provider": "wx95a7d2b78cf30f98"
      }
  }
}
```

## 使用播放组件

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
  <live-room-play liveAppID="{{liveAppID}}" playUrl="{{playUrl}}" orientation="{{orientation}}" objectFit="{{objectFit}}"
    minCache="{{minCache}}" maxCache="{{maxCache}}" mode="{{mode}}" muted="{{muted}}" debug="{{debug}}" bindPlayEvent="onPlayEvent" >
  </live-room-play>
</view>
</view>
```

## 播放组件相关属性说明

直播插件的使用方法和微信原生标签的方法一致，可参考微信小程序标签 [live-player](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html) 的文档说明。

| 属性                      | 类型         | 默认值     | 必填 | 说明                                                         |
| :------------------------ | :----------- | :--------- | :--- | :----------------------------------------------------------- |
| liveAppID                 | Number       | 0          | 是   | 用户的腾讯云 AppID                                           |
| playUrl                   | String       | ""         | 是   | 需用小程序直播播放域名生成的播放地址，详见 [自主拼装直播 URL](https://cloud.tencent.com/document/product/267/32720) |
| version                   | Number       | 1          | 否   | 1.2.4版本插件参数，此处必填值为：2。旧方案接入：填1或不填。高版本无需填写。 |
| mode                      | String       | "live"     | 否   | live（直播），RTC（实时通话，该模式延时更低）                |
| orientation               | String       | "vertical" | 否   | 画面方向，可选值有 vertical、horizontal                      |
| objectFit                 | String       | "contain"  | 否   | 填充模式，可选值有 contain、fillCrop                         |
| minCache                  | Number       | 1          | 否   | 最小缓冲区，单位 s                                           |
| maxCache                  | Number       | 3          | 否   | 最大缓冲区，单位 s                                           |
| muted                     | Boolean      | false      | 否   | 是否静音                                                     |
| debug                     | Boolean      | false      | 否   | 是否显示日志                                                 |
| soundMode                 | String       | 'speaker'  | 否   | 声音输出设备，'speaker'或者'ear'，代表扬声器或听筒           |
| autoplay                  | Boolean      | false      | 否   | 是否自动播放                                                 |
| autopause                 | Boolean      | true       | 否   | 页面跳转时是否自动暂停                                       |
| pictureInPictureMode      | string/Array | "not set"  | 否   | 用户跳转页面后，是否会弹出小窗口，有多种模式（push, pop，空字符串或通过数组形式设置多种模式（如： ["push", "pop"]）） |
| bindPlayEvent             | EventHandle  | null       | 否   | 播放状态变化事件回调                                         |
| bindfullscreenChangeEvent | EventHandle  | null       | 否   | 全屏状态变化事件回调                                         |
| bindNetStatus             | EventHandle  | null       | 否   | 网络状态变化回调                                             |
| bindAttachedEvent         | EventHandle  | null       | 否   | 插件加载完成回调                                             |
| bindenterpictureinpicture | EventHandle  | null       | 否   | 用户进入小窗口回调                                           |
| bindleavepictureinpicture | EventHandle  | null       | 否   | 用户离开小窗口回调                                           |

**在播放区域叠加额外展示信息**
组件提供了一个`<slot>`节点，用于承载组件引用时提供的子节点。本功能受限于微信，只能在组件上叠加`cover-image`、`cover-view`和`canvas`。

## 组件实例化
live-room 组件支持播放、停止播放、全屏等接口，要调用这些接口需要先获取到 live-room-play 的实例。

**怎么获取 live-room-play 组件实例？**
live-room-play 是腾讯视频云直播插件中的一个组件，在腾讯视频云直播插件中暴露了获取 live-room-play 组件实例的接口，您只需要先在 page 的`.js`文件中，将插件加载进来，即可获取到 live-room-play 组件实例。
```js
// 加载插件
var plugin = requirePlugin("liveRoomPlugin")
// 获取 live-room 组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
```

## 组件接口
**live-room-play 组件提供如下接口：**
- 可参考微信小程序组件 [LivePlayerContext 方法](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.html)。
- start
  开始播放。调用之后会启动播放。在开始播放之前，`playUrl`也要保证已经设置到组件属性中。
```
// 获取 live-room-play 组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.start();
```
- stop
  结束播放。
```
// 获取 live-room-play 组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.stop();
```
- requestFullScreen
  全屏播放。
```
// 获取 live-room-play 组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.requestFullScreen(true);        //全屏播放
//liveRoomComponent.requestFullScreen(false);    //退出全屏
```
- pause
  暂停播放。
```
// 获取 live-room-play 组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.pause();        //暂停播放
```
- resume
  恢复播放。
```
// 获取 live-room-play 组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.resume();        //恢复播放
```
- mute
  静音。
```
// 获取 live-room-play 组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.mute();        //静音
```
- 如果小程序需要后台播放纯音频流，可以使用纯音频的转码流进行播放，示例代码如下：
```
this.audio = wx.getBackgroundAudioManager();
this.audio.protocol = 'hls';// 这个属性设置为 hls 才支持 m3u8 类型的直播流
this.audio.title = '后台音乐';// 显示在状态栏的标题
this.audio.src = "http://domain/live/streamName_pureAudio.m3u8?txSecret=xxxx&txTime=xxxxx"; 
// 注：domain 是小程序域名，streamName 是指定的流名称，
// 后面加 _pureAudio 就是纯音频转码流，后台播放时可以节省流量。
```

## 播放事件
播放事件分为：
1. 普通的播放事件，tag 是 playEvent，code 含义见 [状态码](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html)。
2. 错误事件，tag 是 error。现在只有白名单校验出错时会抛出，code 是-1，具体的错误原因在 detail 中给出。

| code | 含义           | 具体错误信息                   |
| :--- | :------------- | :----------------------------- |
| -1   | 白名单校验出错 | 具体的错误原因在 detail 中给出 |
