### Request for Recording

- Subcommand (uint32_sub_cmd): enter 0x5 in GVCommOprHead
- Packet structure (reqbody): req_0x5

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


- Response packet structure (rspbody): rsp_0x5

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
| str_fileID | [String] | Video file ID list; string array.  | Returned only at the end of the recording |

***Note: Recording can only be successfully enabled after the user joins the audio/video room.***

# Error Codes

## 0x5 Recording Error Code Description

| Error Code | Description | Solution |
| --- | --- | --- |
| 30000000 | Failed to resolve SDK request | [Check whether the recording request fields are complete] |
| 30000001 | Failed to resolve SDK request - Recording request packet is missing | [Check whether the recording request fields are complete] |
| 30000002 | Failed to resolve SDK request - Filename field for recorded file is missing | [Check whether the recording request fields are complete] |
| 30000003 | Failed to resolve SDK request - Recording request operation field is missing | [Check whether the recording request fields are complete] |
| 30000004 | Failed to resolve SDK request - Incorrect video source type (such as camera, desktop) | [Check whether the recording request fields are complete] |
| 30000201 | An error occurred while requesting server for internal data packing | [Report to Tencent customer service] |
| 30000202 | An error occurred while requesting server for internal data packing | [Report to Tencent customer service] |
| 30000203 | An error occurred while requesting server for internal data packing | [Report to Tencent customer service] |
| 30000207 | A communication error occurred while requesting recording server - Failed to fetch the address of recording server | [Report to Tencent customer service]
| 30000208 | A communication error occurred while requesting recording server - Timeout of request for recording server | [This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service] 
| 30000301 |An error occurred while resolving the response packet from recording server - Failed to resolve the data packet |[Report to Tencent customer service] |
| 30000302 |An error occurred while resolving the response packet from recording server - Failed to resolve the data packet |[Report to Tencent customer service] |
| 30000303 | An error occurred while resolving the response packet from recording server - No IP is returned | [Report to Tencent Cloud customer service] |
| 30000304 |An error occurred while resolving the response packet from recording server - No port is returned | [Report to Tencent Cloud customer service] |
| 30000305 | An error occurred while resolving the response packet from recording server - No result is returned | [Report to Tencent customer service] |
| 30000401 |An error occurred while obtaining the grocery service IP by querying room |[This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service]
| 30000402 | An error occurred while fetching grocery data by querying room |[This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service]
| 30000403 | grocery does not exist and cannot be fetched by querying room (room does not exist) | [Check whether the room has been activated successfully, and whether the user ID and groupid for recording are correctly entered] |
| 30000404 | Timeout while querying room stream-control server | [This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service] |
| 30000405 |An error occurred with the response packet while querying room - Failed to resolve the data packet | [Report to Tencent customer service]
| 30000406 |An error occurred with the response packet while querying room - Failed to resolve the data packet | [Report to Tencent customer service]
| 30000407 |An error occurred with the response packet while querying room - Failed to resolve the data packet | [Report to Tencent customer service]
| 30000408 | An error occurred with the response packet while querying room - No result is returned | [Report to Tencent customer service] |
| 30000409 |An error occurred with the response packet while querying room - Failed to resolve the data packet | [Report to Tencent customer service]
| 30000410 |Recording room does not exist | [Check whether the room has been activated successfully, and whether the user ID and groupid are correctly entered] |
| 30000411 | Recording room or the initiator of recording does not exist | [Check whether the room has been activated successfully, and whether the user ID and groupid are correctly entered] |
| 30000412 | Request for ending recording has been sent more than once. The user has ended recording	|[This indicates recording has ended. Check if the request for ending recording has been sent more than once. No action is needed for this.]
| 30000413 | Request for ending recording has been sent more than once. The user has ended recording	|[This indicates recording has ended. Check if the request for ending recording has been sent more than once. No action is needed for this.]
| 30000414 | An error occurred with internal server operation type while querying room | [Report to Tencent customer service] |
| 30000415 |Request for starting recording has been sent more than once and recording has started; or the initiator of recording does not exist |[Check whether the room has been activated successfully, and whether the user ID and groupid for recording are correctly entered] |


