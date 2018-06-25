## 1. API Description

This API (GetHostCertList) is used to query information such as HTTPS certificate ID that a user hosts in Tencent Cloud SSL. Paged query is supported.

Domain name for API request: cdn.api.cloud.tencent.com

1) You can query the information of one certificate that corresponds to one domain name at a time.

[Call Demo](https://www.cloud.tencent.com/document/product/228/1734)

## 2. Input Parameters

The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://www.cloud.tencent.com/doc/api/231/4473) page. The Action field for this API is GetHostCertList.

| Parameter | Required | Type | Description |
| --------- | ---- | ------ | ---------------------------------------- |
| host | Yes | String | Domain name |

## 3. Output Parameters

| Parameter| Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://www.cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81). |
| message | String | Module error message description depending on API |
| codeDesc | String | Error message or error code at business side |
| data | Array | Returned result. For more information, please see the description below |

#### `data` Field Description
| Parameter | Type | Description |
| -------- | ------ | ----------------------------------- |
| cert_list | Array | For more information about the HTTPS certificate array, please see the description below |
| count | String | Total number of returned HTTPS certificates |

#### `cert_list` Field Description
| Parameter | Type | Description |
| ----------- | ------ | ----------------------------------- |
| cert_id | String | Certificate ID |
| alias | String | Certificate remarks |
| expire_time | String | Expiration time of certificate |
| subject_name | String | Domain name associated with the certificate |

## 4. Example

### 4.1 Example of Input

> host:www.test.com


### 4.2 GET Request


For a GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.cloud.tencent.com/v2/index.php?
Action=GetCertificates
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462440051
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
```

### 4.3 POST Request
For a POST request, the parameters are input in HTTP Request-body. The request address is:

```
https://cdn.api.cloud.tencent.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'GetCertificates',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462868615,
  'Nonce' => 520585444,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'host' => www.test.com,
)
```

### 4.4 Example of Returned Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "cert_list": [
            {
                "cert_id": "XXXX8XXX",
                "alias": "www.test.com",
                "expire_time": "2019-01-07 07:59:59",
                "subject_name": [
                    "www.test.com"
                ]
            }
        ],
        "count": 1
    }
}
```








