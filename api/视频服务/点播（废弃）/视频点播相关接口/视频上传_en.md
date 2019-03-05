## 1. API Description
 
This API (MultipartUploadVodFile) is used to upload multiple parts of a video file.

Domain: vod.qcloud.com

Note:
1. Only http protocols are supported. 


## 2. Input Parameters
Note
1. Only post protocols are supported.
2. PostBody only stores the file binary streams pointed by offset and dataSize.
3. Content-Type does not support form-data. The application/octet-stream is recommended.
4. Except for the last part, the dataSize of the first part must be equal to 512 KB, and the middle parts must be larger than or equal to 512 KB. The dataSize of all parts must be equal to the content-length.
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileName
<td> Yes
<td> String
<td> Local name of the video file. If the name contains Chinese spaces, rawurlencode encoding is needed. The length should be limited to 40 characters, and the name may not contain characters such as \ / : * ? " < > and |
<tr>
<td> fileSha
<td> Yes
<td> String
<td> sha of the video file. SHA-1 is used to calculate the content of the file
<tr>
<td> fileSize
<td> Yes
<td> Int
<td> Total size of the video file, in bytes
<tr>
<td> dataSize
<td> Yes
<td> Int
<td> Size of the part uploaded, in bytes. dataSize value range is [524288 - 5242880] (non-last parts, the first part is always 524288)
<tr>
<td> offset
<td> Yes
<td> Int
<td> Offset of the uploaded part in the video file. The first part is 0, and the subsequent offsets can be returned based on the last operation
<tr>
<td> fileType
<td> Yes
<td> String
<td> Type of the video file. This can be known from the suffix
<tr>
<td> tags.n
<td> No
<td> String
<td> List of tags of the video
<tr>
<td> classId
<td> No
<td> Int
<td> Category ID of the video
<tr>
<td> isTranscode
<td> No
<td> Int
<td> Whether to perform transcode. 0: No (default), 1: Yes. If the video is not transcoded, you can do it from Video File Management in the Console after the video has been uploaded;
<tr>
<td> isScreenshot
<td> No
<td> Int
<td> Whether to take snapshot. 0: No (default), 1: Yes
<tr>
<td> isWatermark
<td> No
<td> Int
<td> Whether to add watermark. 0: No (default), 1: Yes. Be sure to select watermark file and determine watermark location in advance if you choose to add watermark. Otherwise the upload process may fail;
</tbody></table>


 

## 3. Output Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code. 0:  Succeeded, other values:  Failed
<tr>
<td> message
<td> String
<td> Error message
<tr>
<td> flag
<td> Int
<td> Whether it is the last part. 0: Upload is not completed, 1: The entire file has been uploaded
<tr>
<td> offset
<td> String
<td> The offset from which the next part of data should be uploaded. It has a value only when flag is 0
<tr>
<td> fileId
<td> String
<td> ID of the video file. It has a value only when flag is 1
</tbody></table>

 

## 4. Example
 
Input 1
<pre>
 http://domain/v2/index.php?Action=MultipartUploadVodFile
 &fileName=Inception
 &fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
 &fileSize=1024
 &dataSize=512
 &offset=0
 &fileType=avi
 &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a> 
[The binary content data of the uploaded video file]
</pre>
Note:
The size of the binary content data of the uploaded video file is equal to that specified by dataSize;

Output 1
```

{
    "code" : 0,
    "message" : "",
    "flag" : 0,
    "offset" : "512",
}

```

Input 2
<pre>
 http://domain/v2/index.php?Action=MultipartUploadVodFile
 &fileName=Inception
 &fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
 &fileSize=1024
 &dataSize=512
 &offset=512
 &fileType=avi
 &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
[The binary content data of the uploaded video file]
</pre>
Note:
The size of the binary content data of the uploaded video file is equal to that specified by dataSize. For &COMMON_PARAMS, please refer to [[Common Parameters|Common Parameters section]].

Output 2
```

{
    "code" : 0,
    "message" : "",
    "flag" : 1,
    "fileId" : "18168685704931758788",
}
```


 ## 5. Examples of Other Codes 
