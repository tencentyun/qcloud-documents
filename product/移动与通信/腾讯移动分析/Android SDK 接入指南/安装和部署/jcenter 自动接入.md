AndroidStudio 上可以使用 jcenter 远程仓库自动接入，不需要在项目中导入 jar 包和 so 文件，在 AndroidManifest.xml 中不需要配置 MTA 相关的内容，jcenter 会自动导入（升级 SDK 删除老版本 SDK 的配置）。
在 app build.gradle 文件下配置以下内容：

```
android {
......
defaultConfig {
applicationId "你的包名"
......

ndk {
//根据需要 自行选择添加的对应cpu类型的.so库。
abiFilters 'armeabi', 'armeabi-v7a', 'arm64-v8a'
// 还可以添加 'x86', 'x86_64', 'mips', 'mips64'
}

manifestPlaceholders = [
MTA_APPKEY:"注册应用的appkey",
MTA_CHANNEL:"渠道名称"
]
......
}
......
}

dependencies {
......

// mta包稳定版和测试版本二选一，mid包必须要添加 ，可视化埋点根据需要添加
//mta 3.2 稳定版
compile 'com.qq.mta:mta:3.2.1-release'
//mid  jar包 必须添加
compile 'com.tencent.mid:mid:3.73-release'
//可视化埋点的相关jar包 （根据需要添加），可视化埋点的版本号，和必须和当前MTA的版本号必须匹配使用 需要在配置文件中增加配置，具体请参考 高级功能中可视化埋点的接入。
compile 'com.qq.visual:visual:1.0.8-release'
......
}
```

>**注意：**
>如果在添加以上 abiFilter 配置之后android Studio出现以下提示：
>NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin，则在 Project 根目录的 gradle.properties 文件中添加 android.useDeprecatedNdk=true。
