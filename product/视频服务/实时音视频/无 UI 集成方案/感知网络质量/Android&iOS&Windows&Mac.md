本文档主要介绍如何感知当前网络的好与坏。

当我们在使用微信视频通话的时候，如果遇到网络环境较差的情况（比如在进入电梯以后），微信会在视频通话的界面上提示”您当前的网络质量较差“。本文档主要介绍如何通过 TRTC 完成同样的交互。

![](https://qcloudimg.tencent-cloud.cn/raw/22766930827983b14cf0875776233eeb.jpg)

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

您只需要监听 TRTC 的 onNetworkQuality 并在界面上做相应地提示即可：

<dx-codeblock>
::: Android  java
// 监听 onNetworkQuality 回调并感知当前网络状态的变化
@Override
public void onNetworkQuality(TRTCCloudDef.TRTCQuality localQuality,
                             ArrayList<TRTCCloudDef.TRTCQuality> remoteQuality)
{
    // Get your local network quality
    switch(localQuality) {
        case TRTCQuality_Unknown:
            Log.d(TAG, "SDK has not yet sensed the current network quality.");
            break;
        case TRTCQuality_Excellent:
            Log.d(TAG, "The current network is very good.");
            break;
        case TRTCQuality_Good:
            Log.d(TAG, "The current network is good.");
            break;
        case TRTCQuality_Poor:
            Log.d(TAG, "The current network quality barely meets the demand.");
            break;
        case TRTCQuality_Bad:
            Log.d(TAG, "The current network is poor, and there may be significant freezes and call delays.");
            break;
        case TRTCQuality_VeryBad:
            Log.d(TAG, "The current network is very poor, the communication quality cannot be guaranteed");
            break;
        case TRTCQuality_Down:
            Log.d(TAG, "The current network does not meet the minimum requirements.");
            break;
        default:
            break;
    }
    // Get the network quality of remote users
    for (TRTCCloudDef.TRTCQuality info : arrayList) {
        Log.d(TAG, "remote user : = " + info.userId + ", quality = " + info.quality);
    }
}
:::
::: iOS&Mac  ObjC
// 监听 onNetworkQuality 回调并感知当前网络状态的变化
- (void)onNetworkQuality:(TRTCQualityInfo *)localQuality remoteQuality:(NSArray<TRTCQualityInfo *> *)remoteQuality {
    // Get your local network quality
    switch(localQuality.quality) {
        case TRTCQuality_Unknown:
            NSLog(@"SDK has not yet sensed the current network quality.");
            break;
        case TRTCQuality_Excellent:
            NSLog(@"The current network is very good.");
            break;
        case TRTCQuality_Good:
            NSLog(@"The current network is good.");
            break;
        case TRTCQuality_Poor:
            NSLog(@"The current network quality barely meets the demand.");
            break;
        case TRTCQuality_Bad:
            NSLog(@"The current network is poor, and there may be significant freezes and call delays.");
            break;
        case TRTCQuality_VeryBad:
           NSLog(@"The current network is very poor, the communication quality cannot be guaranteed");
            break;
        case TRTCQuality_Down:
            NSLog(@"The current network does not meet the minimum requirements.");
            break;
        default:
            break;
    }
    // Get the network quality of remote users
    for (TRTCQualityInfo *info in arrayList) {
        NSLog(@"remote user : = %@, quality = %@", info.userId, @(info.quality));
    }
}
:::
::: Windows  C++
// 监听 onNetworkQuality 回调并感知当前网络状态的变化
void onNetworkQuality(liteav::TRTCQualityInfo local_quality,
    liteav::TRTCQualityInfo* remote_quality, uint32_t remote_quality_count) {
    // Get your local network quality
    switch (local_quality.quality) {
    case TRTCQuality_Unknown:
        printf("SDK has not yet sensed the current network quality.");
        break;
    case TRTCQuality_Excellent:
        printf("The current network is very good.");
        break;
    case TRTCQuality_Good:
        printf("The current network is good.");
        break;
    case TRTCQuality_Poor:
        printf("The current network quality barely meets the demand.");
        break;
    case TRTCQuality_Bad:
        printf("The current network is poor, and there may be significant freezes and call delays.");
        break;
    case TRTCQuality_Vbad:
        printf("The current network is very poor, the communication quality cannot be guaranteed");
        break;
    case TRTCQuality_Down:
        printf("The current network does not meet the minimum requirements.");
        break;
    default:
        break;
    }
    // Get the network quality of remote users
    for (int i = 0; i < remote_quality_count; ++i) {
        printf("remote user : = %s, quality = %d", remote_quality[i].userId, remote_quality[i].quality);
    }
}
:::
</dx-codeblock>
