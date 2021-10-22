## 开发环境要求

- Android Studio 3.6.1
- Gradle-5.1.1


## 集成说明

 `TUIKit` 支持以 `module` 源码的方式集成。

### module 源码集成
[TUIKit 源码下载地址](https://github.com/tencentyun/TIMSDK/tree/master/Android)

1. 从 `GitHub` 下载 `Demo` 和 `TUIKit` 源码，把 `TUIKit` 文件夹拷贝到自己的工程目录下，跟 `Demo` 文件夹同级。

2. 在 `settings.gradle` 中添加：
```groovy
// 引入上层应用模块
include ':app'

// 引入组件集成模块
include ':tuikit'
project(':tuikit').projectDir = new File(settingsDir, '../TUIKit/TUIKit')

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

// 引入搜索功能模块
include ':tuisearch'
project(':tuisearch').projectDir = new File(settingsDir, '../TUIKit/TUISearch/tuisearch')

// 引入群组功能模块
include ':tuigroup'
project(':tuigroup').projectDir = new File(settingsDir, '../TUIKit/TUIGroup/tuigroup')

// 引入音视频通话功能模块
include ':tuicalling'
project(':tuicalling').projectDir = new File(settingsDir, '../TUIKit/TUICalling/tuicalling')

// 引入群直播功能模块
include ':tuilive'

```
3. 在 `APP` 的 `build.gradle` 中添加:
```groovy
dependencies {
    implementation project(':tuikit')
    
    ......
}
```
4. 修改 `tuikit` 的 `build.gradle` 文件，替换其中的几个版本号为 `app` 的 `build.gradle` 中的版本号，例如：
```groovy
android {
    compileSdkVersion 30

    defaultConfig {
        minSdkVersion 19
        targetSdkVersion 30
        versionCode 1
        versionName "1.0"
    }

   ......
}
```

5. 在 `gradle.properties` 文件中加入下行，表示自动转换三方库以兼容 `AndroidX`：
```properties
android.enableJetifier=true
```
6. 添加 `maven` 仓库，在 `root` 工程的 `build.gradle` 文件中添加：
```groovy
allprojects {
    repositories {
        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }

        ......
    }
}
```
7. 同步工程，编译运行。

### 模块动态集成
TUIKit 已经实现组件化，支持模块动态集成。

比如，如果您不需要搜索功能，那么只需要在 `tuikit 模块` 的 `build.gradle` 文件中删除下面一行即可：
```groovy
api project(':tuisearch')
```
这样在会话列表界面就不会出现搜索框，如下图所示：

<img src="https://main.qcloudimg.com/raw/2f46dc63648c6d58971c757d844828fb.png" width="500"/>

同样的，如果您不需要音视频通话功能，只需要在 `tuikit 模块` 的 `build.gradle` 文件中删除音视频通话模块集成代码即可：
```groovy
api project(':tuicalling')
```
这样，就不再集成音视频通话功能，聊天页面的更多输入界面就不再出现音视频通话按钮：

<img src="https://main.qcloudimg.com/raw/24fa3b50325f158489fda04556c79329.png" width="500"/>

&nbsp;

## 常见问题

### **Cannot get property 'compileSdkVersion' on extra properties extension as it dose not exist**

如果在同步工程过程中出现该错误，是因为 Demo 工程中 `tuikit` 模块的 `compileSdkVersion` 等版本号都跟随 `app` 模块的版本号，只需要把 `tuikit` 模块的 `build.gradle` 文件中的几个版本号替换为自己工程下 `app` 模块的 `build.gradle` 文件中的版本号即可。例如：
```
android {
    compileSdkVersion rootProject.ext.compileSdkVersion

    defaultConfig {
        minSdkVersion 19
        targetSdkVersion rootProject.ext.targetSdkVersion
        versionCode rootProject.ext.versionCode
        versionName rootProject.ext.versionName

    }

    ......
}
```
替换为：
```groovy
android {
    compileSdkVersion 30

    defaultConfig {
        minSdkVersion 19
        targetSdkVersion 30
        versionCode 1
        versionName "1.0"
    }

   ......
}
```