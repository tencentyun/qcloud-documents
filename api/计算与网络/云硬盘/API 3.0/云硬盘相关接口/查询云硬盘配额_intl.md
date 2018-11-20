
## 1. API Description

This API (DescribeDiskConfigQuota) is used to query the cloud disk quota.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: DescribeDiskConfigQuota |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InquiryType | Yes | String | Inquiry type. Value range: <li>INQUIRY_CBS_CONFIG: query the configuration list of cloud disks </li><li>INQUIRY_CVM_CONFIG: query the configuration list of cloud disks and instances</li> |
| Zones.N | No | Array of String | Query the configurations in one or more [availability zones](/document/api/213/9452#zone). |
| DiskChargeType | No | String | Billing method. Value range: <li>PREPAID: prepaid </li><li>POSTPAID_BY_HOUR: postpaid. </li>|
| DiskType | No | String | Type of hard disk medium. Value range: <li>CLOUD_BASIC: HDD cloud disk </li><li>CLOUD_PREMIUM: Premium cloud disk </li><li>CLOUD_SSD: SSD cloud disk.</li> |
| DiskUsage | No | String | System disk or data disk. Value range: <li>SYSTEM_DISK: system disk </li><li>DATA_DISK: data disk.</li> |
| InstanceFamilies.N | No | Array of String | Filter by the instance model series, such as S1, I1 and M1. For more information, please see [Instance Types](https://cloud.tencent.com/document/product/213/11518) |
| CPU | No | Integer | Number of CPU cores in the instance |
| Memory | No | Integer | Memory size of the instance |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| DiskConfigSet | Array of [DiskConfig](/document/api/362/15669#DiskConfig) | Configuration list of the cloud disk |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Query Cloud Disk Configurations in Guangzhou Zone 3

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=DescribeDiskConfigQuota
&InquiryType=INQUIRY_CBS_CONFIG
&Zones.0=ap-guangzhou-3
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "DiskConfigSet": [
      {
        "Available": true,
        "DiskChargeType": "PREPAID",
        "DiskType": "CLOUD_PREMIUM",
        "DiskUsage": "DATA_DISK",
        "MaxDiskSize": 4000,
        "MinDiskSize": 50,
        "Zone": "ap-guangzhou-3"
      },
      {
        "Available": false,
        "DiskChargeType": "PREPAID",
        "DiskType": "CLOUD_BASIC",
        "DiskUsage": "DATA_DISK",
        "MaxDiskSize": 16000,
        "MinDiskSize": 10,
        "Zone": "ap-guangzhou-3"
      },
      {
        "Available": true,
        "DiskChargeType": "PREPAID",
        "DiskType": "CLOUD_SSD",
        "DiskUsage": "DATA_DISK",
        "MaxDiskSize": 4000,
        "MinDiskSize": 100,
        "Zone": "ap-guangzhou-3"
      }
    ],
    "RequestId": "55db49cf-b9d7-da27-825b-5a02ba6884ca"
  }
}
```

## Example 2 Query Available Cloud Disk Configurations for S3 Models in Guangzhou Zone 3

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=DescribeDiskConfigQuota
&InquiryType=INQUIRY_CVM_CONFIG
&Zones.0=ap-guangzhou-3
&InstanceFamilies.0=S3
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "DiskConfigSet": [
      {
        "Available": true,
        "DeviceClass": "VSELF_3",
        "DiskChargeType": "POSTPAID_BY_HOUR",
        "DiskType": "CLOUD_BASIC",
        "DiskUsage": "DATA_DISK",
        "InstanceFamily": "S3",
        "MaxDiskSize": 4000,
        "MinDiskSize": 10,
        "Zone": "ap-guangzhou-3"
      },
      {
        "Available": true,
        "DeviceClass": "VSELF_3",
        "DiskChargeType": "PREPAID",
        "DiskType": "CLOUD_BASIC",
        "DiskUsage": "DATA_DISK",
        "InstanceFamily": "S3",
        "MaxDiskSize": 16000,
        "MinDiskSize": 10,
        "Zone": "ap-guangzhou-3"
      },
      {
        "Available": true,
        "DeviceClass": "VSELF_3",
        "DiskChargeType": "POSTPAID_BY_HOUR",
        "DiskType": "CLOUD_BASIC",
        "DiskUsage": "SYSTEM_DISK",
        "InstanceFamily": "S3",
        "MaxDiskSize": 1024,
        "MinDiskSize": 50,
        "Zone": "ap-guangzhou-3"
      }
    ],
    "RequestId": "8fdf8796-d60e-4326-8d68-1ee6a58952e9"
  }
}
```


        
