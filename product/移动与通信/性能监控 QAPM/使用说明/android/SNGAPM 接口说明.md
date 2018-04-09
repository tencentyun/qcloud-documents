### 初始化 SNGAPM
```
public static SNGAPM getInstance(Application app, int id, String ver)
```
参数如下
app： 当前应用的 app 对象
id：为[获取项目 id](https://cloud.tencent.com/document/product/683/15220)中项目分配的 id
ver：产品版本号
### 设置 SNGAPM 相关参数。
```
public static SNGAPM set(String key, Object value)
```
参数如下
key 可选为"uuid"、"uin"、"host"、"debug"、"leakfix"、"listener"
value - uuid：string 类型。设置上报数据里的 UUID，用于拉取被混淆堆栈的 mapping（注：在 RDM 上编译时，可以通过编译脚本把 UUID 写到 assets 或者 AndroidManifest.xml 里，细节可以咨询 RDM 的同学）。
uin: string 类型。设置上报数据里附带的 QQ 号。即上报的用户账号。
host: string 类型。设置上报数据到哪个集群。请向 SNGAPM 负责同学（kangtian）申请一个集群域名
debug: bool 类型。是否开启调试日志，true 为开启，false 为不开启，默认为 false。
leakfix: bool 类型。是否开启自动泄漏修复。true 为开启，false 为不开启，默认为false。
listener: 可为 InspectorListener/MemoryCellingListener/BatteryReportListener 类型，用于设置相关监听回调用。
返回值：SNGAPM 对象。
>host 必须设置，而且必须在 run 前设置。先向 SNGAPM 负责同学（kangtian）申请一个集群域名。

### 启动监控。
```
public boolean run(int func)
```
>注意：默认全开为63（SNGAPM.ALL），正式发布的版本，建议以 run(24)来启动，因为下述三个功能（1、2、4）对应用性能都略有影响。在正式版本上，除了触顶时的内存快照之外，只采集监控型数据，不采集分析型数据。

参数如下
func:功能表（1：内存泄漏(SNGAPM.LEAKINSPECTOR)、2：文件 IO(SNGAPM.IO)、4：数据库 IO(SNGAPM.DB)、8：卡顿(SNGAPM.LOOPER)、16：触顶(SNGAPM.CEILING)、32：电量(SNGAPM.BATTERY)、63(SNGAPM.ALL)：开启以上全部监控）
返回值：无