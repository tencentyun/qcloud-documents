Tencent Cloud VOD provides iOS upload DEMO for the scenario of uploading videos on the iOS platform. For more information about upload process, please see [Upload Videos on Client](/document/product/266/9219).

## Download Source Code
You can update [iOS upload demo+source code](http://ugcupload-1252463788.file.myqcloud.com/LiteAVSDK_UGC_Upload_iOS.zip) on the Tencent Cloud official website.
You can see the TXUGCUploadDemo directory after decompressing the downloaded zip file. Publishing-related source code is located in TXUGCUploadDemo/upload.

## Integrate Upload Library and Source Code

1. Copy the upload source code directory TXUGCUploadDemo/upload to your project directory.
2. Import dynamic libraries QCloudCore.framework and QCloudCOSXML.framework (under TXUGCUploadDemo directory) to your project, and add the following dependent libraries:

    ```
    1.CoreTelephony
    2.Foundation
    3.SystemConfiguration
    4.libstdc++.tbd
    ```
    
3. Set Other Linker Flags in Build Settings, and add parameter ***-ObjC***

## Simple Upload of Video

### Initialize an upload object

```objc
TXUGCPublish   *_videoPublish = [[TXUGCPublish alloc] initWithUserID:@"carol_ios"];
```

### Set callback for the upload object

```objc
_videoPublish.delegate = self;
#pragma mark - TXVideoPublishListener
-(void) onPublishProgress:(NSInteger)uploadBytes totalBytes: (NSInteger)totalBytes
{
    self.progressView.progress = (float)uploadBytes/totalBytes;
    NSLog(@"onPublishProgress [%lld/%lld]", uploadBytes, totalBytes);
}

-(void) onPublishComplete:(TXPublishResult*)result
{
    NSString *string = [NSString stringWithFormat:@" upload completed; error code [%d]; message [%@]", result.retCode, result.retCode == 0? result.videoURL: result.descMsg];
    [self showErrorMessage:string];
    NSLog(@"onPublishComplete [%d/%@]", result.retCode, result.retCode == 0? result.videoURL: result.descMsg);
}
```

### Construct the upload parameters

```objc
TXPublishParam *videoPublishParams = [[TXPublishParam alloc] init];

videoPublishParams.signature  = @"xxx";
videoPublishParams.videoPath  = self.uploadTempFilePath;
```
>For rules on computing signature, see [Upload Signature of Client](/document/product/266/9221).

### Call upload

```objc
[_videoPublish publishVideo:videoPublishParams];
```

## Advanced Features
### Upload cover

Include the cover image in the upload parameters.

```objc
TXPublishParam *videoPublishParams = [[TXPublishParam alloc] init];
videoPublishParams.signature  = @"xxx";
videoPublishParams.coverImage = [[UIImage alloc] initWithCGImage:imgRef];
videoPublishParams.videoPath  = self.uploadTempFilePath;
```

### Cancel and resume upload

To cancel an upload, call `canclePublish()` of `TXUGCPublish`.

```objc
[_videoPublish canclePublish];
```

To resume an upload, call `publishVideo` of `TXUGCPublish` again using the same upload parameters, with video and cover paths unchanged.

### Resume upload from breakpoint

VOD supports resuming upload from breakpoint. When an upload is interrupted unexpectedly, you can upload the file again from the point where the upload is interrupted to avoid repeated upload. The validity period for resuming upload from breakpoint is one day. If an interrupted upload is resumed within one day after the interruption, it is resumed from the breakpoint. If it is resumed after one day, the video is uploaded from scratch by default.
`enableResume` in the upload parameters is the switch for resuming upload from breakpoint. It is enabled by default.

## API Description

Initialize upload object `TXUGCPublish::initWithUserID`

| Parameter Name | Description | Type | Required |
| ------ | ------------------ | --------- | ---- |
| userID | User ID used to identify different users | NSString* | No |

Upload `TXUGCPublish.publishVideo`

| Parameter Name | Description | Type | Required |
| ----- | ---- | --------------- | ---- |
| param | Publish parameter | TXPublishParam* | Yes |

Upload parameter `TXPublishParam`

| Parameter Name | Description | Type | Required |
| ------------ | ---------------------------------- | --------- | ---- |
| signature | [Upload Signature of Client](/document/product/266/9221) | NSString* | Yes |
| videoPath | Path of local video file | NSString* | Yes |
| coverImage | Cover image. It can be left empty | UIImage* | No |
| enableResume | Whether to resume upload from breakpoint. It is enabled by default | BOOL | No |


Set upload callback `TXUGCPublish.delegate`

| Member Variable Name | Description | Type | Required |
| -------- | ----------- | ---------------------- | ---- |
| delegate | Listen in the upload progress and result callback | TXVideoPublishListener | Yes |


Progress callback `TXVideoPublishListener.onPublishProgress`

| Variable Name | Description | Type |
| ----------- | -------- | --------- |
| uploadBytes | Uploaded bytes | NSInteger |
| totalBytes | Total bytes | NSInteger |

Result callback `TXVideoPublishListener.onPublishComplete`

| Variable Name | Description | Type |
| ------ | ---- | ---------------- |
| result | Upload result | TXPublishResult* |

Upload result `TXPublishResult`

| Member Variable Name | Description | Type |
| -------- | --------- | --------- |
| retCode | Result code | int |
| descMsg | Error description of failed upload | NSString* |
| videoId | VOD file ID | NSString* |
| videoURL | Address where the video is stored | NSString* |
| coverURL | Address where the cover is stored | NSString* |


## Error Codes

The SDK listens in the video upload status via `TXVideoPublishListener`. Therefore, you can check the video publishing status with the `retCode` in `TXPublishResult`.

| Status code | Constant in TVCCommon | Description |
| :--: | :---------------------------- | :-------------- |
| 0 | TVC_OK | Uploaded successfully |
| 1001 | TVC_ERR_UGC_REQUEST_FAILED | Request for upload failed. This is usually caused by expired or invalid signature of client. You need to apply for a signature again for the App |
| 1002 | TVC_ERR_UGC_PARSE_FAILED | Failed to parse the request information |
| 1003 | TVC_ERR_VIDEO_UPLOAD_FAILED | Failed to upload video |
| 1004 | TVC_ERR_COVER_UPLOAD_FAILED | Failed to upload cover |
| 1005 | TVC_ERR_UGC_FINISH_REQ_FAILED | Request for ending upload failed |
| 1006 | TVC_ERR_UGC_FINISH_RSP_FAILED | An error occurred with the response to ending upload |
| 1008 | TVC_ERR_FILE_NOT_EXIST | The file to be uploaded does not exist |
| 1012 | TVC_ERR_INVALID_SIGNATURE | Signature for uploading video is empty |
| 1013 | TVC_ERR_INVALID_VIDEOPATH | The video file path is empty |
| 1017 | TVC_ERR_USER_CANCLE | User calls the API to cancel upload |

