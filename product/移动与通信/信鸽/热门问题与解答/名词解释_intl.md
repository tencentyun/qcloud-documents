## App List

 **Devices Connected Yesterday:** The number of devices that successfully connected to the XGPush server yesterday.
 **Devices with App Uninstalled Yesterday:** The number of devices on which App is uninstalled yesterday. This value is based on the uninstallation actions reported by XGPush. The number increases by 1 every time the App is uninstalled. No deduplication is performed on the number of devices.
 **Valid Devices: ** The number of devices registered on the XGPush.

## App Configuration
**App Package Name:** For the sake of security, the App package name cannot be changed once entered. A push can only be performed after the App package name is entered. The App package name is used for configuring AndroidManifest.xml, such as com.tencent.news.
**Admin:** All admins have the same permissions. You can delete other admins but cannot delete yourself. To transfer the admin role, add a new admin first, and then replace the old admin account with the new one.
**Test Device:** Before pushing messages, you can test the push on a specific test device to verify whether the push is normal. The ID of the test device is DeviceToken and is obtained via logcat. For more information, please see the developer manual.

**ACCESS KEY:** This is the client authentication key that is used with Access ID to verify whether a call is valid. It needs to be configured in the client SDK and cannot be changed.
**SECRET KEY:** It is used with APPKEY to verify whether an API call is valid. In cased of a leakage, you need to change it and reconfigure the client SDK immediately.
**ACCESS ID:** It is the unique identifier for identifying an App and cannot be changed. It needs to be configured in the client SDK, and is also required for calling backend APIs.

## Creating Push
**Push Content:** Message command is the code received and executed by App. The specific code format is defined by the App developer. By using the message command, you can remotely control the behaviors of Apps, such as: downloading Apps and changing splash screen; modifying the prices of items in mobile games items; updating text or images in Apps silently.
**Immediate/Scheduled Push:** Immediate push is suitable for testing. Scheduled push is often used for the real business.
**Custom Parameters:** You can also customize different key-value pair as needed.
**Offline Retainment:** If a user is offline when the content is pushed, he or she can receive the content when going online next time. You need to set an expiration time for retaining the content offline. If the user is still offline when the expiration time is reached, he or she cannot receive the pushed content. If there is no time limit, it is highly recommended to retain the content for 72 hours.
**Time Period Control:** Set the time period during which users can receive pushed content. You can avoid disturbing users at night, or specify that users can only receive pushed content during specific time periods.
**Action Upon Clicking Notification:** Set the response action performed after the user clicks notification. The action can be directly opening the App, opening a feature page of App, or accessing a URL with browser.
**Multi-package-name Push:** In the multi-package-name push mode, all Apps on the device that are registered with push service using this access_id will receive the messages. This feature is used to differentiate between Apps from different channels and with different package names.

## Push List
**Push List:** This is the list of full/bulk pushes falling under broadcast category. Point-to-point (unicast) pushes will not display in the push list. To view the unicast pushes, go to the "Push Data" page.
**Push Time:** The time to start this push.
**Android - Effective Pushes:** The number of pushes successfully sent to the current online device connected to the server. If saving messages offline is configured, the value of effective pushes increases every time a user goes online, which means the user has also received the pushed message.
**iOS - Effective Pushes:** The number of pushes sent to the iOS server successfully. XGPush is responsible for pushing messages to the iOS server, but due to the restrictions of iOS server, arrivals cannot be counted.
**Arrivals:** The number of users to whom the message is pushed successfully. There is a five-minute delay before the real-time data is generated.
**Cancel Scheduled Push:** Cancel a scheduled push that has not been implemented yet. After the cancellation, the push will no longer be implemented.
**Delete Offline Messages:** Refers to the deletion of offline messages that are stored at backend to be sent. After the deletion, the messages will no longer be sent. However, the messages that have been successfully sent cannot be deleted.

## Push Data
** Android - Effective Pushes:** The number of pushes successfully sent to the current online device connected to the server. If saving messages offline is configured, the value of effective pushes increases every time a user goes online, which means the user has also received the pushed message.
**iOS - Effective Pushes:** The number of pushes sent to the iOS server successfully. XGPush is responsible for pushing messages to the iOS server, but due to the restrictions of iOS server, arrivals cannot be counted.
**Arrivals:** The number of users to whom the message is pushed successfully. There is a five-minute delay before the real-time data is generated.
**Arrival Rate:** Arrivals/Effective Pushes×100%
**Clicks:** For a successful push, the number of clicks on the pushed message. The terminal is required to call a specific function to report this value.
**Click Rate:** Clicks/Arrivals×100%

## Basic Data
**New Devices on Current Day:** The total number of new devices registered on the current day. Integration with client SDK V2.3.6 or above is required.
**Devices with App Uninstalled on Current Day:** The total number of devices on which App is uninstalled on the current day. Integration with client SDK V2.3.6 or above is required.
**Devices Connected on Current Day:** The number of devices that connected to the XGPush server on the current day.

## My Tags
**Tag:** Refers to tagging a certain user or a group of users. Custom tags can be set through client or server calls and then used at the frontend.
**Advanced Data Tag:** The tags that XGPush sets for specific users directly by sorting data. Advanced tags are for use only and cannot be edited or deleted.

