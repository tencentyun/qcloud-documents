## Overview
The client upload SDK for browsers can be used to upload videos and cover files to Tencent Cloud VOD system.

## Integration Method
### Development environment
* Browsers must support HTML 5 to use the SDK.
* The App server is required to distribute the upload signature for client. For information on how to generate a signature, see [Upload Signature](/document/product/266/9221).

### Integration
Introduce ugcuploader.js to the page.
```js
<script src="//imgcache.qq.com/open/qcloud/js/vod/sdk/ugcUploader.js"></script>
```

### Demo
[http://video.qcloud.com/sdk/ugcuploader.html](http://video.qcloud.com/sdk/ugcuploader.html)

## Steps for Upload
###  Step 1: Acquire upload signature
```js
var getSignature = function(callback){
    $.ajax({
        url: 'yourinterface',  //The server acquires the URL of the upload signature of client
        type: 'POST',
        dataType: 'json',
        success: function(result){
            //result.returnData.signature is the acquired signature
            callback(result.returnData.signature);
        }
    });
};

```

###  Step 2: Specify the files to be uploaded

This includes video and cover. Parameter for cover can be left empty if only video is uploaded.

| Parameter Name | Required | Type | Description |
| ------------ | ---- | -------- | --------- |
| videoFile | Yes | File | Video file to be uploaded |
| coverFile | No | File | Cover file to be uploaded |
| getSignature | Yes | Function | Callback function used to acquire signature |
| success | No | Function | Callback function for successful upload |
| error | No | Function | Callback function for failed upload |
| progress | No | Function | Callback function for upload progress |
| finish | No | Function | Callback function for upload result |

Callback functions

| Function name | Description | Parameter Type | Description |
| ------------ | ------ | -------- | ---------------------------------------- |
| getSignature | Callback for acquiring signature | Function | callback: The acquired signature is used as the parameter of callback function, that is, callback (signature); |
| success | Callback for successful upload | Object | type: type of the file uploaded successfully: "video" or "cover" |
| error | Callback for failed upload | Object | type: Type of the file that fails to be uploaded: "video" or "cover" |
| progress | Callback for upload progress | Object | type: type of the file being uploaded: "video" or "cover" <br  />name: name of the file being uploaded <br  />curr: file upload progress |
| finish | Callback for upload result | Object | fileId: video file ID <br  />videoName: video name <br  />videoUrl: video playback address <br  />coverName: cover name <br  />coverUrl: cover display address |

### Step 3: Perform the upload
#### Upload video only

```js
qcVideo.ugcUploader.start({
    videoFile: videoFile,
    getSignature: getSignature,
    success: function(result){
        console.log('type of the successfully uploaded file:' + result.type);
    },
    error: function(result){
        console.log('type of the file failed to be uploaded: ' + result.type);
        console.log('reason for the failed upload: ' + result.msg);
    },
    progress: function(result){
        console.log('type of the file in upload progress: ' + result.type);
        console.log('name of the file in upload progress: ' + result.name);
        console.log('upload progress: ' + result.curr);
        console.log('cos object: ' + result.cos);
        console.log('taskId:' + result.taskId);
    },
    finish: function(result){
        console.log('fileId in the upload result: ' + result.fileId);
        console.log('video name in the upload result: ' + result.videoName);
        console.log('video address in the upload result: ' + result.videoUrl);
    }
});
```

#### Upload both video and cover

```js
qcVideo.ugcUploader.start({
    videoFile: videoFile,
    coverFile: coverFile,
    getSignature: getSignature,
    success: function(result){
        console.log('type of the successfully uploaded file:' + result.type);
    },
    error: function(result){
        console.log('type of the file failed to be uploaded: ' + result.type);
        console.log('reason for the failed upload: ' + result.msg);
    },
    progress: function(result){
        console.log('type of the file in upload progress: ' + result.type);
        console.log('name of the file in upload progress: ' + result.name);
        console.log('upload progress: ' + result.curr);
        console.log('cos object: ' + result.cos);
        console.log('taskId:' + result.taskId);
    },
    finish: function(result){
        console.log('fileId in the upload result: ' + result.fileId);
        console.log('video name in the upload result: ' + result.videoName);
        console.log('video address in the upload result: ' + result.videoUrl);
        console.log('cover name in the upload result: ' + result.coverName);
        console.log('cover address in the upload result: ' + result.coverUrl);
    }
});
```

## Other APIs
### Cancel upload
You can cancel the upload of a video that is being uploaded.

| Parameter | Description |
| ------ | ------------------ |
| cos | cos object returned in progress |
| taskId | taskId returned in progress |

```js
qcVideo.ugcUploader.cancel({
	cos: cos,   
	taskId: taskId  
});
```
### Resume upload from breakpoint

SDK supports resuming upload from breakpoint without performing any operation.

**Internal implementation:** During file upload, SDK records the vodSessionKey of the file in COOKIE. The key name starts with webugc_, for example: webugc_dab2bfc5cfcd8d8561c44f7c68961edd9bbcxxxx. When the file is uploaded again, SDK determines whether an upload has been performed on the file based on the COOKIE. If so, the upload can be resumed from the breakpoint with the acquired vodSessionKey. Otherwise, the file is uploaded from scratch. vodSessionKey is valid for one day.

### File types for upload

| Type | Supported Format |
| ---- | ---------------------------------------- |
| Video | WMV, WM, ASF, ASX<br />RM, RMVB, RA, RAM<br />MPG, MPEG, MPE, VOB, DAT<br />MOV, 3GP, MP4, MP4V, M4V, MKV, AVI, FLV, F4V |
| Audio | MP3, WMA, WAV, ASF, AU, SND, RAW, AFC, ACC |
| Image | JPG, JPEG, JPE<br />PSD<br />SVG, SVGZ<br />TIFF, TIF<br />BMP, GIF, PNG |

### Error Codes at Backend

| Error Code | Description |
| ----------- | ----------------- |
| 10005 | Validity of resuming upload from breakpoint expired |
| 10000-19999 | Request error |
| 20000-29999 | Service error |
| 31001 | Invalid session_key in user request |
| 31002 | The VOD signature in user request already exists |
| 31003 | The file to be uploaded does not exist |
| 32001 | Service error |

### Error Messages at Frontend

| API | Error Message |
| -------------------------- | ---------------------------------------- |
| qcVideo.ugcUploader.start | File name cannot contain characters such as /, :, *, ?, "< >|
|                            | The parameter must be an object |
|                            | videoFile or fileId is required |
|                            | getSignature is required |
|                            | Incorrect format of fileId |
|                            | coverFile is required |
|                            | getSignature must be a function, and success, error, progress and finish (if any) must be functions |
|                            | videoFile must be a video file |
|                            | coverFile must be an image file |
| qcVideo.ugcUploader.cancel | The parameter must be an object |
|                            | cos/taskId cannot be empty |
|                            | Incorrect taskId format |
|                            | Incorrect cos format |

### FAQ

#### How to acquire File object?

  To acquire the File object, use "input" label with "file" as "type".

#### If 50% of a 10 MB file has been uploaded when the load is interrupted - Why is the upload resumed from the 20% of the file?

  A multipart upload is resumed based on the parts that have been uploaded successfully. For example, for a three-part upload, if two parts have been uploaded when the upload is interrupted, the upload will be resumed from the beginning of the third part no matter how far the upload has progressed before the interruption.

#### What is the maximum file size supported for upload?

  A maximum of 60 GB is supported

#### How to perform automatic transcoding for Web upload?

  Include task flow parameter in the signature (check transcoding for upload on console)

#### What is the minimum version supported for Web upload?

  IE10.

