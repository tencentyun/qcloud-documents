## 业界首个零代码调用数据分析 SDK
### 功能说明
无需任何一行代码调用，只要通过简单配置组件，达到代码统计的目的。同时，考虑到扩展性和业务定制化需求，还支持通过加载或远程下发定制的配置文件处理，因此，理论上来说，还可以支持业务的代码调用。
- **支持的统计功能：**
基础统计、页面统计、时长统计、Crash 统计、网速监控、可视化埋点、安装来源。后续会兼容更多的功能。
- **不支持的统计功能：**
自定义事件（可视化部分除外）、接口监控、账号等需要主动且个性化传参的功能。

### 接入说明
1. 【必选】配置 AndroidManifest.xml，接入 SDK 默认的基础统计、时长统计、Crash(jcenter 仓库接入 3.4.0beta 可以不添加，若业务还希望扩展自己的逻辑，可按照要求在 assets 添加配置文件，将待加载的代码配置到文件中。
2.  【基础】AndroidManifest 配置
在 MTA 权限、Appkey 信息的配置的基础上，额外增加以下配置：
```
<provider
android:name="com.tencent.stat.SmartProvider"
android:authorities="当前应用包名“.MTA.SmartProvider"
android:exported="false"></provider>
```
3. 【扩展，可选】assets 配置文件
为了扩展逻辑，支持业务甚至是第三方 SDK 的代码无码加载，我们还支持通过在 assets 目录添加配置文件。
![](https://main.qcloudimg.com/raw/c3b50751d87f384ed302236c71991323.jpg)
a. 在 assets 目录下新建 “MTA_SMART_MODULE” 文件
b. 按以下格式，配置 JSON 文件
```
[
{
"class":"com.tencent.stat.StatCofig",//类名
"method":"setDebugEnable",
"static":1,//是否为静态类型，1：是，0：否
"args" :[ // 参数类型和值
{
"canme":"boolean",//cname:类型，支持 boolean、int、float、String、Context、Applicaton
"cvalue":"true" // calue:参数对应的值;Context、Application不需要填写
]},
{
其他参数信息
}
]
},
{
其他类/方法/参数信息
}
]
```
c. 一些示例，包含MTA、业务自定义的静态/非静态类
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
d. 验证
可参考 Demo 工程的 AndroidMenifest.xml 和 assets 目录下文件。
  i. 导入 mta-NoCode-demo 工程，代码中无需调用任何 MTA SDK 代码
  ii. 运行 apk
  iii. 查看 “MtaSDK” 标签的 Logcat 输出
  iv. 自定义方法可参考 MtaNoCodeCustomClassTest.java 文件
  v. logcat 输出示例
![](https://main.qcloudimg.com/raw/12bcc89ef43f1ef0d53e7940cd9ee9a8.jpg)

## LBS
### 功能说明
按设置的频率定期上报 GPS 信息，默认不调用。
```
//a.初始化
// GPS更新选项
StatGpsOption statGpsOption = new StatGpsOption();
// 默认100米
statGpsOption.setMinDistance(100);
// 默认30分钟
statGpsOption.setMinTime(30 * 60 * 1000);
// 初始化GPS
StatGpsMonitor.getInstance().init(statGpsOption);
//b.启用并上报
// 开始并按设置的更新频率上报GPS信息
StatGpsMonitor.getInstance().startMonitor();
//c.停止上报
// 停止GPS上报
StatGpsMonitor.getInstance().stopMonitor();
```
