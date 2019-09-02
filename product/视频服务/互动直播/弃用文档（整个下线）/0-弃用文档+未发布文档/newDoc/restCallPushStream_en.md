
### Non-interactive Broadcasting Request

- Subcommand (uint32_sub_cmd): Enter 0x6 in GVCommOprHead
- Packet structure: req_0x6

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
***Note: The object that is operated in non-interactive broadcasting is rpt_to_Account (required), and only one object is supported***

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| uint32_oper | unsigned int | Operation type: 1: Enable non-interactive broadcasting; 2: Stop non-interactive broadcasting; | Enable non-interactive broadcasting: Required; Stop non-interactive broadcasting: Required  |
| uint32_live_code | unsigned int | LVB stream output coding:  1: HLS non-interactive broadcasting; 5: RTMP non-interactive broadcasting; 6: HLS+RTMP non-interactive broadcasting  | Enable non-interactive broadcasting: Required; Stop non-interactive broadcasting: Not required  |
| uint32_sdk_type | unsigned int | SDK type: 1: Normal SDK; 2: IoT Camera; | Enable non-interactive broadcasting: Required; Stop non-interactive broadcasting: Required |
| str_channel_name | string | Channel name | Enable non-interactive broadcasting: Required; Stop non-interactive broadcasting: Not required |
| str_channel_describe | string | Channel description | Start non-interactive broadcasting: Optional; Stop non-interactive broadcasting: Not required |
| str_player_pwd | string | You can watch the video only by entering specific password and using the player provided by Tencent Cloud, otherwise the configuration is invalid | Enable non-interactive broadcasting: Required; Stop non-interactive broadcasting: Not required |
| uint32_push_data_type | unsigned int | Data type of non-interactive broadcasting: 0: Non-interactive broadcasting camera; 1: Non-interactive broadcasting data for screen sharing; | Enable non-interactive broadcasting: Required; Stop non-interactive broadcasting: Required  |
| uint32_tape_flag | unsigned int | Whether to record during non-interactive broadcasting: 0: Do not record; 1: Record;  | Enable non-interactive broadcasting: Required; Stop non-interactive broadcasting: Not required  |
| uint32_watermark_flag	| unsigned int | Whether to add watermark: 0: Do not add watermark; 1: Add watermark;	| Start non-interactive broadcasting: Optional; Stop non-interactive broadcasting: Not required (If you need to add watermark, upload relevant watermark image in the LVB console; if this parameter is not specified, the watermark is not added by default) |
| uint32_watermark_id | unsigned int | Watermark ID: 0 is default watermark or ID of corresponding watermark | Start non-interactive broadcasting: Optional; Stop non-interactive broadcasting: Not required (If watermark is enabled but the current parameter is not specified, use the default watermark uploaded by user) |
| rpt_rate_type | unsigned int | Multiple bitrates are supported: 0: Original bitrate; 10: SD bitrate (550K) 20: HD bitrate (900K) | Start non-interactive broadcasting: Optional; Stop non-interactive broadcasting: Not required (If this parameter is not specified, original bitrate URL is returned by default. Array structure. Multiple arrays of URLs can be returned at the same time)





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

- Response packet structure (rspbody): rsp_0x6

		rsp_0x6 definition:
		{
		 "uint32_result":xxx,       // Operation result. 0: Successful; other values: Failed
		 "str_errorinfo":"xxx",
		 "msg_live_url":"[xxx]"
		}

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| uint32_result | unsigned int | Operation result: 0: Successful; other values: Failed | For more information about the error codes, please see appendix |
| str_errorinfo | string | Error information | Error string information |
| uint64_channel_id | unsigned  long long | It is returned when non-interactive broadcasting is enabled |   |
| msg_live_url | [LiveUrl] | LVB URL | See the definition of LiveUrl |
| uint32_tape_task_id | unsigned int | tape_task_id of recording | It is returned only if uint32_tape_flag is set to 1 when non-interactive broadcasting is enabled |

#### LiveUrl

	{
	"uint32_type":"xxx",
	"string_play_url":"xxx"
	"RateType ":xxx
	}

| Parameter Name | Type | Description | Note |
| --- | --- | --- | --- |
| uint32_type | unsigned int | LVB stream output coding: 1: HLS non-interactive broadcasting; 5: RTMP non-interactive broadcasting; 6: HLS+RTMP non-interactive broadcasting; |   |
| string_play_url | String | URL of LVB stream output coding |   | 
| RateType | unsigned int | Bitrate type of this URL:  0: Original bitrate; 10: SD bitrate (550K) 20: HD bitrate (900K) | Original bitrate is used if this parameter is not specified  | 

***Note: non-interactive broadcasting can only be successfully enabled after the user joins the audio/video room.

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




# Error Codes

## 0x6 non-interactive broadcasting Error Codes

