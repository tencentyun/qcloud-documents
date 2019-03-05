The following API is called to initialize MTA before all other StatService methods are called. MTA must be initialized for the third-party SDK lib. App and other non-lib projects do not require initialization, and SDK automatically reports the underlying data. No data is reported during MTA initialization. It merely activates MTA, and preloads the database configuration information.
```
boolean StatService.startStatService(Context ctx, String appkey, String mtaSdkVersion)
```
### Parameters

| Parameter Name | Description |
|---|-----|
| Ctx | device context of the page |
| Appkey | appkey provided by MTA. If it is null, based on the read StatConfig.setAppKey() or the appkey requiredMtaVer configured for manifest.xml, and the version number of MTA SDK that the current App depends on, it can only be com.tencent.stat.common.StatConstants.VERSION for detection of SDK version conflict. |

**MtaSDkException Exception:** The MtaSDkException occurs when the startup fails. This may be a parameter error or an SDK version conflict. For specific conflict solutions, please see SDK Conflict Issues in the Notes. Meanwhile, MTA automatically disables all features.

### Call Location
1. For normal App, it is called in the onCreate() of the initially launched activity specified by AndroidManifest.xml, and after the method of the StatConfig class is used.
2. For lib projects, it is called before all other StatService methods are called and after the method of the StatConfig class is used. 
>**Note:**
>StatConfig Configuration class needs to take effect before this method.


```
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_mtamain);
// androidManifest.xml specifies that this activity is launched first
// Therefore, MTA needs to be initialized in this onCreate
// Call API of StatConfig configuration class before startStatService to enable MTA configuration to take effect in time
String appkey = "amtaandroid0";
// Initialize and Launch MTA
try {
// The third parameter must be com.tencent.stat.common.StatConstants.VERSION
StatService.startStatService(this, appkey,
com.tencent.stat.common.StatConstants.VERSION);
Log.d("MTA","MTA initialization successful")
} catch (MtaSDkException e) {
// MTA initialization failed
Log.d("MTA","MTA initialization failed"+e)
}
}
```

