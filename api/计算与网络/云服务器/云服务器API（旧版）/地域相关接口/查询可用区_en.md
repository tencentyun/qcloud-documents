## 1. API Description
This API (DescribeAvailabilityZones) is used to query the details of Tencent Cloud availability zones.

Domain name for API request: cvm.api.qcloud.com

* For more information about the definition of the availability zone, please see [the region section in the product documentation](https://cloud.tencent.com/doc/product/213/497#2.-.E5.8F.AF.E7.94.A8.E5.8C.BA).
* The content includes the IDCs of availability zones.
* You can view the information on an availability zone by specifying the zone ID.
* The list of availability zone IDs is as follows:

| Availability Zone Name | Availability Zone ID |
|---------|---------|
| Guangzhou Zone 1 | 100001 |
| Guangzhou Zone 2 | 100002 |
| Guangzhou Zone 3 | 100003 |
| Guangzhou Zone 4 | 100004 |
| Shanghai Zone 1 | 200001 |
| Shanghai Zone 2 | 200002 |
| Hong Kong Zone 1 | 300001 |
| Toronto Zone 1 | 400001 |
| Shanghai Finance Zone 1 | 700001 |
| Shanghai Finance Zone 2 | 700002 |
| Beijing Zone 1 | 800001 |
| Beijing Zone 2 | 800002 |
| Singapore Zone 1 | 900001 |
| Shenzhen Finance Zone 1 | 110001 |
| Shenzhen Finance Zone 2 | 110002 |
| Guangzhou Open Zone | 120001 |
| Silicon Valley Zone 1 | 150001 |
| Chengdu Zone 1 | 160001 |
| Chengdu Zone 2 | 160002 |
| Frankfort Zone 1 | 170001 |
| Seoul Zone 1 | 180001 |

## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, please see the page [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| zoneId | No | Int | Availability zone ID |




## 3. Output Parameters


| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Successful; other values: Failed. |
| message | String | Error message |
| totalCount | Int | Number of availability zones |
| zoneSet | Array | List of availability zones |

`zoneSet` is a collection of information on availability zones. An availability zone is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| zoneId | Int | Availability zone ID |
| idcList | Array | IDC list |


`idcList` is a collection of information on IDCs subordinated to an availability zone. An IDC is composed as follows:


| Parameter Name | Type | Description |
|---------|---------|---------|
| idcId | Int | ID of IDC |
| idcName | String | IDC name |




## 4. Example

Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=DescribeAvailabilityZones
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  zoneId=100001
</pre>

Output

```
{
    "code" : 0,
    "message" : "",
    "totalCount" : 1
    "zoneSet" :         {
            "zoneName": "Guangzhou Zone 1", 
            "idcList": [
                {
                    "idcId": 685, 
                    "idcName": "Building AC2, Guangzhou Asia Pacific IDC, China Telecom"
                }, 
                {
                    "idcId": 737, 
                    "idcName": "02, Building AC4, Guangzhou Asia Pacific IDC, China Telecom"
                }, 
                {
                    "idcId": 798, 
                    "idcName": "Building AC2, Guangzhou Southern Base IDC, China Mobile"
                }, 
                {
                    "idcId": 834, 
                    "idcName": "Building AC7, Guangzhou Mid Renmin Road IDC, China Telecom"
                }, 
                {
                    "idcId": 908, 
                    "idcName": "Building AC5, Guangzhou Shiji IDC, China Telecom"
                }, 
                {
                    "idcId": 1035, 
                    "idcName": "M2, Building AC4, Guangzhou Shiji IDC, China Telecom"
                }, 
                {
                    "idcId": 1327, 
                    "idcName": "M3, Building AC4, Guangzhou Shiji IDC, China Telecom"
                }
            ], 
            "zoneId": 100001
      }
}

```





