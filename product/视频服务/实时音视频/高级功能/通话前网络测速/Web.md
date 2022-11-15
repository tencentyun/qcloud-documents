在进房之前，或者通话过程中，可以检测用户的网络质量，可以提前判断用户当下的网络质量情况。若用户网络质量太差，应建议用户更换网络环境，以保证正常通话质量。

本文主要介绍如何基于 [NETWORK_QUALITY](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-ClientEvent.html#.NETWORK_QUALITY) 事件实现通话前网络质量检测。通话过程中感知网络质量，只需监听[NETWORK_QUALITY](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-ClientEvent.html#.NETWORK_QUALITY) 事件即可。

## 实现流程

1. 调用 [TRTC.createClient](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#.createClient) 创建两个 Client，分别称为 uplinkClient 和 downlinkClient。
2. 这两个 Client 都进入同一个房间。
3. 使用 uplinkClient 进行推流，监听 [NETWORK_QUALITY](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-ClientEvent.html#.NETWORK_QUALITY) 事件来检测上行网络质量。
4. 使用 downlinkClient 进行拉流，监听 [NETWORK_QUALITY](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-ClientEvent.html#.NETWORK_QUALITY) 事件来检测下行网络质量。
5. 整个过程可持续 15s 左右，最后取平均网络质量，从而大致判断出上下行网络情况。

> !
> - 检测过程将产生少量的[基础服务费用](https://cloud.tencent.com/document/product/647/17157#.E5.9F.BA.E7.A1.80.E6.9C.8D.E5.8A.A1)。如果未指定推流分辨率，则默认以 640*480 的分辨率推流。

## 代码示例

```js
let uplinkClient = null; // 用于检测上行网络质量
let downlinkClient = null; // 用于检测下行网络质量
let localStream = null; // 用于测试的流
let testResult = {
  // 记录上行网络质量数据
  uplinkNetworkQualities: [],
  // 记录下行网络质量数据
  downlinkNetworkQualities: [],
  average: {
    uplinkNetworkQuality: 0,
    downlinkNetworkQuality: 0
  }
}

// 1. 检测上行网络质量
async function testUplinkNetworkQuality() {
  uplinkClient = TRTC.createClient({
    sdkAppId: 0, // 填写 sdkAppId
    userId: 'user_uplink_test',
    userSig: '', // uplink_test 的 userSig
    mode: 'rtc'
  });

  localStream = TRTC.createStream({ audio: true, video: true });
  // 根据实际业务场景设置 video profile
  localStream.setVideoProfile('480p'); 
  await localStream.initialize();

  uplinkClient.on('network-quality', event => {
    const { uplinkNetworkQuality } = event;
    testResult.uplinkNetworkQualities.push(uplinkNetworkQuality);
  });

  // 加入用于测试的房间，房间号需要随机，避免冲突
  await uplinkClient.join({ roomId: 8080 }); 
  await uplinkClient.publish(localStream);
}

// 2. 检测下行网络质量
async function testDownlinkNetworkQuality() {
  downlinkClient = TRTC.createClient({
    sdkAppId: 0, // 填写 sdkAppId
    userId: 'user_downlink_test',
    userSig: '', // userSig
    mode: 'rtc'
  });

  downlinkClient.on('stream-added', async event => {
    await downlinkClient.subscribe(event.stream, { audio: true, video: true });
		// 订阅成功后开始监听网络质量事件
    downlinkClient.on('network-quality', event => {
      const { downlinkNetworkQuality } = event;
      testResult.downlinkNetworkQualities.push(downlinkNetworkQuality);
    });
  })
  // 加入用于测试的房间，房间号需要随机，避免冲突
  await downlinkClient.join({ roomId: 8080 });
}

// 3. 开始检测
testUplinkNetworkQuality();
testDownlinkNetworkQuality();

// 4. 15s 后停止检测，计算平均网络质量
setTimeout(() => {
  // 计算上行平均网络质量
  if (testResult.uplinkNetworkQualities.length > 0) {
    testResult.average.uplinkNetworkQuality = Math.ceil(
      testResult.uplinkNetworkQualities.reduce((value, current) => value + current, 0) / testResult.uplinkNetworkQualities.length
    );
  }

  if (testResult.downlinkNetworkQualities.length > 0) {
    // 计算下行平均网络质量
    testResult.average.downlinkNetworkQuality = Math.ceil(
      testResult.downlinkNetworkQualities.reduce((value, current) => value + current, 0) / testResult.downlinkNetworkQualities.length
    );
  }
    
  // 检测结束，清理相关状态。
  uplinkClient.leave();
  downlinkClient.leave();
  localStream.close();
}, 15 * 1000);
```

## 结果分析

经过上述步骤，可以拿到上行平均网络质量、下行平均网络质量。网络质量的枚举值如下所示：

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

