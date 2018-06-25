You can use remote jcenter warehouse to connect Android Studio without importing any jar packages and so files in the project. You also do not need to configure MTA-related information in AndroidManifest.xml, because jcenter will import it automatically (by upgrading the SDK while deleting configurations of the old version).
Configure the followings in the app build.gradle file:

```
android {
......
defaultConfig {
applicationId "your package name"
......

ndk {
//Add the .so library for cpu as needed.
abiFilters 'armeabi', 'armeabi-v7a', 'arm64-v8a'
//You can also add 'x86', 'x86_64', 'mips', and 'mips64'
}

manifestPlaceholders = [
MTA_APPKEY:"appkey of the registered App",
MTA_CHANNEL:"Channel name"
]
......
}
......
}

dependencies {
......

// Choose either stable version or test version of mta package. mid package must be added, and visualized event tracking can be added as needed.
//Stable version of mta 3.2
compile 'com.qq.mta:mta:3.2.1-release'
//mid jar package must be added
compile 'com.tencent.mid:mid:3.73-release'
//The jar package (added as needed) and the version number of visualized event tracking must match with the current MTA version number. For more information on how to add configurations in the configuration file, please see Integrating Visualized Event Tracking in Advanced Features.
compile 'com.qq.visual:visual:1.0.8-release'
......
}
```

>**Note:**
>If the following prompt appears on Android Studio after you add the above abiFilter configurations:
>NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin, add android.useDeprecatedNdk=true to the gradle.properties file in the Project root directory.

