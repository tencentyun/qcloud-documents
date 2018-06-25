## 1. API Description

This API (DescribeInstances) is used to query the details of one or more instances.

* You can query the details of an instance based on the information including instance `ID`, instance name, and instance billing method. For more information on filtering, please see the filter `Filter`.
* If the parameter is empty, a certain number (specified by `Limit`, the default is 20) of instances is returned to the current user.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: DescribeInstances |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |
| InstanceIds.N | No | Array of String | To query according to one or more instance IDs, such as `ins-11112222` (for the format of this parameter, please see `id.N` section of API [Introduction](https://cloud.tencent.com/document/api/213/15688)). The maximum number of instances of each request is 100. The parameter does not support specifying both `InstanceIds` and `Filters`. |
| Filters.N | No | Array of [Filter](/document/api/213/15753#Filter) | Filter criteria. <li>zone - String - Required: No - (Filter criteria) Filter by availability zone. </li><li>project-id - Integer - Required: No - (Filter criteria) Filter by project ID. You can view the list of created projects by calling [DescribeProject](https://cloud.tencent.com/document/api/378/4400) or log in to the [console](https://console.cloud.tencent.com/cvm/index); you can also call [AddProject](https://cloud.tencent.com/document/api/378/4398) to create a project. </li><li>host-id - String - Required: No - (Filter criteria) Filter by [CDH](https://cloud.tencent.com/document/product/416) ID. The form of [CDH](https://cloud.tencent.com/document/product/416) ID is like: host-11112222. </li><li>instance-id - String - Required: No - (Filter criteria) Filter by instance ID. The form of instance ID is like: ins-11112222. </li><li>instance-name - String - Required: No - (Filter criteria) Filter by instance name. </li><li>instance-charge-type - String - Required: No - (Filter criteria) Filter by the billing method of instance. (PREPAID: prepaid (by year/month) &#124; POSTPAID_BY_HOUR: postpaid (by traffic) &#124; CDHPAID: [CDH](https://cloud.tencent.com/document/product/416) paid, i.e., only pay for [CDH](https://cloud.tencent.com/document/product/416), excluding instances on the [CDH](https://cloud.tencent.com/document/product/416).) </li><li>private-ip-address - String - Required: No - (Filter criteria) Filter by the private IP of instance primary ENI. </li><li> public-ip-address - String - Required: No - (Filter criteria) Filter by the public IP of instance primary ENI, including the IP automatically assigned when the instance is created and the EIP bound manually when the instance is created. </li>The maximum number of `Filters` of each request is 10, and the maximum number of `Filter.Values`' is 5. The parameter does not support specifying both `InstanceIds` and `Filters`. |
| Offset | No | Integer | Offset. Default is 0. For more information on `offset`, please see relevant sections of API [Introduction](https://cloud.tencent.com/document/api/213/15688). |
| Limit | No | Integer | Number of returned results. The default is 20, and the maximum is 100. For more information on `limit`, please see relevant sections of API [Introduction](https://cloud.tencent.com/document/api/213/15688). |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of instances that meet the condition. |
| InstanceSet | Array of [Instance](/document/api/213/15753#Instance) | Instance details list. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidFilter | Invalid filter. |
| InvalidFilterValue.LimitExceeded | The number of values of parameter [`Filter`](/document/api/213/9451#filter) exceeds the limit. |
| InvalidHostId.Malformed | Invalid [CDH](https://cloud.tencent.com/document/product/416) `ID`. The specified [CDH](https://cloud.tencent.com/document/product/416) `ID`format is incorrect. For example, `ID` length error `host-1122`. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` format is incorrect. For example, `ins-1122` indicates an ID length error. |
| InvalidParameter | Invalid parameter. The parameter does not meet requirements or the parameter is not supported. |
| InvalidParameterValue | Invalid parameter value. The format of the parameter value is incorrect or the parameter value is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |

## 5. Example

## Example 1 View the List of Instances

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstances
&Filters.0.Name=zone
&Filters.0.Values.0=ap-guangzhou-1
&Filters.0.Values.1=ap-guangzhou-2
&Offset=0
&Limit=1
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "InstanceSet": [
      {
        "CPU": 1,
        "CreatedTime": "2016-12-02T00:22:40Z",
        "DataDisks": [
          {
            "DiskId": "disk-4rnslb35",
            "DiskSize": 50,
            "DiskType": "CLOUD_BASIC"
          }
        ],
        "ExpiredTime": "2017-01-02T00:22:48Z",
        "ImageId": "img-0vbqvzfn",
        "InstanceChargeType": "PREPAID",
        "InstanceId": "ins-r8hr2upy",
        "InstanceName": "Test instance",
        "InstanceType": "S1.SMALL2",
        "InternetAccessible": {
          "InternetChargeType": "BANDWIDTH_PREPAID",
          "InternetMaxBandwidthOut": 2,
          "PublicIpAssigned": "TRUE"
        },
        "Memory": 2,
        "Placement": {
          "HostId": "",
          "ProjectId": 0,
          "Zone": "ap-guangzhou-1"
        },
        "PrivateIpAddresses": [
          "10.104.37.58"
        ],
        "PublicIpAddresses": [
          "123.207.32.83"
        ],
        "RenewFlag": "NOTIFY_AND_AUTO_RENEW",
        "SystemDisk": {
          "DiskId": "disk-4rnslbwq",
          "DiskSize": 20,
          "DiskType": "CLOUD_BASIC"
        },
        "VirtualPrivateCloud": {
          "AsVpcGateway": "TRUE",
          "SubnetId": "subnet-6d7kj98i",
          "VpcId": "vpc-4e78ea76"
        }
      }
    ],
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7",
    "TotalCount": 2
  }
}
```
