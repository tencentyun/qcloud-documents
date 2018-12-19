## Overview

As end users demand more for personalization, simple text interaction can no longer satisfy their needs in sharing contents. Tencent Cloud VOD allows users to upload video files stored in clients directly onto the cloud, while providing seamless integration with other business features of VOD service, including transcoding, screenshot, hotlink protection.

## Upload Process

![](//mc.qcloudimg.com/static/img/1cb47b70ba7ab12ddf161f9576ca6849/image.png)

The diagram above described the client upload process, which mainly includes four participants: the client, the App server, Tencent Cloud Video On-Demand system (VOD) and Tencent Cloud Object Storage system (COS). Each step in the diagram will be described in details below.

### Step 1: Client Acquires Upload Signature From App Server

Before the client uploads files to Tencent Cloud, VOD needs to verity if App server has granted permission for the upload operation. Thus, the client must first acquire upload signature from the App server and transmit it to VOD when requesting for upload information. VOD verifies the signature and allows client to proceed with the upload process only if the signature is verified as "valid".

For more information on how App server generates signatures, please see [Client Upload Signatures](/document/product/266/9221).

***Note***: ***DO NOT*** expose secret keys (Secret ID and Secret Key) to clients as this can cause serious security breaches. API secret keys should be kept by App servers only.

### Step 2: Client Initiates Upload Process to VOD

Before the client uploads files to COS, it needs to acquire information such as the target COS Bucket and path. The client initiates upload operation to VOD and acquire information required to upload files to COS. VOD assigns upload information to the client once it verifies the signature as valid.

When the client requests for upload information, it can choose to upload the video only (only request for upload information of the video file) or upload both video and cover image (request upload information for both the video file and cover image file).

### Step 3: Client Uploads Files to COS

The client calls the COS uploading API to upload files based on the upload information acquired when initiating the upload operation.

### Step 4: Client Confirms Upload Process with VOD

Once the client successfully uploads files to COS, it needs to initiate a confirmation request to VOD. Upon receiving the upload confirmation request, VOD returns video information (such as fileId, playback address, cover image address (if available) and so on) and process the videos according to user request. For example, transcoding, applying watermarks, taking screenshots, etc.

## Upload Method

### SDK

Cloud VOD service provides SDKs for different platforms to make it easier for users to develop their client upload features:

* [Android SDK](/document/product/266/9237)
* [iOS SDK](/document/product/266/9238)
* [Web SDK](/document/product/266/9239)

The SDKs encapsulate detailed elements used for clients to interact with VOD and COS. You can simply call a single API in the SDK to complete everything in step 2 - step 4 in the upload process. Thus it is recommended that users integrate the SDK provided by VOD service in their Apps to realize client uploading.
