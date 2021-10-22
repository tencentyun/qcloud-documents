## 什么是 TUIKit？
TUIKit 是基于 IM SDK 实现的一套 UI 组件，其包含会话、聊天、搜索、关系链、群组、音视频通话等功能，基于 UI 组件您可以像搭积木一样快速搭建起自己的业务逻辑。
<img style="width:800px" src="https://qcloudimg.tencent-cloud.cn/raw/bb1176efcf5d9242e6ee56f335fa9a62.jpg"  /> 

>?
>1、会话（TUIConversation），主要用于拉取和展示会话列表。
>2、搜索（TUISearch），主要用于搜索和展示会话或消息。
>3、聊天（TUIChat），主要用于收发和展示消息。
>4、音视频通话（TUICalling），主要用于音视频通话。
>5、关系链（TUIContact），主要用于拉取和展示好友列表。
>6、群组（TUIGroup），主要用于拉取和展示群信息。
## 如何集成 TUIKit？
### 开发环境要求
- Android Studio 3.6.1
- Gradle-5.1.1

### module 源码集成

[TUIKit 源码下载地址](https://github.com/tencentyun/TIMSDK/tree/master/Android)

1. 从 `GitHub` 下载 `Demo` 和 `TUIKit` 源码，把 `TUIKit` 文件夹拷贝到自己的工程目录下，跟 `Demo` 文件夹同级。

2. 在 `settings.gradle` 中添加：
```groovy
// 引入上层应用模块
include ':app'

// 引入内部组件通信模块 (必要模块)
include ':tuicore'
project(':tuicore').projectDir = new File(settingsDir, '../TUIKit/TUICore/tuicore')

// 引入聊天功能模块 (基础功能模块)
include ':tuichat'
project(':tuichat').projectDir = new File(settingsDir, '../TUIKit/TUIChat/tuichat')

// 引入关系链功能模块 (基础功能模块)
include ':tuicontact'
project(':tuicontact').projectDir = new File(settingsDir, '../TUIKit/TUIContact/tuicontact')

// 引入会话功能模块 (基础功能模块)
include ':tuiconversation'
project(':tuiconversation').projectDir = new File(settingsDir, '../TUIKit/TUIConversation/tuiconversation')

// 引入搜索功能模块（需要购买旗舰版套餐）
include ':tuisearch'
project(':tuisearch').projectDir = new File(settingsDir, '../TUIKit/TUISearch/tuisearch')

// 引入群组功能模块
include ':tuigroup'
project(':tuigroup').projectDir = new File(settingsDir, '../TUIKit/TUIGroup/tuigroup')

// 引入音视频通话功能模块
include ':tuicalling'
project(':tuicalling').projectDir = new File(settingsDir, '../TUIKit/TUICalling/tuicalling')
```
3. 在 `APP` 的 `build.gradle` 中添加:
```groovy
dependencies {
    api project(':tuiconversation')
    api project(':tuicontact')
    api project(':tuichat')
    api project(':tuisearch')
    api project(':tuigroup')
    api project(':tuicalling')    
}
```

4. 在 `gradle.properties` 文件中加入下行，表示自动转换三方库以兼容 `AndroidX`：
```properties
android.enableJetifier=true
```
5. 添加 `maven` 仓库，在 `root` 工程的 `build.gradle` 文件中添加：
```groovy
allprojects {
    repositories {
        mavenCentral()
        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }
    }
}
```
6. 同步工程，编译运行。