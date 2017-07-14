## 1. API Description
 The CreateLoadBalancerListeners API is used to create cloud load balancer listeners. Cloud load balancer listener provides specific rules for forwarding user requests, such as port, protocol, session duration, health check and other parameters.
 
Domain for API access: lb.api.qcloud.com
 
Listener configuration rules are as follows:

Usage limit for public network (with daily rate) cloud load balancers:
1) Within one cloud load balancer, a balancer port can only correspond to one protocol type,
2) Within one cloud load balancer, a balancer port can correspond to multiple CVM ports,
3) HTTP, UDP, TCP, HTTPS protocols are supported,
4) Batch creation is not supported when creating HTTPS listeners.

Usage limit for private network cloud load balancers:
1) Within one cloud load balancer, a balancer port can only correspond to one protocol type,
2) Within one cloud load balancer, a balancer port can correspond to multiple CVM ports,
3) Within one cloud load balancer, CVMs must have different ports,
4) UDP, TCP protocols are supported.

## 2. Request Parameters
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is CreateLoadBalancerListeners.


| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| loadBalancerId | Yes | String | The ID of the cloud load balancer instance, which can be loadBalancerId or unLoadBalancerId (recommended). You can query it via the API <a href="https://www.qcloud.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listeners.n.loadBalancerPort | Yes | Int | Listening API of the cloud load balancer listener. Value range: 1-65535. "listeners" is an array, you may create multiple listeners. n is subscript. |
| listeners.n.instancePort | Yes | Int | Listening port of the cloud load balancer instance listener backend CVM. Value range: 1-65535. |
| listeners.n.protocol | Yes | Int | Protocol type of the cloud load balancer instance listener. 1: HTTP, 2: TCP, 3:UDP, 4: HTTPS. <br>Public network (with daily rate) cloud load balancer instances support HTTP, UDP, TCP, HTTPS protocols; <br>Private network cloud load balancer instances support TCP and UDP protocols. |
| listeners.n.listenerName | No | String | Name of the cloud load balancer listener. |
| listeners.n.sessionExpire | No | Int | Session duration of the cloud load balancer listener. Unit: second. <br>Value range for non-HTTP listeners of public network (with daily rate) cloud load balancer instances: 900-3600; <br>Session duration value range for HTTP and HTTPS listeners of public network (with daily rate) cloud load balancer instances: 30-3600; <br>Configuration of this field is not supported for private network cloud load balancer instances. |
| listeners.n.healthSwitch | No | Int | Indicate whether health check is enabled for cloud load balancer instance listener. 1: On; 0: Off. Default value is 1 (On). |
| listeners.n.timeOut | No | Int | Health check response timeout for the cloud load balancer listener. Value range: 2-60. Default is 2. Unit: second. <br><font color="red">The response timeout must be smaller than health check time interval. </font><br>Currently you cannot configure response timeout for public network (with daily rate) HTTP or HTTPS listeners. |
| listeners.n.intervalTime | No | Int | Health check time interval of cloud load balancer listener. Default value: 5; value range: 5-300; unit: second. <br>Value range for HTTPS and HTTP protocols: 30-300 seconds. Default is 30. |
| listeners.n.healthNum | No | Int | Healthy threshold of cloud load balancer listener. Default value is 3, which means the forwarding is considered normal if it is detected to be healthy for three times consecutively. Value range: 2-10; unit: time. |
| listeners.n.unhealthNum | No | Int | Unhealthy threshold of cloud load balancer listener. Default value is 3, which means the forwarding is considered abnormal if it is detected to be unhealthy for three times consecutively. Value range: 2-10; unit: time. |
| listeners.n.httpHash | No | Int | Forwarding method of cloud load balancer listeners. This field is only supported for public network (with daily rate) HTTP or HTTPS listeners. Available values: wrr (weighted round robin), <br>ip_hash (IP_HASH). Default is wrr. |
| listeners.n.httpCode | No | Int | For HTTP and HTTPS listeners, this returned code is used to determine health status. Value range: 1-31. The default is 31. <br>1: it is considered healthy if the health check returns `1xx` codes; 2: it is considered healthy if the health check returns `2xx` codes; 4: it is considered healthy if the health check returns `3xx` codes; 8: it is considered healthy if the health check returns `4xx` codes; 16: it is considered healthy if the health check returns `5xx` codes. <br>If there should be multiple types of codes that can indicate healthy status, enter the accumulated value corresponding to such codes. |
| listeners.n.httpCheckPath | No | String | The health check path for HTTP and HTTPS listeners. Default is `/`. Path must start with `/`. |
| listeners.n.SSLMode | No | String | Authentication type of HTTPS protocols. <br>unidirectional: unidirectional authentication; mutual: mutual authentication. <br><font color="red">This option is mandatory for listeners of HTTPS protocol. </font>|
| listeners.n.certId | No | String | ID of server certificate. For HTTPS listeners, if this field is left empty, you must upload certificate, including certContent, certKey, certName |
| listeners.n.certCaId | No | String | ID of client certificate. For HTTPS listeners, if SSLMode=mutual and this field is left empty, you must upload client certificate, including certCaContent, certCaName |
| listeners.n.certCaContent | No | String | Upload content of client certificate. For HTTPS listeners, if SSLMode=mutual and there is no certCaId, you must upload this content |
| listeners.n.certCaName | No | String | Upload name of client CA certificate. For HTTPS listeners, if SSLMode=mutual and there is no certCaId, you must upload this content. |
| listeners.n.certContent | No | String | Upload content of server certificate. For HTTPS listeners, if there is no certId, you must upload this content. |
| listeners.n.certKey | No | String | Upload key of server certificate. For HTTPS listeners, if there is no certId, you must upload this key. |
| listeners.n.certName | No | String | Upload name of server certificate. For HTTPS listeners, if there is no certId, you must upload this name. |



## 3. Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to [Common Error Code](/doc/api/244/1530) in the Error Code page. |
| message | String | Module error message description depending on API. |
| requestId | Int | Request task ID. The operation status can be queried through API [DescribeLoadBalancersTaskResult](/doc/api/244/4007). |
| listenerIds | Array | Listener ID array. |


## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=CreateLoadBalancerListeners
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
&listeners.1.loadBalancerPort=443
&listeners.1.instancePort=443
&listeners.1.protocol=4
&listeners.1.SSLMode=mutual
&listeners.1.certName=myCertName
&listeners.1.certContent=-----BEGIN CERTIFICATE-----
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
&listeners.1.certKey=-----BEGIN RSA PRIVATE KEY-----
			your own key
			-----END RSA PRIVATE KEY-----
&listeners.1.certCaContent=-----BEGIN CERTIFICATE-----
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
&listeners.1.certCaName=myCertCaName
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "requestId": 28557,
    "listenerIds": [
        "lbl-hox8i4q0"
    ]
}
```



