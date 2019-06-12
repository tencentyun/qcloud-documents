### 请问游戏多媒体引擎 Demo 及 SDK 在哪里下载？

请在 [下载指引](https://cloud.tencent.com/document/product/607/18521) 下载相关 Demo 及 SDK。目前官网上有 Unity 引擎 Demo，Cocos2D 引擎 Demo，Android 原生开发 Demo 及 iOS 原生开发 Demo。

### 游戏多媒体引擎 Demo 下载后如果要换为自己申请的账号可以吗？
- 可以，需要在控制台获取两个号码，分别为 sdkappid、权限密钥。
- 使用客户自己申请的 appid 的话需要在 AVChatViewController 中的 GetAuthBuffer 中修改实时语音的 Key。

### 在使用 Demo 的时候报错：errinfo=priv map info error。怎么办？
相关进房参数出现错误，请检查 sdkappid、权限密钥 是否已经替换。



### 如何取得日志？
QAVSDK_带日期 .log，这个文件为日志文件。目录如下：

| 平台    | 路径                                                         |
| ------- | ------------------------------------------------------------ |
| Windows | %appdata%\Tencent\GME\ProcessName                            |
| iOS     | Application/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/Documents   |
| Android | /sdcard/Android/data/xxx.xxx.xxx/files                       |
| Mac     | /Users/username/Library/Containers/xxx.xxx.xxx/Data/Documents |

### 声音卡顿的主要原因？
-  **音乐卡：**主播使用外放的设备播音乐，然后通过另一个手机采集并主播（这里会必现卡顿，可建议主播带耳机）。
-  **网络卡：**上行丢包率过高或者上行延时波动较大情况下观众会听到卡顿。


### 下载 iOS Demo 之后无法运行
下载官方 iOS Demo 后，在 Xcode（版本为10以上） 编译时出现类似“ld: warning: directory not found for option”等错误，需手动将 Demo 同级目录下的 “GME_SDK” 文件夹下的 “GMESDK.framework” 文件添加到工程的 Framework 列表中。


### 下载 Unity Demo 导出可执行文件时报错
如果使用过程中有 Found plugins with same names and architectures 类似报错，是因为GME SDK 默认提供 x86 架构的 SDK 版本及 x86_64 架构的 SDK 版本，请在 plugins 文件夹中删除其中一份。