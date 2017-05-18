## 1. API Description

This API (GetCdnOverseaProvIspHyDetailStat) is used to query consumption details of specified domain when region, ISP and date are all specified. Time granularity is 5 minutes, which means 288 statistical points per day. Region/province data needs to be analyzed from logs, thus a latency of 20-30 minutes is expected for the data. **Note: Please restrict the frequency with which this API is called under 100 times per minute.**

Domain name for API request: <font style="color:red">cdn.api.qcloud.com</font>

**Details:**

+ Target domains need to be connected to Tencent Cloud overseas CDN before you can query them using this API;
+ Due to the great variety of combinations between regions and ISPs, and the fact that this API returns data with a fine granularity in a large volume, you can only query up to 5 domains at a time;
+ Currently overseas ISPs are not specified, their unified code is -1;
+ If you only specify region but not ISP, the consumption details of every ISP will be returned. You may specify multiple regions;
+ If you specify neither ISP nor region, the consumption retails of every ISP in every region will be returned;
+ Nothing will be returned if there is no data.

[Call Demo](https://www.qcloud.com/document/product/228/1734)

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. See the [Common Request Parameters](https://www.qcloud.com/doc/api/231/4473) page for details. The Action field for this API is GetCdnOverseaProvIspHyDetailStat.

| Parameter Name     | Required | Type     | Description                                       |
| -------- | ---- | ------ | ---------------------------------------- |
| date     | Yes    | String | Query date. Format must be yyyy-mm-dd. For example: 2016-11-20                     |
| hosts.n  | Yes    | String | Domain. You may enter multiple domains, for example: hosts.0=www.test.com&hosts.1=www.test2.com. You can query up to 5 domains at a time |
| provs.n  | No    | String | Specifies regions. Regions are represented with codes. Please refer to the Overseas CDN Log Region Code Mapping Table below      |
| isps.n   | No    | String | Specifies ISP. ISPs are represented with codes. Please refer to the Overseas CDN Log Region Code Mapping Table below    |
| statType | Yes    | String | Specifies query type. You may query data of six types: number of requests (requests); traffic (flux), measured in Byte; number of status codes (statuscode); back-to-origin speed (dlspeed), measured in bit/s; back-to-origin time cost (dltime), measured in seconds; number of failed back-to-origin requests (errorcnt) |

**Overseas CDN Log Region Code Mapping Table**

73: India, 1195: Indonesia, 1176: Singapore, 57: Thailand, 144: Vietnam, 3701: Malaysia, 2588: Philippines, 2026: Taiwan, 1044: Japan, 3379: Korea, 1200: Hong Kong, 3839: Canada, 669: United States, -2: Other Overseas Regions, -3: Unknown;

**Overseas CDN Log ISP Code Mapping Table**

-1: Overseas ISP;

## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | English error message or error code at business side.                           |
| data     | Object | Data result, details are described below                             |

#### data Field Description

| Name        | Type     | Description             |
| --------- | ------ | -------------- |
| date      | String | Entered start date (day)  |
| prov_data | Object | Detailed region data, details are described below |

##### prov_data Field Description

| Name        | Type     | Description                              |
| --------- | ------ | ------------------------------- |
| id        | Int    | Region code                            |
| name      | String | Region                              |
| host           | String | Domain that was specified to be queried                                  |
| isp_value | Object | ISP information. Every ISP has a corresponding detail array. Currently overseas ISPs are not specified |

## 4. Example

### 4.1 Example of Input

> date: 2016-11-20
> hosts.0: www.test.com
> provs.0: 57
> isps.0: -1

### 4.2 GET Request

All the parameters are required to be added after URL in GET request:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnOverseaProvIspHyDetailStat
&SecretId=XXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462416887
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXX
&date=2016-11-20
&hosts.0=www.test.com
&provs.0=57
&isps.0=-1
&statType=bandwidth
```

### 4.3 POST Request

In POST request, the parameters will be filled in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Such formats of parameters as form-data, x-www-form-urlencoded are supported. The array of parameters is as follows:

```
array (
  'Action' => 'GetCdnOverseaProvIspHyDetailStat',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'date' => '2016-11-20',
  'hosts.0' => 'www.test.com',
  'provs.0' => '57',
  'isps.0' => '-1',
  'statType' => 'flux'
)
```

### 4.4 Example of Returned Results

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "date": "2016-09-28",
        "prov_data": {
            "www.test.com": [
                {
                    "id": 57,
                    "name": "Thailand",
                    "host": "www.test.com",
                    "isp_value": {
                        "flux": {
                            "-1": [
                                1,
                                1,
                                1,
                                0,
                                ...
                            ]
                        }
                    }
                }
            ]
       }
    }
}
```

