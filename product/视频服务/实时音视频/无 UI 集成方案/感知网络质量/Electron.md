本文档主要介绍如何感知当前网络的好与坏。

当我们在使用微信视频通话的时候，如果遇到网络环境较差的情况（比如在进入电梯以后），微信会在视频通话的界面上提示”您当前的网络质量较差“。本文档主要介绍如何通过 TRTC 完成同样的交互。

<img src="https://qcloudimg.tencent-cloud.cn/raw/22766930827983b14cf0875776233eeb.jpg" width=800>

## 调用指引

TRTC 提供了一个叫做 **onNetworkQuality** 的回调事件，它会每隔两秒钟一次向您汇报当前的网络质量，其参数包括 localQuality 和 remoteQuality 两个部分：
- **localQuality** ：代表您当前的网络质量，分为 6 个等级，分别是 Excellent、Good、Poor、Bad、VeryBad 和 Down。
- **remoteQuality**：代表远端用户的网络质量，这是一个素组，素组中的每个元素代表一个远端用户的网络质量。

| Quality | 名称 | 说明 |
|---------|---------|---------|
| 0 | Unknown | 未感知到 |
| 1 | Excellent | 当前网络非常好 |
| 2 | Good | 当前网络比较好 |
| 3 | Poor | 当前网络一般 |
| 4 | Bad | 当前网络较差，可能会出现明显的卡顿和通话延迟|
| 5 | VeryBad | 当前网络很差，TRTC 只能勉强保持连接，但无法保证通讯质量|
| 6 | Down | 当前网络不满足 TRTC 的最低要求，无法进行正常的音视频通话|

您只需要监听 TRTC 的 [onNetworkQuality](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onNetworkQuality) 并在界面上做相应地提示即可：

```javascript
import TRTCCloud, { TRTCQuality } from 'trtc-electron-sdk';
const rtcCloud = new TRTCCloud();

function onNetworkQuality(localQuality, remoteQuality) {
  switch(localQuality.quality) {
    case TRTCQuality.TRTCQuality_Unknown:
      console.log('SDK has not yet sensed the current network quality.');
      break;
    case TRTCQuality.TRTCQuality_Excellent:
      console.log('The current network is very good.');
      break;
    case TRTCQuality.TRTCQuality_Good:
      console.log('The current network is good.');
      break;
    case TRTCQuality.TRTCQuality_Poor:
      console.log('The current network quality barely meets the demand.');
      break;
    case TRTCQuality.TRTCQuality_Bad:
      console.log('The current network is poor, and there may be significant freezes and call delays.');
      break;
    case TRTCQuality.TRTCQuality_Vbad:
      console.log('The current network is very poor, the communication quality cannot be guaranteed.');
      break;
    case TRTCQuality.TRTCQuality_Down:
      console.log('The current network does not meet the minimum requirements.');
      break;
    default:
      break;
  }
  for (let i = 0; i < remoteQuality.length; i++) {
    console.log(`remote user: ${remoteQuality[i].userId}, quality: ${remoteQuality[i].quality}`);
  }
}

rtcCloud.on('onNetworkQuality', onNetworkQuality);
```
