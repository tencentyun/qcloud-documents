## 通知分组
通知分类是 iOS 12 以后实现的新功能，在推送的 payload 中可以指定一个 key 为 thread-id 的值，iOS 12 系统中，显示推送时将会根据 thread-id 进行分组。

如果不设置 thread-id 的话，那么默认根据 App 来进行分组，通知超过一个屏幕时，将会根据 App 进行折叠。
![](https://main.qcloudimg.com/raw/7a7c9cc2ac6f7e2c02cabf19be61b286.png)

payload 示例：
```
{
	"aps": {
		"alert": {
			"title": "New Photo",
			"body": "Jane Doe posted a new photo"
		}
	},
	"thread-id": "thread-identifier"
}

```


### 设置分组的简介
可以给每个推送指定一个简介，当它们被聚合到一个通知组里的时候，通知组的下端会显示有来多少个个来自谁的通知。例如像实现上图中的简介效果，那么同时指定 payload 中 summary-arg 这个字段的值为 Michele 即可。
![](https://main.qcloudimg.com/raw/1d6b7afd6c3ba5b569a01b8fe935fdf7.png)

参考示例：
```
{
	"aps": {
		"alert": {
			"title": "Michele",
			"body": "We should celebrate after the conference before you leave your trip!",
			"summary-arg": "Michele"
		}
	},
	"thread-id": "thread-id-that-you-want"
}

```
## 静默推送
通常情况下，请求推送需要先获取用户的同意。但如果在请求推送权限时指定了默认推送的选项，那么可以在不获得用户许可的情况下进行静默推送。静默推送没有声音与提示，用户只可以主动在通知中心看到。   

请求静默推送示例：

Objective-C：
```Objective-C
[[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:UNAuthorizationOptionBadge|UNAuthorizationOptionSound|UNAuthorizationOptionSound|UNAuthorizationOptionProvisional completionHandler:^(BOOL granted, NSError *  \_Nullable error) {

  }];
```

Swift：
```Swift
let notificationCenter = UNUserNotificationCenter.current()

notificationCenter.requestAuthorization(options:[.badge, .sound, .alert, .provisional]) {
}

```


## 紧急推送
紧急推送可以穿透静音与勿扰模式发出通知，权限相当高。所以如果想发出经济推送，那么需要满足几个条件：
- 在苹果开发者网站上申请对应的 Entitlements，只有几种应用可以申请：医药与健康、家庭与安全、公共安全。
- 用户需要允许 App 发出紧急推送。

满足了上面条件以后，就可以发出紧急推送了，在 payload 中将 critical 的值设置为 1 即可。
参考示例：
```
{
	"aps": {
		"sound": {
			"critical": 1
		}
	},
	"name": "warning-sound.aiff",
	"volume": 1.0
}

```
