返回错误码描述。
``` html
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

