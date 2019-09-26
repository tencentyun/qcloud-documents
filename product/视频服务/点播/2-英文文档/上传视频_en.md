Tencent Cloud VOD console provides two video uploading methods: Web-based upload and video pulling.
## Web-based Upload
The Web-based Upload is to upload videos to the VOD service locally. The detailed operation process is as follows:
### 1. Log in to VOD Console
Log in to Tencent Cloud [VOD Console](https://console.cloud.tencent.com/vod), and click "Web-based Upload" in the left menu bar to go to the Web-based upload page.
![](https://mc.qcloudimg.com/static/img/73c9c8cc59307393826f0332bd03eb62/image.png)

### 2. Upload Video
Click the "Add File to Upload" button in the upper right corner, and in the **Upload Video** pop-up window, click "Add Video", select the local video file to be uploaded, and click the "Open" button after confirmation.
![](https://mc.qcloudimg.com/static/img/dac32bf3056217e31e5e95a614d1b7b7/image.png)
You can configure **Video Name** and **Video Category**, and determine whether the **Use Watermark** feature is enabled for video files uploaded this time. If enabled, the videos will be added with default watermarks in the process of video transcoding. After checking the information, click "Start Upload".
![](https://mc.qcloudimg.com/static/img/ceb27e3a013b850eb7a0684ca2775c26/image.png)
It may take a few minutes for the video to be uploaded, and you can check upload progress in the upload list.
In the process of upload, you can delete the upload task. When upload is completed, the files are automatically transcoded based on the transcoding settings in the "Global Settings".
If you want to upload other videos, click "Add File to Upload" to upload other video files.
![](https://mc.qcloudimg.com/static/img/ec41280c9557e1f89f1231d12f8c86fc/image.png)
>**Note: **In the uploading process, you can switch to other pages of the VOD console, but make sure not to close your browser to access other console products, otherwise the upload will be interrupted. Web-based upload supports resuming from break point, and upload in queue. You're recommended to use the Chrome browser.

### 3. Complete Video Upload
You can click "Video Management" in the left menu bar to view and manage successfully uploaded videos on the Cloud Video Management page. For more information, please see [Video Management](https://cloud.tencent.com/document/product/266/14054).
![](https://mc.qcloudimg.com/static/img/d7e98e0377583d5a4e57fbb1c7d148ff/image.png)

## Video Pulling
Video pulling is to directly pull source videos from online websites as shown below:
### 1. Log in to VOD Console
Log in to Tencent Cloud [VOD Console](https://console.cloud.tencent.com/vod), and click "Video Pulling" in the left menu bar to go to the video pulling page.
![](https://mc.qcloudimg.com/static/img/a7dc37df0b257b54edff97c808bbe5b4/image.png)

### 2. Pull Source Video
In the input box, enter the content of the source video to be pulled, with one entry of pulling content in one row. It may take a few minutes for the video pulling to complete, and you can check pulling progress in the video pulling list.
		Format: `video URL, video name, MD5, priority`. MD5 and priority (high/medium/low) are optional. Here are examples:
>Example 1: `http://www.demo.com/1.mp4, Voice of Asia 01, aa81600as44645es543654454wqw, high`
Example 2: `http://www.demo.com/1.mp4, Voice of Asia 02, aa81600as44645es543654454wqw`
Example 3: `http://www.demo.com/1.mp4, Voice of Asia 03`

If you have already configured transcode format on the [Global Settings](https://cloud.tencent.com/document/product/266/14058) page, the transcode process will start automatically when the video is successfully pulled.
If the URL used to pull video already exists in the history, please clear the task history first.

### 3. Complete Video Pulling
You can click "Video Management" in the left menu bar to view and manage successfully pulled videos on the Cloud Video Management page. For more information, please see [Video Management](https://cloud.tencent.com/document/product/266/14054).
![](https://mc.qcloudimg.com/static/img/d7e98e0377583d5a4e57fbb1c7d148ff/image.png)



