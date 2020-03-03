## 1. API Description
This API (CertUpload) is used to upload certificates.
Domain name for API request: wss.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is CertUpload.

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| cert | Yes | String | Certificate content |
| certType | Yes | String | Certificate type (CA means client certificate and SVR means server certificate) |
| key | No | String | Certificate private key, which is required when certType = SVR)
| alias | No | String | Certificate remark |

## 3. Output Parameters
| Parameter | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="common error codes">common error codes</a> in the error codes page.|
| message | String | Module error message description depending on API.|
| data | Array | Data returned by the API. |

The "data" parameter contains the number of domain names under the account as well as the list of domain names, where

| Parameter | Type | Description |
|---------|---------|---------|
|  id    |  String | Certificate id |

## 4. Example
```
https://wss.api.qcloud.com/v2/index.php?
&<Common request parameters>
&Action=CertUpload
&cert=-----BEGIN+CERTIFICATE-----%0D%0AMIIFxTCCBK2gAwIBAgIQExOG1fLHj38bcWMxgd%2BcUTANBgkqhkiG9w0BAQsFADCB%0D%0AlzELMAkGA1UEBhMCQ04xJTAjBgNVBAoTHFRydXN0QXNpYSBUZWNobm9sb2dpZXMs%0D%0AIEluYy4xHzAdBgNVBAsTFlN5bWFudGVjIFRydXN0IE5ldHdvcmsxHTAbBgNVBAsT%0D%0AFERvbWFpbiBWYWxpZGF0ZWQgU1NMMSEwHwYDVQQDExhUcnVzdEFzaWEgRFYgU1NM%0D%0AIENBIC0gRzUwHhcNMTcwMzIzMDAwMDAwWhcNMTgwMzIzMjM1OTU5WjAcMRowGAYD%0D%0AVQQDDBFzYWRmZGFzZi5mLXhqLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC%0D%0AAQoCggEBAIlljWcJfs3Zc4qVhq4IhijOPt9dX3E3%2BT4z3EtPdCfZ54%2Fff9IRiR8M%0D%0AAh9f5JUWBK3aVYfv2%2BQE5GYBs6VFqLp5xpEDKEzPOm2D2qyuqGSxMyhWGQU%2BNS3i%0D%0AQMu%2BTI0PttvOpqMYnIUXyHLgRd6rXnJB7pB0Yy%2FXKvZEZ5QlFgpbsdLWzoPUS9qD%0D%0Av%2B2z5T5mhmU8LzQLoj1dhzSTi9I%2FDxbhhBS3KwO4Dy4mju2PesAU9IiNVdiJnMPu%0D%0AzlrT7QEMhvo%2BxWM0LNBH5YfWiA0HDh5M5A02SA6ac%2Bzyn5sJqPlfBZFdrnMqkM44%0D%0AN%2FarM0VCmL9s1QYKVEXUb%2BhlVjLv3wcCAwEAAaOCAoUwggKBMBwGA1UdEQQVMBOC%0D%0AEXNhZGZkYXNmLmYteGouY29tMAkGA1UdEwQCMAAwYQYDVR0gBFowWDBWBgZngQwB%0D%0AAgEwTDAjBggrBgEFBQcCARYXaHR0cHM6Ly9kLnN5bWNiLmNvbS9jcHMwJQYIKwYB%0D%0ABQUHAgIwGQwXaHR0cHM6Ly9kLnN5bWNiLmNvbS9ycGEwHwYDVR0jBBgwFoAUbVjH%0D%0Afxrn4T8upoyXNUK79NM4rD8wDgYDVR0PAQH%2FBAQDAgWgMB0GA1UdJQQWMBQGCCsG%0D%0AAQUFBwMBBggrBgEFBQcDAjCBmwYIKwYBBQUHAQEEgY4wgYswPAYIKwYBBQUHMAGG%0D%0AMGh0dHA6Ly90cnVzdGFzaWEyLW9jc3AuZGlnaXRhbGNlcnR2YWxpZGF0aW9uLmNv%0D%0AbTBLBggrBgEFBQcwAoY%2FaHR0cDovL3RydXN0YXNpYTItYWlhLmRpZ2l0YWxjZXJ0%0D%0AdmFsaWRhdGlvbi5jb20vdHJ1c3Rhc2lhZzUuY3J0MIIBAwYKKwYBBAHWeQIEAgSB%0D%0A9ASB8QDvAHUA3esdK3oNT6Ygi4GtgWhwfi6OnQHVXIiNPRHEzbbsvswAAAFa%2BfdN%0D%0AXwAABAMARjBEAiBkrtXs%2BrqHITwJqQMpu0SIdjKliny1vqpHjo%2BoAzItzQIgdPmV%0D%0A0BcClvGrPAvAMWvy6tBuricc%2FKclgriZlCnT1n0AdgCkuQmQtBhYFIe7E6LMZ3AK%0D%0APDWYBPkb37jjd80OyA3cEAAAAVr5902NAAAEAwBHMEUCID8Dvmmw70QF021Y4i3y%0D%0ArAB9L0gs8JhJJ%2FfCPBiJRhhoAiEAjkZSMIXAMbr4CW0KViR3wgZo%2F%2BMqP%2FhJNmIe%0D%0Awm3KOaowDQYJKoZIhvcNAQELBQADggEBABnpDVVmTDrsfcbpchMQAitWmncXvk2P%0D%0AU%2F%2FLHQ06cY%2BpTJ%2B2ARLBaImkHfJhKCxav4%2BYZkLpYrmJcQ2stYdErloZtr4t932f%0D%0AO%2F2HUiSJ8nsNTw7JuTg0ZU0kuTRQdaMzMJh%2FnID%2BYJctmeCvwCaiK%2B6WtSc2Vg0I%0D%0AwBt%2FgPMiWiBHnItlJqH4RaOhwjxJi2rYYmQ7Pe0MLTg4QJF5u0C8kO0JfXwYx3GS%0D%0AriHMBZXZG%2BajlZbBTRGTCBW7mDiTg9%2BitfJI6qHGHjpWOscCdUwNZq6bVgUd%2FVGH%0D%0A5WAq11Pgi9KlqF7gZpeodXRJaW0WQrtVO15BWfte9Msal0TpMmbkQ0M%3D%0D%0A-----END+CERTIFICATE-----%0D%0A%0D%0A-----BEGIN+CERTIFICATE-----%0D%0AMIIFZTCCBE2gAwIBAgIQOhAOfxCeGsWcxf%2F2QNXkQjANBgkqhkiG9w0BAQsFADCB%0D%0AyjELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL%0D%0AExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAwNiBWZXJp%0D%0AU2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxW%0D%0AZXJpU2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0%0D%0AaG9yaXR5IC0gRzUwHhcNMTYwODExMDAwMDAwWhcNMjYwODEwMjM1OTU5WjCBlzEL%0D%0AMAkGA1UEBhMCQ04xJTAjBgNVBAoTHFRydXN0QXNpYSBUZWNobm9sb2dpZXMsIElu%0D%0AYy4xHzAdBgNVBAsTFlN5bWFudGVjIFRydXN0IE5ldHdvcmsxHTAbBgNVBAsTFERv%0D%0AbWFpbiBWYWxpZGF0ZWQgU1NMMSEwHwYDVQQDExhUcnVzdEFzaWEgRFYgU1NMIENB%0D%0AIC0gRzUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC39aSJZG%2F97x3a%0D%0A6Qmuc9%2BMubagegRAVUmFYHTYTs8IKB2pM7wXN7W8mekdZaEgUjDFxvRBK%2FDhTb7U%0D%0A8ONLsKKdT86aOhzbz2noCTn9wPWnGwkg%2B%2F4YKg%2FdPQQdV9tMsSu0cwqInWHxSAkm%0D%0AAI1hYFC9D7Sf7Hp%2F5cRcD%2BdK454YMRzNOGLQnCVI8JEqrz6o9SOvQNTqTcfqt6DC%0D%0A0UlXG%2BMPD1eNPjlzf1Vwaab%2BVSTgySoC%2BIkbq2VsdykeOiGXW%2FOIiASH7%2B2LcR05%0D%0APmQ7GEOlM8yzoVojFpM8sHz%2BWxI05ZOPri5%2BvX3HhHHjWr5432G0dVmgohnZvlVZ%0D%0Aoy8XrlbpAgMBAAGjggF2MIIBcjASBgNVHRMBAf8ECDAGAQH%2FAgEAMC8GA1UdHwQo%0D%0AMCYwJKAioCCGHmh0dHA6Ly9zLnN5bWNiLmNvbS9wY2EzLWc1LmNybDAOBgNVHQ8B%0D%0AAf8EBAMCAQYwLgYIKwYBBQUHAQEEIjAgMB4GCCsGAQUFBzABhhJodHRwOi8vcy5z%0D%0AeW1jZC5jb20wYQYDVR0gBFowWDBWBgZngQwBAgEwTDAjBggrBgEFBQcCARYXaHR0%0D%0AcHM6Ly9kLnN5bWNiLmNvbS9jcHMwJQYIKwYBBQUHAgIwGRoXaHR0cHM6Ly9kLnN5%0D%0AbWNiLmNvbS9ycGEwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMCkGA1Ud%0D%0AEQQiMCCkHjAcMRowGAYDVQQDExFTeW1hbnRlY1BLSS0yLTYwMTAdBgNVHQ4EFgQU%0D%0AbVjHfxrn4T8upoyXNUK79NM4rD8wHwYDVR0jBBgwFoAUf9Nlp8Ld7LvwMAnzQzn6%0D%0AAq8zMTMwDQYJKoZIhvcNAQELBQADggEBABUphhBbeG7scE3EveIN0dOjXPgwgQi8%0D%0AI2ZAKYm6DawoGz1lEJVdvFmkyMbP973X80b7mKmn0nNbe1kjA4M0O0hHaMM1ZaEv%0D%0A7e9vHEAoGyysMO6HzPWYMkyNxcCV7Nos2Uv4RvLDpQHh7P4Kt6fUU13ipcynrtQD%0D%0A1lFUM0yoTzwwFsPu3Pk%2B94hL58ErqwqJQwxoHMgLIQeMVHeNKcWFy1bddSbIbCWU%0D%0AZs6cMxhrra062ZCpDCbxyEaFNGAtYQMqNz55Z%2F14XgSUONZ%2FcJTns6QKhpcgTOwB%0D%0AfnNzRnk%2BaWreP7osKhXlz4zs%2BllP7goBDKFOMMtoEXx3YjJCKgpqmBU%3D%0D%0A-----END+CERTIFICATE-----
&certType=SVR
&key=-----BEGIN+RSA+PRIVATE+KEY-----%0D%0AMIIEogIBAAKCAQEAiWWNZwl%2BzdlzipWGrgiGKM4%2B311fcT...(Omitted)...dTh0tEPGcssOuNtHEFW4RywOQVGihxe%2BcszCTo0u%2FiJSS5w8M%3D%0D%0A-----END+RSA+PRIVATE+KEY-----
```

The returned results are as below:
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data":{
		id: "9hyvgrkE"
	}
}
```

