## 场景痛点及解决方案
在屏幕分享等应用场景中，常需要共享系统音频给对方，而采用 Electron 打包 Mac 应用时，Mac 电脑默认声卡不支持采集系统音频，所以在 Mac 电脑上共享系统音频比较困难。基于此，TRTC 提供了在 Mac 端录制系统音频的功能来满足该场景需求，具体接入步骤见下文。

[](id:step1)
### 步骤1：开始系统声音采集

调用 [startSystemAudioLoopback](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startSystemAudioLoopback) 接口开始系统声音采集，并将其混入上行音频流中，接口执行完成会通过 [onSystemAudioLoopbackError](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onSystemAudioLoopbackError) 回调成功或失败的结果。
```javascript
import TRTCCloud, { TRTCAudioQuality } from 'trtc-electron-sdk';
const rtcCloud = new TRTCCloud();
function onSystemAudioLoopbackError(errCode) {
  if (errCode === 0) {
    console.log('启动成功');
  }
  if (errCode === -1330) {
    console.log('开启系统声音录制失败，例如音频驱动插件不可用');
  }
  if (errCode === -1331) {
    console.log('未授权安装音频驱动插件');
  }
  if (errCode === -1332) {
    console.log('安装音频驱动插件失败');
  }
}

trtcCloud.on('onSystemAudioLoopbackError', onSystemAudioLoopbackError);
trtcCloud.startLocalAudio(TRTCAudioQuality.TRTCAudioQualityDefault);
trtcCloud.startSystemAudioLoopback();


```

>! 首次调用 startSystemAudioLoopback 会获取 root 权限（如下图），  在用户单击**好**后，开始自动安装虚拟声卡插件。
>![权限请求框](https://main.qcloudimg.com/raw/c6507054c395f9372246bfc3498f5086.png)  

[](id:step2)
 
### 步骤2：停止系统声音采集 
调用 [stopSystemAudioLoopback](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopSystemAudioLoopback) 接口停止系统声音采集。
```javascript
trtcCloud.stopSystemAudioLoopback();
```

[](id:step3)
### 步骤3：设置系统声音采集音量
调用 [setSystemAudioLoopbackVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setSystemAudioLoopbackVolume) 接口设置系统声音的采集音量。

```javascript
trtcCloud.setSystemAudioLoopbackVolume(60);
```

## 集成小结
TRTC 在 Mac 端是通过虚拟声卡插件 `TRTCAudioPlugin.driver` 来录制系统音频。这个虚拟声卡插件需要拷贝至系统目录 `/Library/Audio/Plug-Ins/HAL` 并重启音频服务后生效。 可以通过 `启动台` 的 `其他`  文件夹中 `音频 MIDI 设置`  应用来检查虚拟声卡插件是否安装成功。在该应用的设备列表中，有名称为 “TRTC Audio Device” 的设备即表明 TRTC 的虚拟声卡插件安装成功。  
