## 1. API Description

This API ( DescribeVodPlayInfo) is used to acquire video information, which acquires video information list according to video file name.
 
Domain: vod.api.qcloud.com

## 2. Input Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileName
<td> Yes
<td> String
<td> Video name (prefix match)
<tr>
<td> pageNo
<td> No
<td> int
<td> Page number
<tr>
<td> pageSize
<td> No
<td> int
<td> Page size
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
<td> totalCount
<td> Int
<td> Total number of videos
<tr>
<td> fileSet
<td> Array
<td> Video list result set
</tbody></table>

</b></th>fileSet video list result set</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileId
<td> String
<td> Video ID
<tr>
<td> fileName
<td> String
<td> Video name
<tr>
<td> duration
<td> String
<td> Video duration
<tr>
<td> status
<td> String
<td> Video status. -1: Upload incomplete, does not exist; 0: Initialize, not in use; 1: Verification failed, not in use; 2: Normal; 3: Paused; 4: Transcoding; 5: Publishing; 6: Deleting; 7: Transcoding failed; 10: Waiting to be transcoded; 11:  Transcoding partially completed; 100: Deleted
<tr>
<td> imageUrl
<td> String
<td> Video cover image
<tr>
<td> playSet
<td> Array
<td> Video play information
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
<td> Format. 0:  ["", "Original"], 1:  ["With watermark", "Original"], 10:  ["Mobile phone", "mp4"], 20:  ["Standard definition", "mp4"], 30:  ["High definition", "mp4"], 110:  ["Mobile phone", "flv"], 120:  ["Standard definition", "flv"], 130:  ["High definition", "flv"]
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
 
Query by a video ID
Input
<pre>
 
 https://domain/v2/index.php?Action=DescribeVodPlayInfo
 &fileName=13425173277
 &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>

</pre>

Output
```
 
{
    "code": 0,
    "message": "",
    "totalCount": "105",
    "fileSet": [
        {
            "fileId": "11624759161874546966",
            "fileName": "13425173277_2015-09-06-18-56-11_2015-09-06-19-06-11",
            "duration": 600,
            "status": "2",
            "image_url": "http://p.qpic.cn/videoyun/0/1203_7626dd7d1c3e48eea1230026126caf7d_1/640",
            "playSet": [
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_7626dd7d1c3e48eea1230026126caf7d.f0.mp4",
                    "definition": 0,
                    "vbitrate": 250000,
                    "vheight": 480,
                    "vwidth": 640
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_7626dd7d1c3e48eea1230026126caf7d.f10.mp4",
                    "definition": 10,
                    "vbitrate": 149128,
                    "vheight": 240,
                    "vwidth": 320
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_7626dd7d1c3e48eea1230026126caf7d.f20.mp4",
                    "definition": 20,
                    "vbitrate": 299837,
                    "vheight": 480,
                    "vwidth": 640
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_7626dd7d1c3e48eea1230026126caf7d.f220.av.m3u8",
                    "definition": 220,
                    "vbitrate": 524288,
                    "vheight": 480,
                    "vwidth": 640
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_7626dd7d1c3e48eea1230026126caf7d.f30.mp4",
                    "definition": 30,
                    "vbitrate": 865828,
                    "vheight": 960,
                    "vwidth": 1280
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_7626dd7d1c3e48eea1230026126caf7d.f40.mp4",
                    "definition": 40,
                    "vbitrate": 1709293,
                    "vheight": 1440,
                    "vwidth": 1920
                }
            ]
        },
        {
            "fileId": "11624759161874546967",
            "fileName": "13425173277_2015-09-06-19-06-11_2015-09-06-19-16-11",
            "duration": 599,
            "status": "2",
            "image_url": "http://p.qpic.cn/videoyun/0/1203_8a5015084d4f47cd9a0bc5ecfe78aecb_1/640",
            "playSet": [
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f0.mp4",
                    "definition": 0,
                    "vbitrate": 246000,
                    "vheight": 480,
                    "vwidth": 640
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f10.mp4",
                    "definition": 10,
                    "vbitrate": 149193,
                    "vheight": 240,
                    "vwidth": 320
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f20.mp4",
                    "definition": 20,
                    "vbitrate": 297656,
                    "vheight": 480,
                    "vwidth": 640
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f220.av.m3u8",
                    "definition": 220,
                    "vbitrate": 524288,
                    "vheight": 480,
                    "vwidth": 640
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f30.mp4",
                    "definition": 30,
                    "vbitrate": 899976,
                    "vheight": 960,
                    "vwidth": 1280
                },
                {
                    "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f40.mp4",
                    "definition": 40,
                    "vbitrate": 1746652,
                    "vheight": 1440,
                    "vwidth": 1920
                }
            ]
        }
	 ]
}

```


