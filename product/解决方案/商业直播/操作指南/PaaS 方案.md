本文为您介绍商业直播小程序插件解决方案的制定。

## 注册腾讯云账号
- 注册 [腾讯云账号](https://cloud.tencent.com/document/product/378/17985)，并完成 [企业实名认证](https://cloud.tencent.com/document/product/378/10496)。
- 注册完成后提供腾讯云账号 APPID 以及 bizname。bziname 为您的唯一品牌标识，将会在域名前缀等被使用。bziname 一旦确定不可变更。

## 注册小程序
在 [微信公众平台](https://mp.weixin.qq.com) 注册并登录小程序。小程序类目请根据您的实际场景选择。

## 安装微信小程序开发工具
- 下载并安装最新版本的 [微信开发者工具](https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html)。
- 使用小程序之前，请先阅读微信小程序提供的 [插件文档](https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/)，了解插件的使用范围和限制。

## 推流及拉流

1. 配置防盗链。
   直播防盗链用于对推流端/播放端身份的权限鉴定，通过使用加密算法对推流 URL 或者播放 URL 进行加密，防止非法用户恶意盗推或者盗播。您可以提供推流密钥/播放密钥到腾讯云为您配置推流防盗链/播放防盗链。
   默认情况下，为您自动开启推流防盗链配置。
2. 生成推流/播放地址。
   打开`https://bizlive.myqcloud.com/tools/address.html?bizname=bizname`工具页面（URL 中的 bizname 参数为您的 bizname），您可以在工具页面中填写流名称以及鉴权密钥，自动生成推流地址以及播放地址。

## 使用插件
1. 申请插件使用权限。
在小程序管理后台的【设置】>【第三方设置】中选择【添加插件】，在弹出的页面中搜索【腾讯云直播助手】，选中插件并添加。
2. 在小程序中引入插件代码，可以参见 [demo 源码](https://bizlive-1258550678.cos.ap-chengdu.myqcloud.com/plugin-demo.zip)。
对于插件的使用者，使用插件前要在 app.json 中声明需要使用的插件，例如：
```js
   {
       ……
       "plugins": {
            "liveRoomPlugin": {
                "version": "1.0.3",
                "provider": "wx95a7d2b78cf30f98"
            }
        }
    }
```
1. 使用插件中的推、拉流组件。
    1) 播放组件
 - 在 page 的 .json 文件中定义需要引入的 live-room-play 组件，使用 plugin:// 协议。
```js
  {
  		"usingComponents": {
    			"live-room-play": "plugin://liveRoomPlugin/live-room-play"	//播放组件
  		}
  }
```
 - 在 page 的 .wxml 文件加载上一步引入的 live-room-play 组件。
```xml
  <view class="container-box">
    <view class="player-view">
      <live-room-play liveAppID="1258550678" playUrl="{{playUrl}}" orientation="{{orientation}}" objectFit="{{objectFit}}"
        minCache="{{minCache}}" maxCache="{{maxCache}}" mode="{{mode}}" muted="{{muted}}" debug="{{debug}}" bindPlayEvent="onPlayEvent" >
      </live-room-play>
    </view>
  </view>
```

 2) 推流组件
 - 在 page 的 .json 文件中定义需要引入的 live-room-push 组件，使用 plugin:// 协议。
```js
  {
  		"usingComponents": {
    			"live-room-push": "plugin://liveRoomPlugin/live-room-push"	//播放组件
  		}
  }
```
 - 在 page 的 .wxml 文件加载上一步引入的 live-room-push 组件。
```xml
  <view class="container-box">
<view class="publisher-view">
  <live-room-push liveAppID="{{liveAppID}}" pushUrl="{{pushUrl}}" orientation="{{orientation}}" muted="{{muted}}" mode="{{mode}}" waitingImage="{{waitingImage}}" enableCamera="{{enableCamera}}" beauty="{{beauty}}" whiteness="{{whiteness}}" backgroundMute="{{backgroundMute}}"
      debug="{{debug}}" autoFocus="{{autoFocus}}" aspect="{{aspect}}" minBitrate="{{minBitrate}}" maxBitrate="{{maxBitrate}}" zoom="{{zoom}}" devicePosition="{{devicePosition}}" sdkAppID="{{sdkAppID}}" accountType="{{accountType}}" userID="{{userID}}" userSig="{{userSig}}"
      roomID="{{roomID}}" nickName="{{nickName}}" avatar="{{avatar}}" bindPushEvent="onPushEvent" bindIMEvent="onIMEvent">
</view>
</view>
```

 3）直播播放相关的属性
<table width="850px">
  <tr align="center">
    <th width="80px">属性</th>
    <th width="80px">类型</th>
    <th width="80px">默认值</th>
    <th width="280px">说明</th>
  </tr>
  <tr >
    <td>playUrl</td>
    <td>String</td>
    <td>""</td>
    <td>通过使用 https://bizlive.myqcloud.com/tools/address.html?bizname=bizname 工具页面获取 </td>
  </tr>
  <tr >
    <td>mode</td>
    <td>String</td>
    <td>"live"</td>
    <td>live（直播），RTC（实时通话，该模式时延更低）</td>
  </tr>
  <tr >
    <td>orientation</td>
    <td>String</td>
    <td>"vertical"</td>
    <td>画面方向，可选值有 vertical、horizontal</td>
  </tr>
  <tr >
    <td>objectFit</td>
    <td>String</td>
    <td>"contain"</td>
    <td>填充模式，可选值有 contain、fillCrop</td>
  </tr>  <tr >
    <td>minCache</td>
    <td>Number</td>
    <td>1</td>
    <td>最小缓冲区，单位s</td>
  </tr>  <tr >
   <td>muted</td>
   <td>Boolean</td>
    <td>false</td>
   <td>是否静音</td>
  </tr>  <tr >
    <td>debug</td>
   <td>Boolean</td>
   <td>false</td>
   <td>是否显示日志</td>
  </tr>  <tr >
   <td>bindPlayEvent</td>
    <td>EventHandle</td>
	<td>-</td>
    <td>播放状态变化事件回调</td>
  </tr>
</table>
4）直播推流组件相关属性说明
<table>
<thead>
<tr>
<th>属性</th>
<th>类型</th>
<th>默认值</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>liveAppID</td>
<td>Number</td>
<td>0</td>
<td>直播 appid</td>
</tr>
<tr>
<td>pushUrl</td>
<td>String</td>
<td>""</td>
<td>直播推流地址</td>
</tr>
<tr>
<td>orientation</td>
<td>String</td>
<td>"vertical"</td>
<td>推流画面方向，可选值有 vertical、horizontal</td>
</tr>
<tr>
<td>muted</td>
<td>Boolean</td>
<td>false</td>
<td>是否静音</td>
</tr>
<tr>
<td>mode</td>
<td>String</td>
<td>"SD"</td>
<td>清晰度，可选值：SD（标清）、HD（高清）、FHD（超清）、RTC（实时通话）</td>
</tr>
<tr>
<td>waitingImage</td>
<td>String</td>
<td>""</td>
<td>进入后台推流时候的垫片图片</td>
</tr>
<tr>
<td>enableCamera</td>
<td>Boolean</td>
<td>true</td>
<td>是否开启摄像头</td>
</tr>
<tr>
<td>beaut</td>
<td>y Number</td>
<td>0</td>
<td>美颜指数，取值 0 - 9，数值越大效果越明显</td>
</tr>
<tr>
<td>whiteness</td>
<td>Number</td>
<td>0</td>
<td>美白指数，取值 0 - 9，数值越大效果越明显</td>
</tr>
<tr>
<td>backgroundMute</td>
<td>Boolean</td>
<td>false</td>
<td>进入后台时是否静音，初始化设置生效</td>
</tr>
<tr>
<td>debug</td>
<td>Boolean</td>
<td>false</td>
<td>是否显示日志</td>
</tr>
<tr>
<td>autoFocus</td>
<td>Boolean</td>
<td>true</td>
<td>自动聚焦，初始化设置生效</td>
</tr>
<tr>
<td>aspect</td>
<td>String</td>
<td>"9:16"</td>
<td>宽高比，可选值有 3:4、9:16</td>
</tr>
<tr>
<td>minBitrate</td>
<td>Number</td>
<td>200</td>
<td>最小码率</td>
</tr>
<tr>
<td>maxBitrate</td>
<td>Number</td>
<td>1000</td>
<td>最大码率</td>
</tr>
<tr>
<td>zoom</td>
<td>Boolean</td>
<td>false</td>
<td>自动调整焦距，初始化设置生效</td>
</tr>
<tr>
<td>devicePosition</td>
<td>String</td>
<td>"front"</td>
<td>摄像头前置或后置，值为front、back。注意这个值只是在组件初始化时生效，不能动态修改。动态切换摄像头用接口 switchCamera</td>
</tr>
<tr>
<td>bindPushEvent</td>
<td>EventHandle</td>
<td>-</td>
<td>推流状态变化事件回调</td>
</tr>
</tbody>
</table>
4. 在播放区域叠加额外展示信息。
组件提供了一个`<slot>`节点，用于承载组件引用时提供的子节点。本功能受限于微信，只能在组件上叠加 cover-image 、 cover-view 和 canvas。

## 获取 live-room-play 组件实例
>?live-room 组件支持播放、停止播放、全屏等接口，要调用这些接口需要先获取到 live-room-play 的实例。

live-room-play 是腾讯视频云直播插件中的一个组件，在腾讯视频云直播插件中展示了获取 live-room-play 组件实例的接口，您只需要先在 page 的 .js 文件中，将插件加载进来，即可获取到 live-room-play 组件实例。

```js
// 加载插件
var plugin = requirePlugin("liveRoomPlugin")
// 获取 live-room 组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
```

>?live-room-push 组件获取同上。 

## 组件接口
### live-room-play 接口
live-room-play 组件提供如下接口：

- start
  开始播放。
  调用之后会启动播放。在开始播放之前，`playUrl` 要保证已经设置到组件属性中。
```js
// 获取live-room-play组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.start();
```
- stop
  结束播放。
```js
// 获取live-room-play组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.stop();
```
- requestFullScreen
  全屏播放。
```js
// 获取live-room-play组件实例
var liveRoomComponent = plugin.instance.getLiveRoomInstance();
liveRoomComponent.requestFullScreen(true);		//全屏播放
//liveRoomComponent.requestFullScreen(false);	//退出全屏
```

### live-room-push 接口

- start
  开始推流。
  调用之后会启动推流。在开始播放之前，`playUrl` 要保证已经设置到组件属性中。
```js
// 获取live-room-push组件实例
var liveRoomPushComponent = plugin.instance.getLiveRoomPushInstance();
liveRoomPushComponent.start();
```
- stop
  结束推流。
```js
// 获取live-room-push组件实例
var liveRoomPushComponent = plugin.instance.getLiveRoomPushInstance();
liveRoomPushComponent.stop();
```
- snapshot
  截图。
```js
liveRoomPushComponent.snapshot({
 success: function (res){
   wx.saveImageToPhotosAlbum({
     filePath: {{imagepath}}
   })
 },
 fail:function(res) {
 }
});
},
```
- switchCamera
  切换前后摄像头。
```js
liveRoomComponent.switchCamera();
```

## 组件事件
### 播放事件
播放事件分为：
- 普通的播放事件，tag 是`playEvent`，`code`含义参见 [状态码](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html)。
- 错误事件，tag 是`error`。目前只有白名单校验出错时会抛出，`code`是-1，具体错误原因会在`detail`里给出。
<table width="850px">
<tr>
    <th width="80px">code</th>
    <th width="80px">含义</th>
    <th width="80px">具体错误信息</th>
  </tr>
  <tr >
    <td>-1</td>
    <td>白名单校验出错</td>
    <td>具体错误原因在 detail 里给出</td>
  </tr>
 </table>

### 推流事件
推流事件分为：
- 普通的推流事件，tag 是`pushEvent`，`code`含义参见 [状态码](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
- 错误事件，tag 是`error`。目前只有白名单校验出错时会抛出，`code`是-1，具体错误原因会在`detail`里给出。
