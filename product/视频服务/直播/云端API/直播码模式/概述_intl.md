Information synchronization between your server and Tencent Cloud's CVM can be implemented by combining the following two ways:
- **API call:** Tencent Cloud provides a set of LVB code management APIs for your backend server, including status query, status management and other features.
- **Message notification:** As long as you register a callback URL for receiving event notifications in Tencent Cloud, Tencent Cloud will actively notify your backend server of such events in case of change of LVB stream status and generation of recording files in the form of event message (JSON).
![](https://main.qcloudimg.com/raw/815a6ec9d0cf7e47639929bd96b06bbe.png)

### Calling method
You can call relevant API using GET request method of HTTP protocol on your server, that is, the parameters in the call are directly added in the URL. Example on how to call the API is provided in every API's documentation, so there is no difficulty in interfacing.
### Security mechanism
To ensure performance, we use HTTP protocol to call the API. Therefore, an effective measure is required to ensure the communication security between your server and Tencent Cloud backend.

All LVB Code-related cloud APIs employ the same security check mechanism - "t + sign verification":
- **t (Expiration time):** If the t value specified in an API request or notification has expired, the request or notification is invalid. This can prevent replay attacks. The format of t is the UNIX timestamp, that is, the number of seconds that have elapsed since January 1, 1970 (midnight in UTC/GMT).
- **sign (security signature):** sign = MD5 (key + t). This means computing the MD5 value by concatenating the encryption key and t. The encryption key here is the CGI call key, which can be specified on the Tencent Cloud LVB [Console](https://console.cloud.tencent.com/live/livecodemanage):
![](https://main.qcloudimg.com/raw/6a3deea265c9dc3a0805a73cc5ad375d.png)
- **How it works**
MD5 is an irreversible HASH algorithm. As long as the key is not disclosed, attackers cannot calculate the key or launch spoofing attacks even if they get many pairs of t and sign.
- **Example**
   If the current time is 2016-08-22 15:16:27 and the validity period is 1 minute, the request or notification that comes with this t received later than 2016-08-22 15:17:27 is invalid:
```
	t = "2016-08-22 15:17:27" = 1471850187
```
   Assume that the key is **5d41402abc4b2a76b9719d911017c592**, and after calculation we can get the following signature:
```
	sign = MD5(5d41402abc4b2a76b9719d911017c5921471850187) = b17971b51ba0fe5916ddcd96692e9fb3
```

### Message notification
For more information, please see Tencent Cloud [Event Message Notification](https://cloud.tencent.com/document/product/267/5957) service.

