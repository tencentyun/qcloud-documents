### Custom Event with NSDictionary as Parameter

```obj-c
/**
 Report custom events

 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param kvs Event parameter, which takes effect only after it is configured in the MTA frontend
 */
+ (void)trackCustomKeyValueEvent:(NSString *)event_id props:(NSDictionary *)kvs;

/**
 Report custom events
 And specify the reporting method

 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param kvs Event parameter, which takes effect only after it is configured in the MTA frontend
 @param appkey: The appKey to be reported. If it is set to nil, report the appkey in the launch function
 @param isRealTime: Whether to report data in real time. If it is set to YES, data is reported in real time with global reporting policy ignored. Otherwise, data is reported according to the global policy.
 */
+ (void)trackCustomKeyValueEvent:(NSString *)event_id
	props:(NSDictionary *)kvs
	appkey:(NSString *)appkey
	isRealTime:(BOOL)isRealTime;

/**
 Start tracking events with custom duration
 This API should be used with the appropriate trackCustomKeyValueEventEnd
 In case of multiple calls, the first start time prevails.

 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param kvs Event parameter, which takes effect only after it is configured in the MTA frontend
 */
+ (void)trackCustomKeyValueEventBegin:(NSString *)event_id props:(NSDictionary *)kvs;

/**
 Start tracking events with custom duration
 And specify the reporting method
 This API should be used with the appropriate trackCustomKeyValueEventEnd
 In case of multiple calls, the first start time prevails.

 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param kvs Event parameter, which takes effect only after it is configured in the MTA frontend
 @param appkey: The appKey to be reported. If it is set to nil, report the appkey in the launch function
 */
+ (void)trackCustomKeyValueEventBegin:(NSString *)event_id
	props:(NSDictionary *)kvs
	appkey:(NSString *)appkey;

/**
 Finish tracking events with custom duration
 This API should be used with the appropriate trackCustomKeyValueEventBegin
 In case of multiple calls, the first end time prevails.

 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param kvs Event parameter, which takes effect only after it is configured in the MTA frontend
 			To ensure proper pairing, the key and value in the parameters must be the same as those in the parameters specified when the tracking starts.
 */
+ (void)trackCustomKeyValueEventEnd:(NSString *)event_id props:(NSDictionary *)kvs;

/**
 Finish reporting events with custom duration
 And specify the reporting method
 This API should be used with the appropriate trackCustomKeyValueEventBegin
 In case of multiple calls, the first end time prevails.

 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param kvs Event parameter, which takes effect only after it is configured in the MTA frontend
 			To ensure proper pairing, the key and value in the parameters must be the same as those in the parameters specified when the tracking starts.
 @param appkey: The appKey to be reported. If it is set to nil, report the appkey in the launch function
 @param isRealTime: Whether to report data in real time. If it is set to YES, data is reported in real time with global reporting policy ignored. Otherwise, data is reported according to the global policy.
 */
+ (void)trackCustomKeyValueEventEnd:(NSString *)event_id
	props:(NSDictionary *)kvs
	appkey:(NSString *)appkey
	isRealTime:(BOOL)isRealTime;


/**
 Directly track events with custom duration
 This method is used to report events with duration already calculated

 @param seconds Duration of custom event (in sec)
 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param kvs Event parameter, which takes effect only after it is configured in the MTA frontend
 */
+ (void)trackCustomKeyValueEventDuration:(uint32_t)seconds
	withEventid:(NSString *)event_id
	props:(NSDictionary *)kvs;

/**
 Directly report events with custom duration
 And specify the reporting method
 This method is used to report events with duration already calculated

 @param seconds Duration of custom event (in sec)
 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param kvs Event parameter, which takes effect only after it is configured in the MTA frontend
 @param appkey: The appKey to be reported. If it is set to nil, report the appkey in the launch function
 @param isRealTime: Whether to report data in real time. If it is set to YES, data is reported in real time with global reporting policy ignored. Otherwise, data is reported according to the global policy.
 */
+ (void)trackCustomKeyValueEventDuration:(uint32_t)seconds
	withEventid:(NSString *)event_id
	props:(NSDictionary *)kvs
	appKey:(NSString *)appkey
	isRealTime:(BOOL)isRealTime;
```
**Example**

