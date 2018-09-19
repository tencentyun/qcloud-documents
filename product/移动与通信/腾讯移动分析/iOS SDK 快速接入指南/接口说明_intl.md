This document describes how to use most of the APIs in the MTA.h header file. For more information on all the APIs and how to use them, please see the MTA.h header file.

## Header File MTA.h
### Enabling MTA
Before using the statistics feature, you need to enable MTA by calling the startWithAppkey method of MTA in the callback of UIApplicationDelegate.

```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions;
```
#### API Content

```
/**
Enable MTA

@param appkey appKey applied from the web page
*/
+ (void)startWithAppkey:(NSString *)appkey;

/**
Check the version and enable MTA.
If the MTA version is smaller than ver parameter, MTA will not be enabled. Otherwise, MTA will be enabled.

@param appkey appKey applied from the web page

@param ver The minimum version supported for enabling

@return If MTA is enabled successfully, YES is returned. Otherwise, NO is returned

*/
+ (BOOL)startWithAppkey:(NSString *)appkey checkedSdkVersion:(NSString *)ver;
```

#### Sample Codes

```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [MTA startWithAppkey:@"ABCDEFG"];
}
```
### Statistics of Number of Times
You can customize event analysis. You can track user behaviors such as number of clicks by configuring the event in the console and tracking it via codes at backend. For more information, please see [Help Documentation](https://cloud.tencent.com/document/product/549/13065).
When an App is created, three events are registered by default. Upon integration of the SDK, the custom event feature is available after you add the sample event tracking code.

#### API Content
```
/**
 Report custom events 
 And specify the reporting method

 @param event_id Event ID, which takes effect only after it is configured in the MTA console
@param kvs Event parameter, which takes effect only after it is configured in the MTA console
 @param appkey: The appKey to be reported. If it is set to nil, report the appkey in the launch function
 @param isRealTime: Whether to report data in real time. If it is set to YES, data is reported in real time with global reporting policy ignored. Otherwise, data is reported according to the global policy.
 */

+ (void)trackCustomKeyValueEvent:(NSString *)event_id
    props:(NSDictionary *)kvs
    appkey:(NSString *)appkey
    isRealTime:(BOOL)isRealTime;
    
```
#### Sample Codes
```
// The following three events are preconfigured by MTA in the console. You can collect the desired data by adding an event tracking code to the specific position

// The homepage entry event for counting the number of times that users enter the homepage
[MTA trackCustomKeyValueEvent:@"HomePage" props:nil];}

// The user registration event for counting the number of times that users click the registration button
[MTA trackCustomKeyValueEvent:@"Register" props:nil]

// The user login event for counting the number of times that users click the login button
[MTA trackCustomKeyValueEvent:@"Login" props:nil];

```


### Statistics of Page Visit Duration
Page visit duration is used to count the visit duration on a page.
>**Note:**
>The feature takes effect only after trackPageViewBegin and trackPageViewEnd are used in pairs.

#### API Content

```
/**
Mark the start of a page visit
This API needs using with the appropriate trackPageViewEnd
If a page visit starts for multiple times, the first time shall prevail

@param page Page ID, which takes effect only after it is configured in the MTA frontend
*/
+ (void)trackPageViewBegin:(NSString *)page;

/**
Mark the start of a page visit
And specify the reporting method
This API needs using with the appropriate trackPageViewEnd
If a page visit starts for multiple times, the first time shall prevail

@param page Page ID, which takes effect only after it is configured in the MTA frontend

@param appkey If this parameter is not nil, report this appkey. Otherwise, report the appkey passed in startWithAppkey.
*/
+ (void)trackPageViewBegin:(NSString *)page appkey:(NSString *)appkey;

/**
Mark the end of a page visit
This API needs using with the appropriate trackPageViewBegin
If a page visit ends for multiple times, the first time shall prevail

@param page Page ID, which takes effect only after it is configured in the MTA frontend
*/
+ (void)trackPageViewEnd:(NSString *)page;

/**
Mark the end of a page visit
And specify the reporting method
This API needs using with the appropriate trackPageViewBegin
If a page visit ends for multiple times, the first time shall prevail

@param page Page ID, which takes effect only after it is configured in the MTA frontend
@param appkey If this parameter is not nil, report this appkey. Otherwise, report the appkey passed in startWithAppkey.
@param isRealTime: Whether to report data in real time. If it is set to YES, data is reported in real time with global reporting policy ignored. Otherwise, data is reported according to the global policy.
*/
+ (void)trackPageViewEnd:(NSString *)page
appkey:(NSString *)appkey
isRealTime:(BOOL)isRealTime;
```

#### Sample Codes

```
-(void) viewDidAppear:(BOOL)animated {
    [MTA trackPageViewBegin:@"Page"];
    [super viewDidAppear:animated];
}

- (void)viewWillDisappear:(BOOL)animated {
    [MTA trackPageViewEnd:@"Page"];
    [super viewWillDisappear:animated];
}
```


### Statistics of Duration of Use
You can report the use duration of an App by adding the appropriate hitting codes to the two callbacks of UIApplicationDelegate.

```
- (void)applicationDidBecomeActive:(UIApplication *)application;
- (void)applicationWillResignActive:(UIApplication *)application;
```
#### API Content

```
/**
Start counting the use duration
You are advised to call it before the App enters the frontend
*/
+ (void)trackActiveBegin;

/**
End counting the use duration
You are advised to call it before the App leaves the frontend
*/
+ (void)trackActiveEnd;
```

#### Sample Codes

```
// Start hitting
- (void)applicationDidBecomeActive:(UIApplication *)application {
    [MTA trackActiveBegin];
}

// End hitting
- (void)applicationWillResignActive:(UIApplication *)application {
    [MTA trackActiveEnd];
}
```

## Header File MTAConfig.h
You can check and modify the header file MTAConfig.h as needed to customize MTA reporting behaviors such as reporting strategies and number of entries reported at a time.
>**Note:**
>You must modify the configuration in MTAConfig before calling the MTA launch function. Otherwise, the configuration may not take effect and may cause undefined behaviors.

For more information, please see the development document in the [sdk zip](http://mta.qq.com/mta/resource/download/sdk/mta-ios-stats-sdk-2.1.2.zip).

