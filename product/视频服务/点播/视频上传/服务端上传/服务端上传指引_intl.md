## Overview

Apps collect a large number of excellent videos from various channels and may store these video resources directly in their servers. Next, the Apps will plan to further process the videos (such as transcoding, taking screenshots, applying watermarks and so on) and publish them into the Content Delivery Network (CDN), so that users can watch the videos and create profit for Apps. Tencent Cloud VOD allows users to upload video files stored in servers directly onto the cloud, while providing seamless integration with the video processing features of VOD service, including transcoding, screenshot, hotlink protection and so on.

## Upload Process

![Image](//mc.qcloudimg.com/static/img/d751bf5e65346dee3a698f097ac2bfdd/image.png)

The diagram above described the server upload process, which mainly includes three participants: the App server, Tencent Cloud Video on-demand system (VOD) and Tencent Cloud Object Storage system (COS). Each step in the diagram will be described in details below.

### Step 1: App Server Initiates Upload Operation to VOD

Before the App server uploads files to COS, it needs to acquire information such as the target COS Bucket and path. The server initiates upload operation to VOD and acquire information required to upload files to COS. VOD verifies the request from server and assigns upload information to it.

When the server requests for upload information, it can choose to upload the video only (only request for upload information of the video file) or upload both video and cover image (request upload information for both the video file and cover image file).

### Step 2: App Server Uploads File to COS

The App server calls the COS uploading API to upload files based on the upload information acquired when initiating the upload operation.

### Step 3: App Server Confirms Upload Process with VOD

Once the App server successfully uploads files to COS, it needs to initiate a confirmation request to VOD. Upon receiving the upload confirmation request, VOD returns video information (such as fileId, playback address, cover image address (if available) and so on) and process the videos according to user request. For example, transcoding, applying watermarks, taking screenshots, etc.

## Upload Method

### API

* [API for App Server to Initiate Upload Operation to VOD](/document/product/266/31767)
* [API for App Server to Upload Files to COS](/document/product/266/31784)
* [API for App Server to Confirm Upload Process with VOD](/document/product/266/31766)

### SDK

Cloud VOD service provides SDKs of different language platforms to make it easier for users to develop their client upload features:

* [PHP SDK](/document/product/266/9725)
* [Java SDK](/document/product/266/10276)

Based on Cloud Image APIs and COS, the SDKs encapsulate detailed elements used for servers to interact with VOD and COS. You can simply call a single API in the SDK to complete everything in step 1 - step 3 in the upload process. Thus ***it is strongly recommended*** that users realize server upload features for their Apps while referring to the SDK provided by VOD service.
