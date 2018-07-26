If you have not activated the Tencent Cloud LVB service, click here to [apply for the service](https://console.cloud.tencent.com/live).
![](https://main.qcloudimg.com/raw/49924e950bf97743789efcf1d881b1cf.png)

### Generate push URL
If the push URL is not ready yet, log in to Tencent Cloud [LVB Console](https://console.cloud.tencent.com/live), select **Access Management** -> **LVB Code Access (Recommended)** -> **Push Generator** to generate a push URL and three playback URLs. The URL with a domain name of livepush.myqcloud.com is the push URL:
![](https://main.qcloudimg.com/raw/3ca98ea018817419a67d954bfc1d2897.png)

### Select the network for LVB
#### Network options

| Network Type | Accessibility | Stability |
|--|--|--|
| Wired network | Low | High |
|Wi-Fi| High | Low |
If possible, it is recommended to use a wired network, which is more stable than Wi-Fi to prevent interference with signals. Wi-Fi is more suitable for live video broadcasting for events because of the convenience it offers.

#### Upstream bandwidth test
The requirement for upstream bandwidth depends on the video quality and resolution. Generally, a better video quality with a higher resolution means a higher requirement for upstream bandwidth. The upstream bandwidth should not be less than 1 Mbps. To check the condition of upstream bandwidth, you can conduct a test using [speedtest](http://www.speedtest.net/).
![](//mc.qcloudimg.com/static/img/b5724af9873220c395e295894205e4ad/image.png)

### Install push software
#### Install OBS
Download the OBS installer package on [OBS official website](https://obsproject.com/download) and then install it with default settings. Windows, Mac, and Linux operating systems are supported. Make sure the downloaded software is Open Broadcaster Software. OBS Studio is also available but is not covered in this document.
![](//mc.qcloudimg.com/static/img/dcbb929e364b1d8e80c04e326a756a26/image.png)

#### Install XSplit
Optionally, download the XSplit installer package on [XSplit official website](https://www.xsplit.com/zh_cn/) and then install it with default settings. XSplit is a paid software. In case of a budget constraint, OBS (**Free**) is recommended. A dedicated XSplit installer package is available for game LVB. For non-game LVB, BroadCaster is recommended.
![](//mc.qcloudimg.com/static/img/18c47cb7646e189acc168e6a5e8e4714/image.png)
