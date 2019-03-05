# Backend APIs

In addition to the client SDK APIs, ILVB backend also provides a number of APIs for developers to initiate calls from their own servers. Currently supported APIs:    

1. Recording
2. Non-Interactive Broadcasting

## Call Format

The request data is Content Body in HTTPs Req+JSON format, and the response data is Content Body in HTTPs Rsp+JSON format.

## Mutual Authentication
For system security consideration, mutual authentication is required for the requests from a third-party backend. For more information on application for mutual authentication certificate, please see related documentation on Tencent Cloud official website: [Product Documentation - Instant Messaging - A Third-Party Callback - Mutual Authentication Configuration Guide - Nginx Mutual Authentication Configuration Guide](http://cloud.tencent.com/doc/product/269/Nginx双向认证配置指南)


## Format of HTTP Request
The format of HTTP request is: `POST URL HTTP/1.1\r\n`

## URL Format for Backend Services

The URL format is: `/ver/servicename/command?parameter/`, where `ver` is the version number, which is `v3` currently. Servicenanme is `openim`. command varies with different requests.

For example, for the request from audio backend, the URL is: `v3/openim/videorelay`

### Domain name:

Test environment:<https://test.tim.qq.com/><br/>
Formal environment:<https://openapi.tim.qq.com/>

### Command:

| Command | Description |
|---------|---------|
| videorelay | Video chat service |

### Parameter

The format of Parameter is: `usersig=xxxx& identifier=xxxx&sdkappid=xxxx&random=xxxxx&apn=x/`

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| sdkappid | unsigned int | appid assigned when using open App SDK | It can be found in "Application List" -> "Application Configuration" -> "Application Information" |
| usersig | String | token of open app sdk | It can be found in "Application List" -> "Application Configuration" -> "Account Integration System" -> "Download User Credentials"  |
| identifier | String | Admin account | Created by developer and can be found in "Application List" -> "Application Configuration" -> "Account Integration System" -> "Admin Account" |
| random | unsigned int | A random integer parameter identifying the current request | A 32-bit random integer |
| apn | unsigned int | Network type: 0 - Unknown; 1 - WiFi; 2 - 2G; 3 - 3G; 4 - 4G | Enter 0 for backend operation |

### Example
The full URL is as follows:<
https://openapi.tim.qq.com/v3/openim/videorelay?usersig=xxxx&apn=1&identifier=xxxx&sdkappid=xxxx&random=xxxx&contenttype=json>

# Content Definitions of Backend APIs

## Packet structure
### Request content consists of common header (GVCommOprHead) and specific packet,  as shown below:

[Request Format]

	{
		"reqhead": object of GVCommOprHead
		"reqbody": Determined by the subcommand in GVCommOprHead
	}

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| reqhead | GVCommOprHead | Common header for audio/video services |  |
| reqbody | Determined by the subcommand in GVCommOprHead |   |   |    |
### Response content consists of common header (GVCommOprHead) and specific packet,  as shown below:
[Response Format]

		{
		"reqhead":object of GVCommOprHead
		"rspbody": Determined by the subcommand in GVCommOprHead
		}

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| reqhead | GVCommOprHead | Common header for audio/video services |   |
| rspbody | Determined by the subcommand in GVCommOprHead |   |    |   |

## Definition of Common Header (GVCommOprHead)

	{
	 "uint32_sub_cmd":xxx,
	 "uint32_seq":xxx,
	 "uint32_auth_key":xxxx,
	 "uint32_sdk_appid":xxx,
	 "str_av_token":"xxx",
	 "str_openid:"xxxx",
	 "rpt_to_Account":["xxxx"],
	 "bytes_cookie_buff":"xxxx",
	 "uint32_result:"xxxx",
	 "str_error_msg:"xxxx"
	}

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| uint32_sub_cmd | unsigned int/Required | Subcommand: 0x5: Request for recording and stopping recording; 0x6: Request for push and stopping push |   |
| uint32_seq | unsigned int/Required | Sequence number of the request | To be returned unchanged by the third party backend |
| uint32_auth_key | unsigned int/Required | Group number | The group defined by a third party |
| uint32_sdk_appid | unsigned int/Required | Open sdk appid |
| str_av_token | String/Optional | Authentication identifier for a third party to call QQ audio/video services (not required)  |   |
| str_openid | String/Optional | The openid that initiates the operation. Not required for backend operation |   |
| rpt_to_Account | String/Optional | List of openids you are working with.**A maximum of 10 openids are allowed.** For the meanings of each of them, please see the business packet | **only one is allowed for 0x5 and 0x6 requests** |
| uint32_result | int/Optional | Non-business result (0: Successful; non-0: Failure) -1: unpacking error; -2: packet error; -3: internal service failed; -4: header verification failed; -5: The av_token verification failed | Only used in the response message |
| str_error_msg | String/Optional | Error message | Only used in the response message |
| bytes_cookie_buff | String | Business cook, which is returned unchanged in response

[Sample Code]

	"reqhead":
	{
		"uint32_sub_cmd":6,
		"uint32_seq":xxx,
		"uint32_auth_key":xxx,
		"uint32_sdk_appid":xxx,
		"rpt_to_Account":["xxx"],
		"bytes_cookie_buff":"xxxx"
	},

