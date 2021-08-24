
### 如何下载 GME Demo 及 SDK？

下载 GME 相关的 Demo 及 SDK，详情请参见 [下载指引](https://cloud.tencent.com/document/product/607/18521) 。目前官网有 Unity 引擎 Demo、Cocos2D 引擎 Demo、Android 及 iOS 原生开发 Demo。

### GME 的 Windows Demo 应该使用什么版本的 VS 打开？
请使用 VS2015 打开。如果需要用 VS2010 打开则请自行对工程进行降级。

### GME Demo 下载后，如何替换为自己申请的账号？

- 需要在 [控制台](https://console.cloud.tencent.com/gamegme/detail/1400391524) 服务管理中获取 AppID 和权限密钥。
- 若使用您申请的 AppID ，则需要在 AVChatViewController 中的 GetAuthBuffer 中修改实时语音的 Key。

### GME 可以只使用一个 OpenId 吗？

初始化 GME 引擎时候将会使用到 OpenId，OpenId 是用户的唯一标识。多端同时使用一个 OpenId，例如异地多端登录，会造成账号异常，无法正常使用 GME 功能。

### 房间内只有一个人，如何在本地体验效果？

请在另一个终端设备使用 demo 进入同一房间即可。

### 使用 Demo 时，报错：errinfo=priv map info error，怎么办？

相关进房参数出现错误，请检查 SDKAppID、权限密钥是否已经替换。

### 如何使用已下载的 Demo？

- 您可以请参见 [Demo 使用文档](https://cloud.tencent.com/document/product/607/43120)。
- 如果是 Unity Demo，请参见 [Unity Demo 使用](https://cloud.tencent.com/document/product/607/48323)。

### Unity 导出的 Demo 为何使用时候经常无声？
Unity 的 Demo 中设置了  OnApplicationFocus，当程序失去焦点时，会 Pause 暂停语音，如果需要后台可播放声音，请将调用 Pause 接口的相关代码去掉即可。

### 如何取得日志？

**提供日志的时候，请同时提供出现问题的相关时间点**
`QAVSDK_` 带日期的 `.log` 文件为日志文件。目录如下：

| 平台    | 路径                                                         |
| ------- | ------------------------------------------------------------ |
| Windows | %appdata%\Tencent\GME\ProcessName                            |
| iOS     | Application/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/Documents   |
| Android | /sdcard/Android/data/xxx.xxx.xxx/files                       |
| Mac     | /Users/username/Library/Containers/xxx.xxx.xxx/Data/Documents |

如果是使用 Unity 引擎，并且在 PC 端开发，可以尝试在 `%appdata%\Tencent\GME\Unity.exe` 路径下找到日志。

在 iOS 真机上，可以通过应用程序支持文件共享来取得日志，具体步骤如下：
1. 在应用程序的 `Info.plist` 文件中添加 UIFileSharingEnabled 键，并将键值设置为“YES”。
2. 将您希望共享的文件放在应用程序的 Documents 目录下。
3. 一旦设备插入到用户计算机，iTunes 就会在选中设备的 Apps 标签中显示一个 File Sharing 区域。
4. 此后，用户就可以向该目录添加文件或者将文件移动到桌面计算机中。

**日志等级**

提供日志时如果有调用过 SetLogLevel 设置的日志等级，建议恢复默认日志等级。
