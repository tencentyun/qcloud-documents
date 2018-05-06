
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
点击 <font color=red>DOWNLOAD</font> 下载网页端源代码，其中：

| 目录 | 说明 | 
|:-------:|---------|
| index.html | demo主页面 | 
| doubleroom.html | 双人视频通话的demo页面 | 
| multiroom.html | 多人视频通话的demo页面 | 
| css| demo页面中使用的 css 样式表 | 
| image | demo页面中使用的资源文件 | 
| js | demo页面中使用的javascript，其中，最为关键的 EXEStart.js就在这里 | 

用本地浏览器双击打开文件中的 index.html，就可以体验和调试 WebEXE 的相关功能。

## 方案对接
下面这幅图简单介绍了如何将 WebEXE 方案整合到您的现有的业务系统中：
![](https://main.qcloudimg.com/raw/30281f823d059c5876968385ef97cbc6.png)

- **step1: 搭建业务服务器**
业务服务器的作用主要是向PC端网页和微信小程序派发 roomid、userid、usersig 这些进行视频通话所必须的信息。其中roomid 和 userid 都可以由您的业务后台自由决定，只要确保不会出现 id重叠 就可以。usersig 的计算则需要参考 [DOC](https://cloud.tencent.com/document/product/454/14548)，我们在官网也提供了 java 和 php 版本的计算[源码](https://cloud.tencent.com/document/product/454/7873#Server)。
 
- **step2: 对接PC Web端代码**
您的web页面需要 include EXEStarter.js，并且把 step1 中获取的 roomid, userid, usersig 这些信息都传递给 EXEStarter.js 的 createExeAsRoom 函数。其中几个关键参数这里详细说明一下：


| 参数 | 详细说明|
|:-------:|---------|
| type | RTCRoom 和 LiveRoom 两种模式，其区别可以看 step3 | 
| template | 界面模板，比如 1v1, 1v3 等等 | 
|sdkAppID | 腾讯云通讯服务用 sdkAppID 区分 IM 客户身份，参考 [DOC](https://cloud.tencent.com/document/product/454/7953#IM_SDKAPPID) 了解怎么获取 | 
|accType   | 曾用于区分 APP 类型，现仅出于兼容性原因而保，参考 [DOC](https://cloud.tencent.com/document/product/454/7953#IM_ACCTYPE) 了解怎么获取|
|userID    | 用户ID，您的业务服务器负责分配，各个端不能重复，否则会出现“被踢下线”的情况 |
| userSig  | 相当于用户密码，具体怎么计算，可以参考 [DOC](https://cloud.tencent.com/document/product/454/14548) 了解。|


- **step3: 对接小程序端代码**
小程序端的对接参考微信端的文档：

| 文档链接 | 适合场景 |
|------------|-------------|
| [**&lt;rtc-room&gt;**](https://cloud.tencent.com/document/product/454/15364) | 纯视频通话场景，比如双人1v1视频通话，或者视频会议 |
|[**&lt;live-room&gt;**](https://cloud.tencent.com/document/product/454/15368)| 直播+连麦混合场景，基于LVB服务实现，所以既能以很低的带宽成本支持上千人的并发观看，又能支持观众和主播之间的实时视频通话|

- **step4: 部署RoomService（可选）**
因为 RoomService 是一个[开源](https://cloud.tencent.com/document/product/454/7873#Server)的（java | Node.js）组件，所以大部分客户都选择自行部署，部署方法见 zip 包中的说明文档。

## API（EXEStarter.js）
**EXEStarter.js**  主要用于唤起 TXCloudRoom.exe 桌面程序，并跟 TXCloudRoom.exe 进行双向通讯，您的 Web 页面只需要 include EXEStarter.js 就可以调用其接口函数，音视频相关的复杂功能，则交给 TXCloudRoom.exe 去完成。

| 成员函数                                    | 功能说明                                     |
| ------------------------------------------- | -------------------------------------------- |
| [setListener(object)](https://cloud.tencent.com/document/product/454/17006#setListener)         | 设置事件通知回调，用于网页接收来自 TXCloudRoom.exe 的消息 |
| [createExeAsRoom(object)](https://cloud.tencent.com/document/product/454/17006#createExeAsRoom) | 通知 TXCloudRoom.exe 创建或者进入指定的房间 |
| [closeExeAsRoom(object)](https://cloud.tencent.com/document/product/454/17006#closeExeAsRoom)   | 通知 TXCloudRoom.exe 离开指定的房间 |
| [setTemplateCfg()](https://cloud.tencent.com/document/product/454/17006#setTemplateCfg)         | 设置 TXCloudRoom.exe 的 UI 模板        |
| [unload()](https://cloud.tencent.com/document/product/454/17006#unload)                         | 页面在 unload 时，调用此接口，清除相关资源   |

下面这段代码演示了如何手写一个简单的 HTML 网页文件，实现 WebEXE 的唤起功能。

```html
<HTML>
<HEAD>
    <meta http-equiv="Content-Type" content="text/html; charset=gb2312"/>
    <TITLE>web+exe解决方案test</TITLE>
    <script type="text/javascript" src="../../sdk/exestart/EXEStarter.js" charset="utf-8"></script>
</HEAD>
<BODY onload="" onunload="">
     <input type=submit value="开课" 
		 onClick="opencourse(document.getElementById('UserID').value, document.getElementById('RoomID').value);">
     <br></br><br></br>
     <input size="30" id="UserID" value="TestUser_1231d21f2d"> userID <br></br>
     <input size="30" id="RoomID" value="room_123d2f456s2s12"> roomID
    <script>
        function opencourse(userID, roomID)
		{
            var tRoomID = roomID;
            var tUserID = userID;
            var roomserverInfo; var roomServerDoMain = "https://room.qcloud.com/";
            //第一步：通过您的账号userid，获取roomserver的 usersig
            getSDKLoginInfo({
                data: {  userID: tUserID, roomServerDomain: 
                       roomServerDomain,method : "GET",time: 24 * 60 * 60 * 7
                },
                success: function (res) {
                    if (res.status && res.status === 200) {roomserverInfo = res.data;}
                },
            });
            //第二步:设置exe的模板样式
            EXEStarter.setTemplateCfg({
                data: { serverDomain: roomServerDoMain,},
                style: {
                    type: EXEStarter.StyleType.RTCRoom,
                    template: EXEStarter.Template.Template1V3,
                    userList: true, IMList: true,whiteboard: true, screenShare: true,
                }
            });

            //第三步：通过usersig和您的房间信息，拉起本地应用程序。
            EXEStarter.createExeAsRoom({
                userdata: {
                    userID: roomserverInfo.userID,
                    userName: "雷锋",
                    sdkAppID: roomserverInfo.sdkAppID,
                    accType: roomserverInfo.accountType,
                    userSig: roomserverInfo.userSig,
                },
                roomdata: {
                    roomAction: EXEStarter.RoomAction.CreateRoom,
                    roomID: tRoomID,
                    roomName:  "雷锋的房间",
                    roomTitle:  "1V1视频",
                    roomLogo: "http://cosgz.myqcloud.com/logo/liveroom_logo.png",
                },
                success: function (ret) {},
                fail: function () {},
                timeout: function () {},
            })
        }
    </script>
</BODY>
</HTML>
```

## 如何录制

## 网络限制

## 原理解释

下图展示了 EXEStarter.js 是如何唤起 TXCloudRoom.exe 并建立双向通讯能力的，这部分您可以选择性的了解，并非关键信息。

![](https://main.qcloudimg.com/raw/c5ec0c09edc90c96d18b0270ebe047c4.png)
- 网页通过 TXCloudRoom:// 伪协议唤起 TXCloudRoom.exe 桌面程序。
- 如果网页成功唤起 TXCloudRoom.exe ，则建立双向通讯通道，网页可以向 exe 程序发送指令，同时 exe 程序也会将各种状态和事件回传给网页。
- 如果网页没有唤起 TXCloudRoom.exe，说明用户没有安装TXCloudRoom.exe，会提示用户下载安装。