## What Is Hotlink Protection Signature?
Hotlink protection signature refers to **txTime** and **txSecret** in the push and playback URLs that helps protect your traffic from being sucked up by attackers who fake your LVB URL.

![](//mc.qcloudimg.com/static/img/4c0ba5f9993da67ff785f10eb4c85f3d/image.png)

## How It Works
To prevent attackers from forging your server to generate push URL, you need to configure **hotlink protection encryption key** in LVB console. Since the attackers are unable to obtain the encryption key easily, they cannot forge a valid push URL, as shown below:
![](//mccdn.qcloud.com/static/img/4ea1512fd335f68f30cca0a01e902966/image.png)


## How to Calculate the Hotlink Protection Signature
### Step 1: Exchange the key
First, set an **encryption key** in the [LVB Console](https://console.cloud.tencent.com/live/livecodemanage) to calculate the hotlink protection signature on you server. As Tencent Cloud has the same key, it can verify the validity of your hotlink protection signature.

Keys are classified into **push hotlink protection keys** and **playback hotlink protection keys**. The former are used to generate the push hotlink protection URLs and the latter are used to generate the playback hotlink protection URLs. On the [LVB Console](https://console.qcloud.com/live), you can configure the push hotlink protection key, as shown below:
![](//mc.qcloudimg.com/static/img/6be1d875f1120a16d3692c60bb4485a9/image.png)
 >  **Playback hotlink protection is disabled by default**
 >   
 > Since the configuration of playback hotlink protection key needs to be synced to thousands of CDN clusters, it cannot be frequently modified in the debugging phase due to long synchronization period. Contact us if you need to configure the playback hotlink protection by calling our customer service. It generally takes 1 to 3 days to complete the synchronization in all of the clusters.

### Step 2: txTime
In the signature, the plaintext is txTime, which indicates the URL validity period. For example, if the current time is 2016-07-29 11:13:45 and the generated URL is expected to expire after 24 hours, txTime can be set to 2016-07-30 11:13:45.

To shorten the URL string, "2016-07-30 11:13:45 " is first converted to a Unix timestamp (1469848425) and then a hexadecimal string. That is, txTime = 1469848425 (decimal) = 579C1B69 (hexadecimal).
 
Generally, txTime is set as expired after 24 hours from the current time. It is not recommended to minimize the expiration time, because once network interruptions occur during broadcasting, VJ cannot resume push if the expiration time is too short.

### Step 3: txSecret

<table><tr><td style="width: 700px; height: 80px; text-align:center; "> 
<B>txSecret = MD5 (KEY + stream_id + txTime)</B> 
</td></tr></table>

Here, the **KEY** is the encryption key you configured in Step 1. The **stream_id** is the LVB code (or stream ID). The **txTime** is 579C1B69 as calculated above. The **MD5** is the standard MD5 hash algorithm.

### Step 4: Combine to obtain a URL
After obtaining the push (or playback) URL, the txTime used to inform Tencent Cloud of the URL expiration time, and the txSecret that can be decrypted and verified only by Tencent Cloud, you can combine them to obtain a hotlink protection security URL.

<table><tr><td style="width: 700px; height: 80px; text-align:center; "> 
rtmp://8888.livepush.myqcloud.com/live/8888_test001?txSecret=xxx&txTime=5C2A3CFF
</td></tr></table>
	
Sample codes (PHP and Java) in the lower half of ["LVB Console" -> "LVB Code Access" -> "Push Generator"](https://console.cloud.tencent.com/live/livecodemanage) page show how to generate hotlink protection URL.





