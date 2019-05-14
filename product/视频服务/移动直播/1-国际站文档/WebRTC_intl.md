
<h2> Viewing Demo </h2>

Open the [experience URL](https://sxb.qcloud.com/miniApp/#/) with Chrome to use the video chat feature of Chrome (WebRTC) + WeChat (Mini Program), as shown below:

![](https://main.qcloudimg.com/raw/81edf044e0a40ccfd4794b91185f1f82.jpg)

## Source Code Debugging

### Client
Click [webrtc(Chrome).zip](https://github.com/TencentVideoCloudMLVBDev/webrtc_pc) to download the source code for PC. This page can only be opened in a browser that supports WebRTC:

| Directory | Description | 
|:-------:|---------|
| index.html | Demo home page | 
|  vue |  vue frame code | 
| third | Third-party js file | 
| component | Main business logics of the demo page are located in js files under the folder | 

### Server
Click [webrtc_server_list.zip](https://github.com/TencentVideoCloudMLVBDev/webrtc_server_java)  to download server-end source code of **Java** version. This code is mainly used to implement a simple (unauthenticated) room list, to support features such as creating or closing a chat room. This code can be ignored if you just want to enable a video call (hard-code a roomid in Chrome and Mini Program end respectively). 

| Directory | Description | 
|:-------:|---------|
| README.pdf | Describes how to use this backend code | 
| Backend API table.pdf | Provides a detailed description on how to implement this backend code internally | 
| src | Backend room list source code of java version | 

## How to Integrate
The following figure describes how to integrate WebRTC solution to your existing business system:
![](https://main.qcloudimg.com/raw/6670541d971f3a133027342b29265aaf.png)

### Step 1: Build a business server
The business server is mainly used to send userid, usersig, roomid, privateMapKey and other information required to implement a video chat to PC Web pages and WeChat mini programs. The roomid and userid can be specified by your business backend. You must ensure that these IDs cannot overlap with each other. For more information on how to calculate the usersig and privateMapKey, please see sample code [(java | PHP)](https://cloud.tencent.com/document/product/454/7873#Server).
 
### Step 2: Integrate with Chrome
Although Google has provided many documents and tutorials on how to use WebRTC, the official documents are too flexible to understand. Tencent Cloud has introduced a simplified encapsulated API. For more information on how to integrate WebRTC to Chrome end by just calling several functions, please see Tencent Cloud [WebRTC API](https://cloud.tencent.com/document/product/647/16865) .

### Step 3: Integrate Mini Program-end code
WeChat version 6.6.6 supports interconnection with WebRTC. For more information on how to implement a mini program that support WebRTC video chat, please see [**&lt;webrtc-room&gt;**](https://cloud.tencent.com/document/product/454/16914) .



