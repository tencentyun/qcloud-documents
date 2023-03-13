## MiniCode
返回错误码描述。
```
/**
 * 成功
 */
public static final int CODE_OK = 0;

//////////////////////////////扫码解析code/////////////////////////////////
/**
 * requestCode不符
 */
public static final int CODE_REQUEST_CODE_ERROR = -10000;
/**
 * 扫码返回Intent空
 */
public static final int CODE_QRCODE_INTENT_NULL = -10001;
/**
 * qrcode空
 */
public static final int CODE_QRCODE_NULL = -10002;
/**
 * 非tmf小程序二维码
 */
public static final int CODE_QRCODE_INVALIDATE = -10003;
/**
 * 二维码内容格式错误
 */
public static final int CODE_QRCODE_FORMAT_ERROR = -10004;
/**
 * appId空
 */
public static final int CODE_APPID_EMPTY = -10005;
/**
 * 二维码解析异常
 */
public static final int CODE_EXCEPTION = -10006;
/**
 * 未找到扫码服务，请检查是否添加了qrcode相关sdk
 */
public static final int CODE_NOT_FOUND_QRCODE_SERVICE = -10007;
/**
 * http小程序二维码解析错误
 */
public static final int CODE_HTTP_QRCODE_PARSE_ERROR = -10008;
/**
 * bad query result
 */
public static final int CODE_HTTP_QRCODE_BAD_QUERY_RESULT = -10009;
/**
 * exception
 */
public static final int CODE_HTTP_QRCODE_EXCEPTION = -10010;
/**
 * returnCode error
 */
public static final int CODE_HTTP_QRCODE_RETURNCODE_ERROR = -10011;
/**
 * data null
 */
public static final int CODE_HTTP_QRCODE_DATA_NULL = -10012;
/**
 * shark null
 */
public static final int CODE_HTTP_QRCODE_SHARK_NULL = -10013;
/**
 * businessId null
 */
public static final int CODE_HTTP_QRCODE_BUSINESSID_NULL = -10014;

//////////////////////////////小程序信息获取code/////////////////////////////////
/**
 * 登录类型错误
 */
public static final int CODE_APPLET_INFO_LOGINTYPE_ERROR = -10100;

/**
 * 调试小程序只能使用开发者账号
 */
public static final int CODE_APPLET_INFO_OPERATE_ACCOUNT_PREVIEW_ERROR = -10101;

/**
 * 登录信息空
 */
public static final int CODE_APPLET_INFO_LOGIN_INFO_EMPTY = -10102;

/**
 * create req error
 */
public static final int CODE_APPLET_INFO_JSON_EXCEPTION = -10103;

/**
 * shark error
 */
public static final int CODE_APPLET_INFO_SHARK_ERROR = -10104;

/**
 * create MiniAppInfo ByQrCode error
 */
public static final int CODE_APPLET_INFO_CREATE_MINIAPPINFO_ERROR = -10105;

//////////////////////////////小程程序检查更新code/////////////////////////////////
/**
 * 小程序下架或无可用小程序
 */
public static final int STATUS_CODE_SERVER_REQUEST_DELETE = 10200;
/**
 * 无更新
 */
public static final int STATUS_CODE_NO_UPDATE = 10201;
/**
 * shark实例空
 */
public static final int STATUS_CODE_SHARK_IS_NULL = -10202;
/**
 * 网络错误
 */
public static final int STATUS_CODE_NETWORK_CHANNEL_ERROR = -10203;
/**
 * 检查更新返回类型错误
 */
public static final int STATUS_CODE_UPDATE_TYPE_ERROR = -10204;
/**
 * 检查更新异常
 */
public static final int STATUS_CODE_UPDATE_EXCEPTION = -10205;

//////////////////////////////小程序下载code/////////////////////////////////
/**
 * 小程序下载信息错误
 */
public static final int STATUS_CODE_FILE_INFO_ERROR = -10300;

/**
 * 小程序包下载catch异常
 */
public static final int STATUS_CODE_DOWNLOAD_EXCEPTION = -10301;

/**
 * 下载文件不存在
 */
public static final int STATUS_CODE_FILE_NOT_EXIST_ERROR = -10302;
/**
 * MD5校验失败
 */
public static final int STATUS_CODE_MD5_ERROR = -10303;
/**
 * zip解压错误
 */
public static final int STATUS_CODE_UNZIP_ERROR = -10304;
/**
 * 移动文件过程文件不存在错误
 */
public static final int STATUS_CODE_TMFAPKG_FILE_NOT_EXIST_ERROR = -10305;
/**
 * 移动文件失败
 */
public static final int STATUS_CODE_MOVE_ERROR = -10306;
/**
 * 小程序包下载后解析catch异常
 */
public static final int STATUS_CODE_PARSE_PKG_EXCEPTION = -10307;
/**
 * 文件下载器下载失败
 */
public static final int STATUS_CODE_DOWNLOAD_ERROR = -10308;


public static final int STATUS_CODE_UPDATE_EXCEPTION_ERROR = -10309;

//////////////////////////////登录和登出code/////////////////////////////////
/**
 * json异常
 */
public static final int CODE_JSON_EXCEPTION = -10400;
/**
 * 网关失败
 */
public static final int CODE_SHARK_FAIL = -10401;
/**
 * 网关返回数据为空
 */
public static final int CODE_RESP_NULL = -10402;
/**
 * 开放平台登录返回错误
 */
public static final int CODE_OPEN_LOGIN_RESP_ERROR = -10403;
/**
 * 开放平台登录返回数据空
 */
public static final int CODE_OPEN_LOGIN_DATA_NULL = -10404;
/**
 * 开放平台登录返回租户数据空
 */
public static final int CODE_OPEN_LOGIN_TENANT_NULL = -10405;
/**
 * 运行平台登录返回数据空
 */
public static final int CODE_OPERATE_LOGIN_DATA_NULL = -10406;
/**
 * logout异常
 */
public static final int CODE_LOGOUT_EXCEPTION = -10407;
/**
 * 服务端json数据解析异常
 */
public static final int CODE_PARSE_JSON_EXCEPTION = -10408;

//////////////////////////////搜索code/////////////////////////////////
/**
 * 搜索创建req json异常
 */
public static final int CODE_SEARCH_JSON_EXCEPTION = -10500;
/**
 * 搜索resp为空
 */
public static final int CODE_SEARCH_RESP_NULL = -10501;
/**
 * 搜索resp.data为空
 */
public static final int CODE_SEARCH_RESP_DATA_NULL = -10502;
/**
 * 搜索解析resp.data为错误
 */
public static final int CODE_SEARCH_PARSE_RESP_ERROR = -10503;
/**
 * 搜索网路retCode.errorCode错误
 */
public static final int CODE_SEARCH_SHARK_ERROR = -10504;
/**
 * 搜索返回JSON_EXCEPTION
 */
public static final int CODE_SEARCH_RESP_DATA_JSON_EXCEPTION = -10505;

//////////////////////////////启动mini app/////////////////////////////////
/**
 * doStartMiniApp exception
 */
public static final int CODE_DO_START_MINI_APP_THROWABLE = -10600;
```

