## 1. API Description
 
This API (DescribeVodPlayUrls) is used to acquire all playback URLs, format, bit rate, height, width information of current video.

Domain: vod.api.qcloud.com
 

## 2. Input Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileId
<td> Yes
<td> String
<td> ID of the video whose information is to be acquired
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
<td> playSet
<td> Array
<td> Play information result set of this video
</tbody></table>
</b></th>playSet Play information result set of this video</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> url
<td> String
<td> Play address
<tr>
<td> definition
<td> Int
<td> Format. 0:  ["", "Original"], 1:  ["With watermark", "Original"], 10:  ["Mobile phone", "mp4"], 20:  ["Standard definition", "mp4"], 30:  ["High definition", "mp4"], 110:  ["Mobile phone", "flv"], 120:  ["Standard definition", "flv"], 130:  ["High definition", "flv"],210:  ["Mobile phone", "hls"], 220:  ["Standard Definition", "hls"], 230:  ["High definition", "hls"],240:  ["Ultra high definition", "hls"]
<tr>
<td> vbitrate
<td> Int
<td> Bit rate. Unit: kbps
<tr>
<td> vheight
<td> Int
<td> Height. Unit: px
<tr>
<td> vwidth
<td> Int
<td> Width. Unit: px
</tbody></table>
 

## 4. Example
 
Input
<pre>
  https://domain/v2/index.php?Action=DescribeVodPlayUrls
  &fileId=2721945854681023354
  &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>

Output
```

{
    "code" : 0,
    "message" : "",
    "playSet" : [
        {
            "url" : "http:\/\/vcloud1200.tc.qq.com\/1200_5b9688d481d8b811095d30a78cf44c4285026a4c.f0.mp4",
            "definition" : 0,
            "vbitrate" : 2332000,
            "vheight" : 576,
            "vwidth" : 1024
        }
    ]
}

```



