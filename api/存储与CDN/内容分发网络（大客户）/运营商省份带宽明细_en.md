## 1. API Description

This API (GetCdnProvIspDetailStat) is used to query the bandwidth consumption details by specified domains, dates, ISPs and provinces. The time granularity is 5 minutes, and there are 288 statistical points each day. Since ISP/province data needs to be analyzed from logs, there is a data latency of about 20-30 minutes.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>

**Note**

+ Due to the great number of combinations of provinces and ISPs and the large volume of fine-granularity data returned by this API, you can only query the data for a maximum of 5 domains at a time;
+ If ISP is specified but province is left empty, the returned results will be the bandwidth consumption details of every province for the ISP. You may specify multiple ISPs;
+ If province is specified but ISP is left empty, the returned results will be the bandwidth consumption details of every ISP in the province. You may specify multiple provinces;
+ If neither ISP nor province is specified, the bandwidth consumption details of every ISP in every province will be returned;
+ If no data exists for the specified province or ISP, nothing will be returned.
+ The returned bandwidth consumption data is measured in bps.

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473). The Action field for this API is GetCdnProvIspDetailStat.

| Parameter Name    | Required | Type     | Description                                       |
| ------- | ---- | ------ | ---------------------------------------- |
| date     | Yes    | String | The date for which the query is made. Format: yyyy-mm-dd. For example, 2016-09-28                    |
| hosts.n | Yes    | String | Specify domains. You may enter multiple domains, for example: hosts.0=www.test.com&hosts.1=www.test2.com. You can query a maximum of 5 domains at a time |
| provs.n | No    | String | Specify provinces. Provinces are identified by codes. For details, click [CDN Log Province Code Mapping Table](https://cloud.tencent.com/document/product/228/6316). |
| isps.n | No    | String | Specify ISPs. ISPs are identified by codes. For details, click [CDN Log ISP Code Mapping Table](https://cloud.tencent.com/document/product/228/6316). |

## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | Error message or error code at business side.                           |
| data     | Object | Data result. For details, refer to the description later.                            |

#### data Field Description

| Name        | Type     | Description             |
| --------- | ------ | -------------- |
| date      | String | The start date specified in input parameter. |
| prov_data | Object |Data details for specified provinces. For details, refer to the description later. |

##### prov_data Field Description

| Name        | Type     | Description                   |
| --------- | ------ | -------------------- |
| id        | Int    | Province code                 |
| name      | String | Province                   |
| host      | String | Domain specified for query              |
| isp_value | Object | ISP information. Each ISP has a details array |

## 4. Example

### 4.1 Input Example

> date: 2016-09-28
> hosts.0: www.test.com
> provs.0: 1442
> isps.0: 2

### 4.2 GET Request

For GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnProvIspDetailStat
&SecretId=XXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462416887
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXX
&date=2016-09-28
&hosts.0=www.test.com
&provs.0=1442
&isps.0=2
```

### 4.3 POST Request

For POST request, the parameters need to be filled in the HTTP Request-body. Request address:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'GetCdnProvIspDetailStat',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'date' => '2016-09-28',
  'hosts.0' => 'www.test.com',
  'provs.0' => '1442',
  'isps.0' => '2'
)

```

### 4.4 Example of Returned Result

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
                    "id": 1442,
                    "name": "Zhejiang",
                    "host": "www.test.com",
                    "isp_value": {
                        "bandwidth": {
                            "2": [
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
























