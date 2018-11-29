## Error Codes
How to use error codes
```
//Get system-defined error codes
var errorCodeMap = WebRTCAPI.fn.getErrorCode();

//Error processing
function errorHandler(error){
    if( error.errorCode >= 70000){
        console.error('Account system error',error.errorMsg)
    }
    else if( error.errorCode === errorCodeMap.XXXXXXXX){
        console.error(error.errorMsg)
    }   
}

//Initialize
var RTC = new WebRTCAPI({ ... });
...
//Callback event
RTC.createRoom({...},function(info){
    console.info(info)
}, function(error){
    errorHandler(error);
});          
...               
//Listen for error event notification
RTC.onErrorNotify(function(error){
    errorHandler(error);
})
```
## Audio & Video

| Key                          | Error Code  | Error Type            | Description                                                          |
| ---------------------------- | ------ | ------------------ | ------------------------------------------------------------ |
| SUCC                         | 0      | Successful                | Successful                                                          |
| PARAM_MISSING                | 10001  | Parameter missing            | Indicates whether the parameter is complete                                              |
| INIT_WS_FAILED               | 10005  | WS initialization failed        | Websocket initialization failed                                           |
| ENTER_ROOM_ERROR             | 10006  | SDK error             | Failed to join the room                                                  |
| CREATE_PEERCONNECTION_FAILED | 10007  | SDK error             | Failed to create PeerConnection                                       |
| GET_USERMEDIA_FAILED         | 10008  | SDK error             | Failed to get the user's audio/video device                                       |
| GET_LOCALSDP_FAILED          | 10009  | SDK error             | Failed to get Local SDP                                             |
| ON_ICE_BROKEN                | 10014  | Connection error            | P2P disconnected                                                   |
| ON_ICE_CLOSE                 | 10015  | Connection error            | P2P connection closed                                                   |
| NOT_IN_WHITE_LIST            | 11000  | The SdkAppid is not in the whitelist  | Troubleshooting steps: Step 1: Check whether the SdkAppid is entered correctly (1400xxxxxx) Step 2: Check whether the TRTC service is activated. If not, you cannot use your SdkAppid.  |
| NOT_FOUND                    | 10031  | SDK error             | No user found                                            |
| NOT_INITED                   | 10032  | SDK error             | Not initialized                                                    |
| START_RTC_FAILED             | 10033  | SDK error             | Push failed                                                      |
| STOP_RTC_FAILED              | 10034  | SDK error             | Failed to stop push                                                  |
| WS_CLOSE                     | 10035  | Connection error            | Websocket closed                                                |
| WS_ERROR                     | 10036  | Connection error            | Websocket error                                                |
| UPDATE_VIDEO_SSRC_FAILED     | 10037  | SDK error             | Failed to update the video source                                                |
| UPDATE_AUDIO_SSRC_FAILED     | 10038  | SDK error             | Failed to update the audio source                                                |
| NOT_FOUND_PEER               | 10039  | SDK error             | No P2P connection found                                         |

## Account System

