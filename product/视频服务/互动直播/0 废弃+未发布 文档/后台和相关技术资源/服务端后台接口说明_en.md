# Specifications of Backend APIs (HTTPs)

The client request data is Content Body in HTTPs Req+JSON format, and the data returned to client by the server is Content Body in HTTPs Rsp+JSON format.

## Mutual Authentication
For system security consideration, mutual authentication is required for the requests from a third-party backend. For more information on application for mutual authentication certificate, please see related documentation on Tencent Cloud official website: [Product Documentation - Instant Messaging - A Third-Party Callback - Mutual Authentication Configuration Guide - Nginx Mutual Authentication Configuration Guide](http://cloud.tencent.com/doc/product/269/Nginx双向认证配置指南)


## Format of HTTP Request
The format of HTTP request is: `POST URL HTTP/1.1\r\n`

## URL Format for Backend Services

The URL format is: `/ver/servicename/command?parameter/`, where `ver` is the version number, which is `v3` currently. Servicenanme is `openim`. command varies with different requests.

For example, for the request from audio backend, the URL is: `v3/openim/videorelay`

### Domain name:

Test environment:<https://test.tim.qq.com/>
Formal environment:<https://openapi.tim.qq.com/>

### Command:

| Command | Description |
|---------|---------|
| videorelay | Video chat service |

### Parameter

The format of Parameter is: `usersig=xxxx& identifier=xxxx&sdkappid=xxxx&random=xxxxx&apn=x/`

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| sdkappid | unsigned int | appid assigned when using open APP sdk | It can be found in "Application List" -> "Application Configuration" -> "Application Information" |
| usersig | String | token of open app sdk | It can be found in "Application List" -> "Application Configuration" -> "Account Integration System" -> "Download User Credentials" |
| identifier | String | Admin account | Created by developer and can be found in "Application List" -> "Application Configuration" -> "Account Integration System" -> "Admin Account" |
| random | unsigned int | A random integer parameter identifying the current request | A 32-bit random integer |
| apn | unsigned int | Network type: 0 - Unknown; 1 - WiFi; 2 - 2G; 3 - 3G; 4 - 4G | Enter 0 for backend operation |

### Example
The full URL is as follows:<
https://openapi.tim.qq.com/v3/openim/videorelay?usersig=xxxx&apn=1&identifier=xxxx&sdkappid=xxxx&random=xxxx&contenttype=json>

# Content Definitions of Backend APIs (json)

## Packet structure

"Request Format"

	{
		"reqhead":object of GVCommOprHead
		"reqbody": Determined by the subcommand in GVCommOprHead
	}

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| reqhead | GVCommOprHead | Common header for audio/video services |   |
| reqbody | Determined by the subcommand in GVCommOprHead |   |  

"Response Format"

		{
		"reqhead":object of GVCommOprHead
		"rspbody": Determined by the subcommand in GVCommOprHead
		}

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| reqhead | GVCommOprHead | Common header for audio/video services |   |
| rspbody | Determined by the subcommand in GVCommOprHead |   |    

## Definition of Common Header GVCommOprHead

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
| uint32_sub_cmd | unsigned int/Required | Subcommand: 1: Kicked out room members 5: Request for recording and stopping recording 6:Request for push and stopping push |   |
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

## Content Definition of API Features

### 0x6 sdk Non-interactive Broadcasting Request

- Subcommand: 0x6
- Request: "reqbody":object of req_0x6

		req_0x6
		{
			"uint32_oper":xxx,
			"uint32_live_code":xxx,
			"uint32_sdk_type":xxx,
			"str_channel_name":"xxx",
			"str_channel_describe":"xxx",
			"str_player_pwd":"xxx",
			"uint32_push_data_type":xxx,
			"uint32_tape_flag":xxx,
			"uint32_watermark_flag":xxx,
			"uint32_watermark_id":xxx,
			"rpt_rate_type":[xxx]
		}
Note: The object on which non-interactive push operation is performed is rpt_to_Account, which is a required entry. Only one is allowed

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| uint32_oper | unsigned int | Operation type: 1: Start push; 2: End push; | Start push: Required; End push: Required  |
| uint32_live_code | unsigned int | LVB stream output coding: 1  hls push; 5  rtmp push; 6  hls+rtmp push;  | Start push: Required; End push: Not required  |
| uint32_sdk_type | unsigned int | SDK type: 1: Normal SDK; 2: IoT Camera; | Start push: Required; End push: Required |
| str_channel_name | string | Channel name | Start push: Required; End push: Not required |
| str_channel_describe | string | Channel description | Start push: Required; End push: Not required |
| str_player_pwd | string | You can watch the video only by entering specific password and using the player provided by Tencent Cloud, otherwise the configuration is invalid | Start push: Required; End push: Not required |
| uint32_push_data_type | unsigned int | Type of pushed data: 0: Push data from camera; 1: Push the screen-sharing data; | Start push: Required; End push: Required |
| uint32_tape_flag | unsigned int | Whether to record during push: 0: Do not record; 1: Record;  | Start push: Required; End push: Not required  |
| uint32_watermark_flag	| unsigned int | Whether to add watermark: 0: Do not add watermark; 1: Add watermark;	| Start push: Optional; End push: Not required (If you need to add watermark, upload relevant watermark image in the LVB console; if this parameter is not specified, the watermark is not added by default) |
| uint32_watermark_id | unsigned int | Watermark ID: 0 is default watermark or ID of corresponding watermark | Start push: Optional; End push: Not required (If watermark is enabled but the current parameter is not specified, use the default watermark uploaded by user) |
| rpt_rate_type | unsigned int | Multiple bitrates are supported: 0: Original bitrate; 10: SD bitrate (550K) 20: HD bitrate (900K) | Start push: Optional; End push: Not required (If this parameter is not specified, original bitrate URL is returned by default. Array structure. Multiple arrays of URLs can be returned at the same time)





	"reqbody":
	{
			"req_0x6":
			{
				"uint32_oper":xxx,
				"uint32_live_code":xxx,
				"uint32_sdk_type":xxx,
				"uint32_push_data_type":xxx
			}
	}

- Response: "rspbody":object of rsp_0x6

		rsp_0x6 definition：
		{
		 "uint32_result":xxx,       // Operation result. 0: Successful; other values: Failed
		 "str_errorinfo":"xxx",
		 "msg_live_url":"[xxx]"
		}

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| uint32_result | unsigned int | Operation result: 0: Successful; other values: Failed | For more information about the error codes, please see the appendix |
| str_errorinfo | string | Error information | Error string information |
| uint64_channel_id | unsigned  long long | It is returned when push is enabled |   |
| msg_live_url | [LiveUrl] | LVB URL | See the definition of LiveUrl |
| uint32_tape_task_id | unsigned int | tape_task_id of recording | It is returned only if uint32_tape_flag is set to 1 when push is enabled |

#### LiveUrl

	{
	"uint32_type":"xxx",
	"string_play_url":"xxx"
	"RateType ":xxx
	}

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| uint32_type | unsigned int | LVB stream output coding: 1: HLS push; 5: RTMP push; 6: HLS+RTMP push; |   |
| string_play_url | String | URL of LVB stream output coding |   
| RateType | unsigned int | Bitrate type of this URL: 0: Original bitrate; 10: SD bitrate (550K) 20: HD bitrate (900K) | Original bitrate is used if this parameter is not specified  

***Note: Non-interactive broadcasting can be enabled successfully only after the user joins the audio/video room.***

#### Example of JSON Packet Request:

Take JSON packet for enabling non-interactive broadcasting as an example, you need to replace the parameters in the packet with yours

{

        "reqhead":{
                "uint32_sub_cmd":6,
                "uint32_seq":xxx,
                "uint32_auth_key":xxx,
                "uint32_sdk_appid":xxx,
                "rpt_to_Account":["xxx"],
                "bytes_cookie_buff":"xxx"
        },

        "reqbody":{
                "req_0x6":{
                        "uint32_oper":xxx,
                        "uint32_live_code":xxx,
                        "uint32_sdk_type":xxx,
                        "str_channel_name":"xxx",
                        "str_channel_describe":"xxx",
                        "uint32_push_data_type":xxx,
                        "uint32_tape_flag":xxx
                }
        }
}


### 0x5 sdk Recording Request

- Subcommand: 0x5
- Request: "reqbody":object of req_0x5

		req_0x5
		{
			"uint32_oper":xxx,
			"string_file_name":"xxx",
			"string_tags":["xxx"],
			"uint32_classid":xxx,
			"uint32_IsTransCode":xxx,
			"uint32_IsScreenShot":xxx,
			"uint32_IsWaterMark":xxx,
			"uint32_sdk_type":xxx,
			"uint32_record_data_type":xxx
		}

***Note: The object on which recording operation is performed is rpt_to_Account, which is a required entry. Only one is allowed.***

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| uint32_oper | unsigned int | Operation type: 1: Start recording; 2: End recording; | Start recording: Required; End recording: Required |
| string_file_name | string | Name of recorded file | Start recording: Required; End recording: Leave it empty |
| string_tags | [string] | Video tag list; string array | Start recording: Optional; End recording: Leave it empty |
| uint32_classid | unsigned int | Video Category ID | Start Recording: Optional; End Recording: Leave it empty |
| uint32_IsTransCode | unsigned int | Whether to transcode | Start Recording: Optional; End Recording: Leave it empty |
| uint32_IsScreenShot | unsigned int | Whether to take a screenshot | Start Recording: Optional; End Recording: Leave it empty |
| uint32_IsWaterMark | unsigned int | Whether to add watermark | Start Recording: Optional; End Recording: Leave it empty |
| uint32_sdk_type | unsigned int | SDK type: 1: Normal SDK; 2: IoT Camera; | Start recording: Required; End recording: Required |
| uint32_record_data_type | unsigned int | Type of recorded data: 0: Record data from camera; 1 Record the screen-sharing data; | Start recording: Required; End recording: Required |

	"reqbody":
	{
		"req_0x5":
		{
			"uint32_oper":xxx,
			"string_file_name":xxx,
			"uint32_sdk_type":xxx,
			"uint32_record_data_type":xxx,
		}
	}

- Response: "rspbody":object of rsp_0x5

		Rsp_0x5 definition:
		{
		 "uint32_result":xxx,       // Operation result. 0: Successful; other values: Failed
		 "str_errorinfo":"xxx",
		 "str_fileID":["xxx"]
		}

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| uint32_result | unsigned int | Operation result: 0: Successful; other values: Failed | For more information about the error codes, please see the appendix |
| str_errorinfo | string | Error information | Error string information |
| str_fileID | [String] | Video file ID list; string array. | Returned only at the end of the recording |

***Note: Recording can be enabled successfully only after the user joins the audio/video room.***

# Error Codes

## 0x6 Push Error Codes

| Error Code | Description | Solution |
| --- | --- | --- |
| 40000000 | Failed to resolve SDK request | "Check whether the push request fields are complete"
| 40000001 | Failed to resolve SDK request - The push request packet is missing | "Check whether the push request fields are complete" |
| 40000002 | Failed to resolve SDK request - The operation field of push request is missing | "Check whether the push request fields are complete" |
| 40000003 | Failed to resolve SDK request - The output coding (HLS/RTMP, etc.) of push request is missing | "Check whether the push request fields are complete" |
| 40000004 | Failed to resolve SDK request - The video source type is incorrect (camera/desktop, etc.) | "Check whether the push request fields are complete" |
| 40000005 | Failed to resolve SDK request - Incorrect request operation (request for push, stop push) | "Check whether the push request fields are complete" |
| 40000201 | An error occurred while requesting server for internal data packing | "Report to Tencent customer service" |
| 40000202 | An error occurred while requesting server for internal data packing | "Report to Tencent customer service" |
| 40000203 | An error occurred while requesting server for internal data packing | "Report to Tencent customer service" |
| 40000207 | A communication error occurred while requesting pushing server - Failed to fetch the address of pushing server | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service" |
| 40000208 | A communication error occurred while requesting pushing server - Timeout of request for pushing server | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service" |
| 40000301 | An error occurred while resolving the response packet from push server - Failed to resolve the data packet | "Report to Tencent customer service" |
| 40000302 | An error occurred while resolving the response packet from push server - Failed to resolve the data packet | "Report to Tencent customer service" |
| 40000303 | An error occurred while resolving the response packet from push server - No IP is returned | "Report to Tencent customer service" |
| 40000304 | An error occurred while resolving the response packet from push server - No port is returned | "Report to Tencent customer service" |
| 40000305 | An error occurred while resolving the response packet from push server - No result is returned | "Report to Tencent customer service" |
| 40000306 | An error occurred while resolving the response packet from push server - Overflow of length of returned URL | "Report to Tencent customer service" |
| 40000401 | An error occurred while obtaining the grocery service IP by querying room | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service" |
| 40000402 | An error occurred while fetching grocery data by querying room | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service" |
| 40000403 | grocery does not exist and cannot be fetched by querying room (the room requesting push does not exist) | "Check whether the room has been activated successfully, and whether the user ID and groupid for the push are entered correctly" |
| 40000404 | Timeout while querying room stream-control server | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service" |
| 40000405 | An error occurred with the response packet while querying room - Failed to resolve the data packet | "Report to Tencent customer service" |
| 40000406 | An error occurred with the response packet while querying room - Failed to resolve the data packet | "Report to Tencent customer service" |
| 40000407 | An error occurred with the response packet while querying room - Failed to resolve the data packet | "Report to Tencent customer service" |
| 40000408 | An error occurred with the response packet while querying room - No result is returned | "Report to Tencent customer service" |
| 40000409 | An error occurred with the response packet while querying room - Failed to resolve the data packet | "Report to Tencent customer service" |
| 40000410 | The room requesting push does not exist | "Check whether the room has been activated successfully, and whether the user ID and groupid for the push are entered correctly" |
| 40000411 | The user who initiates the push does not exist in the room | "Check whether the room has been activated successfully, and whether the user ID and groupid for the push are entered correctly" |
| 40000412 | Request for ending push has been sent more than once and the user has ended push | "This indicates that push has ended. No action is needed for this" |
| 40000413 | Request for ending push has been sent more than once and the user has ended push | "This indicates that push has ended. No action is needed for this" |
| 40000414 | An error occurred with internal server operation type while querying room | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service" |
| 40000415 | Request for starting push has been sent more than once and the user is pushing stream | "This indicates that push is already in progress. No action is needed for this" |
| 1001 | Permission error | "It is generally caused by wrong input of sdkappid" |
| 20101 | The number of channels exceeds the limit | "The number of push channels is limited. Check and delete unnecessary channels in the push console" |
| 20406 | Account is in arrears | "Check whether the account is in arrears" |

## 0x5 Recording Error Code Description

| Error Code | Description | Solution |
| --- | --- | --- |
| 30000000 | Failed to resolve SDK request | "Check whether the recording request fields are complete" |
| 30000001 | Failed to resolve SDK request - Recording request packet is missing | "Check whether the recording request fields are complete" |
| 30000002 | Failed to resolve SDK request - Filename field for recorded file is missing | "Check whether the recording request fields are complete" |
| 30000003 | Failed to resolve SDK request - Recording request operation field is missing | "Check whether the recording request fields are complete" |
| 30000004 | Failed to resolve SDK request - The video source type is incorrect (camera/desktop, etc.) | "Check whether the push request fields are complete" |
| 30000201 | An error occurred while requesting server for internal data packing | "Report to Tencent customer service" |
| 30000202 | An error occurred while requesting server for internal data packing | "Report to Tencent customer service" |
| 30000203 | An error occurred while requesting server for internal data packing | "Report to Tencent customer service" |
| 30000207 | A communication error occurred while requesting recording server - Failed to fetch the address of recording server | "Report to Tencent customer service" |
| 30000208 | A communication error occurred while requesting recording server - Timeout of request for recording server | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service" |
| 30000301 | An error occurred while resolving the response packet from recording server - Failed to resolve the data packet | "Report to Tencent customer service" |
| 30000302 | An error occurred while resolving the response packet from recording server - Failed to resolve the data packet | "Report to Tencent customer service" |
| 30000303 | An error occurred while resolving the response packet from recording server - No IP is returned | "Report to Tencent Cloud customer service" |
| 30000304 | An error occurred while resolving the response packet from recording server - No port is returned | "Report to Tencent Cloud customer service" |
| 30000305 | An error occurred while resolving the response packet from recording server - No result is returned | "Report to Tencent customer service" |
| 30000401 | An error occurred while obtaining the grocery service IP by querying room | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service]
| 30000402 | An error occurred while fetching grocery data by querying room | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service" |
| 30000403 | grocery does not exist and cannot be fetched by querying room (room does not exist) | "Check whether the room has been activated successfully, and whether the user ID and groupid for recording are correctly entered" |
| 30000404 | Timeout while querying room stream-control server | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service" |
| 30000405 | An error occurred with the response packet while querying room - Failed to resolve the data packet | "Report to Tencent customer service" |
| 30000406 | An error occurred with the response packet while querying room - Failed to resolve the data packet | "Report to Tencent customer service" |
| 30000407 | An error occurred with the response packet while querying room - Failed to resolve the data packet | "Report to Tencent customer service" |
| 30000408 | An error occurred with the response packet while querying room - No result is returned | "Report to Tencent customer service" |
| 30000409 | An error occurred with the response packet while querying room - Failed to resolve the data packet | "Report to Tencent customer service" |
| 30000410 | Recording room does not exist | "Check whether the room has been activated successfully, and whether the user ID and groupid are correctly entered" |
| 30000411 | Recording room or the initiator of recording does not exist | "Check whether the room has been activated successfully, and whether the user ID and groupid are correctly entered" |
| 30000412 | Request for ending recording has been sent more than once. The user has ended recording | "This indicates recording has ended. Check if the request for ending recording has been sent more than once. No action is needed for this" |
| 30000413 | Request for ending recording has been sent more than once. The user has ended recording | "This indicates recording has ended. Check if the request for ending recording has been sent more than once. No action is needed for this" |
| 30000414 | An error occurred with internal server operation type while querying room | "Report to Tencent customer service" |
| 30000415 | Request for starting recording has been sent more than once and recording has started; or the initiator of recording does not exist | "Check whether the room has been activated successfully, and whether the user ID and groupid for recording are correctly entered" |




