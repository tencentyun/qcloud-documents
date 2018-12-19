## Connection Procedure
1. Register a Tencent Video Cloud account on [Tencent Cloud Official Website](https://cloud.tencent.com/). If necessary, create a collaboration account for joint management. Go to **User Center** -> **Project Management** -> **User and Permissions** to create a policy and project group.
![](//mc.qcloudimg.com/static/img/97851ddf06d431f26fa9ad34f3dabd4c/image.png)
2. Go to the management center, and select LVB or ILVB products in the cloud products.
![](//mc.qcloudimg.com/static/img/5e701408610f14b05acb608c4e1589ed/image.png)
3. Apply for activating LVB or ILVB services;
![](//mc.qcloudimg.com/static/img/2a501358e45d98e3e9b8a040b138b074/image.png)
4. After the LVB permission is enabled, configure the screencap and porn detection features. For more information on the configuration process, please see "Management Center" in this document.
5. Register an account on porn detection management platform, and **Log In**(http://jh.live.qcloud.com/) using the QQ number registered on the console.
6. Manage and process videos on the platform. For more information, please see "LVB Porn Detection Management Platform" in this document.

## Management Center
### Screencap&Porn Detection configuration page
In the Screencap&Porn Detection configuration page, you can set screencap and porn detection features by clicking the enabling button of **Screencap Settings** or **Porn Detection Settings**. Please note that you must enable screencap before you can enable porn detection. This is because porn detection is based on the screenshots captured with screencap feature. Screencap feature can be enabled independent of porn detection.
![](//mc.qcloudimg.com/static/img/3cb949e784b926c5943f59b71e6ce7b1/image.png)
### Screencap Settings page
* Enabling button: Click **Enabled** to enable the screencap feature. Click this button again to disable the feature.
* Retention Period of Screenshots: Screenshots are usually used for keyframe editing, video cover and porn detection. In these scenarios, it is not necessary to store images for a long time. A policy of deleting images regularly is configured for LVB, with the default retention period of screenshots being 15 days. This means the screenshots are deleted automatically when the period expires. You can also contact video cloud service personnel to store your screenshots for a longer period at backend.
* Screencap Frequency: This is the interval at which screencap is performed. Only 10s is supported.
* Screencap Callback Address: The information about screencap is sent to you via the configured screencap callback address.
![](//mc.qcloudimg.com/static/img/ce0c495d25ad228e764214978a89ce9c/image.png)
>**Note:**
>Screenshots are captured only for the streams which are pushed after the screencap feature is enabled in management center.

### Porn Detection Settings page
* Enabling button: Click **Enabled** to enable the porn detection feature. Click this button again to disable the feature.
* Porn Detection Callback Address: The information about porn detection is sent to you via the configured porn detection callback address.
* Operation Callback Address: The information about your operation is sent to you via the configured operation callback address (when you perform operations such as giving warning, interrupting stream or blocking account on the LVB porn detection management platform, the platform automatically calls the API to send the information about the operation you performed to this callback address).
* secretId: Identify the API caller.
* secretKey: Used for signature string encryption, and signature string verification by server.
![](//mc.qcloudimg.com/static/img/a044d936bacc9245807effa2344cd58c/image.png)

## LVB Porn Detection Management Platform
Tencent Cloud [LVB Porn Detection Management Platform](http://jh.live.qcloud.com) is a comprehensive porn detection platform which ensures accurate porn detection results by relying on Tencent Cloud's powerful backend technology. It gives detailed insight into porn detection with a full range of features to cater for the needs of customers for multi-dimensional presentation and management of porn detection. The well-organized page layout offers a more user-friendly experience.

### What the platform looks like
1. Layout of main page
You can log in to the platform using either the main account or collaborative account. **Sorting**, **Viewing Options**, **Rotate Left**, **Rotate Right**, **Search** and other features are available at the top of the page. The live video streams are displayed in the middle of the page, and the total number of live video streams and the number of monitored streams are shown at the bottom.
The main page of platform is shown as in the figure below:
![](//mc.qcloudimg.com/static/img/c584d5fa539c32c0525f2fd9582c995c/image.png)
2. Manual porn detection
The LVB porn detection management platform presents live video streams to administrators for porn detection. A single customer may have several collaborative accounts. To reduce workload and avoid repeated porn detection for the same stream, the management platform uses locking mechanism for the video streams that are already displayed. To put it simply, when an account is logged in, the live video streams displayed under this account will be locked and cannot be viewed by other collaborative accounts. When another collaborative account is logged in, the platform just selects the streams that have not been viewed at the backend. This ensures that any stream will only be viewed by one account holder for porn detection and will not go through porn detection repeatedly.
3. Display of porn detection on the platform
The value in the upper left corner of each video stream indicates the degree to which the stream involves porn. A smaller value means a higher appropriateness. When the video is counted as porn, the background of the value box changes from green to red. The streamid and popularity value of this stream are shown at the bottom. Each stream has a unique streamid, and the popularity value indicates how many users are watching the stream.
![](//mc.qcloudimg.com/static/img/474f31552e37c7a7bd8276090293e469/image.png)
4. Display of porn detection for a single live video stream
For a live video stream that needs special attention, click on the white area where the streamid and popularity value are located. A new tab page is opened to display the stream separately. The live video stream is shown on the left of the page, and the details of the stream and related features are shown on the right.
![](//mc.qcloudimg.com/static/img/987d73ae3334f2de607586904920bea4/image.png)

### Related features
1. Page Up/Down
A page can only accommodate a limited number of video streams. To view the remaining video streams, click the Page Down button to go to the next page. A new tab page will open so that the opened video stream cannot be overridden.
2. Sorting
Live video streams can be sorted in two ways: sorting by suspiciousness (default) or by popularity in descending order. This makes it easier for you to manage streams based on different dimensions.
![](//mc.qcloudimg.com/static/img/afe6b4a9e925c5063a541d4f4b25edb9/image.png)
3. Viewing Options
Two viewing options are available: Videos and Images.	
![](//mc.qcloudimg.com/static/img/55a314aef0a03fa596b281b48ef2d7f9/image.png)
4. Search
You can search for video streams quickly by streamid.

### Browser limitations
Some browsers support a limited number of long links. On a Chrome browser, the LVB porn detection management platform can open a maximum of 6 video streams when FLV playback protocol is used, which can affect the user experience.
1. HLS playback protocol
If HLS playback protocol is used, there is no limitation on browser on the porn detection management platform.
2. FLV playback protocol
If FLV playback protocol is used, Firefox browser is recommended because it can modify the parameters to control the number of links.

How to modify the parameters:
Enter `about:config` in the address bar of Firefox, then search for and modify the following two configuration items:
`network.http.max-persistent-connections-per-server` and `network.http.max-persistent-connections-per-proxy`.

Tencent Cloud's integrated LVB screencap and porn detection services give users a full range of value-added capabilities including live stream screencap and content audit and allow the flexible integration of these capabilities with the existing live video platforms and mobile applications, enabling users in various industries such as personal live videos, live games, video portal, online education, and social applications to achieve high-quality and controllable live video broadcasting.

