## Overview

The client upload SDK for browsers can be used to upload videos and cover image files to Tencent Cloud VOD system.

## Integration Method

### Development Environment

* Browsers must support HTML 5 to use the SDK.
* App server is required to distribute upload signatures for clients. For information on how to generate signatures, please see [Upload Signature](/document/product/266/9221).

### Integration

Introduce ugcuploader.js into the page.
```js
<script src="//imgcache.qq.com/open/qcloud/js/vod/sdk/ugcUploader.js"></script>
```

### Demo

[http://video.qcloud.com/sdk/ugcuploader.html](http://video.qcloud.com/sdk/ugcuploader.html)

## Steps for Upload

###  Step 1: Acquire Upload Signature
```js
var getSignature = function(callback){
    $.ajax({
        url:  'yourinterface',  //The server acquires the URL for client upload signature
        type:  'POST',
        dataType:  'json',
        success:  function(result){
            //result.returnData.signature is the acquired signature
            callback(result.returnData.signature);
        }
    });
};

```

###  Step 2: Specify Targets to be Uploaded

These targets include videos and cover image information. You can leave the cover image parameters empty if you only upload videos.

| Parameter Name |  Required | Type | Parameter Description |
| ------ | ------ | ------ | ------ | ------ |
| videoFile | Yes | File |  Video files to be uploaded |
| coverFile | No | File | Cover image files to be uploaded |
| getSignature | Yes | Function |  Callback function used to acquire signature |
| success   | No |Function | Callback function when upload succeeds |
| error     | No | Function | Callback function when upload fails |
| progress  | No | Function |  Callback function for upload progress |
| finish    | No | Function | Callback function for upload result |

Callback function description

| Function | Description | Parameter Type | Parameter Description |
| ------ | ------ | ------ | ------ |
| getSignature | Callback for acquiring signature | Function | callback: the acquired signature is used as the parameter of callback function, that is, callback (signature); |
| success | Callback when upload succeeds | Object | type: file type of the successful upload operation, "video" or "cover" |
| error | Callback when upload fails | Object | type: file type of the failed upload operation, "video" or "cover" |
| progress | Callback for upload progress | Object | type: type of the file being uploaded, "video" or "cover" <br/>name: name of the file being uploaded <br/>curr: file upload progress |
| finish   | Callback for upload result | Object | fileId: video file ID <br/>videoName: video name <br/>videoUrl: video playback address <br/>coverName: cover name <br/>coverUrl: cover display address |

### Step 3: Execute the Upload Operation

#### Upload Videos Only

```js
qcVideo.ugcUploader.start({
    videoFile: videoFile,
    getSignature: getSignature,
    success: function(result){
        console.log('Type of the successfully uploaded file:' + result.type);
    },
    error: function(result){
        console.log('Type of the file failed to be uploaded:' + result.type);
        console.log('Reason for the failed upload:' + result.msg);
    },
    progress: function(result){
        console.log('Type of the file during upload progress:' + result.type);
        console.log('Name of the file during upload progress:' + result.name);
        console.log('Upload progress:' + result.curr);
    },
    finish: function(result){
        console.log('fileId in the upload result:' + result.fileId);
        console.log('Video name in the upload result:' + result.videoName);
        console.log('Video address in the upload result:' + result.videoUrl);
    }
});
```

#### Upload Both Videos and Cover Images

```js
qcVideo.ugcUploader.start({
    videoFile: videoFile,
    coverFile: coverFile,
    getSignature: getSignature,
    success: function(result){
        console.log('Type of the successfully uploaded file:' + result.type);
    },
    error: function(result){
        console.log('Type of the file failed to be uploaded:' + result.type);
        console.log('Reason for the failed upload:' + result.msg);
    },
    progress: function(result){
        console.log('Type of the file during upload progress:' + result.type);
        console.log('Name of the file during upload progress:' + result.name);
        console.log('Upload progress:' + result.curr);
    },
    finish: function(result){
        console.log('fileId in the upload result:' + result.fileId);
        console.log('Video name in the upload result:' + result.videoName);
        console.log('Video address in the upload result:' + result.videoUrl);
        console.log('Cover name in the upload result:' + result.coverName);
        console.log('Cover address in the upload result:' + result.coverUrl);
    }
});
```

