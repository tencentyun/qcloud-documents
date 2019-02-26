
## Categorization of Error Codes
The error codes listed here can be categorized into **Access Layer Error Codes** and **Video Cloud Error Codes**. The access layer error codes are uniformly defined across the Tencent Cloud access layer, and the video cloud error codes are only needed in LVB and VOD services.

For more information on how to distinguish between the two types of error codes and how they work, please see [Dual Error Codes](https://cloud.tencent.com/doc/api/258/5820#.E5.8F.8C.E9.94.99.E8.AF.AF.E7.A0.81).

## Access Layer Error Codes

| Error Code | Message | Description |
|---------|---------|---------|
|  4000 | Invalid request parameter | Required parameters are missing, or the format of parameter values is incorrect. For error message, please see the "message" field in error description. |
 |  4100 | Authentication failed | Signature authentication failed. For more information, please see the "Authentication" section in the document. |
 |  4200 | Request expired | The request has expired. For more information, please see the "Request Validity" section in the document. |
 |  4300 | Access denied | The account is blocked or not within the user range of the API. |
 |  4400 | Quota exceeded | The number of requests exceeded the quota limit. For more information, please see the "Request Quota" section in the document. |
 |  4500 | Replay attack | The Nonce and Timestamp parameters ensure that each request is executed only once on the server. Therefore, the Nonce value cannot be the same as the last one, and the difference between Timestamp and Tencent server time cannot be greater than 2 hours. |
 |  4600 | Unsupported protocol | The protocol is not supported. For more information, please see the relevant document. |
 |  5000 | Resource does not exist | The instance corresponding to the resource ID does not exist, or the instance has been returned, or another user's resource is accessed. |
 |  5100 | Resource operation failed | A failure message is returned from the function layer. For error message, please see the "message" field in error description. |
 |  5200 | Failed to purchase the resource | The resource purchase failed. This may be caused unsupported instance configuration or insufficient resources. |
 |  5300 | Failed to purchase the resource | The resource purchase failed because of insufficient balance. |
 |  5400 | Part of operations performed successfully | The batch operation was successful on some resources. For more information, please see the returned value of the method. |
 |  5500 | User failed to pass identity verification | The resource purchase failed because the user failed to pass identity verification. |
 |  6000 | Internal error with the server | An internal error occurred with the server. Try again later or contact customer service. |
 |  6100 | Not supported in the version | This API is not supported in this version or is under maintenance. Note: When this error occurs, check whether the domain name for the API is correct. Domain name may vary with different modules. |
 |  6200 | API is unavailable | The API is under maintenance and is unavailable. Try again later. |
 
## Video Cloud Error Codes
 
 | Error Code | Message |
 |----------|------------|
 | 1000	  | Incorrect input parameter |		
 | 1001	  | An error occurred while obtaining the user account |	
 | 1002	  | The user does not exist |	
 | 1003	  | Incorrect user account ID |	
 | 3000	  | Network error |	
 | 4001   | Incorrect JSON format |	
 | 20100 | An error occurred while creating a channel |	
 | 20101 | Number of channels exceeds the limit |	
 | 20102 | An error occurred while obtaining the channel information |	
 | 20103 | An error occurred while modifying the channel information |	
 | 20104 | An error occurred while obtaining the channel list |	
 | 20105 | An error occurred while deleting a channel |	
 | 20106 | An error occurred while disabling a channel |	
 | 20107 | An error occurred while enabling a channel |	
 | 20108 | Channel is not in an editable status |	
 | 20109 | Channel is not in disabled status |	
 | 20111 | No LVB source is found for the channel |	
 | 20112 | Incorrect LVB source protocol |	
 | 20113 | Incorrect receiver protocol |	
 | 20114 | Failed to activate the service |	
 | 20200 | Pull URL is empty |	
 | 20201 | An error occurred while obtaining the LVB source information |	
 | 20202 | An error occurred while creating a LVB source |	
 | 20203 | An error occurred while deleting a LVB source |	
 | 20204 | Pull URL is empty |	
 | 20250 | Blacklist and whitelist are empty |	
 | 20251 | Blacklist and whitelist do not exist |	
 | 20252 | An error occurred while obtaining the blacklist and whitelist |	
 | 20253 | Number of name lists exceeds the limit |	
 | 20300 | An error occurred while modifying channel status |	
 | 20301 | Channel does not exist |	
 | 20320 | Failed to create recording task |	
 | 20321 | Failed to obtain the list of recording tasks |	
 | 20322 | Time conflict between recording tasks |	
 | 20323 | The start time and end time of the recording task are invalid |	
 | 20326 | Failed to modify recording task |	
 | 20327 | The recording task does not exist |	
 | 20328 | Screencap task does not exist |	
 | 20500 | Watermark does not exist |	

