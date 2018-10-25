## 1. API Description

This  API (ConvertVodFile) is used to perform transcoding and add watermark for uploaded videos. Detailed configuration for transcoding and watermark will follow the configuration parameters of the Console.

Domain: vod.api.qcloud.com

## 2. Input Parameters
 </b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileId
<td> Yes
<td> string
<td> File
<tr>
<td> isScreenshot
<td> No
<td> int
<td> Whether to take snapshot. 0: No. 1: Yes
<tr>
<td> isWatermark
<td> No
<td> int
<td> Whether to add watermark. 0: No. 1: Yes
<tr>
<td> notifyUrl
<td> No
<td> string
<td> Call-back address of transcoding result
</tbody></table>


</b></th> 

## 3. Output Parameters
 </b></th>
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

</b></th> 

## 4. Example

Input 1
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=ConvertVodFile
&fileId=96000077184630899
&isScreenshot=1
&isWatermark=1
&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>

</pre>
Output 1
```
{
    "code" : 0,
    "message" : "",
}

```
## 5. Call-back Information
You can configure transcoding call-back for file upload operations to notify the client about the status of transcoding process. The parameter for call-back address is notifyUrl. The server will send post request to the specified address once transcoding process is finished. The request content will be in json format.
```
{
　　"status":0, //Returned status,
　　"message":"" //Returned information,
　　"task":"transcode" // It will be "file_upload" when the file is uploaded, and "transcode" when the transcoding process is finished
　　"data":{
　　"ret":0 //Error Code,
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
　　"sha":"dasfdsfas",//sha value of file
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



