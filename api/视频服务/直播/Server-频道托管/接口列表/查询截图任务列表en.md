## 1. API Description

Domain name: live.api.qcloud.com
API name: DescribeLVBShotList


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
<td> pageNo
<td> No
<td> Int
<td> Page number, 1 by default
<tr>
<td> pageSize
<td> No
<td> Int
<td> Page size, 10 by default

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
<td> totalCount
<td> Int
<td>Total number
<tr>
<td> taskSet
<td> Array
<td> Task result set
</tbody></table>

</b></th>

The file information structure is as follows:
</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> id
<td> Int
<td> Task ID
<tr>
<td> startTime
<td> String
<td> Fragment start time
<tr>
<td> endTime
<td> String
<td> Fragment end time
<tr>
<td> status
<td> Int
<td> Task status, 0 - Not started, 1 – Starting, 2 – Done, 3 – Exception, and so on

</tbody></table>
