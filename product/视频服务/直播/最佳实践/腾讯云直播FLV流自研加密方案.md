大部分隐私直播或者需要内容安全的直播并不需要硬件级别安全，以及复杂的证书派发验证过程。而且在国内直播中，FLV 直播方式也比较流行。需要针对 FLV 的安全直播方案。

- **使用场景**：在使用 FLV 协议播放的情况下，希望流内容加密，黑客无法通过网络抓取，即使将流 dump 到本地也无法播放。
- **实施方案**：腾讯云直播自研流加密方案，客户通过提工单要求对 FLV 加密，提出加密模式(视频加密，音视频加密)，腾讯云按指定模块对直播流进行加密。在解密播放时，客户通过腾讯云 API 接口 DescribeDRMLicense 请求获取 TXEncryptionToken 密钥字段，添加到播放 URL 参数中，供播放 SDK 解密播放。
**自研加解密流程如下：**
	<img src="https://qcloudimg.tencent-cloud.cn/raw/2a1e8e4926a6c3392bbe0184e164124d.png" width=700>
- **实施方法**：具体实施过程请联系腾讯云商务或者提工单联系腾讯云直播。
- **方案优势**：全部过程可控，密钥和加解密有产品和工具支持，腾讯云提供播放器 SDK，集成方便，方案成熟。
- **存在的问题**：需要集成 SDK，只能支持客户自研播放器。Web 端和浏览器无法播放。

本方案提供 iOS 和 Android 两种接入方式，[单击这里](https://cloud.tencent.com/document/product/647/32689) 下载 SDK。

## iOS 接入
```swift
/**
 * 创建Player 实例。
 */
V2TXLivePlayer *player = [[V2TXLivePlayer alloc] init];

/**
 * 设置播放器的视频渲染 View。 该控件负责显示视频内容。
 *
 * @param view 播放器渲染 View
 * @return 返回值 {@link V2TXLiveCode}
 *         - V2TXLIVE_OK：成功
 */
[player setRenderView:view];

/**
 * 设置播放器回调。
 *
 * 通过设置回调，可以监听 V2TXLivePlayer 播放器的一些回调事件，
 * 包括播放器状态、播放音量回调、音视频首帧回调、统计数据、警告和错误信息等。
 *
 * @param observer 播放器的回调目标对象，更多信息请查看 {@link V2TXLivePlayerObserver}
 */
[player setObserver:self];

/**
 * 密钥请求请参考License获取
 * 设置密钥
 *
 * @note json中的url必须与startLivePlay的url相同，SDK通过url进行二次校验，避免key与url不匹配导致错误解密的情况。
 */
NSString *url = @"http://43.138.234.111:8000/live/flvtest100_1000.flv?caller=PROXY&bizid=5000&request_from=soc&request_type=STDFLV&TXEncryptionToken=ZW5jTW9kZT01JmVuY0tleT0yNmFjZWIxMjViNDczMWNjODRkZTAxZWEyNDA3ZDVmZCZlbmNJVj1iZmEwYmI0NDRhN2NhNDUyMDRjMmNhNzZhYWQyMWFjNA==
";

/**
 * 开始播放音视频流。
 *
 * @param url 音视频流的播放地址，支持 RTMP, HTTP-FLV, TRTC，HLS。
 * @return 返回值 {@link V2TXLiveCode}
 *         - V2TXLIVE_OK: 操作成功，开始连接并播放
 *         - V2TXLIVE_ERROR_INVALID_PARAMETER: 操作失败，url 不合法
 *         - V2TXLIVE_ERROR_REFUSED: RTC 不支持同一设备上同时推拉同一个 StreamId。
 */
[player startLivePlay:url];
```

## Android 接入
```java
/**
 * 创建Player 实例。
 */
V2TXLivePlayer player = new V2TXLivePlayer();

/**
 * 设置播放器的视频渲染 View。 该控件负责显示视频内容。
 *
 * @param view 播放器渲染 View
 * @return 返回值 {@link V2TXLiveCode}
 *         - V2TXLIVE_OK：成功
 */
player.setRenderView(view);

/**
 * 设置播放器回调。
 *
 * 通过设置回调，可以监听 V2TXLivePlayer 播放器的一些回调事件，
 * 包括播放器状态、播放音量回调、音视频首帧回调、统计数据、警告和错误信息等。
 *
 * @param observer 播放器的回调目标对象，更多信息请查看 {@link V2TXLivePlayerObserver}
 */
player.setObserver(this);

/**
 * 密钥请求请参考License获取
 * 设置密钥
 *
 * @note json中的url必须与startLivePlay的url相同，SDK通过url进行二次校验，避免key与url不匹配导致错误解密的情况。
 */
String url = "http://43.138.234.111:8000/live/flvtest100_1000.flv?caller=PROXY&bizid=5000&request_from=soc&request_type=STDFLV&TXEncryptionToken=ZW5jTW9kZT01JmVuY0tleT0yNmFjZWIxMjViNDczMWNjODRkZTAxZWEyNDA3ZDVmZCZlbmNJVj1iZmEwYmI0NDRhN2NhNDUyMDRjMmNhNzZhYWQyMWFjNA==
";

/**
 * 开始播放音视频流。
 *
 * @param url 音视频流的播放地址，支持 RTMP, HTTP-FLV, TRTC，HLS。
 * @return 返回值 {@link V2TXLiveCode}
 *         - V2TXLIVE_OK: 操作成功，开始连接并播放
 *         - V2TXLIVE_ERROR_INVALID_PARAMETER: 操作失败，url 不合法
 *         - V2TXLIVE_ERROR_REFUSED: RTC 不支持同一设备上同时推拉同一个 StreamId。
 */
player.startLivePlay(url);
```

## License 获取
1. 设置 API 接口名称为 `DescribeDRMLicense`。
2. 接口请求域名： `drm.tencentcloudapi.com`。
3. 开发者需要指定使用的 DRM 类型取值 NORMALAES、和需要加密的 Track 类型取值 SD，ContentType 取值 LiveVideo，ContentId 为用户的流 id。
	- 示例：
	- 测试环境请求：
```
POST / HTTP/1.1
Host: drm.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeDRMLicense
<公共请求参数>

{
    "DrmType":"NORMALAES",
    "ContentId":"flvtest100",
    "Tracks":[
        "SD"
    ],
    "ContentType":"LIVEVIDEO"
}

```
	- 请求结果：
```
{
    "Response": {
        "ContentId": "flvtest100",
        "TXEncryptionToken": "ZW5jTW9kZT01JmVuY0tleT0yNmFjZWIxMjViNDczMWNjODRkZTAxZWEyNDA3ZDVmZCZlbmNJVj1iZmEwYmI0NDRhN2NhNDUyMDRjMmNhNzZhYWQyMWFjNA==",
        "RequestId": "47f336fd-b05a-4192-b1f4-8f9d4c5f76f1"
    }
}

```
