
# 腾讯应用云 Crash 接入指南

Crash 是腾讯云为移动开发者提供专业的异常上报和运营统计，帮助开发者快速发现并解决异常，同时掌握产品运营动态，及时跟进用户反馈。


## Andorid Studio 自动集成

### 修改 app 的 build.gradle 文件

用户需要在 app 的 build.gradle 文件中添加如下内容：
 
```
android {
    ......
    defaultConfig {

        // 官网上注册的包名。注意 application ID 和当前的应用包名以及官网上注册应用的包名必须一致。
        applicationId "你的包名" 
        ......

        ndk {
            //根据需要 自行选择添加的对应cpu类型的.so库。 
            abiFilters 'armeabi', 'armeabi-v7a', 'arm64-v8a' 
            // 还可以添加 'x86', 'x86_64', 'mips', 'mips64'
        }

        ......
    }
    ......
}

dependencies {
    ......
   
    
    compile 'com.tencent.tac:crash:1.0.0-release' 

}

```



## 启动 Crash 服务

集成好 Crash 服务后，用户需要自己启动 Crash 服务，具体代码如下：

```
// 首先获取 TACCrashService 实例
TACCrashService crashService = TACCrashService.getInstance();

// 调用 start 接口启动 Crash 服务，context 这里最好是使用应用 context。
crashService.start(context);

```




