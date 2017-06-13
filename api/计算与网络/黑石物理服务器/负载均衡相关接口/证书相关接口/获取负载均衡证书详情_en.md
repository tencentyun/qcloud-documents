## 1. API Description
 
This API (GetBmCertDetail) is used to acquire the details of BM load balancer certificate.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| certId | Yes | String | Certificate ID. |




## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed For more information, please see [Common Error Codes](/document/product/386/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| data | Obj | Returned object. |

"data" is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| certId | String | Certificate ID. |
| certName | String | Certificate name. |
| certType | String | Certificate type (SVR = Server Certificate, CA = Client Certificate). |
| certContent | String | Certificate content. |
| certDomain | String | Primary domain name of certificate. |
| certSubjectDomain | Array | List of sub-domain names of certificate. |
| certUploadTime | String | Upload time of certificate. |
| certBeginTime | String | Time when the certificate takes effect. |
| certEndTime | String | Expiration time of certificate. |
| certLBList | Array | List of BM load balancer objects associated with the certificate. |

Each sub-item of certLBList is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| lbId | String | ID of BM load balancer instance. |
| lbName | String | Name of BM load balancer instance. |
| vpcId | Int | The ID of VPC to which the BM load balancer belongs. |
| regionId | Int | The ID of region to which the BM load balancer belongs. |

Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| -20000 | InvalidResource.CertPlatformErr | An error occurred while accessing the certificate platform |

## 4. Examples
 
Input

<pre>
https://domain/v2/index.php?Action=GetBmCertDetail
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&certId=abcdefgh
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "certId": "abcdefgh",
		"certName": "certName",
		"certType": "SVR",
		"certContent": "-----BEGIN CERTIFICATE-----
            MIIE0DCCA7igAwIBAgIQEgaTYAJIpw1PQxjSr1FlTDANBgkqhkiG9w0BAQsFADBP
            MQswCQYDVQQGEwJDTjEaMBgGA1UEChMRV29TaWduIENBIExpbWl0ZWQxJDAiBgNV
            BAMMG0NBIOayg+mAmuWFjei0uVNTTOivgeS5piBHMjAeFw0xNjA1MTMwODIxMjVa
            Fw0xODA2MTMwODIxMjVaMBUxEzARBgNVBAMMCmcuZi14ai5jb20wggEiMA0GCSqG
            SIb3DQEBAQUAA4IBDwAwggEKAoIBAQC4/Ei7dxUJYXgY1V1PflCMwUrkG8Ack0vw
            +C/hCzivNBw5N0WA1Tch4REOIyDPIBq2wiblw4kSsHOF5CfB9DwDhaknZwzwyynZ
            Wr2NekKjoo6x0viqFydVyiVWGzW1qr6Dn9tiDcp75W/Os+nUzKHcc0Wd5aHvjGKD
            6xEPQKLvCZ0F4208rHWcoSnYiaFJPUAfegd8JvK5al0BvSZoXICo6Taf5x4xHag1
            6ymINH1ClLcAIOpAITWddqV20xaXrvdU7J0BusmYkHc840X3cvBywjFurzN5oLg2
            vtVQhGm6qJ/Fjqdg8w40BZkTQb4PlEX8AJ27g+548giuVnLzf8CHAgMBAAGjggHg
            MIIB3DAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUF
            BwMBMAkGA1UdEwQCMAAwHQYDVR0OBBYEFBvlTUGHZ/GGU4qGT+T7r/Zbcg0pMB8G
            A1UdIwQYMBaAFDDadIbzKJBWntcxMcK9Wc2TEjkdMH8GCCsGAQUFBwEBBHMwcTA1
            BggrBgEFBQcwAYYpaHR0cDovL29jc3AyLndvc2lnbi5jbi9jYTJnMi9zZXJ2ZXIx
            L2ZyZWUwOAYIKwYBBQUHMAKGLGh0dHA6Ly9haWEyLndvc2lnbi5jbi9jYTJnMi5z
            ZXJ2ZXIxLmZyZWUuY2VyMD4GA1UdHwQ3MDUwM6AxoC+GLWh0dHA6Ly9jcmxzMi53
            b3NpZ24uY24vY2EyZzItc2VydmVyMS1mcmVlLmNybDBOBgNVHREERzBFggpnLmYt
            eGouY29tghBzY2hvbGFyLmYteGouY29tggt5dC5mLXhqLmNvbYILZmIuZi14ai5j
            b22CC3R3LmYteGouY29tME8GA1UdIARIMEYwCAYGZ4EMAQIBMDoGCysGAQQBgptR
            AQECMCswKQYIKwYBBQUHAgEWHWh0dHA6Ly93d3cud29zaWduLmNvbS9wb2xpY3kv
            MA0GCSqGSIb3DQEBCwUAA4IBAQCJSd/1xmxwnT/TtKvvxTvDnkCpfsFYVmqiHB/Z
            rXiMdgobUOfF7C8kcBCTqSQAXZF3fjJ1KyhNulvKOffzGGYp+rMwoTAmfaNLUxD/
            X9gPLxZCiysDBQ1BLe16k4aKUHIOmqQNF1MD/8hOZBxjevctKaXc4Xqm2gxJLxDH
            RoY3HKZcdB6t/x7YJU640wvaFqDqIgR6Pc74YjtLrNjkXcf/IQU7c2yjZt9NIGeS
            OTku5DmFasRf04tmE7naB+wkUZOwAqGK8CESNS11BYZjO/M4G/ALS8zCpShUy89H
            hYiYAG5jdNI4vyWwaU4428nG3YvKzlTOpCaowqgbyCcqmtAT
            -----END CERTIFICATE-----",
		"certDomain": "xxx.com",
		"certSubjectDomain": ["s-xxx.com"],
		"certUploadTime": "2017-03-29 11:57:28",
		"certBeginTime": "2016-05-25 08:00:00",
		"certEndTime": "2019-07-25 07:59:59",
		"certLBList": {
			"lbId": "lb-abcdefg",
			"lbName": "lbtest",
			"vpcId": 12345,
			"regionId": 8,
		}
    }
}

```
