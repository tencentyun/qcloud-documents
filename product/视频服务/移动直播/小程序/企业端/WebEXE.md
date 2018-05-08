
<h2> 方案选型 </h2>

WebEXE 和 WebRTC 是我们推出的两套企业端接入方案，下表列出了两套方案的适用场景和优缺点，您可以根据自己的情况自行选择。

| 方案选型| WebEXE | WebRTC |
|:-------:|:-------:|:-------:|
| 文档地址 | [DOC](https://cloud.tencent.com/document/product/454/17004) | [DOC](https://cloud.tencent.com/document/product/454/17005) |
| 试用场景 | 面向公司职员 | 面相普通C类用户 |
| 方案优势 | 可以跳开浏览器的各种限制，实现一些高级特性 | 无需安装插件，Chrome浏览器就能胜任，适合普通用户接入 |
| 方案不足 | 需要使用者按提示安装程序 | 功能受限Chrome浏览器的安全限制 |
| 美颜磨皮 | 支持美颜 | 不支持美颜 |
| 桌面录屏 | 支持桌面录屏 | 不支持录屏 |
| 安装插件 | 需要安装插件 | 不许要任何插件 |
| 依赖的云服务 | [LVB](https://cloud.tencent.com/product/LVB) + [IM](https://cloud.tencent.com/product/im) | [TRTC](https://cloud.tencent.com/product/trtc) + [IM](https://cloud.tencent.com/product/im) |

## Demo体验

用任意浏览器打开 [体验地址](http://img.qcloud.com/open/qcloud/video/act/liteavWeb/avsolution/Index.html) 即可了解 WebEXE 方案，左侧的网页可以替换成您的Web页面，右侧的 TXCloudRoom.exe 用于实现视频通话等功能。

- **网页（Web）**：承载您原有的业务系统和业务逻辑，比如订单系统，CRM系统等各种电子流系统。
- **桌面程序（EXE）**：类似PC版微信这样的应用程序，能够被您的网页直接唤起。具有性能优异，稳定性好能特点，能实现一些浏览器能力范围之外的功能。

![](https://main.qcloudimg.com/raw/30a729f3fc5825c107a342a53ad7b938.png)

## 源码调试
点击 [GitHub](https://github.com/TencentVideoCloudMLVBDev/webexe_web.git) 下载网页端源代码，用本地浏览器双击打开文件中的 index.html，就可以体验和调试 WebEXE 的相关功能。

| 目录 | 说明 |
|:-------:|---------|
| index.html | demo主页面 |
| doubleroom.html | 双人视频通话的demo页面 |
| liveroom.html | 互动视频通话的demo页面 |
| assets | demo页面中使用的 css 样式表和资源文件 |
| js | demo页面中使用的javascript，其中，最为关键的 EXEStart.js就在这里 |

## 方案对接
下面这幅图简单介绍了如何将 WebEXE 方案整合到您的现有的业务系统中：
![](https://main.qcloudimg.com/raw/30281f823d059c5876968385ef97cbc6.png)

### step1: 搭建业务服务器
业务服务器的作用主要是向PC端网页和微信小程序派发 roomid、userid、usersig 这些进行视频通话所必须的信息。其中roomid 和 userid 都可以由您的业务后台自由决定，只要确保不会出现 id重叠 就可以。usersig 的计算则需要参考 [DOC](https://cloud.tencent.com/document/product/454/14548)，我们在官网也提供了 java 和 php 版本的计算[源码](https://cloud.tencent.com/document/product/454/7873#Server)。

### step2: 部署RoomService
WebEXE 实现视频通话服务所使用的 [LiveRoom(直播+连麦)](https://cloud.tencent.com/document/product/454/14606) 和 [RTCRoom(视频通话)](https://cloud.tencent.com/document/product/454/14617) 组件，都依赖一个叫做 RoomService 的后台开源组件（JAVA | Node.js）用于实现视频房间逻辑，您可以点击 [RoomService.zip](https://cloud.tencent.com/document/product/454/7873#Server) 下载到相关代码，部署方法见 zip 包中的说明文档 **README.pdf**。

### step3: 对接PC Web端代码
您的web页面需要 include EXEStarter.js，并且把 step1 中获取的 roomid, userid, usersig 这些信息都传递给 EXEStarter.js 的 createExeAsRoom 函数。其中几个关键参数这里详细说明一下：

| 参数 | 详细说明|
|:-------:|---------|
|sdkAppID | 腾讯云通讯服务用 sdkAppID 区分 IM 客户身份，参考 [DOC](https://cloud.tencent.com/document/product/454/7953#IM_SDKAPPID) 了解怎么获取 |
|accType   | 曾用于区分 APP 类型，现仅出于兼容性原因而保，参考 [DOC](https://cloud.tencent.com/document/product/454/7953#IM_ACCTYPE) 了解怎么获取|
|userID    | 用户ID，您的业务服务器负责分配，各个端不能重复，否则会出现“被踢下线”的情况。 |
|userSig  | 相当于用户密码，具体怎么计算，可以参考 [DOC](https://cloud.tencent.com/document/product/454/14548) 了解。|
|serverDomain| RoomService 地址，step2中部署完RoomService之后即可获得。|
|roomId| 房间ID，您的业务服务器负责分配，小程序端和PC端进入同一个ID的房间，即可进行视频通话。|
| type | RTCRoom 和 LiveRoom 两种模式，其区别可以看 step4 |
| template | 视频窗口摆放样式，默认1V1，更多参考 [Template](https://cloud.tencent.com/document/product/454/17006#EnumDef) 定义。 |
| record | 通话内容是否要进行录制。 |

**EXEStarter.js**  主要用于唤起 TXCloudRoom.exe 桌面程序，并跟 TXCloudRoom.exe 进行双向通讯，您的 Web 页面只需要 include EXEStarter.js 就可以调用其接口函数，音视频相关的复杂功能，则交给 TXCloudRoom.exe 去完成。

| API(EXEStarter.js )                                          | 功能说明                                                  |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| [setListener(object)](https://cloud.tencent.com/document/product/454/17006#setListener) | 设置事件通知回调，用于网页接收来自 TXCloudRoom.exe 的消息 |
| [createExeAsRoom(object)](https://cloud.tencent.com/document/product/454/17006#createExeAsRoom) | 通知 TXCloudRoom.exe 创建或者进入指定的房间               |
| [closeExeAsRoom(object)](https://cloud.tencent.com/document/product/454/17006#closeExeAsRoom) | 通知 TXCloudRoom.exe 离开指定的房间                       |
| [unload()](https://cloud.tencent.com/document/product/454/17006#unload) | 页面在 unload 时，调用此接口，清除相关资源                |

点击[示例代码](https://cloud.tencent.com/document/product/454/17006#code)，可以查看一个简单的唤起 TXCloudRoom.exe 的程序，您也可以在 [GitHub](https://github.com/TencentVideoCloudMLVBDev/webexe_web.git) 上获取一份更加完善的 PC 网页的源代码。

### step4: 对接小程序端代码
小程序端的对接参考微信端的文档：

| 文档链接 | 适合场景 |
|------------|-------------|
| [**&lt;rtc-room&gt;**](https://cloud.tencent.com/document/product/454/15364) | 纯视频通话场景，比如双人1v1视频通话，或者视频会议 |
|[**&lt;live-room&gt;**](https://cloud.tencent.com/document/product/454/15368)| 直播+连麦混合场景，基于LVB服务实现，所以既能以很低的带宽成本支持上千人的并发观看，又能支持观众和主播之间的实时视频通话|

## 如何录制
您可以把用户整个直播过程录制下来，然后作为视频文件用于回看。具体如何实现录制功能，可以查看[全程录制](https://cloud.tencent.com/document/product/454/17026)。

<video src="
http://1252463788.vod2.myqcloud.com/e12fcc4dvodgzp1252463788/c490bab57447398155981625642/TwA4JteAe40A.mp4" controls="controls">
您的浏览器不支持 video 标签。
</video>

## 内网穿透
很多企业内部都有安全网关，禁止企业内部网络对互联网的访问，而腾讯视频云的解决方案都是依赖互联网接入的，所以要解决这个问题，就需要代理服务器的帮助：

![](https://main.qcloudimg.com/raw/22550909ad08fbf301390a23220eb501.png)

### Step1: 搭建音视频代理服务器（用于透传数据）

采用NAT端口映射，就是将内网的机器映射到代理服务器的端口，代理服务器转发内网和腾讯云之间音视频数据包。下载Bash脚本<a href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/WebEXE/Proxy/NATConfig.sh">NATConfig.sh</a>。打开文件和修改下图中IP的值，指定代理服务器接收网卡的IP，以及腾讯云推流和拉流服务器的地址，然后执行脚本，完成配置。

![](https://main.qcloudimg.com/raw/c6e94f62213899f4b7a3e3c111e8cac5.png)


### Step2: 搭建Socks5代理服务器（用于透传信令）

Socks5代理服务器，好比与在内网机器和腾讯云服务器之间搭建了一座桥梁，网络数据包就是桥上的行人，走过桥，河流两边就可以说话和交流。通过下载和执行我们提供的Bash脚本，绑定接收代理的网卡和出口网卡的端口号，来搭建Socks5代理服务器。

如果您的代理服务器是Ubuntu，请下载Bash脚本<a href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/WebEXE/Proxy/Socks5Config_Ubuntu.sh">Socks5Config_Ubuntu.sh</a>，执行脚本，完成配置Socks5。

如果您的代理服务器是CentOS，请下载Bash脚本<a href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/WebEXE/Proxy/Socks5Config_CentOS.sh">Socks5Config_CentOS.sh</a>，执行脚本，完成配置Socks5。


### Step3: 使用EXEStarter.js设置代理服务器

设置Web页面的代理参数，给EXEStarter.js的 createExeAsRoom 接口传入 proxy_ip 和 proxy_port 参数，分别指定代理服务器的IP和端口。

```javascript
EXEStarter.createExeAsRoom({
    //...
    custom: {
     	proxy_ip: "x.x.x.x", 	// 代理IP，可以不设置，默认不开启代理
     	proxy_port: 1080,	    // 代理端口，可以不设置，默认不开启代理
    }
});
```

