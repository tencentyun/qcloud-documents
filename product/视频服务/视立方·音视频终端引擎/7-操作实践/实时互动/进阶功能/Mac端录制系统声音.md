## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | -  | &#10003;  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 场景痛点及解决方案

在屏幕分享等应用场景中，常需要共享系统音频给对方，而 Mac 电脑默认声卡不支持采集系统音频，所以在 Mac 电脑上共享系统音频比较困难。基于此，音视频通话TRTC 提供了在 Mac 端录制系统音频的功能来满足该场景需求，具体接入步骤见下文。

## 集成说明

[](id:step1)
### 步骤1：集成 TRTCPrivilegedTask 库  

SDK 需要使用 [TRTCPrivilegedTask](https://liteavsdk-1252463788.cos.ap-guangzhou.myqcloud.com/TRTCPrivilegedTask/TRTCPrivilegedTask.tar.bz2) 库来获取 root 权限，从而将虚拟声卡插件 TRTCAudioPlugin.driver 安装至系统目录 `/Library/Audio/Plug-Ins/HAL` 。

<dx-tabs>
::: 使用CocoaPods集成  
1. 打开您当前项目根目录下的 `Podfile` 文件，添加下面的内容：
<dx-codeblock>
::: ruby ruby
platform :osx, '10.10'	

target 'Your Target' do
    pod 'TRTCPrivilegedTask', :podspec => 'https://pod-1252463788.cos.ap-guangzhou.myqcloud.com/liteavsdkspec/TRTCPrivilegedTask.podspec'
end
:::
</dx-codeblock>
2. 执行 `pod install` 命令安装 **TRTCPrivilegedTask** 库。

>?
>- 如果项目根目录下没有 `Podfile` 文件，请先执行 `pod init` 命令新建文件再添加以下内容。
>-  CocoaPods 的安装方法，请参见  [CocoaPods 官网安装说明](https://guides.cocoapods.org/using/getting-started.html)。
:::
::: 手动集成
1. 下载 [TRTCPrivilegedTask](https://liteavsdk-1252463788.cos.ap-guangzhou.myqcloud.com/TRTCPrivilegedTask/TRTCPrivilegedTask.tar.bz2) 库。
2. 打开您的 Xcode 工程项目，导入解压后的文件 libPrivilegedTask.a 到您的工程。
3. 选择要运行的 target，选中 Build Phases 项，展开Link Binary with Libraries 项，单击底下的【+】，添加依赖库 `libPrivilegedTask.a`。  
![libPrivilegedTask.a](https://main.qcloudimg.com/raw/cc5b3365e72cee80cda7f0db0a4e1b62.png)  
:::
</dx-tabs> 


[](id:step2)
### 步骤2：取消 App Sandbox 功能  
在 App 的 entitlements 描述文件中，删除 **App Sandbox** 条目。  
![Sandbox](https://main.qcloudimg.com/raw/98fed5571040f24c2891f4b87ddce15e.png)  


[](id:step3)
### 步骤3：虚拟声卡插件打包  
在 [集成 TRTCPrivilegedTask 库](#step1) 和 [取消 App Sandbox 功能](#step2) 后，首次使用系统音频录制功能时，SDK 会从网络下载虚拟声卡插件并安装。如果想加速这个过程，可以将放置在 `TXLiteAVSDK_TRTC_Mac.framework` 的 PlugIns 目录下的虚拟声卡插件 `TRTCAudioPlugin.driver` 打包至 App Bundle 的 Resources 目录。如下图：  
![打包插件](https://main.qcloudimg.com/raw/b04b805d4848f2ecd6fd7dcc83176a9e.png)
或者拷贝至 App Bundle 的 PlugIns 目录。如下图：  
![打包插件2](https://main.qcloudimg.com/raw/05fb5c6ec4dba74c3b5fb880ed28033e.png)  


[](id:step4)
### 步骤4：开始系统声音采集  
调用 [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2979e32c019708dcc9209bb6d2db9486) 接口开始系统声音采集，并将其混入上行音频流中，接口执行完成会通过 [onSystemAudioLoopbackError](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a8644f5136138d13ffa8e0ea68f5c3676) 回调成功或失败的结果。
```Objective-C
TRTCCloud *trtcCloud = [TRTCCloud sharedInstance];
[trtcCloud startLocalAudio];
[trtcCloud startSystemAudioLoopback];
```

>! 集成 TRTCPrivilegedTask 库和取消 App Sandbox 功能后，首次调用 startSystemAudioLoopback 会获取 root 权限。如下图：  
>![权限请求框](https://main.qcloudimg.com/raw/c6507054c395f9372246bfc3498f5086.png)  
>在用户单击【好】后，开始自动安装虚拟声卡插件。



[](id:step5)

### 步骤5：停止系统声音采集 

调用 [stopSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2979e32c019708dcc9209bb6d2db9486) 接口停止系统声音采集。

```Objective-C
TRTCCloud *trtcCloud = [TRTCCloud sharedInstance];
[trtcCloud stopSystemAudioLoopback];
```

[](id:step6)
### 步骤6：设置系统声音采集音量

调用 [setSystemAudioLoopbackVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2979e32c019708dcc9209bb6d2db9486) 接口设置系统声音的采集音量。

```Objective-C
TRTCCloud *trtcCloud = [TRTCCloud sharedInstance];
[trtcCloud setSystemAudioLoopbackVolume:80];
```

## 集成小结

- 音视频通话TRTC 在 Mac 端是通过虚拟声卡插件 `TRTCAudioPlugin.driver` 来录制系统音频。这个虚拟声卡插件需要拷贝至系统目录 `/Library/Audio/Plug-Ins/HAL` 并重启音频服务后生效。 可以通过 `启动台` 的 `其他`  文件夹中 `音频 MIDI 设置`  应用来检查虚拟声卡插件是否安装成功。在该应用的设备列表中，有名称为 “TRTC Audio Device” 的设备即表明 TRTC 的虚拟声卡插件安装成功。  
- 上述步骤中的 [集成 TRTCPrivilegedTask 库](#step1) 和 [取消 App Sandbox 功能](#step2) 是为 TRTC SDK 自动安装虚拟声卡插件提供 root 权限。如不集成 TRTCPrivilegedTask 库并保留 App Sandbox 功能， SDK 不会自动安装自动安装虚拟声卡插件，但如果系统中已安装好虚拟声卡插件，录制系统音频的功能仍然可以正常使用。
> ? 除上述方案外，也可以手动安装虚拟声卡插件来集成该功能：
> 1. 将放置在 `TXLiteAVSDK_TRTC_Mac.framework` 的 PlugIns 目录下的 `TRTCAudioPlugin.driver` 拷贝至系统目录  `/Library/Audio/Plug-Ins/HAL`。
> 2. 重启系统的音频服务。 
><dx-codeblock>
::: 重启系统的音频服务 bash
 sudo cp -R TXLiteAVSDK_TRTC_Mac.framework/PlugIns/TRTCAudioPlugin.driver /Library/Audio/Plug-Ins/HAL  
 sudo kill -9 `ps ax|grep 'coreaudio[a-z]' |awk '{print $1}'`
:::
</dx-codeblock>


[](id:note)
## 注意事项
- App Sandbox 功能取消后，App 内获取到的用户路径会发生变化。  
通过 NSSearchPathForDirectoriesInDomains 等系统方法获取到的 ` ~/Documents`、 `~/Library` 等目录会从沙盒目录切换成用户目录 `/Users/用户名/Documents`、 `/Users/用户名/Library`。
- 集成 TRTCPrivilegedTask 库，可能会使 App 无法上架到 Mac App Store。  
SDK 自动安装虚拟声卡插件时需要关闭 App Sandbox 功能，并获取 root 权限，App 可能会无法上架到 Mac App Store。详情请参见  [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/#hardware-compatibility) 。  
如需上架 App Store 或者使用 Sandbox 功能，建议选择手动安装虚拟音频插件的方案。  
