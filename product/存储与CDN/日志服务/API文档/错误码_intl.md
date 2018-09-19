## Overview

This document describes the error codes and corresponding error messages returned when an error occurs with the request. You can identify the problem based on StatusCode and Body of HTTP. The format of Body is as follows:
```
{
    "errorcode" : <ErrorCode>,
    "errormessage" : <ErrorMessage>
}
```
## Error Codes

| HTTP Status Code | Error Code | Error Message |
| -------------------- | -------------------- | ------------------------------- |
| 400 | InvalidAuthorization | Invalid signature string format |
| 400 | InvalidCompressType | The specified x-cls-compress-type is not supported |
| 400 | InvalidContent | Message body error. Decompression or resolution failed |
| 400 | InvalidContentType | The specified Content-Type is not supported |
| 400 | InvalidParam | Required parameters are missing or some parameters are invalid |
| 400 | MissingAgentIp | x-cls-agent-ip is missing |
| 400 | MissingAgentVersion | x-cls-agent-version is missing |
| 400 | MissingAuthorization | Authorization is missing |
| 400 | MissingContent | Message body is empty |
| 400 | MissingContentType | Content-Type is missing |
| 400 | TopicClosed | Collection feature is disabled for the specified topic |
| 401 | Unauthorized | Authentication failed, possibly due to ID error, repeated use of signature, or signature computing error |
| 403 | LogsetExceed | Number of logsets exceeds the limit of 10 |
| 403 | LogSizeExceed | Size of the submitted log exceeds the limit of 5 MB |
| 403 | NotAllowed | Operation is not allowed |
| 403 | TopicExceed | Number of log topics exceeds the limit of 20 |
| 404 | IndexNotExist | The specified index rule does not exist |
| 404 | LogsetNotExist | The specified logset does not exist |
| 404 | MachineGroupNotExist | The specified server group does not exist |
| 404 | ShipperNotExist | The specified shipping rule does not exist |
| 404 | TopicNotExist | The specified log topic does not exist |
| 405 | NotSupported | Operation is not supported |
| 409 | IndexConflict | The index rule already exists |
| 409 | LogsetConflict | The logset already exists |
| 409 | MachineGroupConflict | The server group already exists |
| 409 | ShipperConflict | The shipping rule already exists |
| 409 | TopicConflict | The log topic already exists |
| 500 | InternalError | Internal error |

