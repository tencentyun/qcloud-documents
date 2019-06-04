## 1. API Description

Domain name: live.api.qcloud.com
 

Note: This API (DescribeRecord) is used to store recorded files on the VOD platform. If you want to use the recording feature, you need to activate a VOD account first and ensure that the account is available. When recording files are stored, the charges (including charges for storage and downstream playback traffic) are calculated with VOD billing method. For more information, please see [relevant document](https://cloud.tencent.com/document/product/267/2818).



## 2. Input Parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
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
<td> Page number. Default is 1
<tr>
<td> pageSize
<td> No
<td> Int
<td> Page size. Default is 10
<tr>

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
<td> Error code. 0: Successful; other values: Failed
<tr>
<td> message
<td> String
<td> Error message
<tr>
<tr>
<td> totalCount
<td> Int
<td> Total number
<tr>
<tr>
<td> fileSet
<td> Array
<td> File result set
<tr>
</tbody></table>

The file information is composed as follows:

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileId
<td> String
<td> File ID
<tr>
<td> startTime
<td> String
<td> Time when the fragmentation process starts
<tr>
<tr>
<td> endTime
<td> String
<td> Time when the fragmentation process ends
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

http://domain/v2/index.php?Action=DescribeRecord&channelId=16093104850681751595&taskId=10&pageSize=10&pageNo=1&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>



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
After the recording, the VOD platform will generate a file, for example:
`http://2527.vod.myqcloud.com/2527_000007d0b18*****bd98f9125ed6569ee9a90001.f0.mp4`
Complete information on access methods can be found via field and API [VOD API](https://cloud.tencent.com/document/product/266/8586)