[Python Example](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/qcloudapi-sdk-python-upload.zip)
[Java Example](https://mc.qcloudimg.com/static/archive/4d3d855a631860048ff92ca55379ffb9/qcloudapi-sdk-java-upload.zip)
[PHP Example](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/qcloudapi-sdk-php-upload.zip)
[JS Example](http://video.qcloud.com/sdk/upload.html)

 ## 6. Upload Process 
As video files are generally large, they need to be uploaded in parts. The MultipartUploadVodFile API uses the multipart upload method.
**What is multipart upload?**
Multipart upload is a function that splits a file into several small parts of data with a specific size, and uploads these parts of data to the server sequentially. These small parts of data in the server will be combined into a resource, which will be verified with sha value to ensure that the merged file is a complete file identical to the file uploaded by the user. Multipart upload has two advantages: it prevents upload failure caused by network instability, and allows breakpoint resume. The disadvantage is that the protocol becomes complicated, making it slightly difficult for users to use the api. We can understand the process of multipart upload through the figure below.

<img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/kehuduan-1.png" alt="kehuduan-1.png">

As can be seen from the figure above, after the multipart upload is completed, the parts will be merged into a file, and the sha value of the file content will be calculated. If the sha value is the same as that of the original file, the file is successfully uploaded.
We can also know that, a part of a file is decided by two values, namely, the offset (offset) and the part size (dataSize). Through these two parameters, we can locate a part in a file and get its content, as shown in the following figure.

<img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/kehuduan-3.png" alt="kehuduan-3.png">

Therefore, each request uses a part as granularity. The process of uploading a complete file using the MultipartUploadVodFile API is shown below.

<img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/kehuduan-2.png" alt="kehuduan-2.png">

When the client needs to upload a file, it will upload the first part whose offset is 0. The size of a part (dataSize) is decided by the content of the part, and the minimum size recommended is 512KB. After receiving the data, the server returns a response to the client, telling the client how many content has been uploaded, and the offset from which the next upload should start. Then, the client will upload multipart data according to the specified offset. If flag is 0, it means that the upload has not yet completed. If the file has been uploaded, or if the file already exists on the server, the server response will set flag to 1 and return a unique ID of the file (fileId).
Therefore, what the client needs to do is call the MultipartUploadVodFile API circularly, after initiating the upload of the first part, to upload the next part content specified by the server according to the server's response, until the server returns a message indicating that the file has been completely uploaded.

## 7. FAQ and Handling Methods 
●**What value should be set for the dataSize of multipart upload?**
The minimum value should be no less than 512KB. Generally, it can be set to 5MB. In case of an unstable network, you can set it to a smaller value, such as 1MB or 2MB.
●**What are the common causes for a transmission failure?**
There are two circumstances. One is that the server returns a response containing an error code, and the other is that the server does not return an error code.
If there is an error code in the response returned, troubleshooting can be performed based on the error code. The error codes and troubleshooting methods are shown in the following table.
<table class="t">
<tbody><tr>
<th> <b>Error Code</b>
</th><th> <b>Error Message</b>
</th><th> <b>Meaning</b>
</th><th> <b>Troubleshooting Method</b>
</th></tr>
<tr>
<td> -26498
</td><td> check signature error!
</td><td> Signature is invalid
</td><td> Read the wiki authentication instructions
</td></tr>
<tr>
<td> 10003
</td><td> key agent secret id is not exist
</td><td> The secret id does not exist or invalid id
</td><td> Check whether the account activates Cloud Video on Demand service or whether the account has expired, or check whether the SecRetId and SecRetKey are correct in <a href="https://console.cloud.tencent.com/capi" class="external free" title="https://console.cloud.tencent.com/capi" target="_blank" rel="nofollow">https://console.cloud.tencent.com/capi</a>
</td></tr>
<tr>
<td> 10004
</td><td> check sign failure
</td><td> Signature verification failed
</td><td> Read the wiki authentication instructions, check whether the signature is correctly sorted, and calculate whether the signature string is consistent with the HTTP request issued
</td></tr>
<tr>
<td> -25997
</td><td> invalid SecretId param
</td><td> Invalid secret id
</td><td> Obtain the secret id correctly, and check whether SecRetId and SecRetKey are correct in <a href="https://console.cloud.tencent.com/capi" class="external free" title="https://console.cloud.tencent.com/capi" target="_blank" rel="nofollow">https://console.cloud.tencent.com/capi</a>
</td></tr>
<tr>
<td> -25976
</td><td> invalid notifyurl param
</td><td> Invalid notifyUrl
</td><td> Call-back address is invalid. Please confirm whether the call-back address is a valid http link
</td></tr>
<tr>
<td> -29200
</td><td> upload file sha checksum not equal
</td><td> sha of the uploaded file is not equal after verification
</td><td> Check whether the sha is calculated correctly
</td></tr>
<tr>
<td> -25986
</td><td> invalid fileType param
</td><td> Invalid fileType
</td><td> fileType is invalid
</td></tr>
<tr>
<td> -25985
</td><td> invalid fileSha param
</td><td> Invalid fileSha
</td><td> fileSha is invalid. Please check the calculation function
</td></tr>
<tr>
<td> -25984
</td><td> invalid tag param
</td><td> Invalid tag
</td><td> Check whether the tag contains invalid characters
</td></tr>
<tr>
<td> -25983
</td><td> nvalid classId param
</td><td> Invalid classId
</td><td> Check whether the classId exists
</td></tr>
<tr>
<td> -25981
</td><td> invalid fileSize param
</td><td> Invalid fileSize
</td><td> Check whether the fileSize is calculated correctly
</td></tr>
<tr>
<td> -25980
</td><td> invalid isScreenshot param
</td><td> Invalid isScreenshot
</td><td> Check whether isScreenshot parameter type is correct
</td></tr>
<tr>
<td> -25979
</td><td> invalid isWatermark param
</td><td> Invalid isWatermark
</td><td> Check whether isWatermark parameter type is correct
</td></tr>
<tr>
<td> -25978
</td><td> invalid isTranscode param
</td><td> Invalid isTranscode
</td><td> Check whether isTranscode parameter type is correct
</td></tr>
<tr>
<td> -25982
</td><td> invalid dataSize param
</td><td> Invalid dataSize
</td><td> Check whether the part size is set correctly
</td></tr>
<tr>
<td> -25977
</td><td> invalid dataSize param, dataSize + offset &gt; fileSize
</td><td> Invalid dataSize
</td><td> The part size plus the offset sent has exceeded the file size. In this case, you should check whether the dataSize of the last part is set correctly, which should be less than the part size set previously
</td></tr></tbody></table>

If no error code is returned, check whether the server still responds. If the status code of http is not 200, you can refer to the error codes specified in the http protocol to quickly identify the cause of the error (distinguish it from the error codes in the message returned by the server (the format is {"code":0,"message":".."}). When the server returns an error code in the message, the http status code is always 200).  If the server does not respond, it may be attributed to bad network. At this time, you should check whether the network is available and check the http. In addition, check whether the HOST file of the host has been modified. If the host for the domain of the access API is modified, a connection failure may also occur. The host file in Windows systems is generally located in the hosts file under C:\Windows\System32\drivers\etc.  The host file in Linux systems is generally located in /etc/hosts. 
●**Every time I upload a part, such parameters as whether to perform transcode, and whether to add watermark will be attached. When do these parameters take effect?**
Transcode, watermark, and screenshot parameters take effect when the first part is uploaded. Transcode, watermark and screenshot parameters for other parts do not take effect. In addition, watermark and screenshot will take effect only when the transcode is set. If the three parameters of the uploaded video are inconsistent with expected, it may be because the video has been uploaded before. 
 ## 8. Setting Transcoding Call-back 
You can configure transcoding call-back for file upload operations to notify the client about the status of transcoding process. The parameter for call-back address is notifyUrl.  Call-back will be effective only when isTranscode is 1. The server will send post request to the specified address once transcoding process is finished. The request content will be in json format.
Call-back status:  Call-back occurs once only after all transcoding results are generated. Call-back statuses include: Success (all or part of the formats are transcoded successfully), and Failure (all format transcoding failed). The call-back information only displays links of all the corresponding formats generated after successful transcoding. If not displayed, it means that the corresponding format transcoding failed. In this case, you can perform another transcoding using ConvertVodFile.

After the file is successfully transcoded, perform call-back,
```
{
　　"status":0, //Returned status,
　　"message":"" //Returned message,
　　"task":"transcode" // It will be "file_upload" when the file is uploaded, and "transcode" when the transcoding process is finished
　　"data":{
　　"ret":0 //Error code,
　　"message":""//Message,
　　"file_id" :123445//File ID
　　"image_video":{
　　"code":0,
　　"duration":0,//Duration
　　"imgUrl":{
		 "id": 3213,
　　"url":"cloud.tencent.com/templurl.png", //Image link
　　"vheight":21,
　　"width":32, 
　　}
　　}
　　"message":"",//Message
　　"vid":"231414" ,//Video ID,
　　"videoUrls":[
　　{
　　"url":"www.qcloucd.com/temp_video.mp4",
　　"md5":"fdasfdsafsadf",//MD5 value
　　"sha":"dasfdsfas",//sha value of file,
　　"size":123 ,//Size
　　"update_time":"2015 08 49 12:0:0", //Update time
　　"vbirate":231,//Bit rate
　　"vheight": 480 ,/ /Video height
　　"vwidth":800 ,//Video width
　　
 }
　　]
　　"player_code" :{
 "h5":"" ,//html5 player code,
　　"flash":"",//flash player code,
　　"iframe":"",//iframe player code
　　}
　　}
}

```

It should be noted that when the file starts to transcode after uploaded, an error code of 303 will be returned since the transcoding has not yet completed. In other cases, you need to pay attention to the error code returned by ret. The other error codes are as follows:
<table class="t">
<tbody><tr>
<th> <b>Error Code</b>
</th><th> <b>Error Type</b>
</th><th> <b>Cause of Error</b>
</th></tr>
<tr>
<td> -300
</td><td> Internal error
</td><td> getvidformat failed
</td></tr>
<tr>
<td> -301
</td><td> Internal error
</td><td> getvidformat timeout
</td></tr>
<tr>
<td> -302
</td><td> Internal error
</td><td> getvidformat failed. The file does not exist
</td></tr>
<tr>
<td> -303
</td><td> Internal error
</td><td> getvidformat failed. The list is empty after file transcoding
</td></tr>
<tr>
<td> -304
</td><td> Internal error
</td><td> getfileinfo failed
</td></tr>
<tr>
<td> -305
</td><td> Internal error
</td><td> getfileinfo timeout
</td></tr>
<tr>
<td> -308
</td><td> Internal error
</td><td> setfileinfo failed
</td></tr>
<tr>
<td> -309
</td><td> Internal error
</td><td> setfileinfo timeout
</td></tr>
<tr>
<td> -350
</td><td> Internal error
</td><td> getfileinfo failed. The file cannot be accessed
</td></tr>
<tr>
<td> -400
</td><td> Internal error
</td><td> OCDispatch failed
</td></tr>
<tr>
<td> -401
</td><td> Internal error
</td><td> OCDispatch timeout
</td></tr>
<tr>
<td> -500
</td><td> Internal error
</td><td> transwm setting failed
</td></tr>
<tr>
<td> -501
</td><td> Internal error
</td><td> transwm setting timeout
</td></tr>
<tr>
<td> -502
</td><td> Internal error
</td><td> Transcoding failed
</td></tr>
<tr>
<td> -503
</td><td> Internal error
</td><td> Transcoding timeout
</td></tr>
<tr>
<td> -550
</td><td> External error
</td><td> Transcoding failed, source file error
</td></tr></tbody></table>



