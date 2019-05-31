Free-run LVB (UGC + OGC) solution means that a VJ can start live broadcasting using his/her phone at any time. This solution is adopted by a number of live broadcasting platforms such as Inke, Huajiao, Douyu and Now. Compared with the single-session LVB solution that works by manually generating one or two LVB URLs, the free-run LVB solution requires you to focus on the **room management** related logic, that is, to maintain a "room list" visible to all users.
![](https://mc.qcloudimg.com/static/img/960995a7912e87179f5c2e1c72eb5f25/image.jpg)

The management and maintenance of a room list involves adding, deleting, modifying and querying rooms.

![](https://mc.qcloudimg.com/static/img/c937eb83b212750e839c57355e0a4c63/image.png)

<h2 id="ADD">ADD: Create a room for broadcasting</h2>

Before starting broadcasting, a VJ needs to apply for the creation of a room, which means adding a new data item to the room list on your sever.

- **Step 1: VJ requests broadcasting (Client -> Server)**
The Client sends the VJ account ID, room title, broadcast cover URL, geographical location (optional) and other information to your Server.

- **Step 2: Server creates a room (Server -> Client)**
The Server adds a record in the room list and sets its status to "Waiting for broadcasting (**inactive**)", and then returns the push [URL](https://cloud.tencent.com/document/product/454/9875), which is required for starting broadcasting, in the response packet to the Client.

- **Step 3: VJ starts push (TXLivePusher)**
After the Client gets the push URL and informs SDK of the URL, the SDK starts push and then notifies you through TXLivePushListener callback whether the push is successful. 

- **Step 4: VJ confirms broadcasting (Client -> Server)**
A VJ's push may not be successful. The failure of push can be caused by many reasons. For example, port 1935 used for push is disabled by the security firewall of the network, or the VJ accidentally selected "Reject" for camera authorization request when the App was just installed. Therefore, the purpose of Step 4 is to inform the backend to switch the room status from "Waiting for broadcasting (**inactive**)" to "Broadcasting...(**active**)" after the Client receives the push success event (ID: 1003) from SDK.

<h2 id="DELETE">DELETE: Close a room</h2>

After the broadcasting is finished, the Client notifies the backend to modify the room status to "Broadcasting Over (**close**)" or delete the room from the list.

- **Step 1: VJ stops broadcasting (Client -> Server)**
When a VJ stops broadcasting, the Client notifies the server of the ID of the live stream to be ended. Then, the server modifies the room status to "Broadcasting Over (**close**)" or delete the room from the list.

- **Step 2: Troubleshoot black-screen rooms (Server -> Tencent Cloud)**
If the VJ is disconnected from network or the App crashes unexpectedly, the Client is unable to notify the server, leaving some dark-screen rooms in the room list (the VJ can no longer push streams and no one closes these rooms, so the viewers can only see the black screen when entering the room).

 The Server can check whether all the rooms are really in the "Broadcasting...<font color='red'>(**active**)</font>" status at a regular basis (preferably every 10s) through Tencent Cloud REST API (**[Live_Channel_GetStatus](https://cloud.tencent.com/doc/api/258/5958)**). If a room is "offline" in three consecutive queries, the Server considers it a "black-screen room" and closes it.
 > If the network becomes unavailable for a short while and then is restored, the SDK is reconnected to the network automatically. The room status you queried during the reconnection may not be accurate. Therefore, it is recommended to consider a room "black-screen" only if you get an "offline" result in three queries in a row.

<h2 id="MODIFY">MODIFY: Room information</h2>

In many scenarios, you need to modify the room information, for example:

- **Add viewers (Client -> Server)**
When a new viewer joins the room, the number of viewers in the room needs to increase by 1. In this case, the viewer's App sends the Server a request for an addition to the room members.

- **Add likes (Client -> Server)**
When a viewer gives a "like" to a VJ, the number of "likes" in the room needs to increase by 1. In this case, the App sends the Server a request for an addition of like in the response function of the "Like" button.
> Note: A complete implementation of "like" involves broadcasting the "like" message to all the viewers through the chat room message channel.

- **Banned broadcasting due to violations (Server -> Tencent Cloud)**
When regulators find that the broadcasting content in a room violates relevant regulations, the broadcasting in the room needs to be banned, which means the room status should be changed to "Broadcasting Over (**close**)". At the same time, your server needs to notify Tencent Cloud through REST API [Enable/Disable Push](https://cloud.tencent.com/doc/api/258/5959) to stop push immediately.
> Note: Tencent Video Cloud's Porn Detection service is to help you identify among a number of rooms the live streams suspected of porn by capturing screenshots regularly, and to notify your backend server of the IDs of the suspected live streams via the address you specify. This service is still in Beta phase and cannot be activated by yourself. Contact us via 400 or submit a ticket if you need this service.

<h2 id="QUERY">QUERY: Room list</h2>

Each viewer would query the current room list from backend after opening the App. Therefore, an API for fetching the list needs to be provided for the App at backend.

- **Paging logic**
If the list contains a large number of rooms (for example, more than 100), it is recommended to add a paging logic that can help reduce server load and improve the list display speed.

- **Construct playback URL**
With the LVB Code (or room ID), you can construct the playback URL in a straightforward way. The following shows the RTMP, FLV and HLS playback URLs constructed with the LVB Code **8888_test_12345_test**. After obtaining the playback URL, the App sends it to Tencent Cloud RTMP SDK for playback:
> ![play](//mccdn.qcloud.com/static/img/8438aadc91d16a1f02921bb178881893/image.png)

- **<font color='red'>Don't</font> construct playback URL on the Client**
Playback URL is issued from the server, instead of being constructed on the Client. This can make your system more flexible. With the growth of your business, you may consider adding playback hotlink protection at the viewer end to prevent your video data from being hacked. However, hotlink protection signature can only be issued from the server, so constructing URL on client makes no sense in this respect.

