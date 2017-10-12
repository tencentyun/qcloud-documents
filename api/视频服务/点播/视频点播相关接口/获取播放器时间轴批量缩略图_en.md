## 1. API Description

This API ( DescribeScreenShot) is used to acquire thumbnails on the player time line. Once size is specified, thumbnails will be acquired according to specified height/width with a frequency of 1 thumbnail per 10 seconds. Every 100 acquired images will be grouped into one large image, with a corresponding address in a fixed format. Users may acquire these images in sequence according to the fixed format after performing certain actions.

Note: This API is only available to users who have purchased certain service packages. For details, see [Product Introduction](http://cloud.tencent.com/product/vod.html#price) for details.

Domain:  vod.api.qcloud.com

## 2. Input Parameters

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileId
<td> Yes
<td> Int
<td> ID number of the video file
<tr>
<td> Width
<td> Yes
<td> Int
<td> Snapshot width (1-300)
<tr>
<td> Height
<td> Yes
<td> Int
<td> Snapshot height (1-300)
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
<td> Error Message
<tr>
<td> data
<td> json string
<td> If code0, return will be null, this indicates that calling was successful
</tbody></table>



## 4. Example

Input
<pre>
 
 https://vod.api.qcloud.com/v2/index.php?Action=DescribeScreenShot  
 &fileId=11324759161874546895
  &width=200
  &height=200
 &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>

</pre>
Output
```
 
{
    "code": 0,
    "message": "",
    "data": null
}

```

## 5.Format of The Generated Snapshot File
Example:
```
http://p.qpic.cn/videoyun/0/2527_3dfcbbea604611e5b999e93ca40bd61b_QB_1/0
```
Where:

<table class="t"><tbody>
<tr>
<td> http://p.qpic.cn/videoyun/0/		
<td> A fixed directory where the images will be stored. Do not change this fixed directory;
<tr>
<td> 2527_3dfcbbea604611e5b636e93ca40bd61b
<td> vid of the file. You can acquire this by using fileid via the API DescribeVodInfo;
<tr>
<td> _QB
<td> Fixed value. Cannot be changed;
<tr>
<td> _1	    
<td>  Thumbnail image group number. Minimum is 1, maximum is (video duration in seconds/10/100). Increase this value to the maximum value to acquire all snapshots;
<tr>
<td> /0	
<td>Fixed value. Cannot be changed;
</tbody></table> 




