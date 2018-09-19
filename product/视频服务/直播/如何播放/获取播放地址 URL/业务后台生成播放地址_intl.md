Suitable to LVB Code mode.

### Playback URL without Hotlink Protection
If It is not convenient to generate a URL with a tool on the console, you can do it with code in your business backend according to the generation logic of the playback URL. There is a mapping relationship between push URL and playback URL. Suppose the format of a push URL is:
```
rtmp://bizid.livepush.myqcloud.com/live/bizid_id?
```
Then, the format of a playback URL is:
```
rtmp://bizid.liveplay.myqcloud.com/live/bizid_id
http://bizid.liveplay.myqcloud.com/live/bizid_id,flv
http://bizid.liveplay.myqcloud.com/live/bizid_id.m3u8
```

For example, if the bizid of an account is 8888 and ID is test, the playback URL is:
```rtmp://bizid.liveplay.myqcloud.com/live/bizid_test
http://bizid.liveplay.myqcloud.com/live/bizid_test,flv
http://bizid.liveplay.myqcloud.com/live/bizid_test.m3u8
```

The bizid can be viewed on the console. The ID is customized and generally composed of uppercase and lowercase letters and underscores.
![](//mc.qcloudimg.com/static/img/0a59cfb3247a2e14def0b03adad64595/image.png)

### Multi-bitrate Playback URL

For multi-bitrate playback, append the bitrate suffix to the URL. For example:
```
SD (550 Kbps) playback address of rtmp protocol:rtmp://11382.liveplay.myqcloud.com/live/11382_test_550
HD (900 Kbps) playback address of rtmp protocol:rtmp://11382.liveplay.myqcloud.com/live/11382_test_900
SD (550 Kbps) playback address of flv protocol: http://11382.liveplay.myqcloud.com/live/11382_test_550.flv
HD (900 Kbps) playback address of flv protocol:http://11382.liveplay.myqcloud.com/live/11382_test_900.flv
SD (550 Kbps) playback address of hls protocol:http://11382.liveplay.myqcloud.com/live/11382_test_550.m3u8
HD (900 Kbps) playback address of hls protocol:http://11382.liveplay.myqcloud.com/live/11382_test_900.m3u8
```

### Playback URL with Hotlink Protection
 
The format of playback URL with hotlink protection is as follows:
 ```
rtmp://bizid.liveplay.myqcloud.com/live/bizid_id?xSecret=xxxx&txTime=xxxx
http://bizid.liveplay.myqcloud.com/live/bizid_id,flv?xSecret=xxxx&txTime=xxxx
http://bizid.liveplay.myqcloud.com/live/bizid_id.m3u8?xSecret=xxxx&txTime=xxxx
```
**Parameter description:**
1. txTime: The valid expiration timestamp of the playback URL. The request sent before this timestamp is valid, otherwise it is invalid and will be rejected.
2. txSecret: The verification string. It is calculated based ontxSecret = MD5(KEY+ path + txTime), and is all in lower case.
Where,
 * txTime: The valid expiration timestamp of the playback URL as mentioned above.
 * path: The file name with suffix removed, for example:
```
rtmp://5000.liveplay.myqcloud.com/live/test2016011415               The path is test2016011415.
http://5000.liveplay.myqcloud.com/live/test2016011415_550.m3u8      The path is test2016011415_550.
http://5000.liveplay.myqcloud.com/live/test2016011415_900.flv       The path is test2016011415_900.
```
 * KEY: User's key that is assigned by the console. You can view the KEY by going to **LVB Code Access** -> **Access Configuration** -> **Application Information**.
![](//mc.qcloudimg.com/static/img/e5c61fc0b7650d35b462a38080432195/image.png)


**Configuration application:**To configure the hotlink protection, [submit a ticket](https://console.cloud.tencent.com/workorder/category) or contact Tencent service personnel. Tel: 4009-100-100.

