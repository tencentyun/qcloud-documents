
## Categorization of Error Codes
The error codes listed here can be categorized into **Access Layer Error Codes** and **Video Cloud Error Codes**. The access layer error codes are uniformly defined across the Tencent Cloud access layer, and the video cloud error codes are only needed in LVB and VOD services.

For more information on how to distinguish between the two types of error codes and how they work, please see [Dual Error Codes](https://cloud.tencent.com/doc/api/258/5820#.E5.8F.8C.E9.94.99.E8.AF.AF.E7.A0.81).

## Access Layer Error Codes

| Error Code | Message | Description |
|---------|---------|---------|
|  4000 | Invalid request parameter | Required parameters are missing, or the format of parameter values is incorrect. For more information on the error message, please see the message field in error description. |
 |  4100 | Authentication failed      | Signature authentication failed. For more information, please see Authentication section in the document. |
 |  4200 | Request expired      | Request has expired. For more information, please see Request Validity section in the document. |
 |  4300 | Access denied      | An account is disabled or is not within the user range for the API. |
 |  4400 | Quota exceeded      | The number of requests has exceeded the quota limit. For more information, please see Request Quota section in the document. |
 |  4500 | Replay attack      | The Nonce and Timestamp parameters of request can ensure that each request is executed only once on the server. Therefore, the Nonce should not be identical to the previous one. The time difference between the Timestamp and Tencent CVM should not be greater than 2 hours. |
 |  4600 | Unsupported protocol    | Protocol is not supported. For more information, please see the document. |
 |  5000 | Resource does not exist    | The instance that the resource ID indicates does not exist, or the instance has been returned, or another user's resource is accessed. |
 |  5100 | Resource operation failed  | The failure message is returned from the Function layer. For more information on the error message, please see the message field in error description.  |
 |  5200 | Failed to purchase resource | Failed to purchase resource. This may be caused unsupported instance configuration, or insufficient resources. |
 |  5300 | Failed to purchase resource | Failed to purchase resource because of insufficient balance.  |
 |  5400 | Part of operations performed successfully | Part of batch operations have been performed successfully. For more information, please see the returned value of method. |
 |  5500 | User failed to pass qualification verification | Failed to purchase resource, because user failed to pass the qualification verification. |
 |  6000 | Internal error on the server | An internal error occurred on the server. Try again later or contact customer service personnel for help. |
 |  6100 | Not supported by the version | The API is not supported by this version or is being maintained. Note: When this error occurs, first check whether the domain name of the API is correct. Different modules may have different domain names. |
 |  6200 |  API is unavailable temporarily | The API is being maintained. Try again later. |
 
 ## Video Cloud Error Codes
 
 | Error Code | Message |
 |----------|------------|
 | 1000	  |  Incorrect input parameter |		
 | 1001	  |  An error occurred while obtaining the user account  |	
 | 1002	  |  User does not exist. |	
 | 1003	  |  Incorrect account ID |	
 | 3000	  |  Network error |	
 | 4001   |  Incorrect JSON format |	
 | 20100 |	An error occurred while creating a channel |	
 | 20101 |	Number of channels exceeds the upper limit |	
 | 20102 |	An error occurred while obtaining channel information |	
 | 20103 |	An error occurred while modifying channel information |	
 | 20104 |	An error occurred while obtaining channel list |	
 | 20105 |	An error occurred while deleting a channel |	
 | 20106 |	An error occurred while disabling a channel |	
 | 20107 |	An error occurred while enabling a channel |	
 | 20108 |	Channel is not in an editable status |	
 | 20109 |	Channel is not in disabled status |	
 | 20111 |	No LVB source is found for the channel |	
 | 20112 |	Incorrect LVB source protocol |	
 | 20113 |	Incorrect receiver protocol |	
 | 20114 |	Failed to activate the service |	
 | 20200 |	Pulling address is empty |	
 | 20201 |	An error occurred while obtaining the LVB source information |	
 | 20202 |	An error occurred while creating a LVB source |	
 | 20203 |	An error occurred while deleting a LVB source |	
 | 20204 |	Pulling address is empty |	
 | 20250 |	Blacklist and whitelist are empty |	
 | 20251 |	Blacklist and whitelist do not exist |	
 | 20252 |	An error occurred while obtaining the blacklist and whitelist |	
 | 20253 |	Number of name lists exceeds upper limit |	
 | 20300 |	An error occurred while modifying channel status |	
 | 20301 |	Channel does not exist |	
 | 20320 |	Failed to create recording task |	
 | 20321 |	Failed to obtain the list of recording tasks |	
 | 20322 |	Time conflict between recording tasks |	
 | 20323 |	The start time and end time of the recording task are invalid |	
 | 20326 |	Failed to modify recording task |	
 | 20327 |	Recording task does not exist |	
 | 20328 |	Screenshot task does not exist |	
 | 20500 |	Watermark does not exist |	

