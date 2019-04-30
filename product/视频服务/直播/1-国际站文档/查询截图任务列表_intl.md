## 1. API Description

Domain name: live.api.qcloud.com
 


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
<td> pageNo
<td> No
<td> Int
<td> Page number. Default is 1
<tr>
<td> pageSize
<td> No
<td> Int
<td> Page size. Default is 10

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
<td> totalCount
<td> Int
<td> Total number
<tr>
<td> taskSet
<td> Array
<td> Task result set
</tbody></table>

</b></th>

The file information is composed as follows:
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> id
<td> Int
<td> Task ID
<tr>
<td> startTime
<td> String
<td> Time when the fragmentation process starts
<tr>
<td> endTime
<td> String
<td> Time when the fragmentation process ends
<tr>
<td> status
<td> Int
<td> Task status. 0 - Not started, 1 - Starting, 2 - Completed, 3 - Exception

</tbody></table>

## 4. Example

Input 1
<pre>

http://domain/v2/index.php?Action=DescribeLVBShotList&channelId=16093104850681751595&pageSize=10&pageNo=1&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>

</pre>

Output 1
```
{

    "code": 0,
    "message": "",
    "totalCount": 2,
    "taskSet ": [
        {
            "id": "16093104850681751583",
            "startTime": "7",
            "endTime": "720",
            "status ": "2
        },
        {
            "id": "16093104850681751599",
            "startTime": "8",
            "endTime": "1806",
            "status ": "2"
        }
    ]

}

```

