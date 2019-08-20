API request parameters depends on specific APIs. Different APIs support different API request parameters. The first letter of API request parameters is lowercase to distinguish them from public request parameters.
We here use DescribeInstances as an example. It supports these API request parameters:

| Parameter | Required | Type | Description | 
|---------|---------|---------|---------|
| instanceIds.n | No | String | ID array of CVM instances to be queried (starting from 0). You can use instanceId and unInstanceId, and the uniform resource ID: unInstanceId is recommended. |
| lanIps.n | No | String | Private IP array of CVMs to be queried.  | 
| searchWord | No | String | User-defined CVM name. |
| offset | No | Int | Offset value, which defaults to 0.  | 
| limit | No | Int | The maximum number of CVM that can be queried at one time. The default is 20 and the maximum is 100. |
| status | No | Int | Status of the CVM to be queried. |
| projectId | No | String | Project ID. The CVM instances for all projects are queried if it is not specified. 0 indicates the default project. If you want to specify a different project, you can call the DescribeProject API to query. |
| simplify | No | Int | Obtains non-real time data. When simplify = 1 is specified, then non-real time data is obtained. |
| zoneId | No | Int | Availability zone ID. The CVM instances for all availability zones are queried if it is not specified. To specify an availability zone, you can call the DescribeAvailabilityZones API to query. |

The fields are described as follows:

 Parameter
 Name of the request parameters supported by this API. You can use it as an API request parameter when using this API. 

Note: If the parameter name is ended with ".n", it indicates that this parameter is an array. Then you need to specify array parameters in sequence. For the DescribeInstances API, if you specify the parameter instanceIds.0=ins-0hm4gvho&instanceIds.1=ins-0hm4gvho, only the CVM instances with the IDs of ins-0hm4gvho and ins-0hm4gvho are queried.
 Required
 Indicates whether this parameter is required. "Yes" means that this parameter must be specified to call this API; "No" means that it may not be specified. In the DescribeInstances API, all API request parameters are not mandatory. You can call this API using common request parameters.
 Type
 Data type of this API parameter.
 Description
 Describes briefly the content of this API request parameter.


If you want to query the auto scaling group list, the request should be:

https://cdb.api.qcloud.com/v2/index.php?
&<Common request parameters>
&instanceIds.0=ins-0hm4gvho
&instanceIds.1=ins-8oby8q00
&offset=0
&limit=20
&status=2
&zoneId=100003


A complete request requires two types of request parameters: common request parameters and API request parameters. Only API request parameter are listed here. For more information about common request parameters, refer to [Common request parameters](https://intl.cloud.tencent.com/document/api/377/4153)