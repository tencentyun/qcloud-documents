API request parameters are specific to each API. This means that different APIs support different API request parameters. The first letter of each API request parameter is lowercase so that the parameter can be differentiated from common request parameters.
Take the API <a href="/doc/api/229/831" title="Query List of Instances">Query List of Instances</a>(DescribeInstances) as an example. It supports the following API request parameters:

| Parameter Name | Required | Type | Description | 
|---------|---------|---------|---------|
| instanceIds.n  | No | String | Array of IDs of CVM instances to be queried. The array subscript starts with 0. You can use instanceId and unInstanceId. The unified resource ID unInstanceId is recommended. |
| lanIps.n | No | String | Array of private IPs of CVMs to be queried.  | 
| searchWord | No | String | CVM alias set by the user. |
| offset | No | Int | Offset; default is 0.  | 
| limit | No | Int | The maximum number of servers allowed to be queried at a time. Default is 20, and the maximum is 100. |
| status | No | Int | Status of CVM to be queried. |
| simplify | No | Int | Obtain non-real time data if simplify=1. |
| zoneId | No | Int | ID of availability zone. If it is left empty, the CVM instances of availability zones will be queried. To specify availability zones, you can call API <a href="/doc/api/229/1286" title="Query Availability Zones">Query Availability Zones</a>(DescribeAvailabilityZones) to query availability zones. |

The description of each field is as follows:
<table class="t">
<tbody>
<td> Parameter Name
</td><td> The name of request parameter supported by the API, which the user can use as an API request parameter when using this API.<br>
Note: When a parameter name ends with ".n", it means the parameter is an array, and you need to input the array parameters in sequence when using it. For example, in the API "Query List of Instances" (DescribeInstances), if you input the parameter instanceIds.0=ins-0hm4gvho&instanceIds.1=ins-0hm4gvho, only CVM instances with IDs of ins-0hm4gvho and ins-0hm4gvho will be queried.
</td></tr>
<tr>
<td> Required
</td><td> Indicate whether this parameter is mandatory. "Yes" means the parameter is mandatory for the API, while "No" means the parameter is not mandatory. In the API "Query List of Instances" (DescribeInstances), all the API request parameters are not required, so the API call can be achieved simply by using common request parameters.
</td></tr>
<tr>
<td> Type
</td><td> The data type of the API parameter.
</td></tr>
<tr>
<td> Description
</td><td> A brief description of the API request parameter.
</td></tr>
</tbody></table>

If a user wants to query the scaling group list, the request link may be as follows:

```
https://cvm.api.qcloud.com/v2/index.php?
&<Common request parameters>
&instanceIds.0=ins-0hm4gvho
&instanceIds.1=ins-8oby8q00
&offset=0
&limit=20
&status=2
&zoneId=100003
```

A complete request needs two types of request parameters: common request parameters and API request parameters. Only API request parameters are listed here. For information on common request parameters, refer to <a href="/doc/api/372/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> section.
