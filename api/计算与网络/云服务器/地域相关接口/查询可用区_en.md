## 1. API Description
This API (DescribeAvailabilityZones) is used to query the details of Tencent Cloud availability zones.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* For the definition of availability zones, please refer to the [Region](https://www.qcloud.com/doc/product/213/497#2.-.E5.8F.AF.E7.94.A8.E5.8C.BA) product documentation.
* The content includes the IDCs of availability zones.
* You can check the information on an availability zone by specifying the zone ID.
* The list of availability zone IDs is as follows: 

| Availability Zone Name | Availability Zone ID |
|---------|---------|
| Beijing Zone 1 |800001|
| Shanghai Zone 1 |200001|
| Guangzhou Zone 1 |100001|
| Guangzhou Zone 2 |100002|
| Guangzhou Zone 3 |100003|
| Hong Kong Zone 1 |300001|
| North America Zone 1 |400001|

## 2. Input Parameters

The following list only provides request parameters for this API. For other parameters, refer to [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| zoneId| No| Int| ID of the availability zone |




## 3. Output Parameters


| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code (0: succeeded; other values: failed) |
| message | String | Error message. |
| totalCount | Int | Number of availability zones. |
| zoneSet| Array | List of availability zones. |

zoneSet is a collection of information on availability zones. The data structure of information on an availability zone is as follows: 

| Parameter Name | Type | Description |
|---------|---------|---------|
| zoneId| Int| ID of availability zone. |
| idcList | Array | IDC list. |


idcList is a collection of information on IDCs subordinated to an availability zone. The data structure of information on an IDC is as follows: 


| Parameter Name | Type | Description |
|---------|---------|---------|
| idcId | Int | ID of IDC. |
| idcName | String | IDC name. |




## 4. Sample Codes

Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=DescribeAvailabilityZones
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
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




