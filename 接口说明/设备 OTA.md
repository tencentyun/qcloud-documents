
## 什么是OTA升级
OTA 升级模块用于实现设备主动或者通过小微 App 控制设备进行固件或 Apk 升级。、

腾讯云小微硬件开放平台支持配置强制升级和非强制升级，强制升级一般用于修复重大安全隐患的更新，这两种方式都会以小红点的方式在小微 App 上提示用户设备有升级信息。在配置升级信息时，您还需要注意配置平台支持正式和测试这两种配置方式，正式配置意味着所有设备都能收到升级更新，而测试配置只有特定的设备(根据设备的 sn 来区分)才会收到升级更新。

## 前后台流程

### 设备端主动查询

[![设备端主动查询](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ota_1.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ota_1.png)</div>

1.  开发者在硬件开放平台上传升级包并配置升级信息；

2.  设备端主动去查询配置平台检测升级信息，根据设备初始化时填入的productVersion参数作为当前设备版本与配置平台配置的目标版本做比较确定是否需要升级；

3.  若需要升级的话，设备端会收到更新通知，并根据当前设备的条件决定是否进行升级；

4.  若设备确认升级的话，下载升级文件，并进行升级替换操作。

### 小微 App 推送更新

[![小微 App 推送更新](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ota_2.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ota_2.png)

1.  开发者在硬件开放平台上传升级包并配置升级信息；

2.  小微 App 在进入设备详情页面后会自动去检测升级信息，根据设备初始化时填入的productVersion参数作为当前设备版本与配置平台配置的目标版本做比较确定是否需要升级；

3.  小微 App 检测到升级信息通知设备下载升级文件；

4.  设备收到更新通知后，根据当前设备的条件决定是否进行升级；

5.  若设备确认升级的话，下载升级文件，并进行升级替换操作。

### 后台推送更新

[![后台推送更新](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ota_3.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ota_3.png)

1.  开发者在硬件开放平台上传升级包并配置升级信息；

2.  开发者可以直接平台针对特定设备推送升级信息。

**备注**：目前硬件开放平台还不支持后台推送更新。

## 用户操作体验

下图分别为小微 App 中的升级提示界面和升级操作界面：

[![用户操作体验](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ota_4.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ota_4.png)</div>

## 如何对接

### Linux SDK 代码对接

在 Linux 设备中接入 OTA 模块首先需要在设备 SDK 初始化的时候同时设置 OTA 升级模块监听器。当设备有更新信息时，会通过该监听器回调通知。

```
// 新的OTA通知
typedef struct _tx_ota_result
{
    /**
     * 收到OTA更新信息
     *
     * @param from    来源 0 定时自动检测 1 App操作 2 ServerPush 3 设备主动查询
     * @param force   是否强制升级
     * @param version 版本号
     * @param title   更新标题
     * @param desc    更新详情
     * @param url     下载链接
     */
    void (*on_ota_result)(int from, bool upgrade, unsigned int version, const char* title, const char* desc, const char* url);                  //SDK状态回调
} tx_ota_result;

/**
 * 配置ota信息的回调
 * @param callback
 */
void tx_config_ota(tx_ota_result* callback);

/**
 * 主动查询OTA升级信息
 */
int tx_query_ota_update();
```

### Android SDK 代码对接

与Linux设备一样，在 Android 设备中接入 OTA 模块首先需要在设备 SDK 初始化的时候同时设置 OTA 升级模块监听器。当设备有更新信息时，会通过该监听器回调通知。

```
/**
 * OTA更新的事件监听器
 */
 public interface OnDeviceOTAEventListener {

    /**
     * 收到OTA更新信息
     *
     * @param from    来源 0 定时自动检测 1 App操作 2 ServerPush 3 设备主动查询
     * @param force   是否强制升级
     * @param version 版本号 {@link TXLoginInfo#productVersion}
     * @param title   更新标题
     * @param desc    更新详情
     * @param url     下载链接
     */
    void onOTAInfo(int from, boolean force, int version, String title, String desc, String url);
}

/**
 * 设置OTA更新的事件监听器
 *
 * @param listener {@link OnDeviceOTAEventListener}
 */
public static void setOnDeviceOTAEventListener(OnDeviceOTAEventListener listener);

/**
 * 设备端主动查询OTA升级信息，只有在有更新的时候才会回调{@link OnDeviceOTAEventListener}
 */
public static int queryOtaUpdate();
```

## 验证流程
1.  首先准备升级的固件包，注意设备初始化时填入的`productVersion`参数是设备的当前版本号(int型），升级流程会以此版本号与配置平台配置的目标版本号对比确认是否需要升级；

2. 接下来配置升级信息，配置的版本号要大于需要升级的设备的版本号，该版本号以下的设备均会收到升级通知：

3. 接下来可以到小微 App 的设备详情页进行测试，见用户操作体验栏中的示例图。

[![OTA配置](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ota_5.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ota_5.png)
