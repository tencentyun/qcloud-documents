众所周知，Web应用的通信过程通常是客户端通过浏览器发出一个请求，服务器端接收请求后进行处理并返回结果给客户端，客户端浏览器将信息呈现。这种机制对于信息变化不是特别频繁的应用可以良好支撑，但对于实时要求高、海量并发的应用来说显得捉襟见肘，尤其在当前业界移动互联网蓬勃发展的趋势下，高并发与用户实时响应是Web应用经常面临的问题，例如金融证券的实时信息、Web导航应用中的地理位置获取、社交网络的实时消息推送等。

传统的请求-响应模式的Web开发在处理此类业务场景时，通常采用实时通讯方案。例如常见的轮询方案，其原理简单易懂，就是客户端以一定的时间间隔频繁请求的方式向服务器发送请求，来保持客户端和服务器端的数据同步。其问题也很明显：当客户端以固定频率向服务器端发送请求时，服务器端的数据可能并没有更新，带来很多无谓请求，浪费带宽，效率低下。

基于Flash，AdobeFlash通过自己的Socket实现完成数据交换，再利用Flash暴露出相应的接口给JavaScript调用，从而达到实时传输目的。此方式比轮询要高效，且因为Flash安装率高，应用场景广泛。然而，移动互联网终端上Flash的支持并不好：IOS系统中无法支持Flash，Android虽然支持Flash但实际的使用效果差强人意，且对移动设备的硬件配置要求较高。2012年Adobe官方宣布不再支持Android4.1+系统，宣告了Flash在移动终端上的死亡。

传统的Web模式在处理高并发及实时性需求的时候，会遇到难以逾越的瓶颈，需要一种高效节能的双向通信机制来保证数据的实时传输。在此背景下，基于HTML5规范的、有Web TCP之称的 WebSocket应运而生。早期HTML5并没有形成业界统一的规范，各个浏览器和应用服务器厂商有着各异的类似实现，如IBM的MQTT、Comet开源框架等。直到2014年，HTML5终于尘埃落地，正式落实为实际标准规范，各个应用服务器及浏览器厂商逐步开始统一，在 JavaEE7中也实现了WebSocket协议。至此无论是客户端还是服务端的WebSocket都已完备。用户可以查阅[HTML5规范](http://www.jb51.net/w3school/html5/)，熟悉新的HTML协议规范及WebSocket支持。

## WebSocket 机制
以下简要介绍一下WebSocket的原理及运行机制。

WebSocket是HTML5下一种新的协议。它实现了浏览器与服务器全双工通信，能更好的节省服务器资源和带宽并达到实时通讯的目的。它与HTTP一样通过已建立的TCP连接来传输数据，但是它和HTTP最大不同是：
- WebSocket是一种双向通信协议。在建立连接后，WebSocket服务器端和客户端都能主动发送数据给对方或向对方接收数据，就像Socket一样；
- WebSocket需要像TCP一样，先建立连接，连接成功后才能相互通信。

传统HTTP客户端与服务器请求响应模式如下图所示：
![](https://main.qcloudimg.com/raw/44a1251733ad215969b14f66a0f2ec61.jpg)

WebSocket模式客户端与服务器请求响应模式如下图：
![](https://main.qcloudimg.com/raw/f62fa2415a9f8bdcbe6ea2053aca41ed.jpg)

上图对比可以看出，相对于传统HTTP每次请求-应答都需要客户端与服务端建立连接的模式，WebSocket是类似Socket的TCP长连接通讯模式。一旦WebSocket连接建立后，后续数据都以帧序列的形式传输。在客户端断开WebSocket连接或Server端中断连接前，不需要客户端和服务端重新发起连接请求。在海量并发及客户端与服务器交互负载流量大的情况下，极大的节省了网络带宽资源的消耗，有明显的性能优势，且客户端发送和接受消息是在同一个持久连接上发起，实时性优势明显。

相比HTTP长连接，WebSocket有以下特点：
- 是真正的全双工方式，建立连接后客户端与服务器端是完全平等的，可以互相主动请求。而HTTP长连接基于HTTP，是传统的客户端对服务器发起请求的模式。
- HTTP长连接中，每次数据交换除了真正的数据部分外，服务器和客户端还要大量交换HTTP header，信息交换效率很低。Websocket协议通过第一个request建立了TCP连接之后，之后交换的数据都不需要发送 HTTP header就能交换数据，这显然和原有的HTTP协议有区别所以它需要对服务器和客户端都进行升级才能实现（主流浏览器都已支持HTML5）。此外还有 multiplexing、不同的URL可以复用同一个WebSocket连接等功能。这些都是HTTP长连接不能做到的。


下面再通过客户端和服务端交互的报文对比WebSocket通讯与传统HTTP的不同点：

在客户端，new WebSocket实例化一个新的WebSocket客户端对象，请求类似 ws://yourdomain:port/path 的服务端WebSocket URL，客户端WebSocket对象会自动解析并识别为WebSocket请求，并连接服务端端口，执行双方握手过程，客户端发送数据格式类似：

```
GET /webfin/websocket/ HTTP/1.1
Host: localhost
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: xqBt3ImNzJbYqRINxEFlkg==
Origin: http://localhost:8080
Sec-WebSocket-Version: 13
```

可以看到，客户端发起的WebSocket连接报文类似传统HTTP报文，`Upgrade：websocket`参数值表明这是WebSocket类型请求，`Sec-WebSocket-Key`是WebSocket客户端发送的一个 base64编码的密文，要求服务端必须返回一个对应加密的`Sec-WebSocket-Accept`应答，否则客户端会抛出`Error during WebSocket handshake`错误，并关闭连接。

服务端收到报文后返回的数据格式类似：

```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: K7DJLdLooIwIG/MOpvWFB3y3FE8=
```

`Sec-WebSocket-Accept`的值是服务端采用与客户端一致的密钥计算出来后返回客户端的，`HTTP/1.1 101 Switching Protocols`表示服务端接受WebSocket协议的客户端连接，经过这样的请求-响应处理后，两端的WebSocket连接握手成功, 后续就可以进行TCP通讯了。用户可以查阅[WebSocket协议栈](http://tools.ietf.org/html/rfc6455)了解WebSocket客户端和服务端更详细的交互数据格式。

在开发方面，WebSocket API 也十分简单：只需要实例化 WebSocket，创建连接，然后服务端和客户端就可以相互发送和响应消息。在WebSocket 实现及案例分析部分可以看到详细的 WebSocket API 及代码实现。

腾讯云公网有日租类型七层负载均衡转发部分支持Websocket，目前包括英魂之刃、银汉游戏等多家企业已接入使用。当出现不兼容问题时，请修改websocket配置，websocket server不校验下图中圈出的字段：

![](https://main.qcloudimg.com/raw/bd313e9a949fb949256be37499354d4b.png)

一个使用WebSocket应用于视频的业务思路如下：
- 使用心跳维护websocket链路，探测客户端端的网红/主播是否在线
- 设置负载均衡7层的proxy_read_timeout默认为60s
- 设置心跳为50s，即可长期保持Websocket不断开

近期Websocket将开放自定义配置。
