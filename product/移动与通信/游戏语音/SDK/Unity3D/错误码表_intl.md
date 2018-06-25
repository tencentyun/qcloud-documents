## 1 Overview
This document introduces the error codes of GVoice C++ API SDK.

      
## 2 Error Code List
	
|Error	|Hexadecimal value |Decimal value |Meaning|
|--|--|--|--|
|GCLOUD_VOICE_SUCC|	0x0|	0	|Success|
|GCLOUD_VOICE_PARAM_NULL|	0x1001|	4097	|Some parameters are null|
|GCLOUD_VOICE_NEED_SETAPPINFO|	0x1002	|4098|	Need to call SetAppInfo first before calling other APIs|
|GCLOUD_VOICE_INIT_ERR|	0x1003|	4099|	Init Error|
|GCLOUD_VOICE_RECORDING_ERR|	0x1004	|4100|	Operation failed as it's recording now|
|GCLOUD_VOICE_POLL_BUFF_ERR|	0x1005|	4101|	poll buffer is not enough or null|
|GCLOUD_VOICE_MODE_STATE_ERR|	0x1006|	4102|	call some api, but the mode is not correct, maybe you shoud call SetMode first and correct|
|GCLOUD_VOICE_PARAM_INVALID|	0x1007|	4103	|some param is null or value is invalid for our request, used right param and make sure is value range is correct by our comment|
|GCLOUD_VOICE_OPENFILE_ERR|	0x1008	|4104|	Error while opening a file|
|GCLOUD_VOICE_NEED_INIT|	0x1009|	4105|	Need to call Init before this operation|
|GCLOUD_VOICE_ENGINE_ERR|	0x100A|	4106	|you have not get engine instance, this common in use c# api. but not get gcloudvoice instance first|
|GCLOUD_VOICE_POLL_MSG_PARSE_ERR|	0x100B|	4107|	this common in c# api, parse poll msg err|
|GCLOUD_VOICE_POLL_MSG_NO|	0x100C	|4108|	poll no msg to update|
|GCLOUD_VOICE_REALTIME_STATE_ERR|	0x2001|	8193	|call some realtime api, but state err. such as OpenMic but you have not Join Room first|
|GCLOUD_VOICE_JOIN_ERR|	0x2002	|8194	|Failed to join the room|
|GCLOUD_VOICE_QUIT_ROOMNAME_ERR|	0x2003|	8195|	Error while quitting. The quitting roomname does not match the joining roomname|
|GCLOUD_VOICE_OPENMIC_NOTANCHOR_ERR|	0x2004|	8196|	open mic in bigroom,but not anchor role|
|GCLOUD_VOICE_AUTHKEY_ERR|	0x3001|	12289|	apply authkey api error|
|GCLOUD_VOICE_PATH_ACCESS_ERR|	0x3002	|12290|	Failed to access the path: the file does not exist or the access is denied|
|GCLOUD_VOICE_PERMISSION_MIC_ERR|	0x3003|	12291|	you have not right to access micphone in android|
|GCLOUD_VOICE_NEED_AUTHKEY|	0x3004|	12292|	Call ApplyMessageKey to get the authkey first|
|GCLOUD_VOICE_UPLOAD_ERR	|0x3005	|12293|	upload file err|
|GCLOUD_VOICE_HTTP_BUSY|	0x3006|	12294|	http is busy,maybe the last upload/download not finish.|
|GCLOUD_VOICE_DOWNLOAD_ERR|	0x3007|	12295|	download file err|
|GCLOUD_VOICE_SPEAKER_ERR|	0x3008|	12296|	open or close speaker tve error|
|GCLOUD_VOICE_TVE_PLAYSOUND_ERR|	0x3009|	12297|	tve play file error|
|GCLOUD_VOICE_INTERNAL_TVE_ERR|	0x5001|	20481|	internal TVE err, our used|
|GCLOUD_VOICE_INTERNAL_VISIT_ERR	|0x5002	|20482	|internal Not TVE err, out used|
|GCLOUD_VOICE_INTERNAL_USED|	0x5003|	20483|	internal used, you should not get this err num|

