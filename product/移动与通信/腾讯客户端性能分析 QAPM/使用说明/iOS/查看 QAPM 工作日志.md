```
void loggerFunc(QAPMLoggerLevel level, const char* log) {
    
    NSLog(@"log level: %zd, log info:%s", level, log);
    
    if (level == QAPMLogLevel_Event) { ///外发版本 log

    } else if (level == QAPMLogLevel_Info) { ///灰度和内部版本 log

    } else if (level == QAPMLogLevel_Debug) { ///内部版本 log
        
    }
}


- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    /********************************  设置 QAPM 日志回调 ****************/
    [QAPMPerformanceProfile registerLogCallback: loggerFunc];
}
```
