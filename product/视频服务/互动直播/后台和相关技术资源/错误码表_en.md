## IMSDK Error Codes
Since ILVB SDK contains IMSDK, some error codes are returned by IMSDK. Click **[here](/doc/product/269/1671)** to view the error codes.

## AVSDK Client Error Codes

| Error Code Name | Error Code Value | Description | Reason | Solution
|---------|---------|---------|---------|---------|
| AV_ERR_FAILED | 1 | General error | Find the specific reason by analyzing log | Analyze log
| AV_ERR_REPEATED_OPERATION | 1001 | Repetitive operation | "This error occurs while performing a certain operation if the same operation is already in process. This error occurs while performing the operation of joining room if you are joining the room. Operations are mainly categorized into four types: AVContext type, room type, device type, and member type. `Operations of AVContext Type`: StartContext/StopContext. `Operations of Room Type`: EnterRoom/ExitRoom. `Operations of Device Type`: Turn on/off a certain device. `Operations of Member Type`: Request the screen/cancel the screen." | Perform the next operation after the previous operation has been completed.
| AV_ERR_EXCLUSIVE_OPERATION | 1002 | Exclusive operation | This error occurs while performing a certain operation if the same type of other operation is already in process. This error occurs while performing the operation of exiting room if you are joining the room. | Perform the next operation after the previous operation has been completed.
| AV_ERR_HAS_IN_THE_STATE | 1003 | Already in the status | This error occurs while performing the operation that allows an object to join a certain status if the object is already in this status. This error occurs while performing the operation of joining room if you are already in the room. | Since you are already in the desired status, this operation can be considered to be successful and treated as a success.
| AV_ERR_INVALID_ARGUMENT | 1004 | Error parameter | This error occurs while passing a wrong parameter if you are calling SDK API. This error occurs if the passed room type is not AVRoom::ROOM_TYPE_PAIR or AVRoom::ROOM_TYPE_MULTI when you are joining the room. | Read the API documentation carefully, make clear of the valid value range of each parameter for each API, determine which parameters are not specified as required, ensure the correctness of passed parameters, and perform corresponding preventive measures.
| AV_ERR_TIMEOUT | 1005 | Timeout | This error occurs if the operation result has not been returned within a specific period of time. In most cases, this error tends to occur in scenarios where signaling transmission is involved and network problem occurs. This error occurs if you have not joined the room in 30 seconds after performing the operation of joining room. | Check whether a network problem occurred, and try again.
| AV_ERR_NOT_IMPLEMENTED | 1006 | Not implement | This error occurs while calling SDK API if the corresponding feature is not yet supported. | This feature is not supported currently, so please find an alternative solution.
| AV_ERR_NOT_IN_MAIN_THREAD | 1007 | Not in main thread | The external SDK API is required to be called in the main thread. This error occurs while calling SDK API at business end but not in the main thread. | Modify the business logic to ensure SDK API is called in the main thread.
| AV_ERR_RESOURCE_IS_OCCUPIED | 1008 | Resources are occupied | This error occurs if certain resources such as camera and screen have been occupied when needed. | Determine which resources are used and occupied by whom, to make sure that the SDK-related features are used at the right time and no conflict occurs when resources are used.
| AV_ERR_CONTEXT_NOT_EXIST | 1101 | AVContext object is not in CONTEXT_STATE_STARTED status | This error occurs while calling the API which is only allowed to be called in CONTEXT_STATE_STARTED status if AVContext object is not in such status. | Modify the business logic to ensure that SDK API is called at a right time.
| AV_ERR_CONTEXT_NOT_STOPPED | 1102 | AVContext object is not in CONTEXT_STATE_STOPPED status | This error occurs while calling the API which is only allowed to be called in CONTEXT_STATE_STOPPED status if AVContext object is not in such status. If the object is not in such status, This error occurs while calling AVContext::DestroyContext. | Modify the business logic to ensure that SDK API is called at a right time.
| AV_ERR_ROOM_NOT_EXIST | 1201 | AVRoom object is not in ROOM_STATE_ENTERED status | This error occurs while calling the API which is only allowed to be called in ROOM_STATE_ENTERED status if AVRoom object is not in such status. | Modify the business logic to ensure that SDK API is called at a right time.
| AV_ERR_ROOM_NOT_EXITED | 1202 | AVRoom object is not in ROOM_STATE_EXITED status | This error occurs while calling the API which is only allowed to be called in ROOM_STATE_EXITED status if AVRoom object is not in such status. If the object is not in such status, This error occurs while calling AVContext::StopContext. | Modify the business logic to ensure that SDK API is called at a right time.
| AV_ERR_DEVICE_NOT_EXIST | 1301 | Device does not exist | This error occurs while using a device that does not exist or has not been initialized. | Check whether the device exists, make sure that device ID is entered correctly, and ensure that the device is used after it is successfully initialized.
| AV_ERR_ENDPOINT_NOT_EXIST | 1401 | AVEndpoint object does not exist | This error occurs while obtaining the AVEndpoing object of an audio or video which is not sent by any member. | Modify the business logic to ensure that SDK API is called at a right time.
| AV_ERR_ENDPOINT_HAS_NOT_VIDEO| 1402 | Member does not send a video| This error occurs while performing the operation that requires a member to send a video if he or she is not sending any videos. This error occurs while requesting a member's screen if he or she is not sending any videos. | Modify the business logic to ensure that SDK API is called at a right time.
| AV_ERR_TINYID_TO_OPENID_FAILED | 1501 | Failed to transfer Tinyid to identifier | You need to transfer tinyid to identifier when receiving the signaling of information update of a member. This error occurs if problems exist in IMSDK-related logic and the network. | Check whether a network problem occurs, and view the log to confirm whether problems exist in IMSDK-related logic.
| AV_ERR_OPENID_TO_TINYID_FAILED | 1502 | Failed to transfer identifier to tinyid | You need to transfer identifier to tinyid when calling the API StartContext. This error occurs if problems exist in IMSDK-related logic and the network or you have not logged in. | Check whether a network problem occurs, view the log to confirm whether problems exist in IMSDK-related logic, and determine whether you have called IMSDK's login API successfully.
| AV_ERR_DEVICE_TEST_NOT_EXIST | 1601 | AVDeviceTest object is not in DEVICE_TEST_status_STARTED status (Windows-specific) | This error occurs while calling the API which is only allowed to be called in DEVICE_TEST_status_STARTED status if AVDeviceTest object is not in such status. | Modify the business logic to ensure that SDK API is called at a right time.
| AV_ERR_DEVICE_TEST_NOT_STOPPED | 1602 | AVDeviceTest object is not in DEVICE_TEST_STATE_STOPPED status (Windows-specific) | This error occurs while calling the API which is only allowed to be called in DEVICE_TEST_STATE_STOPPED status if AVDeviceTest object is not in such status. If the object is not in such status, This error occurs while calling AVContext::StopContext. | Modify the business logic to ensure that SDK API is called at a right time.
| AV_ERR_INVITE_FAILED | 1801 | Failed to send invitation | A failure occurred while sending an invitation. | The invitation module is only used in DEMO. Currently, the invitation feature is not supported externally, so this error can be ignored at business end.
| AV_ERR_ACCEPT_FAILED | 1802 | Failed to accept invitation | A failure occurred while accepting an invitation. | The invitation module is only used in DEMO. Currently, the invitation feature is not supported externally, so this error can be ignored at business end.
| AV_ERR_REFUSE_FAILED | 1803 | Failed to refuse invitation | A failure occurred while refusing an invitation. | The invitation module is only used in DEMO. Currently, the invitation feature is not supported externally, so this error can be ignored at business end.

