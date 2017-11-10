## 功能介绍
如果您的产品中直播内容很好，那么仅靠 APP 的传播势必阻碍产品的发展速度，依靠社交平台（微信朋友圈、新浪微博等等）的网页链接分享能力能够很好地解决这个问题。

**微信朋友圈分享** 是目前最流行也是最有效果的社交传播方案，本文就以微信分享为例，介绍如何为您的产品构建起 Web 端的闭环体验。

![](//mc.qcloudimg.com/static/img/00d2cbbce2b70639effcab3124a8db3b/image.jpg)

## 技术难点
要在网页上观看直播，只需要在页面中添加一个 **video标签** 即可，这看似并没有什么难度。然而，要做到较好的用户体验，需要克服很多的技术难点：
- **如何在Android浏览器上做好兼容？**
Android 浏览器的差异就跟 Android 系统一样种类繁多，制式和标准各不统一，经常会遇到在某款手机上效果调整OK，但到了另一款手机上就完全变了样，兼容性问题是个非常耗时，且依赖经验的过程。

- **如何在Web页面上跟主播文字互动？**
主播用 APP 做直播，观众在网页端观看，那么只有观看没有互动能有什么效果呢？所以我们必须要解决在网页上跟主播互动的难题。

- **面对 X5 浏览器内核应当怎样应对？**
Android系统上，从微信或者QQ上点开的网页，基本都是QQ浏览器推出的 X5 内核，X5 内核在视频播放这里有自己的策略和规则，如果您不清楚，会面临很多的坑要踩。

- **面对 PC 浏览器内核应当怎样应对？**
PC 上的浏览器都不能原生支持直播视频流，所以如果 Web 页面被在 PC 上打开却看不了视频，也是非常尴尬的事情。

好，接下来就让我们通过如下的对接攻略，帮您解决上述提到的几个技术难题。

## 对接攻略
整体技术架构如下图所示：
![](//mc.qcloudimg.com/static/img/b76f4b3b1b1961d8a8d4d0ea4dc14ad2/image.png)

| 对接步骤 | 步骤说明 | 参考指引 |
|:----------:|-------------|:------------:|
| step1 | 您的APP在直播开始前，先要把分享URL先分享到微信朋友圈上去。 | [微信分享URL](#step1.3A-.E5.BE.AE.E4.BF.A1.E5.88.86.E4.BA.ABurl) |
| step2 | 分享者好的好友在朋友圈中看到这条分享，并点击打开。 |  [用户打开链接](#step2.3A-.E7.94.A8.E6.88.B7.E6.89.93.E5.BC.80.E9.93.BE.E6.8E.A5) |
| step3 | 微信内嵌的WebView（浏览器）会从URL指定的静态CDN服务器上拉取Web页面（HTML+JS） |  [Web页面制作](#step3.3A-web.E9.A1.B5.E9.9D.A2.E5.88.B6.E4.BD.9C) |
| step4 | 网页中的JS（javascript）代码通过 ajax 异步请求方式到您的业务后台Server获取必要的展示信息。 |  [Web后台搭建](#step4.3A-web.E5.90.8E.E5.8F.B0.E6.90.AD.E5.BB.BA) |
| step5 | 网页通过组合直播（LVB）、点播（VOD）和云通讯（IM）等服务，实现Web端的直播观看体验。 |  [页面做了什么](#step5.3A-.E9.A1.B5.E9.9D.A2.E5.81.9A.E4.BA.86.E4.BB.80.E4.B9.88) |


### Step1: 微信分享URL
我们在小直播的源码中，使用友盟的组件默认实现了到新浪、微信、朋友圈、QQ 以及 QQ空间 的分享能力，以便您直接快速参考:

<table class="t">
<tbody><tr>
<th width=150> 所属平台
</th><th width=450> 源码参考
</th><th width=150> 参考文档
</th></tr>
<tr>
<td style="text-align: center;"> iOS 平台
</td><td> 在“小直播”的终端源码包中搜索 "WechatTimeLine" 即可。
</td><td style="text-align: center;"> <a href="http://dev.umeng.com/social/ios/quick-integration">友盟分享组件</a>
</td></tr>
<tr>
<td style="text-align: center;"> Android 平台
</td><td> 在“小直播”的终端源码包中搜索 "ShareAction" 即可。
</td><td style="text-align: center;"> <a href="http://dev.umeng.com/social/android/quick-integration">友盟分享组件</a>
</td></tr>
</tbody></table>

具体分享的URL是什么呢？我们会在 [页面做了什么](#step5.3A-.E9.A1.B5.E9.9D.A2.E5.81.9A.E4.BA.86.E4.BB.80.E4.B9.88) 中向您详细介绍。

### Step2: 用户打开链接
这一步是用户操作，我们不需要做什么，但是有几个点我们需要给您同步：
- **安全拦截**
不是所有的视频地址都能在微信里播放的，更精确的说，是大部分 URL 都不行，必须要去微信申请安全许可。否则，即使网页可以打开，里面的视频也是加载不出来，因为微信在流媒体加载前就已经给你拦截掉了。

- **X5 内核**
由于都是隶属腾讯旗下的产品，Android 版微信的内嵌网页，大概率是使用 X5 浏览器内核（QQ浏览器内核）打开页面，但也有可能是使用系统自带的浏览器打开。X5 浏览器内核对常见流媒体视频协议的支持还是不错的，尤其是 HLS(m3u8) 和 MP4。

- **Safari 内核**
在 iOS 平台并没有其它浏览器内核出来表演的份，只有 Safari 内核可以使用，但是微信有能力操控它内嵌的 WebView 控件实现一些 iPhone 自带的 Safari 浏览器默认不开启的功能，比如 Video 的自动播放。（然而，这个功能指开放给了部分域名）

### Step3: Web页面制作
这部分工作可以交给贵团队的 Web **前端工程师**处理。当然，从零开始制作一个支持在线直播观看，同时又具备聊天室功能的 Web 页面，还是需要一定的经验储备的，所以我们想要尽可能地为您提供一些快速上手的参考：

小直播源码集中包含 Web 分享页面的 [DEMO源码](https://cloud.tencent.com/document/product/454/6991) ，实现了**直播观看**、**文本消息**以及**点赞**等功能。

| 文件名 | 所属文件夹 | 功能说明 |
|:-------: |:--------------:|-------------|
| mobile.css | css | 示例网页的CSS样式表文件，负责控制页面的外观和形态，可以自由修改和替换。 |
| pictures | img | 示例网页所用的示例图片，您可以根据需要自行替换和调整。 |
| json2.js     | sdk |  IM 云通讯的基础JS库，主要用于提供Web端的聊天室功能相关API。 | 
| webim.js    | sdk | IM 云通讯的基础JS库，主要用于提供Web端的聊天室功能相关API。 |
| base.js      |  js  | IM 云通讯的基础JS库，主要用于提供Web端的聊天室功能相关API。 |
| lib.js          | js     | 本页面依赖的一些基本的 javascript 公共脚本文件 |
| config.js    |  js   |  配置中心，比如后台服务器地址就是在这里进行配置 | 
| xzb.js        |  js | 核心 javascript 文件，直播观看和 IM 聊天室的实现逻辑，都位于此 js 中。 |
| xiaozhibo.html| 根目录 | 唯一的 html 页面，其中的 PlayerContainer 为视频渲染区域，其上紧贴着的 div 是聊天区域。|

#### 3.1 配置config.js

| 配置项 | 含义 | 参考文档 |
|:-------: |:--------------|:----------:|
| SERVER | 为该网页提供视频播放信息的业务服务器。 | [DOC](https://cloud.tencent.com/document/product/454/8046#step4.3A-web.E5.90.8E.E5.8F.B0.E6.90.AD.E5.BB.BA) |
| accountMode | IM SDK 的账号集成模式（配置要跟小直播中保持一致）。 | [DOC](https://cloud.tencent.com/document/product/454/7980) | 
| sdkAppID | IM 服务开通后分配的一个id，如果分享URL的参数中携带可以不配置。 | [DOC](https://cloud.tencent.com/document/product/454/7953#3.2-im-sdk-appid) |
| accountType |  IM 服务开通后分配的一个type，如果分享URL的参数中携带可以不配置。 | [DOC](https://cloud.tencent.com/document/product/454/7953#3.3-im-sdk-.E8.B4.A6.E5.8F.B7.E7.B1.BB.E5.9E.8B) |

#### 3.2 调试&部署页面
- 如果您要调试，要注意直接 <font color='red'>在 Windows 下用浏览器打开 xiaozhibo.html 是不行的</font>，需要将其上传到一台可访问的服务器上进行调试，如果您没有自己的服务器，可以参照源码包里的 readme.pdf 部署一台。
 
- 静态网页的部署推荐使用[CDN 内容分发网络](https://cloud.tencent.com/product/cdn)，CDN 的优势就是能极大的缩减用户打开页面的速度，从而提升用户体验。

### Step4: Web后台搭建
这部分工作可以交给贵团队的**后端工程师**处理，主要工作就是在您的业务服务器上提供一个 **信息查询接口：**。

因为 Step3 中的 Web 页面是静态的，但是每个直播的信息都不一样，比如主播是谁？主播的头像是什么？房间的标题是什么？甚至，有没有录播的回放录像？

这些信息就需要 Web 页面中的 xzb.js 通过 ajax 异步请求到您的业务后台服务器查询。我们在小直播中，将这一查询协议定义为 [GetUserInfo](https://cloud.tencent.com/document/product/454/7895#9..E8.8E.B7.E5.8F.96.E6.8C.87.E5.AE.9A.E4.B8.BB.E6.92.AD.E7.9A.84.E8.AF.A6.E7.BB.86.E4.BF.A1.E6.81.AF)。

小直播源码集中包含 PHP 后台服务器 [DEMO源码](https://cloud.tencent.com/document/product/454/6991) ，其中 GetUserInfo.php 中提供了对 GetUserInfo 协议的实现。

### Step5: 页面做了什么
完成 Step4 之后基本已经搞定了本文档所言功能的对接，但到这里您的感觉可能是：
> “按照你的步骤做完了，但好像整个系统就是个黑盒子，它里面原理是什么？”

接下来我们从**分享URL的构成**和**网页的内部原理**两个方面来介绍其内部的原理：


#### 5.1 分享URL的构成

<table class="t" style="text-align: center; width:750px">
<tbody>
<tr><td>
http://imgcache.qq.com/open/qcloud/video/share/xiaozhibo.html?sdkappid=1400012345&acctype=8888&userid=test1234&type=0
</td></tr>
</tbody></table>

这个 URL 的主体是一个叫做 xiaozhibo 的 html 页面，它被放置于 imgcache.qq.com 域名上，该域名是腾讯云的静态CDN 地址。

> html 的名字以及服务器的域名您都可以根据自己的情况部署，但我们很推荐您将网页部署到腾讯云的静态 CDN 上，因为它可以让您的用户不论是在北京还是在青海，都能从最近的服务器拉取到该文件。

接下来，xiaozhibo.html 后面跟了一组参数，这组参数用来告诉 Web 页面： 应该进哪个聊天室？ 应该播哪个视频URL？主播叫什么？头像是什么样子？视频究竟是直播还是点播？

| 参数名 | 含义 | 备注 |
|---------|---------|---------|
| sdkappi | IM 服务开通后分配的一个id，用来进入聊天室的必备信息。 | [参考文档](https://cloud.tencent.com/document/product/454/7953#3.2-im-sdk-appid) |
| acctype |  IM 服务开通后分配的一个type，跟 sdkappi 配合使用。 | [参考文档](https://cloud.tencent.com/document/product/454/7953#3.3-im-sdk-.E8.B4.A6.E5.8F.B7.E7.B1.BB.E5.9E.8B) |
| userid | 主播的 userid | 在小直播里，主播 id 即为房间号 |
| type | 视频类型 | 0 - 代表直播， 1 - 代表点播，也就是录像回放 | 

#### 5.2 网页的内部原理

xiaozhibo.html 中挂载的 xzb.js 是网页的主控 javascript 文件，也就是驱动整个页面的逻辑中枢，它以如下的步骤去实现整个页面的功能：
- **主函数**
init() 为全局主入口函数，它串联起整个页面的全部逻辑链条：initParams() -> initLogin() -> initPlayer() -> ...

- **解析URL中的参数** 
initParams() 函数负责将 URL 尾部的 userid 等参数解析出来，initParams() 的最后一个动作是去 config.js 中 SERVER 配置项所指定的服务器地址上，用 userid 作为参数查询播放URL。

- **创建播放器**
initPlayer() 函数会根据当前是 PC 浏览器还是手机浏览器，选择相应的方式创建播放器。

- **视频播放**
loadVideo() 负责驱动网页中的播放器播放视频URL，需要您注意的是，大部分手机浏览器是限制视频的自动播放的（可能设计者考虑流量的问题），所以如果您发现同样的页面在不同手机上的自动播放表现不一致，这并不是什么奇怪的事情。

- **登录到聊天室**
initLogin() 通过从 URL 中解析的 sdkappid 和 acctype 等参数（如果 URL 中不懈怠则直接使用 config.js 中配置的 sdkappid 和 acctype），登录到聊天室中（Web 页面不具备创建聊天室的能力，所以成功进入的前提是主播在小直播 App 端已经创建了聊天室）。

## 常见问题
### 1. 微信拦截
不管直播还是点播都会有一个播放URL，需要把播放地址的域名添加到安全域名的列表里，不添加会有可能被微信以"非微信官方网页"为由拦截视频地址，导致不能播放视频。

登录微信公众平台进入“公众号设置”的“功能设置”里添加“JS接口安全域名”。设置域名后，该域名的网页内容不会被重新排版或者被拦截，但依然要遵守微信平台运营规则，否则依然会受到相应处罚。

[怎么去掉“非微信官方网页，将由微信转换为手机预览模式”的提示页面？](https://www.zhihu.com/question/45748989)

### 2. Flash 跨域
PC 浏览器要依靠 Flash 控件完成视频播放，但 Flash 本身有跨域问题，如果你的网页以及 Step4 中的后台服务器不是部署在腾讯云的，需要在服务器的根目录下添加跨域配置文件 crossdomain.xml ：

```xml
<?xml version="1.0"?>
<cross-domain-policy>
		<allow-access-from domain="*" secure="false"/>
</cross-domain-policy>
```



