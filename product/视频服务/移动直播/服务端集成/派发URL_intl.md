<h2 id="Why"> Why should I assign URLs?</h2>

A push URL is required for LVB push, and a playback URL is required for LVB playback. For either single-session LVB or free-run LVB, assigning URLs at backend is more flexible than hardcoding URLs in your Apps.

Assigning URLs refers to the processes of returning push URLs to Apps when VJs are ready to push streams ([iOS](https://cloud.tencent.com/document/product/454/7879) | [Android](https://cloud.tencent.com/document/product/454/7885)) on Apps and returning playback URLs to Apps when viewers need to play back the streams ([iOS](https://cloud.tencent.com/document/product/454/7880) | [Android](https://cloud.tencent.com/document/product/454/7886)) on Apps.

<h2 id="URL"> Composition of URL </h2>

### Composition of playback URL

A standard push URL is shown below, which consists of three parts:
 ![url](//mc.qcloudimg.com/static/img/6b4fd09ab2c7d6f1503070f8c994f4e0/image.png)

- **LVB Code**
It is also called room ID. Random numbers or user ID is recommended. BIZID prefix is required in a valid LVB code.

- **txTime**
It refers to the time when the URL expires. The format is UNIX time stamp in hexadecimal notation, for example, 5867D600 means that the URL will expire at 00:00:00 AM on Jan. 1, 2017. Generally, txTime is set to a time which is 24 hours later than the current time. <font color='red'>It is not recommended to set a too short validity period</font> to avoid the inability of VJ to restore push in case of a flash breakdown of network during the broadcasting.

- **txSecret**
This refers to hotlink protection signature, which is used to prevent attackers from simulating your backend server to generate push URL. For more information about computing method, please see [Computing of Hotlink Protection](https://cloud.tencent.com/document/product/454/9875).

- **Sample Code**
Go to [**LVB Console** -> **LVB Code Access** -> **Push Generator**](https://console.cloud.tencent.com/live/livecodemanage). In the lower part of the page, the sample code (PHP and Java) is provided to show how to generate a hotlink protection URL.

### Composition of playback URL
Constructing a playback URL is as simple as constructing a push URL, except that the sub-domain name needs to be changed from **livepush** to **<font color='red'>liveplay</font>**:
![](//mc.qcloudimg.com/static/img/b7d8744654af4a174edf47f8998348a4/image.png)


<h2 id="Secret"> Hotlink protection signature</h2>

### What is hotlink protection signature?
Hotlink protection signature refers to **txTime** and **txSecret** in the push and playback URLs. It helps protect your traffic from being sucked up by attackers who fake your LVB URL.

![](//mc.qcloudimg.com/static/img/4c0ba5f9993da67ff785f10eb4c85f3d/image.png)

### How it works
To prevent attackers from simulating your server to generate push URL, you need to configure in LVB console a **hotlink protection encryption key** that is unlikely to be obtained by attackers for faking a valid push URL. The figure below shows how it works.
![](//mccdn.qcloud.com/static/img/4ea1512fd335f68f30cca0a01e902966/image.png)

### How do I calculate the hotlink protection signature?
#### Step1: Exchange the key
First, set an "encryption key" in the [LVB Console](https://console.cloud.tencent.com/live/livecodemanage) to calculate the hotlink protection signature on you server. As Tencent Cloud has the same key, Tencent Cloud can verify the validity of your hotlink protection signature.

Keys are classified into **push hotlink protection keys** and **playback hotlink protection keys**. The former are used to generate the push hotlink protection URLs and the latter are used to generate the playback hotlink protection URLs. In [LVB Console](https://console.cloud.tencent.com/live/livecodemanage), you can configure the push hotlink protection key, as shown below:
![](//mc.qcloudimg.com/static/img/6be1d875f1120a16d3692c60bb4485a9/image.png)
 > **The playback hotlink protection cannot be configured.**
 >   
 > Since the configuration of playback hotlink protection key needs to be synchronized to thousands of CDN clusters, the key cannot be frequently modified in the debugging phase due to a long synchronization period. Contact us if you need to configure the playback hotlink protection by calling our customer service. It generally takes 1 to 3 days to complete the configurations for all of the CDN clusters.

#### step2 : txTime
In the signature, the plaintext is txTime, which indicates the URL validity period. For example, if the current time is 2016-07-29 11:13:45 and the generated URL is expected to expire after 24 hours, txTime can be set to 2016-07-30 11:13:45.

To shorten the URL string, "2016-07-30 11:13:45" is first converted to a Unix timestamp (1469848425) and then a hexadecimal string. That is, txTime = 1469848425 (decimal) = 579C1B69 (hexadecimal).
 
Generally, txTime is set to a time which is 12 hours later than the current time. <font color='red'>It is not recommended to set a too short validity period</font> to avoid the inability of VJ to restore push in case of a flash breakdown of network during the broadcasting.

#### step3 : txSecret

<table><tr><td style="width: 700px; height: 80px; text-align:center; "> 
<B>txSecret = MD5 (KEY + stream_id + txTime)</B> 
</td></tr></table>

Here, the **KEY** is the encryption key you configured in Step 1. The **stream_id** is the LVB code (or stream ID). The **txTime** is 579C1B69 as calculated above. The **MD5** is the standard MD5 hash algorithm.

#### Step 4: Combine to obtain a URL
Combine the push (or playback) URL, the txTime indicating the expiration time of the URL and the txSecret that can be decrypted and verified only by Tencent Cloud to generate a secure hotlink protection URL.

<table><tr><td style="width: 700px; height: 80px; text-align:center; "> 
rtmp://8888.livepush.myqcloud.com/live/8888_test001?txSecret=xxx&txTime=5C2A3CFF
</td></tr></table>
	
> Go to [**LVB Console** -> **LVB Code Access** -> **Push Generator**](https://console.cloud.tencent.com/live/livecodemanage). In the lower part of the page, the sample code (PHP and Java) is provided to show how to generate a hotlink protection URL.





