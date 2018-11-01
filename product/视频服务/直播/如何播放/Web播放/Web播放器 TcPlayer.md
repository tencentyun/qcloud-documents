## 功能介绍

腾讯云Web播放器主要解决在手机浏览器和PC浏览器上播放音视频流的问题，使您的视频内容可以不依赖用户安装App就可以在朋友圈、微博等社交平台进行传播。

本文档适合有一定Javascript语言基础的开发人员阅读。

## 基础知识
对接之前先要了解如下的基础知识，非常有必要：

- **直播和点播**
直播是指视频源是实时的，一旦主播停播了，这个地址就已经失去意义了，而且由于是实时直播，所以播放器在播直播视频的时候是没有进度条滴。
点播是指视频源是一个服务器上的文件，文件只要没有被提供方删除，就随时可以播放， 而且由于整个视频都在服务器上，所以播放器在播点播视频的时候是有进度条的哦。

- **协议的支持**
Web播放器的视频播放能力本身不是网页代码实现的，而是靠浏览器的支持，所以其兼容性并不像我们想象的那么好，您必须要接受一个事实：<font color=red>**不是所有的手机浏览器都能有符合预期的表现**</font>，有些手机浏览器甚至根本就不支持视频播放。

 最常见的用于网页直播的视频源地址是以m3u8结尾的地址，我们称其为HLS (HTTP Live Streaming)，这是苹果推出的标准。由于苹果的影响力，目前各手机浏览器产品对这种格式的兼容性最好，但它有个天然的问题，就是延迟比较大，一般是20-30秒左右的延迟，没有办法，在手机浏览器上我们并没有其它选择。

 在PC上情况会好很多，因为PC上的浏览器目前还没有抛弃flash控件，而flash控件不追求洁癖，支持的视频源格式挺多的，而且各浏览器上的flash控件都是Adobe它家自己开发，所以兼容性非常好。（悄悄滴告诉您，Chrome最近对flash的态度不太友好）
