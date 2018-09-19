#### APIs
```objc
/**
 Enumerated values of API statistics
 */
typedef enum {
	/**
	 API call successful
	 */
	MTA_SUCCESS = 0,

	/**
	 API call failed
	 */
	MTA_FAILURE = 1,

	/**
	 A logic error occurred while calling the API
	 */
	MTA_LOGIC_FAILURE = 2
} MTAAppMonitorErrorType;


/**
 Data structure of API statistics
 */
@interface MTAAppMonitorStat : NSObject

/**
 Monitoring service API name
 */
@property (nonatomic, retain) NSString *interface;

/**
 Size of request package (in bytes)
 */
@property uint32_t requestPackageSize;

/**
 Size of response package (in bytes)
 */
@property uint32_t responsePackageSize;

/**
 Time taken for calling API (in ms)
 */
@property uint64_t consumedMilliseconds;

/**
 Response code returned by the service side
 */
@property int32_t returnCode;

/**
 Error code type
 */
@property MTAAppMonitorErrorType resultType;

/**
 Sampling rate of reporting (default is 0, which means no sample)
 */
@property uint32_t sampling;
@end

/**
 Generate statistics on the calls of network interface
 For more information on parameters, please see the description in data structure of API statistics.

 @param stat: API statistics. For more information, please see the description in data structure of API statistics.
 */
+ (void)reportAppMonitorStat:(MTAAppMonitorStat *)stat;

/**
 Generate statistics on the calls of network interface
 And specify the reporting method
 For more information on parameters, please see the description in data structure of API statistics.

 @param stat: API statistics. For more information, please see the description in data structure of API statistics.
 @param appkey: The appKey to be reported. If it is set to nil, report the appkey in the launch function
 @param isRealTime: Whether to report data in real time. If it is set to YES, data is reported in real time with global reporting policy ignored. Otherwise, data is reported according to the global policy.
 */
+ (void)reportAppMonitorStat:(MTAAppMonitorStat *)stat appkey:(NSString *)appkey isRealTime:(BOOL)isRealTime;
```
#### Example
```obj-c
-(IBAction) clickNormaltButton:(id)sender{
	MTAAppMonitorStat* stat = [[MTAAppMonitorStat alloc] init]; 
	[stat setInterface:@"interface1"];
	// ...
	[stat setRetsultType: SUCCESS];
	[MTA reportAppMonitorStat:stat];
}
```