```obj-c
// Statistics on clicks
- (IBAction)clickKVButton:(id)sender {
	[MTA trackCustomKeyValueEvent:@"KVEvent"
		props:[NSDictionary dictionaryWithObject:@"Value" forKey:@"Key"]];
}

// Statistics on duration
- (IBAction)clickStartKvButton:(id)sender {
	[MTA trackCustomKeyValueEventBegin:@"KVEvent"
		props:[NSDictionary dictionaryWithObject:@"Value" forKey:@"TimeKey"]];
}

- (IBAction)clickEndKvButton:(id)sender {
	[MTA trackCustomKeyValueEventEnd:@"KVEvent"
		props:[NSDictionary dictionaryWithObject:@"Value" forKey:@"TimeKey"]];
}
```
### Custom Event with NSArray as Parameter

**API**

```obj-c
/**
 Report custom events

 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param array Event parameter, which takes effect only after it is configured in the MTA frontend
 */
+ (void)trackCustomEvent:(NSString *)event_id args:(NSArray *)array;


/**
 Report custom events
 And specify the reporting method

 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param array Event parameter, which takes effect only after it is configured in the MTA frontend
 @param appkey: The appKey to be reported. If it is set to nil, report the appkey in the launch function
 @param isRealTime: Whether to report data in real time. If it is set to YES, data is reported in real time with global reporting policy ignored. Otherwise, data is reported according to the global policy.
 */
+ (void)trackCustomEvent:(NSString *)event_id
	args:(NSArray *)array
	appkey:(NSString *)appkey
	isRealTime:(BOOL)isRealTime;

/**
 Start tracking events with custom duration
 This API should be used with the appropriate trackCustomEventEnd
 In case of multiple calls, the first start time prevails.

 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param array Event parameter, which takes effect only after it is configured in the MTA frontend
 */
+ (void)trackCustomEventBegin:(NSString *)event_id args:(NSArray *)array;

/**
 Start tracking events with custom duration
 And specify the reporting method
 This API should be used with the appropriate trackCustomEventEnd
 In case of multiple calls, the first start time prevails.

 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param array Event parameter, which takes effect only after it is configured in the MTA frontend
 @param appkey: The appKey to be reported. If it is set to nil, report the appkey in the launch function
 */
+ (void)trackCustomEventBegin:(NSString *)event_id
	args:(NSArray *)array
	appkey:(NSString *)appkey;

/**
 Finish tracking events with custom duration
 This API should be used with the appropriate trackCustomKeyValueEventBegin
 In case of multiple calls, the first end time prevails.

 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param array Event parameter, which takes effect only after it is configured in the MTA frontend
 				To ensure proper pairing, values in the parameters must be the same as those in the parameters specified when the tracking starts.
 */
+ (void)trackCustomEventEnd:(NSString *)event_id args:(NSArray *)array;

/**
 Finish tracking events with custom duration
 And specify the reporting method
 This API should be used with the appropriate trackCustomKeyValueEventBegin
 In case of multiple calls, the first end time prevails.

 @param event_id Event ID, which takes effect only after it is configured in the MTA frontend
 @param array Event parameter, which takes effect only after it is configured in the MTA frontend
 				To ensure proper pairing, values in the parameters must be the same as those in the parameters specified when the tracking starts.
 @param appkey: The appKey to be reported. If it is set to nil, report the appkey in the launch function
 @param isRealTime: Whether to report data in real time. If it is set to YES, data is reported in real time with global reporting policy ignored. Otherwise, data is reported according to the global policy.
 */
+ (void)trackCustomEventEnd:(NSString *)event_id
	args:(NSArray *)array
	appkey:(NSString *)appkey
	isRealTime:(BOOL)isRealTime;
```

**Example**

```obj-c
// Statistics on clicks
- (IBAction)clickNormaltButton:(id)sender {
	[MTA trackCustomEvent:@"NormalEvent" args:[NSArray arrayWithObject:@"arg0"]];
}

// Statistics on duration
- (IBAction)clickStartButton:(id)sender {
	[MTA trackCustomEventBegin:@"TimeEvent" args:[NSArray arrayWithObject:@"arg0"]];
}

- (IBAction)clickEndButton:(id)sender {
	[MTA trackCustomEventEnd:@"TimeEvent" args:[NSArray arrayWithObject:@"arg0"]];
}
```
### Reporting Cached Events

**API**

```obj-c
/**
 Report the cached data
 If any cached event exists (for example, the reporting policy is not "Report in real time", or the reporting of an event failed)
 This method can be called to report cached events.

 @param maxStatCount The maximum number of reported events
 */
+ (void)commitCachedStats:(int32_t)maxStatCount;
```
