### Feature Overview

The following functions can be used to dynamically adjust the settings for Apps and SDKs.

### API Settings for Android Apps

1. Session duration (Default: 30,000 ms. If a user switches back to the App within 30,000 ms, it is considered that no new sessions are created.)
```
void StatConfig.setSessionTimoutMillis(int sessionTimoutMillis)
```
2. The number of times to resend failed messages (default: 3)
```
void StatConfig.setMaxSendRetryCount(int maxSendRetryCount)
```
3. Maximum number of concurrent user-defined events of time type (default: 1,024)
```
void StatConfig.setMaxParallelTimmingEvents(int max)
```

4. Set the installation channel.
```
void StatConfig.setInstallChannel(String installChannel)
```
5. Set App Key.
```
void StatConfig.setAppKey(Context ctx, String appkey)
```
6. Set whether to enable statistics (default: true).
```
void StatConfig.setEnableStatService(boolean enableStatService)
```
If it is false, the statistics feature is disabled and no information is cached or reported.
7. Set the number of messages created in the session (default is 0, namely, no limits).
```
void StatConfig.setMaxSessionStatReportCount(int maxSessionStatReportCount)
```
If the value is 0, it indicates that you can create as many messages as you want in the session. If the value is greater than 0, the number of messages that can be created in each session does not exceed this value; if the actual number of the created messages exceeds the set value, the new messages will be discarded.

8. Set the number of sessions (default: 20) created per day or within each process time.
To prevent too many reported sessions caused by developers' improper MTA calling, the maximum number of sessions created per day or within each process time is set for the SDK. When this value is reached, the SDK no longer creates and reports new sessions. The number of sessions will be cleared if the process restarts or there are cross-day sessions.
```
void StatConfig.setMaxDaySessionNumbers (int maxDaySessionNumbers)
```
9. Set the maximum length (in bytes, default: 4k) of a single event.
To prevent increased traffic caused by a too long reporting event, the SDK does not report a single event exceeding 4k by default. For error/exception stack events, the length of exception stack does not exceed 100 (but can exceed 4k).
```
void StatConfig.setMaxReportEventLength (int maxReportEventLength)
```
10. Whether multiple processes are supported (default: false)
If MTA is used by multiple processes in the same App, please see "Multi-process Support" in the Notes.
```
void StatConfig.setEnableConcurrentProcess(boolean enableConcurrentProcess)
```

### API Settings for iOS Apps

1. The attribute configuration of MTAConfig singleton object can be used to dynamically adjust the settings for Apps and SDKs. It is called as follows:

```
[[MTAConfig getInstance] setPropertyName:value];
```
2. Session duration (Default: 30s. If a user switches back to the App 30 seconds after leaving it, it is considered that a new session is created)

```
@property uint32_t sessionTimeoutSecs
```
3. The number of times to resend failed messages (default: 3)

```
@property uint32_t maxSendRetryCount
```
4. Maximum number of concurrent user-defined events of time type (default: 1,024)

```
@property uint32_t maxParallelTimingEvents
```
5. Set the installation channel (default: appstore).

```
@property (nonatomic, retain) NSString* channel
```
6. Set App Key.

```
@property (nonatomic, retain) NSString* appkey
```
7. Set whether to enable statistics (default: true).

```
@property BOOL statEnable
```
If the value is false, the statistics feature is disabled and no information is cached or reported. Set the maximum number of messages sent in the session (default is 0, namely, no limits).
```
@property int32_t maxSessionStatReportCount
```
If the value is 0, it indicates that you can send as many messages as you want in the session. If the value is greater than 0, the number of messages that can be sent in each session does not exceed this value; if f the actual number of messages sent exceeds the set value, the new messages will be discarded.

