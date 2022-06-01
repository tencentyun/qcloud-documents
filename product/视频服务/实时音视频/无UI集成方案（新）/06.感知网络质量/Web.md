本文档主要介绍如何感知当前网络的好与坏。

当我们在使用微信视频通话的时候，如果遇到网络环境较差的情况（比如在进入电梯以后），微信会在视频通话的界面上提示”您当前的网络质量较差“。本文档主要介绍如何通过 TRTC 完成同样的交互。

![](https://qcloudimg.tencent-cloud.cn/raw/22766930827983b14cf0875776233eeb.jpg)

## 实现流程
TRTC Web SDK 提供了 [NETWORK_QUALITY](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-ClientEvent.html#.NETWORK_QUALITY) 事件来实现通话过程中感知网络质量。实现流程如下：
1. 创建 Client，可以参考文档 [进入房间](to-do) `步骤1` 。
2. Client 监听 [NETWORK_QUALITY](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-ClientEvent.html#.NETWORK_QUALITY) 事件。
3. Client 进入房间，可以开始发布和订阅音视频流。

## 代码示例
 ```js
 // 创建 Client 
const client = TRTC.createClient({
  mode: 'rtc',
  sdkAppId,
  userId,
  userSig
});

// 监听 NETWORK_QUALITY 事件
client.on('network-quality', event => {
  const { uplinkNetworkQuality，downlinkNetworkQuality } = event;
});

// Client 进入房间，可以开始发布和订阅音视频流
try {
  await client.join({ roomId });
  console.log('进房成功');
} catch (error) {
  console.error('进房失败，请稍后再试' + error);
}
```

## 结果分析

经过上述步骤，可以拿到上行网络质量（uplinkNetworkQuality）、下行网络质量（downlinkNetworkQuality）。网络质量的枚举值如下所示：

| 数值 | 含义                                                         |
| :--- | :----------------------------------------------------------- |
| 0    | 网络状况未知，表示当前 client 实例还没有建立上行/下行连接    |
| 1    | 网络状况极佳                                                 |
| 2    | 网络状况较好                                                 |
| 3    | 网络状况一般                                                 |
| 4    | 网络状况差                                                   |
| 5    | 网络状况极差                                                 |
| 6    | 网络连接已断开 注意：若下行网络质量为此值，则表示所有下行连接都断开了 |

> 建议：当网络质量大于3时，应引导用户检查网络并尝试更换网络环境，否则难以保证正常的音视频通话。<br>也可通过下述策略来降低带宽消耗：
> - 若上行网络质量大于3，则可通过 [LocalStream.setVideoProfile()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html#setVideoProfile) 接口降低码率 或 [LocalStream.muteVideo()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html#muteVideo) 方式关闭视频，以降低上行带宽消耗。
> - 若下行网络质量大于3，则可通过订阅小流（参考：[开启大小流传输](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-27-advanced-small-stream.html)）或者只订阅音频的方式，以降低下行带宽消耗。