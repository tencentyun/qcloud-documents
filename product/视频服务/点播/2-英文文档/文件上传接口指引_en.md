## File Upload Interface Description

### Upload Small Files(Less than 5MB) API
1. [Simple Upload](/document/api/436/7749)

### Upload Large Files(More than 5MB) API
1. [Initialize Upload](/document/api/436/7746)
2. [Part Upload](/document/api/436/7750)
3. [Complete Upload](/document/api/436/7742)

## Function Description
1. Upload media (and cover) files.
2. API in which step follow[server upload overview](/document/product/266/9759#.E4.B8.8A.E4.BC.A0.E6.B5.81.E7.A8.8B).

## SDK
It is recommended to use the [packaged SDK](/document/product/436/6474) for API calls.

## Way Of Use

For the usage, please refer to the documents in the above API links, the syntax of each API is:
```
PUT <ObjectName> HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

The following variables in the grammar take values from [VOD return result of Apply Upload](/document/product/266/31767)：  

`<ObjectName>`is **MediaStoragePath** (for the cover file is **CoverStoragePath**)

`<BucketName>-<APPID>`is **StorageBucket** 

`<Region>`is **StorageRegion**

Pay attention to the following two points for API requests:

1. Authorization signature uses [VOD apply upload results](/document/product/266/31767). TempCertificate's SecretId and SecretKey are calculated according to the signature document guidelines.
2. Pass the **x-cos-security-token** field in the HTTP header or the form-data of the POST request packet to identify the security token used by the request and assign a Token field equal to **TempCertificate**
