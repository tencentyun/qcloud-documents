## 1. API Description

This API (DescribeInstances) is used to query the details of one or more instances.

Domain name for API request: cvm.api.qcloud.com

* You can query the details of an instance according to its `ID`, name, or billing method. Filter information can be found in `Filter`.
* If the parameter is empty, a certain number (specified by `Limit`, the default is 20) of instances are returned to the current user.

## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version number, used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | array of Strings | No | To query according to one or more instance IDs, such as `ins-11112222`. For the format of this parameter, please see `id.N` section of API [Introduction](https://intl.cloud.tencent.com/document/product/213/11646). `InstanceIds` and `Filters` cannot be specified at the same time.
| Filters.N | array of [Filter](https://cloud.tencent.com/document/api/213/9451#filter) objects | No | Filter criteria can be found in Table of Instance Filter Criteria. The maximum number of `Filters` of each request is 10, and the maximum number of `Filter.Values` is 5. `InstanceIds` and `Filters` cannot be specified at the same time. |
| Offset | Integer | No | Offset. Default is 0. For more information on `offset`, please see relevant sections of API [Introduction](https://intl.cloud.tencent.com/document/product/213/11646). |
| Limit | Integer | No | Number of results to be returned. Default is 20. Maximum is 100. For more information on `limit`, please see relevant sections of API [Introduction](https://intl.cloud.tencent.com/document/product/213/11646). |

Table of Instance Filter Criteria

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| zone | String | No | (Filter criteria) Filter by [Availability Zone](/document/api/213/9452#zone). |
| project-id | Integer | No | (Filter criteria) Filter by project ID. You can query the list of created projects by calling [DescribeProject](/document/api/378/4400), or view the list by logging in to the [Console](https://console.cloud.tencent.com/project). You can also create a new project by calling [AddProject](https://intl.cloud.tencent.com/document/product/378/4398). |
| host-id | String | No | (Filter criteria) Filter by [CDH](/document/product/416) `ID`, such as: `host-11112222`. |
| instance-id | String | No | (Filter criteria) Filter by instance `ID`, such as: `ins-11112222`. |
| instance-name | String | No | (Filter criteria) Filter by instance name. |
| instance-charge-type | String| No | (Filter criteria) Filter by instance billing method. Value range:<br><li>POSTPAID_BY_HOUR: postpaid (by traffic)<br><li>CDHPAID: [CDH](/document/product/416) paid, i.e. only pay for [CDH](/document/product/416), excluding instances on the [CDH](/document/product/416). |
| private-ip-address | String| No | (Filter criteria) Filter by the private `IP` of the instance primary ENI. |
| public-ip-address | String | No | (Filter criteria) Filter by the private `IP` of the instance primary ENI, including `IP` automatically assigned when the instance is created and Elastic `IP` manually bound after the instance is created. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |
| TotalCount | Integer | Number of instances that meet the condition. |
| InstanceSet | array of [Instance](https://cloud.tencent.com/document/api/213/9451#instance) objects | List of instance details. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| InvalidParameter | Invalid parameter. Parameter does not meet the requirement or is not supported. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidHostId.Malformed | Invalid [CDH](/document/product/416) `ID`. Specified [CDH](/document/product/416) `ID` is in an incorrect format. For example, `host-1122` indicates `ID` length error. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidFilterValue.LimitExceeded | The number of values of parameter [Filter](https://cloud.tencent.com/document/api/213/9451#filter) exceeds the limit. |
| InvalidFilter | The specified [Filter](https://cloud.tencent.com/document/api/213/9451#filter) is not supported. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |
| InternalServerError | Internal service error. |


## 5. Example

Input

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstances
&Version=2017-03-12
&Filters.1.Name=zone
&Filters.1.Values.1=ap-guangzhou-1
&Filters.1.Values.2=ap-guangzhou-2
&Offset=0
&Limit=1
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

Output

<pre>
{
    "Response": {
        "TotalCount": 2,
        "InstanceSet": [
            {
                "Placement": {
                    "Zone": "ap-guangzhou-1",
                    "HostId": "",
                    "ProjectId": 0
                },
                "InstanceId": "ins-r8hr2upy",
                "InstanceType": "S1.SMALL2",
                "CPU": 1,
                "Memory": 2,
                "InstanceName": "\u6d4b\u8bd5\u5b9e\u4f8b",
                "SystemDisk": {
                    "DiskType": "CLOUD_BASIC",
                    "DiskId": "disk-4rnslbwq",
                    "DiskSize": 20
                },
                "DataDisks": [
                    {
                        "DiskType": "CLOUD_BASIC",
                        "DiskId": "disk-4rnslb35",
                        "DiskSize": 50
                    }
                ],
                "PrivateIpAddresses": [
                    "10.104.37.58"
                ],
                "PublicIpAddresses": [
                    "123.207.32.83"
                ],
                "InternetAccessible": {
                    "InternetMaxBandwidthOut": 2,
                    "PublicIpAssigned": "TRUE"
                },
                "VirtualPrivateCloud": {
                    "VpcId": "vpc-4e78ea76",
                    "SubnetId": "subnet-6d7kj98i",
                    "AsVpcGateway": "TRUE"
                },
                "ImageId": "img-0vbqvzfn",
                "CreatedTime": "2016-12-02T00:22:40Z",
                "ExpiredTime": "2017-01-02T00:22:48Z"
            }
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>

