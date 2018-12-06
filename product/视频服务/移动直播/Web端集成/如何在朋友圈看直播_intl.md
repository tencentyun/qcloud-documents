## Feature Overview
If the LVB content within your product looks very good, then propagation of APP alone will inevitably hinder the development of the product. You can solve this problem by relying on the web page sharing capability of social platforms (such as WeChat's Moments and Sina Weibo).

**Sharing content to WeChat's Moments** is the most popular and effective social propagation solution. Here we take WeChat sharing as an example to describe how to build a Web-based closed-loop experience for your product.

![](//mc.qcloudimg.com/static/img/00d2cbbce2b70639effcab3124a8db3b/image.jpg)

## Technical Difficulties
To realize LVB on the web page, just add a **video tag** to the page, which looks easy. But to make better user experience, many technical difficulties need to be overcome:
- **How do I make it compatible on Android browser?**
Just as Android system, Android browsers can be divided into various categories and their modes and standards are not unified. Often, an effect is OK on a mobile phone, but it may change completely on another one. Compatibility is a very time-consuming and experience-based issue.

- **How do I interact with VJ using text on a web page?**
The VJ performs LVB using APP while the audiences watch it on the web page. What is the point of watching without interaction? So we must solve the problem of interacting with the VJ on the web page.

- **How do I deal with the X5 browser kernel?**
On the Android system, web pages opened from WeChat or QQ are basically based on X5 kernel launched by QQ Browser. The X5 kernel has its own policies and rules for video playback. If you are not clear about them, you may face many problems.

- **How do I deal with PC browser kernel?**
Browsers on PC cannot natively support LVB stream. If the web page is opened on a PC, but you cannot watch the video, it may look unreasonable.

Next, we use the following interfacing solutions to help you solve the technical problems mentioned above.

## Interfacing
The overall technical architecture is shown as in the figure below:
![](//mc.qcloudimg.com/static/img/b76f4b3b1b1961d8a8d4d0ea4dc14ad2/image.png)

| Interfacing Step | Description | Guide |
|:----------:|-------------|:------------:|
| Step 1 | Before your LVB begins on your App, share the URL to the WeChat's Moments first. | [Share URL to WeChat](#step1.3A-.E5.BE.AE.E4.BF.A1.E5.88.86.E4.BA.ABurl) |
| Step 2 | The friends of the sharer see this sharing in Moments and click to open it. | [User opens the link](#step2.3A-.E7.94.A8.E6.88.B7.E6.89.93.E5.BC.80.E9.93.BE.E6.8E.A5) |
| Step 3 | WebView (browser) embedded in WeChat pulls Web pages (HTML+JS) from the static CDN server specified by the URL | [Web Page Production](#step3.3A-web.E9.A1.B5.E9.9D.A2.E5.88.B6.E4.BD.9C) |
| Step 4 | The JS (javascript) code in the web page gets the necessary display information from your business backend server via ajax asyn requests. | [Web Backend Building](#step4.3A-web.E5.90.8E.E5.8F.B0.E6.90.AD.E5.BB.BA) |
| Step 5 | The web page realizes LVB watching on the Web by combining Live Broadcasting (LVB), Video on-demand (VOD) and Instant Messaging (IM) services. | [Internal principle of the web page](#step5.3A-.E9.A1.B5.E9.9D.A2.E5.81.9A.E4.BA.86.E4.BB.80.E4.B9.88) |


### Step 1: Share URL to WeChat
In the source code of Mini LVB, we use the components of Umeng to achieve the sharing capabilities to Sina, WeChat, WeChat's Moments, QQ and Qzone by default for your quick reference:

<table class="t">
<tbody><tr>
<th width=150> Platform
</th><th width=450> Source Code Reference
</th><th width=150> Reference Document
</th></tr>
<tr>
<td style="text-align: center;"> iOS platform
</td><td> Search for "WechatTimeLine" in the "mini LVB" terminal source package.
</td><td style="text-align: center;"> <a href="http://dev.umeng.com/social/ios/quick-integration">Umeng sharing component</a>
</td></tr>
<tr>
<td style="text-align: center;"> Android platform
</td><td> Search for "ShareAction" in the "mini LVB" terminal source package.
</td><td style="text-align: center;"> <a href="http://dev.umeng.com/social/android/quick-integration">Umeng sharing component</a>
</td></tr>
</tbody></table>

What is the shared URL specifically? We will explain it in detail in [Internal principle of the web page](#step5.3A-.E9.A1.B5.E9.9D.A2.E5.81.9A.E4.BA.86.E4.BB.80.E4.B9.88).

### Step 2: Users open the link
This step is done by users, and we don't need to do anything, but there are a few points we need to tell you:
- **Security blocking**
Not all video addresses can be used for playback in WeChat. Precisely speaking, most URLs cannot be used for such playback. You must go to WeChat to apply for a security license. Otherwise, even if the web page can be opened, the video within it will not be loaded because WeChat has already blocked it before the stream media is loaded.

- **X5 kernel**
Since it is Tencent's affiliated product, the embedded web page of Android version WeChat is mostly opened using the X5 browser kernel (QQ browser kernel), but it may also be opened using the system's own browser. The X5 browser kernel supports common streaming media video protocols, especially HLS (m3u8) and MP4.

- **Safari kernel**
For iOS platform, only the Safari kernel can be used, but WeChat can control its embedded WebView control to implement some features that are not enabled by Safari browser provided by the iPhone by default, such as the automatic video playback. (However, this feature is only open to some domain names.)

### Step 3: Web page production
This part of work can be handled by your team's Web **frontend engineers**. Of course, creating a Web page that supports online LVB watching and chat room requires some experience. Here we provide you with some quick reference:

The mini LVB source code set contains the [DEMO Source Code](https://cloud.tencent.com/document/product/454/6991) of the Web sharing page, which implements such features as **LVB watching**, **text message** and **Like**.

| File Name | Folder | Feature Description |
|:-------: |:--------------:|-------------|
| mobile.css | css | The CSS style sheet file of the sample web page, which controls the appearance and form of the page, and can be freely modified and replaced. |
| pictures | img | The sample images used for the sample web page, which can be replaced and adjusted as needed. |
| json2.js | sdk | The basic JS library of IM, which is mainly used to provide a API related to web-based chat room. | 
| webim.js | sdk | The basic JS library of IM, which is mainly used to provide a API related to web-based chat room. |
| base.js | js | The basic JS library of IM, which is mainly used to provide a API related to web-based chat room. |
| lib.js | js | Some basic javascript public script files depended on by this page |
| config.js | js | Configuration center. For example, the backend server address is configured here | 
| xzb.js | js | The core javascript file. The implementation logic of LVB watching and IM chat room is located in this js. |
| xiaozhibo.html | Root directory | The only html page, where PlayerContainer is the video rendering area, and the div on it is the chat area. |

#### 3.1 Configure config.js

| Configuration Item | Description | Reference Document |
|:-------: |:--------------|:----------:|
| SERVER | A business server that provides video playback information for the web page. | [DOC](https://cloud.tencent.com/document/product/454/8046#step4.3A-web.E5.90.8E.E5.8F.B0.E6.90.AD.E5.BB.BA) |
| accountMode | Account integration mode of IM SDK (the configuration should be consistent with that of the mini LVB). | [DOC](https://cloud.tencent.com/document/product/454/7980) | 
| sdkAppID | An ID assigned after the IM service is activated. You do not need to configure it, if it is contained in the parameter of shared URL. | [DOC](https://cloud.tencent.com/document/product/454/7953#3.2-im-sdk-appid) |
| accountType | A type assigned after the IM service is activated. You do not need to configure it, if it is contained in the parameter of shared URL. | [DOC](https://cloud.tencent.com/document/product/454/7953#3.3-im-sdk-.E8.B4.A6.E5.8F.B7.E7.B1.BB.E5.9E.8B) |

#### 3.2 Debug & deploy page
- If you want to debug the page, note that you cannot directly <font color='red'>open xiaozhibo.html with a browser in Windows</font>. You need to upload it to an accessible server for debugging. If you do not have your own server, you can deploy one by following readme.pdf in the source package.
 
- For the deployment of static web pages, it is recommended to use [Content Delivery Network (CDN)](https://cloud.tencent.com/product/cdn). The advantage of CDN is that it can greatly reduce the time for users to open pages, resulting in better user experience.

### Step 4: Web backend building
This part of the work can be handled by your team's **backend engineers**. The main task is to provide a **information query API** on your business server:

The Web page in Step 3 is static, but the information of each LVB is different. For example, who is the VJ? What is the profile photo of the VJ? What is the title of the room? Even, are there recorded playback videos?

The information requires xzb.js in the Web page to query on your business backend server via an ajax async request. We defined this query protocol as [GetUserInfo](https://cloud.tencent.com/document/product/454/7895#9..E8.8E.B7.E5.8F.96.E6.8C.87.E5.AE.9A.E4.B8.BB.E6.92.AD.E7.9A.84.E8.AF.A6.E7.BB.86.E4.BF.A1.E6.81.AF) in mini LVB.

The mini LVB source code set contains the PHP backend server [DEMO source code](https://cloud.tencent.com/document/product/454/6991), where GetUserInfo.php provides the implementation of the GetUserInfo protocol.

### Step 5: Internal principle of the web page
After completing Step 4, you have basically completed the interfacing of the features described in this document, but here you may think:
> "The whole system completed by following the steps above just seems like a black box. What is the principle?"

Next, we introduce its internal principle from two aspects: **the composition of shared URL** and **the internal principle of web page**:


#### 5.1 The composition of shared URL

<table class="t" style="text-align: center; width:750px">
<tbody>
<tr><td>
http://imgcache.qq.com/open/qcloud/video/share/xiaozhibo.html?sdkappid=1400012345&acctype=8888&userid=test1234&type=0
</td></tr>
</tbody></table>

The main body of this URL is an html page called xiaozhibo. It is placed on the domain name imgcache.qq.com, which is the static CDN address of Tencent Cloud.

> The name of the html and the domain name of the server can be deployed according to your needs. But we recommend that you deploy the web page to the static CDN of Tencent Cloud, because it allows your users to pull this file from the nearest server no matter they are in Beijing or Qinghai.

Next, xiaozhibo.html is followed by a set of parameters that tell the Web page: Which is the chat room to be entered? Which video URL should be played? What is the name of the VJ? What is the profile photo? Is it a VOD or LVB?

| Parameter Name | Description | Remarks |
|---------|---------|---------|
| sdkappi | An ID assigned after the IM service is activated, which is required for you to enter the chat room. | [Reference Document](https://cloud.tencent.com/document/product/454/7953#3.2-im-sdk-appid) |
| acctype | A type assigned after the IM service is activated, which is used in conjunction with sdkappi. | [Reference Document](https://cloud.tencent.com/document/product/454/7953#3.3-im-sdk-.E8.B4.A6.E5.8F.B7.E7.B1.BB.E5.9E.8B) |
| userid | userid of VJ | In mini LVB, the VJ ID is the room number |
| type | Video type | 0 - LVB; 1 - VOD, that is, video playback | 

#### 5.2 The internal principle of the web page

The xzb.js file mounted in xiaozhibo.html is the main control javascript file of the web page, that is, the logic hub that drives the entire page. It implements the features of the entire page by following the steps below:
- **Main function**
init() is the global main entry function that concatenates all logic chains of the entire page: initParams() -> initLogin() -> initPlayer() -> ...

- **Resolve parameters in the URL** 
The initParams() function resolves parameters (such as userid) at the end of the URL. The last action of initParams() is to go to the server address specified in the SERVER configuration item in config.js, and query the playback URL with userid as the parameter.

- **Create a player**
The function initPlayer() selects the method to create a player based on the browser type (PC browser or mobile browser).

- **Video playback**
loadVideo() drives the player in the webpage to play the video URL. Note that most mobile browsers limit auto-play of videos (designers maybe consider the traffic problem). So it is normal if the auto-play of the same page on different phones is inconsistent.

- **Log in to the chat room**
initLogin() logs in to the chat room using parameters (such as sdkappid and acctype) resolved from the URL (if they are not contained in URL, use sdkappid and acctype configured in config.js directly). (Web pages do not have the capability to create chat rooms. Therefore, the VJ must have created a chat room on the mini LVB App before the chat room can be entered successfully.)

## FAQ
### 1. WeChat blocking
Regardless of LVB or VOD, there will be a playback URL, and the domain name of the playback address needs to be added to the list of secure domain names, otherwise the video address may be blocked by WeChat as a "non-WeChat official webpage", resulting in video playback failure.

Log in to the WeChat MP Platform and add "JS API Security Domain Name" in "Feature Settings" of "Official Account Settings". After the domain name is set, the web page content of the domain name will not be re-formatted or blocked, but WeChat platform operating rules must still be followed, otherwise penalties will applied accordingly.

[How do I remove the prompt page "Non-WeChat official web page. It will be converted to mobile preview mode"?](https://www.zhihu.com/question/45748989)

### 2. Flash cross-domain
PC browsers rely on Flash controls to complete the video playback, but Flash itself has cross-domain issues. If your web page and the backend server in Step 4 are not deployed in Tencent Cloud, you need to add the cross-domain configuration file crossdomain.xml in the root directory of the server:

```xml
<?xml version="1.0"?>
<cross-domain-policy>
		<allow-access-from domain="*" secure="false"/>
</cross-domain-policy>
```




