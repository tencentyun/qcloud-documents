## 1. Background
In recent years, a growing number of personal live video platforms featuring beauty VJs and live shows emerge in the industry. According to statistics, there are nearly 1,000 online live video platforms in China with more than 300 million users. It is increasingly clear that the online live video industry has become a highly competitive industry in the market. The research report from Founder Securities Institute shows that the size of social live video market will increase from CNY 2.6 billion in 2016 to CNY 29.5 billion in 2020, with a compound annual growth rate of 83%.
With a high interactivity, this new business allows a host of individual users to become the creators of UGC by simply starting live video broadcasting on their mobile phones. The large number of platforms will inevitably lead to a fierce competition in the industry, creating vicious competitions and general chaos in the market. Some VJs even make indecent moves to seek attention by making use of regulatory loopholes. This imposes higher requirements on the regulation of live video content. However, the huge base of VJs and live rooms makes it almost impossible for a large live video platform to audit video content manually. 

## 2. Product Overview
### 2.1 Introduction
The LVB+Porn Detection integrated solution, as an important value-adding component of Tencent Cloud's LVB product, comes with a full range of auxiliary LVB features including screencap, recording, watermark, porn detection and cold backup. By combining such features with Tencent Cloud LVB's core capabilities for various stages from push SDK, transcoding, channel management, LVB CDN, playback SDK, to statistics, Tencent Cloud provides customers with one-stop VPaas (Video Platform as a Service). With flexible, fast, and high-quality LVB platform services, users can get the live video broadcasting business started quickly and keep it on track reliably, catering for the needs of various business scenarios such as personal live videos, mass-participation live videos and live games.

### 2.2 How porn detection works
Tencent Cloud's LVB porn detection can identify the live streams involving pornographic content, deliver the results to users and present the results on the porn detection management platform. To put it simply, it is about capturing screenshots of live streams at a certain frequency and then using the Cloud Image system to determine whether the screenshots contain pornographic content. Any live stream with screenshots containing pornographic content will be considered as a pornographic live stream. The extent to which the live stream involves pornography is determined based on the number of screenshots with pornographic content and the pornographic level, and then be quantified as a value to be displayed on the porn detection platform.	

### 2.3 Key advantages
The key advantages of the LVB+Porn Detection integrated solution include the following:
* It is powered by the industry-leading porn detection technology, which is built on Tencent's years of technical expertise and capabilities in audio/video and image processing, including 100 million-level daily average playbacks of Tencent Video, QQ audio/video chat, and million-level daily concurrent peak for hundreds of millions of images uploaded to Qzone;
* Provide a solution integrating real-time capturing of live stream screenshots and real-time porn detection;
* Large-scale (over 120,000) distributed transcoding-based screenshot cluster; semantic analysis of 100,000 sensitive words based on malicious motives, which helps decrease the on-screen comments involving porn and prostitution by 90%;
* High detection rate: A detection rate of 95% is ensured, which means 95 out of 100 porn images can be detected. If false acceptance rate is 5%, it means that 5 out of 100 non-porn images are allowed to be identified as porn images. This greatly reduces the workload required for manual audit.

### 2.4 Application scenarios 	
It can be used in any application scenarios where porn detection of live video screenshots is required, including live games, live shows, ILVB, video portals, and education/finance live videos. In order to ease the heavy workload of manual audit for live video platforms, an automatic and intelligent approach to content audit and porn detection is needed to detect and respond to suspicious live rooms in real time by capturing screenshots of channels and calling API for intelligent porn detection.
## 3. Integration Procedure
**How to integrate porn detection feature**

