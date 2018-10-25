## 1. API Description
 
This API (DescribeRecordPlayInfo) is used to help ILVB users to acquire video information, which is only available to ILVB users. It Acquires video information list according to video file name.

Domain: vod.api.qcloud.com

## 2. Input Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> vid
<td> Yes
<td> String
<td> ID of the file returned by ILVB recording feature
<tr>
<td> notifyUrl
<td> No
<td> String
<td> Call-back address, used to notify that file recording is complete and whether transcoding process is finished
You need to pass this parameter to receive corresponding call-back content before relevant actions are finished. Otherwise there will be no call-back content.
<tr>
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
<td> fileSet
<td> Array
<td> Video list result set
<tr>
</tbody></table>
<tr>


</b></th>fileSet video list result set</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> vid
<td> String
<td> ID of recorded file
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
<td> Video status. -1: Upload incomplete, does not exist; 0: Initialize, not in use; 1: Verification failed, not in use;
2: Normal; 3: Paused; 4: Transcoding; 5: Publishing; 6: Deleting; 7: Transcode failed; 10: Waiting to be transcoded; 11: Transcoding partially completed (final state) 100: Deleted
<tr>
<tr>
<td> imageUrl
<td> String
<td> Video cover image
<tr>
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
<tr>
<td> definition
<td> Int
<td> Format. 0:  ["", "Original"], 1:  ["With watermark", "Original"], 10:  ["Mobile phone", "mp4"], 20:  ["Standard definition", "mp4"], 
30:  ["High definition", "mp4"], 210:  ["Mobile phone", "hls"], 220:  ["Standard Definition", "hls"], 230:  ["High definition", "hls"]
<tr>
<td> vbitrate
<td> Int
<td> Bit rate. Unit: kbps
<tr>
<td> vheight
<td> String
<td> Height. Unit: px
<tr>
<td> vwidth
<td> String
<td> Width. Unit: px
<tr>
</tbody></table>
 

## 4. Example
 
 Query by a video ID 
Input
<pre>
https://domain/v2/index.php?Action=DescribeRecordPlayInfo &vid=1200_c5997fa0f77745a49824150da4e4a6cc&notifyUrl=test.com
 &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>

</pre>
Output
```

{
    "code": 0,
    "message": "",
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
	 ]

}

```


