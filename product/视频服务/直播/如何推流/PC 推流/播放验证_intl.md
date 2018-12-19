### Confirming playback URL
If the push URL (livepush) is `rtmp://3891.livepush.myqcloud.com/live/3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F`, the playback URL (liveplay) is:

| Playback Protocol | Playback URL | 
|---------|---------|
| FLV |  [rtmp://3891.<font color='red'>liveplay</font>.myqcloud.com/live/3891_test]() |
| RTMP | [http://3891.<font color='red'>liveplay</font>.myqcloud.com/live/3891_test.flv]() |
| HLS(m3u8) | [http://3891.<font color='red'>liveplay</font>.myqcloud.com/live/3891_test.m3u8]() |


### RTMP DEMO playback verification
[Download](https://cloud.tencent.com/document/product/454/6555) RTMP DEMO, generate a QR code from the playback URL using the online QR code [generator](http://cli.im/), and then scan the QR for playback.

### VLC playback verification
Click [VLC download address](http://www.videolan.org/vlc/) to install the player with default settings. Open the player, click **Media Menu**, select **Open Network Streaming**, enter the playback URL, and click **Play**.
![](//mc.qcloudimg.com/static/img/7923a14be5525bd37719c18d54243403/image.png)




