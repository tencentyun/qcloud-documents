Mobile Tencent Analytics (MTA) Statistics SDK for Android provides two integration methods: manual integration and automatic integration via jcenter. This document describes the manual integration method. For more information on automatic integration, please see the [Automatic Integration via jcenter](https://cloud.tencent.com/document/product/549/12864 ).

### Obtaining AppKey
Log in to [MTA Mobile Statistics](http://mta.qq.com/), and register the App as prompted to obtain AppKey.

### Importing SDK into Project
Download SDK package, decompress it to the local directory, and copy mta-sdk-x.x.x.jar[1] in the lib directory to the libs directory (create one if it does not exist) of your application project.
>Take Eclipse as an example:
Right click **Root Directory** -> **Properties** -> **Java Build Path** -> **Libraries** -> **Add JARs** of the project. Select the mta-sdk-xxxjar file in the libs directory of the current project, and click **OK** to import it.

### Configuring AndroidManifest.xml File
Add the two types of configurations as follows:

| Meta-Data | Type | Use | Required |
|---------|---------|---------|--------|
| TA_APPKEY | String, which cannot be a pure numeric string | The AppKey provided by MTA is used to identify the uniqueness of each App. | Yes |
| InstallChannel | String; if it is a pure numeric string, it cannot exceed the range represented by int | Used to mark the application promotion channel, and distinguish the source of new users to view statistics | Yes |
| Provider | Android component | Compatible with Android 6.0 (required for MID 3.5+) | No |
>**Note:**
>AppKey and installChannel can also be configured in codes. For more information, please see App Configuration API.

| Required Permission | Use | Required |
|---------|---------|---------|
| INTERNET | Allow Apps to connect network so that they can send data to our server | Yes |
| READ_PHONE_STATE | Obtain the IMEI of a user's mobile phone to uniquely identify the user. (The App running on the tablet reads the mac address as the user's unique identifier | Yes |
| ACCESS_NETWORK_STATE | Obtain the network status of a device | Yes |
| ACCESS_WIFI_STATE | Obtain WiFi network status of a device | Yes |
| WRITE_EXTERNAL_STORAGE | Obtain SD card information | Yes |

#### Sample File:

```
<?xml version="1.0" encoding="utf-8"?>
<manifest ......>
<uses-sdk android:minSdkVersion="7" android:targetSdkVersion="7"/>
<!-Authorized by MTA.< -->
<!-If it is a third-party lib project, prompt App developers to grant the following permissions in the manual! < -->
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.WRITE_SETTINGS"/>
<!-- Configure appkey and channel for application or call API of StatConfig class for codes < -->
<application ......>
<activity ......>
......
</activity>
<!-- This configuration must be added for versions later than MID3.5 (mid-sdk-3.5.jar) -->
<provider
android:name="com.tencent.mid.api.MidProvider"
android:authorities="Your package name.TENCENT.MID.V3"
android:exported="true" >
</provider>
<meta-data android:name="TA_APPKEY" android:value="ABCDEFG12233456"/>
<!-- Change value to the channel via which the App is published. Use different names for different publishing channels < -->
<meta-data android:name="InstallChannel" android:value="play"/>
<!-- Note: If the channel to be entered is a pure numeric string, do not exceed the range indicated by int! < -->
```
### Add SDK References in Codes

```
import com.tencent.stat.StatConfig
import com.tencent.stat.StatService
```
**StatConfig class:** MTA configuration class. You can set the report policy, Debug switch, and session timeout. To take effect in time, it is required to be called before MTA is initialized. Usually the default SDK configuration is used.
**StatService class:** MTA statistics class. Developers are required to call the API according to the following steps.

### Add SDK Statistics
Call the API (for more information, please see XXXXXXXXXX (to be added)) provided by the StatService class for codes to embed the statistics feature of MTA.

### Verify Whether Data Report is Normal
After you embed MTA, start the App, and trigger MTA statistics API. Generally after about 5 seconds, you can see the update of real-time metrics on the homepage of your App. It indicates that you have successfully embedded MTA, and you can continue further statistical development. If no real-time metric update shows after a few minutes, check the following items:
(1) Whether WiFi of the device is enabled and whether the device is connected with the network;
(2) Whether APPKEY and permissions are configured correctly.
(3) Ensure that the MTA statistics API has been triggered;
(4) Open debug switch of MTA, and view the logcat prompt labeled "MtaSDK". Check whether there is an error log;
(5) If logcat prompts "Compatibility problem was found in this device!", remove and reinstall apk by referring to Compatibility Errors.

