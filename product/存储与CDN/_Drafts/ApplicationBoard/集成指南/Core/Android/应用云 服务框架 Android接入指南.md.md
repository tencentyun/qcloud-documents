### 集成SDK到你的应用

请修改您的 build.gradle 文件以加载应用云的配置。

1.应用级 build.gradle（\<project\>/\<app-module\>/build.gradle）：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:core:1.0.0'
}
```

2.按 IDE 中显示的栏中的“立即同步”：

![](https://www.gstatic.com/mobilesdk/160330_mobilesdk/images/android_studio_gradle_changed_butterbar@2x.png)


### 添加初始化代码

在你需要启动应用云服务前，调用以下代码初始化框架：

```
TACApplication.configure(context);
```

默认使用下发的配置文件初始化框架。如果需要动态修改配置，可以调用以下代码：

```
TACApplicationOptions applicationOptions = TACApplicationOptions.newDefaultOptions(this);

... // 调用子服务的参数，具体配置项请参考具体子服务的开发文档

TACApplication.configureWithOptions(this, applicationOptions);
```

