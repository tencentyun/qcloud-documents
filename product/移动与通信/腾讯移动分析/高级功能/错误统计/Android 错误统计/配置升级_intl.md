### Library File
MTA supports Java and Native exception capturing. Java Crash module is integrated into the MTA subject jar package by default. Add additional so file and call the API to enable Native Crash (c/c++ or so exception capturing). If Native encoding is used in your project, it is recommended to enable Native Crash module, otherwise so file is not required.
**Java Crash:** Replace the old version with new mta 3.x.x.jar.
**Native Crash:** libMtaNativeCrash_v2.so. Delete the old version of ibMtaNativeCrash.so. For more information on the storage of different ABI files, please see below.
MTA Native Crash supports all the architectures supported in Android system: armeabi, armeabi-v7a, arm64-v8a, x86, x86_64, mips, mips64.

In the process of integration, you must pay close attention to the storage of so library files of different architectures, otherwise a problem may occur. Generally, only so files of the architectures supported by the project are retained, and DO NOT import those of other architectures. See the example below:
**Before integration:** If libMyCustom.so is the so file of the actual project, only the architectures armeabi, armeabi-v7a and arm64-v8a are supported.
![](http://developer.qq.com/wiki/mta/imgs/20170524174726_30894.png)
**After integration:** If only so architectures supported by the project are retained, you only need to copy the so file under the architecture of Mta Native Crash to the directory corresponding to the project, that is, to copy libMtaNativeCrash_v2.so of MTA armeabi to the armeabi directory corresponding to the project. Be sure to keep the so files under the supported architecture directory consistent, and those of other architectures are not required. The following shows a project integrated with MTA that comes with native crash module:
![](http://developer.qq.com/wiki/mta/imgs/20170524174741_17213.png)
### Configuring Project

For major configurations, please see MTA connection configuration feature. The following example describes the configuration of AndroidMenifest.xml file.

```java
<application>
...Other configurations of the project's application metric

<!-- MTA configuration item< -->
<!-- Change value to appkey assigned by MTA. You can skip this step if you have called the API < -->
<meta-data
android:name="TA_APPKEY"
android:value="A91LM44JGFLV" />

<!-- Change value to the release channel (market) of App. You can skip this step if you have called the API < -->
<meta-data
android:name="InstallChannel"
android:value="MyApp" />

<!-- For the configuration of MID 3.x, you need to replace "Your App package name" with the actual package name of the project < -->
<provider
android:name="com.tencent.mid.api.MidProvider"
android:authorities="your App package name.TENCENT.MID.V3"
android:exported="true" >
</provider>
</application>

<!-- MTA permission configuration item -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```
