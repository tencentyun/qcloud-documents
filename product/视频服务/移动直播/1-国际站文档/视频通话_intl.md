## Feature Description
RTCRoom is a video chat solution that is used for real-time video chats between two or more people. It is applied in such scenarios as online customer service, remote loss assessment, remote account opening and online court hearing. This solution is implemented in several versions on various platforms including iOS, Android, mini programs and Windows, and supports interoperability between platforms.

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/00bb03cae1a3e448320b970fe4bbc450.png" />

## RTCRoom

RTCRoom involves a Client and a Server.

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/c6ab9b4d88f8948675921c7e19169672.png" />

- **Client (Terminal)**
RTCRoom's terminal component is available at an open source basis. It encapsulates Tencent Video Cloud LiteAVSDK (used for audio/video and includes TXLivePusher and TXLivePlayer APIs) and LiteIMSDK (used for sending and receiving messages and includes TIMManager and TIMConversation APIs).

 You don't need to use LiteAVSDK and LiteIMSDK, which are underlying SDKs. You can implement the video chat feature by simply using RTCRoom's createRoom, enterRoom, leaveRoom and other APIs.
 
 At the same time, RTCRoom relies on a backend service for room management and status coordination, as described below.

- **Server (Backend)**
RoomService is RTCRoom's backend component, which is also open-source. Its code logic fulfills two purposes: the first is to manage rooms (add, delete, modify or query rooms) and viewers (maintain the room members who are in the process of a video chat); the second is to control Tencent-RTC and IM services (by calling Tencent Cloud's backend REST APIs).

 You can deploy the provided source code to your business backend, or use the free RoomService service offered by Tencent Cloud.

<h2 id="Client">Interfacing with terminal</h2>

#### Step 1: Download the SDK for your platform.

