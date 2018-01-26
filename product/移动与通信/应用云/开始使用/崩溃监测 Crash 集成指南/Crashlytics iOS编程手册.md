# 应用云 Crashlytics 服务 iOS 编程手册

## 服务启动与停止

当您集成了 Crashlytics 服务之后，系统将会在程序启动的时候自动启动服务。

如果您不希望在启动的时候默认启动 Crashlytics 服务，您可以在配置中设置关掉 (例如在AppDelegate中加入如下代码).

~~~
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
    options.crashOptions.enable = NO;
~~~


## 手动上报异常


~~~
/**
 上报异常信息

 @param exception 异常
 */
- (void) reportException:(NSException*)exception;

~~~


## 其他功能

其他功能请参考 TACCrashService.h 中的定义