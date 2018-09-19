
## 获取播放地址

### 1.频道模式获取播放地址

创建一个频道,选择需要的播放码率，如下图
![](https://mc.qcloudimg.com/static/img/9ce69e0956fa742c04fea9398a9a9988/1233.png)


在接收方设置中，选择需要的播放协议，如下图
![](https://mc.qcloudimg.com/static/img/c86206664ad3289911b276d1a9686e82/123.png)


单击确认。创建完成后，在频道信息中可查看到各种码率和播放协议对应的播放URL，如下图
![](https://mc.qcloudimg.com/static/img/afecc7c3963e083c27fba7748b718651/12334.png)


### 2.直播码模式获取播放地址
进入直播吗模式，在推流生成器中输入直播码，可得到对应的推流id和播放id。
* 推流生成器是一个推流播放地址生成的工具，仅是一个工具，工具展示出URL时该条流并未建立，实际推流成功后，才会建立对应的一条流
* 直播码即 一条流的id，等同于频道模式的频道概念，或者房间的概念。
![](https://mc.qcloudimg.com/static/img/de6150ff5a0f8c766ddbd64f72edd9bb/133.png)

**如需多码率，则获取到播放URL后，在URL后携带码率后缀**，

例：

```
rtmp协议，标清（550kbps）播放地址：rtmp://2001.liveplay.myqcloud.com/live/2001_test_550
rtmp协议，高清（900kbps）播放地址：rtmp://2001.liveplay.myqcloud.com/live/2001_test_900
flv协议，标清（550kbps）播放地址： http://2001.liveplay.myqcloud.com/live/2001_test_550.flv
flv协议，高清（900kbps）播放地址：http://2001.liveplay.myqcloud.com/live/2001_test_900.flv
hls协议，标清（550kbps）播放地址：http://2001.liveplay.myqcloud.com/live/2001_test_550.m3u8
hls协议，高清（900kbps）播放地址：http://2001.liveplay.myqcloud.com/live/2001_test_900.m3u8

```

### 3.业务后台生成播放地址
**适用于直播码模式**

#### 3.1 不带防盗链的播放地址
在控制台上通过工具生成地址不够方便，您可根据播放地址的生成逻辑在您的业务后台用代码实现

推流地址和播放地址是有对应关系的，如下，
假设推流地址格式：
`rtmp://bizid.livepush.myqcloud.com/live/bizid_id？`

则播放地址格式：
```
rtmp://bizid.liveplay.myqcloud.com/live/bizid_id
http://bizid.liveplay.myqcloud.com/live/bizid_id,flv
http://bizid.liveplay.myqcloud.com/live/bizid_id.m3u8
```

例如：帐号对应的bizid为8888，,id为test，则播放地址为：
```rtmp://bizid.liveplay.myqcloud.com/live/bizid_test
http://bizid.liveplay.myqcloud.com/live/bizid_test,flv
http://bizid.liveplay.myqcloud.com/live/bizid_test.m3u8
```

bizid可在控制台上查看，id为自定义部分，一般由大小英文字幕和下划线组成
![](https://mc.qcloudimg.com/static/img/f70a09344a89e7c1c4491b1cf6a567f9/132.png)

#### 3.2 多码率播放地址

同上，如需多码率，在URL后携带码率后缀，

例：
```
rtmp协议，标清（550kbps）播放地址：rtmp://2001.liveplay.myqcloud.com/live/2001_test_550
rtmp协议，高清（900kbps）播放地址：rtmp://2001.liveplay.myqcloud.com/live/2001_test_900
flv协议，标清（550kbps）播放地址： http://2001.liveplay.myqcloud.com/live/2001_test_550.flv
flv协议，高清（900kbps）播放地址：http://2001.liveplay.myqcloud.com/live/2001_test_900.flv
hls协议，标清（550kbps）播放地址：http://2001.liveplay.myqcloud.com/live/2001_test_550.m3u8
hls协议，高清（900kbps）播放地址：http://2001.liveplay.myqcloud.com/live/2001_test_900.m3u8
```

#### 3.3 带防盗链的播放地址
 
 携带防盗链的播放地址格式如下：
 ```
rtmp://bizid.liveplay.myqcloud.com/live/bizid_id?xSecret=xxxx&txTime=xxxx
http://bizid.liveplay.myqcloud.com/live/bizid_id,flv?xSecret=xxxx&txTime=xxxx
http://bizid.liveplay.myqcloud.com/live/bizid_id.m3u8?xSecret=xxxx&txTime=xxxx
```
**参数说明：**
1.txTime：播放地址的有效截止时间戳，在该时间戳之前请求是合法请求，时间戳之后的请求是非法请求会被拒绝。
2.txSecret：校验串，**算法为：txSecret = MD5(KEY+ path + txTime)**字母小写
其中
* txTime：播放地址的有效截止时间戳，同上
* path：取的是去掉后缀的文件名。如：
```
rtmp://5000.liveplay.myqcloud.com/live/test2016011415               path为test2016011415
http://5000.liveplay.myqcloud.com/live/test2016011415_550.m3u8      path为test2016011415_550
http://5000.liveplay.myqcloud.com/live/test2016011415_900.flv       path为test2016011415_900
```
* KEY：为用户的密钥；由控制分配，进入直播码模式——接入配置——应用信息 即可查看
![](https://mc.qcloudimg.com/static/img/f96379d3803342bb5e4d4465c23d1c7a/12.png)


**配置申请**

如需配置播放防盗链，可提交工单或者联系腾讯商务人员，联系电话：4009-100-100
