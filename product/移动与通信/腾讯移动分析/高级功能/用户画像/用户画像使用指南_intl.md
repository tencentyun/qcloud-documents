### User Guide for Android User Profile
You do not need to perform any configurations for the new version of Android SDK for the SDK reports data independently.
### User Guide for iOS User Profile
The iOS user profile data are obtained based on the QQ account and IDFA data reporting. Developers can freely select one of them for reporting. To ensure the accuracy of the profile data, it is recommended that developers report both QQ account and IDFA data simultaneously.
1. Report the QQ account

```obj-c
/**
 The Number of New Account field in the real-time data will be updated every time a new account is added.
 If the type of reported account is QQ number, the user profile feature can be activated.

 @param account Account name
 @param accountType Account type
 */
+ (void)setAccount:(NSString *)account type:(MTAAccountType)accountType;
```
**Example**
```obj-c
[MTA setAccount:@"991145990" type:AT_QQ];
```
2. Report IDFA

```obj-c
/**
 The device IDFA. It is recommended to set this field for Apps with the advertising permission. The user profile feature can be activated after this field is set.
 It is left blank by default.
 */
@property (nonatomic, copy) NSString *ifa;
```
**Example**
```obj-c
[[MTAConfig getInstance] setIfa:@"yourIDFA"];
```
Notes for IDFA Upload
Theoretically, IDFA can be used only after an advertising SDK is integrated. If you want to collect IDFA without using any ads, do the followings to get approved by Appstore.
 ![](https://main.qcloudimg.com/raw/5c6762eb5cfa531c83862703000dc876.png)
 The descriptions of the options in the figure above are as follows:
 1. serve advertisements within the app
&nbsp;&nbsp;&nbsp; In-App advertising service, which is applicable to scenarios where ads are integrated into the App. If this service is applicable to your situation, tick this option.

2. Attribute this app installation to a previously served advertisement.
&nbsp;&nbsp;&nbsp; If the number of installations caused by ads needs to be tracked and counted, tick this option.

3. Attribute an action taken within this app to a previously served advertisement
&nbsp;&nbsp;&nbsp; If the user behavior after ads have been installed needs to be tracked and counted, tick this option.

4. Limit Ad Tracking setting in iOS
  &nbsp;&nbsp;&nbsp; It is used for confirmation, so tick this option.
