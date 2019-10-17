
## Compatibility Description
LVB code is a solution of LVB designed by Tencent Cloud for VIP customers. Until lately, it can only be activated through internal application. Therefore, the initial solution is not compatible with [Channel Hosting](https://cloud.tencent.com/doc/api/258/5659) mode.

Confirm the following before enabling the LVB Code mode:
(1) **Your online business does not rely on Channel Hosting**. If you always use the Channel Hosting mode, incompatibility after switching will impose many difficulties to you.
(2) **You do not use a large number of interactive LVB services**. The non-interactive broadcasting uses the Channel Hosting mode and many incompatibility issues will occur after switching.


## Enable LVB Code Mode
### 1. Enable LVB service
Log in to the Tencent Cloud [LVB Console](https://console.cloud.tencent.com/live). If you have not activated the service, please activate it first.
![](//mc.qcloudimg.com/static/img/fa16d8bc971a8fa5c881f00553fe855d/image.png)

### 2. Switch to LVB Code mode
If you see a green dot at the upper right corner of your channel access after activating LVB service and entering **LVB Management** page, you are in the Channel Hosting mode.
![](//mc.qcloudimg.com/static/img/dd67f3bae42d2c5df6deefe5d5f7e091/image.png)

Click the **LVB Code Access (Recommended)** tab, and you can see the switch to enable the LVB code service:
![](//mc.qcloudimg.com/static/img/5a33cf2173f1b39c458e3da7fa808bc9/image.png)

Click the **Enable LVB Code** button, and you can see a compatibility tip. If your online business is dependent on the Channel Hosting mode, it is not recommended to enable this service. Then, enter the configuration page:
![](//mc.qcloudimg.com/static/img/9f3f012d7fddf7c0c21dc734f5c36ad5/image.png)

### 3. Configure key parameters
Before the LVB Code mode is actually enabled, you need to define four configuration items as shown above:

| Configuration Item | Value Range | Description |
|----------|----------------------|--------------|
| LVB Recording | Enable or Disable | If this is enabled, all LVB videos are recorded in background by default. [Reference Documentation](https://cloud.tencent.com/doc/api/258/5691) |
| Push Hotlink Protection Key | A 32-character lowercase string | To ensure security, the push URL needs to be bound to hotlink protection to avoid being hacked by others. The key is used to calculate the hotlink protection signature. [Reference Documentation](https://cloud.tencent.com/doc/api/258/5693) |
| API Authentication Key | A 32-character lowercase string | Your server needs to provide authentication information when calling the Tencent Cloud backend APIs. The key is used by Tencent Cloud to verify the validity of your server's identity. [Reference Documentation](https://cloud.tencent.com/doc/api/258/5956) |
| Callback URL | HTTP protocol-based URL | Tencent Cloud sends the notifications of push, push interruption and other events to you via this URL. HTTPS protocol is not supported. [Reference Documentation](https://cloud.tencent.com/doc/api/258/5957) |

### 4. Activate the service
Click **Confirm Access** to switch your Tencent Cloud LVB service to the LVB Code mode. After enabling this mode, the page will display as follows:
![](//mc.qcloudimg.com/static/img/1400072859844bc1fa5dcf45bfa205c1/image.png)

You will notice two significant changes on the page:
(1) The LVB Code Access (Recommended) tab becomes active.
(2) At the top of the page, a bizid number appears, which is used to assemble the push address. For more information, please see [Reference Documentation](https://cloud.tencent.com/doc/api/258/5649#.E6.8E.A8.E6.B5.81.E5.9C.B0.E5.9D.80).

### 5. Use auxiliary tools and codes
The page where the LVB Code mode is activated also provides an **address generator**, used to facilitate your URL test, because manual calculation of the hotlink protection signature is very difficult.
![](//mc.qcloudimg.com/static/img/7fe2bd6e762c1e109f77f36853b9749e/image.png)

At the bottom of the page, the page also provides two push address generation codes: PHP and Java. You can embed them in your backend program.

## Return to Channel Mode
After enabling the LVB Code mode, if you find that the mode is not applicable to you, you can return to the Channel Hosting mode by clicking **Enable Channel Hosting** on **Channel Hosting** tab.
![](//mc.qcloudimg.com/static/img/2cc6da75cb59781c95a7b5646055e271/image.png)







