### Push URL 
In the actual application scenario, it is impossible to create push and playback URLs manually for each VJ. Instead, these URLs are constructed automatically by your server. Any URL that conforms to Tencent Cloud specifications can be used as a push URL. A standard push URL is shown below, which consists of three parts:
 ![url](//mc.qcloudimg.com/static/img/6b4fd09ab2c7d6f1503070f8c994f4e0/image.png)
- **LVB Code**
It is also called room ID. Random numbers or user ID is recommended. BIZID prefix is required in a valid LVB code.
- **txTime**
It refers to the time when the URL expires. It is expressed as a hexadecimal UNIX timestamp, for example, 5867D600 indicates the URL will expire at 00:00:00 AM on Jan. 1, 2017. Generally, txTime is set to a time which is 24 hours later than the current time. It is not recommended to set a too short validity period to avoid the inability of VJ to restore push in case of a flash breakdown of network during the broadcasting.
- **txSecret**
This refers to hotlink protection signature, which is used to prevent attackers from simulating your backend server to generate push URL. For more information about computing method, see [Computing of Hotlink Protection](https://cloud.tencent.com/document/product/267/13458).
- **Sample Code**
Go to [LVB Console](https://console.cloud.tencent.com/), select **LVB Code Access (Recommended)** -> [**Push Generator**](https://console.cloud.tencent.com/live/livecodemanage). In the lower part of the page, **Push URL Sample Code** (PHP and Java) is provided to show how to generate a hotlink protection URL.

### Playback URL
Constructing a playback URL is as simple as constructing a push URL, except that the sub-domain name needs to be changed from livepush to liveplay:
![](//mc.qcloudimg.com/static/img/b7d8744654af4a174edf47f8998348a4/image.png)

