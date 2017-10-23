## 1. API Description

This API (MultiPullVodFile) is used to pull a batch of video files to Tencent Cloud from existing resource library, according to URLs passed by the user. Through this API, multiple video files can be pulled in batched. The order of each video is determined based on the value of "n" from the input parameter.

Domain: vod.api.qcloud.com
 

## 2. Input Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> pullset.n.url
<td> Yes
<td> String
<td> URLs of the videos to be pulled. "n" is an integer,"1" for the first video,"2" for the second video and so on
<tr>
<td> pullset.n.fileName
<td> Yes
<td> String
<td> Name of the video file
<tr>
<td> pullset.n.fileMd5
<td> No
<td> string
<td> MD5 of the video file
<tr>
<td> pullset.n.isTranscode
<td> No
<td> Int
<td> Whether to perform transcode. 0: No (default), 1: Yes. If the video is not transcoded, you can do it from Video File Management in the Console after the video has been uploaded;
<tr>
<td> pullset.n.isScreenshot
<td> No
<td> Int
<td> Take snapshot or not. 0: No (default), 1: Yes
<tr>
<td> pullset.n.isWatermark
<td> No
<td> Int
<td> Whether to add watermark. 0: No (default), 1: Yes. Be sure to select watermark file and determine watermark location in advance if you choose to add watermark. Otherwise the upload process may fail;
<tr>
<td> pullset.n.notifyUrl
<td> No
<td> String
<td> Tencent Cloud will notify the caller that the video has been successfully pulled by calling back on this URL address.
<tr>
<td> pullset.n.classId
<td> No
<td> Int
<td> Category ID of the video
<tr>
<td> pullset.n.tags
<td> No
<td> String
<td> Tags of the video. Multiple tags are separated using commas
<tr>
<td> pullset.n.priority
<td> No
<td> Int
<td> Priority. 0: Medium. 1: High. 2: Low
<tr>
<td> pullset.n.isReport
<td> No
<td> Int
<td> Call-back switch. Determines whether to return packets to the developer. 0: No (default), 1: Yes
</tbody></table>

 

## 3. Output Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error Code, 0:  Succeeded, other values:  Failed
<tr>
<td> message
<td> String
<td> Error Message
<tr>
<td> data
<td> array
<td> Submit list of files to be uploaded
</tbody></table>

data is an array. Formats for each item are as follows
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> source_url
<td> string
<td> Origin server address
<tr>
<td> file_id
<td> uint
<td> file_id
<tr>
<td> file_name
<td> string
<td> File name
</tbody></table>

 

## 4. Example
 
Input 1
<pre>
 https://domain/v2/index.php?Action=MultiPullVodFile
 &pullset.1.url=http%3A%2F%2Fv.qq.com%2Fcover%2Ft%2Ftofg0ynqvcjac58.mp4 //The URL must point to the address of the downloadable video
 &pullset.1.fileName=test
 &pullset.1.isTranscode=1
 &pullset.1.priority=1
 &pullset.1.isScreenshot=1
 &pullset.1.isWatermark=1
 &pullset.1.notifyUrl=http%3A%2F%2Ftest.com%2Ftest
 &pullset.1.classId=0
 &pullset.1.isReport=1
 &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>

Output 1
```

{
    "code" : 0,
    "message" : "",
}

```

## 5. Call-back Instruction
General

● Call Relationship
	Video cloud-->Developer
	Request method
	HTTP POST
● Data Format
	json
● Input Parameter Description
	The "path" section of the POST refers to the notify_url passed by the developer (including parameters determined by the developer), which is passed when calling the API
	The "data" section of the POST is json. Required fields are as follows:
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> task
<td> Yes
<td> string
<td> transcode: Transcode file_upload: Upload
<tr>
<td> status
<td> Yes
<td> int
<td> 0 indicates success
<tr>
<td> message
<td> Yes
<td> string
<td>Error description
<tr>
<td> data
<td> No
<td> object
<td>Extension section, detailed data of each API
</tbody></table>

Note: If the developer specifies to transcode when calling the API, there will be two call-backs. One is for the success of uploading, the other is for the success of transcoding. [Call-back Instruction of Transcode Result](http://cloud.tencent.com/wiki/v2/MultipartUploadVodFile#8..E8.AE.BE.E7.BD.AE.E8.BD.AC.E7.A0.81.E5.9B.9E.E8.B0.83)

● Output Parameter Description
The call-back API needs to return data in json format. Required fields are as follows:
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error Code, 0:  Succeeded, other values:  Failed
<tr>
<td> message
<td> String
<td> Error Message
</tbody></table>


status definition
<table class="t"><tbody><tr>
<th><b>Parameter</b></th>
<th><b>Description</b></th>
<tr>
<td> 0 
<td> Success
<tr>
<td> 10001
<td> Failed to pull file from the origin server
</tbody></table>


API description
The call-back parameters required by the APIs are as follows. Data should be filled in the "data" section of the http post.

The structure of "data" section is as follows
<table class="t"><tbody><tr>
<th><b>Parameter</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td>image_video
<td>object
<td>Video information
<tr>
<td> ret
<td> int
<td> 0 means success. Other values mean failure (Users don't need to consider this field)
<tr>
<td> message
<td> string
<td> Acquire error information of the video information API
<tr>
<td> file_id
<td> string
<td> Video ID
<tr>
<td> source_url
<td> string
<td> Pull URL
</tbody></table>

The image_video field is as follows:
<table class="t"><tbody><tr>
<th><b>Parameter</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td>code
<td>int
<td>1 means success (internal error code, no need to consider this value)
<tr>
<td> duration
<td> int
<td> Video duration
<tr>
<td> imgUrls
<td> array
<td> Video cover list
id: Snapshot ID
url: Snapshot address
vheight: Snapshot height
vwidth: Snapshot width
<tr>
<td> message
<td> string
<td> API returned information
<tr>
<td> vid
<td> string
<td> vid
<tr>
<td> videoUrls
<td> array
<td> Video basic information and play information list
accessperm:0 No need to consider this value
definition:int Resolution
filename:string File name after transcoding
md5: File MD5 after transcoding
sha: File sha after transcoding
size: File size after transcoding
update_time: Update time of the file
url: Play address of the file
vbitrate: Video bit rate   0 if not trancoded
vheight: Video height   0 if not trancoded
vwidth: Video width    0 if not trancoded
</tbody></table>

Example: API URL for pulling file
```
"image_video" > array(
      code>int
      duration>int
      imgUrls>array(   // Video snapshot information
         array(
            id>int
            url>'string'
            vheight>int
            vwidth>int
         )
     )
     message>'string'
     vid>'string'
     videoUrls>array(   // Video play information
        array(
            url>'string'
            md5>'string'
            sha>'string'
            size>'string'
            update_time>'string'
            vbitrate>int
            vheight>int
						vwidth>int
        )
			)
   )
),
"ret">'int',Acquire error code of video information
"message">'string',Acquire error description of video information,
"file_id">int,File ID
"player_code">array(
"h5">'string',h5 player code
"flash">'string'，flash player code
"iframe">'string'，iframe code
)

```


