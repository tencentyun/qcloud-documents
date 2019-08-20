## Overview

In the age of Internet, excellent and popular video resources are becoming more and more welcomed by users. App vendors can create huge benefit for themselves if they are able to publish hot videos onto the Internet and provide them to hundreds of millions of users to view. Tencent Cloud VOD service provides powerful video management, edit and publish features which allow App vendors to publish videos to Tencent Cloud quickly and share them with high efficiency.

Tencent Cloud VOD service provides various uploading methods for different scenarios to help App vendors upload their local video resources to Tencent Cloud. Next, we'll introduce three uploading methods: console upload, server upload and client upload.

## Console Upload

Console upload means that App admin logs to the Tencent Cloud VOD console and uploads local videos into Tencent Cloud VOD system through web pages. You can enter the console upload page from [here](https://console.cloud.tencent.com/vod/webupload).

### Steps

* Click the "Add File" button and choose the local files to be uploaded in the dialog.

![Image](//mc.qcloudimg.com/static/img/67f44639beef13229348205328df0c42/image.png)

* After the files are selected, you can specify whether to apply watermarks and whether to automatically enable transcoding when the videos are uploaded.

![Image](//mc.qcloudimg.com/static/img/287a91c3df1453988c94c24b5d3401cc/image.png)

* After the videos are added, click "Upload" to start uploading the videos in the upload list into Tencent Cloud VOD system.

![Image](//mc.qcloudimg.com/static/img/b70d01343223d4b2baeb1fa0865e6321/image.png)

### Feature

This upload method is simple to perform, since the App admin only needs to log in to the Tencent Cloud VOD console page to upload videos. The admin can follow the instructions on the console page to specify video category information, whether to transcode, as well as configure and modify cover images for successfully uploaded videos.

## Server Upload

Server upload means to use APIs or SDKs provided by VOD service to upload video resources stored in App backend into Tencent Cloud VOD system.

### Steps

Server video upload includes three steps: initiate upload action to VOD, upload files to COS and confirm the upload process with VOD. For more information about each step and how to perform them, please see [Server Upload Overview](/document/product/266/9759).

![Image](//mc.qcloudimg.com/static/img/d751bf5e65346dee3a698f097ac2bfdd/image.png)

### Feature

Server upload method is a suitable approach when App needs to upload videos stored in the server into Tencent Cloud VOD system quickly and reliably. Compared to console upload, using server upload SDK does not need any manual effort from the App admin, improving publish and management efficiency.

## Client Upload

Client upload means to upload videos on the client into Tencent Cloud VOD system by using mobile device (iOS and Android) SDKs and Web SDKs provided by VOD service.

### Steps

Client upload includes four steps: acquire upload signature from App server, initiate upload action to VOD, upload files to COS and confirm the upload process with VOD. For more information about each step and how to perform them, please see [Client Upload Overview](/document/product/266/9219).

![Image](//mc.qcloudimg.com/static/img/1cb47b70ba7ab12ddf161f9576ca6849/image.png)

### Feature

Using client upload allows users to directly upload captured videos, recorded videos or downloaded videos from their mobile devices into Tencent Cloud VOD system quickly. In this way, users do not need to upload videos to the App server first and then let the server upload videos to Tencent Cloud VOD system, which simplifies the uploading process as well as saves time and upload bandwidth usage for the server.
