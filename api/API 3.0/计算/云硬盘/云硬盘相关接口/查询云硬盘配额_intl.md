## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (DescribeDiskConfigQuota) is used to query the cloud disk quota.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeDiskConfigQuota |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InquiryType |Yes | String | Inquiry type. Value range:<br><li> INQUIRY_CBS_CONFIG: query the configuration list of cloud disks <br><li>INQUIRY_CVM_CONFIG: query the configuration list of cloud disks and instances |
| Zones.N | No | Array of String | Query the configurations in one or more [availability zones](/document/api/213/9452#zone). |
| DiskChargeType | No | String | Billing method. Value range:<br><li>PREPAID: Prepaid<br><li>POSTPAID_BY_HOUR: Postpaid. |
| DiskTypes.N | No | Array of String | Type of cloud disk medium. Value range:<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_PREMIUM: Premium cloud disk<br><li>CLOUD_SSD: SSD cloud disk. |
| DiskUsage | No | String | System disk or data disk. Value range:<br><li>SYSTEM_DISK: System disk<br><li>DATA_DISK: Data disk. |
| InstanceFamilies.N | No | Array of String | Filter by instance model series, such as: S1, I1, M1. For more information, please see [Instance Type](https://cloud.tencent.com/document/product/213/11518) |.
| CPU | No | Integer | Number of CPU cores in an instance. |
| Memory | No | Integer | Memory size of the instance. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| DiskConfigSet | Array of [DiskConfig](/document/api/362/##DiskConfig) | List of cloud disk configuration. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Query cloud disk configurations in Guangzhou Zone 3

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=DescribeDiskConfigQuota
&InquiryType=INQUIRY_CBS_CONFIG
&Zones.0=ap-guangzhou-3
&<Common request parameters>
```

#### Output example

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

### Example 2 Query available cloud disk configurations for S3 Models in Guangzhou Zone 3

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=DescribeDiskConfigQuota
&InquiryType=INQUIRY_CVM_CONFIG
&Zones.0=ap-guangzhou-3
&InstanceFamilies.0=S3
&<Common request parameters>
```

#### Output example

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


