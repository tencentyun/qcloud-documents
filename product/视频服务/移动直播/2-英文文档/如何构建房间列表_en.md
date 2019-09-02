## Room List
Each VJ has his or her own LVB room. The room list for all the VJs is shown below:
![001](//mc.qcloudimg.com/static/img/1e6d141a053482e568110d1c1cfc7344/image.png)

## How to Work with LVB Rooms
### 1. How it works
The key functions of LVB background are managing and maintaining the **room list**, and providing the APIs for adding, deleting, modifying and querying the room list:
![](//mc.qcloudimg.com/static/img/e8a2be9cf6c85a65d0cbdbaac0951228/image.png)

- ** Create a room (Add)**
Before starting an LVB, the VJ needs to create a room, which means adding a new data entry to the room list.

- ** Close a room (Delete) **
After an LVB is finished, the App needs to notify the background to modify the room status to **LVB Finished** or delete the room from the list.

- ** Modify room status (Modify) **
When a new viewer joins the LVB, the number of viewers of the room increases by 1;
When a viewer gives a "like" to the VJ, the number of "likes" of the room increases by 1;
When a video stream is interrupted unexpectedly, you can receive a notification from Tencent Cloud which indicates the room status needs to be adjusted;
When regulators find that the LVB content in a room has violated relevant regulations, the LVB in the room needs to be banned, which means the room status should be changed to "Banned".

- **Query room list (Query)**
Each viewer would query the current room list in the background after opening the App. Therefore, an interface for fetching the list needs to be provided for the App in the background. Furthermore, if your App has a large install base, the interface capacity must be enough to accommodate a large number of concurrent accesses.

### 2. Activate LVB Code
For more information about how to activate LVB Code, please see [How to configure LVB Code Access]. (Https://cloud.tencent.com/document/product/454/7953#1.2-.E7.9B.B4.E6.92.AD.E7.A0.81.E6.8E.A5.E5.85. A5.E6.80.8E.E4.B9.88.E9.85.8D.EF.BC.9F)

### 3. Create a room

Before initiating an LVB, the App on mobile device first requests the server to create a room by using a protocol:

- **Request (App -> Server)**
The most important information is your account ID. At the same time, it is recommended to provide LVB title, geographical location, LVB cover URL and other information. A room will be created in the LVB background based on these information.

- **Response (Server -> App)**
The server may give two types of responses: 1. Allowing the LVB and returning the push URL (as shown in the figure below) and other information to the App; 2. Rejecting the LVB and returning the reason for the error.

- **How to construct a push URL**
You can construct a push URL in the background by referring to [How to obtain the push URL](https://cloud.tencent.com/document/product/454/7915).

- **Modify status (New -> Broadcasting)**
Do not set a new room to a status of "Broadcasting", because this may cause a black screen if the VJ fails to push stream successfully. The failure of push can be attributed to many factors. For example, port 1935 used for push is disabled by the security firewall of the network, or the VJ mistakenly selected "Reject" for the request for camera permission immediately after the App was installed.

 The process should proceed as follows: The App confirms the success of push after receiving the **PUSH_BEGIN** event of RTMP SDK, and then uses a protocol to notify the background to change the room status to "Broadcasting".
 
 > In Mini LVB, the option of App notification is selected. For the sample implementation, please see [More About Protocol - Modify Online Status](https://cloud.tencent.com/doc/product/454/6808#2..E4.BF.AE.E6.94.B9.E5.9C.A8.E7.BA.BF.E7.8A.B6.E6.80.81).


### 4. Close a room

When an LVB ends, the App needs to use a protocol to notify the server so that it can delete the relevant records at the earliest possible time. Otherwise, the LVB list is full of offline VJ channels.

However, this does not mean everything is fine. Any unexpected situation, such as disconnection of VJ's mobile phone from network, crash of App, or running out of traffic, can prevent the App from informing the server that the VJ is offline, thus leaving some "zombie channels" in the LVB list.

These zombie channels have a significant impact on user experience, so we need **"double insurance"** to avoid this problem. You can choose one of the following options:

- **Receive Notification**
You can use Tencent Cloud's **[Notification Message Service](https://cloud.tencent.com/doc/api/258/5957)**: Register a **callback URL** for your server on Tencent Cloud, which will notify you of any change of the online status of channel you have interest in.

- **Active Query**
You can use Tencent Cloud's status query API (**[Live_Channel_GetStatus](https://cloud.tencent.com/doc/api/258/5958)**) to regularly check whether all the channels "Broadcasting" are really in a "Pushing" status. You're recommended to conduct a poll every 1 minute. If a channel is offline in three consecutive polls, you can consider setting its status to offline.

> The Mini LVB App here reuses the protocol used to modify the room status during room creation. When a room is created, App uses this protocol to change its status from "New" to "Broadcasting", but here the status is changed from "Broadcasting" to "Closed". For more information, please see [More About Protocol - Modify Online Status](https://cloud.tencent.com/doc/product/454/6808#2..E4.BF.AE.E6.94.B9.E5.9C.A8.E7.BA.BF.E7.8A.B6.E6.80.81).


### 5. Modify Room Information

In many scenarios, we need to modify the room information, for example:

- **Increase the number of viewers**
When a new viewer joins the LVB, the number of viewers of the room needs to increase by 1, which can be implemented by allowing the App to send a notification protocol when the viewer enters the room.
> For more information about Mini LVB's implementation for this scenario, please see [More About Protocol - Modify Counter](https://cloud.tencent.com/doc/product/454/6808#3..E4.BF.AE.E6.94.B9.E8.AE.A1.E6.95.B0.E5.99.A8).

- **Increase the number of "likes"**
When a viewer gives a "like" to a VJ, the number of "likes" of the room needs to increase by 1, which can be achieved by allowing the App to send a notification protocol in the response function for the "Like" button. A complete "Give a Like" implementation needs a broadcasting of "likes" through IM channel, which will not be discussed further here.
> For more information about Mini LVB's implementation for this scenario, please see [More About Protocol - Modify Counter](https://cloud.tencent.com/doc/product/454/6808#3..E4.BF.AE.E6.94.B9.E8.AE.A1.E6.95.B0.E5.99.A8).

- **Unexpected stream interruption**
You can use Tencent Cloud **[Notification Message Service](https://cloud.tencent.com/doc/api/258/5957)**. In case of an interruption of video stream, you'll receive a notification from Tencent Cloud that indicates the status of a room needs to be adjusted.
> For the Mini LVB implementation for this scenario, please see Mini LVB backend PHP source code.

- **Banned LVB due to violation of regulations**
When regulators find that the LVB content in a room has violated relevant regulations, the LVB in the room needs to be banned, which means the room status should be changed to "Banned". Use the backend API [LVB Code- Enable/Disable Push](https://cloud.tencent.com/doc/api/258/5959) to ban an LVB.

- **Additional Notes**
The number of viewers and "likes" are frequently modified. In the first version of Mini LVB PHP source code, these status data is stored in database. This design is easy to understand but not reasonable. If your App has a large install base, it is recommended to use Tencent Cloud's [**Redis**](https://cloud.tencent.com/product/crs.html) service for an optimization. Our future source code versions will provide implementations accordingly.


### 6. Room list query API

The room list is maintained and managed on the server to be used by the App at viewer end, so query API is required. For the implementation of query API, the following points should be taken into consideration:

- **Paging logic**
If the list contains a large number of rooms (for example, more than 20), it is recommended to add a paging logic that can help reduce server load and improve the list display speed.
> For more information about the Mini LVB implementation for this scenario, please see [More About Protocol - Pull List](https://cloud.tencent.com/doc/product/454/6808#4..E6.8B.89.E5.8F.96.E5.88.97.E8.A1.A8).

- **Construct playback URL**
With the LVB Code (or room ID), you can construct the playback URL in a straightforward way. The following shows the RTMP, FLV and HLS playback URLs constructed with the LVB Code **8888_test_12345_test**. After obtaining the playback URL, the App sends it to Tencent Cloud RTMP SDK for playback:
> ![play](//mccdn.qcloud.com/static/img/8438aadc91d16a1f02921bb178881893/image.png)

- **Do not construct the URL at the App end**
Otherwise, the logic will be locked in the App code. It is recommended to allow the server to construct the URL and then return it to App. With the growth of your business, you may consider adding playback hotlink protection at the player end to prevent your video data from being stolen by other users. However, hotlink protection signature can only be issued on the server, so constructing URL at client makes no sense in this respect.
