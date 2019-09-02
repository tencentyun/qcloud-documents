## Solution Overview
The LVB Code solution is an **LVB channel management solution** different from channel hosting in the following aspects:

The [Channel Hosting](https://cloud.tencent.com/doc/api/258/5659) mode is applicable to LVB activities. You can complete operations such as creating channels, managing URLs, banning LVB streams and adding watermarks in the backend by clicking appropriate webpage entries in the [LVB Console](https://console.cloud.tencent.com/live).

In scenarios in which LVB channels need to be frequently created and managed, such as LVB Apps like Inke and Huajiao, this mode is rather obstructive. The channel needs to synchronize the VJ channel name, description, status, URL, and other information with the Tencent Cloud backend, and understands the internal security protection rules. For example, the maximum access count (x) every second is specified for backend APIs, or the channel that is not stopped cannot be deleted.

The **LVB Code solution** is more applicable to non-manual scenarios, which allows customers to fully control and manage LVB streams. In addition to lowering the interfacing difficulty, this solution is highly customizable:
(1)**The push and playback URLs can be customized**: Customers can define push or playback URLs by themselves without applying to Tencent Cloud. For example, most customers can push streams after obtaining push URLs using user account IDs.
(2) **This solution is more applicable to developing LVB Apps**: In the LVB Code solution, Tencent Cloud focuses on audio/video-related features such as push, transcoding, CDN delivery, recording, and security protection, and does not impose excessive limitation and intervention on the status, list, and URL. You can independently implement your business scenarios or use Tencent Cloud backend APIs to obtain channel information, with no need to conform to various limitation rules of Tencent Cloud backend. The solution is highly free and is applicable to complex LVB application scenarios such as LVB Apps.

![](//mccdn.qcloud.com/static/img/aa6cf00971df050b3b781b126064131f/image.png)

## Interfacing

It is very easy to deploy the LVB Code solution. You can have a super simple LVB backend by interfacing with the LVB Code solution as follows:

### 1. Enable the LVB Code mode
The initial access mode of Tencent Cloud LVB server is channel hosting. You need to manually switch to the LVB Code mode. For switching operations, please see [Service Activation](https://cloud.tencent.com/doc/api/258/6100).


### 2. Assign a push URL
A VJ needs to request a push URL from your backend server before starting push. The push URLs in the LVB Code mode shall conform to certain construction rules as follows:
![](//mc.qcloudimg.com/static/img/6ea8ebb159c57fc4ef934a5e57a55dcd/image.png)

- **BIZID**: 
8888 in the figure above is an example and indicates the BIZID assigned by Tencent Cloud. You can find BIZID at the top of the [LVB Console](https://console.cloud.tencent.com/live), as shown below:
![](//mc.qcloudimg.com/static/img/1400072859844bc1fa5dcf45bfa205c1/image.png)

- **LVB Code**:
8888_test_12345_test in the figure above is the LVB Code. It must be prefixed with **BIZID and an underline**, and the remaining can be freely specified as long as it does not conflict with the assigned LVB Code.

- **Hotlink protection signature**:
In the preceding figure, txTime indicates the URL expiration time while txSecret indicates the hotlink protection signature. The combination of the two can be used for security protection. For more information, please see [Security Protection](https://cloud.tencent.com/doc/api/258/5693).

- **Address generator**:
An address generator is provided on the console for you to test URLs since it is inconvenient to manually compute hotlink protection signatures:
![](//mc.qcloudimg.com/static/img/7e0b45fcf24595bfb31da3e3dbc8812e/image.png)

> **For other customers**
> Many customers use user account IDs as the LVB Code. For example, your BIZID on Tencent Cloud LVB platform is 2121, and a user's account is his/her phone number (such as 15919131751) because most of your users register with their mobile phone numbers. You can assign the following push URL to the user:
> 
>  `rtmp://2121.livepush.myqcloud.com/live/2121_15919131751?txSecret=aaa&txTime=bbb`


### 3. Manage the LVB list
You can maintain an LVB channel list as required. The following figure shows a recommended implementation solution:
![server](//mccdn.qcloud.com/static/img/56bb81fdbc4c5ab4cdea9448cbe3554c/image.png)

- **Step 1: Initiate an LVB** 
>When initiating an LVB, the App requests a push URL from the server. The generation of the push URL has been described above.
>
>The server adds a record to the LVB list when returning a push URL to the App. The most important information in the record is **LVB Code** and **user ID** (many customers directly use user IDs as their room IDs for easy management). You can also add **cover image address**, **number of likes**, **number of live viewers**, and other information to the list as required.

- **Step 2: End an LVB** 
>When the App ends an LVB, it also needs to notify the server. Then, the server can delete relevant records at the earliest possible time. Otherwise, the LVB list is full of offline VJ channels.

- **Step 3: Handle an emergency** 
> Unexpected incidents may occur. For example, the VJ App may crash or the traffic is used up. In this case, the App is unable to notify the server that the VJ is offline and some "zombie channels" remain in the LVB list. There are three solutions:
> 
> (Solution 1) You can use Tencent Cloud **[Notification Message Service](https://cloud.tencent.com/doc/api/258/5957)**: Register a **callback URL** for your server on Tencent Cloud, which will notify you of any change of the online status of the channel you have interest in. This solution has an instant response.
> 
> (Solution 2) You can use Tencent Cloud's status query API (**[Live_Channel_GetStatus](https://cloud.tencent.com/doc/api/258/5958)**) to regularly check whether all the channels <font color='red'>"Broadcasting"</font> are really in a "Pushing" status. However, this method has a slow response in case of a query for a large number of channels. You're recommended to conduct a poll every 1 minute. If a channel is offline in three consecutive polls, you can consider setting its status to offline.
>
> (Solution 3) You can add the **heartbeat mechanism** between the App and the server: When a VJ pushes streams, one heartbeat packet is sent to the server per minute. If the server fails to receive heartbeat packets for three consecutive minutes, the VJ is considered to be offline.

### 4. Interface with LVB
With the LVB Code, you can construct the push URL and playback URL. The following figure shows the RTMP, FLV, and HLS playback URLs constructed using the LVB Code **8888_test_12345_test**. After obtaining the playback URL, the App can send it to the Tencent Cloud RTMP SDK for playing:
![play](//mccdn.qcloud.com/static/img/8438aadc91d16a1f02921bb178881893/image.png)

>**Note**
> <font color='red'>It is not recommended to construct the playback URL on the App</font>, because the logic will be locked in the App code. It is recommended that the server return the constructed playback URL to the App, to facilitate subsequent extension. For example, with the product development, you may need to add more parameters and suffixes to the URL to implement more features.

### 5. Interface with record playback
With record playback, you can record the LVB process as an online VOD and provide it to your App users for playback. For more information on interfacing, please see [Record Playback](https://cloud.tencent.com/doc/api/258/5691).




