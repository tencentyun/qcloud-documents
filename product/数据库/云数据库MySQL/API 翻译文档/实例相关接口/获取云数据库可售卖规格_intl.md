## 1. API Description

Domain name for API request: cdb.tencentcloudapi.com.

This API (DescribeDBZoneConfig) is used to query the available database specifications for different regions.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: cdb.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/236/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeDBZoneConfig |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-20 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/236/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of database configurations for available regions |
| Items | Array of [RegionSellConf](/document/api/236/##RegionSellConf) | Configuration details for available regions |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/236/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| CdbError | Backend error or process error. |
| InvalidParameter | Parameter error. |

## 5. Example

### Example 1 Query supported database specifications

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=DescribeDBZoneConfig
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "Items": [
      {
        "Area": "South China",
        "IsDefaultRegion": 0,
        "Region": "ap-guangzhou",
        "RegionName": "Guangzhou",
        "ZonesConf": [
          {
            "DrZone": [
              "ap-shanghai-1",
              "ap-shanghai-2",
              "ap-beijing-1",
              "ap-beijing-2",
              "ap-guangzhou-open-1",
              "ap-guangzhou-3",
              "ap-guangzhou-4",
              "ap-chengdu-1",
              "ap-chengdu-2"
            ],
            "HourInstanceSaleMaxNum": 30,
            "IsBm": false,
            "IsCustom": true,
            "IsDefaultZone": false,
            "IsSupportDr": true,
            "IsSupportVpc": true,
            "PayType": [
              "0",
              "1",
              "2"
            ],
            "ProtectMode": [
              "0",
              "1",
              "2"
            ],
            "SellType": [
              {
                "Configs": [
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Small game apps with tens of thousands of daily active users or tool apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 1000,
                    "Qps": 1000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Small game apps with tens of thousands of daily active users or tool apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 2000,
                    "Qps": 2400,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Medium-sized game apps with hundreds of thousands of daily active users",
                    "Iops": 0,
                    "Memory": 4000,
                    "Qps": 4400,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 8000,
                    "Qps": 7200,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 16000,
                    "Qps": 18000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 32000,
                    "Qps": 25000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 64000,
                    "Qps": 37689,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 96000,
                    "Qps": 40919,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 128000,
                    "Qps": 61378,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 244000,
                    "Qps": 122755,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 488000,
                    "Qps": 245509,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 6000,
                    "VolumeMin": 6000,
                    "VolumeStep": 5
                  }
                ],
                "EngineVersion": [
                  "5.5",
                  "5.6",
                  "5.7"
                ],
                "TypeName": "Z3"
              }
            ],
            "Status": 1,
            "Zone": "ap-guangzhou-2",
            "ZoneConf": {
              "BackupZone": [
                "ap-guangzhou-2"
              ],
              "DeployMode": [
                0
              ],
              "MasterZone": [
                "ap-guangzhou-2"
              ],
              "SlaveZone": [
                "ap-guangzhou-2"
              ]
            },
            "ZoneName": "Guangzhou Zone 2"
          },
          {
            "DrZone": [
              "ap-shanghai-1",
              "ap-shanghai-2",
              "ap-beijing-1",
              "ap-beijing-2",
              "ap-guangzhou-open-1",
              "ap-guangzhou-2",
              "ap-guangzhou-4",
              "ap-seoul-1",
              "ap-chengdu-1",
              "ap-chengdu-2"
            ],
            "HourInstanceSaleMaxNum": 30,
            "IsBm": false,
            "IsCustom": true,
            "IsDefaultZone": false,
            "IsSupportDr": true,
            "IsSupportVpc": true,
            "PayType": [
              "0",
              "1"
            ],
            "ProtectMode": [
              "0",
              "1",
              "2"
            ],
            "SellType": [
              {
                "Configs": [
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Small game apps with tens of thousands of daily active users or tool apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 1000,
                    "Qps": 1000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Small game apps with tens of thousands of daily active users or tool apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 2000,
                    "Qps": 2400,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Medium-sized game apps with hundreds of thousands of daily active users",
                    "Iops": 0,
                    "Memory": 4000,
                    "Qps": 4400,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 8000,
                    "Qps": 7200,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 16000,
                    "Qps": 18000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 32000,
                    "Qps": 25000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 64000,
                    "Qps": 37689,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 96000,
                    "Qps": 40919,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 128000,
                    "Qps": 61378,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 244000,
                    "Qps": 122755,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 488000,
                    "Qps": 245509,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 6000,
                    "VolumeMin": 6000,
                    "VolumeStep": 5
                  }
                ],
                "EngineVersion": [
                  "5.5",
                  "5.6",
                  "5.7"
                ],
                "TypeName": "Z3"
              }
            ],
            "Status": 1,
            "Zone": "ap-guangzhou-3",
            "ZoneConf": {
              "BackupZone": [
                "ap-guangzhou-3"
              ],
              "DeployMode": [
                0
              ],
              "MasterZone": [
                "ap-guangzhou-3"
              ],
              "SlaveZone": [
                "ap-guangzhou-3"
              ]
            },
            "ZoneName": "Guangzhou Zone 3"
          },
          {
            "HourInstanceSaleMaxNum": 30,
            "IsBm": false,
            "IsCustom": true,
            "IsDefaultZone": false,
            "IsSupportDr": false,
            "IsSupportVpc": true,
            "PayType": [
              "0",
              "1",
              "2"
            ],
            "ProtectMode": [
              "0",
              "1",
              "2"
            ],
            "SellType": [
              {
                "Configs": [
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Small game apps with tens of thousands of daily active users or tool apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 360,
                    "Qps": 120,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 500,
                    "VolumeMin": 10,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Small game apps with tens of thousands of daily active users or tool apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 1000,
                    "Qps": 1000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 500,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Small game apps with tens of thousands of daily active users or tool apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 2000,
                    "Qps": 2400,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 500,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Medium-sized game apps with hundreds of thousands of daily active users",
                    "Iops": 0,
                    "Memory": 4000,
                    "Qps": 4400,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 1000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 8000,
                    "Qps": 7200,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 1000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 12000,
                    "Qps": 15000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 1000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 16000,
                    "Qps": 18000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 1000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 24000,
                    "Qps": 23000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 1000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 48000,
                    "Qps": 37000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 1000,
                    "VolumeMin": 1000,
                    "VolumeStep": 5
                  }
                ],
                "EngineVersion": [
                  "5.5",
                  "5.6",
                  "5.7"
                ],
                "TypeName": "Z3"
              }
            ],
            "Status": 4,
            "Zone": "ap-guangzhou-1",
            "ZoneConf": {
              "BackupZone": [
                "ap-guangzhou-1"
              ],
              "DeployMode": [
                0
              ],
              "MasterZone": [
                "ap-guangzhou-1"
              ],
              "SlaveZone": [
                "ap-guangzhou-1"
              ]
            },
            "ZoneName": "Guangzhou Zone 1"
          },
          {
            "DrZone": [
              "ap-shanghai-1",
              "ap-shanghai-2",
              "ap-shanghai-3",
              "ap-beijing-1",
              "ap-beijing-2",
              "ap-guangzhou-open-1",
              "ap-guangzhou-2",
              "ap-guangzhou-3",
              "na-ashburn-1",
              "ap-chengdu-1",
              "ap-chengdu-2",
              "ap-bangkok-1"
            ],
            "HourInstanceSaleMaxNum": 30,
            "IsBm": false,
            "IsCustom": true,
            "IsDefaultZone": true,
            "IsSupportDr": true,
            "IsSupportVpc": true,
            "PayType": [
              "0",
              "1",
              "2"
            ],
            "ProtectMode": [
              "0",
              "1",
              "2"
            ],
            "SellType": [
              {
                "Configs": [
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Small game apps with tens of thousands of daily active users or tool apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 1000,
                    "Qps": 1000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Small game apps with tens of thousands of daily active users or tool apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 2000,
                    "Qps": 2400,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Medium-sized game apps with hundreds of thousands of daily active users",
                    "Iops": 0,
                    "Memory": 4000,
                    "Qps": 4400,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 8000,
                    "Qps": 7200,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 16000,
                    "Qps": 18000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 32000,
                    "Qps": 25000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 64000,
                    "Qps": 37689,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 96000,
                    "Qps": 40919,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 128000,
                    "Qps": 61378,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 244000,
                    "Qps": 122755,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 488000,
                    "Qps": 245509,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 6000,
                    "VolumeMin": 6000,
                    "VolumeStep": 5
                  }
                ],
                "EngineVersion": [
                  "5.5",
                  "5.6",
                  "5.7"
                ],
                "TypeName": "Z3"
              }
            ],
            "Status": 2,
            "Zone": "ap-guangzhou-4",
            "ZoneConf": {
              "BackupZone": [
                "ap-guangzhou-4"
              ],
              "DeployMode": [
                0
              ],
              "MasterZone": [
                "ap-guangzhou-4"
              ],
              "SlaveZone": [
                "ap-guangzhou-4"
              ]
            },
            "ZoneName": "Guangzhou Zone 4"
          }
        ]
      },
      {
        "Area": "Asia Pacific",
        "IsDefaultRegion": 0,
        "Region": "ap-bangkok",
        "RegionName": "Bangkok",
        "ZonesConf": [
          {
            "DrZone": [
              "ap-guangzhou-4"
            ],
            "HourInstanceSaleMaxNum": 30,
            "IsBm": false,
            "IsCustom": true,
            "IsDefaultZone": true,
            "IsSupportDr": true,
            "IsSupportVpc": true,
            "PayType": [
              "0",
              "1"
            ],
            "ProtectMode": [
              "0",
              "1",
              "2"
            ],
            "SellType": [
              {
                "Configs": [
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Small game apps with tens of thousands of daily active users or tool apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 1000,
                    "Qps": 1000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Small game apps with tens of thousands of daily active users or tool apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 2000,
                    "Qps": 2400,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Medium-sized game apps with hundreds of thousands of daily active users",
                    "Iops": 0,
                    "Memory": 4000,
                    "Qps": 4400,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 8000,
                    "Qps": 7200,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 16000,
                    "Qps": 18000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 32000,
                    "Qps": 25000,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 64000,
                    "Qps": 37689,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 96000,
                    "Qps": 40919,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 128000,
                    "Qps": 61378,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 244000,
                    "Qps": 122755,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                  },
                  {
                    "CdbType": "CUSTOM",
                    "Connection": 0,
                    "Cpu": 0,
                    "Device": "Z3",
                    "Info": "Large game apps with millions of daily active users",
                    "Iops": 0,
                    "Memory": 488000,
                    "Qps": 245509,
                    "Status": 0,
                    "Type": "High availability version",
                    "VolumeMax": 6000,
                    "VolumeMin": 6000,
                    "VolumeStep": 5
                  }
                ],
                "EngineVersion": [
                  "5.5",
                  "5.6",
                  "5.7"
                ],
                "TypeName": "Z3"
              }
            ],
            "Status": 2,
            "Zone": "ap-bangkok-1",
            "ZoneConf": {
              "BackupZone": [
                "ap-bangkok-1"
              ],
              "DeployMode": [
                0
              ],
              "MasterZone": [
                "ap-bangkok-1"
              ],
              "SlaveZone": [
                "ap-bangkok-1"
              ]
            },
            "ZoneName": "Bangkok Zone 1"
          }
        ]
      }
    ],
    "RequestId": "f1ccdafe-6803-455e-bb84-e33c08ba8247",
    "TotalCount": 17
  }
}
```


## 6. Other Resources

Cloud API 3.0 comes with the following development tools to make it easier to call the API.

* [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
* [Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
* [Tencent Cloud SDK 3.0 for PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
* [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
* [Tencent Cloud SDK 3.0 for NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
* [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)
* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)

