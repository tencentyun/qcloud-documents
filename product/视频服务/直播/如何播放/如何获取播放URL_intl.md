
## How to Get a Playback URL

### 1. Getting a playback URL in channel mode

When you create a channel, select the required playback bitrate, as shown below:
![](https://mc.qcloudimg.com/static/img/9ce69e0956fa742c04fea9398a9a9988/1233.png)


In receiver settings, select the required playback protocol, as shown below:
![](https://mc.qcloudimg.com/static/img/c86206664ad3289911b276d1a9686e82/123.png)


Click **OK**. After the channel is created, you can view playback URLs for various playback bitrates and playback protocols in the channel information, as shown below:
![](https://mc.qcloudimg.com/static/img/afecc7c3963e083c27fba7748b718651/12334.png)


### 2. Getting a Playback URL in LVB code mode
Switch to LVB code mode, and enter the LVB code in the push generator to get the corresponding push id and playback id.
* The push generator is a tool used to generate push and playback URLs. When a URL is generated, the stream is not created until the push is actually successful.
* The LVB code is a stream id, equivalent to a channel in channel mode or a room.
![](https://mc.qcloudimg.com/static/img/de6150ff5a0f8c766ddbd64f72edd9bb/133.png)

**For multi-bitrate playback, when you obtain a playback URL, append the bitrate suffix to the URL.** 

For example:

```
SD (550 Kbps) playback address of rtmp protocol: rtmp://2001.liveplay.myqcloud.com/live/2001_test_550
HD (900 Kbps) playback address of rtmp protocol: rtmp://2001.liveplay.myqcloud.com/live/2001_test_900
SD (550 Kbps) playback address of flv protocol: http://2001.liveplay.myqcloud.com/live/2001_test_550.flv
HD (900 Kbps) playback address of flv protocol: http://2001.liveplay.myqcloud.com/live/2001_test_900.flv
SD (550 Kbps) playback address of hls protocol: http://2001.liveplay.myqcloud.com/live/2001_test_550.m3u8
HD (900 Kbps) playback address of hls protocol: http://2001.liveplay.myqcloud.com/live/2001_test_900.m3u8

```

### 3. Generating a playback URL at the backend
**Suitable to LVB Code mode.**

#### 3.1 Playback URL without hotlink protection
If It is not convenient to generate a URL in the console with a tool, you can do it in your business backend using code according to the generation logic of the playback URL. 

There is a mapping relationship between push URL and playback URL as follows.
Suppose the format of a push URL is:
`rtmp://bizid.livepush.myqcloud.com/live/bizid_id? `

Then, the format of playback URLs are:
```
rtmp://bizid.liveplay.myqcloud.com/live/bizid_id
http://bizid.liveplay.myqcloud.com/live/bizid_id,flv
http://bizid.liveplay.myqcloud.com/live/bizid_id.m3u8
```

For example, if the bizid of an account is 8888 and id is test, the playback URLs are:
```rtmp://bizid.liveplay.myqcloud.com/live/bizid_test
http://bizid.liveplay.myqcloud.com/live/bizid_test,flv
http://bizid.liveplay.myqcloud.com/live/bizid_test.m3u8
```

The bizid can be viewed on the console. The id is customizable and comprised of uppercase and lowercase letters and underscores.
![](https://mc.qcloudimg.com/static/img/f70a09344a89e7c1c4491b1cf6a567f9/132.png)

#### 3.2 Multi-bitrate playback URL

For multi-bitrate playback, append the bitrate suffix to the URL. For example:

For example:
```
SD (550 Kbps) playback address of rtmp protocol: rtmp://2001.liveplay.myqcloud.com/live/2001_test_550
HD (900 Kbps) playback address of rtmp protocol: rtmp://2001.liveplay.myqcloud.com/live/2001_test_900
SD (550 Kbps) playback address of flv protocol: http://2001.liveplay.myqcloud.com/live/2001_test_550.flv
HD (900 Kbps) playback address of flv protocol: http://2001.liveplay.myqcloud.com/live/2001_test_900.flv
SD (550 Kbps) playback address of hls protocol: http://2001.liveplay.myqcloud.com/live/2001_test_550.m3u8
HD (900 Kbps) playback address of hls protocol: http://2001.liveplay.myqcloud.com/live/2001_test_900.m3u8
```

#### 3.3 Playback URL with hotlink protection
 
 The format of a playback URL with hotlink protection is as follows:
 ```
rtmp://bizid.liveplay.myqcloud.com/live/bizid_id?xSecret=xxxx&txTime=xxxx
http://bizid.liveplay.myqcloud.com/live/bizid_id,flv?xSecret=xxxx&txTime=xxxx
http://bizid.liveplay.myqcloud.com/live/bizid_id.m3u8?xSecret=xxxx&txTime=xxxx
```
**Parameter description:**
1. txTime: The expiration timestamp of the playback URL. The request sent before this timestamp is valid, otherwise it is invalid and will be rejected.
2. txSecret: The verification string. **It is calculated based on txSecret = MD5 (KEY + path + txTime)**, and is all in lower case.
Where,
* txTime: The expiration timestamp of the playback URL as mentioned above.
* path: The file name with suffix removed. For example:
```
rtmp: //5000.liveplay.myqcloud.com/live/test2016011415               path is test2016011415
http: //5000.liveplay.myqcloud.com/live/test2016011415_550.m3u8      path is test2016011415_550
http: //5000.liveplay.myqcloud.com/live/test2016011415_900.flv       path is test2016011415_900
```
* KEY: User's key assigned by the console. You can view the KEY by going to **LVB Code Mode** -> **Access Configuration** -> **Application Information**.
![](https://mc.qcloudimg.com/static/img/f96379d3803342bb5e4d4465c23d1c7a/12.png)


**Configuration application** 

To configure the hotlink protection, submit a ticket or contact Tencent's service personnel. Tel: 4009-100-100.

