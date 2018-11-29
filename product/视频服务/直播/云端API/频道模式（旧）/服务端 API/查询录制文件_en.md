## 1. API Description
Domain name: live.api.qcloud.com

API name: GetVodRecordFiles

Query the result of the recorded file of channel, including file name, task ID, file ID, and recording message.


## 2. Input Parameters
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> channelId
<td> <font color"red">Yes</font>
<td> Int
<td> Channel ID
<tr>
<td> startTime
<td> <font color"red">Yes</font>
<td> String
<td> Enter the value encoded from YYYY-MM-DD HH:MM:SS
For example: 2016-01-01%2000:00:00 (encoded from 2016-01-01 00:00:00)
<tr>
<td> endTime
<td> <font color"red">No</font>
<td> String
<td> Enter YYYY-MM-DD HH:MM:SS (encoded value). There is no limit on the end time by default

<tr>
<td> pageNum
<td> <font color"red">No</font>
<td> Int
<td> Page number. Default is 1
<tr>
<td> pageSize
<td> <font color"red">No</font>
<td> Int
<td> Number of records in a page. Default is 20

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
<td> total_count
<td> int
<td> Total number of returned files
<tr>
<td> filesInfo
<td> Array
<td>   [ {
            "fileId": "9896125784085567721",
            "fileName": "LVB -aaa-20160112-1455-20160112-1457",
            "reportMessage": null,
            "taskId": "57",
            "startTime": "7",
            "endTime": "128"
        }]
</tbody></table>

</b></th>

## 4. Example

Input 1
<pre>
https://domain/v2/index.php?Action=GetVodRecordFiles&channelId=9896125784085535840&startTime=2016-01-01+00%3A00%3A00&pageNum=1&pageSize=20

</pre>

Output 1
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "filesInfo": [
        {
            "fileId": "9896125784085567721",
            "fileName": "LVB -aaa-20160112-1455-20160112-1457",
            "reportMessage": null,
            "taskId": "57",
            "startTime": "7",
            "endTime": "128"
        },
        {
            "fileId": "9896125784085567722",
            "fileName": "LVB -aaa-20160112-1457-20160112-1459",
            "reportMessage": null,
            "taskId": "57",
            "startTime": "128",
            "endTime": "250"
        },
        {
            "fileId": "9896125784085567723",
            "fileName": "LVB -aaa-20160112-1459-20160112-1459",
            "reportMessage": null,
            "taskId": "57",
            "startTime": "250",
            "endTime": "299"
        },
        {
            "fileId": "9896125784085567727",
            "fileName": "LVB -aaa-20160112-1510-20160112-1512",
            "reportMessage": null,
            "taskId": "58",
            "startTime": "7",
            "endTime": "132"
        },
        {
            "fileId": "9896125784085567736",
            "fileName": "LVB -aaa-20160112-1512-20160112-1514",
            "reportMessage": null,
            "taskId": "58",
            "startTime": "132",
            "endTime": "258"
        },
        {
            "fileId": "9896125784085567739",
            "fileName": "LVB -aaa-20160112-1514-20160112-1515",
            "reportMessage": null,
            "taskId": "58",
            "startTime": "258",
            "endTime": "301"
        },
        {
            "fileId": "9896125784085567756",
            "fileName": "LVB -aaa-20160112-1525-20160112-1526",
            "reportMessage": null,
            "taskId": "61",
            "startTime": "7",
            "endTime": "60"
        }
    ],
    "totalCount": 7
}

```

