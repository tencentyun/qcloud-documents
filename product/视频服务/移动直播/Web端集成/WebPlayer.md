## 功能介绍

腾讯云Web播放器主要解决在手机浏览器和PC浏览器上播放音视频流的问题，使您的视频内容可以不依赖用户安装App就可以在朋友圈、微博等社交平台进行传播。

本文档适合有一定Javascript语言基础的开发人员阅读，同时，如果要实现微信分享功能，推荐您关注 [移动直播-如何在朋友圈中看直播？](https://www.qcloud.com/document/product/454/8046)。


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
<script src="//qzonestyle.gtimg.cn/open/qcloud/video/live/h5/live_connect.js" charset="utf-8"></script>;
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
var player = new TencentCloud.Player("id_test_video", {
"m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8",
"autoplay" : true,      //iOS下safari浏览器是不开放这个能力的
"coverpic" : "http://www.test.com/myimage.jpg",
});
```

这段代码就可以支持在PC以及手机浏览器上播放HLS（m3u8）协议的直播视频了，不过，前面我们有说过，HLS（m3u8）协议的视频虽然兼容性还不错（部分Android手机依然不支持），但其延迟非常高，大约20秒以上的延迟。

#### 3.2 PC上实现更低的延迟
那么对于PC浏览器而言，我们是否可以做的更好呢？当然可以，因为PC浏览器支持flash，它可强大多了，现在我们的代码要这样写：
```javascript
var player = new TencentCloud.Player("id_test_video", {
"m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8",
"flv": "2157.liveplay.myqcloud.com/live/2157_358535a.flv", //增加了一个flv的播放地址
"autoplay" : true,      //iOS下safari浏览器是不开放这个能力的
"coverpic" : "http://www.test.com/myimage.jpg",
});
```
跟前一段代码的区别就在于，我们增加了一个flv的播放地址，腾讯云Web播放器如果发现目前的浏览器是PC浏览器，会主动选择flv链路，因为可以实现更低的延迟。

当然，前提条件是FLV和HLS（m3u8）这两个地址都是可以出流的，如果您使用腾讯云的视频直播服务，这个问题是不需要犯愁的，因为腾讯云的每一条直播频道都默认支持FLV、RTMP和HLS（m3u8）三种播放协议。

#### 3.3 播放不了怎么办？
（to-do：补充一张正常效果图）
如果这段代码运行正常，您将看到上面的效果，但如果您发现不能播放，基本上逃不出如下几个原因：

-  **（原因一） 直播结束了？**
也就是主播不在直播中状态，这种情况就没办法了，我们能做的就是提示一下“主播已经离开”。

- **（原因二） 本地网页调试**
目前腾讯云的 Web 播放器是不支持本地网页去调试的，主要是浏览器有跨域安全限制。

- **（原因三） 手机兼容问题**
FLV 和 RTMP 这两种地址，在普通的手机浏览器上都是不支持的（最新版本的QQ浏览器支持flv协议的播放），只能用HLS（m3u8)。

- **（原因四） 跨域安全问题**
PC浏览器的视频播放是基于Flash控件实现的，但做过Flash开发的同学都知道，<font color='red'>Flash控件会做跨域访问检查</font>，不过只有当您要播放的视频URL不是隶属于腾讯云时，才会碰到这个问题。解决方法就是：在视频服务器的根域名下的跨域配置文件 crossdomain.xml 中增加 qq.com 和 qzonestyle.gtimg.cn 两个域名：
```xml
<cross-domain-policy>
<allow-access-from domain="*.qq.com" secure="false"/>
<allow-access-from domain="qzonestyle.gtimg.cn" secure="false"/>
</cross-domain-policy>
```

#### 3.4 如果是点播呢？
点播和直播的用法是一样一样的，但细节之处有些许区别，比如：
- 点播文件在播放时，播放界面上有进度条展示播放进度，而直播视频是没有的。
- 点播文件的播放不受时间限制（url加了防盗链的话另说），而直播的地址只要主播端结束推流，就播放不了了。
- 点播的m3u8地址，全球第一个用户的访问是没有限制的，直播的m3u8有“懒启动”时间，大约30秒，也就是全球第一个用户的访问一定是失败的，需要30秒后重试才能成功（腾讯云播放器会自动处理这个问题）。
- mp4这种播放协议只能用来点播，不能用来做直播；
- rtmp这种播放协议只能用来做直播，不能用来做点播；

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
var player = new TencentCloud.Player("id_test_video", {
"m3u8"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.m3u8",
"m3u8_hd": "http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8", 
"m3u8_sd": "http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8", 
"autoplay" : true,      //iOS下safari浏览器是不开放这个能力的
"coverpic" : "http://www.test.com/myimage.jpg",
});
```

### Step 5：定制错误提示语
我们默认的提示语您可能觉得不符合您的需求，比如“连接服务器失败”或者“视频格式不支持”等等，我们担心这些提示语在您看来可能太干瘪了，所以腾讯云Web播放器支持提示语定制：
（to-do ander补充）


## 参数列表

| 参数       |     含义  |   示例  |
| :-------- | :--------| :------ |
| m3u8      |   m3u8 播放URL - 原画|  http://2157.liveplay.myqcloud.com/2157_358535a.m3u8| 
| m3u8_hd   |   m3u8 播放URL - 高清|  http://2157.liveplay.myqcloud.com/2157_358535a_900.m3u8 |
| m3u8_sd   |   m3u8 播放URL - 标清|  http://2157.liveplay.myqcloud.com/2157_358535a_550.m3u8 | 
| flv       |   flv 播放URL - 原画|  http://2157.liveplay.myqcloud.com/2157_358535a.flv| 
| flv_hd    |   flv 播放URL - 高清|  http://2157.liveplay.myqcloud.com/2157_358535a_900.flv|
| flv_sd    |   flv 播放URL - 标清|  http://2157.liveplay.myqcloud.com/2157_358535a_550.flv| 
| mp4       |   mp4  播放URL - 原画|  http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.mp4| 
| mp4_hd    |   mp4  播放URL - 高清|  http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.mp4|
| mp4_sd    |   mp4  播放URL - 标清|  http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.mp4| 
| rtmp      |   rtmp 播放URL - 原画|  rtmp://2157.liveplay.myqcloud.com/live/2157_280d88| 
| rtmp_hd   |   rtmp 播放URL - 高清|  rtmp://2157.liveplay.myqcloud.com/live/2157_280d88_900 |
| rtmp_sd   |   rtmp 播放URL - 标清|  rtmp://2157.liveplay.myqcloud.com/live/2157_280d88_550 | 
| autoplay   |   是否自动播放|  iOS下safari浏览器是不开放这个能力的（微信内嵌Webview对特定网页有做App级别的特殊支持） | 
| coverpic  |   预览封面    |  http://www.test.com/myimage.jpg | 

## 错误码表
（to-do ander补充）


## 常见问题

（to-do ander补充）

