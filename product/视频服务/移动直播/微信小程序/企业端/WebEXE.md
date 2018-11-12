
<h2> 方案选型 </h2>

WebEXE 和 WebRTC 是我们推出的两套企业端接入方案，下表列出了两套方案的适用场景和优缺点，您可以根据自己的情况自行选择。

| 方案选型| WebEXE | WebRTC |
|:-------:|:-------:|:-------:|
| 文档地址 | [DOC](https://cloud.tencent.com/document/product/454/17004) | [DOC](https://cloud.tencent.com/document/product/454/17005) |
| 适用场景 | 面向公司职员 | 面向普通C类用户 |
| 方案优势 | 可以跳开浏览器的各种限制，实现一些高级特性 | 无需安装插件，Chrome浏览器就能胜任，适合普通用户接入 |
| 方案不足 | 需要使用者按提示安装程序 | 功能受到Chrome浏览器的安全限制 |
| 美颜磨皮 | 支持美颜 | 不支持美颜 |
| 桌面录屏 | 支持桌面录屏 | 需要安装录屏插件 |
| 本地录制 | 支持本地录制 | 不支持本地录制 |
| 依赖的云服务 | [LVB](https://cloud.tencent.com/product/LVB) + [IM](https://cloud.tencent.com/product/im) | [TRTC](https://cloud.tencent.com/product/trtc) + [IM](https://cloud.tencent.com/product/im) |

## Demo体验

用任意浏览器打开 [体验地址](http://img.qcloud.com/open/qcloud/video/act/liteavWeb/avsolution/Index.html) 即可了解 WebEXE 方案，左侧的网页可以替换成您的Web页面，右侧的 TXCloudRoom.exe 用于实现视频通话等功能。

- **网页（Web）**：承载您原有的业务系统和业务逻辑，比如订单系统，CRM系统等各种电子流系统。
- **桌面程序（EXE）**：类似PC版微信这样的应用程序，能够被您的网页直接唤起。具有性能优异，稳定性好等特点，能实现一些浏览器能力范围之外的功能。

![](https://main.qcloudimg.com/raw/30a729f3fc5825c107a342a53ad7b938.png)

## 源码调试

### PC 网页
点击 [GitHub](https://github.com/TencentVideoCloudMLVBDev/webexe_web_source) 下载网页端源代码，用本地浏览器双击打开文件中的 index.html，就可以体验和调试 WebEXE 的相关功能。首次使用时，会提示需要下载和安装本地客户端插件。

| 目录 | 说明 |
|:-------:|---------|
| index.html | demo主页面 |
| doubleroom.html | 双人视频通话的demo页面 |
| liveroom.html | 互动视频通话的demo页面 |
| assets | demo页面中使用的 css 样式表和资源文件 |
| js | demo页面中使用的javascript，其中，最为关键的 EXEStart.js就在这里 |
| exe | 包含TXCloudRoomSetup.exe安装包 |

### Server
点击 [GitHub](https://github.com/TencentVideoCloudMLVBDev/roomlist_server_java ) 可以下载一份 **java** 版本的 Server 端源码，这份代码的主要作用是实现了一个简单的（无鉴权的）房间列表，可以支持创建通话房间、关闭通话房间等功能。如果您只是希望打通视频通话（在 PC 网页和小程序各写死一个 roomid），则不太需要这部分代码的帮助。 

| 目录 | 说明 |
|:-------:|---------|
|README.pdf | 介绍了如何使用这份后台代码 |
|后台接口表.pdf| 介绍了这份后台代码的内部实现细节 |
| src | java 版本的后台房间列表源代码 |


## 方案对接
下面这幅图简单介绍了如何将 WebEXE 方案整合到您的现有的业务系统中：
![](https://main.qcloudimg.com/raw/c89609dcfa5388a7a3d4d00d5d7f94cc.png)

### step1: 搭建业务服务器
业务服务器的作用主要是向PC端网页和微信小程序派发 roomid、userid、usersig 这些进行视频通话所必须的信息。其中roomid 和 userid 都可以由您的业务后台自由决定，只要确保不会出现 id重叠 就可以。usersig 的计算则需要参考 [DOC](https://cloud.tencent.com/document/product/454/14548)，我们在官网也提供了 java 和 php 版本的计算[源码](https://cloud.tencent.com/document/product/454/7873#Server)。

### step2: 部署RoomService
WebEXE 实现视频通话服务所使用的 [LiveRoom(直播+连麦)](https://cloud.tencent.com/document/product/454/14606) 和 [RTCRoom(视频通话)](https://cloud.tencent.com/document/product/454/14617) 组件，都依赖一个叫做 RoomService 的后台开源组件（JAVA | Node.js）用于实现视频房间逻辑，您可以点击 [RoomService.zip](https://cloud.tencent.com/document/product/454/7873#Server) 下载到相关代码，部署方法见 zip 包中的说明文档 **README.pdf**。

### step3: 对接PC Web端代码
您的web页面需要 include [**EXEStarter.js**](https://cloud.tencent.com/document/product/454/17006) 这个 javascript 文件，并且把 step1 中获取的 roomid, userid, usersig 这些信息都传递给 [**EXEStarter.js**](https://cloud.tencent.com/document/product/454/17006) 的 **startEXE** 函数。其中几个关键参数这里详细说明一下：

|      参数      | 详细说明                                     |
| :----------: | ---------------------------------------- |
|   sdkAppID   | 腾讯云通讯服务用 sdkAppID 区分 IM 客户身份，参考 [DOC](https://cloud.tencent.com/document/product/454/7953#IM_SDKAPPID) 了解怎么获取 |
|   accType    | 曾用于区分 APP 类型，现仅出于兼容性原因而保，参考 [DOC](https://cloud.tencent.com/document/product/454/7953#IM_ACCTYPE) 了解怎么获取 |
|    userID    | 用户ID，您的业务服务器负责分配，各个端不能重复，否则会出现“被踢下线”的情况  |
|   userSig    | 相当于用户密码，具体怎么计算，可以参考 [DOC](https://cloud.tencent.com/document/product/454/14548) 了解 |
| serverDomain | RoomService 地址，step2中部署完RoomService之后即可获得 |
|    roomId    | 房间ID，您的业务服务器负责分配，小程序端和PC端进入同一个ID的房间，即可进行视频通话 |
|     type     | RTCRoom 和 LiveRoom 两种模式，其区别可以看 step4     |
|   template   | 视频窗口摆放样式，默认1V1，更多参考 [Template](https://cloud.tencent.com/document/product/454/17006#EnumDef) 定义 |
|    mixRecord    | 云端录制，在这种录制模式下，EXE并不参与录制工作，所有录制均在后台进行，因此 WebEXE 和 WebRTC 两种解决方案都通用，但也存在缺乏定制型的缺点。 |
|    screenRecord    | 本地录制，是WebEXE特有的录制模式，EXE程序直接抓取本地的画面并实时生成录制影片，根据参数不同，EXE会将生成的影片文件存在本地或者推到云端。|                         |
|    cloudRecordUrl |  如果 screenRecord 选择 RecordScreenToServer 或者 RecordScreenToBoth，需要指定一个 rtmp:// 推流地址，这样视频流就能按照正常的推流录制模式，直接将影片内容录制到云端。|

 [**EXEStarter.js**](https://cloud.tencent.com/document/product/454/17006)   主要用于唤起 TXCloudRoom.exe 桌面程序，并跟 TXCloudRoom.exe 进行双向通讯，您的 Web 页面只需要处理房间管理等逻辑，音视频相关的复杂功能，则交给 TXCloudRoom.exe 去完成。

点击[示例代码](https://cloud.tencent.com/document/product/454/17006#Code)，可以查看一个简单的唤起 TXCloudRoom.exe 的程序，您也可以在 [GitHub](https://github.com/TencentVideoCloudMLVBDev/webexe_web_source) 上获取一份更加完善的适用于 PC 端网页的源代码。

### step4: 对接小程序端代码
小程序端的对接参考微信端的文档：

| 文档链接                                     | 适合场景                                     |
| ---------------------------------------- | ---------------------------------------- |
| [**&lt;rtc-room&gt;**](https://cloud.tencent.com/document/product/454/15364) | 纯视频通话场景，比如双人1v1视频通话，或者视频会议               |
| [**&lt;live-room&gt;**](https://cloud.tencent.com/document/product/454/15368) | 直播+连麦混合场景，基于LVB服务实现，所以既能以很低的带宽成本支持上千人的并发观看，又能支持观众和主播之间的实时视频通话 |

## 如何录制
您可以把用户整个直播过程录制下来，然后作为视频文件用于回看。具体如何实现录制功能，可以查看[全程录制](https://cloud.tencent.com/document/product/454/17026)。

<video src="
http://1252463788.vod2.myqcloud.com/e12fcc4dvodgzp1252463788/c490bab57447398155981625642/TwA4JteAe40A.mp4" controls="controls">
您的浏览器不支持 video 标签。
</video>