| Error Code  | Error Type  | Description                                                          |
| ------ | -------- | ------------------------------------------------------------ |
| 70001  | Account system  | UserSig has expired. Try to generate a new one. If it expires immediately after its generation, check if you've entered a short validity period or 0 |
| 70002  | Account system  | The UserSig length is 0. Confirm whether the signature calculation is correct.                      |
| 70003  | Account system  | UserSig verification failed. Confirm whether the sig content is truncated, for example, due to insufficient buffer length  |
| 70004  | Account system  | UserSig verification failed. Confirm whether the sig content is truncated, for example, due to insufficient buffer length  |
| 70005  | Account system  | UserSig verification failed. Use a tool to check whether the generated sig is correct            |
| 70006  | Account system  | UserSig verification failed. Use a tool to check whether the generated sig is correct            |
| 70007  | Account system  | UserSig verification failed. Use a tool to check whether the generated sig is correct            |
| 70008  | Account system  | UserSig verification failed. Use a tool to check whether the generated sig is correct            |
| 70009  | Account system  | Failed to verify sig with the business public key. Confirm whether the private key for the generated UserSig matches the SdkAppid  |
| 70010  | Account system  | UserSig verification failed. Use a tool to check whether the generated sig is correct            |
| 70013  | Account system  | The UserID in UserSig does not match that in the request. Check whether the UserID entered when you log in matches that in sig  |
| 70014  | Account system  | The SdkAppid in UserSig does not match that in the request. Check whether the SdkAppid entered when you log in matches that in sig  |
| 70015  | Account system  | No authentication method found for the appId and account type. Confirm whether the account integration is performed  |
| 70016  | Account system  | The length of the pulled public key is 0. Confirm whether the public key has been uploaded. Try again after 10 minutes if you upload a new public key  |
| 70017  | Account system  | Internal verification timed out for third-party tickets. Try again later. If you have tried repeated attempts without success, contact technical support  |
| 70018  | Account system  | Failed to verify third-party tickets internally                                        |
| 70019  | Account system  | The ticket field verified using https is empty. Enter a correct sig               |
| 70020  | Account system  | No SdkAppid found. Confirm whether it has been configured on Tencent Cloud                 |
| 70052  | Account system  | UserSig has expired. Generate a new one and try again                        |
| 70101  | Account system  | Request package information is empty                                                |
| 70102  | Account system  | Incorrect request package account type                                            |
| 70103  | Account system  | Incorrect phone number format                                              |
| 70104  | Account system  | Incorrect email format                                                  |
| 70105  | Account system  | Incorrect TLS account format                                              |
| 70106  | Account system  | Invalid account format type                                              |
| 70107  | Account system  | UserID does not exist                                               |
| 70113  | Account system  | Invalid batch quantity                                                |
| 70114  | Account system  | Restricted for security reasons                                                |
| 70115  | Account system  | The uin does not match the developer uin of the corresponding appId |
| 70140  | Account system  | SdkAppid does not match AccType                                    |
| 70145  | Account system  | Incorrect account type                                                  |
| 70169  | Account system  | Internal error. Try again later. If you have tried repeated attempts without success, contact technical support            |
| 70201  | Account system  | Internal error. Try again later. If you have tried repeated attempts without success, contact technical support            |
| 70202  | Account system  | Internal error. Try again later. If you have tried repeated attempts without success, contact technical support            |
| 70203  | Account system  | Internal error. Try again later. If you have tried repeated attempts without success, contact technical support            |
| 70204  | Account system  | appId does not have a corresponding  acctype                                     |
| 70205  | Account system  | Failed to find AccType. Try again later                                     |
| 70206  | Account system  | Invalid batch quantity in the request                                          |
| 70207  | Account system  | Internal error. Try again later                                              |
| 70208  | Account system  | Internal error. Try again later                                              |
| 70209  | Account system  | Failed to obtain the developer uin flag                                       |
| 70210  | Account system  | The uin does not match the developer uin in the request |
| 70211  | Account system  | Invalid uin in the request                                               |
| 70212  | Account system  | Internal error. Try again later. If you have tried repeated attempts without success, contact technical support            |
| 70213  | Account system  | Failed to access the internal data. Try again later. If you have tried repeated attempts without success, contact technical support    |
| 70214  | Account system  | Failed to verify internal tickets                                              |
| 70221  | Account system  | Invalid login. Use UserSig to authenticate again                         |
| 70222  | Account system  | Internal error. Try again later                                              |
| 70225  | Account system  | Internal error. Try again later. If you have tried repeated attempts without success, contact technical support            |
| 70231  | Account system  | Internal error. Try again later. If you have tried repeated attempts without success, contact technical support            |
| 70236  | Account system  | Failed to verify user signature                                      |
| 70308  | Account system  | Internal error. Try again later. If you have tried repeated attempts without success, contact technical support            |
| 70346  | Account system  | Failed to verify tickets                                                  |
| 70347  | Account system  | Failed to verify expired tickets                                        |
| 70348  | Account system  | Internal error. Try again later. If you have tried repeated attempts without success, contact technical support            |
| 70362  | Account system  | Internal timeout. Try again later. If you have tried repeated attempts without success, contact technical support            |
| 70401  | Account system  | Internal error. Try again later                                              |
| 70402  | Account system  | Invalid parameter. Check whether the required fields are entered, or whether the fields are entered as required in the protocol  |
| 70403  | Account system  | The operator is not an App admin and does not have permission to operate                         |
| 70050  | Account system  | Restricted due to too many failures and retries. Check whether the ticket is correct and try again after one minute.  |
| 70051  | Account system  | The account has been blacklisted. Contact technical support                            |

