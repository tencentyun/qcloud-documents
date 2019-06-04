## Feature Description
**LVB+Joint Broadcasting** is an LVB mode commonly used in the **Live Show** and **Online Education** scenarios. With a good applicability to many scenarios, it supports online live broadcasting featuring both high concurrency and low cost, but also enables video chats between VJs and viewers via joint broadcasting.

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/aacdf8cdfa825f64f34af9c3c3e4154e.jpg" />

## LiveRoom

If you only need a simple LVB solution that allows VJs broadcasting, viewers watching the broadcasting, and text interaction, please see [Single-session LVB](https://cloud.tencent.com/document/product/454/14551) or [Free-run LVB](https://cloud.tencent.com/document/product/454/7916).

However, if you want to go with joint broadcasting, it's not easy to implement it by only using TXLivePusher and TXLivePlayer. To solve this problem, **LiveRoom**, a component consisting of Client and Server, is provided:

- **Client (Terminal)**
LiveRoom component on Client encapsulates Tencent Video Cloud LiteAVSDK (used for audio/video and includes TXLivePusher and TXLivePlayer APIs) and LiteIMSDK (used for sending and receiving messages and includes TIMManager and TIMConversation APIs). It takes too much time and effort to perform LVB and joint broadcasting by directly using LiteAVSDK and LiteIMSDK. LiveRoom makes it very easy for you to use LVB and joint broadcasting by calling createRoom, enterRoom, and leaveRoom.
 
- **Server (Backend)**
RoomService is LiveRoom's background component. It has two responsibilities: The first is to manage rooms (add, delete, modify or query rooms) and viewers (especially when a joint broadcasting with VJ involves multiple viewers); the second is to control the Tencent Cloud LVB, Tencent-RTC and IM services (by calling Tencent Cloud backend REST APIs).

![](https://mc.qcloudimg.com/static/img/5a153aa265f6b41dbd88126d786c47e7/image.png)


<h2 id="Client">Interfacing with terminal</h2>

#### Step 1: Download the SDK for your platform.

| Platform | Programming Language | SDK Download | API Documentation | 
|:-------:|:-------:| :-------:| :-------:|
| iOS | Objective-C | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#iOS) | [API documentation](https://cloud.tencent.com/document/product/454/14730) | 
| Android | java | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Android) | [API documentation](https://cloud.tencent.com/document/product/454/14642) | 
| IE browser | javascript | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Windows) | [API documentation](https://cloud.tencent.com/document/product/454/14766) | 
| PC(C++) | C++ | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Windows) | [API documentation](https://cloud.tencent.com/document/product/454/14745) | 

-  LiteAV SDK in the decompressed SDK folder is used to implement audio/video related features.
-  LiteIM SDK in the decompressed SDK folder is used to implement IM related features.
-  LiveRoom in the decompressed Demo\liveroom folder provides open source code to make it easy for you to debug and customize as needed.


<h4 id="CLIENT_LOGIN">Step 2: Log in to RoomService (login)</h4>
LiveRoom cannot run by relying on the component on Client alone. It also needs a background service, which is called **RoomService**, to manage rooms and coordinate status. To use RoomService, LiveRoom must **log in** to RoomService.

See [RoomService](#Server) to learn how to enter the parameters of the login function.

#### Step 3: Get room lists (getRoomList)
Both VJs and viewers (teachers and students) need room lists. You can get room lists by calling **getRoomList** in LiveRoom. Each room in a list has roomInfo. When you create a room, it is recommended that you define roomInfo in JSON format for high scalability.

> Skip this step if you want to use your own room list. But you need to specify roomID in Step 4, and the roomID must be unique.

#### Step 4: VJs start broadcasting (createRoom)
To start broadcasting, call the API **startLocalPreview** in LiveRoom to enable local camera preview. A "view" object needs to be specified to display video images in the camera. During the period, LiveRoom requests camera permissions and VJs look at cameras to adjust beautifying and whitening effects.

Then, a room is created in the room list in the background by calling the API **createRoom** of LiveRoom, and the VJ goes into the push mode.

> **Parameter roomID**
> If you do not enter the roomId when calling createRoom, a roomID will be automatically assigned to you at backend via the callback API of createRoom. If you want to manage the room list on your own, the roomID can be assigned by your server. You only need to enter the assigned roomID when calling createRoom.

#### Step 5: View LVB (enterRoom)
Viewers can enter live rooms and view LVB via **enterRoom** in LiveRoom. A "view" object needs to be specified for enterRoom to display video images in the LVB stream.

Besides, after viewers enter a room, you can get the list of viewers by calling **getAudienceList** in LiveRoom. The list may not contain all the viewers. If the number of viewers is less than 30, all of them will display in the list. Otherwise, the last 30 viewers will display in the list. (For the sake of performance, at most 10 profile photos can display in the screen.)

#### Step 6: Joint broadcasting (joinPusher)
Joint broadcasting is a process that requires the participation of both a VJ and viewers, as shown below:
![](https://mc.qcloudimg.com/static/img/52c2eaa6d4ade76fbc71d81e479fd50c/image.jpg)

- 1 (viewer): Initiates a request for joint broadcasting through **requestJoinPusher**.

- 2 (VJ): Receives the callback notification from **onRecvJoinPusherRequest**. A prompt asking whether the VJ to accept the request appears.

- 3 (VJ): Selects **acceptJoinPusher** to accept or **rejectJoinPusher** to reject the request.

- 4 (viewer): Learns whether his request is accepted or not through **RequestJoinPusherCallback**.

- 5 (viewer): Enables his local camera by calling **startLocalPreview** if his request is accepted. The SDK applies permissions for the viewer's camera and microphone as startLocalPreview needs a view object to display the image of the camera.

- 6 (viewer): Goes into the joint broadcasting mode (push on viewer side) by calling **joinPusher**.

- 7 (VJ): Once the viewer is ready for joint broadcasting, the VJ receives a notification of **onPusherJoin**, which encapsulates the viewer's information into the "pusherInfo" object. Next, the VJ displays the remote image of the viewer on the screen through the **addRemoteView** function.

- 8 (viewer): If one or more viewers are under joint broadcasting, the viewer end will also receive the onPusherJoin notification, and the images of other viewers will display on the screen via addRemoteView.

> You can ignore the last step if you want a 1v1 joint broadcasting.

#### Step 7: On-screen comment (sendMsg)
LiveRoom provides message delivery APIs. You can send ordinary text messages (on-screen comments) via **sendRoomTextMsg** and custom messages (such as giving a like, or sending a flower) via **sendRoomCustomMsg**.

You can receive text and custom messages sent from others in the chatroom via **onRecvRoomTextMsg** and **onRecvRoomCustomMsg** in RoomListenerCallback.

> ** <font color='red'> ATTENTION </font> **
> 
> You can receive at most 40 messages in one second via Tencent Cloud IM. If you refresh all of them to the screen based on the receipt frequency, LVB stuttering will occur. Mind the refresh frequency.
>
> That is the reason why some customers gain very smooth experience in trial but suffer serious stuttering after release.

<h2 id="Server">Interfacing with backend</h2>

**Why need to log in to LiveRoom?** 

LiveRoom cannot run by relying on the component on Client alone. It also needs a background service, which is called **RoomService**, to manage rooms and coordinate status. To use RoomService, LiveRoom must **log in** to RoomService.

**How do I enter parameters related to login?**

The parameters should be entered based on application scenarios, as shown below. Solution 1 is intended for debugging, solution 2 for quick go-live, and solution 3 for customization.

| Parameter Name | Solution 1 (for Testing Only) | Solution 2 (Tencent Cloud RoomService) | Solution 3 (User-deployed RoomService) |
| :-------:| :-------:| :-------: | :-------:|
| serverDomain | Use Tencent Cloud RoomService<br> `https://room.qcloud.com/weapp`<br>`/live_room` | [Configure](#TencentRoom) in advance before using Tencent Cloud RoomService<br> `https://room.qcloud.com/weapp`<br>`/live_room` | [Self-deployed](#SelfRoom) RoomService<br> `https://[yourcompany]/weapp`<br>`/live_room` |
| sdkAppID | Obtained from the testing URL <br>`https://room.qcloud.com/weapp`<br>`/utils/get_login_info_debug` | User-defined. [How to obtain it?](https://cloud.tencent.com/document/product/454/7953#IM_SDKAPPID) | User-defined. [How to obtain it?](https://cloud.tencent.com/document/product/454/7953#IM_SDKAPPID) |
| accType | Obtained from the testing URL<br> `https://room.qcloud.com/weapp`<br>`/utils/get_login_info_debug` | User-defined. [How to obtain it?](https://cloud.tencent.com/document/product/454/7953#IM_ACCTYPE) | User-defined. [How to obtain it?](https://cloud.tencent.com/document/product/454/7953#IM_ACCTYPE) | 
| userID | Obtained from the testing URL<br> `https://room.qcloud.com/weapp`<br>`/utils/get_login_info_debug` | User-defined, such as 9527 | User-defined, such as 9527 | 
| userSig | Obtained from the testing URL <br> `https://room.qcloud.com/weapp`<br>`/utils/get_login_info_debug` | Generated by your server. [How to generate it?](https://cloud.tencent.com/document/product/454/14548) | Generated by your server. [How to generate it?](https://cloud.tencent.com/document/product/454/14548)| 
| **Account owner** | Tencent Cloud test account | Your account | Your account | 
| **Account limits** | Available from 10:00 to 22:00 | No limit. Customization is not supported. | No limit. Customization is supported. | 
| **Application scenarios** | Debugging by Terminal Development team before go-live | Early stage after go-live | Growth stage |

<h3 id="DebugRoom"> Solution 1: For testing only</h3>

This solution uses the test accounts provided by Tencent Cloud for debugging. These accounts are only available from 10:00 to 22:00 during the debugging period.

#### Step 1: Configure RoomService
For serverDomain, enter `https://room.qcloud.com/weapp/live_room`.

#### Step 2: Get parameters required for login
Get relevant parameters from the testing URL (`https://room.qcloud.com/weapp/utils/get_login_info_debug`).


<h3 id="TencentRoom"> Solution 2: Use Tencent Cloud RoomService </h3>

This solution uses your Tencent Cloud account and Tencent Cloud RoomService. You need to configure RoomService before implementing this solution.

 ![](https://mc.qcloudimg.com/static/img/32d0a7583f62eb51a2dc0290f8c23afd/image.png)

#### Step 1: Configure RoomService
The URL of Tencent Cloud RoomService is:

``` 
https://room.qcloud.com/weapp/live_room 
```

Click [RoomTool.zip](http://dldir1.qq.com/hudongzhibo/mlvb/RoomTool.zip) to download the backend configuration tool for Tencent Cloud RoomService. This tool is based on Node.js and can only be used when Node.js has been [installed](http://nodejs.cn/download/). The PDF and PPT files in the configuration tool package describe in detail how to configure the RoomService. The following provides an overview of the configuration items.

| Configuration Item | Description | Obtained From |
|---------|---------|---------|
| LVB appID | Identifies customers in Tencent Cloud LVB | [DOC](https://cloud.tencent.com/document/product/454/7953#LVB_APPID) |
| LVB APIKey | Used for security protection when backend REST APIs of Tencent Cloud LVB are called | [DOC](https://cloud.tencent.com/document/product/454/7953#LVB_API_SECRECT) |
| IM sdkAppID | Identifies IM customers in Tencent Cloud IM service | [DOC](https://cloud.tencent.com/document/product/454/7953#IM_SDKAPPID) |
| IM accountType | Used to identify App type and now is retained for compatibility. | [DOC](https://cloud.tencent.com/document/product/454/7953#IM_ACCTYPE) |
| IM administrator | Required for IM REST API in RoomService to send room's system messages. | [DOC](https://cloud.tencent.com/document/product/454/7953#IM_ADMIN) |
| IM privateKey | Used by RoomService to issue the administrator's usersig to call IM REST API to send room's system messages. | [DOC](https://cloud.tencent.com/document/product/454/7953#IM_PRIKEY) |
| IM publicKey | Used by RoomService to verify login user's identity. | [DOC](https://cloud.tencent.com/document/product/454/7953#IM_PRIKEY) |

#### Step 2: Get parameters required for login
RoomService can only be used when `login(serverDomain, sdkAppID, accType, userID, userSig)` is called successfully on terminal. The first four parameters can be hard-coded at Client, but UserSig must be issued by your backend server. If UserSig is calculated at Client, the signature keys need to be written in the terminal code, causing the risk of being hacked.

RoomService and IM use the same UserSig issued by your server, so a UserSig can be used to log in to both IM and RoomService. For more information on how to use it, please see [issuing UserSig](https://cloud.tencent.com/document/product/454/14548).

<h3 id="SelfRoom"> Solution 3: User-deployed RoomService</h3>

This solution uses your Tencent Cloud account and the RoomService you deploy, allowing you to modify and customize the internal logic as needed.

#### Step 1: Download source code, modify configuration, and deploy RoomService
Download RoomService backend source code from [CODE](https://cloud.tencent.com/document/product/454/7873#Server). The source code package is composed of three directories, among which live_room contains the source code you need.

After downloading the source code, decompress the package, locate the file config.js under the folder live_room, and then modify some configuration items. The configuration items are similar to those in Solution 1, except that you can modify local source code directly without using the configuration tool for RoomService. You can configure them by referring to Step 1 in Solution 1.

![](https://main.qcloudimg.com/raw/74512dcd5d06edac59b4d051da94e75f.png)

| Configuration Item | Description | Obtained From |
|---------|---------|:-------:|
| LVB pushSecretKey | Required for calculating the hotlink protection signature of a push URL | [DOC](https://cloud.tencent.com/document/product/454/7953#LVB_PUSH_SECRECT) |
| LVB APIKey | Used for security protection when backend REST APIs of Tencent Cloud LVB are called | [DOC](https://cloud.tencent.com/document/product/454/7953#LVB_API_SECRECT) |

Then, you can deploy RoomService on your backend server and notify your terminal development engineer of the public network URL of your server, so that he/she can specify the backend URL for RoomService when calling the parameter [login](#CLIENT_LOGIN) on terminal. For example:

``` 
https://[www.yourcompany.com]/weapp/live_room 
```

#### Step 2: Get parameters required for login
After Step 1, you have created your RoomService, which also authenticates user identity based on `sdkAppID, accType, userID and userSig` (or another authentication method you desire). Similarly, you need to assign a login signature to Client as described in [Generating UserSig](https://cloud.tencent.com/document/product/454/14548).

> In the backend source code of RoomService, the function getSig in `logic\im_mgr.js` generates the UserSig in the sample code in node.js. The sample code in Java and PHP will be available soon.



## How It Works
### 1. Two "paths"

Tencent Cloud uses two paths to implement LVB plus joint broadcasting. LVB is implemented using standard RTMP and FLV protocols over standard CDN, which allows as many viewers as possible to watch the live show with very low bandwidth costs. However, the latency is greater than 2 seconds. Joint broadcasting is implemented using UDP protocol over special Direct Connect. With a latency of around 500 ms, joint broadcasting allows at most 10 people to enable video chat simultaneously, with the cost of each push higher than that of ordinary LVB.

![](https://main.qcloudimg.com/raw/ca3441a2671fda6b336edf9921b4cd8a.png)


| Path | LVB Path | Joint Broadcasting Path |
| :--------------:  | :-----: | :-----------: | 
| Latency | >=2s | Around 500 ms |
| Underlying protocol | RTMP/HTTP-FLV | Private UDP protocol |
| Price/Fee | low | Each push higher than LVB |
| Maximum number of concurrent viewers | No upper limit | <=10 |
| TXLivePusher | SD, HD, and FHD are available for setVideoQuality | MAIN_PUBLISHER and SUB_PUBLISHER are available for setVideoQuality |
| TXLivePlayer      |  PLAY_TYPE_LIVE_FLV |  PLAY_TYPE_LIVE_RTMP_ACC |
| Playback URL | Ordinary FLV URLs | RTMP URLs with hotlink protection signatures |

 
### 2. Function principle
You can integrate LiveRoom without having to understand the function principle. If you are interested, the following figure provides a general picture on how it works.
![](https://main.qcloudimg.com/raw/f24eee40faab1d4ab54389b139d6c0fa.gif)



