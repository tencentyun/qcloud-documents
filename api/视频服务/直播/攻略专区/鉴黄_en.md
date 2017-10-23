## 1. Background
Recently there has been a spurt of individual LVB platforms that focus on webcam girl shows. According to statistics, there are currently about 1000 of these platforms, and their users combined have exceeded 300 million. There have been more and more indications that LVB has become one of the fastest growing industries. According to Founder Securities' report, the market size of social LVB is projected to increase from 2.6 billion CNY in 2016 to 29.5 billion CNY in 2020, with an annual compound growth rate of 83%.
On these highly interactive LVB platforms, many individual users have become creators of UGC contents. Now, LVB simply requires a phone. In this market environment, intense, chaotic, or even malicious competition is not totally unexpected. For example, to attract viewers, some VJs make suggestive, or even inappropriate moves. This situation poses a challenge for LVB content regulation. Because there are numerous VJs and live rooms, it's hardly possible for a large LVB platform to manually review all the contents. 

## 2. About the Product
### 2.1 Product Overview
LVB Porn Detection Integrated Solution is an important value-added service of Tencent LVB Product. It offers integrated LVB features such as screenshot, screencap, watermark, porn detection and cold backup. Together with Tencent Cloud LVB's core components such as push SDK, transcoding, channel management, LVB SDK, playback SDK and statistics, Tencent Cloud offers integrated VPaaS (Video Platform as a Service) service to customers. With Tencent's flexible, fast and high-quality LVB platform, fast deployment of stable and fast LVB applications such as personal, universal and game LVB is now possible.

### 2.2 How Porn Detection Works
Tencent Cloud Porn Detection can detect adult contents in LVB streams, and report to the porn detection management platform. Simply put, the feature takes screenshots of LVB streams at a certain interval, and calls YouTu system to identify adult contents in the screenshots. If the screenshots are identified as adult contents, the corresponding LVB streams will be labeled as inappropriate. Furthermore, based on the number of screenshots that are identified and how revealing they are, a quantified value indicating the inappropriate level of an LVB stream is computed and shown intuitively on the porn detection platform.	

### 2.3 Core Advantages
Tencent Cloud LVB porn detection has the following competitive advantages:
* Tencent has accumulated strong media and image processing experience and expertise in its many businesses, including Tencent Video, which supports hundreds of millions of daily video playbacks; QQ video chat; Qzone, which has hundreds of millions of daily image uploads, concurrently peaking at millions. In sum, Tencent has the leading porn detection technology in the industry.
* Real time screenshot and real time porn detection integrated solution;
* Large distributive transcoding and screenshot clusters with over 120,000 nodes. With sensitive word database that contains 100 thousand words, reducing adult and prostitution comments by 90%;
* High accuracy: the recognition rate is as high as 95%. That is, 95 out of 100 adult images could be successfully detected; the false negative rate is 5%, i.e. at most 5 normal images would be identified as adult images out of 100. The pressure on manual review is significantly relieved.

### 2.4 Application Scenarios 	
The service could be used in any application scenario that requires porn detection, such as game, beauty show, interactive, eduction and financial LVB, as well as video websites. The service is able to reduce the workload for manual review on LVB platforms by using its automatic and intelligent content reviewing and porn detection mechanism, taking real time screenshots of channels and calling porn detection APIs to identify suspicious live rooms and react in time.
## 3. Interfacing Process
**Porn detection interfacing process**