| Error Code | Description | Solution |
| --- | --- | --- |
| 40000000 | Failed to resolve SDK request | [Check whether the non-interactive broadcasting request fields are complete] |
| 40000001 | Failed to resolve SDK request - The non-interactive broadcasting request packet is missing | [Check whether the non-interactive broadcasting request fields are complete] |
| 40000002 | Failed to resolve SDK request - The non-interactive broadcasting request operation field is missing | [Check whether the non-interactive broadcasting request fields are complete] |
| 40000003 | Failed to resolve SDK request - The output coding (HLS/RTMP, etc.) of non-interactive broadcasting request is missing | [Check whether the non-interactive broadcasting request fields are complete] |
| 40000004 | Failed to resolve SDK request - Incorrect video source type (camera/desktop, etc.) | Check whether the non-interactive broadcasting request fields are complete |
| 40000005 | Failed to resolve SDK request - Incorrect request operation (request for non-interactive broadcasting , stop non-interactive broadcasting ) | "Whether the non-interactive broadcasting request fields are entered completely" |
| 40000201 | An error occurred while requesting server for internal data packing | [Report to Tencent customer service] |
| 40000202 | An error occurred while requesting server for internal data packing | [Report to Tencent customer service] |
| 40000203 | An error occurred while requesting server for internal data packing | [Report to Tencent customer service] |
| 40000207	| A communication error occurred while requesting non-interactive broadcasting server - Failed to fetch the address of non-interactive broadcasting server	| [This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service] |
| 40000208	| A communication error occurred while requesting non-interactive broadcasting server - Request for non-interactive broadcasting server timed out | [This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service] |
| 40000301 |An error occurred while resolving the response packet from non-interactive broadcasting server - Failed to resolve the data packet |[Report to Tencent customer service] |
| 40000302 |An error occurred while resolving the response packet from non-interactive broadcasting server - Failed to resolve the data packet |[Report to Tencent customer service] |
| 40000303 | An error occurred while resolving the response packet from non-interactive broadcasting server - No IP is returned | [Report to Tencent customer service] |
| 40000304 | An error occurred while resolving the response packet from non-interactive broadcasting server - No port is returned | [Report to Tencent customer service] |
| 40000305 | An error occurred while resolving the response packet from non-interactive broadcasting server - No result is returned | Report to Tencent customer service |
| 40000306 | An error occurred while resolving the response packet from non-interactive broadcasting server - Overflow of length of returned URL | Report to Tencent customer service |
| 40000401 |An error occurred while obtaining the grocery service IP by querying room | This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service |
| 40000402 | An error occurred while fetching grocery data by querying room | [This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service] |
| 40000403 | grocery does not exist and cannot be fetched by querying room (the room requesting non-interactive broadcasting does not exist) | [Check whether the room has been activated successfully, and whether the user ID and groupid for non-interactive broadcasting are correctly entered] |
| 40000404 | Timeout while querying room stream-control server | [This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service] |
| 40000405 |An error occurred with the response packet while querying room - Failed to resolve the data packet | [Report to Tencent customer service] |
| 40000406 |An error occurred with the response packet while querying room - Failed to resolve the data packet | [Report to Tencent customer service] |
| 40000407 |An error occurred with the response packet while querying room - Failed to resolve the data packet | [Report to Tencent customer service] |
| 40000408 | An error occurred with the response packet while querying room - No result is returned | [Report to Tencent customer service] |
| 40000409 |An error occurred with the response packet while querying room - Failed to resolve the data packet | [Report to Tencent customer service] |
| 40000410 | The room requesting non-interactive broadcasting does not exist | [Check whether the room has been activated successfully, and whether the user ID and groupid for non-interactive broadcasting are entered correctly] |
| 40000411 | The user who initiates the non-interactive broadcasting does not exist in the room | [Check whether the room has been activated successfully, and whether the user ID and groupid for the non-interactive broadcasting are entered correctly] |
| 40000412 | Request for ending non-interactive broadcasting has been sent more than once. User has ended non-interactive broadcasting | [This indicates non-interactive broadcasting has ended. No action is needed for this] |
| 40000413 | Request for ending non-interactive broadcasting has been sent more than once. User has ended non-interactive broadcasting | [This indicates non-interactive broadcasting has ended. No action is needed for this] |
| 40000414	| An error occurred with internal server operation type while querying room | [This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service] |
| 40000415 | Request for starting non-interactive broadcasting has been sent more than once. Non-interactive broadcasting is in progress | [This indicates non-interactive broadcasting is already in progress. No action is needed for this] |
| 1001 | Permission error | [This is often caused by incorrectly entered sdkappid] |
| 20101 | The number of channels exceeds the limit | [A limit is imposed on the number of non-interactive broadcasting channels. Check for and delete unnecessary channels in the non-interactive broadcasting console] |
| 20406 | Account is in arrears | [Check whether the account is in arrears] |


