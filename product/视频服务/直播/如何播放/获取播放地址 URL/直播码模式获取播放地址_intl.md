Switch to LVB key mode, enter the LVB key in the push generator to get corresponding push ID and playback ID.
* The push generator is a tool used to generate push and playback URLs. A stream is not created when a URL is generated until the push is actually successful.
* The LVB key is a stream ID, just like a channel or a room under the channel mode.
![](//mc.qcloudimg.com/static/img/f4b599a0961fe7096b16b9898f717589/image.png)

For multi-bitrate playback, when you obtain a playback URL, append the bitrate suffix to the URL. For example:

```
SD (550 Kbps) playback address of rtmp protocol:rtmp://11382.liveplay.myqcloud.com/live/11382_test_550
HD (900 Kbps) playback address of rtmp protocol:rtmp://11382.liveplay.myqcloud.com/live/11382_test_900
SD (550 Kbps) playback address of flv protocol: http://11382.liveplay.myqcloud.com/live/11382_test_550.flv
HD (900 Kbps) playback address of flv protocol:http://11382.liveplay.myqcloud.com/live/11382_test_900.flv
SD (550 Kbps) playback address of hls protocol:http://11382.liveplay.myqcloud.com/live/11382_test_550.m3u8
HD (900 Kbps) playback address of hls protocol:http://11382.liveplay.myqcloud.com/live/11382_test_900.m3u8

```
