## 1. API Description
 
Domain name: eip.api.qcloud.com
API name: DescribeEip

This API is used to query elastic public IP.

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> eipIds.n <td> No <td> String <td> List of EIP instance IDs, with subscripts starting with 0
<tr>
<td> eips.n <td> No <td> String <td> List of EIPs, with subscripts starting with 0
<tr>
<td> unInstanceIds.n <td> No <td> String <td> List of server instance IDs, with subscripts starting with 0. It can be obtained from unInstanceId in the returned field of <a href="http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeInstances">DescribeInstances</a> API.
<tr>
<td> networkInterfaceIds.n <td> No <td> String <td> List of unique IDs of ENIs, with subscripts starting with 0. It can be obtained from networkInterfaceId in the returned field of <a href="/doc/api/245/4814" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a> API.
<tr>
<td> privateIpAddresss <td> No <td> String <td> Private IP of the server.
<tr>
<td> searchKey <td> No <td> String <td> EIP Instance name (fuzzy match).
<tr>
<td> status.n <td> No <td> Int <td> Status list, with subscripts starting with 0<br>0: Creating...; 1: Binding...; 2: Bound; 3: Unbinding...; 4: Not bound; 6: Going offline...; 9: Failed to create
<tr>
<td> type <td> No <td> Int <td> 0: CVM; 1: NAT gateway
<tr>
<td> limit <td> No <td> Int <td> Return the number of EIPs. The default is 20 and the maximum is 100
<tr>
<td> offset <td> No <td> Int <td> Offset. The default is 0.
<tr>
<td> orderBy <td> No <td> String <td> Sorting field, which can be: EipId, eip, ispId, status, unInstanceId, arrears, createdAt
<tr>
<td> orderType <td> No <td> Int <td> 1: Backward sequence; 0: Forward sequence. The default is backward sequence.
</tbody></table>

 > In query API, a default maximum number of returned records is generally set for a single query. To traverse all resources, you need to use "limit" and "offset" for paging queries; For example, to query the 40 records between 110 and 149, you can set offset = 110 and limit = 40. 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values ​indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, please refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| totalCount | Int | Return the number of EIPs matching the filter criteria; if "limit" and "offset" are specified, the value may be greater than the number in the data list |
| data | Array | Return a list |

Data structure


<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> data.eipSet <td> Array <td> Return the EIP information list
<tr>
<td> data.eipSet.eipId <td> String <td> EIP instance ID
<tr>
<td> data.eipSet.eipName <td> String <td> EIP name
<tr>
<td> data.eipSet.eip <td> String <td> EIP address
<tr>
<td> data.eipSet.ispId <td> Int <td> Carrier ID<br> 0: China Telecom; 1: Unicom; 2: China Mobile; 3: CERNET; 4: PCCW; 5: BGP; 6: Hong Kong
<tr>
<td> data.eipSet.status <td> Int <td> Status<br> 0: Creating...; 1: Binding...; 2: Bound; 3: Unbinding...; 4: Not bound; 6: Going offline...; 9: Failed to create
<tr>
<td> data.eipSet.type <td> Int <td> Type<br> 0: CVM; 1: NAT gateway
<tr>
<td> data.eipSet.arrears <td> Int <td> Whether the EIP is isolated due to arrears<br> 1: Isolated due to arrears; 0: Normal. You cannot perform any administrative operation on an EIP isolated due to arrears.
<tr>
<td> data.eipSet.unInstanceId <td> String <td> The instance ID of the server to which the EIP is bound. If there is no binding between them, leave the parameter empty.
<tr>
<td> data.eipSet.networkInterfaceId <td> String <td> The unique ID of ENI
<tr>
<td> data.eipSet.privateIpAddress <td> String <td> Private IP of the server
<tr>
<td> data.eipSet.createdAt <td> String <td> Time of creation
<tr>
<td> data.eipSet.updatedAt <td> String <td> Time of updating
<tr>
<td> data.eipSet.freeSecond <td> Int <td> Duration (in seconds) in which the server was not bound to an EIP
</tbody></table>

 

## 4. Example
 
Input
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
</pre>

Output
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "eipSet": [
            {
                "eipId": "eip-co9m2t7k",
                "eipName": "",
                "eip": "119.29.239.140",
                "ispId": 5,
                "status": 2,
                "arrears": 0,
                "unInstanceId": "ins-pjrzryru",
                "createdAt": "2016-07-11 21:23:35",
                "updatedAt": "2016-07-11 21:23:35",
                "freeSecond": 0,
                "type": 0,
                "privateIpAddress": "10.104.211.58",
                "networkInterfaceId": ""
            }
        ]
    },
    "totalCount": 1
}

```

