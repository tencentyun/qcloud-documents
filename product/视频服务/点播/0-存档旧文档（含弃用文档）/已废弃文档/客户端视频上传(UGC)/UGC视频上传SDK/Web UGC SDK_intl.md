## SDK Integration
1. Import js script into the page
https://qzonestyle.gtimg.cn/open/qcloud/js/vod/sdk/uploaderh5V3.js

2. Deploy [calculator_worker_sha1.js](http://video.qcloud.com/calculator_worker_sha1.js) on the server. This file is used to calculate the sha1 of the files to be uploaded. Usually, you simply need to download this file to the root directory in the same domain as the upload service. The reason that they need to be in the same domain is that SDK uses html5 worker to calculate SHA1 asynchronously in order to optimize uploading process. "Same domain" is a restriction of html5 worker.

## Local Video Upload

### Initialize Upload Component

```javascript
var ErrorCode = qcVideo.get('ErrorCode');
ErrorCode.UN_SUPPORT_BROWSE !== qcVideo.uploader.initUGC(
        //1: Basic information of the upload
        {
            upBtnId: upBtnId, //ID of upload button (ID of any page element)

            /*
                @desc, function used to acquire signature from the server. This function contains two parameters:
                argObj: Information of the file to be uploaded. Critical information includes:
                    f: Video file name (can be acquired from the argObj of getSignature),
                    ft: Video file type (can be acquired from the argObj of getSignature),
                    fs: Video file sha1 value (must be acquired from the argObj of getSignature),
                callback: After the client has acquired the signature from its server, it will call this function to pass the signature to SDK                    
            */
            getSignature: function(argObj, callback){
                // Call the APP backend server and return signature
	            var sigUrl = 'http://yourdomain?'
	            + 'f=' + encodeURIComponent(argObj.f)
	            + '&ft=' + encodeURIComponent(argObj.ft)
	            + '&fs=' + encodeURIComponent(argObj.fs);

                $.get(sigUrl).done(function(ret) {
					callback(ret.signature);
				})
            }
            ,after_sha_start_upload: false //Upload process consists of two phases: sha calculation and network file transmission. This option is used to define whether network transmission upload shall start immediately after sha has been calculated (by default, upload does not start immediately)
            ,sha1js_path: 'http://<your domain>/<your configured directory>/<sha1 calculation script>.js' //Location for calculating sha1, default is  'http://<your domain>/calculator_worker_sha1.js'
        }
        //2: Callback function
        , {
            /**
            * Update file status and progress
            * @param args { id: File ID, size: File size, name: File name, status: Status, percent: Progress, speed: Speed, errorCode: Error code }
            */
            onFileUpdate: function (args) {
                console.log(args);
            },
            /**
            * File status has changed
            * @param info  { done: Number of uploaded files, fail: Number of failed files, sha: Number of SHA values calculated or waiting to be calculated, wait: Number of files waiting to be uploaded, uploading: Number of files that are being uploaded }
            */
            onFileStatus: function (info) {
                console.log('Total number of various statuses' , info);
            },
            /**
            *  Filter prompt for file errors when uploading
            * @param args {code:{-1: File type error, -2: File name error} , message: Reason for error, solution: Solution }
            */
            onFilterError: function (args) {
                console.log('message:' + args.message + (args.solution ? (';solution==' + args.solution) : ''));
            }
        }
    ));
```


### API

```
qcVideo.uploader.startUpload()
Function: Start uploading
Parameter: None;
Response: None;
```

```
qcVideo.uploader.stopUpload()
Function: Stop uploading
Parameter: None;
Response: None;
```

```
qcVideo.uploader.reUpload()

Function: Resume uploading (re-upload incorrect files)
Parameter: None;
Response: None;
```

```
qcVideo.uploader.deleteFile(fid)

Function: Delete local upload task
Parameter: fid file ID;
Response: None;
```

```
qcVideo.uploader.getOriginalFile(fid)

Function: Acquire local file object
Parameter: None;
Response: FILE object;
```

## Compatibility

Currently, this SDK only supports HTML5 upload. It has been tested on major browsers such as Chrome, Safari, and can function normally. Different manufacturers may use different methods to implement HTML5, please analyze your specific circumstance if you cannot use this SDK on certain machines.
