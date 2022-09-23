Tencent Cloud VOD provides Android upload DEMO for the scenario of uploading videos on the Android platform. For more information about upload process, please see [Upload Videos from Client](/document/product/266/9219).

## Download Source Code

You can update [Android upload demo+source code](https://liteav.sdk.qcloud.com/download/ugc/LiteAVSDK_UGC_Upload_Android.zip) on the Tencent Cloud official website.
You can see the Demo directory after decompressing the downloaded zip file. Upload-related source code is located in Demo/app/src/main/java/com/tencent/ugcupload/demo/videoupload.

## Integrate Upload Library and Source Code

1. Copy the upload source code directory Demo/app/src/main/java/com/tencent/ugcupload/demo/videoupload to your project directory, but the package name needs to be modified manually.
2. Integrate all the jar packages under directory Demo/app/libs/upload into your project. Keep the upload directory structure so that you can update the library later.

Dependent libraries:

| jar file | Description |
| --------------------------- | ---------------------------------------- |
| cos-xml-android-sdk-1.2.jar | File upload package of Tencent Cloud COS. This component is used for uploading videos (TXUGCPublish) |
| qcloud-core-1.2.jar | File upload package of Tencent Cloud COS. This component is used for uploading videos (TXUGCPublish) |
| okhttp-3.8.1.jar | Open source HTTP component |
| okio-1.13.0.jar | Open source network I/O component |
| xstream-1.4.7.jar | Open source serialization component |
| fastjson-1.1.62.android.jar | Open source json component |

3. Some access permissions related to network and storage are required for uploading videos. The following permission declarations can be added in AndroidManifest.xml:

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

## Simple Upload of Video
### Initialize an upload object

```java
TXUGCPublish mVideoPublish = new TXUGCPublish(this.getApplicationContext(), "carol_android")
```

### Set callback for the upload object

```java
mVideoPublish.setListener(new TXUGCPublishTypeDef.ITXVideoPublishListener() {
    @Override
    public void onPublishProgress(long uploadBytes, long totalBytes) {
        mProgress.setProgress((int) (100*uploadBytes/totalBytes));
    }

    @Override
    public void onPublishComplete(TXUGCPublishTypeDef.TXPublishResult result) {
        mResultMsg.setText(result.retCode + " Msg:" + (result.retCode == 0 ? result.videoURL : result.descMsg));
    }
});
```

### Construct the upload parameters

```java
TXUGCPublishTypeDef.TXPublishParam param = new TXUGCPublishTypeDef.TXPublishParam();

param.signature = "xxx";
param.videoPath = "xxx";
```
>For the rules on computing signature, see [Upload Signature of Client](/document/product/266/9221).

### Call upload

```java
int publishCode = mVideoPublish.publishVideo(param);
```

## Advanced Features
### Upload cover

Include the cover path in the upload parameter.

```java
TXUGCPublishTypeDef.TXPublishParam param = new TXUGCPublishTypeDef.TXPublishParam();

param.signature = "xxx";
param.videoPath = "xxx";
param.coverPath = "xxx";
```
>For the rules on computing signature, see [Upload Signature of Client](/document/product/266/9221).

### Cancel and resume upload

To cancel an upload, call `canclePublish()` of `TXUGCPublish`.

```java
mVideoPublish.canclePublish();
```

To resume an upload, call `publishVideo` of `TXUGCPublish` again using the same upload parameters, with video and cover paths unchanged.

### Resume upload from breakpoint

VOD supports resuming upload from breakpoint. When an upload is interrupted unexpectedly, you can upload the file again from the point where the upload is interrupted to avoid repeated upload. The validity period for resuming upload from breakpoint is one day. If an interrupted upload is resumed within one day after the interruption, it is resumed from the breakpoint. If it is resumed after one day, the video is uploaded from scratch by default.
`enableResume` in the upload parameters is the switch for resuming upload from breakpoint. It is enabled by default.


## API Description

Initialize upload object `TXUGCPublish`

| Parameter Name | Description | Type | Required |
| --------- | ---------------------- | ------- | ---- |
| context | Context of application | Context | Yes |
| customKey | Used to identify different users. The account ID of App is recommended | String | No |

Upload `TXUGCPublish.publishVideo`

| Parameter Name | Description | Type | Required |
| ----- | ---- | ---------------------------------- | ---- |
| param | Upload parameter | TXUGCPublishTypeDef.TXPublishParam | Yes |

Upload parameter `TXUGCPublishTypeDef.TXPublishParam`

| Parameter Name | Description | Type | Required |
| ------------ | ---------------------------------- | ------- | ---- |
| signature | [Upload Signature of Client](/document/product/266/9221) | String | Yes |
| videoPath | Path of local video file | String | Yes |
| coverPath | Path of local cover file. No cover file is uploaded by default | String | No |
| enableResume | Whether to resume upload from breakpoint. It is enabled by default | boolean | No |

Set upload callback `TXUGCPublish.setListener`

| Parameter Name | Description | Type | Required |
| -------- | ----------- | ---------------------------------------- | ---- |
| listener | Listen in the upload progress and result callback | TXUGCPublishTypeDef.ITXVideoPublishListener | Yes |


Progress callback `TXUGCPublishTypeDef.ITXVideoPublishListener.onPublishProgress`

| Variable Name | Description | Type |
| ----------- | -------- | ---- |
| uploadBytes | Uploaded bytes | long |
| totalBytes | Total bytes | long |

Result callback `TXUGCPublishTypeDef.ITXVideoPublishListener.onPublishComplete`

| Variable Name | Description | Type |
| ------ | ---- | ----------------------------------- |
| result | Upload result | TXUGCPublishTypeDef.TXPublishResult |

Upload result `TXUGCPublishTypeDef.TXPublishResult`

| Member Variable Name | Description | Type |
| -------- | --------- | ------ |
| retCode | Result code | Int |
| descMsg | Error description of failed upload | String |
| videoId | VOD file ID | String |
| videoURL | Address where the video is stored | String |
| coverURL | Address where the cover is stored | String |


## Error Codes

The SDK listens in the video upload status via API `TXUGCPublishTypeDef.TXVideoPublishListener`. Therefore, you can check the video upload status with the `retCode` in `TXUGCPublishTypeDef.TXPublishResult`.

| Status code | Constant in TVCConstants | Description |
| :--: | :----------------------------- | :--------------------- |
| 0 | NO_ERROR | Uploaded successfully |
| 1001 | ERR_UGC_REQUEST_FAILED | Request for upload failed. This is usually caused by expired or invalid signature of client. You need to apply for a signature again for the App |
| 1002 | ERR_UGC_PARSE_FAILED | Failed to parse request information |
| 1003 | ERR_UPLOAD_VIDEO_FAILED | Failed to upload video |
| 1004 | ERR_UPLOAD_COVER_FAILED | Failed to upload cover |
| 1005 | ERR_UGC_FINISH_REQUEST_FAILED | Request for ending upload failed |
| 1006 | ERR_UGC_FINISH_RESPONSE_FAILED | An error occurred with the response to ending upload |
| 1007 | ERR_CLIENT_BUSY | Client is busy (Object cannot process more requests) |
| 1008 | ERR_FILE_NOEXIT | The file to be uploaded does not exist |
| 1009 | ERR_UGC_PUBLISHING | The video is being uploaded |
| 1010 | ERR_UGC_INVALID_PARAM | Upload parameter is empty |
| 1012 | ERR_UGC_INVALID_SIGNATURE | Signature for uploading video is empty |
| 1013 | ERR_UGC_INVALID_VIDOPATH | The video file path is empty |
| 1014 | ERR_UGC_INVALID_VIDEO_FILE | The video file does not exist under the current path |
| 1015 | ERR_UGC_FILE_NAME | The file name of the video to be uploaded is too long (exceeds 40 characters) or contains special characters |
| 1016 | ERR_UGC_INVALID_COVER_PATH | Invalid path of the cover of the video file. The file does not exist |

