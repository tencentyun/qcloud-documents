## Overview
If your product has excellent LVB contents, propagating them only via App will inevitably limit the development pace of the product. A good solution is to use web page URL sharing feature of social platforms (such as WeChat Moments and Sina Weibo).

**WeChat Moments sharing** is the most popular and effective social propagation solution. This document describes how to build closed-loop experience for your product on the Web application with WeChat sharing as an example.

![](//mc.qcloudimg.com/static/img/00d2cbbce2b70639effcab3124a8db3b/image.jpg)

## Technical Difficulties
To watch LVB on a web page, you only need to add a **video tag** to the page, which seems easy. However, to achieve better user experience, you need to overcome many technical difficulties:
- **How to achieve good compatibility on Android browsers?**
Like Android systems, Android browsers differ with each other and use various systems and standards. The case that an effect is normal on one mobile phone but becomes abnormal on another one always occurs. Compatibility issues are time-consuming and dependent on experience.

- **How to interact with VJ through text messages on the web page?**
Imaging that a VJ is performing LVB on an App while viewers can watch on the web page but cannot interact with the VJ, it will be less interesting. Therefore, we have to solve the problem of interacting with the VJ on the web page.

- **How to deal with X5 browser kernel?**
On Android system, web pages that can be opened on WeChat or QQ are based on X5 kernel launched for QQ Browser. X5 kernel has its own strategies and rules in video playback. If you do not know them, you will face many troubles.

- **How to deal with PC browser kernel?**
All PC browsers cannot directly support LVB stream. If you open a web page on the PC but cannot watch the video, it will be embarrassing.

The following is interfacing guides for you to solve the above technical problems.

## Interfacing Guide
The overall technical architecture is shown below:
![](//mc.qcloudimg.com/static/img/b76f4b3b1b1961d8a8d4d0ea4dc14ad2/image.png)

|Interfacing steps | Step Instructions | Reference URL |
|:----------:|-------------|:------------:|
| Step 1 | Share the LVB URL to WeChat Moments before the LVB on your App starts.  | [Share URL to WeChat](#step1.3A-.E5.BE.AE.E4.BF.A1.E5.88.86.E4.BA.ABurl) |
| Step 2 | Friends of sharers see this shared URL, and click to open it.  |  [Users open the URL](#step2.3A-.E7.94.A8.E6.88.B7.E6.89.93.E5.BC.80.E9.93.BE.E6.8E.A5) |
| Step 3 | WebView (browser) embedded in WeChat pulls a web page (HTML+JS) from a static CDN server specified by the URL |[Make a web page](#step3.3A-web.E9.A1.B5.E9.9D.A2.E5.88.B6.E4.BD.9C) |
| Step 4 | JS (JavaScript) codes in the web page obtain the necessary display information from your business backend server through the Ajax async request method.  |  [Build the web background](#step4.3A-web.E5.90.8E.E5.8F.B0.E6.90.AD.E5.BB.BA) |
| Step 5 | The web page achieves LVB experience on the web application through the combination of LVB, VOD, IM and other services.  |  [What has the page done](#step5.3A-.E9.A1.B5.E9.9D.A2.E5.81.9A.E4.BA.86.E4.BB.80.E4.B9.88) |


### Step 1: Share URL to WeChat
In source codes of Mini LVB, we have achieved the feature of sharing to Sina Weibo, WeChat, WeChat Moments, QQ and Qzone by default by using the components provided by Umeng. You can directly refer to the codes:

<table class="t">
<tbody><tr>
<th width=150> Platform
</th><th width=450> Source Code Reference
</th><th width=150> References
</th></tr>
<tr>
<td style="text-align: center;"> iOS platform
</td><td> Search "WechatTimeLine" in the terminal source code package of Mini LVB.
</td><td style="text-align: center;"> <a href="http://dev.umeng.com/social/ios/quick-integration">Umeng sharing components</a>
</td></tr>
<tr>
<td style="text-align: center;"> Android platform
</td><td> Search "ShareAction" in the terminal source code package of Mini LVB.
</td><td style="text-align: center;"> <a href="http://dev.umeng.com/social/android/quick-integration">Umeng sharing components</a>
</td></tr>
</tbody></table>

We detail the shared URL in [What has the page done](#step5.3A-.E9.A1.B5.E9.9D.A2.E5.81.9A.E4.BA.86.E4.BB.80.E4.B9.88)

### Step 2: Users open the URL
This step is operated by users, so we just need to synchronize the following for you:
- **Security blocking**
Not all of video URLs can be played on the WeChat. Specifically, most URLs can not be played unless you have applied for security licenses in WeChat. Otherwise, even if you can open a web page, the video on it cannot load because WeChat blocks it before the streaming media load.

- **X5 kernel**
Since both WeChat and X5 kernel belong to Tencent, web pages embedded in WeChat for Android are usually opened via the X5 browser kernel (QQ browser kernel), but may also via the system browser. X5 browser kernel supports common streaming video protocols, especially HLS (M3U8) and MP4 protocols.

- **Safari kernel**
On the iOS platform, only Safari kernel can be used. However, WeChat can control WebView control embedded in the Safari to achieve some features that the Safari browser does not enable by default, such as auto video playback. However, this feature is available only to part of domain names.

### Step 3: Make a web page
This can be finished by web **frontend engineers** in your team. Certainly, it need some experience to create from scratch a web page that supports online LVB and features chat room. Therefore, we provide you with some quick reference as much as possible:

Source codes of Mini LVB contain [DEMO source codes](https://cloud.tencent.com/document/product/454/6991) for sharing web page, and achieve features such as **LVB**, **sending text messages** and **giving likes**.

| File Name | Folder | Feature Description |
|:-------: |:--------------:|-------------|
| mobile.css | css | CSS files of the exemplary page, which is used to control page appearance and shape, and can be freely modified and replaced.  |
| pictures | img | Exemplary pictures used on the exemplary page, which can be replaced and adjusted based on needs.  |
| json2.js     | sdk |  Basic JS library of IM, mainly used to provide APIs related to chat room on the Web application.  | 
| webim.js    | sdk | Basic JS library of IM, mainly used to provide APIs related to chat room on the Web application.  |
| base.js      |  js  | Basic JS library of IM, mainly used to provide APIs related to chat room on the Web application.  |
| lib.js          | js     |Some basic common JavaScript script files that this page depends on |
| config.js    |  js   |  Configuration center. For example, the backend server IP is configured here| 
| xzb.js        |  js | Core JavaScript files, where the implementation logic of LVB and IM chat room is located.  |
| xiaozhibo.html| Root directory | The only HTML page, in which the PlayerContainer means the video rendering area, and the div close to it means the chat area. |

#### 3.1 Configure config.js

| Configuration Item | Description | References |
|:-------: |:--------------|:----------:|
| SERVER | Business server that provides video playback information for this web page.  | [DOC](https://cloud.tencent.com/document/product/454/8046#step4.3A-web.E5.90.8E.E5.8F.B0.E6.90.AD.E5.BB.BA) |
| accountMode | Account integration mode of IM SDK. Its configuration should be consistent with that in Mini LVB.  | [DOC](https://cloud.tencent.com/document/product/454/7980) | 
| sdkAppID | An ID assigned after the IM service is activated, which requires no configuration if parameters in the shared URL contain the ID.  | [DOC](https://cloud.tencent.com/document/product/454/7953#3.2-im-sdk-appid) |
| accountType | A type assigned after the IM service is activated, which requires no configuration if parameters in the shared URL contain the type.  | [DOC](https://cloud.tencent.com/document/product/454/7953#3.3-im-sdk-.E8.B4.A6.E5.8F.B7.E7.B1.BB.E5.9E.8B) |

#### 3.2 Debug & deploy the page
- To debug the page, you should not open the xiaozhibo.html with a browser on Windows. Instead, upload it to an accessible server. If you have no server, deploy one by referring to the readme.pdf in the source code package.
 
- To deploy static web pages, it is recommended to use [CDN Delivery Network](https://cloud.tencent.com/product/cdn). CDN can help quickly open an page, enhancing user experience.

### Step 4: Build the web background
This can be finished by web **backend frontend engineers** in your team. The main job is to provide a **information query API** for your business server.

The web page in Step 3 is static, but information on each LVB is different. For example, who is the VJ? What is the profile photo of the VJ? What is the title of the room? Is there a recorded playback video?

These information needs to be queried in your business backend server by the xzb.js in the web page through the Ajax async request method. In Mini LVB, we define this query protocol as [GetUserInfo](https://cloud.tencent.com/document/product/454/7895#9..E8.8E.B7.E5.8F.96.E6.8C.87.E5.AE.9A.E4.B8.BB.E6.92.AD.E7.9A.84.E8.AF.A6.E7.BB.86.E4.BF.A1.E6.81.AF).

The source codes of Mini LVB contain [DEMO source codes](https://cloud.tencent.com/document/product/454/6991) of the PHP backend server, in which GetUserInfo protocol is achieved in GetUserInfo.php.

### Step 5: What has the page done
After Step 4, you have finished interfacing with features in this document, but you may wonder:
> "I finished according to the steps, but the whole system seems a black box. What 's the principle of it?"

The following introduces the principle from **the composition of the shared URL** ** and **the internal principle of web page**:


#### 5.1 The composition of the shared URL

<table class="t" style="text-align: center; width:750px">
<tbody>
<tr><td>
http://imgcache.qq.com/open/qcloud/video/share/xiaozhibo.html?sdkappid=1400012345&acctype=8888&userid=test1234&type=0
</td></tr>
</tbody></table>

In this URL, the subject is an HTML page named xiaozhibo and placed on the imgcache.qq.com domain name, which is a static CDN URL of Tencent Cloud.

> You can deploy HTML name and the server domain name based on your needs, but we recommend you to deploy the web page on Tencent Cloud's static CDN so that your users can pull the file from the server closest to them whether in Beijing or in Qinghai.

The parameters following xiaozhibo.html are used to tell the web page the chat room to be entered, the video URL to be played, the name and profile photo of the VJ, and the video type (LVB or VOD).

| Parameter Name | Description | Note |
|---------|---------|---------|
| sdkappi | ID assigned after IM service is activated, which is the necessary information to enter the chat room.  [References](https://cloud.tencent.com/document/product/454/7953#3.2-im-sdk-appid) |
| acctype | type assigned after the IM service is activated, which is used with sdkappi.  | [References](https://cloud.tencent.com/document/product/454/7953#3.3-im-sdk-.E8.B4.A6.E5.8F.B7.E7.B1.BB.E5.9E.8B) |
| userid | User ID of the VJ. In Mini LVB, the VJ ID is room ID |
| type | video type | 0 means LV; 1 means VOD, that is, playback video | 

#### 5.2 The internal principle of web page

The xzb.js mounted in xiaozhibo.html is the master JavaScript file, namely, the logical center to drive the whole page. It achieves features of the page through the following steps:
- **Main function**
The init () is the global main function, which connects all the logic chains of the whole page: initParams () -> initLogin () -> initPlayer () -> ...

- **Resolve the parameters in the URL** 
The initParams () function resolves parameters at the end of the URL, such as userid. Its last operation is to, by using userid as the parameter, query playback URL on the server IP specified by the SERVER configuration item in config.js.

- **Create a player**
The initPlayer () function chooses the appropriate way to create a player based on the browser type (PC browser or mobile browser).

- **Play the video**
The loadVideo () drives the player in the web page to play the video URL. Note that most mobile browsers limit auto video playback. This may because the designers consider the traffic consumption. Therefore, it is normal that the video on the same page may be played automatically or not on different mobile phones.

- **Log in to the chat room**
The initLogin () logs in to the chat room through sdkappid, acctype and other parameters resolved from the URL, or directly through sdkappid and acctype configured in config.js if the URL does not contain these parameters. To enter the chat room, the VJ must create a chat room in the Mini LVB App in advance because web pages cannot create a chat room.

## FAQs
### 1. WeChat blocking
Both LVB and VOD have a playback URL, whose domain name needs to be added to the security domain name list. Otherwise WeChat will block the URL because it is "not a WeChat-verified web page", causing video playback failure.

Log in to WeChat Official Account Admin Platform to enter the "Official Account Settings", and then add "JS API Security Domain Name" in "Feature Settings". After that, the contents in the web page with the domain name will not be re-laid out or be blocked, but still have to comply with operating rules of WeChat platform. Otherwise, WeChat will impose punishment.

[How to remove the notification that "This is not a WeChat-verified web page, and will be displayed in the phone preview mode"? ](https://www.zhihu.com/question/45748989)

### 2. Flash cross-domain problems
PC browsers need Flash controls to play videos, but Flash has cross-domain problems. Therefore, if your web page and the backend server in Step 4 are not deployed in Tencent Cloud, you need to add the cross-domain configuration file crossdomain.xml under the root directory of the server:

```xml
<?xml version="1.0"?>
<cross-domain-policy>
		<allow-access-from domain="*" secure="false"/>
</cross-domain-policy>
```




