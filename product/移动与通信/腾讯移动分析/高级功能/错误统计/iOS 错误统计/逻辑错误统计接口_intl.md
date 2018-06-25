Error Statistics can be used to perform statistical analysis on the crash and logic errors of Apps. Crash is automatically captured and reported by MTA without calling additional API. However, users need to call relevant API to report log errors.
```obj-c
/**
Calculate logic errors of program
Logic errors only have description but not stack information

@param error Error description
*/
+ (void)trackError:(NSString *)error;

/**
Calculate logic errors of program
And specify the reporting method
Logic errors only have description but not stack information

@param error Error description
@param appkey If this parameter is not nil, report this appkey. Otherwise, report the appkey passed in startWithAppkey.
@param isRealTime Whether to enable real-time reporting. If it is set to YES, then report in real time and ignore global reporting policy. Otherwise, report according to the global policy.
*/
+ (void)trackError:(NSString *)error appkey:(NSString *)appkey isRealTime:(BOOL)isRealTime;

/**
Statistics exceptional
Exception message includes the cause of the exception and the stack

@param exception Exception message
*/
+ (void)trackException:(NSException *)exception;

/**
Statistics exceptional
And specify the reporting method
Exception message includes the cause of the exception and the stack

@param exception Exception message
@param appkey If this parameter is not nil, report this appkey. Otherwise, report the appkey passed in startWithAppkey.
@param isRealTime Whether to enable real-time reporting. If it is set to YES, then report in real time and ignore global reporting policy. Otherwise, report according to the global policy.
*/
+ (void)trackException:(NSException *)exception appkey:(NSString *)appkey isRealTime:(BOOL)isRealTime;
```
