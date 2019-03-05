## 1. API Description
 
This API (DescribeVodCover) is used to set the cover for the video.

Domain:  vod.api.qcloud.com

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileId <td> Yes <td> Int <td> ID of the video file
<tr>
<td> type <td> Yes <td> Int <td> Cover setting method (1: Use screenshot url, not 1: Upload local image)
<tr>
<td> para <td> Yes <td> String <td> If the value of type is 1, para refers to screenshot url; if the value of type is not 1, para refers to the local path of the local image.
<tr>
<td> imageData <td> No <td> String <td> If the value of type is not 1, it means using a local image as the cover, and this parameter refers to base64 string data of the image (valid only when the value of type is not 1).
</tbody></table>

 

## 3. Output Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Error code, 0:  Succeeded, other values:  Failed
<tr>
<td> message <td> String <td> Error message
</tbody></table>

 

## 4. Example
 
Input
<pre>
  https://domain/v2/index.php?Action=DescribeVodCover
  &fileId=8782277315343726561
	&para=D:/image/123.jpg
  &type=2
  &imageData=8d451afe8b1611e4919815f8b80b7a9a
  &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>
The cover is a network file
https://domain/v2/index.php?Action=DescribeVodCover
  &fileId=8782277315343726561
  &para=http://test.com/123.jgp
  &type=1
  &COMMON_PARAMS

Output
```

{
    "code": 0,
    "message": ""
}

```