1. (1) Register a Tencent Video Cloud account
       Tencent Cloud official website: https://cloud.tencent.com/
       
   (2) Create collaborator accounts for co-management if needed. Create policy and project groups in "User Center" -> "Project Management" -> "Users and Permissions".
   
   ![](//mc.qcloudimg.com/static/img/8427faa2f38459402cf3887d47c97403/image.png)
   
2. Enter Management Center, select LVB product or ILVB product.

![](//mc.qcloudimg.com/static/img/df1f28d22e12396946e2e210981d9b8e/image.png)
   
3. Apply to enable LVB or ILVB service.

  ![](//mc.qcloudimg.com/static/img/9cdfcd6cefc295c77997e19ef11bf240/image.png)
  
4. After the application is approved, configure screenshot porn detection. For detailed process, see section 4.1 Management Center in this document.

5. Register and log in to the porn detection management platform (use the same QQ you registered in the console).
  Link: http://jh.live.qcloud.com
  
6. Manage videos on the platform. For detailed process, see section 4.2 Porn Detection Management Platform in this document.


## 4. Product Interface
### 4.1 Management Center
#### 4.1.1 Screenshot Porn Detection Configuration Page
![](//mc.qcloudimg.com/static/img/c106f874195ac9cd3e4b08c7e77af702/image.png)

 In screenshot porn detection edit page, click the "Enable" button in screenshot configuration or porn detection configuration to configure the feature.
Note that since porn detection relies on screenshot, the latter must be enabled when screenshot is already enabled before. You may enable screenshot on its own.
#### 4.1.2 Screenshot Configuration Page
![](//mc.qcloudimg.com/static/img/3929b0e5d7641a49506bd9a51575ff2d/image.png)
* Enable the feature: click on the button to enable screenshot feature. Click on it again to disable.
* Screenshot retention time: screenshots are typically used to edit keyframes, used as video cover images, in porn detection scenarios and so on. These scenarios usually do not require permanent storage of the images. Therefore the LVB cloud employs a periodical deletion strategy: by default, images are deleted after 15 days. To store the screenshots longer, you can contact your Video Cloud co-workers and achieve longer screenshot retention time once your request is approved.
* Screenshot interval: the interval at which screenshots are taken. Currently 10s is the only supported option.
* Screenshot callback address: information about screenshots is reported to you through this callback address.

***Note: Screenshots are only generated for new streams after you enabled screenshot feature in Management Center. Previous streams will not generate any screenshots regardless of their push status. Keep this in mind to avoid affecting your business.***


#### 4.1.3 Porn Detection Configuration Page
![](//mc.qcloudimg.com/static/img/b73c7d9a1510be732a4a576619212f81/image.png)
* Enable the feature: click on the button to enable porn detection feature. Click on it again to disable.
* Porn detection callback address: results of porn detection is reported to you through this callback address.
* Operation callback address: Information about related operations is reported to you through this callback. (When you perform warning, stream blocking and account banning operations in the porn detection management platform, the platform will call the API and report related operation information to this callback address.)
* secretId: used to identify the API caller
* secretKey: a private key used to encrypt signature string, and is also used by the server to verify signature string.


### 4.2 LVB Porn Detection Management Platform
Tencent Cloud LVB porn detection management platform provides comprehensive services. It yields accurate detection results relying on Tencent Cloud's powerful backend technology; it displays porn detection information in multiple vectors using its comprehensive features, to satisfy different presentation and management demands for customers; it offers superb user experience with its intuitive user interface.

Link: http://jh.live.qcloud.com

#### 4.2.1 Platform Introduction
1. Interface
You can use either the main account or the collaborator account to log in. On the upper part of the platform interface are features such as "sort", "viewing mode", "rotate left", "rotate right", search and so on, as shown below. Customers may use the features as needed. The middle is the ongoing video stream, and the bottom shows the total number of LVB streams and the number of those under monitoring.

![](//mc.qcloudimg.com/static/img/c584d5fa539c32c0525f2fd9582c995c/image.png)

2. Manual Porn Detection
LVB cloud porn detection management platform displays LVB streams for manual review. A customer may have multiple collaborator accounts. To prevent the same LVB stream from being monitored by multiple workers, the management platform implemented a lock mechanism to ongoing video steams. Simply put, LVB streams displayed to an account are locked upon account login, other collaborator accounts cannot view these streams. When other collaborator accounts log in, the platform will only call LVB streams that are not yet viewed to ensure that each stream is only viewed and monitored by one account holder and that no stream is monitored twice.

3. Porn Detection Display
The value at the upper-left corner indicates the inappropriate level of the video stream. A lower value means a more legitimate video. The underframe of the value turns from green to red if the content is identified as adult.
The streamid and popularity are shown below a stream. Each stream has a unique streamid, and popularity indicates how many terminal users are viewing the video.

![](//mc.qcloudimg.com/static/img/474f31552e37c7a7bd8276090293e469/image.png)

4. Individual LVB Stream Presentation
For LVB streams that require special attention, you can click on the white area where streamid and popularity are shown to open a separate browser tab to monitor the stream individually. The ongoing video stream is displayed on the left of the page, while relevant details of the stream and operation control are located on the right.

![](//mc.qcloudimg.com/static/img/987d73ae3334f2de607586904920bea4/image.png)

#### 4.2.2 Operations
1. Pages
Streams can't fit into a single page, use the "next page" button to go to the next page. To preserve opened streams, the platform will open a new tab to display the new page.

2. Sorting
There are two sorting options: descending order by suspicion level (default) and descending order by viewer count. Customers can conveniently manage LVB streams from different angles.

![](//mc.qcloudimg.com/static/img/afe6b4a9e925c5063a541d4f4b25edb9/image.png)

3. Viewing Mode
There are two viewing modes: video mode and image mode.	

![](//mc.qcloudimg.com/static/img/55a314aef0a03fa596b281b48ef2d7f9/image.png)

4. Searching
Customers can find a video stream quickly by searching its streamid.

#### 4.2.3 Browser Restriction

Some browsers restrict the number of concurrent persistent connections. For example, Chrome allows at most 6 concurrent FLV video streams, severely affecting the user experience of LVB porn detection management platform.
** 1. HLS Playback Protocol**
For HLS protocol, the platform has no special requirements on browser.
** 2. FLV Playback Protocol**
For FLV protocol, it's recommended to use Firefox browser. Unlike Chrome, you can configure the number of concurrent connections on Firefox.
Changing parameter:
Enter "about:config" in Firefox's address bar, search and modify the following two options:
network.http.max-persistent-connections-per-server and network.http.max-persistent-connections-per-proxy

## 5. Conclusion
With Tencent Cloud LVB Screenshot Porn Detection Integrated Service, users can leverage comprehensive integrated service system to quickly access LVB screenshot, content review and other important value-added services as well as integrate these services into existing LVB platforms and mobile Apps. Personal LVB, game LVB, video website, online eduction, social Apps... Users can have access to quality, manageable LVB services no matter which industry they're from.

