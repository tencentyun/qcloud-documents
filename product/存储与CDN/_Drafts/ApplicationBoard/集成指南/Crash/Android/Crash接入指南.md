
# 应用云 Crash 服务 Android 接入指南

Crash 服务是腾讯云为移动开发者提供专业的异常上报和运营统计，帮助开发者快速发现并解决异常，同时掌握产品运营动态，及时跟进用户反馈。


## 集成 Crash 服务到你的应用

### 添加 Crash 服务依赖

你需要在 module 下的 build.gradle 添加依赖：

```

dependencies {
    ......
    
    compile 'com.tencent.tac:crash:1.0.0' 

}

```

### 添加符号表和mapping文件上传插件

如果你使用了 so 文件或者对代码进行了混淆，那么需要添加插件来上传符号表和mapping文件。

1、在项目根目录下的 build.gradle 文件中添加依赖

```
buildscript {
	 ......
	 
    dependencies {
        ......
        
        classpath 'com.tencent.tac:crash-plugin:1.0.0'
    }
}

```

2、在 module 下的 build.gradle 文件中添加插件

```
......
 
apply plugin: 'com.tencent.tac.crash'

```

## 启动 Crash 服务

集成好 Crash 服务后，你可以很方便的启动 Crash 服务，具体代码如下：

```
// 首先获取 TACCrashService 实例
TACCrashService crashService = TACCrashService.getInstance();

// 调用 start 接口启动 Crash 服务，context 这里最好是使用 application context。
crashService.start(context);

```

## 高级功能

### 设置用户场景

你可以在应用运行的过程中设置当前用户场景，应用 crash 后，Crash 服务会将当前设置的场景信息进行上报。

```
int tag = 1;
crashService.seUserSceneTag(context, tag); // 设置用户场景
``` 

### 添加自定义信息

你可以添加自定义数据，应用 crash 后，Crash 服务会自动上报这些数据。

```
String key = "userName";
String value = "xiaoming";

crashService.putUserData(context, key, value); // 添加自定义数据
```

当然你也可以查询或者删除自定义数据：

```
String name = crashService.getUserData(context, key); // 查询自定义数据

crashService.removeUserData(context, key); // 删除自定义数据
```


