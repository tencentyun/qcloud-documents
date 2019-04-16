According to Tencent Cloud's statistics, the customer complaints about unsuccessful push focus on the following three reasons:
![](//mc.qcloudimg.com/static/img/8f0d4acce0ae96705239f7984efd0382/image.png)

## Incorrect txSecret
Tencent Cloud currently requires adding Hotlink protection to all push URLs to ensure security. Miscalculated hotlink protection or expired push URLs will be **rejected** by Tencent Cloud. In this case, RTMP SDK will throw a **PUSH_WARNING_SERVER_DISCONNECT** event, and [RTMP SDK DEMO](https://cloud.tencent.com/document/product/454/6555) behaves as follows: 
![](//mc.qcloudimg.com/static/img/83e5c2dce6707f5c0c5e6dfc8fc548e5/image.png)

Please see [How to Obtain the Push URL](https://cloud.tencent.com/document/product/454/7915) to learn how to obtain a reliable push URL.

## Expired txTime
Some customers who worry about their LVB traffic being stolen would set a rather conservative txTime, such as 5 minutes after the current time. In fact, with txSercet signature, you don't need to set such a short validity period. Furthermore, with a too-short validity period, in case of a network interruption during LVB, the VJ would not be able to resume push due to expiration of push URL.

It's recommended to set the txTime to a value that is 12 or 24 hours after the current time, which is longer than a normal LVB duration.

## Push URL Is in Use Already
A push URL can only have one push end, and any other Client attempting to push will be rejected by Tencent Cloud. In this case, RTMP SDK will throw a **PUSH_WARNING_SERVER_DISCONNECT** event.

## Unable to Connect to CVM
The default port number used by RTMP push is **1935**. If the firewall of the network for your test doesn't open the port 1935 to the Internet, you may be unable to connect to the server. In this case, you can verify whether the problem is caused by this reason by changing network (for example, use 4G instead).

## Mini LVB Push URL
The push URL for Mini LVB can be obtained by debugging. You can search for the keyword **startPush** in the global search, then set a debugging breakpoint here, which is the calling point of RTMP SDK by Mini LVB. The parameter startPush is the push URL.




