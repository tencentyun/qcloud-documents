## 1. API Description
 
This API (DescribeRegions) is used to obtain the availability zones of CPM.

Domain for API request: <font style="color:red">bm.api.cloud.tencent.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, please see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| regionId | No | Int | Region ID. CPM availability zones currently include: 8 - Beijing, 4 - Shanghai, 1-Guangzhou |



## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Succeeded; other values: Failed. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. For more information, please see [Module Error Codes](/doc/api/456/6725). |
| data | obj | Region information, (taking "regionId" as the "Key") |

"data" is "json" information of region and is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| regionId | Int | Region ID |
| regionName | String | Region name |
| setName | String | Abbreviation for the region |
| zones | obj | Information of availability zones under the region. (taking "zoneId" as the "Key") |

"zones" is "json" information of availability zone and is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| zoneId| Int| Availability zone ID |
| zoneName | String | Availability zone name |
| zoneEname | String | Availability zone English name |


## 4. Example
 
Input

```
	https://domain/v2/index.php?
	Action=DescribeRegions</code>
	&<Common request parameters>
```
Output

```
{
    "code": 0,
    "message": "OK",
    "codeDesc" : "Success",
    "data": {
        "1": {
            "regionId": "1",
            "regionName": "South China (Guangzhou)",
            "setName": "ap-guangzhou",
            "zones": {
                "1000100003": {
                    "zoneId": "1000100003",
                    "zoneName": "Guangzhou Zone 1",
                    "zoneEname": "ap-guangzhou-bls-1"
                }
            }
        },
        "4": {
            "regionId": "4",
            "regionName": "East China (Shanghai)",
            "setName": "ap-shanghai",
            "zones": {
                "1000400001": {
                    "zoneId": "1000400001",
                    "zoneName": "Shanghai Zone 1",
                    "zoneEname": "ap-shanghai-bls-1"
                }
            }
        },
        "8": {
            "regionId": "8",
            "regionName": "North China (Beijing)",
            "setName": "ap-beijing",
            "zones": {
                "1000800001": {
                    "zoneId": "1000800001",
                    "zoneName": "Beijing Zone 1",
                    "zoneEname": "ap-beijing-bls-1"
                },
                "1000800002": {
                    "zoneId": "1000800002",
                    "zoneName": "Beijing Zone 2 ",
                    "zoneEname": "ap-beijing-bls-2"
                }
            }
        }
    }
}

```
