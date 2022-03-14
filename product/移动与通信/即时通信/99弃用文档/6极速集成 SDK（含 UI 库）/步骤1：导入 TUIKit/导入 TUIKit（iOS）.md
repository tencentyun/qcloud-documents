## 什么是 TUIKit？
TUIKit 是基于 IM SDK 实现的一套 UI 组件，其包含会话、聊天、搜索、关系链、群组、音视频通话等功能，基于 UI 组件您可以像搭积木一样快速搭建起自己的业务逻辑。
![](https://qcloudimg.tencent-cloud.cn/raw/0a88fefe060ab42d4422cdff6d869937.jpg)

>?
>1. 会话（TUIConversation），主要用于拉取和展示会话列表。
>2. 搜索（TUISearch），主要用于搜索和展示会话或消息。
>3. 聊天（TUIChat），主要用于收发和展示消息。
>4. 音视频通话（TUICalling），主要用于音视频通话。
>5. 关系链（TUIContact），主要用于拉取和展示好友列表。
>6. 群组（TUIGroup），主要用于拉取和展示群信息。

## 如何集成 TUIKit？

### 开发环境要求

- Xcode 10 及以上
- iOS 9.0 及以上
>?更多实操教学视频请参见：[极速集成 TUIKit（iOS）](https://cloud.tencent.com/edu/learning/course-3130-56699)。

### CocoaPods 集成

`TUIKit` 从 5.7.1435 版本开始支持模块化集成，您可以根据自己的需求选择所需模块集成。

<ol><li>在 Podfile 中增加以下内容。
```
# 防止 TUI 组件里的 *.xcassets 与您项目里面冲突。
install! 'cocoapods', :disable_input_output_paths => true  

# TUI 组件依赖了静态库，需要屏蔽如下设置，如果报错，请参考常见问题说明。
# use_frameworks!

# 集成聊天功能
pod 'TUIChat'
# 集成会话功能
pod 'TUIConversation'
# 集成关系链功能
pod 'TUIContact'
# 集成群组功能
pod 'TUIGroup'
# 集成搜索功能（需要购买旗舰版套餐）
pod 'TUISearch'
# 集成音视频通话功能
pod 'TUICalling'
```

>! 腾讯云的 [音视频库](https://cloud.tencent.com/document/product/647/32689) 不能同时集成，会有符号冲突，如果您使用了非 [TRTC](https://cloud.tencent.com/document/product/647/32689#TRTC) 版本的音视频库，音视频通话建议 pod 集成 `TUICalling/Professional` 版本，该版本依赖的 [LiteAV_Professional](https://cloud.tencent.com/document/product/647/32689#.E4.B8.93.E4.B8.9A.E7.89.88.EF.BC.88professional.EF.BC.89) 音视频库包含了音视频的所有基础能力。

<li> 执行以下命令，安装 TUI 组件。<br>
```bash
pod install
```
 如果无法安装 TUIKit 最新版本，执行以下命令更新本地的 CocoaPods 仓库列表。<br>
 
```bash
 pod repo update
```

<li> TUI 组件集成后效果。<br>

![](https://qcloudimg.tencent-cloud.cn/raw/083905832dcc7f8cc1d14ddaf15232e9.jpg)

>? TUI 组件集成后支持文件夹分层显示，方便您阅读和修改源代码。
</ol></li>

## 常见问题

### 1. target has transitive dependencies that include statically linked binaries

如果在 pod 过程中出现该错误，是因为`TUIKit`使用到了第三方静态库，需要在 podfile 中注释掉 `use_frameworks!`。

如果在某种情况下，需要使用`use_frameworks!`，则请使用`cocoapods 1.9.0`及以上版本进行 `pod install`，并修改为：

```
use_frameworks! :linkage => :static
```

如果您使用的是 `swift`，请将头文件引用改成 @import 模块名形式引用。
