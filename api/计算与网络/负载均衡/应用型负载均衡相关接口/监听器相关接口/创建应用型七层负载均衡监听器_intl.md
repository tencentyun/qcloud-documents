## API Description
This API (CreateForwardLBSeventhLayerListeners) is used to create application-based load balancer layer-7 listener. A load balancer listener provides specific rules for forwarding user requests, including parameters such as port, protocol, session persistence, health check and so on.
 
Domain name for API access: `lb.api.qcloud.com`


## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is CreateForwardLBSeventhLayerListeners.


| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| loadBalancerId | Yes | String | ID of load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listeners.n.loadBalancerPort | Yes | Int | Listening port of application-based load balancer listener. Value range: 1-65535. listeners is an array. You can create multiple listeners. n is subscript. |
| listeners.n.protocol | Yes | Int | Protocol type of application-based load balancer instance listener. 1: HTTP, 4: HTTPS. |
| listeners.n.listenerName | No | String | Name of application-based load balancer listener. |
| listeners.n.SSLMode | No | String | Verification mode of HTTPS listener. unidirectional: Unidirectional verification; mutual: Mutual verification. This field is required for HTTPS listeners. |
| listeners.n.certId | No | String | Server certificate ID. For HTTPS listeners, if this field is left empty, certificate must be uploaded, including certContent, certKey, certName. |
| listeners.n.certCaId | No | String | Client certificate ID. If SSLMode=mutual and this field is left empty for listener, client certificate must be uploaded, including certCaContent, certCaName. |
| listeners.n.certCaContent | No | String | Content of the client certificate to be uploaded. If SSLMode=mutual and certCaId is left empty, this parameter must be set. |
| isteners.n.certCaName | No | String | Name of the client certificate to be uploaded. If SSLMode=mutual and certCaId is left empty, this parameter must be set. |
| listeners.n.certContent | No | String | Content of the client certificate to be uploaded. If certId is left empty, this parameter must be set. |
| listeners.n.certKey | No | String | Key of the client certificate to be uploaded. If certId is left empty, this parameter must be set. |
| listeners.n.certName | No | String | Name of the client certificate to be uploaded. If certId is left empty, this parameter must be set. |



## Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |
| listenerIds | Array | Listener ID array. |


## Example
 
Request
```
https://lb.api.qcloud.com/v2/index.php?Action=CreateForwardLBSeventhLayerListeners
&<Common request parameters>
&loadBalancerId=lb-abcdefgh
&listeners.0.loadBalancerPort=443s
&listeners.0.protocol=4
&listeners.0.SSLMode=mutual
&listeners.0.certName=myCertName
&listeners.0.certContent=-----BEGIN CERTIFICATE-----
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
			-----END CERTIFICATE-----
&listeners.0.certKey=-----BEGIN RSA PRIVATE KEY-----
			your own key
			-----END RSA PRIVATE KEY-----
&listeners.0.certCaContent=-----BEGIN CERTIFICATE-----
			MIIEPDCCAySgAwIBAgIJAJiHd00fZNxoMA0GCSqGSIb3DQEBBQUAMHExCzAJBgNV
			BAYTAkNOMQswCQYDVQQIEwJHUzELMAkGA1UEBxMCU1oxDTALBgNVBAoTBFhYWFgx
			DjAMBgNVBAsTBVhYWFhYMQ4wDAYDVQQDEwVBQUFBQTEZMBcGCSqGSIb3DQEJARYK
			d3d3QHFxLmNvbTAeFw0xNjA4MTExMTUyNTZaFw0xNzA4MDIxMTUyNTZaMHExCzAJ
			BgNVBAYTAkNOMQswCQYDVQQIEwJHUzELMAkGA1UEBxMCU1oxDTALBgNVBAoTBFhY
			WFgxDjAMBgNVBAsTBVhYWFhYMQ4wDAYDVQQDEwVBQUFBQTEZMBcGCSqGSIb3DQEJ
			ARYKd3d3QHFxLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAM29
			SL0TlZaqZb4jEjZ8mkwSeWGVhYaskYtDvxvZQSHZF2A1DtpGojsz+Z3KxgVo4edj
			Y26lfxmFPwPhxoBRgCYDqEOLAOKWRxzXYyP2kr9FN4vs0hzizT4IVxJciOUwmIaQ
			bjzzFQN5BeJ/UTekrs1/YwfJAakP7TvoKUlfBvkKFzRlgdxnGk+/C7+cg1P9F9J4
			rjm/Rn+0HhO0QshsAo1IT4jZF356yvk/g0upLhZexo39jKf4ypmtcHTusYcAoRGh
			bCk26taM4aeQxMnB715ZkQhqB1+dyM6SWRFysYpteEK+jEH8wWPQriqIlcRJxncy
			/8B4RmHIJxXRG8Tb8TUCAwEAAaOB1jCB0zAdBgNVHQ4EFgQUp/qOq6q7ezAVxEhX
			trsPMa4aiq4wgaMGA1UdIwSBmzCBmIAUp/qOq6q7ezAVxEhXtrsPMa4aiq6hdaRz
			MHExCzAJBgNVBAYTAkNOMQswCQYDVQQIEwJHUzELMAkGA1UEBxMCU1oxDTALBgNV
			BAoTBFhYWFgxDjAMBgNVBAsTBVhYWFhYMQ4wDAYDVQQDEwVBQUFBQTEZMBcGCSqG
			SIb3DQEJARYKd3d3QHFxLmNvbYIJAJiHd00fZNxoMAwGA1UdEwQFMAMBAf8wDQYJ
			KoZIhvcNAQEFBQADggEBAJ2XTOKyR2nFgaWcTG5d92tSij3lIoZCBo4dwrleYFuW
			cYUYSi65QskJpuDHr5KttmI4+0tt9OQOB/oHIEbkCqgEAC7PREJAgapcf5+ItMHN
			rNh151CkTyoK1Z09tw3OrX5GQVAHSpz0+BQTE+MPas5lyidwP1PqQFY9nZW4J3PG
			RAbiiSnQ1eN5g0aKzIZpbEbP7Y7BGT9b+rLt+VUbmQ30h96zHchSsUsQ32dchwLm
			N0ZL1PyCivQ+A1snbqA3uHZnoXBd8/yq0QNg0o15edx+GfbY5FJbgXf3FER+NgMB
			wPeJ62izpROBQvXYNb3e72gM1xCAlgD+MBpNeGlx56g=
			-----END CERTIFICATE-----
&listeners.0.certCaName=myCertCaName
```
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "listenerIds": [
        "lbl-66tqmiro"
    ]
}
```