## AVSDK Service Side Error
| Error Code Name | Error Code Value | Description | Reason | Solution
|---------|---------|---------|---------|---------|
| AV_ERR_SERVER_FAILED | 10001 | General error | Find the specific reason by analyzing the log to confirm the error code returned to the client by the backend. | Analyze the log to obtain the error code returned to the client by the backend, and contact the colleague at the backend to help solve the problem.
| AV_ERR_SERVER_INVALID_ARGUMENT | 10002 | Error parameter | A wrong parameter is passed when calling SDK API or sending signaling to the backend within SDK. Find the specific reason by analyzing the log to confirm the error code returned to the client by the backend. | Make sure to pass right parameters when calling SDK API. Analyze the log to obtain the error code returned to the client by the backend, and contact the colleague at the backend to help solve the problem.
| AV_ERR_SERVER_NO_PERMISSION | 10003 | No permission | You have no permission to use a certain feature. Find the specific reason by analyzing the log to confirm the error code returned to the client by the backend. This error occurs if the signature is incorrect or expired when joining the room. | Make sure to configure the correct permission parameters before using the corresponding feature. Analyze the log to obtain the error code returned to the client by the backend, and contact the colleague at the backend to help solve the problem.
| AV_ERR_SERVER_TIMEOUT | 10004 | Timeout | Find the specific reason by analyzing the log to confirm the error code returned to the client by the backend. | Analyze the log to obtain the error code returned to the client by the backend, and contact the colleague at the backend to help solve the problem.
| AV_ERR_SERVER_ALLOC_RESOURCE_FAILED | 10005 | Insufficient resources | This error occurs if you fail to allocate more resources (such as memory) or the resource volume exceed the limit (for example, beyond the maximum number of room members) when performing certain operations. Find the specific reason by analyzing the log to confirm the error code returned to the client by the backend. | Analyze the log to obtain the error code returned to the client by the backend, and contact the colleague at the backend to help solve the problem.
| AV_ERR_SERVER_ID_NOT_IN_ROOM | 10006 | Not in the room | This error occurs while performing certain operations if you are not in the room. Find the specific reason by analyzing the log to confirm the error code returned to the client by the backend. | Analyze the log to obtain the error code returned to the client by the backend, and contact the colleague at the backend to help solve the problem.
| AV_ERR_SERVER_NOT_IMPLEMENT | 10007 | Not implement | This error occurs while calling SDK API if the corresponding feature is not yet supported. | This feature is not supported currently, so please find an alternative solution.
| AV_ERR_SERVER_REPEATED_OPERATION | 10008 | Repetitive operation | Find the specific reason by analyzing the log to confirm the error code returned to the client by the backend. | Analyze the log to obtain the error code returned to the client by the backend, and contact the colleague at the backend to help solve the problem.
| AV_ERR_SERVER_ID_NOT_IN_ROOM| 10009| Room does not exist | This error occurs while performing certain operations if the room does not exist. | Analyze the log to obtain the error code returned to the client by the backend, and contact the colleague at the backend to help solve the problem.
| AV_ERR_SERVER_ENDPOINT_NOT_EXIST | 10010 | Member does not exist | This error occurs while performing the corresponding operations of a member when he or she does not exist. | Analyze the log to obtain the error code returned to the client by the backend, and contact the colleague at the backend to help solve the problem.
| AV_ERR_SERVER_INVALID_ABILITY| 10011 | Invalid capability | Find the specific reason by analyzing the log to confirm the error code returned to the client by the backend. | Analyze the log to obtain the error code returned to the client by the backend, and contact the colleague at the backend to help solve the problem.


