## Effect Experience

### Demo installation
Download and install our Demo to experience how online quizzes are presented. Two options are available to experience it, both of which allow for perfect "sound-image-question" synchronization.

 | iOS platform (ipa) | Android platform (apk) | OBS Studio customized version (exe) |
 | --------- | --------- | --------- |
 |  [iOS](https://www.pgyer.com/liteAV) | [Android](http://dldir1.qq.com/hudongzhibo/xiaozhibo/LiteAVDemo_Smart_4.1.QARoom.apk)  |[Obs Studio](http://dldir1.qq.com/hudongzhibo/xiaozhibo/obs_distribute_question.zip)|
 
### Option 1: Online quiz room
Create a room to view what it looks like at the host end and enter the room to view what it looks like at the viewer end.

- Demos for the iPhone platform are provided in an enterprise-signed manner. Go to **Settings** -> **General** -> **Device Management** to add a trust certificate first.
- Demos are only used to illustrate the technical expertise of Tencent Cloud. They do not represent how the final product looks like. Read this document carefully before you integrate any demo.

![](https://mc.qcloudimg.com/static/img/0eeed7dc697cf3c26c7053d6776a64fd/image.jpg)

### Option 2: OBS Studio
With this option, [Obs Studio](http://dldir1.qq.com/hudongzhibo/xiaozhibo/obs_distribute_question.zip), which was modified by Tencent Cloud, is used directly to push streams:
- We have added a **Question Assignment** button to the **Tools** menu bar, so that you can insert questions into LVB streams. You can edit questions in an ini file in advance.
- Open the Demo App in iOS or Android and choose the **Quiz Player** function to experience how questions are received at the viewer end.

![](https://mc.qcloudimg.com/static/img/ba2b8baff92a6ee13f18c0a29e5d9718/image.gif)

<h2 id="SDK">SDK Downloading</h2>

- **LiteAVSDK (4.1.3173)**
is used for RTMP push and FLV playback. The Smart version provides both of the two functions, and the LivePlay version only provides FLV playback.

<table>
  <tr align="center">
    <th width="150px">Operating System</th>
    <th width="150px">Download Link</th>
		<th width="100px">RTMP Push</th>
		<th width="100px">RTMP Playback</th>
		<th width="100px">FLV Playback</th>
		<th width="200px">Notes</th>
  </tr>
  <tr align="center" >
	  <td rowspan="2">iOS</td>
		<td><a href="http://liteavsdk-1252463788.cosgz.myqcloud.com/answer/TXLiteAVSDK_Smart_iOS_4.1.3173.zip">DOWNLOAD</a></td>
		<td>YES</td>
		<td>YES</td>
		<td>YES</td>
		<td>Both SDK and Demo source codes are in a zip file</td>
  </tr>
	<tr align="center">
		<td><a href="http://liteavsdk-1252463788.cosgz.myqcloud.com/answer/TXLiteAVSDK_LivePlay_iOS_4.1.3173.zip">DOWNLOAD</a></td>
		<td>NO</td>
		<td>YES</td>
		<td>YES</td>
		<td>Size increment: 700 KB, both SDK and Demo source codes are in a zip file</td>
  </tr>
	<tr align="center">
	  <td rowspan="2">Android</td>
		<td><a href="http://liteavsdk-1252463788.cosgz.myqcloud.com/answer/LiteAVSDK_Smart_Android_4.1.3173.zip">DOWNLOAD</a></td>
		<td>YES</td>
		<td>YES</td>
		<td>YES</td>
		<td>Both SDK and Demo source codes are in a zip file</td>
  </tr>
	<tr align="center">
		<td><a href="http://liteavsdk-1252463788.cosgz.myqcloud.com/answer/LiteAVSDK_LivePlay_Android_4.1.3173.zip">DOWNLOAD</a></td>
		<td>NO</td>
		<td>YES</td>
		<td>YES</td>
		<td>jar increment: 350 KB, both SDK and Demo source codes are in a zip file</td>
  </tr>
</table>

- **LiteIMSDK (1.3.0.130)**
is used for functions such as chat room and on-screen comment. The download link here points to a simplified version. You may download a full version from the Tencent [Instant Messaging](https://cloud.tencent.com/product/im) (IM) website.

| Operating System | Download Link | Notes |
|---------|---------|---------|
| iOS | [DOWNLOAD](http://dldir1.qq.com/hudongzhibo/im/liteim/ImSDK_IOS.zip) | This is a simplified version, with a size increment of 1.74 MB. |
| Android | [DOWNLOAD](http://dldir1.qq.com/hudongzhibo/im/liteim/liteimsdk-release.aar) | This is a simplified version, with a size increment of 670 KB. |



## Our Advantages
- **Precise "sound-image-question" synchronization**
Both Tencent Cloud SDK and the cloud support inserting **questions** or **time synchronization signaling** into LVB streams to achieve perfect synchronization of sounds, images and question pop-ups.

- **Ultra-low latency deviation at the viewer end**
The latency correction technology supported by the [**speedy playback mode**](https://cloud.tencent.com/document/product/454/7880#.E5.8D.A1.E9.A1.BF.26amp.3B.E5.BB.B6.E8.BF.9F) in Tencent Cloud SDK can keep the latency deviation between viewers within 1 sec, thus ensuring that viewers answer questions synchronously.

- **Integration with WeChat Mini Programs**
Tencent Cloud SDK is packed in WeChat by default and made publicly available as a [&lt;live-player&gt;](https://cloud.tencent.com/document/product/454/12519)  tag. Set the mode to live, and also set min-cache and max-cache to 1 to enable ultra-low latency in playback.

## Method Details

### Method 1: Transparent question transmission
![](https://mc.qcloudimg.com/static/img/57c924fa3ca6642aabfb9bf5156041fc/image.jpg)

#### How it works
- **Message delivery (OBS)**:
If you are using OBS to push streams in studios, you can replace the current OBS software directly with  [Obs Studio](http://dldir1.qq.com/hudongzhibo/xiaozhibo/obs_distribute_question.zip), which was modified by Tencent Cloud. We have added a **Question Assignment** button to the **Tools** menu bar, so that you can insert questions into LVB streams. You can edit questions in an ini file in advance.

- **Message delivery (App)**:
To simply use your App to push streams, you can use the sendMessage method of the TXLivePusher in Tencent Cloud SDK. This method allows inserting a buffer, the length of which must be limited to 10 KB, to RTMP streams.
```objectiveC
//iOS sample code
[_answerPusher sendMessage:[mesg dataUsingEncoding:NSUTF8StringEncoding]];
```
```java
//Android sample code
mTXLivePusher.sendMessage(questionInfo.getBytes("UTF-8"));
```

- **Message receiving**:
By using the onPlayEvent (PLAY_EVT_GET_MESSAGE: 2012) function of the TXLivePlayer in Tencent Cloud SDK, you can have the message received by your App and the questions spread to the massive viewer-end Apps at exactly the time when a specific image is played back.

For more information about integration solutions for message receiving, please see our integration document ([iOS Platform](https://cloud.tencent.com/document/product/454/7880#Message) | [Android Platform](https://cloud.tencent.com/document/product/454/7886#Message))).

### Method 2: NTP Time Synchronization
![](https://mc.qcloudimg.com/static/img/c7f9687497710d6c65f79577e5248035/image.jpg)

#### How it works
1. Tencent Cloud inserts in real time an international standard timestamp calibrated by NTP into LVB streams every other second.
2. The program director in the studio assigns questions at the appropriate time based on the pace at which the host raises questions. The assignment system inserts the current international standard time into the questions assigned each time.
3. When playing back video streams inserted with such timestamps, SDK notifies your App of the time when the currently played back image was recorded. Considering a fixed latency from the studio to the cloud, make sure you correct the deviation in advance.
4. Your App can display specified questions as needed according to the time notifications saying when the current image was recorded from the SDK.

In summary, the biggest difference between Method 1 and Method 2 is how questions are spread. In Method 2, the questions are quickly sent to the viewer-end App through the IM channel and cached at the viewer end. Then the questions are displayed after the player is notified of the expected NTP timestamp.


### Method 3: Mini Program Solutions
While both of the above two methods provide perfect "sound-image-question" synchronization, what matters more than this minor optimization on experience is the spreading capability of an App. Mini Program happens to provide an App with the capability of viral spread.

Tencent Cloud SDK is packed in WeChat by default and made publicly available as a [&lt;live-player&gt;](https://cloud.tencent.com/document/product/454/12519) tag.
- If an flv playback URL is used,
- set the mode to live,
- min-cache and max-cache to 1,
- and push-end GOP to 1.

This minimizes the playback latency and keeps the latency deviation between viewers within 1 sec. Although exact "sound-image-question" synchronization is unrealizable, the effects can be as good as they are in an App. (Online quizzes were not popularized when the video cloud SDK was packed in WeChat, so inserting messages into audio/video streams is not supported.)

The rest step is to assign questions to the mini program through the websocket channel of the mini program or by using the webim solution.

<video src="
http://1252463788.vod2.myqcloud.com/95576ef5vodtransgzp1252463788/d76641444564972818989641965/v.f20.mp4" controls="controls">
Your browser does not support video tags.
</video>

## Integration Guide (Method 1)
### Step 1: Activate Tencent Cloud LVB service
Contact us for activating Tencent Cloud [LVB service](https://cloud.tencent.com/document/product/267/13551). You can call our 400 customer service number to rush the approval process if you need it urgently.

### Step 2: Obtain the push URL
To simply obtain a push URL, please see the document [How to Get URL Quickly](https://cloud.tencent.com/document/product/267/7977)..
To understand the relationship between push URL and Live room ID, please see the document [How to realize auto construction at the backend](https://cloud.tencent.com/document/product/267/13457).
To protect the push URL from being stolen, please see the document [Hotlink protection signature](https://cloud.tencent.com/document/product/267/13458).

### Step 3: Obtain the playback URL
There is a one-to-one mapping between the playback URL and the push URL. Please see the following figure for the mapping rule.
![](https://mc.qcloudimg.com/static/img/64342b926e05da462a54b8ce4f8c526f/image.png)

Be sure to use the playback URL in <font color='red'>**FLV**</font> format, because RTMP tends to stutter in high-concurrency scenarios.

### Step 4: Configure the push end
If you are using your App to push streams, please see the document([iOS](https://cloud.tencent.com/document/product/454/7879) | [Android](https://cloud.tencent.com/document/product/454/7885))..

If you are using OBS to push streams, note the following important settings:
#### I-frame interval (GOP)
Generally, two methods are available for integration studios: OBS Studio push and encoder push, both having mature configuration APIs. It is recommended to set GOP (also known as "keyframe interval") to 1 sec, which reduces the viewer-end latency deviation to a very low level.

Setting GOP to x264 has little effect on the encoding efficiency, but causes much latency. The higher the GOP is, the more cache there is on the server. Excessively high GOP has huge impact on viewers who just entered, because it takes time for SDK to correct latency.

The following figure shows the keyframe interval settings in OBS Studio:
![](https://mc.qcloudimg.com/static/img/204d041289f535ef9355ca8b45780e5d/image.jpg)

#### Encoding parameters
| Recommended Configuration | Resolution | Video Bitrate | Frame Rate | Number of Channels | Sampling Rate | Audio Bitrate |
|----------------|---------|---------|---------| --------|----|----|
| Image Quality Priority | 540x960 | 1000 Kbps | 25 | 1 | 48k | 72 Kbps |
| Cost Priority | 360x640 | 600 Kbps | 20 | 1 | 48k | 72 Kbps |
![](https://mc.qcloudimg.com/static/img/3c4a53b596e1663b5d12e4779922045a/image.jpg)
![](https://mc.qcloudimg.com/static/img/2516df29225a4e13db1c0a217dc0996c/image.jpg)

### Step 5: Integrate the player
1. Download the [SDK](#SDK) version listed in the second section of the document.

2. See the integration document ([iOS](https://cloud.tencent.com/document/product/454/7880) | [Android](https://cloud.tencent.com/document/product/454/7886))) to integrate the player. It takes about half a day to finish the work in the two platforms.

3. **<font color='red'>Change the default settings</font>**
 Normal LVB scenarios are set by default in the SDK, so it is necessary to change the settings as follows:
 ```objectiveC
//iOS Source Code
TXLivePlayConfig *config = [[TXLivePlayConfig alloc] init];
TXLivePlayer *player = [[TXLivePlayer alloc] init];
//
//Enable message receiving. Failing to receive messages means this function has not been enabled (default: disabled).
config.enableMessage = YES;
//
//Set the break-event point for latency to 2 seconds. (Given the latency due to the transmission from the cloud and the push end, the actual latency is more than 3 seconds: 3 seconds for SDK push latency and 4-5 seconds for obs push latency.)
config.bAutoAdjustCacheTime = YES;
config.maxAutoAdjustCacheTime = 2;
config.minAutoAdjustCacheTime = 2;
config.cacheTime = 2;
config.connectRetryCount = 3;
config.connectRetryInterval = 3;
config.enableAEC = NO;
//First setConfig and then startPlay
[player setConfig:config];
``` 
```java
//Android Source Code
mTXLivePlayConfig = new TXLivePlayConfig();
mTXLivePlayer = new TXLivePlayer(context);
//
//Enable message receiving. Failing to receive messages means this function has not been enabled (default: disabled).
mTXLivePlayConfig.setEnableMessage(true);
//
//Set the break-event point for latency to 2 seconds. (Given the latency due to the transmission from the cloud and the push end, the actual latency is more than 3 seconds: 3 seconds for SDK push latency and 4-5 seconds for OBS push latency.)
mTXLivePlayConfig.setAutoAdjustCacheTime(true);
mTXLivePlayConfig.setCacheTime(2.0f);
mTXLivePlayConfig.setMaxAutoAdjustCacheTime(2.0f);
mTXLivePlayConfig.setMinAutoAdjustCacheTime(2.0f);
//
//First setConfig and then startPlay
mTXLivePlayer.setConfig(mTXLivePlayConfig);
```

4. Be sure to use the playback URL in <font color='red'>**FLV**</font> format, because RTMP tends to stutter in high-concurrency scenarios.

### Step 6: Questions spreading
- If you are using your App to assign questions, you can use the sendMessage calling method in TXLivePusher. Please see the document ([iOS](https://cloud.tencent.com/document/product/454/7879#Message) | [Android](https://cloud.tencent.com/document/product/454/7885#Message)). for details.

- If you are using the customized [Obs Studio](http://dldir1.qq.com/hudongzhibo/xiaozhibo/obs_distribute_question.zip) to assign questions, you can first edit the questions in a local ini file and then a program director will spread the questions at an appropriate time.

<font color='red'>**Reliability evaluation**</font>
Some customers may worry if the unstable audio/video channels will cause any stutter or video data loss that makes the viewer unable to see the questions.
- Frame loss with LVB audio/video data occurs on a per-GOP basis. If GOP is 1, then 1 second of audio/video data will be lost each time.
- According to the node deployment by Tencent Cloud, 90% of the video stutter is caused by a slow network connection at the viewer end. In this case, the other network connections won't be smooth, either.

The solution to this problem is to send a question message every second (if GOP is set to 1 second) and eliminate the repeated question numbers at the viewer end. This prevents audio/video stutter from affecting the reliability of question arrival.

### Step 7: Receiving question messages
In our push APP Demo and customized OBS Studio, questions are organized into a buffer in json format and inserted into audio/video streams before being sent out.

Once you receive this buffer, you can parse it and complete the UI display. If you need to adjust json format to support more customizations, modify the source code or contact us for help.

- Switch the **enableMessage** toggle button in TXLivePlayConfig to **YES**.
- TXLivePlayer listens into messages by **TXLivePlayListener**, message No.: **PLAY_EVT_GET_MESSAGE (2012)**.

```objectiveC
 //iOS code
 -(void) onPlayEvent:(int)EvtID withParam:(NSDictionary *)param {
    [self asyncRun:^{
        if (EvtID == PLAY_EVT_GET_MESSAGE) {
            dispatch_async(dispatch_get_main_queue(), ^{ //Throw to the main thread to avoid thread security issues
                if ([_delegate respondsToSelector:@selector(onPlayerMessage:)]) {
                    [_delegate onPlayerMessage:param[@"EVT_GET_MSG"]];
                }
            });
        }
    }];
}
```

```java
//Android sample code
mTXLivePlayer.setPlayListener(new ITXLivePlayListener() {
        @Override
        public void onPlayEvent(int event, Bundle param) {
            if (event == TXLiveConstants.PLAY_ERR_NET_DISCONNECT) {
                roomListenerCallback.onDebugLog("[AnswerRoom] Pull failed: network disconnected");
                roomListenerCallback.onError(-1, "Network disconnected, pull failed");
            }
            else if (event == TXLiveConstants.PLAY_EVT_GET_MESSAGE) {
                String msg = null;
                try {
                    msg = new String(param.getByteArray(TXLiveConstants.EVT_GET_MSG), "UTF-8");
                    roomListenerCallback.onRecvAnswerMsg(msg);
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                }
            }
        }
});
```

### Step 8: Developing a quiz system
Due to Tencent Cloud's position as a PaaS service provider, quiz and payment systems that are closely associated with your business are not included in our offering package, so you need to develop them by yourself.

A common solution is to collect customers' answers as HTTP(S) requests to the quiz server. You just need to get prepared to deal with surges in highly concurrent requests.

Some customers may ask whether the IM system can be used to do the quizzes. The answer for now is no, because the IM system is good at spreading messages, while the aim of doing quizzes is to collect information.

### Step 9: Displaying quiz result
The quiz will be closed after the questions are displayed for a while. Then the quiz system will gather the results and deliver them to the viewers.

If you are using the customized [Obs Studio](http://dldir1.qq.com/hudongzhibo/xiaozhibo/obs_distribute_question.zip) to spread results, prepare a simple server that provides an http API for communication with OBS about questions, answers and the number of people in the agreed json format. In this way, questions and answers are delivered.

## Integration Guide (Method 2)
### Step 1: Activate Tencent Cloud LVB service
Repeat the corresponding step in Method 1.

### Step 2: Obtain the push URL and add NTP timestamp
Follow the corresponding step in Method 1, except that an extra parameter is required to obtain the push URL:

**Add NTP timestamp**
Add the parameter <font color='red'>&txAddTimestamp=2</font> after obtaining the push URL. (txAddTimestamp was previously set to 1, which caused black screen in mini programs.) The server inserts an international standard SEI timestamp into LVB streams every other second (with a deviation less than 100 ms). If you use our player to playback the video streams, you will receive a message that notifies NTP time of the current image every other second.

### Step 3: Obtain the playback URL
Repeat the corresponding step in Method 1.

### Step 4: Configure the push end
Repeat the corresponding step in Method 1.

### Step 5: Integrate the player
Follow the corresponding step in Method 1, except that the message obtained is not in json format, but a 8-byte (64-bit) timestamp.


```java
long timeStamp = byteArrayToInt(param.getByteArray(TXLiveConstants.EVT_GET_MSG));
/**
* Convert a 8-byte array into a long value
*/
public static long byteArrayToInt(byte[] byteArray) {
        byte[] a = new byte[8];
        int i = a.length - 1, j = byteArray.length - 1;
        for (; i >= 0; i--, j--) {// Copy data from the end of b (the lowest bit of an int)
            if (j >= 0)
                a[i] = byteArray[j];
            else
                a[i] = 0;// If b.length is less than 4, pad the highest bit with zeros
        }
        // Note that this is different from converting a byte array into an int in that the conversion requires converting the elements of the array into a long before doing the shift.
        // Doing the shift directly will not produce correct results, because Java takes numbers as int by default if not specified otherwise.
        long v0 = (long) (a[0] & 0xff) << 56;// &0xff converts a byte to an int without difference, preventing Java from keeping the sign bit of the high bits after the automatic type promotion.
        long v1 = (long) (a[1] & 0xff) << 48;
        long v2 = (long) (a[2] & 0xff) << 40;
        long v3 = (long) (a[3] & 0xff) << 32;
        long v4 = (long) (a[4] & 0xff) << 24;
        long v5 = (long) (a[5] & 0xff) << 16;
        long v6 = (long) (a[6] & 0xff) << 8;
        long v7 = (long) (a[7] & 0xff);
        return v0 + v1 + v2 + v3 + v4 + v5 + v6 + v7;
}
```

<h3 id="IMRest"> Step 6: Questions spreading</h3>
If you are using your own IM system to assign questions, ignore this section. If you are using Tencent Cloud IM service to do this, follow these steps:

- **1. Activate IM service**
>Activate Tencent Cloud [Instant Messaging](https://console.cloud.tencent.com/avc) service.

- **2. Configure IM service**
>Complete the initial [configuration](https://cloud.tencent.com/document/product/454/7980) following the document. Be sure to select <font color='red'>**standalone mode**</font> for integration mode.

- **3. Use [REST](https://cloud.tencent.com/document/product/269/1520) API to create a BChatRoom for question assignment**
> [REST](https://cloud.tencent.com/document/product/269/1520) The API in Tencent Cloud IM is specially designed for integration at the server end. The action of creating a group is usually triggered by your server, so the use of REST APIs is an appropriate method to perform the integration.
 >
 >**BChatRoom** is very ideal for assigning questions, because it is originally intended for system notifications, which ensures high message arrival rate and reliability.
 >
 >Use [v4/group_open_http_svc/create_group](https://cloud.tencent.com/document/product/269/1615) to create a group. For the test method, please see **How to use REST APIs at the IM background.pdf - Step 3** in the [SDK](#SDK) package.

- **4. Use [REST](https://cloud.tencent.com/document/product/269/1520) API to create an AVChatRoom for sending on-screen comments**
 >**AVChatRoom** is very suitable for sending on-screen comments in a chat room. Featuring strict dirty words filtering and frequency limitation logics, AVChatRoom is specially designed to optimize large chat room scenarios.
 >
 >Use [v4/group_open_http_svc/create_group](https://cloud.tencent.com/document/product/269/1615) to create a group. For the test method, please see **How to use REST APIs at the IM background.pdf - Step 4** in the [SDK](#SDK) package.
 >
 >The frequency for AVChatroom is limited to 40 comments/sec by default. Contact us if you want to adjust this limitation, because the bandwidth fee will be higher for more comments per sec.

- **5. Use [REST](https://cloud.tencent.com/document/product/269/1520) API to send question broadcasts in BChatRoom**
>Use [v4/group_open_http_svc/send_group_msg](https://cloud.tencent.com/document/product/269/1629)  to send messages. For the test method, please see **How to use REST APIs at the IM background.pdf - Step 5** in the [SDK](#SDK) package.


### Step 7: Message receiving and on-screen comment sending and receiving

The client uses IM SDK to receive messages or send and receive on-screen comments. The integration steps are as follows.
- **1. Integrate simplified IMSDK**
Simplified IMSDK is in [SDK](#SDK). Please see **"Integration Guide - IMSDK.pdf"** in the zip package for more information.

-  **2. Perform the integration with the source code**
The SDK package contains a source code file named **AnswerPlayIMCenter** that encapsulates simple calls to IMSDK (equivalent to sample code the integration document). The following describes the member functions in this class:

| Member functions | Role | 
|-------------|---------|
| initIMCenter | For initialization. Your IM service information with Tencent Cloud is required. | 
| loginIMUser | For login. Try comparing IMSKD to a UI-less version of QQ. Just as logging in is required for receiving and sending messages with QQ, you can log in to IMSKD by simply changing the login credentials from your QQ username and login password to your Userid and UserSig issued by your server. | 
| joinIMGroup | For joining BChatRoom and AVChatRoom created by your backend server using a REST API in Step 6. | 
| sendChatMessage | For sending on-screen comments | 
| onRecvChatMessage | For receiving on-screen comments from AVChatRoom. Make sure you set a limit on the rendering frequency. <font color='red'>Do not refresh the screen every time an on-screen comment is received</font>, which would otherwise pose a huge challenge to the phone performance. This issue has been ignored by many customers because it is hard to detect owing to the relatively small number of messages during the test. | 
| onRecvIssueMessage | For receiving question messages from BChatRoom. As described in Method 2, every question should be displayed with an international NTP time. |

- **3. Timing of question display**
Do not display a question received by onRecvIssueMessage until the player finishes the GET_MESSAGE callback. If the callback time is not sooner than the NTP time of the question, the question can be displayed.

- **4. How do I get a UserSig?**
A UserSig is an important information for logging into IMUser, which is like a login password in QQ. UserSigs are issued by your server using RSA asymmetric encryption, so they provide a high level of security.

 For the ways to issue a UserSig, please see [TLS Backend APIs](https://cloud.tencent.com/document/product/269/1510). For a quick debugging process, you can use a [small tool](https://mc.qcloudimg.com/static/archive/c82316423df2060bc88127bbffc88fac/archive.zip) in Windows, which allows you to start terminal logic debugging before the backend developers get involved.
 >Note: The public and private keys in the small tool are for test purposes only.





### Step 8: Developing a quiz system
Due to Tencent Cloud's position as a PaaS service provider, quiz and payment systems that are closely associated with your business are not included in our offering package, so you need to develop them by yourself.

A common solution is to collect customers' answers as HTTP(S) requests to the quiz server. You just need to get prepared to deal with surges in highly concurrent requests.

Some customers may ask whether the IM system can be used to do the quizzes. The answer for now is no, because the IM system is good at spreading messages, while the aim of doing quizzes is to collect information.


### Step 9: Displaying quiz result
The quiz will be closed after the questions are displayed for a while. Then the quiz system will gather the results and deliver them to the viewers. To deliver the results, you can continue to use the question spread channel in **Step 6**.



