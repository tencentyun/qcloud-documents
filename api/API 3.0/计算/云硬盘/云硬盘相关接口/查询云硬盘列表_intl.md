## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (DescribeDisks) is used to query the list of cloud disks.

* The details of the cloud disk can be queried based on the ID, type or status of the cloud disk. The relationship between different conditions is AND. For more information about filtering, please see the `Filter`.
* If the parameter is empty, a certain number (specified by `Limit`; the default is 20) of cloud disk lists are returned to the current user.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeDisks |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DiskIds.N | No | Array of String | Query by one or more cloud disk IDs, such as `disk-11112222`. For the format of this parameter, please see the ids.N section of the API [Introduction](/document/product/362/15633). This parameter does not support specifying both `DiskIds` and `Filters`. |
| Filters.N | No | Array of [Filter](/document/api/362/##Filter) | Filter conditions. This parameter does not support specifying both `DiskIds` and `Filters`.<br><li> disk-usage - Array of String - Required: No - (Filter condition) Filter by the type of the cloud disk. (SYSTEM_DISK: system disk &#124; DATA_DISK: data disk) <br><li> disk-charge-type - Array of String - Required: No - (Filter condition) Filter by the billing method of the cloud disk. (PREPAID: prepaid (by year/month) &#124; POSTPAID_BY_HOUR: postpaid (by usage))<br><li> portable - Array of String - Required: No - (Filter condition) Filter according to whether they are elastic cloud disks or not. (TRUE: elastic cloud disk &#124; FALSE: non-elastic cloud disk)<br><li> project-id - Array of Integer - Required: No - (Filter condition) Filter by the ID of the project to which the cloud disk belongs.<br><li> disk-id - Array of String - Required: No - (Filter condition) Filter by the cloud disk ID, such as `disk-11112222`.<br><li> disk-name - Array of String - Required: No - (Filter condition) Filter by cloud disk name.<br><li> disk-type - Array of String - Required: No - (Filter condition) Filter by the type of the cloud disk medium. (CLOUD_BASIC: HDD cloud disk &#124; CLOUD_PREMIUM: premium cloud disk &#124; CLOUD_SSD: SSD cloud disk.)<br><li> disk-state - Array of String - Required: No - (Filter condition) Filter by the cloud disk status. (UNATTACHED: unmounted &#124; ATTACHING: mounting &#124; ATTACHED: mounted &#124; DETACHING: unmounting &#124; EXPANDING: expanding capacity &#124; ROLLBACKING: rolling back &#124; TORECYCLE: to be reclaimed.)<br><li> instance-id - Array of String - Required: No - (Filter condition) Filter by the ID of the CVM instance to which the cloud disk is mounted. You can use this parameter to query the cloud disk mounted on the specified CVM.<br><li> zone - Array of String - Required: No - (Filter condition) Filter by the [availability zone](/document/api/213/9452#zone).<br><li> instance-ip-address - Array of String - Required: No - (Filter condition) Filter by the IP address of the private or public network of the CVM to which the cloud disk is mounted.<br><li> instance-name - Array of String - Required: No - (Filter condition) Filter by the name of the instance to which the cloud disk is mounted.<br><li> tag - Array of [Tag](/document/product/362/15669) - Required: No - (Filter condition) Filter by the tag bound to the cloud disk. |
| Offset | No | Integer | Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](/document/product/362/15633). |
| Limit | No | Integer | Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](/document/product/362/15633). |
| Order | No | String | The order of the output cloud disk list. Value: <br><li>ASC: Sort in an ascending order<br><li>DESC: Sort in a descending order. |
| OrderField | No | String | The field by which the cloud disk list is sorted. Value range: <br><li>CREATE_TIME: sorted by the creation time of cloud disks <br><li>DEADLINE: sorted by the expiration time of cloud disks <br>By default, the cloud disk list is sorted by the creation time of cloud disks. |
| ReturnBindAutoSnapshotPolicy | No | Boolean | Whether the ID of the periodic snapshot policy bound to the cloud disk needs to be returned in the cloud disk details. TRUE: return; FALSE: do not return. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of cloud disks that meet the condition. |
| DiskSet | Array of [Disk](/document/api/362/##Disk) |List of cloud disk details. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidFilter | The specified Filter is not supported. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Query all the mounted data disks

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=DescribeDisks
&Filters.0.Name=disk-usage
&Filters.0.Values.0=DATA_DISK
&Filters.1.Name=disk-state
&Filters.1.Values.0=ATTACHED
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "DiskSet": [
      {
        "Attached": true,
        "AutoRenewFlagError": false,
        "CreateTime": "2017-07-27 15:16:56",
        "DeadlineError": false,
        "DeadlineTime": "2017-10-27 15:17:05",
        "DifferDaysOfDeadline": -139,
        "DiskChargeType": "PREPAID",
        "DiskId": "disk-5w50lrms",
        "DiskName": "data1",
        "DiskSize": 10,
        "DiskState": "ATTACHED",
        "DiskType": "CLOUD_BASIC",
        "DiskUsage": "DATA_DISK",
        "Encrypt": false,
        "InstanceId": "ins-6p8zngem",
        "IsReturnable": false,
        "Placement": {
          "ProjectId": 10086,
          "Zone": "ap-guangzhou-2"
        },
        "Portable": true,
        "RenewFlag": "NOTIFY_AND_AUTO_RENEW",
        "ReturnFailCode": 2,
        "RollbackPercent": 0,
        "Rollbacking": false,
        "SnapshotAbility": true
      }
    ],
    "RequestId": "e63c7075-4b34-4825-9850-b19edb1eda89",
    "TotalCount": 1
  }
}
```


