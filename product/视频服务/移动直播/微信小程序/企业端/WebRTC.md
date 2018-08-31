
<h2> Demo 体验 </h2>

用 Chrome 浏览器打开 [体验地址](https://sxb.qcloud.com/miniApp/#/)，即可体验 Chrome（WebRTC） + 微信（小程序）的视频通话功能，如下图所示：

![](https://main.qcloudimg.com/raw/81edf044e0a40ccfd4794b91185f1f82.jpg)

## 源码调试

### Client
点击 [webrtc(Chrome).zip](https://github.com/TencentVideoCloudMLVBDev/webrtc_pc) 下载PC端的网页源代码，该页面只能运行于支持 WebRTC 的浏览器中：

| 目录 | 说明 | 
|:-------:|---------|
| index.html | Demo主页面 | 
| vue| vue框架代码 | 
| third | 第三方 js 文件 | 
| component | Demo页面的主要业务逻辑位于该文件夹下的各个 js 文件中 | 

### Server
点击 [webrtc_server_list.zip](https://github.com/TencentVideoCloudMLVBDev/webrtc_server_java) 可以下载一份 **java** 版本的 Server 端源码，这份代码的主要作用是实现了一个简单的（无鉴权的）房间列表，可以支持创建通话房间、关闭通话房间等功能。如果您只是希望打通视频通话（在 Chrome 和 小程序端 写死一个 roomid），则不太需要这部分代码的帮助。 

| 目录 | 说明 | 
|:-------:|---------|
|README.pdf | 介绍了如何使用这份后台代码 | 
|后台接口表.pdf| 介绍了这份后台代码的内部实现细节 | 
| src | java 版本的后台房间列表源代码 | 

## 对接原理
下面这幅图简单介绍了如何将 WebRTC 方案整合到您的现有的业务系统中：
![](https://main.qcloudimg.com/raw/6670541d971f3a133027342b29265aaf.png)

### step1: 搭建业务服务器
业务服务器的作用主要是向PC端网页和微信小程序派发 userid、usersig、roomid、 privateMapKey 这些进行视频通话所必须的信息。其中roomid 和 userid 都可以由您的业务后台自由决定，只要确保不会出现 id重叠 就可以。usersig 和 privateMapKey 的计算则需要参考示例源码[（java | PHP）](https://cloud.tencent.com/document/product/454/7873#Server)。
 
### step2: 对接 Chrome
虽然谷歌给出了很多的文档和教程介绍如何使用使用 WebRTC，但是官方文档过于追求灵活性，所以理解成本很高，腾讯云推出了一个简化版的封装接口，阅读腾讯云 [WebRTC API](https://cloud.tencent.com/document/product/647/16865) 了解如何通过几个函数的调用就能完成 WebRTC 的 Chrome 端对接。

### step3: 对接小程序端代码
微信 6.6.6 版本中开始支持 WebRTC 互通，参考 [**&lt;webrtc-room&gt;**](https://cloud.tencent.com/document/product/454/16914) 了解如何快速实现一个支持 WebRTC 视频通话的小程序。


