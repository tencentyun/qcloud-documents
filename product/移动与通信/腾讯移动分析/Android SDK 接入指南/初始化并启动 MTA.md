在所有其它 StatService 方法被调用之前调用以下接口初始化 MTA，第三方合作 SDK lib 必须初始化 MTA，App 以及其它非 lib 类的项目可以不执行初始化，SDK 会自动上报基础数据。初始化 MTA 并不会上报任何数据，仅仅是激活 MTA，并预加载数据库的配置信息。
```
boolean StatService.startStatService(Context ctx, String appkey, String mtaSdkVersion)
```
### 参数说明

|参数名|描述|
|---|-----|
|Ctx |页面的设备上下文|
|Appkey| MTA 提供的 appkey，若为 null，则按读取 StatConfig.setAppKey() 或 manifest.xml 配置的 appkey requiredMtaVer 当前 App 依赖的 MTA SDK 版本号，只能为 com.tencent.stat.common.StatConstants.VERSION，用于 SDK 版本冲突检测|

**MtaSDkException异常：**启动失败时会抛出 MtaSDkException 异常，可能是参数出错，也可能是 SDK 版本冲突，具体的冲突解决办法见注意事项中的 SDK 冲突问题，同时 MTA 会自动禁止所有功能。

### 调用位置
1. 对于普通 App：AndroidManifest.xml 指定首先启动的 activity 的 onCreate() 处，StatConfig 类的方法之后。
2. 对于 lib 工程，在其它所有 StatService 方法被调用之前，StatConfig 类的方法之后。 
>**注意：**
>StatConfig 配置类需要在此方法前才能及时生效。


```
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_mtamain);
// androidManifest.xml指定本activity最先启动
// 因此，MTA的初始化工作需要在本onCreate中进行
// 在startStatService之前调用StatConfig配置类接口，使得MTA配置及时生
String appkey = "amtaandroid0";
// 初始化并启动MTA
try {
// 第三个参数必须为：com.tencent.stat.common.StatConstants.VERSION
StatService.startStatService(this, appkey,
com.tencent.stat.common.StatConstants.VERSION);
Log.d("MTA","MTA初始化成功")
} catch (MtaSDkException e) {
// MTA初始化失败
Log.d("MTA","MTA初始化失败"+e)
}
}
```