1. (1) Register a Tencent Video Cloud account
       Link to Tencent Cloud official website: https://cloud.tencent.com/
       
   (2) If necessary, create a collaboration account for joint management. Go to **User Center** -> **Project Management** -> **User and Permissions** to create a policy and project group.
   
   ![](//mc.qcloudimg.com/static/img/8427faa2f38459402cf3887d47c97403/image.png)
   
2. Go to the Console, and select LVB or ILVB in the cloud products.

![](//mc.qcloudimg.com/static/img/df1f28d22e12396946e2e210981d9b8e/image.png)
   
3. Apply for activating LVB or ILVB.

  ![](//mc.qcloudimg.com/static/img/9cdfcd6cefc295c77997e19ef11bf240/image.png)
  
4. After the LVB permission is enabled, configure the screencap and porn detection features. For more information on the configuration process, please see "4.1 Console" in this document.

5. Register an account on porn detection management platform, and log in using the QQ number registered on the console.
  Link: http://jh.live.qcloud.com
  
6. Manage and process videos on the platform. For more information, please see "4.2 LVB Porn Detection Management Platform" in this document.


## 4. Overview of Product Interface
### 4.1 Console
#### 4.1.1 Screencap&Porn Detection configuration page
![](//mc.qcloudimg.com/static/img/c106f874195ac9cd3e4b08c7e77af702/image.png)

 In the Screencap&Porn Detection configuration page, you can set screencap and porn detection features by clicking the enabling button of **Screencap Settings** or **Porn Detection Settings**.
Please note that you must enable screencap before you can enable porn detection. This is because porn detection is based on the screenshots captured with screencap feature. Screencap feature can be enabled independent of porn detection.
#### 4.1.2 Screencap Settings page
![](//mc.qcloudimg.com/static/img/3929b0e5d7641a49506bd9a51575ff2d/image.png)
* Enabling button: Click **Enabled** to enable the screencap feature. Click this button again to disable the feature.
* Retention Period of Screenshots: Screenshots are usually used for keyframe editing, video cover and porn detection. In these scenarios, it is not necessary to store images for a long time. A policy of deleting images regularly is configured for LVB, with the default retention period of screenshots being 15 days. This means the screenshots are deleted automatically when the period expires. You can also contact video cloud service personnel to store your screenshots for a longer period at backend.
* Screencap Frequency: This is the interval at which screencap is performed. Only 10s is supported.
* Screencap callback URL: The information about screencap is sent to you via the configured screencap callback URL.

***Note: Screenshots are captured only for the streams which are pushed after the screencap feature is enabled in the console. Be aware of this to avoid impact on your business.***


#### 4.1.3 Porn Detection Settings page
![](//mc.qcloudimg.com/static/img/b73c7d9a1510be732a4a576619212f81/image.png)
* Enabling button: Click **Enabled** to enable the porn detection feature. Click this button again to disable the feature.
* Porn Detection Callback URL: The information about porn detection is sent to you via the configured porn detection callback URL.
* Operation callback address: The information about your operation is sent to you via the configured operation callback URL (when you perform operations such giving warning, interrupting stream or blocking account on the LVB porn detection management platform, the platform automatically calls the API to send the information about the operation you performed to this callback URL).
* secretId: Identify the API caller.
* secretKey is a key used for signature string encryption and signature string verification by the server.


### 4.2 LVB porn detection management platform
Tencent Cloud LVB Porn Detection Management Platform is a comprehensive porn detection platform which ensures accurate porn detection results by relying on Tencent Cloud's powerful backend technology. It gives detailed insight into porn detection with a full range of features to cater for the needs of customers for multi-dimensional presentation and management of porn detection. The well-organized page layout offers a more user-friendly experience.

Link: http://jh.live.qcloud.com

#### 4.2.1 What the platform looks like
1. Layout of main page
You can log in to the platform using either the main account or collaborative account. **Sorting**, **Viewing Options**, **Rotate Left**, **Rotate Right**, **Search** and other features are available at the top of the page. The live video streams are displayed in the middle of the page, and the total number of live video streams and the number of monitored streams are shown at the bottom.

![](//mc.qcloudimg.com/static/img/c584d5fa539c32c0525f2fd9582c995c/image.png)

2. Manual porn detection
The LVB porn detection management platform presents live video streams to administrators for porn detection. A single customer may have several collaborative accounts. To reduce workload and avoid repeated porn detection for the same stream, the management platform uses locking mechanism for the video streams that are already displayed. To put it simply, when an account is logged in, the live video streams displayed under this account will be locked and cannot be viewed by other collaborative accounts. When another collaborative account is logged in, the platform just selects the streams that have not been viewed at the backend. This ensures that any stream will only be viewed by one account holder for porn detection and will not go through porn detection repeatedly.

3. Display of porn detection on the platform
The value in the upper left corner of each video stream indicates the degree to which the stream involves porn. A smaller value means a higher appropriateness. When the video is counted as porn, the background of the value box changes from green to red.
The streamid and popularity value of this stream are shown at the bottom. Each stream has a unique streamid, and the popularity value indicates how many users are watching the stream.

![](//mc.qcloudimg.com/static/img/474f31552e37c7a7bd8276090293e469/image.png)

4. Display of porn detection for a single LVB stream
For a live video stream that needs special attention, click on the white area where the streamid and popularity value are located. A new tab page is opened to display the stream separately. The live video stream is shown on the left of the page, and the details of the stream and related features are shown on the right.

![](//mc.qcloudimg.com/static/img/987d73ae3334f2de607586904920bea4/image.png)

#### 4.2.2 Feature management
1. Page up and down feature
A page can only accommodate a limited number of video streams. To view the remaining video streams, click the Page Down button to go to the next page. A new tab page will open so that the opened video stream cannot be overridden.

2. Sort feature
Live video streams can be sorted in two ways: sorting by suspiciousness (default) or by popularity in descending order. This makes it easier for you to manage streams based on different dimensions.

![](//mc.qcloudimg.com/static/img/afe6b4a9e925c5063a541d4f4b25edb9/image.png)

3. View feature
You can view live video streams by video or by image.	

![](//mc.qcloudimg.com/static/img/55a314aef0a03fa596b281b48ef2d7f9/image.png)

4. Search feature
You can search for video streams quickly by streamid.

#### 4.2.3 Browser limits

Browsers have restrictions on long links. If you use Chrome, for the FLV playback protocol, the LVB porn detection management platform can open up to 6 video streams, which does not affect the user experience.
**1. HLS playback protocol**
If HLS playback protocol is used, there is no limitation on browser on the porn detection management platform.
**2. FLV playback protocol**
If the playback protocol is an FLV, use Firefox browser as Firefox can modify the parameters to control the number of links, but Chrome cannot.
Parameter modification method:
Enter "about:config" in the address bar of Firefox, and then search and modify the following two configuration items:
network.http.max-persistent-connections-per-server and network.http.max-persistent-connections-per-proxy

## 5. Conclusion
Tencent Cloud's integrated LVB screencap and porn detection services give users a full range of value-added capabilities including live stream screencap and content audit and allow the flexible integration of these capabilities with the existing live video platforms and mobile applications, enabling users in various industries such as personal live videos, live games, video portal, online education, and social applications to achieve high-quality and controllable live video broadcasting.

