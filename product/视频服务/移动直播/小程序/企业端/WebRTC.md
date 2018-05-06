## Demo 体验

用 Chrome 浏览器打开 [体验地址](http://img.qcloud.com/open/qcloud/video/act/liteavWeb/webrtc/webrtc.html#/)，即可体验 Chrome（WebRTC） + 微信（小程序）的视频通话功能，如下图所示：

![](https://main.qcloudimg.com/raw/81edf044e0a40ccfd4794b91185f1f82.jpg)

## 源码调试

### Client
点击 [webrtc(Chrome).zip](http://dldir1.qq.com/hudongzhibo/mlvb/webrtc(Chrome).zip) 下载PC端的网页源代码，该页面只能运行于支持 WebRTC 的浏览器中：

| 目录 | 说明 | 
|:-------:|---------|
| index.html | Demo主页面 | 
| vue| vue框架代码 | 
| third | 第三方 js 文件 | 
| component | Demo页面的主要业务逻辑位于该文件夹下的各个 js 文件中 | 

### Server
点击 [webrtc_server_list.zip](http://dldir1.qq.com/hudongzhibo/mlvb/webrtc_server_list.zip) 可以下载一份 **java** 版本的 Server 端源码，这份代码的主要作用是实现了一个简单的（无鉴权的）房间列表，可以支持创建通话房间，关闭通话房间等功能。如果您只是希望打通视频通话（在 Chrome 和 小程序端 写死一个 roomid），则不太需要这部分代码的帮助。 

| 目录 | 说明 | 
|:-------:|---------|
|README.pdf | 介绍了如何使用这份后台代码 | 
|后台接口表.pdf| 介绍了这份后台代码的内部实现细节 | 
| src | java 版本的后台房间列表源代码 | 

## 对接原理

