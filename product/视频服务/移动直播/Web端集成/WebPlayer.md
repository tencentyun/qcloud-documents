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

 在PC上情况会好很多，因为PC上的浏览器目前还没有抛弃flash控件，而flash控件不追求洁癖，支持的视频源格式挺多的，而且各浏览器上的flash控件都是Adobe它家自己开发，所以兼容性非常好。（悄悄滴告诉你，Chrome最近对flash的态度不太友好）
![](//mc.qcloudimg.com/static/img/ea4a95c7a0c8d88c7b6557277510efea/image.png)

## 对接攻略

### Step 1：页面准备工作
在需要播放视频的页面（包括PC或H5）中引入初始化脚本
```
<script src="//imgcache.qq.com/open/qcloud/video/vcplayer/TcPlayer.js" charset="utf-8"></script>;
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
"m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8",
"autoplay" : true,      //iOS下safari浏览器是不开放这个能力的
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
"flv": "2157.liveplay.myqcloud.com/live/2157_358535a.flv", //增加了一个flv的播放地址，用于PC平台的播放
"autoplay" : true,      //iOS下safari浏览器是不开放这个能力的
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
目前腾讯云的 Web 播放器是不支持本地网页去调试的，主要是浏览器有跨域安全限制。所以您如果是在Windows上随便放一个test.html文件然后测试，是肯定播放不了的，需要将其上传到一个服务器上进行测试。

- **（原因三） 手机兼容问题**
FLV 和 RTMP 这两种地址，在普通的手机浏览器上都是不支持的（最新版本的QQ浏览器支持flv协议的播放，但普及度还不高），只能用HLS（m3u8)。

- **（原因四） 跨域安全问题**
PC浏览器的视频播放是基于Flash控件实现的，但做过Flash开发的同学都知道，<font color='red'>Flash控件会做跨域访问检查</font>，不过只有当您要播放的视频URL不是隶属于腾讯云时，才会碰到这个问题。解决方法就是：在视频服务器的根域名下的跨域配置文件 crossdomain.xml 中增加 qq.com 和 qzonestyle.gtimg.cn 两个域名：
```xml
<cross-domain-policy>
<allow-access-from domain="*.qq.com" secure="false"/>
<allow-access-from domain="qzonestyle.gtimg.cn" secure="false"/>
</cross-domain-policy>
```

### Step 4：多清晰度的支持
#### 4.1 原理介绍
我们知道优酷、土豆、腾讯上的视频有些是有多清晰度选择的，这个效果如何实现呢？
![](//mc.qcloudimg.com/static/img/5769d1bd31db2d9ed258d0bf62be3f0f/image.png)

这里要特别科普一下：<font color='red'>**播放器本身是没有能力去改变视频的清晰度的**</font>，在视频源产生的地方其实只有一种清晰度，我们称之为**原画**。

那么多清晰度是怎么实现的呢？ 这里就是视频云发挥作用的地方了：
- 对于直播，来自主播那一端的原始视频会在腾讯云进行实时的转码，分出两路转码后的视频，比如我们常说的**高清-HD**，以及**标清-SD**，每一路视频都有其对应的地址：
```
http://2157.liveplay.myqcloud.com/2157_358535a.m3u8          // 原画
http://2157.liveplay.myqcloud.com/2157_358535a_900.m3u8      // 高清
http://2157.liveplay.myqcloud.com/2157_358535a_550.m3u8      // 标清
```

- 对于点播，一个视频文件上传到腾讯云以后，您可以操作对该视频文件进行转码，产生另外几种清晰度的视频，比如我们常说的**高清-HD**，以及**标清-SD**。
```
http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.m3u8           // 原画
http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8      // 高清
http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8      // 标清
```

#### 4.2 代码实现
如下的代码是让播放器支持多种清晰度的支持，也就是在播放器的用户界面上展示多种清晰度线路的选择。

```javascript
var player = new TcPlayer('id_test_video', {
"m3u8"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.m3u8",//请替换成实际可用的播放地址
"m3u8_hd": "http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8",
"m3u8_sd": "http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8",
"autoplay" : true,      //iOS下safari浏览器是不开放这个能力的
"coverpic" : "http://www.test.com/myimage.jpg",
});
```

#### 4.3 实现用例
这里有一个线上的示例代码，里面使用了多种分辨率的设置以及切换功能，在PC浏览器中右键“查看页面源码”即可查看页面的代码实现：
[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-clarity.html?autoplay=true](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-clarity.html?autoplay=true)

正常情况将看到这样的效果：
![](//mc.qcloudimg.com/static/img/68c513d931214e86549dd9c0426efe04/image.png)

<font color="red">pc端现已支持多种清晰度播放并支持切换的功能，移动端将在2.2版本中支持，敬请期待。</font>

### Step 5：定制错误提示语
我们默认的提示语您可能觉得不符合您的需求，比如“网络错误，请检查网络配置或者播放链接是否正确”或者“视频解码错误”等等，我们担心这些提示语在您看来可能太干瘪了，所以腾讯云Web播放器将支持提示语定制：

#### 5.1 代码实现
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

#### 5.2 实现用例
这里有一个线上的示例代码，里面使用了自定义提示文案的功能，在PC浏览器中右键“查看页面源码”即可查看页面的代码实现：
[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?m3u8=http://2527.vod.myqcloud.com/2527_b393eb1.f230.av.m3u8](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?m3u8=http://2527.vod.myqcloud.com/2527_b393eb1.f230.av.m3u8)

#### 5.3 错误码对照表
| Code  | 提示语|说明                                       |
|-------|-----------|---------------------------------------|
| 1   	| 网络错误，请检查网络配置或者播放链接是否正确|  (H5提示的错误)          |
| 2     | 视频解码错误 | 视频格式WEB播放器无法解码(H5提示的错误)            |
| 3     | 网络错误，请检查网络配置或者播放链接是否正确|  (H5提示的错误)          |
| 4	    | 视频源错误，请检查播放链接是否有效|         (H5提示的错误)           |
| 1001	| 网络错误，请检查网络配置或者播放链接是否正确|  网络已断开( NetConnection.Connect.Closed) (Flash提示的错误)               |
| 1002	| 视频源错误，请检查播放链接是否有效|  拉取播放文件失败( NetStream.Play.StreamNotFound)，可能是服务器错误或者视频文件不存在 (Flash提示的错误)     |
| 2032	| 视频源错误，请检查播放链接是否有效|   (Flash提示的错误)                 |
| 2048	| 网络错误，请检查网络配置或者播放链接是否正确| 请求m3u8文件失败，可能是网络错误或者跨域问题 (Flash提示的错误) |


<font color="red">由于Flash的黑盒特性以及H5视频播放标准的不确定性，错误提示语会时长更新</font>
## 源码参考
这里有一个线上的示例代码，在PC浏览器中右键“查看页面源码”即可查看页面的代码实现：

[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true)

您也用它来测试播放器的效果，在链接后面加上需要播放的视频地址，刷新后就会播放这个视频地址，例如：

<table class="t" style="width:750px">
<tbody>
<tr><td>
http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true&m3u8=http://live.hkstv.hk.lxdns.com/live/hks/playlist.m3u8
</td></tr>
</tbody></table>

## 参数列表

| 参数             | 类型     | 默认值   | 参数说明                                     |   示例
|-----------------|--------- |--------  |-------------------------------------------- |----------------------------|
| m3u8             | String  | 无       |  原画m3u8 播放URL                                | http://2157.liveplay.myqcloud.com/2157_358535a.m3u8 |
| m3u8_hd             | String  | 无       |  高清m3u8 播放URL                                | http://2157.liveplay.myqcloud.com/2157_358535ahd.m3u8 |
| m3u8_sd             | String  | 无       |  标清m3u8 播放URL                          | http://2157.liveplay.myqcloud.com/2157_358535asd.m3u8 |
| flv             | String  | 无       |  原画flv 播放URL                                  | http://2157.liveplay.myqcloud.com/2157_358535a.flv |
| flv_hd             | String  | 无       |  高清flv 播放URL                                  | http://2157.liveplay.myqcloud.com/2157_358535ahd.flv |
| flv_sd             | String  | 无       |  标清flv 播放URL                                  | http://2157.liveplay.myqcloud.com/2157_358535asd.flv |
| mp4             | String  | 无       |  原画mp4 播放URL                                  | http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.mp4 |
| mp4_hd             | String  | 无       |  高清mp4 播放URL                                  | http://200002949.vod.myqcloud.com/200002949_b6ffc.f40.mp4 |
| mp4_sd             | String  | 无       |  标清mp4 播放URL                                  | http://200002949.vod.myqcloud.com/200002949_b6ffc.f20.mp4 |
| rtmp             | String  | 无       |  原画rtmp 播放URL                                | rtmp://2157.liveplay.myqcloud.com/live/2157_280d88 |
| rtmp_hd             | String  | 无       |  高清rtmp 播放URL                                | rtmp://2157.liveplay.myqcloud.com/live/2157_280d88hd |
| rtmp_sd             | String  | 无       |  标清rtmp 播放URL                                | rtmp://2157.liveplay.myqcloud.com/live/2157_280d88sd |
| width            | Number  | 无     | <font color="red">必选</font>，设置播放器宽度，单位为像素 |   640                                        |
| height           | Number  | 无     | <font color="red">必选</font>，设置播放器高度，单位为像素 |   480                                        |
| live             | Boolean  | false | <font color="red">可选</font>，设置视频是否为直播类型，将决定是否渲染时间轴等控件 |  true                   |
| autoplay         | Boolean  | false | 是否自动播放 |  true                                                                                  |
| coverpic         | String   | 无     | 预览封面    |  http://www.test.com/myimage.jpg                                                          |
| wodring         | Object   | 无     | 自定义文案    |  { 2032: '请求视频失败，请检查网络'}                                                          |


## 常见问题

- **为什么H5播放视频拉伸变形了？**

    H5并不具备拉伸视频的能力，请检查播放器的容器宽高是否设置正确。

-  **为什么我自己的div无法在盖在视频上？**

    不同浏览器对于video标签的实现方案不同，比如您的网页如果是从QQ或者微信里打开的（这里说的是Android系统下），那么极高的概率会使用QQ或微信捆绑的X5浏览器内核，也就是QQ浏览器内核，该团队考虑当时处于某些原因的考虑，采用了“视频video标签一定要处于最上层”的实现方案（相关信息参考[QQ浏览器文档说明](http://x5.tencent.com/guide?id=2009)），不过最近通过公司内部的各种协调，QQ浏览器团队正在逐步修改这个策略，您在看到这个文档时，可能最新版本的X5浏览器内核已经解决了这个问题。

-  **iOS系统下视频自动全屏播放**

    如果您的视频是在APP内实现内联播放（即您自己的App包装一个iOS的 webview 控件，用此控件显示网页，这种模式下您可以对 webview 进行一些细节定制，它的表现可以和标准 safari 浏览器有所不同），可以通过在 HTML 中的 &lt;video&gt; 标签设置 webkit-playsinline 属性(如果在 iOS10 下，则设置为 playsinline 属性)，同时 WebView 需要设置 allowsInlineMediaPlayback，这样页面在APP里打开时，视频就能以非全屏模式（即内联的方式）播放。

    如果您的页面是在Safari下打开的，目前iOS10以下版本的Safari是无法禁止视频自动全屏播放的，iOS10可以通过前面说的方法（为 &lt;video&gt; 标签设置 playsinline 属性）实现非全屏模式（即内联的方式）播放。我们的播放器已经自动加上这个属性，只需要终端支持即可。
	
-  **为什么在移动端浏览器视频无法自动播放**

	  在移动端 WEB 自动播放视频只有两个办法，通过设置 &lt;video&gt; 标签 autoplay 属性 或者调用 &lt;video&gt; 标签提供的 play() 方法，然而现实是在移动端WEB中视频自动播放一直是被禁止的，目前通用的办法是通过用户手动触发播放（例如监听用户的点击事件并调用 play()方法）。除此之外不排除一些特殊定制的 webview 支持 &lt;video&gt; 标签 autoplay 属性或者通过其他特殊的函数调用实现自动播放，那么在这类 Webview 下打开页面就有可能自动播放。我们的播放器已经在 autoplay 设置为 true 的情况下，为 &lt;video&gt; 标签加上 autoplay 属性，只要终端支持即可。


-  **为什么在 PC Chrome 中Flash播放器会有两个播放按钮？**

	  从Chrome 42版本开始将不再自动播放Flash（谷歌购买了WebRTC并进行开源并不是没有想法的）, 只对主要的Flash内容进行自动播放，其它的Flash内容将被暂停播放，除非用户决定去手动点开它。

- **为什么在 PC 浏览器中可以播放直播视频，移动端却不行**

    在移动端浏览器中播放直播视频，目前只支持hls(m3u8)协议，因此需要确认直播拉流地址是否有hls(m3u8)拉流url，如果您只给我们的播放器一个flv或者rtmp的地址，是没有什么办法在手机上观看的。