## Recording Error Codes
| Error Code Name | Error Description | Solution |
|---------|---------|---------|
| 30000000 | Failed to resolve SDK request | "Check whether the recording request fields are complete"
| 30000001 | Failed to resolve SDK request - Recording request packet is missing | "Check whether the recording request fields are complete"
| 30000002 | Failed to resolve SDK request - Filename field for recorded file is missing | "Check whether the recording request fields are complete"
| 30000003 | Failed to resolve SDK request - Recording request operation field is missing | "Check whether the recording request fields are complete"
| 30000004 | Failed to resolve SDK request - Incorrect video source type (such as camera, desktop) | "Check whether the recording request fields are complete"
| 30000201 | An error occurred while requesting server for internal data packing | "Report to Tencent customer service"
| 30000202 | An error occurred while requesting server for internal data packing | "Report to Tencent customer service"
| 30000203 | An error occurred while requesting server for internal data packing | "Report to Tencent customer service"
| 30000207 | A communication error occurred while requesting recording server - Failed to fetch the address of recording server | "Report to Tencent customer service"
| 30000208 | A communication error occurred while requesting recording server - Timeout of request for recording server | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service"
| 30000301 | An error occurred while resolving the response packet from recording server - Failed to resolve the data packet | "Report to Tencent customer service"
| 30000302 | An error occurred while resolving the response packet from recording server - Failed to resolve the data packet | "Report to Tencent customer service"
| 30000303 | An error occurred while resolving the response packet from recording server - No IP is returned | "Report to Tencent Cloud customer service"
| 30000304 | An error occurred while resolving the response packet from recording server - No port is returned | "Report to Tencent Cloud customer service"
| 30000305 | An error occurred while resolving the response packet from recording server - No result is returned | "Report to Tencent customer service"
| 30000401 | An error occurred while obtaining the grocery service IP by querying room | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service"
| 30000402 | An error occurred while fetching grocery data by querying room | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service"
| 30000403 | grocery does not exist (room does not exist) and cannot be fetched by querying room | "Check whether the room has been activated successfully, and whether the user ID and groupid are correctly entered"
| 30000404 | Timeout while querying room stream-control server | "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service"
| 30000405 | An error occurred with the response packet while querying room - Failed to resolve the data packet | "Report to Tencent customer service"
| 30000406 | An error occurred with the response packet while querying room - Failed to resolve the data packet | "Report to Tencent customer service"
| 30000407 | An error occurred with the response packet while querying room - Failed to resolve the data packet | "Report to Tencent customer service"
| 30000408 | An error occurred with the response packet while querying room - No result is returned | "Report to Tencent customer service" |
| 30000409 | An error occurred with the response packet while querying room - Failed to resolve the data packet | "Report to Tencent customer service"
| 30000410 | Recording room does not exist | "Check whether the room has been activated successfully, whether the user ID and groupid for recording are correctly entered, or whether the user has exited the room"
| 30000411 | Recording room or the initiator of recording does not exist | "Check whether the room has been activated successfully, whether the user ID and groupid for recording are correctly entered, or whether the user has exited the room"
| 30000412 | Request for ending recording has been sent more than once. The user has ended recording	| "This indicates recording has ended. Check if the request for ending recording has been sent more than once. No action is needed for this."
| 30000413 | Request for ending recording has been sent more than once. The user has ended recording	| "This indicates recording has ended. Check if the request for ending recording has been sent more than once. No action is needed for this."
| 30000414 | An error occurred with internal server operation type while querying room | "Report to Tencent customer service"
| 30000415 | Request for starting recording has been sent more than once and recording has started; or the initiator of recording does not exist | "Check whether the room has been activated successfully, and whether the user ID and groupid for recording are correctly entered" |


