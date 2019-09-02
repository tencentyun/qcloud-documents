### Push Timeliness
For full push API and bulk push API (bulk account, bulk token, tag), it takes about thirty seconds for task scheduling. While the single-push API (single push account, single push token) generally takes only seconds.
>Note:
>Pushes peak at 12:00 p.m. and from 6:00 p.m. to 8:00 p.m., and then some messages may be delayed.


#### Local Notification Delay
To display local notifications, the App must be at the frontend, and XGPush service must be active and runs normally. If the App is closed, local notifications cannot be displayed. The local notification pops up based on the network heartbeat which is about once every five minutes. Timely notification popup cannot be guaranteed for there may be a certain time lag before and after the popup.

### Failed to Receive Notifications
If notifications pushed on [XGPush Web](http://xg.qq.com/) using the token obtained cannot be received, please check the following (Make sure that SDK is the latest version. The problem occurred in old versions may have been fixed in the new version. If text-based push error occurs, refresh the page and try again).

#### Failed to Receive Pushes after Successful Registration:

1. Check whether the package name of current App is consistent with that entered when registering XGPush. If not, it is recommended to enable multiple package names for pushing.
2. Check whether the notification bar permission is enabled on the device. For some mobiles, such as Oppo, Vivo, the notification bar permission needs to be manually enabled.
3. XGPush is divided into [Message in Notification Bar](https://cloud.tencent.com/document/product/548/13949#.E6.8E.A8.E9.80.81.E9.80.9A.E7.9F.A5) and [In-App Message](https://cloud.tencent.com/document/product/548/13949#.E5.BA.94.E7.94.A8.E5.86.85.E6.B6.88.E6.81.AF) (transparently transferred message). Messages in notification bar can be displayed in the notification bar, while In-App messages cannot be displayed there.
4. Make sure the mobile is in normal mode. Some mobiles put network and activity restriction on XGPush process at the backend when the phones are in low battery, power saving mode, or unscramble mode.


#### Failed to Receive Pushes due to Unsuccessful Registration:
**1. Registration error codes:**
For error 10004 and 20, please see [XGPush Error Code](https://cloud.tencent.com/document/product/548/13991).

**Error 10004**
Reason: The .so file is incompletely imported. The .so file is used to adapt CPUs of different device types. If error 10004 occurs, check whether the imported .so library file supports the CPU of current device. If not, add the corresponding .so file (the complete .so library is in the Other-Platform-SO directory under SDK folder).

**Solution for eclipse developing tool:**
Copy the .so file required for the CPU of the device to the lib directory.

**Solution for Androidstudio developing tool:**
For Androidstudio, you can add a folder named jniLibs in the .main file directory, and add the 7 .so library folders under Other-Platform-SO of the SDK documentation to the added directory, or use [Automatic Access](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E7%A7%BB%E5%8A%A8%E4%B8%8E%E9%80%9A%E4%BF%A1/%E4%BF%A1%E9%B8%BD/Android%20%E6%8E%A5%E5%85%A5/Android%20SDK%20%E9%9B%86%E6%88%90%E6%8C%87%E5%8D%97/%E9%9B%86%E6%88%90%E5%88%86%E7%B1%BB.md) to automatically import the .so file.

**2. No registration callback:**
Check whether the current *network* is in good condition (it is recommended to use 4G network for test as WiFi may provide insufficient bandwidth due to excessive users), and whether *wup package* is added. *Nubia mobiles* (some models do not support third-party push) released in the second half of 2015 and in 2016 cannot be used to register XGPush. The specific models include Nubia Z11 series, Nubia Z11S series, and Nubia Z9S series. The previously released models work well, including Z7 series, my Prague series (cannot be used to register XGPush 2.47 and 3.X).

#### Pushes cannot be Received if App is Closed
Now, all third-party push services cannot guarantee that messages can be received after App is closed. For XGPush, this is because of the restriction on XGPush service from custom ROM of mobiles. All activities of XGPush are based on the normal connection to Internet of XGPush service.
QQ and WeChat are on the system-level App whitelist, and the relevant services will not terminate after the App is closed. Therefore, the user can receive messages after closing the App, because the relevant service is still running at the backend.
For Android devices, messages pushed after App is closed and the connection between XGPush service and XGPush server is broken will become offline messages. A maximum of 72 offline messages can be saved, and two offline messages can be saved for each device at most. If messages pushed after App is closed cannot be received, check whether the unregistration API XGPushManager.unregisterPush(this) is called.

#### Failed to Receive Account-based Pushes
Each account can be bound with a maximum of 15 devices. If the limit is exceeded, the first bound account is automatically forced out by the latest one. The valid account registered for each device is the last bound account. If multiple devices are bound with multiple accounts, all devices can receive the push.

#### Failed to Receive Tag-based Push
Check whether the tag is successfully bound. A maximum of 10,000 tags can be set for one App, and each token can have a maximum of 100 tags under one App. A tag cannot contain any space.

### Whether XGPush is Supported Overseas
The pushed messages can be received as long as the XGPush server domain name openapi.xg.qq.com can be pinged successfully. The overseas server of XGPush is deployed in Hong Kong. Due to the high network delay in overseas regions, quality of XGPush push overseas is slightly worse than that in China.
Test method: In the network environment to be tested, open the command line, enter "ping openapi.xg.qq.com", and press Enter. If the following logs appear, XGPush server has been successfully connected:

```
admin$ ping openapi.xg.qq.com
PING openapi.xg.qq.com (******* ip address): 56 data bytes
64 bytes from 14.215.138.42: icmp_seq=0 ttl=54 time=4.364 ms
64 bytes from 14.215.138.42: icmp_seq=1 ttl=54 time=5.352 ms
64 bytes from 14.215.138.42: icmp_seq=2 ttl=54 time=4.514 ms
64 bytes from 14.215.138.42: icmp_seq=3 ttl=54 time=4.924 ms
64 bytes from 14.215.138.42: icmp_seq=4 ttl=54 time=4.447 ms
64 bytes from 14.215.138.42: icmp_seq=5 ttl=54 time=4.843 ms
64 bytes from 14.215.138.42: icmp_seq=6 ttl=54 time=5.946 ms
```
### Data Push
#### Push is Suspended
1. The full push with the same content can only be pushed once per hour, otherwise it will be suspended.
2. A maximum of 30 full pushes can be pushed per hour, otherwise it will be suspended.

#### Result Statistics
[Next day]: Pushed data can be viewed the next day.
[Real time]: Pushed data can be viewed immediately. A maximum of 14 real-time statistics are allowed per week.

#### Actual Volume
It refers to volume of messages pushed normally when XGPush server is successfully connected during the offline saving period of messages. (For example, if the message is saved offline for three days, the actual issuing data is stable on the fourth day, and the data increase as the number of devices connecting to XGPush servers increases).

#### History Details
The history details only show data related to full push, tag-based push, and number-package-based push on the official website (other push APIs do not show push details).

#### Data Overview
It shows the data of the day, i.e. the total volume of all pushes (single push, broadcast (bulk and full push), messages in notification bar and In-App message) within the day.

