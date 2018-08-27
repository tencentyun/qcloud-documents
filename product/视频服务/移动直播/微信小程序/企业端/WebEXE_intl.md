
<h2> Solutions </h2>

WebEXE and WebRTC are the two access solutions for enterprises. The following table lists the application scenarios and advantages/disadvantages of these two solutions. You can choose accordingly based on your own needs.

| Solution | WebEXE | WebRTC |
|:-------:|:-------:|:-------:|
| URL for documentation |  [DOC](https://cloud.tencent.com/document/product/454/17004) | [DOC](https://cloud.tencent.com/document/product/454/17005) |
| Application scenario | To B (company employees) | To C (individual customers) |
| Advantage | Some advanced features can be implemented regardless of restrictions in browsers | It can be directly implemented in Chrome browser without the need to install plug-ins, which is suitable for ordinary users |
| Disadvantage | You need to install the program as prompted | Features are subject to the secure limits of Chrome browser |
| Beauty filter | Supported | Not supported |
| Desktop screencap | Supported | A screencap plug-in needs to be installed |
| Local recording | Supported | Not supported |
| Dependent cloud service | [LVB](https://cloud.tencent.com/product/LVB) + [IM](https://cloud.tencent.com/product/im) | [TRTC](https://cloud.tencent.com/product/trtc) + [IM](https://cloud.tencent.com/product/im) |

## Viewing Demo

Open the [experience URL](http://img.qcloud.com/open/qcloud/video/act/liteavWeb/avsolution/Index.html) in a browser to get started with the WebEXE solution. The website on the left side can be replaced with your own Web page, and the TXCloudRoom.exe on the right side can be used to implement video chat and other features.

- **Web page (Web)**: Hosts the original business system and business logics, such as order system, CRM system, and other electronic stream systems.
- **Desktop application (EXE)**: Applications like WeChat for PC, which can be directly triggered by your Web page. Featuring high performance and good stability, it can implement features that cannot be implemented on some browsers.

![](https://main.qcloudimg.com/raw/30a729f3fc5825c107a342a53ad7b938.png)

## Source Code Debugging

### PC Web page
Click [GitHub](https://github.com/TencentVideoCloudMLVBDev/webexe_web_source) to download the source code for Web page. Double click index.html in a local browser to use and debug the appropriate features of WebEXE. When using it for the first time, you will be prompted to download and install local client plug-ins.

| Directory | Description |
|:-------:|---------|
|  index.html  | Home page of demo |
| doubleroom.html  | Demo page of one-on-one video chat |
|  liveroom.html  | Demo page of interactive video chat |
|  assets | CSS style sheet and resource file used in demo page |
| js |  The javascript used in demo page, where EXEStart.js is located. |
| exe | TXCloudRoomSetup.exe installation package is included |

### Server
Click [GitHub](https://github.com/TencentVideoCloudMLVBDev/roomlist_server_java )  to download server-end source code of **Java** version. This code is mainly used to implement a simple (unauthenticated) room list, to support features such as creating or closing a chat room. This code can be ignored if you just want to enable a video call (hard-code a roomid in PC Web page and Mini Program end respectively). 

| Directory | Description |
|:-------:|---------|
| README.pdf | Describes how to use this backend code |
| Backend API table.pdf | Provides a detailed description on how to implement this backend code internally |
| src | Backend room list source code of java version |


## Solution Integration
The following figure describes how to integrate WebEXE solution to your existing business system:
![](https://main.qcloudimg.com/raw/c89609dcfa5388a7a3d4d00d5d7f94cc.png)

### Step 1: Build a business server
The business server is mainly used to send roomid, userid, usersig and other information required to implement a video chat to PC Web pages and WeChat mini programs. The roomid and userid can be specified by your business backend. You must ensure that these IDs cannot overlap with each other. For more information on how to calculate the usersig, please see [DOC](https://cloud.tencent.com/document/product/454/14548). We also provide the calculation [source code](https://cloud.tencent.com/document/product/454/7873#Server) of java and php versions.

### Step 2: Deploy RoomService
Both [LiveRoom (LVB+Joint broadcasting)](https://cloud.tencent.com/document/product/454/14606) and [RTCRoom (Video chat)](https://cloud.tencent.com/document/product/454/14617)  components used by WebEXE to implement a video chat rely on a backend open source component (JAVA | Node.js) called RoomService to implement room logics. Click [RoomService.zip](https://cloud.tencent.com/document/product/454/7873#Server)  to download the appropriate code. For more information on how to deploy the code, please see **README.pdf** in the zip package.

### Step 3: Integrate PC Web-end code
Your Web page needs to include the javascript file [**EXEStarter.js**](https://cloud.tencent.com/document/product/454/17006) , and sends the roomid, userid, usersig obtained in Step 1 to the **startEXE** function of [**EXEStarter.js**](https://cloud.tencent.com/document/product/454/17006). Some of the key parameters are described as follows:

| Parameter | Description |
| :----------: | ---------------------------------------- |
|  sdkAppID  | Tencent Cloud IM service uses sdkAppID to identify IM users. For more information on how to get this value, please see [DOC](https://cloud.tencent.com/document/product/454/7953#IM_SDKAPPID) . |
|  accType  | It was used to distinguish App types and is now saved for compatibility reasons. For more information on how to get this value, please see [DOC](https://cloud.tencent.com/document/product/454/7953#IM_ACCTYPE). |
|  userID  | User ID, which is assigned by your business server. Users will be forced offline in case of overlapped IDs. |
| userSig | Equivalent to the user password. For more information on how to calculate this value, please see [DOC](https://cloud.tencent.com/document/product/454/14548) . |
| serverDomain | RoomService address, which is obtained after the RoomService is deployed in Step 2. |
| roomId  | Room ID, which is assigned by your business server. Users can start a video chat if they join a room with the same ID either from mini program end or PC end. |
|   type  | RTCRoom and LiveRoom modes. Differences can be found in Step 4. |
|  template  | Layout of video windows. Default is 1V1. For more information, please see [Template](https://cloud.tencent.com/document/product/454/17006#EnumDef) . |
| mixRecord  | Cloud recording. In this mode, EXE does not participate in recording tasks which will be executed at the backend. Therefore, both WebEXE and WebRTC are applicable. However, customization is not supported. |
| screenRecord | Local recording mode specific to WebEXE. EXE program directly captures screen images locally and generates a recorded video in real time. Depending on different parameters, EXE will store the generated video files locally or push them onto the cloud. | |
|    cloudRecordUrl | If you choose RecordScreenToServer or RecordScreenToBoth for screenRecord, you need to specify a rtmp:// push URL. In this case, the video stream can record the video content to the cloud according to the standard push and recording modes. |

 [**EXEStarter.js**](https://cloud.tencent.com/document/product/454/17006)  is mainly used to trigger the TXCloudRoom.exe desktop program and implement a two-way communication with TXCloudRoom.exe. Your Web page only needs to process room management logics, and TXCloudRoom.exe handles complicated audio/video features.

Click [sample code](https://cloud.tencent.com/document/product/454/17006#Code), and you can find a program used to trigger TXCloudRoom.exe. You can also obtain well-designed source code applicable to PC Web page from [GitHub](https://github.com/TencentVideoCloudMLVBDev/webexe_web_source).

### Step 4: Integrate Mini Program-end code
For the integration of Mini Program-end code, please see documents about integration of WeChat-end code:

| Document URL | Application Scenario |
| ---------------------------------------- | ---------------------------------------- |
| [**&lt;rtc-room&gt;**](https://cloud.tencent.com/document/product/454/15364) | Scenarios of video chat only, such as one-on-one video chat, or video conference |
| [**&lt;live-room&gt;**](https://cloud.tencent.com/document/product/454/15368) | Combined scenarios of LVB+Joint broadcasting implemented based on LVB service, to allow thousands of viewers to watch LVB concurrently at a very low bandwidth cost and support real-time chat among VJs and viewers.

## How to Record LVB
You can record a user's entire LVB process as a video file for replay. For more information on how to implement the recording feature, please see [Record Entire LVB](https://cloud.tencent.com/document/product/454/17026)..

<video src="
http://1252463788.vod2.myqcloud.com/e12fcc4dvodgzp1252463788/c490bab57447398155981625642/TwA4JteAe40A.mp4" controls="controls">
Your browser does not support video tags.
</video>

## NAT Traversal
Many enterprises have a secure gateway to block Internet access of enterprise internal network. But all Tencent Cloud solutions are accessed over the Internet. To solve this problem, a proxy server is required. For more information on how to solve this problem, please see [DOC](https://cloud.tencent.com/document/product/454/17139) .

![](https://main.qcloudimg.com/raw/0411610edea069af3fefbcbb09464bf1.png)




