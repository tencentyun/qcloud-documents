## 1. API Description
This API (DescribeEipBm) is used to query the list of EIPs in use.

Domain: <font style="color:red">eip.api.qcloud.com</font>

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|-------|----|---|----|----|
| eipIds.n | No | String | List of EIP instance IDs, with the subscripts starting from 0 |
| eips.n | No | String | List of EIPs, with the subscripts starting from 0 |
| unInstanceIds.n | No | String | List of CPM instance IDs, with the subscript starting from 0. It can be obtained from "instanceId" in the returned fields of API [DescribeDevice](/doc/api/456/6728) |
| searchKey | No | String | Name of EIP instance (fuzzy match) |
| status.n | No | Int |Status list, with the subscripts starting from 0<br>0: Creating; 1: Binding; 2: Bound; 3: Unbinding; 4: Unbound; 6: Going offline; 9: Creation failed |
| offset | No | Int | Offset; default is 0 |
| limit | No | Int | Number of returned EIPs. Default is 20 and maximum is 100 |
| orderBy | No | String | Sorting field. Supported values: eipId, eip, status, unInstanceId, arrears, and createdAt. [View the description](# datastruct) |
| orderType | No | Int | 1: Backward sequence; 0: Forward sequence. Default is backward sequence |
| vpcId | No | Int | The vpcId to which the EIP belongs. EIPs belonging to the specified VPC will be filtered out |
| payMode | No | String | Billing mode. flow: Bill By Traffic; bandwidth: Bill by Bandwidth |

 > For query APIs, a default maximum number of returned records is generally set for a single query. To traverse all the resources, you need to use "limit" and "offset" for paging queries; For example, to query the 40 records between 110 and 149, you can set offset = 110 and limit = 40.

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725).  |
| message | String | Error message |
| codeDesc | String | Error code description |  
| totalCount | Int | Return the number of EIPs matching the filter criteria; if "limit" and "offset" are specified, the value may be greater than the number in the data array |
| data | Array | Return list of EIP instances. For more information on its composition, please see below |

<span id="datastruct">Parameter data is composed as follows:</span>

| Parameter Name | Type | Description |
|---|---|---|
| data.eipSet | Array | Return the EIP information array |
| data.eipSet.eipId | String | EIP instance ID |
| data.eipSet.eipName | String | EIP name |
| data.eipSet.eip | String | EIP address |
| data.eipSet.ispId | Int | ISP ID 0: China Telecom; 1: China Unicom; 2: China Mobile; 3: CERNET; 4: PCCW; 5: BGP; 6: Hong Kong |
| data.eipSet.status | Int | Status. 0: Creating 1: Binding; 2: Bound; 3: Unbinding; 4: Unbound; 6: Going offline; 9: Creation failed |
| data.eipSet.arrears | Int | Whether the EIP is isolated due to arrears 1: Isolated due to arrears; 0: Normal. You cannot perform any administrative operation on an EIP isolated due to arrears. |
| data.eipSet.unInstanceId | String | ID of CPM instance to which the EIP is bound. If there is no binding between them, leave the parameter empty |
| data.eipSet.freeAt | String | Unbinding time of EIP |
| data.eipSet.createdAt | String | Creation time of EIP |
| data.eipSet.updatedAt | String | Update time of EIP |
| data.eipSet.freeSecond | Int | Duration in which the EIP is not bound to CPM (in seconds) |
| data.eipSet.payMode | String | Billing mode of EIP. "flow": Bill by Traffic; "bandwidth": Bill by Bandwidth |
| data.eipSet.bandwidth | Int | The upper limit of bandwidth in the mode of "Bill by Bandwidth (in MB) |
| data.eipSet.latestPayMode | String | Billing mode of EIP upon the last change. "flow": Bill by Traffic; "bandwidth": Bill by Bandwidth |
| data.eipSet.latestBandwidth | Int | The upper limit of bandwidth for the EIP billing mode upon the last change (in MB). It is only available in the mode of "Bill by Bandwidth". |

## 4. Error Codes
| Error Code | Error Message | Error Description |
|---|---|---|
| 9003 | ParamInvalid | Incorrect request parameter |
| 9006 | InternalErr | An error occurred with internal data operation |


## 5. Example
 
Input
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &Action=DescribeEipBm
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>&startNum=0&endNum=20
</pre>

Output
```

{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"eipSet": [{
			"eipId": "eip-qcloudbm",
			"eipName": "",
			"eip": "111.111.111.111",
			"ispId": 5,
			"status": 4,
			"arrears": 0,
			"unInstanceId": "",
			"freeAt": "2016-10-13 11:23:19",
			"createdAt": "2016-10-13 11:23:18",
			"updatedAt": "2016-10-13 11:23:19",
			"freeSecond": 3600,
			"type": null,
			"payMode": "bandwidth",
			"bandwidth": 10,
			"latestPayMode": "flow",
			"latestBandwidth": 0
		}]
    },
    "totalCount": 1
}

```


