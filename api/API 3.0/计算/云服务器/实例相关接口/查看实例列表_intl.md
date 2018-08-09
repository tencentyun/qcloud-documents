## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeInstances) is used to query the details of one or more instances.

* You can query the details of an instance according to its `ID`, name, or billing method. See `Filter` for filtering information.
* If the parameter is empty, a certain number (specified by `Limit`, the default is 20) of instances are returned to the current user.

A maximum of 40 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeInstances |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceIds.N | No | Array of String | Query by one or more instance IDs, such as `ins-11112222`. (For the format of this parameter, please see the `id.N` section in the API [Introduction](https://cloud.tencent.com/document/api/213/15688)). A maximum of 100 instances are allowed for each request. The parameter does not support specifying both `InstanceIds` and `Filters`. |
| Filters.N | No | Array of [Filter](/document/api/213/##Filter) | Filter conditions.<br/><li> zone - String - Required: No - (Filter condition) Filter by availability zone.</li><li> project-id - Integer - Required: No - (Filter condition) Filter by project ID. You can view the list of created projects by calling [DescribeProject](https://cloud.tencent.com/document/api/378/4400) or by logging in to the [console](https://console.cloud.tencent.com/cvm/index). You can also create a new project by calling [AddProject](https://cloud.tencent.com/document/api/378/4398).</li><li> host-id - String - Required: No - (Filter condition) Filter by [CDH](https://cloud.tencent.com/document/product/416) ID. Example of a [CDH](https://cloud.tencent.com/document/product/416) ID: host-11112222.</li><li> instance-id - String - Required: No - (Filter condition) Filter by instance ID. Example of an instance ID: `ins-11112222`.</li><li> instance-name - String - Required: No - (Filter condition) Filter by instance name.</li><li> instance-charge-type - String - Required: No - (Filter condition) Filter by instance billing method. (PREPAID: prepaid (by year/month) &#124;POSTPAID_BY_HOUR: postpaid (by traffic) &#124; CDHPAID: [CDH](https://cloud.tencent.com/document/product/416) paid, i.e., only pay for [CDH](https://cloud.tencent.com/document/product/416), excluding instances on the [CDH](https://cloud.tencent.com/document/product/416). )  </li><li> private-ip-address - String - Required: No - (Filter condition) Filter by the private IP of the instance primary ENI.</li><li> public-ip-address - String - Required: No - (Filter condition) Filter by the public IP of the instance primary ENI, including the IP automatically assigned when an instance is being created and the EIP manually bound after the instance has been created.</li><li> tag-key - String - Required: No - (Filter condition) Filter by tag key.</li><li> tag-value - String - Required: No - (Filter condition) Filter by tag value.</li><li> tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key is replaced with the specific tag key. See Example 2 for usage.</li><br/>The maximum number of `Filters` for each request is 10, and that of `Filters.Values` is 5. The parameter does not support specifying both `InstanceIds` and `Filters`. |
| Offset | No | Integer | Offset. Default is 0. For more information about `Offset`, please see the relevant section in API [Introduction](https://cloud.tencent.com/document/api/213/15688). |
| Limit | No | Integer | Number of values to be returned. Default is 20. Maximum is 100. For more information about `Limit`, please see the relevant section in API [Introduction](https://cloud.tencent.com/document/api/213/15688). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of instances matching the filter condition. |
| InstanceSet | Array of [Instance](/document/api/213/##Instance) | List of details of an instance. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidFilter | Invalid filter. |
| InvalidFilterValue.LimitExceeded | [`Filter`](/document/api/213/9451#filter)Number of parameter values exceeds the limit. |
| InvalidHostId.Malformed | Invalid [CDH](https://cloud.tencent.com/document/product/416) `ID`. The specified [CDH](https://cloud.tencent.com/document/product/416) `ID` is in an incorrect format. For example, `host-1122` has an invalid `ID` length. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. Specified instance `ID` is not in a correct format. For example, `ins-1122` has an invalid instance `ID` length. |
| InvalidParameter | Invalid parameter. The parameter does not meet the requirement or is not supported. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | Number of parameter values exceeds the limit. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |

## 5. Example

## Example 1 View the list of instances

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstances
&Filters.0.Name=zone
&Filters.0.Values.0=ap-guangzhou-1
&Filters.0.Values.1=ap-guangzhou-2
&Offset=0
&Limit=1
&<Common request parameters>
```

#### Output example

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

### Example 2 Query instances bound with tags

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstances
&Filters.0.Name=tag:city
&Filters.0.Values.0=shenzhen
&Offset=0
&Limit=1
&<Common request parameters>
```

#### Output example

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
        "Tags": [
          {
            "tagKey": "city",
            "tagValue": "shenzhen"
          }
        ],
        "VirtualPrivateCloud": {
          "AsVpcGateway": "TRUE",
          "SubnetId": "subnet-6d7kj98i",
          "VpcId": "vpc-4e78ea76"
        }
      }
    ],
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7",
    "TotalCount": 1
  }
}
```


