#### 接口
```objc
/**
 接口统计的枚举值
 */
typedef enum {
	/**
	 接口调用成功
	 */
	MTA_SUCCESS = 0,

	/**
	 接口调用失败
	 */
	MTA_FAILURE = 1,

	/**
	 接口调用出现逻辑错误
	 */
	MTA_LOGIC_FAILURE = 2
} MTAAppMonitorErrorType;


/**
 接口统计的数据结构
 */
@interface MTAAppMonitorStat : NSObject

/**
 监控业务接口名
 */
@property (nonatomic, retain) NSString *interface;

/**
 上传请求包量，单位字节
 */
@property uint32_t requestPackageSize;

/**
 接收应答包量，单位字节
 */
@property uint32_t responsePackageSize;

/**
 消耗的时间，单位毫秒
 */
@property uint64_t consumedMilliseconds;

/**
 业务返回的应答码
 */
@property int32_t returnCode;

/**
 业务返回类型
 */
@property MTAAppMonitorErrorType resultType;

/**
 上报采样率，默认0含义为无采样
 */
@property uint32_t sampling;
@end

/**
 对网络接口的调用情况进行统计
 参数的详细信息请看接口统计数据结构中的相关说明

 @param stat 接口统计的数据，详情请看接口统计数据结构的相关说明
 */
+ (void)reportAppMonitorStat:(MTAAppMonitorStat *)stat;

/**
 对网络接口的调用情况进行统计
 并指定上报方式
 参数的详细信息请看接口统计数据结构中的相关说明

 @param stat 接口统计的数据，详情请看接口统计数据结构的相关说明
 @param appkey 需要上报的appKey，若传入nil，则上报到启动函数中的appkey
 @param isRealTime 是否实时上报，若传入YES，则忽略全局上报策略实时上报。否则按照全局策略上报。
 */
+ (void)reportAppMonitorStat:(MTAAppMonitorStat *)stat appkey:(NSString *)appkey isRealTime:(BOOL)isRealTime;
```
#### 示例
```obj-c
-(IBAction) clickNormaltButton:(id)sender{
	MTAAppMonitorStat* stat = [[MTAAppMonitorStat alloc] init]; 
	[stat setInterface:@"interface1"];
	// ...
	[stat setRetsultType: SUCCESS];
	[MTA reportAppMonitorStat:stat];
}
```
