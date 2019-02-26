## Generating URLs Quickly
If you want to generate a group of URLs for testing, you only need to open [**LVB Console** -> **LVB Code Access** -> **Push Generator**](https://console.cloud.tencent.com/live/livecodemanage), and click the **Generate Push URL** button, to generate a push URL and three playback URLs with different playback protocols.
![](https://mc.qcloudimg.com/static/img/cc7c9364fab232a94025b4ee1a2ac3d8/image.png)

You can test the validity of these URLs using **RTMP Push** and **LVB Player** features provided with our Demo [Video Cloud Toolkit](https://cloud.tencent.com/document/product/454/6555#DE).


## Assigning URLs via Backend

Assigning URLs via Backend is more flexible than hardcoding these URLs in your Apps. If your LVB products support free-run LVB, it cannot meet your requirements to generate URLs manually.

You then need to assign URLs via backend. For more information about Tencent Cloud's push and playback URLs and how to make your backend servers generate these URLs automatically, please see [DOC](https://cloud.tencent.com/document/product/454/9875).

## Why can't I push streams?

- The expiration time is too short. URLs are considered invalid after the set expiration time.
![](https://mc.qcloudimg.com/static/img/da82219b2d8068dc1aa1fe1d00abb6a3/image.png)
- One push URL cannot be used by two persons at the same time. Otherwise a conflict occurs.
