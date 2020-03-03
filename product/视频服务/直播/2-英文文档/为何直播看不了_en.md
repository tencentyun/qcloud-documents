When you can't watch LVB, you maybe feel frustrated, or just think of Tencent Cloud as a **black box** and have no idea about what goes wrong inside it.
Take it easy. By following the steps below, you can identify the cause of problem in a short time.

![](//mc.qcloudimg.com/static/img/29c74afc399429e40a21b28e7abe87d9/image.png)

## Step 1. Check the playback URL
First of all, check whether the playback URL is correct. An incorrect URL is the most likely cause of most problems. Tencent Cloud's LVB URLs include push URL and playback URL. You need to first verify whether **the push URL is mistakenly used as the playback URL*.
![diff](//mccdn.qcloud.com/static/img/1d093770d4b9bfaec5e15b01bdb65d00/image.png)

>**Playback URL for Mini LVB**
>
>The push URL for Mini LVB can be obtained by debugging. You can search for the keyword **startPlay** in the global search, then set a debugging breakpoint here, which is the calling point of RTMP SDK by Mini LVB. The parameter startPlay is the playback URL.

## Step 2. Check the video stream
A correct playback URL does not always mean a normal playback. Next, you need to check whether the video stream is normal:
- For **LVB**, the LVB URL becomes unavailable once the VJ stops the push.
- For **VOD**, if the video file has been removed, watching videos is also impossible.

A frequently used solution is making a check using VLC, an open-source player on PC that supports many protocols:
![](//mc.qcloudimg.com/static/img/7923a14be5525bd37719c18d54243403/image.png)

## Step 3. Check the player end
If there's no problem with the video stream, then you need to check whether the player is normal on a case-by-case basis:

### 3.1 Web browser (A)
- **Format support**: mobile browsers **only support playback URLs in an HLS (m3u8) and MP4**format.

- **HLS (m3u8)**: Tencent Cloud HLS protocol is based on Lazy Start. In short, Tencent Cloud only launch the transcoding for HLS format when viewers request for playback URL in an HLS format. The purpose of Lazy Start is to prevent wasting resources. But it also creates a problem: **the playback URL in an HLS format cannot be played until 30 seconds after the first user in the world initiates a request**.

- [**Tencent Cloud Web player: **](https://cloud.tencent.com/document/product/454/7503) Support playback URLs based on multiple protocols, and adopt the best playback strategy based on the current platform (PC, Android or iOS?). Meanwhile, the internal selective retry logic can also deal with the Lazy Start of HLS (m3u8).

### 3.2 RTMP SDK (B)
If [RTMP SDK DEMO](https://cloud.tencent.com/document/product/454/6555) works normally for playback, it's recommended to check whether the interfacing logic is incorrect by referring to RTMP SDK playback document ([iOS](https://cloud.tencent.com/document/product/454/7880) & [Android](https://cloud.tencent.com/document/product/454/7886)).

## Step 4. Firewall Blocking (C)
It is common that the corporate network environments of many customers restrict video playback through firewalls that detect whether the resources requested by HTTP are streaming media resources (After all, no boss wants his employees to watch videos during working hours).
 
The fact that you can watch the LVB normally via 4G network but cannot watch it in your company's Wi-Fi network indicates your company has imposed restrictions on the network strategy. In this case, you can contact the administrator for a special handling on your IP.

## Step 5. Check the pusher end (D)
If the LVB URL does not work and there is no possibility of firewall limitation described in Step 4, it is likely that the push is unsuccessful. Go to [Why the Push is Unsuccessful](https://cloud.tencent.com/document/product/454/7951) for a further troubleshooting.



