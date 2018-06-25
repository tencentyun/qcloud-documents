## First Data Analysis SDK with Zero Code Call in the Industry
### Feature Description
You can achieve code statistics by simply configuring components, eliminating the need of calling codes. In addition, in consideration of scalability and business customization needs, custom configurations can be loaded and issued remotely for processing. Theoretically, the SDK also supports code call for business.
- **Supported statistics features:**
Basic statistics, page statistics, duration statistics, Crash statistics, network speed monitoring, visualized event tracking, and installation sources. More features will be compatible in the future.
- **Unsupported statistics features:**
Custom events (excluding visualization-related events), API monitoring, account, and other features requiring active and personalized parameter specification.

### Integration Description
1. [Required] Configure AndroidManifest.xml to integrate with the default basic statistics, duration statistics, Crash (not required for jcenter warehouse to integrate with 3.4.0beta) of the SDK. If you want to expand the logic for the business, you can add the configuration file in "assets" as required and configure the codes to be loaded into the file.
2. [Basic] AndroidManifest configuration
In addition to the configuration of MTA permission and Appkey information, the following configurations are also added:
```
<provider
android:name="com.tencent.stat.SmartProvider"
android:authorities="Name of the current App package ".MTA.SmartProvider"
android:exported="false"></provider>
```
3. [Extended, optional] assets configuration file
You are also allowed to add configuration files in "assets" directory to extend the logic and load third-party SDK without codes.
![](https://main.qcloudimg.com/raw/c3b50751d87f384ed302236c71991323.jpg)
a. Create a "MTA_SMART_MODULE" file in "assets" directory
b. Configure JSON file in the following format
```
[
{
"class":"com.tencent.stat.StatCofig",//class name
"method":"setDebugEnable",
"static":1,// Whether it is static. 1: Yes; 0: No
"args" :[ // Parameter type and value
{
"canme":"boolean",//cname: Type. boolean, int, float, String, Context, and Applicaton are supported.
"cvalue":"true" // cvalue: Value of the parameter; Context and Application are not required
]},
{
Other parameter information
}
]
},
{
Other class/method/parameter information
}
]
```
c. Some examples, including static/non-static MTA and custom business classes
```
[
{
"class":"com.tencent.stat.StatConfig",
"method":"setDebugEnable",
"static":1,
"args":[
{
"cname":"boolean",
"cvalue":"true"
}
]
},
{
"class":"com.tencent.stat.autotrackapp.SmartMeoduleTest",
"method":"inerFunc",
"static":0,
"args":[
{
"cname":"Application",
"cvalue":""
}
]
},
{
"class":"com.tencent.stat.autotrackapp.SmartModuleTest",
"method":"staticFunc",
"static":1,
"args":
[
{
"canme":"Application",
"cvalue":""
}
]
}
]
```
d. Verification
Please see AndroidMenifest.xml and files under "assets" directory of Demo project.
  i. Import mta-NoCode-demo project without calling any MTA SDK code
  ii. Run apk
  iii. View Logcat output of the "MtaSDK" tag
  iv. For more information on custom method, please see MtaNoCodeCustomClassTest.java file
  v. logcat output example
![](https://main.qcloudimg.com/raw/12bcc89ef43f1ef0d53e7940cd9ee9a8.jpg)

## LBS
### Feature Description
The GPS information is reported periodically according to the set frequency, and is not called by default.
```
//a. Initialize
// GPS update option
StatGpsOption statGpsOption = new StatGpsOption();
// 100 meters by default
statGpsOption.setMinDistance(100);
// 30 minutes by default
statGpsOption.setMinTime(30 * 60 * 1000);
// Initialize GPS
StatGpsMonitor.getInstance().init(statGpsOption);
//b. Enable and report
// Start and report GPS information according to the set update frequency
StatGpsMonitor.getInstance().startMonitor();
//c. Stop reporting
// Stop GPS reporting
StatGpsMonitor.getInstance().stopMonitor();
```

