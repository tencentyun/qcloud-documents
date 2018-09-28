## Log Location

Logs are written to the storage of terminal at the same time when they are output to the development console. Developers can find the logs at the following locations:

### Android

SDK | Directory
:--:|:--:
iLiveSDK | tencent/imsdklogs/SDK name/ilivesdk_YYYYMMDD.log
IMSDK | tencent/imsdklogs/SDK name/imsdk_YYYYMMDD.log
AVSDK | tencent/imsdklogs/SDK name/QAVSDK_YYYYMMDD.log

### iOS

SDK | Directory
:--:|:--:
iLiveSDK|Library/Caches/ilivesdk_YYYMMDD.log
IMSDK|Library/Caches/imsdk_YYYMMDD.log
AVSDK|Library/Caches/QAVSDK_YYYMMDD.log

### Mac

SDK | Directory
--|--
iLiveSDK|/Users/**user**/Library/Caches/ilivesdk_YYYMMDD.log
IMSDK|/Users/**user**/Library/Caches/imsdk_YYYMMDD.log
AVSDK|/Users/**user**/Library/Caches/QAVSDK_YYYMMDD.log

* Note: "user" is the account to log in to your own computer. For example, if the current computer's login account is zhangsan, the cache path is /Users/zhangsan/Library/Caches

### PC

SDK | Directory
:--:|:--:
iLiveSDK | Application running directory/txsdklog/ilivesdk_YYYMMDD.log
IMSDK | Application running directory/txsdklog/imsdk_YYYMMDD.log
AVSDK | Application running directory/txsdklog/QAVSDK_YYYMMDD.log

### Web

SDK | Directory
:--:|:--:
iLiveSDK | %appdata%/Tencent/iLiveSDK/txsdklog/ilivesdk_YYYMMDD.log<br/>(Enter %appdata% in Run in the Start Menu to open the appdata directory)
IMSDK|%appdata%/Tencent/iLiveSDK/txsdklog/imsdk_YYYMMDD.log
AVSDK|%appdata%/Tencent/iLiveSDK/txsdklog/QAVSDK_YYYMMDD.log


## API for Acquiring Logs

When the user needs to report the log, call the API for reporting log. iLiveSDK will directly transmit the log to the Tencent Cloud backend.   

**Android API**   

```java
/**
 * Report the log
 *
 * @param desc Description
 * @param data - 0: today; 1: yesterday; 2: the day before yesterday, and so on
 * @param callBack Callback
 * 
 */
ILiveSDK.getInstance().uploadLog(String desc, int data ILiveCallBack callback);
```
**iOS API**         

```java
/**
 Log reporting
 
 @param logDesc       Log description
 @param dayOffset    Date, 0: today; 1: yesterday; 2: the day before yesterday, and so on
 @param uploadResult Report callback
 */
(void)uploadLog:(NSString *)logDesc logDayOffset:(int)dayOffset uploadResult:(ILiveLogUploadResultBlock)uploadResult;
```

**PC API**

```c++
//API not opened yet
```

**Web API**

```js
//API not opened yet
```

Developers can query and download the logs uploaded by users at [Log Query Platform](http://vip.avc.qcloud.com/SdkLog/home).
![](https://main.qcloudimg.com/raw/deec9b5df4e0ae801f49854bb48da0b4.png)



