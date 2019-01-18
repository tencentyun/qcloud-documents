## 接入

唤醒模块目前内置于SDK中，集成SDK后即可使用。

唤醒模块默认开启，调用

```
TXAIAudioSDK.getInstance().setAudioWakeupEnable(false);
```

后，唤醒模块停止工作。 我们需要不断将录制到的声音使用**TXAIAudioSDK.getInstance().feedRecordData(buffer)**传递给唤醒模块，进行检测，我们使用的声音源为16bit 16KHZ 单声道的PCM原始数据，并且需要自行实现回声消除和噪声抑制。

具体使用方法可以查阅Demo中的**MainService.java**。