| Platform | Programming Language | SDK Download | API Documentation | 
|:-------:|:-------:| :-------:| :-------:|
| iOS | Objective-C | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#iOS) | [API documentation](https://cloud.tencent.com/document/product/454/15156) | 
| Android | java | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Android) | [API documentation](https://cloud.tencent.com/document/product/454/15026) | 
| WeChat Mini Program | javascript | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#XiaoChengXu) | [API documentation](https://cloud.tencent.com/document/product/454/15364) | 
| IE browser | javascript | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Windows) | [API documentation](https://cloud.tencent.com/document/product/454/14766) | 
| Windows (C++) | C++ | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Windows) | [API documentation](https://cloud.tencent.com/document/product/454/14745) | 
| Windows (C#) | C# | [DOWNLOAD](https://cloud.tencent.com/document/product/454/7873#Windows) | [API documentation](https://cloud.tencent.com/document/product/454/13641) | 

-  LiteAV SDK in the decompressed SDK folder is used to implement audio/video related features.
-  LiteIM SDK in the decompressed SDK folder is used to implement IM related features.
-  RTCRoom in the decompressed Demo\rtcroom folder is provided at an open source basis to make it easier for debugging and customization as needed.

<h4 id="CLIENT_LOGIN">Step 2: Log in to RoomService (login)</h4>

RTCRoom cannot run by relying on the terminal component alone. It also needs a backend service, which is called **RoomService**, to manage rooms and coordinate status. **Login** is required for RTCRoom to use RoomService.

See [RoomService](#Server) to learn how to enter the parameters of the login function.

#### Step 3: Get room list
You can get a room list by calling the API **getRoomList** of RTCRoom. Each room in the list has its roomInfo, which is input when createRoom is called. It is recommended to define roomInfo in JSON format for a high scalability.

> Skip this step if you want to use your own room list. But you need to specify roomID in Step 4, and the roomID must be unique.
	
#### Step 4: Create a room
Enable local camera preview by calling the API **startLocalPreview** of RTCRoom. A "view" object needs to be specified to display the video images from the camera. During this period, RTCRoom requests the authorization to use camera and VJ can adjust the beauty filter and whitening effects by facing the camera.

Then, a room is created in the room list at backend by calling the API **createRoom** of RTCRoom, and the creator of the room goes into the push mode.

> **Parameter RoomID**
> 
> If you do not enter the roomId when calling createRoom, a roomID will be automatically assigned to you at backend via the callback API of createRoom. If you want to manage the room list on your own, the roomID can be assigned by your server. You only need to enter the assigned roomID when calling createRoom.

#### Step 5: Join a room
You can join a room identified by roomID by calling the API **enterRoom** of RTCRoom. If there are already members in the room, **onGetPusherList** of RoomListenerCallback returns a list of existing room members (pusherInfoList).

Next, by calling the API **addRemoteView** and specifying the pusherInfo and the "view" object, the remote image specified by the pusherInfo can be displayed on the specified "view".

When you are in the room, RoomListenerCallback notifies you of members who join or leave the room using **onPusherJoin** and **onPusherQuit**.

#### Step 6: Receive/send text messages
LiveRoom comes with APIs for sending messages. You can send text messages via the API **sendRoomTextMsg**, or send custom messages (such as URLs of images) via the API **sendRoomCustomMsg**.

You can receive text and custom messages sent from others in the chatroom via **onRecvRoomTextMsg** and **onRecvRoomCustomMsg** in RoomListenerCallback.

<h2 id="Server">Interfacing with backend</h2>

**Why is login required for RTCRoom?** 

RTCRoom cannot run by relying on the terminal component alone. It also needs a backend service, which is called **RoomService**, to manage rooms and coordinate status. **Login** is required for RTCRoom to use RoomService.

**How do I enter parameters related to login?**

The parameters should be entered based on application scenarios, as shown below. Solution 1 is intended for debugging, solution 2 for quick go-live, and solution 3 for customization.

| Parameter Name | Solution 1 (for Testing Only) | Solution 2 (Tencent Cloud RoomService) | Solution 3 (User-deployed RoomService) |
| :-------:| :-------:| :-------: | :-------:|
| serverDomain | Tencent Cloud RoomService<br> `https://room.qcloud.com/weapp`<br>`/rtc_room` | Tencent Cloud RoomService<br> `https://room.qcloud.com/weapp`<br>`/rtc_room`([Configuration](#TencentRoom) is needed in advance) | [User-deployed](#SelfRoom) RoomService<br> `https://[yourcompany]/weapp`<br>`/rtc_room` |
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
Enter `https://room.qcloud.com/weapp/rtc_room` as the serverDomain.

#### Step 2: Get parameters required for login
Get relevant parameters from the testing URL (`https://room.qcloud.com/weapp/utils/get_login_info_debug`).


<h3 id="TencentRoom"> Solution 2: Use Tencent Cloud RoomService </h3>

This solution uses your Tencent Cloud account and Tencent Cloud RoomService. You need to configure RoomService before implementing this solution.

 ![](https://mc.qcloudimg.com/static/img/32d0a7583f62eb51a2dc0290f8c23afd/image.png)

#### Step 1: Configure RoomService
The URL of Tencent Cloud RoomService is:

``` 
https://room.qcloud.com/weapp/rtc_room 
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
Download RoomService backend source code from [CODE](https://cloud.tencent.com/document/product/454/7873#Server). The source code package is composed of three directories, among which rtc_room contains the source code you need.

> Only the source code in node.js is available now. The source code in php and java is still under development. Please visit our official website regularly to learn about the latest updates.

After downloading the source code, decompress the package, locate the file config.js under the folder rtc_room, and then modify some configuration items. The configuration items are similar to those in Solution 1, except that you can modify local source code directly without using the configuration tool for RoomService. You can configure them by referring to Step 1 in Solution 1.

![](https://main.qcloudimg.com/raw/74512dcd5d06edac59b4d051da94e75f.png)

| Configuration Item | Description | Obtained From |
|---------|---------|:-------:|
| LVB pushSecretKey | Required for calculating the hotlink protection signature of a push URL | [DOC](https://cloud.tencent.com/document/product/454/7953#LVB_PUSH_SECRECT) |
| LVB APIKey | Used for security protection when backend REST APIs of Tencent Cloud LVB are called | [DOC](https://cloud.tencent.com/document/product/454/7953#LVB_API_SECRECT) |

Then, you can deploy RoomService on your backend server and notify your terminal development engineer of the public network URL of your server, so that he/she can specify the backend URL for RoomService when calling the parameter [login](#CLIENT_LOGIN) on terminal. For example:

``` 
https://[www.yourcompany.com]/weapp/rtc_room 
```

#### Step 2: Get parameters required for login
After Step 1, you have created your RoomService, which also authenticates user identity based on `sdkAppID, accType, userID and userSig` (or another authentication method you desire). Similarly, you need to assign a login signature to Client as described in [Generating UserSig](https://cloud.tencent.com/document/product/454/14548).

> In the backend source code of RoomService, the function getSig in `logic\im_mgr.js` generates the UserSig in the sample code in node.js. The sample code in Java and PHP will be available soon.

