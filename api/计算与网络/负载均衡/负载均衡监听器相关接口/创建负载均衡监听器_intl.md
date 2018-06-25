## API Description
This API (CreateLoadBalancerListeners) is used to create load balancer listeners. A load balancer listener provides specific rules for forwarding user requests, including parameters such as port, protocol, session persistence, health check and so on.
 
Domain name for API access: `lb.api.qcloud.com`
 
The rules for configuring listeners are as follows:

- A load balancer port can only have one protocol in one load balancer.
- Public network-based load balancer listeners support HTTP, UDP, TCP, and HTTPS protocols. Private network-based load balancer listeners only support UDP and TCP protocols.
- Batch creation is not supported when creating HTTPS listeners.


## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is CreateLoadBalancerListeners.


| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| loadBalancerId | Yes | String | ID of the load balancer instance, which can be queried via the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listeners.n.loadBalancerPort | Yes | Int | Listening port of the load balancer listener. Value range: 1-65535. listeners is an array. You can create multiple listeners. n is subscript. |
| listeners.n.instancePort | Yes | Int | Listening port of backend CVM of load balancer listener. Value range: 1-65535. |
| listeners.n.protocol | Yes | Int | Protocol type of the load balancer instance listener. 1: HTTP, 2: TCP, 3:UDP, 4: HTTPS.<br> Public network-based load balancer instances support HTTP, UDP, TCP, and HTTPS protocols. <br>Private network-based load balancer instances support TCP and UDP protocols. |
| listeners.n.listenerName | No | String | Name of the load balancer listener. |
| listeners.n.sessionExpire | No | Int | Session persistence duration of the load balancer listener. Value range: 0 or 30-3600. Default is 0. | |
| listeners.n.healthSwitch | No | Int | Whether to enable health check for load balancer instance listeners: 1 (Enable) and 0 (Disable). Default is 1 (Enable). |
| listeners.n.timeOut | No | Int | Health check response timeout for the load balancer listener (in sec). Value range: 2-60. Default is 2.<br><font color="red"> The response timeout must be smaller than health check time interval.</font><br> The response timeout for public network-based load instance listeners with HTTP or HTTPS protocol cannot be set. |
| listeners.n.intervalTime | No | Int | Health check time interval of the load balancer listener (in sec). Default: 5. Value range: 5-300. |
| listeners.n.healthNum | No | Int | Healthy threshold of the load balancer listener (in count). Default value is 3, which means the forwarding is considered normal if it is detected to be healthy for three times consecutively. Value range: 2-10. |
| listeners.n.unhealthNum | No | Int | Unhealthy threshold of the load balancer listener (in count). Default value is 3, which means the forwarding is considered abnormal if it is detected to be unhealthy for three times consecutively. Value range: 2-10. |
| listeners.n.httpHash | No | String | Forwarding method of the load balancer listener. This field is only supported for public network-based load balancers with HTTP or HTTPS listeners. Available values: wrr (polling by weight), ip_hash (hashing a value based on the source IP and forwarding the value to the backend server), least_conn <br>(minimum number of connections). Default is wrr. |
| listeners.n.scheduler | No | String | Forwarding method of the load balancer listener. This field is only supported for public network-based load balancers with TCP or UDP listeners. Available values: wrr (polling by weight), least_conn <br>(minimum number of connections). Default is wrr. |
| listeners.n.httpCode | No | Int | For HTTP and HTTPS listeners of public network-based load balancers. This returned code is used to determine health status. Value range: 1-31. Default is 31.<br> 1: It is considered healthy if the health check returns `1xx` codes; 2: It is considered healthy if the health check returns `2xx` codes; 4: It is considered healthy if the health check returns `3xx` codes; 8: It is considered healthy if the health check returns `4xx` codes; 16: It is considered healthy if the health check returns `5xx` codes.<br> If there are multiple codes that can show the health status, enter the accumulated value corresponding to such codes. |
| listeners.n.httpCheckPath | No | String | For HTTP and HTTPS listeners of public network-based load balancers. Default is `/`. Path must start with `/`. |
| listeners.n.SSLMode | No | String | For HTTPS listeners of public network-based load balancers.<br> unidirectional: Unidirectional verification; mutual: Mutual verification.<br><font color="red"> This option is required for HTTPS listeners.</font> |
| listeners.n.certId | No | String | For HTTPS listeners of public network-based load balancers. Server certificate ID. For HTTPS listeners, if this field is left empty, certificate must be uploaded, including certContent, certKey, certName. |
| listeners.n.certCaId | No | String | For HTTPS listeners of public network-based load balancers. Client certificate ID. For HTTPS listeners, if SSLMode=mutual and this field is left empty, client certificate must be uploaded, including certCaContent, certCaName. |
| listeners.n.certCaContent | No | String | Upload content of client certificate. For HTTPS listeners, if SSLMode=mutual and certCaId is left empty, this entry must be uploaded. |
| listeners.n.certCaName | No | String | Upload name of client CA certificate. For HTTPS listeners, if SSLMode=mutual and certCaId is left empty, this entry must be uploaded. |
| listeners.n.certContent | No | String | Upload content of server certificate. For HTTPS listeners, if certId is left empty, this entry must be uploaded. |
| listeners.n.certKey | No | String | Upload key of server certificate. For HTTPS listeners, if certId is left empty, this entry must be uploaded. |
| listeners.n.certName | No | String | Upload name of server certificate. For HTTPS listeners, if certId is left empty, this entry must be uploaded. |



## Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |
| requestId | Int | Request task ID. The operation status can be queried via the API [DescribeLoadBalancersTaskResult](https://cloud.tencent.com/document/api/214/4007). |
| listenerIds | Array | Listener ID array. |


## Example
 
Request
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=CreateLoadBalancerListeners
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
&listeners.0.loadBalancerPort=443
&listeners.0.instancePort=443
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
</pre>
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 28557,
    "listenerIds": [
        "lbl-hox8i4q0"
    ]
}
```