## Non-interactive Broadcasting Error Codes
| Error Code Name | Error Description | Solution |
|---------|---------|---------|
| 40000000	| Failed to resolve SDK request	| "Check whether the push request fields are complete"
| 40000001	| Failed to resolve SDK request - The push request packet is missing	| "Check whether the push request fields are complete"
| 40000002	| Failed to resolve SDK request - The operation field of push request is missing	| "Check whether the push request fields are complete"
| 40000003	| Failed to resolve SDK request - The output coding (HLS/RTMP, etc.) of push request is missing	| "Check whether the push request fields are complete"
| 40000004	| Failed to resolve SDK request - The video source type is incorrect (camera/desktop, etc.)	| "Check whether the push request fields are complete"
| 40000005	| Failed to resolve SDK request - Incorrect request operation (request for push, stop push)	| "Check whether the push request fields are complete"
| 40000006	| User ID is incorrect when you send request for push	| "Check whether the push request fields are correct"
| 40000007	| Push room ID is 0	| "Check whether the push room ID is correct"
| 40000201	| An error occurred while requesting server for internal data packing	| "Report to Tencent customer service"
| 40000202	| An error occurred while requesting server for internal data packing	| "Report to Tencent customer service"
| 40000203	| An error occurred while requesting server for internal data packing	| "Report to Tencent customer service"
| 40000207	| A communication error occurred while requesting pushing server - Failed to fetch the address of pushing server	| "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service"
| 40000208	| A communication error occurred while requesting pushing server - Timeout of request for pushing server	| "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service"
| 40000301	| An error occurred while resolving the response packet from push server - Failed to resolve the data packet	| "Report to Tencent customer service"
| 40000302	| An error occurred while resolving the response packet from push server - Failed to resolve the data packet	| "Report to Tencent customer service"
| 40000303	| An error occurred while resolving the response packet from push server - No IP is returned	| "Report to Tencent customer service"
| 40000304	| An error occurred while resolving the response packet from push server - No port is returned	| "Report to Tencent customer service"
| 40000305	| An error occurred while resolving the response packet from push server - No result is returned	| "Report to Tencent customer service"
| 40000306	| An error occurred while resolving the response packet from push server - Overflow of length of returned URL	| "Report to Tencent customer service"
| 40000401	| An error occurred while obtaining the grocery service IP by querying room	| "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service"
| 40000402	| An error occurred while fetching grocery data by querying room	| "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service"
| 40000403	| grocery does not exist and cannot be fetched by querying room (the room requesting push does not exist)	| "Check whether the room has been activated successfully, and whether the user ID and groupid for the push are entered correctly"
| 40000404	| Timeout while querying room stream-control server	| "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service"
| 40000405	| An error occurred with the response packet while querying room - Failed to resolve the data packet	| "Report to Tencent customer service"
| 40000406	| An error occurred with the response packet while querying room - Failed to resolve the data packet	| "Report to Tencent customer service"
| 40000407	| An error occurred with the response packet while querying room - Failed to resolve the data packet	| "Report to Tencent customer service"
| 40000408	| An error occurred with the response packet while querying room - No result is returned	| "Report to Tencent customer service"
| 40000409	| An error occurred with the response packet while querying room - Failed to resolve the data packet	| "Report to Tencent customer service"
| 40000410	| The room requesting the push does not exist	| "Check whether the room has been activated successfully, and whether the user ID and groupid for the push are entered correctly, or whether the user has exited the room"
| 40000411	| The user who initiates the push does not exist in the room	| "Check whether the room has been activated successfully, and whether the user ID and groupid for the push are entered correctly, or whether the user has exited the room"
| 40000412	| Request for ending push has been sent more than once and the user has ended push	| "This indicates that push has ended. No action is needed for this"
| 40000413	| Request for ending push has been sent more than once and the user has ended push	| "This indicates that push has ended. No action is needed for this"
| 40000414	| An error occurred with internal server operation type while querying room	| "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service"
| 40000415	| Request for starting push has been sent more than once and the user is pushing stream	| "This indicates that push is already in progress. No action is needed for this"
| 40000500	| Control the frequency of starting push	| "Unexceptional. Error is returned if a user send push request repeatedly within 3 seconds. The request should be retried after 3 seconds upon initiation of the last request"
| 1001	| Permission error	| "It is generally caused by wrong input of sdkappid"
| 20101	| The number of channels exceeds the limit	| "The number of push channels is limited. Check and delete unnecessary channels in the push console"
| 20406	| Account overdraft	| "Check whether the account is in arrears"
| 50002	| Incorrect input parameters | Check whether user ID and sdkappid are entered correctly
| 50003	| Pull URL is not fetched at the backend	| "Report to Tencent customer service"
| 50004	| Push type of push request is incorrect	| Check whether the push type field is entered correctly
| 50005	| Backend console connection timeout	| "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service"
| 50006	| Backend console connection timeout	| "This may be caused by network problem, please try again. If the problem persists, report to Tencent customer service"
| 50007	| The parameter returned from the backend is null	| "Report to Tencent customer service"

