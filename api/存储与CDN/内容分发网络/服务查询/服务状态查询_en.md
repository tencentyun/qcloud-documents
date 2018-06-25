## API Description
**GetCdnMonitorData** is used to query the CDN delay and availability data monitored by ISPs for every province.

Domain name for API request: <font style="color:red">cdn.api.qcloud.com</font>

**Note**

+ The delay and availability data are updated every other minute. Do not call the API frequently.
+ The data comes from the third-party monitoring tools, which access the monitored files regularly to obtain the service status data.
+ The API returns the delay/availability data for every province from the three major ISPs - China Unicom, China Mobile and China Telecom, as well as the average availability/delay data for every province from six ISPs including China Telecom, China Mobile, China Unicom, Great Wall Broadband, China Tietong Telecom and Beijing Teletron.
+ The frequency of calling the API is limited to 100/min.


[View the example](https://cloud.tencent.com/document/product/228/1734)

## Input Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473). The Action field for this API is GetCdnMonitorData. No input parameter is needed for this API.


## Output Parameters
| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error message or error code at business side |
| data | Array | Returned result. For more information, please see the description below. |

#### "data" is composed as follows:

#### data

| Parameter Name | Type | Description |
| ---------- | ----- | ----------- |
| succ_rate | Array | Availability data (in %) |
| delay_time | Array | Delay data (in ms) |

#### succ_rate/delay_time

| Parameter Name | Type | Description |
| ------ | ------ | ---------------------------------------- |
| pro_id | Int | Province ID |
| name | String | Province name |
| value | Array | "1": China Telecom<br/>"2": China Unicom<br/>"4" :China Mobile<br/>"16777215": Average of China Telecom, China Mobile, China Unicom, Great Wall Broadband, China Tietong Telecom and Beijing Teletron |

## Example

### GET Request
For a GET request, all the parameters are required to be appended to the URL (commas are transcoded):
```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnMonitorData
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
```

### POST Request
For a POST request, the parameters are input in HTTP Request body. The request address is:
```
https://cdn.api.qcloud.com/v2/index.php
```
The parameters support formats such as formdata and xwwwformurlencoded. The array of parameters is as follows:

```
array (
	'Action' => 'GetCdnMonitorData',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX'
)
```

### Example of Returned Result
Note: IP in the example is only for reference.
```
{
    "code":0,
    "message":"",
    "codeDesc":"Success",
    "data":{
        "succ_rate":
           [{
                "pro_id":1,
                "name":"Heilongjiang",
                "value":{
                    "1":98.289166666667,
                    "2":99.073333333333,
                    "4":100,
                    "16777215":98.789166666667
                }
            }....
           ]
        "delay_time":
           [{
                "pro_id":1,
                "name":"Heilongjiang",
                "value":{
                    "1":491.16666666667,
                    "2":260.58333333333,
                    "4":280.91666666667,
                    "16777215":357.91666666667
                }
            }
            .....
      	]
    }
}
```



