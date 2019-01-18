List of client error codes:

| Value | Cause and solution |
|-|-|
| 0 | Successful call |
| 2 | Parameter error, for example, a single-character alias is bound, or the length of iOS token is not 64 characters |
| 20 | Authentication error. Incorrect configuration of access id or access key |
| 10000 | Starting error |
| 10001 | Error code of operation type, which may occur when the parameter is wrong |
| 10002 | Callback this error code if a registration request arrives when another registration operation is in progress. |
| 10003 | Permission mismatch or required permissions are missing. |
| 10004 | .so library is not imported correctly (For Androidstudio, you can add jniLibs named folder under the "main" directory to add 7 .so library folders under Other-Platform-SO of SDK documentation). |
| 10005 | The XGRemoteService node of AndroidManifest file is not configured or the name of the action package in the node is incorrectly configured. |
| 10100 | Current network is unavailable (switch the network and try again) |
| 10101 | Failed to create linkage (switch the network and try again) |
| 10102 | The linkage is actively closed during request processing (switch the network and try again) |
| 10103 | The server closes the link during request processing (switch the network and try again) |
| 10104 | An exception occurs on the client during request processing (switch the network and try again) |
| 10105 | Message sending or receiving timeout during request processing (switch the network and try again) |
| 10106 | Request for sending timeout during request processing (switch the network and try again) |
| 10107 | Request for receiving timeout during request processing (switch the network and try again) |
| 10108 | The server returns exceptional messages. |
| 10109 | Unknown exception. Switch the network or restart the device. |
| 10110 | The handler used to create the linkage is null. |
| Others | In case of other unknown errors, record the error and contact us. |

