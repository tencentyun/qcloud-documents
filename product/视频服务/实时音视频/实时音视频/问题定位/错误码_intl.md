### iLiveSDK error codes
| Constant Definition               | Error Code | Error Description                                             |
| ---------------------- | ------ | ---------------------------------------------------- |
| NO_ERR                 | 0      | Success                                                 |
| ERR_IM_NOT_READY       | 8001   | IM module not ready or not loaded                                        |
| ERR_AV_NOT_READY       | 8002   | AV module not ready or not loaded                                 |
| ERR_NO_ROOM            | 8003   | No valid room                                         |
| ERR_ALREADY_EXIST      | 8004   | Target already exists                                           |
| ERR_NULL_POINTER       | 8005   | Null pointer error                                           |
| ERR_ENTER_AV_ROOM_FAIL | 8006   | Failed to enter the AV room                                       |
| ERR_USER_CANCEL        | 8007   | Operation is canceled by user                                             |
| ERR_WRONG_STATE        | 8008   | Exceptional status (This is deprecated and is only returned when CallSDK call status switching failed) |
| ERR_NOT_LOGIN          | 8009   | Not logged in                                               |
| ERR_ALREADY_IN_ROOM    | 8010   | Already in the room                                           |
| ERR_BUSY_HERE          | 8011   | Busy now (Previous request is not completed)                               |
| ERR_NET_UNDEFINE       | 8012   | Network is unrecognized or unreachable                               |
| ERR_SDK_FAILED         | 8020   | iLiveSDK processing failed (General)                               |
| ERR_INVALID_PARAM      | 8021   | Invalid parameter passed by API (For example, "option" passed by the API for creating a room or entering a room is null)     |
| ERR_NOT_FOUND          | 8022   | Target not found                                         |
| ERR_NOT_SUPPORT        | 8023   | Request not supported                                           |
| ERR_ALREADY_STATE      | 8024   | Already in this state (Usually caused by repeated call)                       |
| ERR_KICK_OUT           | 8050   | Kicked offline                                             |
| ERR_EXPIRE             | 8051   | Ticket expired (Need to update ticket userSig)                          |
| ERR_PARSE_FAIL         | 8052   | Failed to parse network request                                      |
| ERR_ALLOC_FAIL         | 8053   | Memory allocation failed. Check whether memory is sufficient                       |


