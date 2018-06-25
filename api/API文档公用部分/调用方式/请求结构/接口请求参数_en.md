A complete Tencent Cloud API request requires two types of request parameters: common request parameter and API request parameter. This document will describe API request parameters used in Tencent Cloud API requests. For more information about common request parameters, please see [Common Request Parameters](/document/api/377/4153).
API request parameters depend on specific APIs. Different APIs support different API request parameters. In order to differentiate from common request parameters, the initial letters of API request parameters are all lowercases.
>**Note:**
>The parameters in this document use Tencent Cloud CVM as example. For actual parameters for other Tencent Cloud products, refer to their API parameter instructions accordingly.

The following parameter list uses the Tencent Cloud CVM API DescribeInstances as example. This API supports the following API request parameters:

| Parameter | Description | Type | Required |
|---------|---------|---------|---------|
| instanceIds.n | Array of IDs of CVMs to be queried. The array subscript starts from 0. Both instanceId and unInstanceId are supported, but it is recommended to use unified resource ID: unInstanceId. | String | No |
| lanIps.n | Array of private IPs of the CVMs to be queried. | String | No |
| searchWord | CVM alias set by the user. | String | No |
| offset | Offset. Default is 0. | Int | No |
| limit | The maximum number of servers allowed to be queried at a time. Default is 20, and the maximum is 100. | Int | No |
| status | Status of the CVM to be queried. | Int | No |
| projectId | Project ID. CVM instances of all projects are queried if this is left empty. 0 indicates default project. Call the API [DescribeProject](/document/product/378/4400)  to look for the IDs of other projects. | String | No |
| simplify | Obtain non-real time data if simplify=1 is added when passing parameters. | Int | No |
| zoneId | Availability zone ID. CVM instances of all availability zones are queried if this is left empty. Call the API [DescribeAvailabilityZones](/doc/api/229/1286) to look for the IDs of other availability zones. | Int | No |

The fields are described as below:

**Parameter name:** Request parameter name supported by the API. Users can use this as API request parameter when using this API. A parameter name which ends with ".n" indicates that the parameter is an array, and array parameters need to be passed when using this parameter.
**Required:** Indicate whether this parameter is required. "Yes" means the parameter is required when you call the API. "No" means the parameter can be left empty.
**Type:** Data type of the API parameter.
**Description:** A brief description of the API request parameter.

### Example
The format of API request parameters in API request links for Tencent Cloud products are shown below. Take Tencent Cloud CVM as example, suppose a user needs to query the list of scaling groups, the request link should be:

<pre>
https://cvm.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&instanceIds.0=ins-0hm4gvho
&instanceIds.1=ins-8oby8q00
&offset=0
&limit=20
&status=2
&zoneId=100003
</pre>


