# Integration Overview

Built on Tencent's more than a decade of experience in QQ audio/video development, ILVB (Interactive Live Video Broadcasting) provides a complete set of solutions for live audio or video broadcasting, multiuser audio/video interaction and IM text interaction.

This chapter focuses on the overall integration process of AVSDK and server end. For more information about IM, please see [IM Integration Solution in LVB Scenario](/doc/product/269/%E7%9B%B4%E6%92%AD%E5%9C%BA%E6%99%AF%E4%B8%8B%E7%9A%84IM%E9%9B%86%E6%88%90%E6%96%B9%E6%A1%88)

For more information about client integration, please see [Integration Documentation](/doc/product/268/%E8%B0%83%E7%94%A8%E6%B5%81%E7%A8%8B%EF%BC%88Android%EF%BC%89)
You can also refer to Integration Demo FreeShow ([Download on Android](http://android.myapp.com/myapp/detail.htm?apkName=com.tencent.qcloud.suixinbo), [Download on iOS](https://itunes.apple.com/cn/app/sui-xin-bo/id1037944078?mt=8))
For the demo source code and introduction to the source code, please see github ([Android Source Code](https://github.com/zhaoyang21cn/Android_Suixinbo), [iOS Source Code ](https://github.com/zhaoyang21cn/iOS_Suixinbo), [Server-end Source Code](https://github.com/zhaoyang21cn/SuiXinBoPHPServer))

**！ Note: Be sure to read the source code introduction of FreeShow**

## SDK Structure
**ILVB SDK consists of two parts, IMSDK and AVSDK.**

![IMSDK+AVSDK Interaction Diagram](https://mccdn.qcloud.com/static/img/c1f2ab3b3d40eef889fe76dba49de7fa/im%2Bavsdk.png)

IMSDK, or instant messaging SDK, provides AVSDK with such features as account login, signaling channel, IM on-screen commenting, log module and log reporting.

AVSDK provides a range of features such as camera capturing, encoding, decoding and beauty filter. The overall framework of AVSDK is shown below.

![AVSDK Structure](https://mccdn.qcloud.com/static/img/423aa6782eaaa503b0c29f7cec5aaca6/image.png)

## Interaction Logic for Login
Tencent Cloud ILVB provides two ways of account interfacing.

- Hosted mode
  
	Tencent takes care of the account registration, password storage and verification.
- Standalone mode

	The third party stores account system on its own, and in ILVB, Tencent carries out a certain level of verification on the third party's account system. This is the most widely used verification method currently.

**This section focuses on the standalone mode.**

For more information, please see [Account Login Integration](https://cloud.tencent.com/doc/product/268/%E8%B4%A6%E5%8F%B7%E7%99%BB%E5%BD%95%E9%9B%86%E6%88%90%E8%AF%B4%E6%98%8E)

1. App logs in to business server, which then authenticates the user identity.

2. After performing the authentication successfully, the business server encrypts the user identify information using private key to generate **UserSig** to return to the client.

3. The **UserSig** is transmitted to the login API of IMSDK, and the login to Tencent Cloud server is completed.

![The process of issuing UserSig](https://mccdn.qcloud.com/static/img/fe587958a511ca5211ecae36165833dc/image.png)

## Interaction Logic for Creating a Room
ILVB achieves the exchange of audio/video streams based on the concept of room. This means the viewers and the VJ must be in the same room to achieve the messaging. But operations related to **room management** do not fall within ILVB scope. The features such as room number assignment, list of room members, and joining/exiting room by VJ and viewers can be managed by the client (can be implemented using IMSDK. For more information, please see [Room Status Notification](https://cloud.tencent.com/doc/product/268/%E6%88%BF%E9%97%B4%E7%8A%B6%E6%80%81%E9%80%9A%E7%9F%A5))

The interaction process for creating a room is as follows:

1. VJ sends a request for creating a room to the business server.

2. Business server assigns the room number.	

3. VJ creates the room by calling the AVSDK API for creating room using the assigned room number.

4. Inform business server of the creation.

![The interaction process for creating a room](//mccdn.qcloud.com/static/img/682b59a66ee6dfd391f1b5841320b799/image.png)

## Interaction Logic for Viewer to Join a Room
When the VJ has created the room, the list of rooms with a status of "Broadcasting..." already exists on the service-end live broadcasting platform. Viewers can see the room list after login. After clicking the room to join in, viewers can send IM messages or business logic to notify VJ and other viewers in the room. The flow diagram is as follows:

**Note: AVSDK does not support the notification of viewer joining the room, and does not maintain the number and list of room members. These can be implemented by IMSDK or client (see the dotted line of the diagram)**

![ Viewer joins the room for interaction](//mccdn.qcloud.com/static/img/cc9e2d826186c7e7af274d72827ca5ad/image.png)

## Interaction Logic for IM Messages Between Viewers and VJ
While watching the performance of VJ, viewers can interact with the VJ through IM by chatting, giving flowers, giving gifts, etc.

If any viewer wants to perform billed operations like giving flowers or gifts, two options are available:

- When a viewer gives flowers, ILVB cloud sends a callback to the service back-end to deduct the fee from the balance of the account
- When a viewer gives flowers, App sends an upstream request to LVB platform, which, after deducting the fee from the balance of the account, sends the message via [IMSDK REST API](/doc/product/269/%E5%9C%A8%E7%BE%A4%E7%BB%84%E4%B8%AD%E5%8F%91%E9%80%81%E6%99%AE%E9%80%9A%E6%B6%88%E6%81%AF)

**In case of a large number of room members, a huge message volume may cause performance issues at VJ end. In this case, the rendering strategy needs to be optimized at client side. At the same time, ILVB cloud (IMSDK) can control the message frequency.**

![IM and other message interactions](//mccdn.qcloud.com/static/img/85ec89b3af73dfad66491abdd75f3f8a/image.png)

## Interaction Logic for Viewer to Quit the Room
When a viewer quits the room, a notification also needs to be sent to VJ and other viewers. For more information about the process, please see [Interaction Logic for Viewer to Join the Room]()

## Interaction Logic for VJ to Quit the Room
When a VJ quits the room, the following should be done:

- Notify the service-end live broadcasting platform to terminate the room
- Notify other viewers of the quitting
- Show LVB end page (display the broadcasting duration, popularity, etc.)

The flow diagram is as follows:

![Interactions involved when VJ quits the room](//mccdn.qcloud.com/static/img/1756876dc4b82627d695511d6bd81c1d/image.png)


## Joint Video Broadcasting
Joint broadcasting is a feature developed by Tencent Cloud's ILVB SDK in LVB scenario and allows the video connection and chatting between VJ and viewer(s). Other viewers can see the video views of the VJ and the invited viewer(s). Some Apps such as Inke and JMEI have implemented this feature.

You can download FreeShow to have a try by referring to the wrapped code ([Download on Android](http://android.myapp.com/myapp/detail.htm?apkName=com.tencent.qcloud.suixinbo), [Download on iOS](https://itunes.apple.com/cn/app/sui-xin-bo/id1037944078?mt=8))

The implementation process for joining a broadcasting is as follows:
![Inviting viewer A to join the broadcasting](//mccdn.qcloud.com/static/img/94595a0b1a426415c39b4e81e085c255/image.png)
**Note**
- Inviting viewer A to join broadcasting requires sending P2P (peer-to-peer) messages (using private chatting message of IMSDK, which is implemented via CustomElem)
- Be sure not to send the broadcast message indicating viewer A joins broadcasting until viewer A has joined the broadcasting successfully (has enabled the microphone and camera and uploaded the local view)
- The notification of joining broadcasting can be sent through broadcast message (CustomElem) of IM


The implementation process for quitting broadcasting is as follows:
![Viewer A is quitting a broadcasting](//mccdn.qcloud.com/static/img/29b14a667d287144e6612262ac39ba4f/image.png)
**Note**
- This should be considered for both VJ and viewer A quitting the broadcasting (code protection is needed)
- The notification of quitting broadcasting can be sent at the same time when the quitting viewer closes the upload of local video. But it is recommended to send the notification before closing the local video.

## Push RTMP/HLS (watching on H5 or Web)
ILVB SDK can directly transcode the private protocol to RTMP and HLS, which are then shared by client to Apps such as WeChat, QQ, Moments and QZone.

**Tips**
**You can simply set the parameter TIMAvManage.StreamParam to recording without the need to call the API for recording (recording has the same lifecycle as push and is finished with the ending of push)**

**Note**
- ILVB uses CDN for LVB, so it is very important to apply for the LVB permission at client side.
- LVB has a limit on the number of channels, so sufficient channels need to be applied in advance at client side.
- If any channel fails to be terminated normally due to various client exceptions, developer needs to disable the channel manually on Tencent Cloud console. Otherwise the channel always exists (taking up the total number of channels)

Please see the document [Non-interactive Broadcasting Development](/doc/product/268/3226)

## Record VJ's Video (playback)
ILVB features API for recording audio/video to record VJ's audio/video and store it on the VOD server. After the transcoding, features such as playback and distribution can be implemented.

**Note**
- VOD service needs to be activated.
- The recording feature only applies to VJ, the person who joins the room first and has the audio and video stream.
- During recording, one MP4 file is generated every 60 minutes.
- Transcoding takes time.
- The API for ending recording needs to be called explicitly.

For more documents, please see [Recording Feature Development](/doc/product/268/3218#6-.E6.B3.A8.E6.84.8F.E4.BA.8B.E9.A1.B9)

# Porn Detection
To be added

## Must-read: Considerations for Development
* In case of a large number of viewers, an dramatic increase of message volume will happen. In this case, **pay close attention to the performance at VJ end** to avoid stutters caused by soaring CPU usage resulting from too much rendering codes.
* A VJ may get disconnected for some reason (CRASH, network interruption), so heartbeat test for VJ should be added on the service-end live broadcasting platform to ensure the real-time update of LVB list.
* ILVB does not support such operations as management of room members, which need to be implemented on the service-end live broadcasting platform or by using [IMSDK Solution](/doc/product/269/%E7%9B%B4%E6%92%AD%E5%9C%BA%E6%99%AF%E4%B8%8B%E7%9A%84IM%E9%9B%86%E6%88%90%E6%96%B9%E6%A1%88).