### AVSDK module error codes
| Error Code Name                          | Error Code | Description                                                         | Reason                                                         |
| ----------------------------------- | ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| AV_ERR_FAILED                       | 1      | General error                                                     | The reason can be located through log analysis                             |
| AV_ERR_REPEATED_OPERATION           | 1001   | Repeated operation                                                     | This operation is already in process                       |
| AV_ERR_EXCLUSIVE_OPERATION          | 1002   | Exclusive operation                                                     | Previous operation is not completed yet                                         |
| AV_ERR_HAS_IN_THE_STATE             | 1003   | Already in the desired status                                               | The object is already in the desired status                               |
| AV_ERR_INVALID_ARGUMENT             | 1004   | Wrong parameter                                                     | Wrong parameter passed                                               |
| AV_ERR_TIMEOUT                      | 1005   | Timeout                                                         | The operation result has not been returned within a specific period of time                             |
| AV_ERR_NOT_IMPLEMENTED              | 1006   | Not implemented                                                       | The feature is not supported yet                                           |
| AV_ERR_NOT_IN_MAIN_THREAD           | 1007   | Not in the main thread                                                   | The external SDK API is required to be called in the main thread                                   |
| AV_ERR_RESOURCE_IS_OCCUPIED         | 1008   | Resource is occupied                                                   | The resource needed is occupied                                     |
| AV_ERR_CONTEXT_NOT_EXIST            | 1101   | AVContext object is not in CONTEXT_STATE_STARTED status                 | This error occurs while calling an API that can be called only if the AVContext object is in CONTEXT_STATE_STARTED status when the object is not in such status. |
| AV_ERR_CONTEXT_NOT_STOPPED          | 1102   | AVContext object is not in CONTEXT_STATE_STOPPED status                 | This error occurs while calling an API that can be called only if the AVContext object is in CONTEXT_STATE_STOPPED status when the object is not in such status. If the object is not in such status, this error occurs while calling AVContext::DestroyContext. |
| AV_ERR_ROOM_NOT_EXIST                | 1201   | AVRoom object is not in ROOM_STATE_ENTERED status                       | This error occurs while calling an API that can be called only if the AVRoom object is in ROOM_STATE_ENTERED status when the object is not in such status. |
| AV_ERR_ROOM_NOT_EXITED              | 1202   | AVRoom object is not in ROOM_STATE_EXITED status                        | This error occurs while calling an API that can be called only if the AVRoom object is in ROOM_STATE_EXITED status when the object is not in such status. If the object is not in such status, this error occurs while calling AVContext::StopContext. |
| AV_ERR_DEVICE_NOT_EXIST             | 1301   | Device does not exist                                                   | This error occurs while using a device that does not exist or has not been initialized. |
| AV_ERR_ENDPOINT_NOT_EXIST           | 1401   | AVEndpoint object does not exist                                         | This error occurs while obtaining the AVEndpoint object of a member when the member is not sending any audio or video. |
| AV_ERR_ENDPOINT_HAS_NOT_VIDEO       | 1402   | No video sent                                                   | This error occurs while performing an operation that requires a member to send a video when the member is not sending any videos. For example, this error occurs while requesting a member's screen if he or she is not sending any videos. |
| AV_ERR_TINYID_TO_OPENID_FAILED      | 1501   | Failed to transfer tinyid to identifier                                       | You need to transfer tinyid to identifier when receiving the signaling of information update of a member. This error occurs in case of IMSDK-related logic problem or network problem. |
| AV_ERR_OPENID_TO_TINYID_FAILED      | 1502   | Failed to transfer identifier to tinyid                                      | You need to transfer identifier to tinyid when calling the API StartContext. This error occurs in case of IMSDK-related logic problem or network problem or if the user has not logged in. |
| AV_ERR_DEVICE_TEST_NOT_EXIST        | 1601   | AVDeviceTest object is not in DEVICE_TEST_STATE_STARTED status (Windows-specific) | This error occurs while calling an API that can be called only if the AVDeviceTest object is in DEVICE_TEST_STATE_STARTED status when the object is not in such status. |
| AV_ERR_DEVICE_TEST_NOT_STOPPED      | 1602   | AVDeviceTest object is not in DEVICE_TEST_STATE_STOPPED status (Windows-specific) | This error occurs while calling an API that can be called only if the AVDeviceTest object is in DEVICE_TEST_STATE_STOPPED status when the object is not in such status. If the object is not in such status, this error occurs while calling AVContext::StopContext. |
| AV_ERR_INVITE_FAILED                | 1801   | Sending failure                                                     | A failure occurred while sending an invitation                                         |
| AV_ERR_ACCEPT_FAILED                | 1802  | Accepting failure                                                      | A failure occurred while accepting an invitation                                         |
| AV_ERR_REFUSE_FAILED                | 1803   | Refusing failure                                                     | A failure occurred while refusing an invitation                                         |
| AV_ERR_IMSDK_FAIL                   | 6999   | IMSDK callback notification failure                                            | The reason can be located through log analysis                                   |
| AV_ERR_IMSDK_TIMEOUT                 | 7000   | IMSDK callback notification timeout                                        | The reason can be located through log analysis                                   |
| AV_ERR_SERVER_FAILED                | 10001  | General error                                                     | The reason can be located through log analysis                                 |
| AV_ERR_SERVER_INVALID_ARGUMENT      | 10002   | Wrong parameter                                                     | Wrong parameter                                                   |
| AV_ERR_SERVER_NO_PERMISSION         | 10003  | No permission                                                     | No permission to use the feature                                         |
| AV_ERR_SERVER_TIMEOUT               | 10004  | Failed to request the room address                                       | The reason can be located through log analysis                                 |
| AV_ERR_SERVER_ALLOC_RESOURCE_FAILED | 10005  | Failed to connect to the room                                           | The reason can be located through log analysis                                 |
| AV_ERR_SERVER_ID_NOT_IN_ROOM        | 10006  | Not in the room                                                     | You are performing an operation related to a room that you are not in                               |
| AV_ERR_SERVER_NOT_IMPLEMENT          | 10007  | Not implemented                                                       | The feature corresponding to the called SDK API is not supported yet                        |
| AV_ERR_SERVER_REPEATED_OPERATION    | 10008  | Repeated operation                                                     | The reason can be located through log analysis                                 |
| AV_ERR_SERVER_ROOM_NOT_EXIST        | 10009  | Room does not exist                                                   | You are performing an operation related to a room that does not exist                                 |
| AV_ERR_SERVER_ENDPOINT_NOT_EXIST    | 10010  | Member does not exist                                                   | You are performing an operation related to a member that does not exist                     |
| AV_ERR_SERVER_INVALID_ABILITY       | 10011  | Invalid capability                                                     | The reason can be located through log analysis                                 |
