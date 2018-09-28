A complete Tencent Cloud API request requires two types of request parameters: common request parameters and API request parameters. This document describes API request parameters used in Tencent Cloud API requests. For more information about common request parameters, see [Common Request Parameters](https://cloud.tencent.com/document/product/582/13381).
API request parameters vary with different APIs. The initial letter of each API request parameter is in lowercase so that it can be differentiated from a common request parameter.
>**Note:**
>This document illustrates parameters specific to Tencent Cloud CVMs. For parameters specific to other Tencent Cloud products, see the relevant API documents.

For example, the Tencent Cloud CVM API [Query Instance List](/document/api/229/831) (DescribeInstances) supports the following API request parameters:

| Parameter Name | Description | Type | Required |
|---------|---------|---------|---------|
| instanceIds.n | An array containing the IDs of CVM instances to be queried, with the subscripts starting from 0. You can use either instanceId or unInstanceId. The unified resource ID unInstanceId is recommended. | String | No |
| lanIps.n | Array of private IPs of the CVMs to be queried. | String | No |
| searchWord | CVM alias set by the user. | String | No |
| offset | Offset. Default is 0. | Int | No |
| limit | The maximum number of servers that can be queried at a time. Default is 20, and the maximum is 100. | Int | No |
| status | Status of the CVM to be queried. | Int | No |
| projectId | Project ID. If this parameter is left empty, the CVM instances of all projects will be queried. 0 indicates the default project. Call the [Query Project List](/document/product/378/4400) (DescribeProject) API to query other projects. | String | No |
| simplify | Obtain non-real time data if simplify=1 in the input parameter | Int | No |
| zoneId | Availability zone ID. If this parameter is left empty, the CVM instances of all availability zones will be queried. Call the [Query Availability Zones](/document/api/229/1286) (DescribeAvailabilityZones) API to query the specified availability zone. | Int | No |

The elements of each parameter are described as follows:

**Parameter Name:** The request parameter name supported by the API. You can use it as an API request parameter when calling the API. A parameter name that ends with ".n" represents an array, for which you need to input the array parameters individually.
**Required:** Indicates whether this parameter is required. "Yes" means the parameter is required when you call the API. "No" means the parameter can be left empty.
**Type:** Data type of the API parameter.
**Description:** A brief description of the API request parameter.

### Use Case
The following example shows how API request parameters look in an API request link for a Tencent Cloud product. If, for example, you want to query the list of scaling groups for a Tencent Cloud CVM, the request link should look like this:

<pre>
https://cvm.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/document/api/229/6976">Common request parameters</a>>
&instanceIds.0=ins-0hm4gvho
&instanceIds.1=ins-8oby8q00
&offset=0
&limit=20
&status=2
&zoneId=100003
</pre>