![](//mc.qcloudimg.com/static/img/ea4a95c7a0c8d88c7b6557277510efea/image.png)

## 对接攻略

### Step 1：页面准备工作
在需要播放视频的页面（包括PC或H5）中引入初始化脚本
```
<script src="//imgcache.qq.com/open/qcloud/video/vcplayer/TcPlayer-2.2.1.js" charset="utf-8"></script>;
```

>注意：**<font color="red">直接用本地网页是调试不了的</font>，因为腾讯云Web播放器处理不了这种情况下的跨域问题。**

### Step 2：HTML里放置容器

 在需要展示播放器的页面位置加入播放器“容器”，也就是放一个div，然后给它取个名字，比如: id_test_video 。之后视频的画面都会在这个容器里渲染，容器的大小控制您可以使用div的属性进行控制，示例代码如下：

```
<div id="id_test_video" style="width:100%; height:auto;"></div>
```

### Step 3：对接视频的播放
接下来就要写 javascript 代码了，这些代码的作用是去指定的 URL 地址拉取音视频流，并将视频画面呈现到Step2中添加的容器里。

#### 3.1 一次简单的播放
如下是一条典型的直播URL地址，它是HLS（m3u8）协议的，如果主播还在直播中的话，那么用 VLC 等播放器是可以直接打开该 URL 进行观看的：
```
http://2157.liveplay.myqcloud.com/2157_358535a.m3u8      // m3u8播放地址
```
![](//mc.qcloudimg.com/static/img/7923a14be5525bd37719c18d54243403/image.png)

我们现在要在手机浏览器上播放这个 URL 的视频，javascript代码可以这样写：
```javascript
var player = new TcPlayer('id_test_video', {
"m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8", //请替换成实际可用的播放地址
"autoplay" : true,      //iOS下safari浏览器，以及大部分移动端浏览器是不开放视频自动播放这个能力的
"coverpic" : "http://www.test.com/myimage.jpg",
"width" :  '480',//视频的显示宽度，请尽量使用视频分辨率宽度
"height" : '320'//视频的显示高度，请尽量使用视频分辨率高度
});
```

这段代码就可以支持在PC以及手机浏览器上播放HLS（m3u8）协议的直播视频了，不过，前面我们有说过，HLS（m3u8）协议的视频虽然兼容性还不错（部分Android手机依然不支持），但其延迟非常高，大约20秒以上的延迟。

#### 3.2 PC上实现更低的延迟
那么对于PC浏览器而言，我们是否可以做的更好呢？当然可以，因为PC浏览器支持flash，它可强大多了，现在我们的代码要这样写：
```javascript
var player =  new TcPlayer('id_test_video', {
"m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8",
"flv": "http://2157.liveplay.myqcloud.com/live/2157_358535a.flv", //增加了一个flv的播放地址，用于PC平台的播放 请替换成实际可用的播放地址
"autoplay" : true,      //iOS下safari浏览器，以及大部分移动端浏览器是不开放视频自动播放这个能力的
"coverpic" : "http://www.test.com/myimage.jpg",
"width" :  '480',//视频的显示宽度，请尽量使用视频分辨率宽度
"height" : '320'//视频的显示高度，请尽量使用视频分辨率高度
});
```
跟前一段代码的区别就在于，我们增加了一个flv的播放地址，腾讯云Web播放器如果发现目前的浏览器是PC浏览器，会主动选择flv链路，因为可以实现更低的延迟。

当然，前提条件是FLV和HLS（m3u8）这两个地址都是可以出流的，如果您使用腾讯云的视频直播服务，这个问题是不需要犯愁的，因为腾讯云的每一条直播频道都默认支持FLV、RTMP和HLS（m3u8）三种播放协议。

#### 3.3 播放不了怎么办？
如果您发现视频不能播放，基本上逃不出如下几个原因：

-  **（原因一） 视频源有问题**
如果是直播URL，那一定要检查一下是不是主播已经停止推流了，状态不处于“直播中”的情况，可以用浮窗提示一下观众：“主播已经离开”。
如果是点播URL，那要检查您要播放的文件是否还在服务器上，比如要播放的地址是否已经被其它人从点播系统移除了。

- **（原因二） 本地网页调试**
目前腾讯云的 Web 播放器是不支持本地网页去调试的（即通过file://协议来打开视频播放的网页），主要是浏览器有跨域安全限制。所以您如果是在Windows上随便放一个test.html文件然后测试，是肯定播放不了的，需要将其上传到一个服务器上进行测试。当然前端工程师可以通过反向代理的方式对线上的页面进行本地代理以实现本地调试，这是主流可行的本地调试办法。

- **（原因三） 手机兼容问题**
FLV 和 RTMP 这两种地址，在普通的手机浏览器上都是不支持的（最新版本的QQ浏览器支持flv协议的播放，但普及度还不高），只能用HLS（m3u8)。

- **（原因四） 跨域安全问题**
PC浏览器的视频播放是基于Flash控件实现的，但做过Flash开发的同学都知道，<font color='red'>Flash控件会做跨域访问检查</font>，当您要播放的视频所存放的服务器没有部署跨域策略时，才会碰到这个问题。解决方法就是：在视频服务器的根域名下的跨域配置文件 crossdomain.xml 中增加 qq.com 域名：
```xml
<cross-domain-policy>
<allow-access-from domain="*.qq.com" secure="false"/>
</cross-domain-policy>
```

### Step 4：给播放器设置封面
在前面的代码例子中，您应该注意到 “coverpic” 这个参数了，在这里将详细介绍这个属性的使用方法。
<font color="red">备注：封面功能有可能在部分移动端播放环境下失效，由于移动端视频播放环境相对 PC 来说比较复杂，各个浏览器和 APP 的 Webview 对 H5 video 实现的方式并不统一。如果遇到功能失效的情况，欢迎向我们的技术支持反馈（反馈内容包括系统、浏览器或APP的版本等关键信息），我们将尽可能去支持。</font>

#### 4.1 简单设置封面
coverpic可以传入一个图片地址作为播放器的封面，将在播放器区域内居中并且以图片的实际分辨率进行显示

```
"coverpic" : "http://www.test.com/myimage.jpg"
```
#### 4.2 设置封面的展现样式
coverpic 同时支持传入一个对象，对象中可以进行设置封面的展现样式 style 和图片地址 src。<br>

style支持的样式有3种：
- "default" 居中并且以图片的实际分辨率进行显示。
- "stretch" 拉伸铺满播放器区域，图片可能会变形。
- "cover" 优先横向等比拉伸铺满播放器区域，图片某些部分可能无法显示在区域内。

```
"coverpic" : {"style":"stretch", "src":"http://www.test.com/myimage.jpg"}
```
#### 4.3 实现用例

这里有一个线上的示例代码，里面使用了cover方式显示封面，在PC浏览器中右键“查看页面源码”即可查看页面的代码实现：
[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-cover.html](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-cover.html)

<font color="red">备注：在某些移动端设置封面会无效，具体说明请查看常见问题</font>

### Step 5：多清晰度的支持
#### 5.1 原理介绍
我们知道优酷、土豆、腾讯上的视频有些是有多清晰度选择的，这个效果如何实现呢？
![](//mc.qcloudimg.com/static/img/5769d1bd31db2d9ed258d0bf62be3f0f/image.png)

这里要特别科普一下：<font color='red'>**播放器本身是没有能力去改变视频的清晰度的**</font>，在视频源产生的地方其实只有一种清晰度，我们称之为**原画**，而原画视频编码格式和封装格式有很多种，在 Web 端无法完全支持播放所有的视频格式，点播支持必须是以 H.264 为视频编码，以 mp4、flv 为封装格式的视频。

那么多清晰度是怎么实现的呢？ 这里就是视频云发挥作用的地方了：
- 对于直播，来自主播那一端的原始视频会在腾讯云进行实时的转码，分出多路转码后的视频，比如我们常说的**高清-HD**，以及**标清-SD**，每一路视频都有其对应的地址：
```
http://2157.liveplay.myqcloud.com/2157_358535a.m3u8          // 原画
http://2157.liveplay.myqcloud.com/2157_358535a_900.m3u8      // 高清
http://2157.liveplay.myqcloud.com/2157_358535a_550.m3u8      // 标清
```

- 对于点播，一个视频文件上传到腾讯云以后，您可以操作对该视频文件进行转码，产生另外几种清晰度的视频，比如我们常说的**高清-HD**，以及**标清-SD**，需要注意的是，上传后的原始视频是未经过腾讯云转码的，不能直接用于播放。
```
http://200002949.vod.myqcloud.com/200002949_b6ffc.f240.m3u8         // 原画，用转码后的超清替换
http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8      // 高清
http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8      // 标清
```
<font color="red">备注：上传后的原始视频是未经过腾讯云转码的，不能直接用于播放</font><br>

#### 5.2 代码实现
如下的代码是让播放器支持多种清晰度的支持，也就是在播放器的用户界面上展示多种清晰度线路的选择。

```javascript
var player = new TcPlayer('id_test_video', {
"m3u8"      : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f240.m3u8",//请替换成实际可用的播放地址
"m3u8_hd"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8",
"m3u8_sd"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8",
"autoplay"  : true,      //iOS下safari浏览器，以及大部分移动端浏览器是不开放视频自动播放这个能力的
"coverpic"  : "http://www.test.com/myimage.jpg",
});
```

#### 5.3 实现用例
这里有一个线上的示例代码，里面使用了多种分辨率的设置以及切换功能，在PC浏览器中右键“查看页面源码”即可查看页面的代码实现：
[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-clarity.html?autoplay=true](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-clarity.html?autoplay=true)

正常情况将看到这样的效果：
![](//mc.qcloudimg.com/static/img/68c513d931214e86549dd9c0426efe04/image.png)

<font color="red">pc端现已支持多种清晰度播放并支持切换的功能，移动端尚未支持。</font>

### Step 6：定制错误提示语
我们默认的提示语您可能觉得不符合您的需求，比如“网络错误，请检查网络配置或者播放链接是否正确”或者“视频解码错误”等等，我们担心这些提示语在您看来可能太干瘪了，所以腾讯云Web播放器将支持提示语定制：

#### 6.1 代码实现
如下是让播放器支持自定义提示语的核心代码，设置的提示语主要落在wording属性上。
```javascript
var player = new TcPlayer('id_test_video', {
"m3u8"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.m3u8",//请替换成实际可用的播放地址
"autoplay" : true,      //iOS下safari浏览器是不开放这个能力的
"coverpic" : "http://www.test.com/myimage.jpg",
"wording": {
    2032: "请求视频失败，请检查网络",
    2048: "请求m3u8文件失败，可能是网络错误或者跨域问题"
}
});
```

#### 6.2 实现用例
这里有一个线上的示例代码，该示例将播放失败，同时使用了自定义提示文案的功能，在PC浏览器中右键“查看页面源码”即可查看页面的代码实现：
[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?m3u8=http://2527.vod.myqcloud.com/2527_b393eb1.f230.av.m3u8](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?m3u8=http://2527.vod.myqcloud.com/2527_b393eb1.f230.av.m3u8)

#### 6.3 错误码对照表
| Code  | 提示语|说明                                       |
|-------|-----------|---------------------------------------|
| 1   	| 网络错误，请检查网络配置或者播放链接是否正确 |  (H5提示的错误)          |
| 2     | 网络错误，请检查网络配置或者播放链接是否正确 | 视频格式WEB播放器无法解码(H5提示的错误)            |
| 3     | 视频解码错误 |  (H5提示的错误)          |
| 4	    | 当前系统环境不支持播放该视频格式 |         (H5提示的错误)           |
| 5	    | 当前系统环境不支持播放该视频格式 |  播放器判断当前浏览器环境不支持播放传入的视频，可能是当前浏览器不支持MSE或者Flash插件未启用 |
| 10	| 请勿在file协议下使用播放器，可能会导致视频无法播放|   |
| 11	| 使用参数有误，请检查播放器调用代码|   |
| 12	| 请填写视频播放地址|   |
| 13	| 直播已结束,请稍后再来| RTMP正常播放过程中触发事件 (NetConnection.Connect.Closed) (Flash提示的错误)  |
| 1001	| 网络错误，请检查网络配置或者播放链接是否正确|  网络已断开( NetConnection.Connect.Closed) (Flash提示的错误)               |
| 1002	| 获取视频失败，请检查播放链接是否有效|  拉取播放文件失败( NetStream.Play.StreamNotFound)，可能是服务器错误或者视频文件不存在 (Flash提示的错误)     |
| 2032	| 获取视频失败，请检查播放链接是否有效|   (Flash提示的错误)                 |
| 2048	| 无法加载视频文件，跨域访问被拒绝 | 请求m3u8文件失败，可能是网络错误或者跨域问题 (Flash提示的错误) |

<font color="red">备注：</font><br>
<font color="red">Code 1 ~ 4 对应的是 H5 的原生事件。</font><br>
<font color="red">由于Flash的黑盒特性以及H5视频播放标准的不确定性，错误提示语会不定期更新。</font>

## 源码参考
这里有一个线上的示例代码，在PC浏览器中右键“查看页面源码”即可查看页面的代码实现：

[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true)

您可以用它来测试播放器的效果，在链接后面加上需要播放的视频地址，刷新后就会播放这个视频地址：

```
http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true&m3u8=http%3A%2F%2F1251132611.vod2.myqcloud.com%2F4126dd3evodtransgzp1251132611%2F8a592f8b9031868222950257296%2Ff0.f240.m3u8
```

## 参数列表
下面列出了播放器支持的所有参数，并进行了详细的说明。

| 参数             | 类型     | 默认值   | 参数说明
|-----------------|--------- |--------  |-------------------------------------------- |
| m3u8            | String   | 无       |  原画m3u8 播放URL  <br> 示例: `http://2157.liveplay.myqcloud.com/2157_358535a.m3u8` |
| m3u8_hd         | String   | 无       |  高清m3u8 播放URL  <br> 示例: `http://2157.liveplay.myqcloud.com/2157_358535ahd.m3u8` |
| m3u8_sd         | String   | 无       |  标清m3u8 播放URL  <br> 示例: `http://2157.liveplay.myqcloud.com/2157_358535asd.m3u8` |
| flv             | String   | 无       |  原画flv 播放URL  <br> 示例: `http://2157.liveplay.myqcloud.com/2157_358535a.flv` |
| flv_hd          | String   | 无       |  高清flv 播放URL  <br> 示例: `http://2157.liveplay.myqcloud.com/2157_358535ahd.flv` |
| flv_sd          | String   | 无       |  标清flv 播放URL  <br> 示例: `http://2157.liveplay.myqcloud.com/2157_358535asd.flv` |
| mp4             | String   | 无       |  原画mp4 播放URL  <br> 示例: `http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.mp4` |
| mp4_hd          | String   | 无       |  高清mp4 播放URL  <br> 示例: `http://200002949.vod.myqcloud.com/200002949_b6ffc.f40.mp4` |
| mp4_sd          | String   | 无       |  标清mp4 播放URL  <br> 示例: `http://200002949.vod.myqcloud.com/200002949_b6ffc.f20.mp4` |
| rtmp            | String   | 无       |  原画rtmp 播放URL  <br> 示例: `rtmp://2157.liveplay.myqcloud.com/live/2157_280d88` |
| rtmp_hd         | String   | 无       |  高清rtmp 播放URL  <br> 示例: `rtmp://2157.liveplay.myqcloud.com/live/2157_280d88hd` |
| rtmp_sd         | String   | 无       |  标清rtmp 播放URL   <br> 示例: `rtmp://2157.liveplay.myqcloud.com/live/2157_280d88sd` |
| width           | Number   | 无       | <font color="red">必选</font>，设置播放器宽度，单位为像素   <br> 示例:  640   |
| height          | Number   | 无       | <font color="red">必选</font>，设置播放器高度，单位为像素   <br> 示例: 480  |
| volume          | Number   | 0.5      | 设置初始音量，范围：0~1 [v2.2.0+]    <br> 示例: 0.6   |
| live            | Boolean  | false    | <font color="red">必选</font>，设置视频是否为直播类型，将决定是否渲染时间轴等控件，以及区分点直播的处理逻辑  <br> 示例:  true  |
| autoplay        | Boolean  | false    | 是否自动播放<br><font color="red">备注：该选项只对大部分PC平台生效</font>  <br> 示例:  true |
| coverpic        | String / Object| 无 | 预览封面，可以传入一个图片地址或者一个包含图片地址 src 和显示样式 style 的对象。<br>style可选属性：<br>default 居中1:1显示 <br>stretch 拉伸铺满播放器区域，图片可能会变形 <br>cover 优先横向等比拉伸铺满播放器区域，图片某些部分可能无法显示在区域内    <br> 示例:  "http://www.test.com/myimage.jpg" <br>或者<br>{"style": "cover", "src": "http://www.test.com/myimage.jpg"} |
| controls        | String   |"default" | default 显示默认控件，none 不显示控件，system 移动端显示系统控件 <font color="red">备注：如果需要在移动端使用系统全屏，就需要设置为system。默认全屏方案是使用 Fullscreen API + 伪全屏的方式</font> [例子](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-consoles.html)  <br> 示例:  "system"  |
| systemFullscreen| Boolean  |false     | 开启后，在不支持 Fullscreen API 的浏览器环境下，尝试使用浏览器提供的 webkitEnterFullScreen 方法进行全屏，如果支持，将进入系统全屏，控件为系统控件  <br> 示例:  true  |
| flash           | Boolean  | true     | 是否优先使用 flash 播放视频，<br><font color="red">备注：该选项只对PC平台生效</font> [v2.2.0+]  <br> 示例:  true  |
| flashUrl        | String   | 无       | 可以设置 flash swf url <br><font color="red">备注：该选项只对PC平台生效</font> [v2.2.1+]  |
| h5_flv          | Boolean  | false    | 是否启用 flv.js 的播放 flv。启用时播放器将在支持 MSE 的浏览器下，采用 flv.js 播放 flv，然而并不是所有支持 MSE 的浏览器都可以使用 flv.js ,所以播放器不会默认开启这个属性。[v2.2.0+]   <br> 示例: true |
| x5_player       | Boolean  | false    | 是否启用 TBS 的播放 flv 或 hls 。启用时播放器将在 TBS 模式下(例如 Android 的微信、QQ浏览器）将 flv 或 hls 播放地址直接赋给 `<video>` 播放。[TBS 视频能力](https://x5.tencent.com/tbs/product/video.html) [v2.2.0+]   <br> 示例:  true   |
| x5_type         | String   | 无       | 通过 video 属性 “x5-video-player-type” 声明启用同层H5播放器，支持的值：h5 (该属性为TBS内核实验性属性，非 TBS 内核不支持)。[TBS H5同层播放器接入规范](https://x5.tencent.com/tbs/guide/video.html)   <br> 示例: "h5"  |
| x5_fullscreen   | String   | 无       | 通过 video 属性 “x5-video-player-fullscreen” 声明视频播放时是否进入到 TBS 的全屏模式，支持的值：true (该属性为 TBS 内核实验性属性，非 TBS 内核不支持) 。   <br> 示例: "true"   |
| x5_orientation  | Number   | 无       | 通过 video 属性 “x5-video-orientation” 声明 TBS 播放器支持的方向，可选值：0（landscape 横屏）, 1：（portraint竖屏）, 2：（landscape &verbar; portrait跟随手机自动旋转）。 (该属性为 TBS 内核实验性属性，非 TBS 内核不支持) [v2.2.0+]  <br> 示例:  0   |
| wording         | Object   | 无       | 自定义文案   <br> 示例: { 2032: '请求视频失败，请检查网络'}  |
| clarity         | String   | 'od'     | 默认播放清晰度 [v2.2.1+] <br> 示例: clarity: 'od'  |
| clarityLabel    | Object   | {od: '超清', hd: '高清', sd: '标清'} | 自定义清晰度文案 [v2.2.1+] <br> 示例: clarityLabel: {od: '蓝光', hd: '高清', sd: '标清'}  |
| listener        | Function | 无       | 事件监听回调函数，回调函数将传入一个JSON格式的对象  <br> 示例: function(msg){<br>//进行事件处理 <br>}  |

## 实例方法列表
下面列出了播放器实例支持的方法。

| 方法             | 参数                   | 返回值                       | 说明                                    |  示例
|-----------------|------------------------|----------------------------- |----------------------------------------|---------------------|
|play()           | 无                     | 无                           | 开始播放视频                             | player.play() |
|pause()          | 无                     | 无                           | 暂停播放视频                             | player.pause() |
|togglePlay()     | 无                     | 无                           | 切换视频播放状态                          | player.togglePlay() |
|mute(muted)      | {Boolean} [可选]       | true,false {Boolean}         | 切换静音状态，不传参则返回当前是否静音      | player.mute(true) |
|volume(val)      | {int} 范围：0~1 [可选]  | 范围：0~1                    | 设置音量，不传参则返回当前音量             | player.volume(0.3) |
|playing()        | 无                     | true,false {Boolean}         | 返回是否在播放中                         | player.playing() |
|duration()       | 无                     | {int}                       | 获取视频时长 <br><font color="red">备注：只适用于点播</font> | player.duration() |
|currentTime(time)| {int} [可选]           | {int}                       | 设置视频播放时间点，不传参则返回当前播放时间点 <br><font color="red">备注：只适用于点播</font> | player.currentTime() |
|fullscreen(enter)| {Boolean} [可选]       | true,false {Boolean}         | 调用全屏接口(Fullscreen API)，不支持全屏接口时使用伪全屏模式，不传参则返回值当前是否是全屏 <br><font color="red">备注：移动端系统全屏没有提供api，也无法获取系统全屏状态</font> | player.fullscreen(true) |
|buffered()       | 无                     |  0~1                        | 获取视频缓冲数据百分比 <br><font color="red">备注：只适用于点播</font> | player.buffered()  |
|destroy()        | 无                     |  无                        | 销毁播放器实例[v2.2.1+] | player.destroy()  |
|switchClarity()  | {String}[必选]         |  无                        | 切换清晰度，传值"od"、"hd"、"sd" [v2.2.1+] | player.switchClarity('od')  |

<font color="red">备注：以上方法必须是 Tcplayer 的实例化对象，且需要初始化完毕才可以调用（即load事件触发后）</font><br>

## 进阶攻略
这里介绍一些视频播放器SDK的进阶使用方法

### 使用广告SDK
TcPlayer提供了集成 IMA SDK 的版本，若需使用广告功能，需在页面中引入以下代码

```
<!-- Google IMA SDK  -->
<script type="text/javascript" src="//imasdk.googleapis.com/js/sdkloader/ima3.js"></script>
<!-- 使用集成 IMA SDK 的版本 -->
<script type="text/javascript" src="//restcplayer.qcloud.com/sdk/tcplayer-web-1.0.1.js"></script>
```

通过adTagUrl和auth参数使用广告功能，帐号及License信息可登录 https://tcplayer.qcloud.com 注册申请，或联系 tcplayer@tencent.com 咨询反馈。

```
var player = new TcPlayer('id_test_video', {
  /* Advertisement-related parameter */
  "adTagUrl": "http://ad_tag_url",	//VAST,VMAP,VAPID视频广告Tag
  "auth": {
    "user_id": "your_user_id",		//广告帐户ID 
    "app_id": "your_app_id",		//应用ID 
    "license": "your_license"		//应用license
  }
});
```
<font color="red">备注：TcPlayer 2.2.0 之后的文档描述不适用于集成 IMA SDK 的版本，tcplayer-web-1.0.1 为独立的分支</font><br>

### ES Module
TcPlayer 提供了 ES Module 版本，module name 为 TcPlayer 。 下载地址：
```
http://imgcache.qq.com/open/qcloud/video/vcplayer/TcPlayer-module-2.2.1.js
```
### 开启优先H5播放模式
TcPlayer 是采用 H5 `<video>` 和 Flash 相结合的方式来进行视频播放的，在不同的播放环境中，播放器会选择默认最合适的播放方案。

虽然目前浏览器厂商已经开始逐步放弃对 Flash 插件的支持，但是在国内仍有大量的浏览器不支持 MSE，在播放 FLV HLS（m3u8）时无法切换到H5 `<video>`的播放模式，而播放 RTMP 必须使用 Flash 模式才可以播放，
因此 TcPlayer 仍是默认优先启用 Flash 播放模式，如果在检测到 Flash 插件不可用的情况下，将采用 H5 `<video>`进行播放。

默认 Flash 模式的原因是 Flash 支持的视频格式最广，而H5 `<video>`默认只支持 MP4（h.264）（其他非腾讯云提供的视频格式这里就不列出了），在特定条件下才能支持HLS（m3u8）、FLV。

从2.2.0版本开始，提供了可以设置播放模式优先级的属性，如果想优先采用H5 `<video>`播放模式，需要把 flash 属性设置为 false ，这样在播放时默认将启用H5 `<video>`播放，如果H5 `<video>`不可用将采用 Flash 播放，如果没有检测到 Flash 插件将会提示“当前系统环境不支持播放该视频格式”


### 监听事件
TcPlayer 是采用 H5 `<video>` 和 Flash 相结合的方式来进行视频播放，由于两种方式播放视频时触发的事件不尽相同，所以我们以 H5 `<video>` 的规范为准，对 Flash 的播放事件做了一定程度的转换，以实现播放事件命名的统一。TcPlayer 对这两种播放方式所触发的原生事件进行了捕获和透传。

[H5事件参考列表](https://www.w3.org/wiki/HTML/Elements/video#Media_Events)
[Flash事件参考列表](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/events/NetStatusEvent.html)

统一后的事件列表

```
error
timeupdate
load
loadedmetadata
loadeddata
progress
fullscreen
play
playing
pause
ended
seeking
seeked
resize
volumechange
```
<font color="red">注意事项：</font>
* 如果通过系统控制栏进行全屏，将无法监听到 fullscreen 事件。

Flash模式下特有的事件
```
netStatus
```

<font color="red">备注：由于Flash的黑盒特性以及H5视频播放标准在各个平台终端的实现不一致性，事件的触发方式和结果会有差异，开发过程中可以留意这些差异</font><br>

在非自动播放的条件下，加载视频至待播放状态，移动端和PC Flash 触发的事件区别
移动端：
![移动端](//mc.qcloudimg.com/static/img/ddf4e9ff5998dc84b1887fba0e94d446/image.png)
PC Flash：
![PC Flash](//mc.qcloudimg.com/static/img/f49d8aa8ef678b63ac73e69f254c20bb/image.png)

<font color="red">备注：以上是两种平台的差异，然而在移动端的各种设备和 APP 之间同样存在差异。</font><br>

应用案例：

通过事件监听，可以进行播放失败重连，[在线例子链接](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-reconnect.html)

## 更新日志
TcPlayer在不断的更新以及完善中，为了方便大家了解版本情况，下面列出的是TcPlayer发布的主版本介绍，而一些历史bug修复，小功能版本没有列出。

| 日期             | 版本     | 更新内容
|-----------------|--------- |-------------------------------------------- |
| 2016.12.28      | 2.0.0    | 首个版本  |
| 2017.3.4        | 2.1.0    | 至2017.6.30，经历数次的迭代开发逐步趋于稳定，目前文档的功能描述中，如果没有特殊说明，皆基于此版本。  |
| 2017.6.30       | 2.2.0    | 1.增加控制播放环境判断的参数： flash、h5_flv、x5_player。<br>2.调整播放器初始化逻辑，优化错误提示效果。<br>3.增加flv.js支持，在符合条件的情况下可以采用flv.js播放 flv <br>4.支持x5-video-orientation属性，<br>5.增加播放环境判断逻辑，可通过参数调整H5与Flash的优先级，以及是否启用TBS播放。<br>6.启用版本号发布方式，避免影响旧版本的使用者。<br> 7.优化事件触发的时间戳，统一为标准时间。<br>8.bug修复|
| 2017.12.7       | 2.2.1    | 1.增加systemFullscreen参数。<br> 2.增加flashUrl参数。<br>3.修复音量max后进行静音切换的UI问题。<br> 4.修复ios11微信下需要单击两次才能播放的问题。<br> 5.修复safari 11 系统样式被遮挡的问题。<br>6.适配在x5内核会触发seeking，但不会触发seeked的情况。<br>7.修复进度条拖拽到起始位置，设置currentTime失败的问题。<br> 8.切换清晰度保持音量不变。<br> 9.修复页面宽度为0，播放器宽度判断失败问题 <br> 10.destroy方法增加完全销毁播放器节点|
| 2017.12.20      | 2.2.1    | 1.增加可配置清晰度文案功能<br> 2.设置默认清晰度<br> 3.支持切换清晰度方法|

## 常见问题

- **TcPlayer支持哪些浏览器？**

    TcPlayer 经过测试并支持的浏览器有，桌面端：IE10+、Edge、Chrome、Firefox、QQ浏览器，MAC Safari，移动端：Android4.4+，iOS8.0+，微信、手机QQ、QQ浏览器、Chrome、Safari。
    如需支持IE8、IE9浏览器需要在引入播放器脚本前，引入Polyfill脚本。如下所示：
    ```
    <!--[if lt IE 9]>
    <script src="//imgcache.qq.com/open/qcloud/video/vcplayer/libs/es5-shim.js" charset="utf-8"></script>
    <script src="//imgcache.qq.com/open/qcloud/video/vcplayer/libs/es5-sham.js" charset="utf-8"></script>
    <![endif]-->
    <script src="//imgcache.qq.com/open/qcloud/video/vcplayer/TcPlayer-2.2.1.js" charset="utf-8"></script>;
    ```

- **为什么在移动端 TcPlayer 全屏后无法使视频全屏，仍然会显示浏览器的界面？**

    首先要了解一些背景知识，TcPlayer 提供的全屏方案是 Fullscreen API + 伪全屏的方式，如果浏览器支持 Fullscreen API 那么进入全屏时，视频容器将会铺满屏幕，控制栏是 TcPlayer 提供的控制栏，如图所示
    ![](//mc.qcloudimg.com/static/img/df40b2b49390f8fc314fd040ba026156/image.png)
    （Android Chrome）

    如果浏览器不支持Fullscreen API 则会进入伪全屏模式，如图所示：
    ![](//mc.qcloudimg.com/static/img/d5746d9bef48b411c3bac576fe6925b1/image.png)![](//mc.qcloudimg.com/static/img/1e20288d6f69a5cf7a886f95edd40ec3/image.png)
    （左：Android 微信，右：iOS 微信）

    这两种全屏模式显示的控制栏都是 TcPlayer 提供的控制栏，进入方式都是通过单击控制栏的全屏按钮，或者 TcPlayer 提供的全屏方法实现的。
    然而在移动端不一定可以显示 TcPlayer 提供的控制栏，大部分情况下移动端webview会劫持视频播放，并使用 webview 提供的控制栏，这样就无法显示 TcPlayer 的控制栏，也无法使用 TcPlayer 提供的全屏方案。如图所示：
    ![](//mc.qcloudimg.com/static/img/d027ca6fce35059e05428128b9823d70/image.png)![](//mc.qcloudimg.com/static/img/b28d69f15a60321d1a6e2b3a93b53038/image.png)
    （左：Android 微信，TBS劫持视频播放，右：iOS QQ浏览器劫持视频播放）
    进入全屏后：
    ![](//mc.qcloudimg.com/static/img/0ab29e27c7aa89587cec96d7530ab4f7/image.png)![](//mc.qcloudimg.com/static/img/a260a96ed73d2a4d7d0260c4584a128a/image.png)
    （左：Android 微信，右：iOS QQ浏览器）
    可以看到控制栏与 TcPlayer 是不同的，而这种全屏方式是没有接口提供给 JS 调用的，所以 TcPlayer 无法实现这样的全屏方式。
    （我们通常会把视频区域铺满屏幕的全屏模式称为**系统全屏**，而视频区域铺满浏览器的页面可视区域称为**伪全屏**）
    综上所诉如果全屏后看到浏览器的界面则是进入了伪全屏，如果想在移动端全屏时必须进入系统全屏，只能使用系统提供的控制栏，选择控制栏类型可以通过 TcPlayer 的 controls 属性进行设置。

- **为什么H5播放视频拉伸变形了？**

    H5并不具备拉伸视频的能力，请检查播放器的容器宽高是否设置正确。

-  **为什么我自己的 div 无法在盖在视频上？**

    不同浏览器对于 `<video>` 标签的实现方案不同，比如您的网页如果是从QQ或者微信里打开的（这里说的是Android系统下），那么极高的概率会使用QQ或微信捆绑的X5浏览器内核，也就是QQ浏览器内核，该团队考虑当时处于某些原因的考虑，采用了“视频 `<video>` 标签一定要处于最上层”的实现方案（相关信息参考[QQ浏览器文档说明](http://x5.tencent.com/guide?id=2009)），不过最近通过公司内部的各种协调，QQ浏览器团队正在逐步修改这个策略，您在看到这个文档时，可能最新版本的X5浏览器内核已经解决了这个问题。

-  **为什么设置封面无效？**

    这个问题的原因和上一个问题“ div 无法在盖在视频上”是一样的，除非浏览器允许元素能够覆盖 `<video>` 标签，不然封面将会无法显示。

-  **为什么在某些移动端浏览器视频会默认全屏播放？**

	如果您的视频是在APP内实现内联播放（即您自己的App包装一个iOS的 webview 控件，用此控件显示网页，这种模式下您可以对 webview 进行一些细节定制，它的表现可以和标准 safari 浏览器有所不同），可以通过在 HTML 中的 `<video>` 标签设置 webkit-playsinline 属性(如果在 iOS10 下，则设置为 playsinline 属性)，同时 WebView 需要设置 allowsInlineMediaPlayback，这样页面在APP里打开时，视频就能以非全屏模式（即内联的方式）播放。

	如果您的页面是在Safari下打开的，目前iOS10以下版本的Safari是无法禁止视频自动全屏播放的，iOS10可以通过前面说的方法（为 `<video>` 标签设置 playsinline 属性）实现非全屏模式（即内联的方式）播放。我们的播放器已经自动加上这个属性，只需要终端支持即可。

	如果是Android终端，众所周知Android系统有各种各样的定制版本，每个版本对 `<video>` 标签的实现都有差别，并没有一个完整的统一标准，所以在Android上播放视频所展现的一致性，相比iOS要差很多。按照现有通用的办法，播放器已经自动加上 webkit-playsinline playsinline 属性，只需要终端支持即可。

-  **为什么在移动端浏览器视频无法自动播放？**

	在移动端 WEB 自动播放视频只有两个办法，通过设置 `<video>` 标签 autoplay 属性 或者调用 `<video>` 标签提供的 play() 方法，然而现实是在移动端WEB中视频自动播放一直是被禁止的，目前通用的办法是通过用户手动触发播放（例如监听用户的单击事件并调用 play()方法）。除此之外不排除一些特殊定制的 webview 支持 `<video>` 标签 autoplay 属性或者通过其他特殊的函数调用实现自动播放，那么在这类 Webview 下打开页面就有可能自动播放。我们的播放器已经在 autoplay 设置为 true 的情况下，为 `<video>` 标签加上 autoplay 属性，只要终端支持即可。

-  **为什么在 PC Chrome 中Flash播放器会有两个播放按钮？**

	从Chrome 42版本开始将不再自动播放Flash（谷歌购买了WebRTC并进行开源并不是没有想法的）, 只对主要的Flash内容进行自动播放，其它的Flash内容将被暂停播放，除非用户决定去手动点开它。

-  **为什么在 PC 浏览器中可以播放直播视频，移动端却不行？**

    在移动端浏览器中播放直播视频，目前只支持hls(m3u8)协议，因此需要确认直播拉流地址是否有hls(m3u8)拉流url，如果您只给我们的播放器一个flv或者rtmp的地址，是没有什么办法在手机上观看的。
