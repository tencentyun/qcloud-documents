## 1. Background

In some scenarios, when a user joins or exits a room or any status change occurs, the client may want to notify others in the room of these, or trigger some logic processing in the business backend. But considering such factors as the path length of notification signaling, the frequency of users' joining or exiting large ILVB room and the access performance of HTTPS service at client, Tencent ILVB backend currently does not provide the direct callback about status changes to the business backend. To cater for the client which has demand for such notification, we provide several implementation solutions for the reference of technical personnel.

## 2. [Solution 1] Notification Based on Self-built Channel

If the client has its own public network access service to achieve the signaling interaction between App and its own business backend, follow the process below to achieve the notification mechanism. We assume that the business backend needs to process some business logics before spreading the notification to others in the room. The assumption also applies for the following scenario. If spreading such notification is not needed, you just need to ignore the steps for spreading in the solution.

![Notification Based on Self-built Channel](//mccdn.qcloud.com/img56cdd27e26d02.png)

Advantages of the solution:  

+ Being simple and intuitive, the solution makes full use of the existing infrastructure of client.

Drawbacks of the solution:

+ The entire process relies on the quality of client's own signaling/message**`access service`**, but small and medium-sized businesses usually have more or less potential problems in such aspects as number of access points, the coverage, concurrency capacity, security (channel encryption) and stability.
+ The connection mechanism between the backend and App in some businesses is insufficient to handle the real-time signaling interaction logic.

For the businesses that have difficulties in the self-maintained signaling access service, the following solution is recommended.

## 3. [Solution 2] Notification Based on OpenSSO Channel/QAL

This solution introduces Tencent Cloud OpenSSO as the access layer, which is the only difference between it and Solution 1. Tencent Cloud OpenSSO provides the access coverage comparable to QQ, and has been tested by a mass of users in massive concurrency handling, security, reliability and stability, being able to solve the potential access problems found in the [solution described above](#2-基于业务自建通道的通知方案). In addition, client can use this high-quality channel to transmit other signals, thereby reducing the maintenance costs and improving the overall quality of signal transmission. It is worth mentioning that IMSDK (1.7 and above) also reuses this channel to transmit the IM message signaling. This means the quality of the channel is absolutely guaranteed 

![Notification Based on OpenSSO Channel](//mccdn.qcloud.com/img56cdd2d9be4d0.png)

## 4. [Solution 3] Callback Based on ImSdk API

AVSDK of Tencent Cloud ILVB relies on the IMSDK of Tencent Instant Messaging (IM), so the App using Tencent Cloud ILVB service naturally has the IM capability. As a result, the notification of joining/exiting audio/video room can be implemented based on the [Third-party Callback](http://avc.qcloud.com/wiki2.0/im/第三方回调/第三方回调简介/第三方回调简介.html) mechanism provided by ImSdk.

![Callback Based on ImSdk Callback API](//mccdn.qcloud.com/img56cdd457088cf.png)

Advantages of the solution:

+ IMSDK directly provides a message API which is easy to use.
+ The use of IM channel throughout the process ensures the quality of signaling transmission.

Note: The current IM mechanism is that either all messages are called back or no message is called back. Therefore, if the client has used the IM service without callback, then the solution needs to change the callback mechanism to "Call Back All".

## 5. Solution for Notification of End of Live Broadcasting Featuring Beauty VJ

Generally, in the common live broadcasting Apps featuring beauty VJs, only one VJ transmits the upstream audio/video data and other users watch the video and interact with VJ through IM messages. After a VJ exits the room, it is usually necessary to notify all the viewers of the end of the live broadcasting, even if the room has not been physically terminated (as long as there are users in the room, the room cannot be terminated by the audio/video backend).

In this case, we recommend [Solution 3](#4-【方案三】基于ImSdk接口的回调方案) Callback Based on ImSdk API). First, we assume that a heartbeat mechanism exists between the business App and the business backend to ensure that the business backend is aware of any status change of App in a timely manner. Second, we assume that the client is using Tencent Cloud IM service to send IM broadcast messages through App or business backend (client can also send IM messages using a third-party messaging service or self-built channel). The process is as follows:
- If VJ's App **`exits`** the audio/video room normally, the App can send an IM broadcast message to all the viewers after the exit performed by AVSDK. When viewers' Apps receive the message, a pop-up indicating the end of live broadcasting appears.
- If VJ's App **`exits`** abnormally (Crash, network interruption and timeout, etc.), the heartbeat between the business backend and the App would surely time out, indicating that the VJ's App has been forced to exit the room. At this point, the business backend sends an IM broadcast messages to all the viewers in this room. When viewers' Apps receive the message, a pop-up indicating the end of live broadcasting appears.

Why does the logic for notifying of the end of live broadcasting use **IM message notification** instead of the event callback **`OnEndpointsUpdateInfo(EVENT_ID_ENDPOINT_EXIT)`** of AVSDK? This is mainly because the Tencent Cloud ILVB solution supports super-large rooms with up to 10,000-level online users, where the joining and exiting of users are highly frequent and uncontrollable. Notifying App of all such operations using callback of AVSDK can produce significant effect on the App performance. Currently, AVSDK backend only issues notification of user's joining and exiting if the number of people in the room is ***`less than 50 `***. When the number is greater than 50, AVSDK backend does not send such notification and the App will no longer receive the callback **`OnEndpointsUpdateInfo(EVENT_ID_ENDPOINT_EXIT/ENTER)`**. In ILVB featuring beauty VJs, the number of people in VJ's room is often more than 50. In this case, it is not recommended to use AVSDK callback to give notification of the end of live broadcasting.
