## 1. API Description

Domain name: live.api.qcloud.com
API name: DescribeRecord

Note: Recording files are stored on the VOD platform. If you want to use the recording function, you need to activate a VOD account first and then ensure that the account is available. When recording files are stored, the charges (including charges for storage and downstream playback traffic) are calculated with VOD billing method. For more information, refer to [Relevant Document](https://www.qcloud.com/document/product/267/2818).


## 2. Input parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> channelId
<td> Yes
<td> String
<td> Channel ID
<tr>
<td> taskId
<td> Yes
<td> Int
<td> Task ID
<tr>
<td> pageNo
<td> No
<td> Int
<td> Page number, 1 by default
<tr>
<td> pageSize
<td> No
<td> Int
<td> Page size, 10 by default
<tr>

</tbody></table>


</b></th>

## 3. Output parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code, 0: succeeded; other values: failed
<tr>
<td> message
<td> String
<td> Error message
<tr>
<tr>
<td> totalCount
<td> Int
<td>Total number
<tr>
<tr>
<td> fileSet
<td> Array
<td> File result set
<tr>
</tbody></table>

The file information structure is as follows:

<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileId
<td> String
<td> File ID
<tr>
<td> startTime
<td> String
<td> Fragment start time
<tr>
<tr>
<td> endTime
<td> String
<td> Fragment end time
<tr>
<tr>
<td> fileName
<td> String
<td> File name
<tr>
</tbody></table>

</b></th>

## 4. Example

Input 1
<pre>

http://domain/v2/index.php?Action=DescribeRecord&channelId=16093104850681751595&taskId=10&pageSize=10&pageNo=1&<a href="https://www.qcloud.com/doc/api/229/6976">Public Request Parameters</a>



</pre>

Output 1
```
{

    "code": 0,
    "message": "",
    "totalCount": 2,
    "fileSet": [
        {
            "fileId": "16093104850681751583",
            "startTime": "7",
            "endTime": "720",
            "fileName": "LVB -sparrow_hls-20160120-0958-20160120-1010"
        },
        {
            "fileId": "16093104850681751599",
            "startTime": "8",
            "endTime": "1806",
            "fileName": "LVB -sparrow_hls-20160120-1010-20160120-1040"
        }
    ]

}

```
After the recording, the VOD platform will generate a file, for example, 
http://2527.vod.myqcloud.com/2527_000007d0b18*****bd98f9125ed6569ee9a90001.f0.mp4
Complete information on access methods can be found from fileId and [VOD API](http://www.qcloud.com/doc/api/257/API%E6%A6%82%E8%A7%88).
