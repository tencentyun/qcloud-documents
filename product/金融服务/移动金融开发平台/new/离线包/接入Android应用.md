## 集成
1. 参考 [Android 应用接入-IDE 方式 ](https://cloud.tencent.com/document/product/1034/85243)或者 [Android 应用接入-Gradle 方式](https://cloud.tencent.com/document/product/1034/85242)，完成框架接入。
2. 在 module 级别 build.gradle 中，配置依赖。
```groovy
implementation 'com.tencent.tmf.android:webview:+'
implementation 'com.tencent.tmf.android:weboffline:+'
implementation 'com.tencent.tmf.android:hybrid:+'
```
3. 在 app module build.gradle 中增加配置。
```
   android{
       packagingOptions {
   //不允许AS打包时优化so库，因为X5内核的so库做了MD5的校验，否则会出现加载成功X5内核后，会被删掉
   //这里统一不优化so库，若要优化其他模块so库，也可单独对某个so库配置
           doNotStrip "**/*.so"
       }
   }
```

## 初始化

### 协议版本
早期版本离线包任务推拉是依赖数据同步组件来完成的，从3.0.2.0版本起，离线包支持直接使用移动网关来实现任务推拉，可以解除任务推拉对数据同步组件的依赖。不过本次协议调整对新版服务有依赖，考虑到私有化客户不同的服务版本，SDK 侧做了兼容，同时保留了两套协议实现，客户在初始化时根据自身服务情况指定协议版本即可。
```java
public class ProtocolType {
    /**
     * 旧协议，依赖数据同步组件实现任务推拉
     */
    public static final int PROTOCOL_TYPE_CONCH = 0;
    /**
     * 新协议：与数据同步组件解耦
     */
    public static final int PROTOCOL_TYPE_SHARK = 1;
}
```
>?
> - 如果您对接的是公有云版本服务，协议版本需选择 PROTOCOL_TYPE_SHARK。
> - 如果您对接的是私有化版本服务，默认协议版本是 PROTOCOL_TYPE_CONCH，如果需要选择 PROTOCOL_TYPE_SHARK，请联系管理员确认服务版本是否支持新协议。

### 初始化
```java
//离线包初始化
OfflineManager.init(context, protocolType);//根据对接服务版本，选择protocoType

//context 使用ApplicationContext
TMFHybridManager.getInstance().init(context);
```

## 使用默认 UI 打开一个离线包
完成初始化操作后，可以使用如下方式打开一个离线包。
```java
//方法一，指定BID打开离线包
TMFHybridManager.getInstance().startAppById(bid);
//方法二，指定URL打开离线包（URL需要满足离线包URL格式要求）
String url="https://www.qq.com/h5/index.html?_bid=yourBid";
TMFHybridManager.getInstance().startAppByUrl(url);
```

## 使用默认 UI 打开一个 URL
HCotainer 支持指定 URL 打开一个包含 Webview 的页面：
```java
String url="https://www.qq.com";
TMFHybridManager.getInstance().startAppByUrl(url);
```

## 使用自定义的 UISetting 打开页面
SDK 提供默认的 UI 布局用于打开离线包，UI布局元素配置如下：
```java
//打开一个BID
TMFHybridManager.getInstance().startAppById(bid, getCustomUiSettings());
//打开一个URL
TMFHybridManager.getInstance().startAppByUrl(url, getCustomUiSettings());

private UISettings getCustomUiSettings() {
        return new UISettings.Builder()
                .fullScreen(false)//是否全屏
                .dividerColor(getResources().getColor(R.color.poc_gray_D8D8D8))
                .showDivider(false)
                .showMainTitle(true)//是否展示主标题
                .mainTitleText("银行业务交易")//主标题文本
                .mainTitleTextColor(getResources().getColor(R.color.qmui_config_color_red))//主标题文本颜色
                .showSubTitle(true)//是否展示副标题
                .subTitleText("进行中")//副标题文本
                .subTitleTextColor(getResources().getColor(R.color.app_color_blue))//副标题文本颜色
                .setTitleViewBackGroundColor(getResources().getColor(R.color.color_default_black))
                .setBackBtnIcon(R.mipmap.h5_default_back)//返回按钮icon
                .showOptionMenu(true)//是否展示option menu
                .optionMenuIcon0(R.drawable.brand_icon)
                .optionMenuIcon1(R.mipmap.about_logo)
                .showProgress(true)//是否展示架在进度条
                .progressColor(getResources().getColor(R.color.qmui_config_color_red))//进度条颜色
                .build();
    }
```

## 使用完全自定义的 H5 页面
如果上述的自定义 UI 不能满足 H5 页面的展示需求，可以按照如下方法实现对页面的完全自定义。值得一提的是，完全自定义的 H5 页面是全局生效。
```java
//设置完全自定义的H5展示页面 
TMFHybridManager.getInstance().setCustomView(new TestCustomViewProvider());
//移除完全自定义H5页面
TMFHybridManager.getInstance().setCustomView(null);
//实现 CustomViewProvider 接口，实现相关方法
public class TestCustomViewProvider implements CustomViewProvider {

    @Override
    public IH5TitleViewProvider createTitleView(Context context) {
        return new TestCustomTitleView(context);
    }

    @Override
    public IH5ContentViewProvider createH5ContentView(Context context) {
        return new TestCustomContentView(context);
    }
}
```

## 添加全局公共资源包
当制定打开的离线包对公共资源包有依赖时，可以通过下面方法增加对公共资源包的引用；确保通过 BID 打开离线包时可以正确找到对应的公共资源。
```java
//添加全局公共资源包，bid对应公共资源包bid
TMFHybridManager.getInstance().addCommonResource(bid);
```

## 配置虚拟地址
通过 BID 打开离线包时，默认会使用 `http://www.default.com` 作为离线包的虚拟地址，可以调用如下的接口设置虚拟地址：
```java
//设置虚拟地址
TMFHybridManager.getInstance().setVirtualAddress("https://www.qq.com");
```

## 附带参数打开离线包
当离线包有附加参数添加到 Url，可以使用如下的方式进行参数传递：
```java
Bundle bundle = new Bundle();
bundle.putString(OfflineAppBundleKey.KEY_ENTRANCE_PATH, entryPath);//入口文件路径,默认为index.html
bundle.putStringArray(OfflineAppBundleKey.KEY_COMMON_RESOURCES, commonRes);//公共资源包列表
bundle.putString(OfflineAppBundleKey.KEY_URL_PARAMS, stringOfUrlParams);//Url参数，Json字符串格式

//附带参数打开离线包
TMFHybridManager.getInstance().startAppById(id, bundle, UISettings.getDefault());
```

## 使用集成视图展示离线包或者 URL
SDK 中提供了 EmbedView 用于快速集成打开离线包或者 URL。
```java
public class EmbedViewTestActivity extends TopBarActivity {

    private EmbedView embedView;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Bundle bundle = getIntent().getExtras();
        String bidOrUrl = "";
        if (null != bundle) {
            bidOrUrl = bundle.getString("key_bid_url");
        }
      //获取EmbedView实例，并添加到布局
        embedView = TMFHybridManager.getInstance().getOfflineContentView(this, bidOrUrl);
        FrameLayout frameLayout = findViewById(R.id.embed_view_container);
        frameLayout.addView(embedView,
                new LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
    }

    @Override
    protected void onResume() {
        super.onResume();
        embedView.onResume();
    }

    @Override
    protected void onStop() {
        super.onStop();
        embedView.onStop();
    }

    @Override
    protected void onPause() {
        super.onPause();
        embedView.onPause();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        embedView.onDestroy();
    }

    @Override
    protected View getContentView() {
        return LayoutInflater.from(this).inflate(R.layout.activity_embed_view_test, null, false);
    }
}
```

## 设置在线资源域名
可以通过下面的方法设置离线包对应的在线资源地址。
```java
//设置在线资源域名
TMFHybridManager.getInstance().setHostForOnlineApp("http://www.qq.com");
```


## 手动检查离线包更新
```java
OfflineManager mOfflineManager = new OfflineManager(context);

mUpdateSetting = new UpdateSetting();
mUpdateSetting.ignoreFreqLimit = true;
mUpdateSetting.fromPush = false;

List<String> list = new ArrayList<>();
list.add(BID);
mOfflineManager.checkLatestUpdate(list, mUpdateSetting, new IOfflineUpdateCallback() {
        @Override
        public void update(int code, List<UpdateEntity> updateInfos) {
            if(code == OfflineManager.CHECK_CODE_SUCC_NO_UPDATE){
                Log.d(TAG, "update, 无更新");
            }else {
                Log.d(TAG, "update, code=" + code + " " + (updateInfos == null ? null :
                	updateInfos.toString()));
            }

        }

        @Override
        public void downloadProgress(ProgressEntity progressInfo) {
            Log.d(TAG, "downloadProgress, " + progressInfo.toString());
        }

        @Override
        public void downloadFinish(DownloadInfo downloadInfo) {
            Log.d(TAG, "downloadFinish, " + downloadInfo.toString());
        }
    };);
```

## 获取本地离线包版本
```java
/**
 * 获取本地离线包的版本
 */
public static String getBizVersion(final Context context, final String businessId) 
```

使用示例：
```java
String version = mOfflineManager.getBizVersion(context, "testBid");//testBid为离线包Bid
```

## 删除本地离线包
```java
/**
 * 清理指定离线包(同步接口)
 *
 * @param businessIds 要清理的离线包id列表
 * @return 清理成功的离线包id列表
 */
public static List<String> deleteBiz(final Context context, final List<String> businessIds)
```

使用示例：
```java
//要删除的本地离线包Bid
List<String> bids = new ArrayList<>();
bids.add("testBid");

mOfflineManager.deleteBiz(context, bids);
```

## 全量检查更新
全量检查是指检查所有离线包是否有新版。
```java
/**
 * 检查所有最新离线包的更新
 *
 * @param updateSetting
 * @param callback
 */
public void checkAllUpdate(UpdateSetting updateSetting, final IOfflineUpdateCallback callback)
```
**使用场景**：
首次启动之后，想确保所有离线包更新到最新版。不过需要注意的是，全量检查更新时应将自动下载安装功能关闭，否则可能会导致后台下载大量离线包新版，影响用户体验。
**使用示例**：
```java
UpdateSetting updateSetting = new UpdateSetting();
updateSetting.isDownload = false; //关闭自动下载功能，仅做版本检查

mOfflineManager.checkAllUpdate(updateSetting, new IOfflineUpdateCallback() {
    @Override
    public void update(int i, List<UpdateEntity> list) {
        if (i == OfflineManager.CHECK_CODE_SUCC_NO_UPDATE) {
            // 无更新
        } else if (i == OfflineManager.CHECK_CODE_IGNORE_HAD_UPDATE_IN_A_SHORT_TIME) {
            // 不要频繁更新
        } else {
            // 有更新，list中是有更新的离线包信息
        }
    }

    @Override
    public void downloadProgress(ProgressEntity progressEntity) {

    }

    @Override
    public void downloadFinish(DownloadInfo downloadInfo) {

    }
});
```

## API

## UpdateSetting
```java
// 是否下载，默认为true
public boolean isDownload = true;
// 是否忽略检查更新频率限制，默认为false
public boolean ignoreFreqLimit = false;
// 是否仅wifi下下载，默认为false
public boolean downloadOnlyInWiFi = false;
// 是否来推送触发的检查更新，开发者无需关心，默认fasle即可
public boolean fromPush = false;
// 是否忽略延迟检查更新，默认为true。自动检查离线包更新时为false，延迟5秒触发检查更新，避免下载流程影响正常加载体验
public boolean ignoreDelay = true;
// 检查到更新先删除本地缓存，然后再下载最新离线包。默认为false
public boolean deleteOldBizBeforeDownload = false；
```

## UpdateEntity
```java
//全量更新
public static final int E_UPDATE_TYPE_NORMAL = 1;
//增量更新
public static final int E_UPDATE_TYPE_INCR = 2;
//主包
public static final int E_PKG_TYPE_MAIN = 0;
//公共包
public static final int E_PKG_TYPE_COMMON = 1;
//离线包字符串id
public String bid = "";
//离线包版本
public int version = 0;
//更新类型 EUpdateType
public int updateType = 0;
//离线包类型 EPkgType
public int pkgType = 0;
```

## ProgressEntity
```java
//离线包Id
public String bid;
//下载进度(0~100)
public int progress;
//文件总大小(字节)
public long totalBytes;
```

## DownloadInfo
```java
//参考{@link com.tencent.tmf.weboffline.api.OfflineManager}
public int code;
//离线包id
public String bid;
//错误信息
private String message;
```

## OfflinePkg
```java
//离线包id
private String bid;
//离线包检查更新的目标版本
private int targetVersion;
```

## TMFWebResourceResponse
```java
//返回WebResourceResponse
private WebResourceResponse resourceResponse;
//本地资源路径
private String path;
```

## OfflineConfig
```java
/**
* 是否检查到有新包就把旧包删掉，而不是下载到新包之后才替换(可选)
* 默认为true，客户担心下载时间比较长，要求一检查到有新包就把旧包删掉
*/
public boolean deleteOldBizBeforeDownload;

/**
* 是否开启fallback(可选)
*/
public boolean fallbackEnable;

/**
* 是否存在SD卡(可选)
*/
public boolean storeInSDCard;

/**
* 是否为快校验模式(可选)
* 快校验：整包md5校验
* 非快校验：签名校验和所有文件sha1校验
*/
public boolean quickVerify;

/**
* 线程池(可选)
*/
public ExecutorService threadPool;

/**
* 用户自定义公钥(必选)
*/
private String publickKey;

/**
* 调用loadUrlAysn方法时，是否检查更新，默认为true(可选)
*/
private boolean isCheckUpdateOnLoadUrl;
/**
 * 收到push时下载方式
 */
private int downloadModeOnPush;
/**
 * 协议类型{@link com.tencent.tmf.weboffline.api.entitiy.ProtocalType}
 */
private int protocalType;
```

## DefaultUpdateInfoListener
```java
/**
* 接收到离线包推送时忽略
*/
public static final int DOWNLOAD_IGNORE_ON_PUSH = 1;
/**
* 接收到离线包推送时立刻下载离线包
*/
public static final int DOWNLOAD_RIGHTNOW_ON_PUSH = 2;
/**
* 接收到离线包推送时WIFI环境下才下载离线包
*/
public static final int DOWNLOAD_ONLY_WIFI_ON_PUSH = 3;

/**
* @param context
* @param downloadMode 下载方式
*/
public DefaultUpdateInfoListener(Context context, int downloadMode)
```

## IOfflineUpdateCallback
```java
/**
 * 检查更新回调
 * @param code 参考{@link com.tencent.tmf.weboffline.api.OfflineManager}
 * @param updateInfos 更新信息
 */
void update(final int code, final List<UpdateEntity> updateInfos);

/**
 * 下载进度
 * @param progressInfo
 */
void downloadProgress(ProgressEntity progressInfo);

/**
 * 下载回调
 * @param downloadInfo
 * @param
 */
void downloadFinish(DownloadInfo downloadInfo);
```

## AbsLoadUrlCallback
```java
/**
 * 返回离线包加载url
 */
public abstract void onFinish(String url);
```

## OfflineManager
```Java
// 定义更新回调错误码:0成功，1参数出错，2下载更新包出错，3没有sd卡，4其他错误
// 短时间内更新过
public static final int CHECK_CODE_IGNORE_HAD_UPDATE_IN_A_SHORT_TIME = 5;
// 暂无更新（已是最新）
public static final int CHECK_CODE_SUCC_NO_UPDATE = 8;
// 检查更新完成,有更新包
public static final int CHECK_CODE_SUCC_CAN_UPDATE = 10;
// 只在WiFi下更新，当前不是WiFi网络
public static final int CHECK_CODE_ERR_NOT_WIFI = 2;
// 参数错误
public static final int CHECK_CODE_ERR_PARAM = 1;
// 检查更新结果解析出错
public static final int CHECK_CODE_ERR_RESP_NULL = 11;
// 检查更新结果解析出错
public static final int CHECK_CODE_ERR_RESP_PARSE_ERROR = 12;
// 检查更新结果中r字段不为0
public static final int CHECK_CODE_ERR_RESP_RET_ERROR = 13;
// 检查更新结果中没有下载链接
public static final int CHECK_CODE_ERR_RESP_NO_URL = 14;
// URL中没有_bid参数，无法获取离线包id
public static final int CHECK_CODE_ERR_URL_WITHOUT_BID = 15;
// 网络通道的错误
public static final int CHECK_CODE_ERR_NETWORK_CHANNEL_ERROR = 16;
// 检查更新结果中单个bid的r字段不为0
public static final int CHECK_CODE_ERR_RESP_SUBRET_ERROR = 17;
// 本地已存在
public static final int CHECK_CODE_LOCAL_EXIST = 18;

// 下载离线包的错误码
// 下载离线包成功
public static final int DOWNLOAD_CODE_SUCCESS = 0;
// 内层zip解压出错
public static final int DOWNLOAD_CODE_ERROR_UNPACK = 1;
// 下载后合并差分包出错
public static final int DOWNLOAD_CODE_ERROR_PATCH = 2;
// 下载后解密出错
public static final int DOWNLOAD_CODE_ERROR_DECRYPT = 3;
// 外层zip解压出错
public static final int DOWNLOAD_CODE_ERROR_OUTER_UNPACK = 4;
// 签名或sha-1校验失败
public static final int DOWNLOAD_CODE_ERROR_S_FAIL = 5;
// 整包md5校验失败
public static final int DOWNLOAD_CODE_ERROR_FULL_PACKAGE_CHECK_FAIL = 6;
// 重复下载差分包
public static final int DOWNLOAD_CODE_ERROR_PATCH_DUPLICATE = 7;
// cannot get download filePath
public static final int DOWNLOAD_CODE_ERROR_FILE_PATH = 8;
// 离线包解析异常
public static final int DOWNLOAD_CODE_OFFLINE_PACKAGE_PARSE = 9;
//下载IOEXCEPTION和IllegalAccessException异常
public static final int CODE_DOWNLOAD_IOEXCEPTION = -100000;
//下载EXCEPTION异常
public static final int CODE_DOWNLOAD_EXCEPTION = -100001;
//下载取消
public static final int CODE_DOWNLOAD_CANCEL = -100002;
//没有网
public static final int CODE_NO_NETWORK = -100003;
//下载参数错误
public static final int CODE_PARAM_ERROR = -100004;
//下载目录创建失败
public static final int CODE_DOWNLOAD_DIR_CREATE_FAIL = -100005;

/**
 * 使用默认配置初始化
 *
 * @param context
 */
public static void init(Context context)

/**
 * 初始化
 *
 * @param context
 * @param config
 */
public static void init(Context context, OfflineConfig config)

/**
 * 检查所有最新离线包的更新
 *
 * @param updateSetting
 * @param callback
 */
public void checkAllUpdate(UpdateSetting updateSetting, final IOfflineUpdateCallback callback);

/**
 * 检查最新离线包的更新
 *
 * @param bids 离线包id列表
 * @param updateSetting 更新设置
 * @param callback 回调
 */
public void checkLatestUpdate(final List<String> bids, UpdateSetting updateSetting,
final IOfflineUpdateCallback callback)

/**
 * 检查最新离线包的更新
 *
 * @param bid 离线包id
 * @param updateSetting 更新设置
 * @param callback 回调
 */
public void checkLatestUpdate(final String bid, UpdateSetting updateSetting,
      final IOfflineUpdateCallback callback)

/**
 * 通过url检查最新离线包的更新
 *
 * @param url url
 * @param updateSetting 检查更新设置
 * @param callback 回调
 */
public void checkUpdateByUrl(final String url, UpdateSetting updateSetting, final IOfflineUpdateCallback callback)

/**
 * url转换，实现fallback url地址转换
 *
 * @param url
 * @param callback
 */
public void loadUrlAysn(final String url, final SimpleCallback<String> callback)

/**
 * 拦截资源
 *
 * @param url 资源url
 * @return null：本地资源不存在
 */
public TMFWebResourceResponse shouldInterceptRequest(String url)

/**
 * 清理所有的离线包数据
 *
 * @param context
 * @param callback
 */
public static void deleteAllOfflineData(final Context context, final SimpleCallback<Integer> callback)

/**
 * 清理指定离线包(同步接口)
 *
 * @param businessIds 要清理的离线包id列表
 * @return 清理成功的离线包id列表
 */
public static List<String> deleteBiz(final Context context, final List<String> businessIds)

/**
 * 清理指定离线包
 *
 * @param callback 是否成功清理，如果本来就没有对应的离线数据也算清除成功
 */
public static void deleteBiz(final Context context, final String businessId,
final SimpleCallback<Integer> callback)

/**
 * 获取本地离线包的配置
 */
public static void getBizConfig(final Context context, final String businessId,
final SimpleCallback<JSONObject> callback)

/**
 * 获取上次更新离线包的时间戳
 */
public static void getBizUpdateTime(final Context context, final String businessId,
final SimpleCallback<Long> callback)

/**
 * 获取本地离线包的配置
 */
public static void getBizConfig(final Context context, final String businessId,
final SimpleCallback<JSONObject> callback)

/**
 * 获取本地离线包的版本
 */
public static String getBizVersion(final Context context, final String businessId)

/**
 * 获取主bid
 *
 * @param url
 * @return
 */
public static String getBusinessId(String url)

/**
 * 获取本地离线包的版本
 *
 * @param context
 * @param callback
 */
public static void getLocalOfflineVersions(final Context context, final SimpleCallback<String> callback)

/**
 * 从assets解压预置的离线包
 *
 * @param context
 * @param businessId
 * @param callback callback返回-1表示解压失败，0表示成功
 */
@Deprecated
public static void releaseBizFromAssets(final Context context, final String businessId,
final SimpleCallback<Integer> callback)
```
