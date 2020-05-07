# SDK 1.5.2.362 更新信息

## 【更新时间】 
 2016年08月16日

## 【最新特性】
1. 播放端不再限制只能播放腾讯云您的域名。
2. 增加音频解码对 HE-AAC V2的支持。
3. 推流及播放 VideoView 支持调整大小、支持保留最后一帧渲染。
4. 优化就近接入，更智能地选择就近接入点。
5. 彻底解决跟 Libyuv 符号冲突的问题。
6. 更新 Android 硬件编码支持的机型列表（HWSupportList.java）。
7. 修复过去一周测试团队发现的若干 bug。

## 【接口变更-IOS】
过去一个月的试用期间，不少热心客户对于接口的易用性吐槽颇多，针对这些建议，我们对SDK的接口易用性进行了调整。初次更新新版本的时候您可能会发现有些编译错误，请耐心阅读，并盼您认同新的接口有更好的功能表现。

### 1. TXLivePlayer 类
- **(void) setupVideoWidget:(CGRect)frame containView:(UIView*)view insertIndex:(unsignedint)idx;**
1.5.2版本将参数frame废弃，**设置此参数无效**，控件大小与参数 view 的大小保持一致。

- **(void) resetVideoWidgetFrame:(CGRect)frame;**
1.5.2版本将此方法废弃，**调用此方法无效**，如需修改控件的大小及位置，请调整父 view （方法 setupVideoWidget 中参数 view）的大小及位置；具体参考 [渲染控制](https://cloud.tencent.com/doc/api/258/4734)。

- **(NSArray*) getSDKVersion;**
1.5.2版本将此接口由实例方法变更为TXLivePush 和 TXLivePlayer的类方法。

- **(int)sendCustomYUVData: (unsigned char *)pYUVBuff dataLen:(unsigned int)dataLen;**
1.5.2版本 sendCustomYUVData 增加函数返回值，SDK 内部不再做帧率控制，请务必保证调用该函数的频率和 TXLivePushConfig 中设置的帧率一致，否则编码器输出的码率会不受控制。

| 返回值     | 含义                      | 
|-------------|-------------------------|
| >0          |调用频率超过了 TXLivePushConfig 中设置的帧率              | 
| =0          |数据被成功送交 SDK 内核              | 
| -1           |视频分辨率非法                          | 
| -2           |YUV数据长度 dataLen 与设置的视频分辨率所要求的长度不一致                         | 

### 2. TXLivePush类
- **(NSArray*) getSDKVersion;**
1.5.2版本将此接口由实例方法变更为 TXLivePush 和  TXLivePlayer 的类方法。


## 【接口变更-Android】
### 1. TXLivePlayer类
- **public static int[] getSDKVersion()**
1.5.2版本将此接口由成员函数变更为静态函数。

### 2.TXLivePusher类
- **public static int[] getSDKVersion()**
1.5.2版本将此接口由成员函数变更为静态函数。

- **public int sendCustomYUVData(byte [] yuvBuffer)**
1.5.2版本 sendCustomYUVData 增加函数返回值，SDK 内部不再做帧率控制，请务必保证调用该函数的频率和 TXLivePushConfig 中设置的帧率一致，否则编码器输出的码率会不受控制。

| 返回值     | 含义                      | 
|-------------|-------------------------|
| >0          |调用频率超过了 TXLivePushConfig 中设置的帧率              | 
| =0          |数据被成功送交 SDK 内核              | 
| -1           |视频分辨率非法                          | 
| -2           |YUV 数据长度 dataLen 与设置的视频分辨率所要求的长度不一致  

## 【测试情况】
 测试总用例数：280 通过用例数：273 不通过用例数：7。
