### NSDictionary 为参数的自定义事件

```obj-c
/**
 上报自定义事件

 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param kvs 事件的参数，参数需要先在MTA前台配置好才能生效
 */
+ (void)trackCustomKeyValueEvent:(NSString *)event_id props:(NSDictionary *)kvs;

/**
 上报自定义事件
 并且指定上报方式

 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param kvs 事件的参数，参数需要先在MTA前台配置好才能生效
 @param appkey 需要上报的appKey，若传入nil，则上报到启动函数中的appkey
 @param isRealTime 是否实时上报，若传入YES，则忽略全局上报策略实时上报。否则按照全局策略上报。
 */
+ (void)trackCustomKeyValueEvent:(NSString *)event_id
	props:(NSDictionary *)kvs
	appkey:(NSString *)appkey
	isRealTime:(BOOL)isRealTime;

/**
 开始统计自定义时长事件
 此接口需要跟trackCustomKeyValueEventEnd配对使用
 多次调用以第一次开始时间为准

 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param kvs 事件的参数，参数需要先在MTA前台配置好才能生效
 */
+ (void)trackCustomKeyValueEventBegin:(NSString *)event_id props:(NSDictionary *)kvs;

/**
 开始统计自定义时长事件
 并指定上报方式
 此接口需要跟trackCustomKeyValueEventEnd配对使用
 多次调用以第一次开始时间为准

 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param kvs 事件的参数，参数需要先在MTA前台配置好才能生效
 @param appkey 需要上报的appKey，若传入nil，则上报到启动函数中的appkey
 */
+ (void)trackCustomKeyValueEventBegin:(NSString *)event_id
	props:(NSDictionary *)kvs
	appkey:(NSString *)appkey;

/**
 结束统计自定义时长事件
 此接口需要跟trackCustomKeyValueEventBegin配对使用
 多次调用以第一次结束时间为准

 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param kvs 事件的参数，参数需要先在MTA前台配置好才能生效
 			参数中的key和value必须跟开始统计时传入的参数一样才能正常配对
 */
+ (void)trackCustomKeyValueEventEnd:(NSString *)event_id props:(NSDictionary *)kvs;

/**
 结束上报自定义时长事件
 并指定上报方式
 此接口需要跟trackCustomKeyValueEventBegin配对使用
 多次调用以第一次结束时间为准

 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param kvs 事件的参数，参数需要先在MTA前台配置好才能生效
 			参数中的key和value必须跟开始统计时传入的参数一样才能正常配对
 @param appkey 需要上报的appKey，若传入nil，则上报到启动函数中的appkey
 @param isRealTime 是否实时上报，若传入YES，则忽略全局上报策略实时上报。否则按照全局策略上报。
 */
+ (void)trackCustomKeyValueEventEnd:(NSString *)event_id
	props:(NSDictionary *)kvs
	appkey:(NSString *)appkey
	isRealTime:(BOOL)isRealTime;


/**
 直接统计自定义时长事件
 这个方法用于上报统计好的时长事件

 @param seconds 自定义事件的时长，单位秒
 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param kvs 事件的参数，参数需要先在MTA前台配置好才能生效
 */
+ (void)trackCustomKeyValueEventDuration:(uint32_t)seconds
	withEventid:(NSString *)event_id
	props:(NSDictionary *)kvs;

/**
 直接上报自定义时长事件
 并指定上报方式
 这个方法用于上报统计好的时长事件

 @param seconds 自定义事件的时长，单位秒
 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param kvs 事件的参数，参数需要先在MTA前台配置好才能生效
 @param appkey 需要上报的appKey，若传入nil，则上报到启动函数中的appkey
 @param isRealTime 是否实时上报，若传入YES，则忽略全局上报策略实时上报。否则按照全局策略上报。
 */
+ (void)trackCustomKeyValueEventDuration:(uint32_t)seconds
	withEventid:(NSString *)event_id
	props:(NSDictionary *)kvs
	appKey:(NSString *)appkey
	isRealTime:(BOOL)isRealTime;
```
**示例**

