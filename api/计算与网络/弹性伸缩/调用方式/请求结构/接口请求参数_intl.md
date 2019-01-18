API request parameters are specific to each API. This means that different APIs support different API request parameters. The first letter of each API request parameter is in lowercase so that the parameters can be differentiated from common request parameters.
Take the <a href="/doc/api/229/831" title="Query List of Instances">Query List of Instances</a>(DescribeInstances) API as an example. It supports the following API request parameters:

| Parameter Name | Required | Type | Description | 
|---------|---------|---------|---------|
| instanceIds.n  | No | String | An array containing the IDs of CVM instances to be queried. Array subscript starts from 0. You can use either instanceId or unInstanceId. The unified resource ID unInstanceId is recommended. |
| lanIps.n | No | String | Array of private IPs of the CVMs to be queried.  | 
| searchWord | No | String | CVM alias set by the user. |
| offset | No | Int | Offset. Default is 0.  | 
| limit | No | Int | The maximum number of servers allowed to be queried at a time. Default is 20, and the maximum is 100. |
| status | No | Int | Status of the CVM to be queried. |
| projectId | No | String | Project ID. If this parameter is left empty, the CVM instances of all projects will be queried. 0 means default project. To specify other projects, you can call the Query Project List API to query projects. |
| simplify | No | Int | Obtain non-real time data if simplify=1 is added when passing parameters. |
| zoneId | No | Int | ID of availability zone. If this parameter is left empty, the CVM instances of all availability zones will be queried. To specify availability zones, you can call the <a href="/doc/api/229/1286" title="Query Availability Zones">Query Availability Zones</a>(DescribeAvailabilityZones) API to query availability zones. |

Here are the descriptions of each field:
<table class="t">
<tbody>
<td> Parameter Name
</td><td> Name of request parameter supported by the API. The user can use this name as an API request parameter when using this API.<br>
Note: When a parameter name ends with ".n", it means the parameter is an array, and you need to pass the array parameters in sequence when using it. For example, for the API "Query List of Instances" (DescribeInstances), if you pass the parameter instanceIds.0=ins-0hm4gvho&instanceIds.1=ins-0hm4gvho, only CVM instances with IDs of ins-0hm4gvho and ins-0hm4gvho will be queried.
</td></tr>
<tr>
<td> Required
</td><td> Indicates whether this parameter is mandatory. "Yes" means the parameter is mandatory for the API, while "No" means the parameter is not mandatory. For the API "Query List of Instances" (DescribeInstances), all the API request parameters are not required, which means you can call the API successfully simply by using common request parameters.
</td></tr>
<tr>
<td> Type
</td><td> Data type of the API parameter.
</td></tr>
<tr>
<td> Description
</td><td> A brief description of the API request parameter.
</td></tr>
</tbody></table>

If a user wants to query the list of scaling groups, the request link may be as follows:

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

A complete request needs two types of request parameters: common request parameters and API request parameters. Only API request parameters are listed here. For information on common request parameters, refer to <a href="/doc/api/372/Common Request Parameters" title="Common Request Parameters">Common Request Parameters</a> section.
