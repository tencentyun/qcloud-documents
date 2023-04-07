## SDK集成
1. 参考[Android应用接入-IDE方式](https://cloud.tencent.com/document/product/1034/85243)或者 [Android应用接入-Gradle方式](https://cloud.tencent.com/document/product/1034/85242) ，完成框架接入。
2. 在 module 级别 build.gradle 中，添加应用发布依赖。
```groovy
implementation 'com.tencent.tmf.android:upgrade:+'
```

## SDK 使用

### buildNo
buildNo 为应用发布版本大小比较时使用的唯一参数，格式一般为6-7位数字，buildNo 需符合以下设计规则：
App 每发布一个版本时（包括正式版/灰度版），buildNo 需唯一且递增，同时，buildNo 与版本号需成正相关关系，即 buildNo 大的 App 版本号必须大于等于 buildNo小的 App 版本号。一个版本号可对应多个 buildNo，用于灰度升级场景做版本比较。
>?由于灰度时未正式发布新版，新包版本号仍为旧版本号，此时使用 build 号仍然可以比较版本大小，定向对灰度用户进行升级。
>

### 协议版本[](id:xybb)
早期版本应用发布任务推拉是依赖数据同步组件来完成的，从3.0.2.0版本起，应用发布支持直接使用移动网关来实现任务推拉，可以解除任务推拉对数据同步组件的依赖。不过本次协议调整对新版服务有依赖，考虑到私有化客户不同的服务版本，SDK 侧做了兼容，同时保留了两套协议实现，客户在初始化时根据自身服务情况指定协议版本即可。
```java
public class ProtocolType {
    /**
     * 旧协议，依赖数据同步组件实现任务推拉
     */
    public static final int PROTOCOL_TYPE_CONCH = 0;
    /**
     * 新协议：与数据同步组件解耦，
     */
    public static final int PROTOCOL_TYPE_SHARK = 1;
}
```
>?
> - 如果您对接的是公有云版本服务，协议版本需选择 PROTOCOL_TYPE_SHARK。
> - 如果您对接的是私有化版本服务，默认协议版本是 PROTOCOL_TYPE_CONCH，如果需要选择 PROTOCOL_TYPE_SHARK，请联系管理员确认服务版本是否支持新协议。

### 初始化
>?应用发布组件依赖基础库组件，在初始化应用发布组件前请确保基础库初始化已完成，基础库初始化时需传入正确的 buildNo。
>
应用发部组件初始化是通过UpgradeService类来完成的，接口定义如下：
```java
/**
 * 初始化
 *
 * @param context
 * @param callback 自动检查更新回调，推送及@autoUpgradeCheck触发的更新单都通过该回调返回
 * @param protocolType 协议类型
 */
public static void init(Context context, IAutoCheckCallback callback, int protocolType)
```

  - 入参
<table>
<tr>
<th>参数名称</th>
<th>参数类型</th>
<th>参数描述</th>
<th>必选</th>
</tr>
<tr>
<td>context</td>
<td>Context</td>
<td>上下文一般使用 Activity 等系统组件即可。</td>
<td>Y</td>
</tr>
<tr>
<td>callback</td>
<td>IAutoCheckCallback</td>
<td>推送及autoUpgradeCheck方法触发的更新单，都通过该回调通知。</td>
<td>Y</td>
</tr>
<tr>
<td>protocolType</td>
<td>int</td>
<td>协议版本，具体定义请参见 <a href="#xybb">协议类型</a>。</td>
<td>Y</td>
</tr>
<table>

  - Sample
```java
//TMFBase初始化
TMFBaseConfig config = new TMFBaseConfig.Builder()
                .buildNo(BuildConfig.BUILD_NO) // 必须，请遵循buildNo涉及规则
                .debug(true)
  							//...
                .build();

TMFBase.init(this, config);

//应用发布组件初始化
UpgradeService.init(this, new IAutoCheckCallback() {
    @Override
    public void onLimit(UpgradeInfo upgradeInfo) {
        // 有更新单，但更新单受弹窗频率限制，一般无需理会
    }

    @Override
    public void onUpgrade(UpgradeInfo upgradeInfo) {
        // 有更新单，根据更新单信息，处理更新弹窗逻辑
    }
}, protocalType);
```

### 检查更新
应用发布组件更新任务下发支持推送、拉取两种方式，推拉结合。初始化完成之后，会自动注册推送监听，但没有触发主动拉取更新单，开发者需根据使用场景自行触发主动拉取任务。
主动拉取支持两种方式：
- 自动检查更新：该方式会检查弹窗频率限制，更新结果通过初始化传入的 IAutoCheckCallback 回调给开发者。
- 手动检查更新：该方式不会检查弹窗评率限制，检查更新结果会通过独立设置的 UpgradeCheckCallback 回调给开发者。使用场景是应用内的**检查更新**菜单，由用户触发。

### 自动检查更新
自动检查更新是对初始化推送场景的补充，增加更新单检查频率，在弹窗频率允许范围内更及时地处理更新单。建议应用发布组件初始化完成之后即可以触发一次自动检查更新。
接口定义如下：
```java
/**
 * 自动检查更新，更新单通过初始化时设置的全局 IAutoCheckCallback 回调返回
 */
public static void autoUpgradeCheck()
```
使用示例：
```java
UpgradeService.autoUpgradeCheck();
```

### 自动检查更新回调
```java
/**
 * 版本升级自动检查监听器
 */
public interface UpgradeCheckListener {
    /**
     * 有更新单，回调开始更新
     *
     * @param upgradeInfo 版本升级信息
     */
    public void onUpgrade(UpgradeInfo upgradeInfo);
}

/**
 * 推送及自动检查更新回调，会对更新单做弹窗频率限制判断
 */
public interface IAutoCheckCallback extends IUpgradeChecker.UpgradeCheckListener{

    /**
     * 有更新单，但不满足弹窗频率限制
     * @param upgradeInfo
     */
    void onLimit(UpgradeInfo upgradeInfo);
}
```

>?更新单回调不保证是在 UI 线程，因此处理弹窗、提示时需要注意不要直接在回调中操作 UI。
>

### 更新单信息
```java
public class UpgradeInfo {
    /**
     * 普通更新类型, 只提醒一次
     **/
    public static final int UPGRADE_TYPE_ONCE = 0x01;
    /**
     * 普通更新类型, 多次提醒，无间隔
     */
    public static final int UPGRADE_TYPE_MULTI = 0x02;
    /**
     * 强制更新类型
     **/
    public static final int UPGRADE_TYPE_FORCED = 0x03;

    private String apkUrl;//apk下载链接
    private String title;//消息标题
    private String content;//消息内容
    private String versionName;//版本名，例:"3.2.4"
    private int buildNo;//build号
    private int type;//更新类型（普通/强制）
    private long noticeInterval; //更新弹窗频率限制，单位ms
    private boolean onlyWifi; //是否仅wifi下载
    //... 省略get/set 方法
}
```

>?目前版本 versionName 仅支持“x.x.x”三位数字形式，控制台配置的 versionName 也必须符合该形式，否则返回的更新数据 UpdateInfo 可能为空。

### 手动检查
手动检查是不对弹窗频率限制做检查，每次调用都会返回检查结果。使用场景是应用内的**检查更新**菜单，由用户触发。
接口定义如下：
```java
/**
 * 手动检查更新，不包含展示频率控制
 *
 * @param callback
 */
public static void manualCheckUpgrade(UpgradeCheckCallback callback) {
    UpgradeCenter.getUpgradeChecker().manualCheckUpgrade(callback);
}
  
/**
 * 升级检查回调通用接口
 */
public interface UpgradeCheckCallback {
    /**
     * 本地更新检查回调
     *
     * @param resultCode  检查结果返回码（有新版/无新版/网络错误）
     * @param upgradeInfo 版本升级信息
     */
    public void onResult(int resultCode, UpgradeInfo upgradeInfo);
}

/** 检测到新版本 **/
public static final int HAS_NEW_VERSION = 0x01;
/** 无新版本 **/
public static final int NO_NEW_VERSION = 0x02;
/** 网络错误 **/
public static final int NETWORK_ERROR = 0x03;
```
使用示例：
```java
UpgradeService.manualCheckUpgrade(new IUpgradeChecker.UpgradeCheckCallback() {
    @Override
    public void onResult(int resultCode, UpgradeInfo upgradeInfo) {
        Message message = new Message();
        if (resultCode == HAS_NEW_VERSION && null != upgradeInfo) {
            //有新版本，可以处理更新弹窗逻辑
        } else if (resultCode == NO_NEW_VERSION) {
            //无更新，当前版本已最新提示
        } else if (resultCode == NETWORK_ERROR) {
            //检查更新出现错误，请稍后再试
        }
    }
});
```
>?更新单回调不保证是在 UI 线程，因此处理弹窗、提示时需要注意不要直接在回调中操作 UI。
>

### 阶段上报
应用发布管理后台有完整的应用发布报表，包括下发、下载、安装等阶段。由于应用发布 SDK 只负责更新单推拉，更新单弹窗提示、下载、安装等后续处理流程由 App 开发者来完成，所以关键阶段数据上报需 App 开发者回调给 SDK。阶段上报接口定义如下：
```java
/**
 * 版本升级各阶段状态监听回调
 */
public interface IUpgradePhaseMonitor {

    /**
     * 升级展示回调（升级弹窗/通知栏展示时回调，对于未下载升级包情况）
     */
    void onUpgradeShow();

    /**
     * 安装展示回调（安装弹窗/通知栏展示时回调，对于已下载未安装情况），如果没有该步骤可以不调用
     */
    void onInstallShow();

    /**
     * 升级点击回调（升级弹窗/通知栏用户点击时回调）
     *
     * @param isOK 是否点击取消
     */
    void onUpgradeClick(boolean isOK);

    /**
     * 安装点击回调（安装弹窗/通知栏用户点击时回调），如果没有该步骤可以不调用
     *
     * @param isOK 是否点击取消
     */
    void onInstallClick(boolean isOK);

    /**
     * 开始下载回调（调起下载器开始下载）
     */
    void onStartDownload();

    /**
     * 下载结果回调（升级安装包下载结果回调）
     *
     * @param isSuccess 是否下载成功
     */
    void onDownloadResult(boolean isSuccess);

    /**
     * 开始安装回调（调起系统安装界面）
     */
    void onStartInstall();

    /**
     * 升级调起安装流程异常回调
     */
    void onInstallException();
}
```

使用示例：
```java
//收到更新单后，展示更新弹窗时调用
UpgradeService.getUpgradePhaseMonitor().onUpgradeShow();
//用户看到更新弹窗后，点击确定取消时调用，isOk为true表示确认安装，为false表示取消安装
UpgradeService.getUpgradePhaseMonitor().onUpgradeClick(isOk);
//用户选择确认安装后，触发下载流程时调用
UpgradeService.getUpgradePhaseMonitor().onStartDownload();
//下载结束之后调用，isSuccess是下载结果
UpgradeService.getUpgradePhaseMonitor().onDownloadResult(isSuccess);
//开始安装时调用（调起系统安装界面）
UpgradeService.getUpgradePhaseMonitor().onStartInstall();
```

### 测试
1. 打一个较低版本的包（例如 buildNo 设置为100000），安装在测试机上。
2. 修改 buildNo 为高版本（例如 buildNo 设置为100001）再打包，通过控制台应用发布模块上传并发布
>?这里填的版本号和 build 号与当前 Apk 包一致。
>
3. 在控制台发布完成，有一定延迟，等1分钟左右客户端就可以拉取到更新单了。如果是推送请确保移动网关 tcp 通道是开启状态。


## 调试

### 调试日志
过滤 TAG 为“TMF_Upgrade”日志，可查 SDK 的输出日志。
![](https://qcloudimg.tencent-cloud.cn/raw/cc9d8282f3428f30a358e3c9c7403a32.png)


