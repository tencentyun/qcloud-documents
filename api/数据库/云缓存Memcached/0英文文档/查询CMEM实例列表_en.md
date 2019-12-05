## 1. API Description

This API (DescribeCmem) is used to query CMEM instance list.
It can be called from regions of Guangzhou, Shanghai and North America.

Domain name: cmem.api.qcloud.com

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> limit <td> No <td> Int <td> Page size. Its default value is 20 and the maximum 100.
<tr>
<td> offset <td> No <td> Int <td> Offset. The default is 0.
<tr>
<td> vpcId <td> No <td> Int <td> VPC network ID. Its optional values are -1, 0 and normal vpcId, where -1 indicates all networks and 0 indicates basic network.
<tr>
<td> subnetId <td> No <td> Int <td> VPC subnet ID. The default value is -1, which means that this parameter is ignored.
</tbody></table>

 

## 3. Output Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Error code, 0: Succeeded, other values: Failed
<tr>
<tr>
<td> totalCount <td> Int <td> The total number of instances that meet the conditions except the "limit" and "offset" parameters. It can be used with "limit" and "offset" for paging queries.
<tr>
<td> message <td> String <td> Error message
<tr>
<td> data <td> Array <td> Returned array
<tr>
<td> data.cmemId <td> Int <td> MemcachedID
<tr>
<td> data.cmemName <td> String <td> Instance name
<tr>
<td> data.expire <td> Int <td> Used to switch on/off the "expire". The value 0 indicates disabled and 1 enabled.
<tr>
<td> data.status <td> Int <td> When the "status" is equal to 1, the operations, such as  "rename", "clear" and "enable expire", are possible.
<tr>
<td> data.autoRenew <td> Int <td> Automatic renewal flag. The value 0 indicates disabled and 1 enabled.
<tr>
<td> data.wanIp <td> String <td> Instance IP
<tr>
<td> data.port <td> Int <td> Instance service port
</tbody></table>

 

## 4. Example
 
Input
<pre>
  https://cmem.api.qcloud.com/v2/index.php?Action=DescribeCmem
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &limit=10
  &offset=0

</pre>
Output
```

{
    "code": 0,
    "message": "",
    "totalCount": 1,
    "data": [
        {
            "cmemId": 104017148,
            "cmemName": "test",
            "expire": 1,
            "status": 1,
            "autoRenew": 0,
            "wanIp": "10.66.152.150",
            "port": 9101,
            "projectId": 0
        }
    ]
}

```


