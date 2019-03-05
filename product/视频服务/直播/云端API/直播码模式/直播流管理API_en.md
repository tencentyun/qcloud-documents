## Communicate with Tencent Cloud Backend
![](//mc.qcloudimg.com/static/img/bb38ba7d007910df41b2775a63c6e0d3/image.png)

Information synchronization between your server and Tencent Cloud's CVM can be implemented by combining the following two ways:
- **API call**: Tencent Cloud provides a set of LVB code management APIs for your backend server, including status query, status management and other features.
- **Message notification**: As long as you register the callback URL for receiving event notifications in Tencent Cloud, Tencent Cloud will actively notify your backend server of such events as change of LVB stream status and generation of recording files in a format of event message (JSON).


## API Call
Tencent Cloud provides a set of LVB Code management APIs for your backend server, including status query, status management and other features.

### 1. API List

| API                                | Description                                                   |
|---------------------------------|--------------------------------------------------------------|
| [Get_LiveStat](https://cloud.tencent.com/doc/api/258/6110) | Statistics query - query the push and playback information |
| [Get_LivePushStat](https://cloud.tencent.com/doc/api/258/6110) | Statistics query - query the push information |
| [Get_LivePlayStat](https://cloud.tencent.com/doc/api/258/6110) | Statistics query - query the playback information |
| [Get_LivePushStatHistory](https://cloud.tencent.com/document/product/267/9579) | Obtain the history of push |
| [Get_LivePushStatHistory](https://cloud.tencent.com/document/product/267/9580) | Obtain the history of playback statistics |
| [Live_Channel_GetStatus](https://cloud.tencent.com/doc/api/258/5958) | Query only status information of a stream (old version API) | 
| [Live_Channel_SetStatus](https://cloud.tencent.com/doc/api/258/5959) | It is used to **ban** an LVB stream, mainly available for porn detection | 
| [Live_Tape_GetFilelist](https://cloud.tencent.com/doc/api/258/5960) | Query the list of **recording files** for a stream in the LVB process | 
| [Live_Queue_Get](https://cloud.tencent.com/doc/api/258/5961) | Query the list of **screenshot files** for a stream in the LVB process |
| [Live_Channel_GetChannelList](https://cloud.tencent.com/document/product/267/7997) | Query channel list |
| [Live_Channel_GetLiveChannelList](https://cloud.tencent.com/document/product/267/8862) | Query the channel list in LVB |
| [mix_streamv2.start_mix_stream_advanced](https://cloud.tencent.com/document/product/267/8832) | API for stream mixing on the cloud |
| [channel_manager](https://cloud.tencent.com/document/product/267/9500) | Stop pushing stream and delay the availability of API - It can disable push for a specified stream |
| [Live_Tape_Start](https://cloud.tencent.com/document/product/267/9567) | Create a recording task - It supports scheduled recording task and real-time recording |
| [Live_Tape_Stop](https://cloud.tencent.com/document/product/267/9568) | End a recording task |

### 2. Call Method

You can call relevant API using GET request method of HTTP protocol on your **server**, that is, the parameters in the call are directly added in the URL. Example on how to call the API is provided in every API's documentation, so there is no difficulty in interfacing.

### 3. Security Mechanism
To ensure performance, we use HTTP protocol to call the API. Therefore, an effective measure to ensure the communication security between your server and Tencent Cloud backend is needed.

All cloud APIs related to LVB code adopt the same security check mechanism - **t + sign verification**:
- **t (validity period)**: If the t value specified in an API request or notification has expired, the request or notification is invalid. The purpose is to prevent network replay attacks. The format of t is the UNIX time stamp, that is, the number of seconds that have elapsed since January 1, 1970 (midnight in UTC/GMT).

- **sign (security signature)**: <font color='blue'>sign=MD5 (key + t)</font>, that is, to calculate the MD5 value by concatenating the strings of the encryption key and t. The encryption key here is CGI call key, which can be configured in Tencent Cloud LVB [Console](https://console.cloud.tencent.com/live/livecodemanage):

![](//mc.qcloudimg.com/static/img/e5034b47cead66be46b1f81a1fea8274/image.png)

- **Security Principle**
MD5 is an irreversible HASH algorithm. As long as the key is not disclosed, attackers cannot calculate the key or launch spoofing attacks even if they get many pairs of t and sign.

- **Example**
   If the current time is 2016-08-22 15:16:27 and the validity period is 1 minute, the request or notification that comes with this t received later than 2016-08-22 15:17:27 is invalid.
```
	t = "2016-08-22 15:17:27" = 1471850187
```
   Assume that the key is **5d41402abc4b2a76b9719d911017c592**, and after calculation we can get the following signature:
```
	sign = MD5(5d41402abc4b2a76b9719d911017c5921471850187) = b17971b51ba0fe5916ddcd96692e9fb3
```

## Error Code
1. HTTP error codes 

| Error Code | Description | Remarks |
|---------|---------|---------|
| 403 | Forbidden | To ensure security, verification is enabled for the API. If this error occurs when you perform verification via browser, you can check whether skey is contained in cookie |
| 404 | Not Found | Check whether the request comes with host |

2. Returned error codes

| Error Code | Description | Remarks |
|---------|---------|---------|
| appid is invalid | appid is invalid, which means the feature is not activated ||

**Note: The above error codes are specific to the APIs in "1. API List" of this document. [Event Message Notification](https://cloud.tencent.com/document/product/267/5957) is not included**.

## Message Notification
For more information, please see Tencent Cloud [Event Message Notification](https://cloud.tencent.com/document/product/267/5957) service. 

