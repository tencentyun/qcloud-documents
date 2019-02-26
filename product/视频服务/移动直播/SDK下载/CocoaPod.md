## step1. 修改Podfile文件

修改 pod 所需的 Podfile 文件，增加腾讯云 LiteAV SDK 的pod路径，如下有两种设置方案：
```
注意：
TXLiteAVSDK_Smart 为 直播精简版，不支持点播缓存功能和点播flv播放。
TXLiteAVSDK_UGC 为 短视频功能版，不支持点播缓存功能和点播flv播放。
TXLiteAVSDK_Player 为 独立播放器版。
TXLiteAVSDK_Professional 为 全功能专业版。
TXLiteAVSDK_Professional_Rename 为 符号重命名版。
```

- **方案一：** 使用腾讯云提供的pod路径，该方案下载的是最新版本的SDK, 下载速度较快

```
platform :ios, '8.0'

target 'test' do

#pod 'TXLiteAVSDK_Smart', :podspec => 'http://pod-1252463788.cosgz.myqcloud.com/liteavsdkspec/TXLiteAVSDK_Smart.podspec'
#pod 'TXLiteAVSDK_UGC', :podspec => 'http://pod-1252463788.cosgz.myqcloud.com/liteavsdkspec/TXLiteAVSDK_UGC.podspec'
#pod 'TXLiteAVSDK_Player', :podspec => 'http://pod-1252463788.cosgz.myqcloud.com/liteavsdkspec/TXLiteAVSDK_Player.podspec'
pod 'TXLiteAVSDK_Professional', :podspec => 'http://pod-1252463788.cosgz.myqcloud.com/liteavsdkspec/TXLiteAVSDK_Professional.podspec'
#pod 'TXLiteAVSDK_Professional_Rename', :podspec => 'http://pod-1252463788.cosgz.myqcloud.com/liteavsdkspec/TXLiteAVSDK_Professional_Rename.podspec'

end

```

**- 方案二：** 使用pod官方的路径，支持选择版本号，比如 `pod 'TXLiteAVSDK_Professional', '3.9.2749'`

```
source 'https://github.com/CocoaPods/Specs.git'
platform :ios, '8.0'

target 'test' do

#pod 'TXLiteAVSDK_Smart'
#pod 'TXLiteAVSDK_UGC'
#pod 'TXLiteAVSDK_Player'
pod 'TXLiteAVSDK_Professional', '3.9.2749'
#pod 'TXLiteAVSDK_Professional_Rename'

end
```

## step2. 执行安装
命令行输入 pod install 执行安装，第一次执行会比较慢，因为会完整下载Zip 包并解压，后续有了缓存会很快。

```
pod install
```

或执行版本检查更新

```
pod update
```