## MiniApp
```
小程序信息描述类。
/**
 * 正式小程序
 */
public static final int TYPE_ONLINE = MiniSDKConst.ONLINE;
/**
 * 调试小程序
 */
public static final int TYPE_DEVELOP = MiniSDKConst.DEVELOP;
/**
 * 预览小程序
 */
public static final int TYPE_PREVIEW = MiniSDKConst.PREVIEW;
/**
 * 小程序id
 */
public String appId;
/**
 * 小程序版本类型(正式、预览、开发版)
 */
public int appVerType;
/**
 * 小程序版本
 */
public String version;
/**
 * 小程序名
 */
public String name;
/**
 * 小程序图标
 */
public String iconUrl;
/**
 * 小程序简介
 */
public String appIntro;
/**
 * 开发者企业名称
 */
public String appDeveloper;
/**
 * 时间戳
 */
public long time;
```

## MiniStartOptions
```
/**
 * 打开小程序时是否强制检查更新，false:优先使用本地缓存，同时异步获取最新数据；true：待网络返回后才打开小程序
 */
public boolean isForceUpdate = false;
/**
 * 入口地址
 */
public String entryPath;
/**
 * 接受小程序启动过程中错误情况
 */
public ResultReceiver resultReceiver;
```


## MiniScene
```
/**
 * 小程序主入口，「最近使用」列表
 */
public static final int LAUNCH_SCENE_MAIN_ENTRY = 1001;
/**
 * 扫码打开
 */
public static final int LAUNCH_SCENE_QR_CODE_FROM_SCAN = 1011;
/**
 * 搜索打开
 */
public static final int LAUNCH_SCENE_SEARCH = 2005;
```

## SearchOptions
```
/**
 * 搜索关键字，为空时搜索全部小程序
 */
public String keyWord = "";
/**
 * 暂不支持
 */
public int pageIndex;
/**
 * 暂不支持
 */
public int pageSize;
```

## ShareData
```
/**
     * 分享来源，ShareSource中的值
     */
    public int shareSource;
    /**
     * 分享目标， ShareTarget中的值
     */
    public int shareTarget;
    /**
     * 分享面板设置的ID，用于区分分享渠道
     */
    public int shareItemId;
    /**
     * 分享标题
     */
    public String title;
    /**
     * 分享摘要
     */
    public String summary;
    /**
     * 分享图片的路径。为本地图片路径或者网络图片路径
     */
    public String sharePicPath;
    /**
     * 是否为本地图片。如果为True，则sharePicPath为本地图片的路径；否则，sharePicPath为网络图片的路径
     */
    public boolean isLocalPic;
    /**
     * 从服务端获取的字段：分享链接
     */
    public String targetUrl;
    /**
     * 小程序包信息
     */
    protected MiniAppInfo miniAppInfo;
```


## ShareSource
```
public static class ShareSource {

    public static final int INNER_BUTTON = 11; // 来自小程序|小游戏的内部按钮
    public static final int MORE_BUTTON = 12;  // 来自胶囊按钮的更多选项
}
```

## ShareTarget
```
public static class ShareTarget {
    public static final int QQ = 0;// 转发到QQ通讯录
    public static final int QZONE = 1;// 转发到QQ空间
    public static final int WECHAT_FRIEND = 3;//转发到微信好友
    public static final int WECHAT_MOMENTS = 4;//转发到微信朋友圈
}
```

## ShareTarget
```
public static class ShareResult {
    public static final int SUCCESS = 0;// 分享成功
    public static final int FAIL = 1;// 分享失败
    public static final int CANCEL = 2;// 分享取消
}
```