```obj-c
// 次数统计
- (IBAction)clickKVButton:(id)sender {
	[MTA trackCustomKeyValueEvent:@"KVEvent"
		props:[NSDictionary dictionaryWithObject:@"Value" forKey:@"Key"]];
}

// 时长统计
- (IBAction)clickStartKvButton:(id)sender {
	[MTA trackCustomKeyValueEventBegin:@"KVEvent"
		props:[NSDictionary dictionaryWithObject:@"Value" forKey:@"TimeKey"]];
}

- (IBAction)clickEndKvButton:(id)sender {
	[MTA trackCustomKeyValueEventEnd:@"KVEvent"
		props:[NSDictionary dictionaryWithObject:@"Value" forKey:@"TimeKey"]];
}
```
### NSArray 为参数的自定义事件

**接口**

```obj-c
/**
 上报自定义事件

 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param array 事件的参数，参数需要先在MTA前台配置好才能生效
 */
+ (void)trackCustomEvent:(NSString *)event_id args:(NSArray *)array;


/**
 上报自定义事件
 并指定上报方式

 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param array 事件的参数，参数需要先在MTA前台配置好才能生效
 @param appkey 需要上报的appKey，若传入nil，则上报到启动函数中的appkey
 @param isRealTime 是否实时上报，若传入YES，则忽略全局上报策略实时上报。否则按照全局策略上报。
 */
+ (void)trackCustomEvent:(NSString *)event_id
	args:(NSArray *)array
	appkey:(NSString *)appkey
	isRealTime:(BOOL)isRealTime;

/**
 开始统计自定义时长事件
 此接口需要跟trackCustomEventEnd配对使用
 多次调用以第一次开始时间为准

 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param array 事件的参数，参数需要先在MTA前台配置好才能生效
 */
+ (void)trackCustomEventBegin:(NSString *)event_id args:(NSArray *)array;

/**
 开始统计自定义时长事件
 并指定上报方式
 此接口需要跟trackCustomEventEnd配对使用
 多次调用以第一次开始时间为准

 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param array 事件的参数，参数需要先在MTA前台配置好才能生效
 @param appkey 需要上报的appKey，若传入nil，则上报到启动函数中的appkey
 */
+ (void)trackCustomEventBegin:(NSString *)event_id
	args:(NSArray *)array
	appkey:(NSString *)appkey;

/**
 结束统计自定义时长事件
 此接口需要跟trackCustomKeyValueEventBegin配对使用
 多次调用以第一次结束时间为准

 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param array 事件的参数，参数需要先在MTA前台配置好才能生效
 				参数中的各项必须跟开始统计时传入的参数一样才能正常配对
 */
+ (void)trackCustomEventEnd:(NSString *)event_id args:(NSArray *)array;

/**
 结束统计自定义时长事件
 并指定上报方式
 此接口需要跟trackCustomKeyValueEventBegin配对使用
 多次调用以第一次结束时间为准

 @param event_id 事件的ID，ID需要先在MTA前台配置好才能生效
 @param array 事件的参数，参数需要先在MTA前台配置好才能生效
 				参数中的各项必须跟开始统计时传入的参数一样才能正常配对
 @param appkey 需要上报的appKey，若传入nil，则上报到启动函数中的appkey
 @param isRealTime 是否实时上报，若传入YES，则忽略全局上报策略实时上报。否则按照全局策略上报。
 */
+ (void)trackCustomEventEnd:(NSString *)event_id
	args:(NSArray *)array
	appkey:(NSString *)appkey
	isRealTime:(BOOL)isRealTime;
```

**示例**

```obj-c
// 次数统计
- (IBAction)clickNormaltButton:(id)sender {
	[MTA trackCustomEvent:@"NormalEvent" args:[NSArray arrayWithObject:@"arg0"]];
}

// 时长统计
- (IBAction)clickStartButton:(id)sender {
	[MTA trackCustomEventBegin:@"TimeEvent" args:[NSArray arrayWithObject:@"arg0"]];
}

- (IBAction)clickEndButton:(id)sender {
	[MTA trackCustomEventEnd:@"TimeEvent" args:[NSArray arrayWithObject:@"arg0"]];
}
```
### 上报当前缓存的事件

**接口**

```obj-c
/**
 上报当前缓存的数据
 若当前有缓存的事件（比如上报策略不为实时上报，或者有事件上报失败）时
 调用此方法可以上报缓存的事件

 @param maxStatCount 最大上报事件的条数
 */
+ (void)commitCachedStats:(int32_t)maxStatCount;
```