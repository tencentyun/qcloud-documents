Android 端文字识别 SDK 主要涉及的类有 OcrSDKKit、OcrSDKConfig、OcrType、OcrModeType、ISDKKitResultListener、ISdkOcrEntityResultListener 以及 OCR 识别返回实体类，下面对其支持的 API 做出详细说明。

### OcrSDKKit

 OcrSDKKit 是文字识别 OCR 的对外接口类，文字识别功能主要集中在这个类中。

| API                                                 | 功能描述                |
| --------------------------------------------------- | :---------------------- |
| [getInstance()](#getInstance())                     | 创建 OcrSDKKit 的单例     |
| [release()](#release())                             | 主动释放资源            |
| [getVersion()](#getVersion())                       | 获取当前 SDK 的版本号信息 |
| [initWithConfig()](#initWithConfig())               | 初始化 SDK 配置信息       |
| [updateFederationToken()](#updateFederationToken()) | 主动更新临时密钥        |
| [startProcessOcr()](#startProcessOcr())                      | 启动 OCR 识别，返回 JsonString           |
| [startProcessOcrResultEntity()](#startProcessOcrResultEntity()) | 启动 OCR 识别，返回不同模式对应实体对象 |

#### [getInstance()](id:getInstance())

```java
public static OcrSDKKit getInstance()
```
- 功能描述：
创建 OcrSDKKit 的单例。
- 返回结果：
 OcrSDKKit 的单例对象。	



#### [release()](id:release())

```java
public void release()
```

- 功能描述：
主动释放资源的方法，可在退出应用或者需要清理资源的时候调用。




#### [getVersion()](id:getVersion())

```java
public final String getVersion() 
```

- 功能描述：
获取 SDK 当前的版本号。
- 返回结果：
当前 SDK 的版本信息。




#### [initWithConfig()](id:initWithConfig())

```java
public void initWithConfig(Context context, OcrSDKConfig config)
```

- 功能描述：
初始化 SDK 信息。
- 传入参数：

| 参数类型                      | 参数名称 | 参数含义            |
| ----------------------------- | -------- | ------------------- |
| Context                       | context  | 应用的上下文信息    |
| [OcrSDKConfig](#OcrSDKConfig) | config   | SDK 配置参数的实体类 |




#### [updateFederationToken()](id:updateFederationToken())

```java
public void updateFederationToken(final String tmpSecretId, final String tmpSecretKey,final String token)
```

- 功能描述：
主动更新临时密钥信息，在您与服务器兑换得到临时密钥之后主动调用设置。
- 传入参数：

| 参数类型 | 参数名称     | 参数含义              |
| -------- | ------------ | --------------------- |
| String   | tmpSecretId  | 临时密钥 SecretId      |
| String   | tmpSecretKey | 临时密钥 SecretKey     |
| String   | token        | 兑换后的临时访问 token |




#### [startProcessOcr()](id:startProcessOcr())

```java
public void startProcessOcr(Activity activity, OcrType ocrType, CustomConfigUi customConfigUi, ISDKKitResultListener resultListener)
```

- 功能描述：
启动默认界面进行 OCR 识别，可进行部分 UI 元素的自定义配置。(**如 CustomConfigUi 传入 null，可使用默认 UI 配置**)
- 传入参数：

| 参数类型                                        | 参数名称       | 参数含义                                                     |
| ----------------------------------------------- | -------------- | ------------------------------------------------------------ |
| Activity                                        | activity       | 启动 OCR 默认界面的当前界面 Activity 对象                        |
| [OcrType](#OcrType)                             | ocrType        | 启动的 OCR 识别类型                                            |
| [CustomConfigUi](#CustomConfigUi)               | customConfigUi | 启动默认界面时候传入的界面配置参数，如需完全使用默认配置，可传入 null |
| [ISDKKitResultListener](#ISDKKitResultListener) | resultListener | 用于接收 OCR 识别结果的回调对象                                |



#### [startProcessOcrResultEntity()](id:startProcessOcrResultEntity())

```java
public <T extends OcrResult> void startProcessOcrResultEntity(Activity activity, OcrType ocrType,CustomConfigUi customConfigUi, Class<T> entity,ISdkOcrEntityResultListener<T> ocrEntityResultListener) 
```

- 功能描述：
启动默认界面进行 OCR 识别，可进行部分 UI 元素的自定义配置。(**如 CustomConfigUi 传入 null，可使用默认 UI 配置**)，根据指定不同的识别模式返回不同识别结果类型实体。
- 传入参数：

| 参数类型                                                    | 参数名称                | 参数含义                                                     |
| ----------------------------------------------------------- | ----------------------- | ------------------------------------------------------------ |
| Activity                                                    | activity                | 启动 OCR 默认界面的当前界面 Activity 对象                    |
| [OcrType](#OcrType)                                         | ocrType                 | 启动的 OCR 识别类型                                          |
| [CustomConfigUi](#CustomConfigUi)                           | customConfigUi          | 启动默认界面时候传入的界面配置参数，如需完全使用默认配置，可传入 null |
| Class < T >                                                 | entity                  | OCR 识别结果的实体类                                          |
| [ISdkOcrEntityResultListener](#ISdkOcrEntityResultListener) | ocrEntityResultListener | 用于接收 OCR 识别结果的回调对象                              |
| < T > extends OcrResult                                     | < T >                   | OCR 识别识别结果 OcrResult 的子类型                          |

OCR 识别结果的实体类，OCR 识别识别结果 OcrResult 的子类型

### [OcrSDKConfig](id:OcrSDKConfig)

OcrSDKConfig 是在 OCR 初始化时需要传入的 SDK 的配置信息实体类，采用构建者 builder 的方式进行参数配置。

支持参数及其默认值如下：

| 类型                | 名称             | 含义                                                         | 默认值                                         |
| ------------------- | ---------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| [OcrType](#OcrType) | ocrType          | 默认识别类型                                                 | IDCardOCR_FRONT，IDCardOCR_BACK 均代表 id_card |
| int                 | cardType         | 身份证模式时正反面0正，1反                                   | 0正面                                          |
| int                 | modeType         | 识别模式类型：0代表手动拍摄模式，1代码自动捕获模式，2代表自动+手动模式（先使用自动超时后转为手动拍照模式） | 2代表自动 + 手动模式                           |
| int                 | autoTimeout      | 自动捕获超时（毫秒单位，最少设置5秒，内部上限30秒）          | 20000毫秒                                      |
| String              | resultUrl        | 发送识别请求的 ResultUrl 信息                                | https://ocr.tencentcloudapi.com/               |
| String              | secretId         | 请求使用的密钥信息（如果使用固定密钥模式，可传入固定密钥）   | 空                                             |
| String              | secretKey        | 请求使用的密钥信息（如果使用固定密钥模式，可传入固定密钥）   | 空                                             |
| String              | tempToken        | 请求使用的临时 token 信息                                    | 空                                             |
| boolean             | cropIdCard       | 开启身份证照片裁剪（去掉证件外多余的边缘、自动矫正拍摄角度）开关 | false                                          |
| boolean             | cropPortrait     | 开启人像照片裁剪（自动抠取身份证头像区域）                   | false                                          |
| boolean             | copyWarn         | 开启复印件告警                                               | false                                          |
| boolean             | borderCheckWarn  | 开启边框和框内遮挡告警                                       | false                                          |
| boolean             | reshootWarn      | 开启翻拍告警                                                 | false                                          |
| boolean             | detectPsWarn     | 开启 PS 检测告警                                             | false                                          |
| boolean             | tempIdWarn       | 开启临时身份证告警                                           | false                                          |
| boolean             | invalidDateWarn  | 开启身份证有效日期不合法告警                                 | false                                          |
| boolean             | quality          | 开启图片质量分数（评价图片的模糊程度）                       | false                                          |
| String              | retImageType     | 图像预处理，检测图片倾斜的角度，将原本倾斜的图片围绕中心点转正，最终输出一张正的名片抠图。 | 空                                             |
| boolean             | canCancelWaiting | 允许在识别过程中（出现loading提示框），点击back主动取消      | false                                          |
| boolean | isOpenClipImage | 选择图片时是否启用采集功能 | true |
| boolean             | retBorderCutImage | 银行卡专用，是否返回预处理（精确剪裁对齐）后的银行卡图片数据    | false |
| boolean             | retCardNoImage    | 银行卡专用，是否返回卡号的切图图片数据，默认false。    | false |
| boolean             | enableQualityValue | 银行卡专用，是否返回图片质量分数（图片质量分数是评价一个图片的模糊程度的标准）    | false |

### [OcrType](id:OcrType)

OcrType 是一个枚举类型，列举了当前文字识别 OCR 的 SDK 所支持业务类型的种类，大致如下：

| OcrType类型                     | 代表含义               | 对应结果实体类                                        |
| ------------------------------- | ---------------------- | ----------------------------------------------------- |
| OcrType.IDCardOCR_FRONT         | 身份证人像面识别模式   | [IdCardOcrResult](#IdCardOcrResult)                   |
| OcrType.IDCardOCR_BACK          | 身份证国徽面识别模式   | [IdCardOcrResult](#IdCardOcrResult)                   |
| OcrType.BankCardOCR             | 银行卡正面识别模式     | [BankCardOcrResult](#BankCardOcrResult)               |
| OcrType.BusinessCardOCR         | 名片卡正面识别模式     | [BusinessCardOcrResult](#BusinessCardOcrResult)       |
| OcrType.VinOCR                  | 车辆的 VIN 识别模式      | [VinOcrResult](#VinOcrResult)                         |
| OcrType.LicensePlateOCR         | 车辆的车牌识别模式     | [CarLicensePlateResult](#CarLicensePlateResult)       |
| OcrType.DriverLicenseOCR_FRONT  | 驾驶证主页识别模式     | [DriverLicenseCardResult](#DriverLicenseCardResult)   |
| OcrType.DriverLicenseOCR_BACK   | 驾驶证副页识别模式     | [DriverLicenseCardResult](#DriverLicenseCardResult)   |
| OcrType.VehicleLicenseOCR_FRONT | 行驶证主页识别模式     | [VehicleLicenseCardResult](#VehicleLicenseCardResult) |
| OcrType.VehicleLicenseOCR_BACK  | 行驶证副页识别模式     | [VehicleLicenseCardResult](#VehicleLicenseCardResult) |
| OcrType.GENERAL_VIN | 车辆的VIN码通用识别模式（主要推荐拍照模式使用） | [VinOcrResult](#VinOcrResult) |
| OcrType.IDCardOCR_HK03 | 香港身份证03版本识别模式 | [HKIDCardOcrResult](#HKIDCardOcrResult) |
| OcrType.IDCardOCR_HK18 | 香港身份证18版本识别模式 | [HKIDCardOcrResult](#HKIDCardOcrResult) |
| OcrType.Exit_Entry_HK_Macao_Card | 港澳台通行证识别模式 | [PermitOcrResult](#PermitOcrResult) |
| OcrType.MLID_PASSPORT | 国际护照识别模式 | [MLIDPassportOcrResult](#MLIDPassportOcrResult) |
| OcrType.HMT_RESIDENT_PERMIT_OCR | 港澳台居住证 | [HmtResidentPermitOcrResult](#HmtResidentPermitOcrResult) |



### OcrModeType

OcrModeType 是一个枚举类型，列举了卡片识别模式

| OcrModeType 类型        | 代表含义                                           |
| ---------------------- | -------------------------------------------------- |
| OCR_DETECT_MANUAL      | 手动拍摄模式                                       |
| OCR_DETECT_AUTO_MANUAL | 自动识别模式（tips：20s后提示 是否切换到手动拍摄） |



###  [LanguageStyle](id:LanguageStyle)

LanguageStyle 是一个枚举类型，列举了支持的语言类型

| LanguageStyle 类型 | 代表含义                                           |
| ---------------------- | -------------------------------------------------- |
| AUTO   | 跟随系统语言                             |
| ENGLISH | 英文 |
| SIMPLIFIED_CHINESE | 简体中文 |




### [CustomConfigUi](id:CustomConfigUi)

此为用户自定义 UI 的配置类，当前支持配置的属性如下表所示，可以通过 javabean set 的方式设置。

| 类型    | 名称                     | 含义                                                         |
| ------- | ------------------------ | ------------------------------------------------------------ |
| boolean | isShowTitleBar           | 设置是否显示默认界面的标题栏                                 |
| String  | titleBarText             | 设置标题栏显示的文字内容                                     |
| int     | titleColor               | 设置标题栏背景颜色（0xFFFFFF类型）                           |
| String  | remindDialogText         | 设置提醒 dialog 信息文字内容                                 |
| int     | remindDialogTextColor     | 设置提醒dialog信息文字颜色（0xFFFFFF类型）                   |
| int     | remindDialogTextSize      | 设置提醒dialog信息文字大小                                   |
| int     | remindDialogConfirmColor | 设置提醒 dialog 中确认按钮（切换模式）的颜色（0xFFFFFF类型） |
| String  | remindDialogConfirmText   | 设置提醒dialog中确认按钮的文字内容                           |
| int     | remindDialogCancelColor   | 设置提醒dialog中取消按钮的颜色（0xFFFFFF类型）               |
| String  | remindDialogCancelText    | 设置提醒dialog中取消按钮的文字内容                           |
| boolean | remindDialogShowTitle     | 是否显示提示dialog的title                                    |
| int     | cardFrameColor           | 设置卡片预览框四角选中时的颜色（0xFFFFFF类型）               |
| int     | successRemindTextColor   | 设置自定捕捉或拍摄成功后，提示的文字颜色（0xFFFFFF类型）     |
| Int     | statusBarColor           | 设置状态栏背景颜色（0xFFFFFF类型）                           |
| boolean | isShowStatusBar           | 设置默认界面是否显示状态栏，默认true                         |
| int     | imageSelectResId         | 设置默认界面中图库中图片选择的图标资源 id                    |
| int     | lightImageOnResId        | 设置默认界面打开闪光灯的图标资源 id                          |
| int     | lightImageOffResId       | 设置默认界面关闭闪光灯的图标资源 id                          |
| int     | takePicturesResId        | 设置默认界面主动拍照按钮的图标资源 id                        |
| int     | backActionIconResId      | 设置默认界面返回按钮的图标资源id                             |
| boolean | isRemoveAlbum            | 设置默认界面是否显示相册选取按钮，默认为显示                 |
| boolean | isRemoveFlash            | 设置默认界面是否显示闪光灯点击按钮，默认显示                 |
| boolean | isLandscape              | 设置默认界面为横屏模式，默认false                            |
| boolean | isShowTips               | 设置默认界面是否显示tips框，默认true                         |
| String  | showTipsText             | 设置提醒tips的文字内容，默认“请避免识别内容折角、遮挡和反光”（不超过15字）  |
| boolean | isShowStatusBar          | 设置默认界面是否显示状态栏，默认true                         |
| int     | showTipsTextColor         | 设置提醒tips的文字颜色（0xFFFFFF类型）                       |
| int     | showTipsTextSize          | 设置提醒tips的文字大小                                       |
| boolean | isShowTipsIcon            | 设置是否显示提醒tips上的icon图标                             |
| boolean | isShowTipsBackground      | 置是否显示提醒tips的背景框                                   |
| int     | portraitLayoutResId       | 竖屏布局的资源id，具体使用方法参考[自定义UI布局](#自定义UI布局) |
| int     | landscapeLayoutResId      | 横屏布局的资源id，具体使用方法参考[自定义UI布局](#自定义UI布局) |
| boolean | useDeepColorStatusBarIcon | 是否使用深色的状态栏图标与文字（配合浅色状态栏颜色使用），默认false |
| String  | bottomTipsContext         | 预览框自带下方tips的内容的动态设置**（"\n"，可以主动换行）** |

### [自定义 UI 布局](id:自定义UI布局)

OCR SDK支持自定义UI布局，SDK会提供默认的竖屏布局文件**demo_ocr_detect_fragment.xml**和横屏布局文件**demo_ocr_detect_hor_fragment.xml**，集成方可以在此基础上进行做UI的修改。**不要删除或者修改默认的view与view对应的id**，

相关资源可以在SDK提供的安装包的**res文件夹**内获取

下面提供了一份竖屏的默认布局文件：

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#000000"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <!--  相机的预览View -->
    <TextureView
        android:id="@+id/camera_surface_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

    <!--  整体的遮照View以及识别框  -->
    <com.tencent.ocr.sdk.component.CameraMaskView
        android:id="@+id/ocr_mask_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:txy_line_color="@color/blue"
        app:txy_line_length="30dp"
        app:txy_line_margin="5dp"
        app:txy_line_padding="0dp"
        app:txy_line_width="3dp"
        app:txy_maskView_view_type="id_back"
        app:txy_mask_color="@color/grey_text"
        app:txy_mask_margin="90dp"
        app:txy_position_flag="margin"
        app:txy_tip_color="@color/white"
        app:txy_tip_margin="20dp"
        app:txy_tip_size="15sp" />

    <!--  自定义的Tips显示界面  -->
    <com.tencent.ocr.sdk.component.OcrDetectTipsView
        android:id="@+id/ocr_tips_tv"
        android:layout_width="wrap_content"
        android:layout_height="40dp"
        android:layout_alignParentTop="true"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="370dp" />

    <!--  底部三个按钮对应的界面 -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_alignParentBottom="true"
        android:layout_marginStart="30dp"
        android:layout_marginEnd="30dp"
        android:layout_marginBottom="26dp"
        android:gravity="center_vertical|center_horizontal"
        android:orientation="horizontal">
        <!--  相册选择按钮   -->
        <ImageButton
            android:id="@+id/album_image_button"
            android:layout_width="40dp"
            android:layout_height="40dp"
            android:layout_marginRight="50dp"
            android:background="@drawable/demo_txy_ocr_photo_album" />

        <!--  进行拍照按钮   -->
        <ImageButton
            android:id="@+id/take_picture_button"
            android:layout_width="80dp"
            android:layout_height="80dp"
            android:background="@drawable/demo_txy_ocr_take_pictures" />

        <!-- 闪光灯按钮  -->
        <ImageButton
            android:id="@+id/light_image_button"
            android:layout_width="40dp"
            android:layout_height="40dp"
            android:layout_marginStart="50dp"
            android:background="@drawable/demo_txy_ocr_light_off" />
    </LinearLayout>

    <!-- 默认返回按钮对应的View  -->
    <ImageView
        android:visibility="invisible"
        android:id="@+id/txy_detect_back"
        android:layout_marginTop="16dp"
        android:layout_marginStart="10dp"
        android:src="@drawable/txy_action_back"
        android:layout_width="32dp"
        android:layout_height="32dp"/>

    <!-- 上层的title布局   -->
    <include layout="@layout/demo_show_title_bar"/>
</RelativeLayout>
```

如果添加在默认布局上添加了view，有需要对view进行控制的话，可以调用参考下面方式进行注册：

```java
OcrSDKKit.getInstance().setOcrEventListener(new OcrEventListener() {
    @Override
    public void onMainViewCreate(View mainView) {
        // 界面创建的回调（主线程）
        if (mainView != null) {
            Button button = mainView.findViewById(R.id.demo_test_button);
            // button事件的注册与处理，注意View的判空！
            button.setOnClickListener(v -> {
               Log.e(TAG, "click");
            });
        }
    }

    @Override
    public void onMainViewDestroy() {
        // 界面销毁的回调（主线程）
    }
});
```



### 修改CameraMaskView

CameraMaskView是主体的遮罩组件，提供使用属性配置的方式进行修改，直接在xml里进行操作即可目前已支持的属性如下表：

| 属性                                       | 类型                                    | 含义                                                         |
| ------------------------------------------ | --------------------------------------- | ------------------------------------------------------------ |
| txy_mask_color                             | color\|reference                        | 外部蒙层的默认颜色                                           |
| txy_tip_text                               | string\|reference                       | 默认的提示文本                                               |
| txy_tip_color                              | color\|reference                        | 上方提示文字的颜色（默认）                                   |
| txy_tip_light_color                        | color\|reference                        | 上方提示文字的颜色（正确提醒）                               |
| txy_tip_error_color                        | color\|reference                        | 上方提示文字的颜色（异常提醒）                               |
| txy_tip_size                               | integer\|dimension                      | 上方提示文字的大小                                           |
| txy_tip_margin                             | integer\|dimension                      | 上方提示文字距离选择框的距离                                 |
| txy_tip_textStyle                          | enum[normal、bold、italic、bold_italic] | 上方提示的字体样式                                           |
| txy_tip_show                               | boolean                                 | 是否显示上方提示，默认显示                                   |
| txy_line_color                             | color\|reference                        | 选择框的边线颜色(默认)                                       |
| txy_line_light_color                       | color\|reference                        | 选择框的边线颜色(正确提醒)                                   |
| txy_line_error_color                       | color\|reference                        | 选择框的边线颜色(异常提醒)                                   |
| txy_line_width                             | integer\|dimension                      | 选择框边线的宽度                                             |
| txy_line_length                            | integer\|dimension                      | 选择框边线的长度                                             |
| txy_line_padding                           | integer\|dimension                      | 选择框边线距离中心透明框的距离                               |
| txy_line_margin                            | integer\|dimension                      | 选择框边线距离手机屏幕的距离                                 |
| txy_position_flag                          | enum[center、margin]                    | 选择框的位置，center代表居中，margin代表顶部                 |
| txy_mask_margin                            | integer\|dimension                      | txy_position_flag = margin，选择框的距离顶部的位置           |
| txy_mask_view_use_type                     | enum[portrait、landscape]               | portrait代表适配竖屏，landscape适配横屏                      |
| txy_rect_height_weight_hor                 | integer                                 | 仅适用于横屏，中间高度所占屏幕的比例                         |
| txy_front_head_icon                        | reference                               | 正面人像图的替换图@drawable/head                             |
| txy_back_emblem_icon                       | reference                               | 背面徽章图的替换图@drawable/emblem                           |
| txy_bottom_tips_textStyle                  | enum[normal、bold、italic、bold_italic] | 下方提示的字体样式                                           |
| txy_bottom_tips_txt                        | string\|reference                       | 下方提示的默认文本内容，**（"\n"，可以主动换行）**           |
| txy_bottom_tip_size                        | integer\|dimension                      | 下方提示的字体大小                                           |
| txy_bottom_tip_color                       | color\|reference                        | 下方提示的颜色                                               |
| txy_bottom_tip_margin_top                  | integer\|dimension                      | 下方提示距离边线框上方的距离                                 |
| txy_bottom_tip_show                        | boolean                                 | 下方提示是否显示，默认不显示                                 |
| txy_is_show_scanline                       | boolean                                 | 是否显示内置扫描线，默认不显示                               |
| txy_scanline_animator_time                 | integer                                 | 扫描线完成一次扫描动画需要的时间**（单位ms）**，默认1500ms   |
| txy_scanline_start_color                   | color\|reference                        | 扫描线动画区域的起始颜色，0～40%的区域为此颜色               |
| txy_scanline_mid_color                     | color\|reference                        | 扫描线动画区域的过渡颜色，40%～80%为起始颜色与此颜色的渐变效果 |
| txy_scanline_end_color                     | color\|reference                        | 扫描线动画区域的终止颜色，80%～100%为过渡颜色与此颜色的渐变效果 |
| txy_scanline_start_color_size_range        | integer                                 | 从0到这一位置的百分比都是起始颜色，默认40（百分比）          |
| txy_scanline_start_to_mid_color_size_range | integer                                 | txy_scanline_start_color_size_range到这个位置为起始到过渡色的渐变区间，默认80（百分比） |

```xml
<!-- demo里的参考扫描线的颜色 -->
<!--  起始颜色  -->
<color name="txy_scanline_start_color">#00000000</color>
<!--  过渡颜色  -->
<color name="txy_scanline_mid_color">#22F77C61</color>
<!--   终止颜色 -->
<color name="txy_scanline_end_color">#EEF77C61</color>
```

**如果上面和[CustomConfigUi](#CustomConfigUi)传入的属性产生冲突时，CustomConfigUi配置的优先级更高**


### 自定义 Tips 和部分 UI 文字

SDK会提供**demo_tips_string.xml**，如果需要修改tips提示，可以保持key不变，直接修改对应的value。同时最后把demo_tips_string.xml 放到依赖ocr sdk的module的资源下进行打包，Android studio会自动完成资源替换、覆盖。目前支持的替换内容如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- 默认dialog上的信息   -->
    <string name="txy_ocr_cancel">取消</string>
    <string name="txy_ocr_ok">确定</string>
    <string name="txy_ocr_change_mode">切换模式</string>
    <string name="txy_ocr_tips">提示</string>
    <string name="txy_ocr_change_mode_info">未能识别内容，是否切换模式拍照上传?</string>
    <string name="txy_ocr_loading">数据加载中</string>
    <string name="txy_ocr_back">返回</string>
    <string name="txy_ocr_title">标题</string>
    <string name="txy_ocr_setting">设置</string>
    <string name="txy_ocr_permission_info">您已拒绝或禁用权限，请手动授予允许访问</string>
    <string name="txy_ocr_change_mode_manual">已切换至手动拍摄</string>
    <string name="txt_user_cancel_ocr">用户主动停止文字识别</string>
    <string name="txt_inner_sdk_ocr">文字识别内部错误，请重试</string>
    <string name="txt_select_image_error">选择图片发生异常</string>
    <string name="txy_auto_mode_time_out_error">未自动捕获到照片</string>
    <string name="txy_ocr_tip_default_txt">请避免识别内容折角、遮挡和反光</string>
    <!--  OCR识别里的文字信息  -->
    <string name="txy_ocr_tip_please">请将</string>
    <string name="txy_ocr_tip_id_card">身份证</string>
    <string name="txy_ocr_tip_bank_card">银行卡</string>
    <string name="txy_ocr_tip_business_card">名片</string>
    <string name="txy_ocr_tip_card">卡证</string>
    <string name="txy_ocr_tip_car_card">车牌</string>
    <string name="txy_ocr_tip_car_vin">车辆VIN码</string>
    <string name="txy_ocr_tip_driver_license">驾驶证</string>
    <string name="txy_ocr_tip_vehicle_license">行驶证</string>
    <string name="txy_ocr_tip_hold_in_kuang">置于此框内</string>
    <string name="txy_ocr_txt_identify">识别</string>
    <string name="txy_ocr_hk_idcard_03">香港身份证03</string>
    <string name="txy_ocr_hk_idcard_18">香港身份证18</string>
    <string name="txy_ocr_exit_entry_hk_macao_card">港澳通行证</string>
    <!-- 错误信息 -->
    <string name="txy_ocr_error_result_txt">ocr识别请求失败</string>
    <!-- 错误信息 -->
    <string name="txy_ai_camera_open_error">打开相机失败</string>
    <string name="txy_ai_camera_close_error">关闭相机失败</string>
    <string name="txy_ai_camera_preview_error">预览相机失败</string>

    <!--  提示信息  -->
    <string name="ocr_auto_succeed">自动捕获成功，请等待验证结果</string>
    <string name="ocr_manual_succeed">手动捕获成功，请等待验证结果</string>
    <string name="ocr_card_closer">请靠近一些</string>
    <string name="ocr_card_farer">请离远一些</string>
    <string name="ocr_cam_blur">焦距模糊</string>
    <string name="ocr_no_card">请放入</string>
    <string name="ocr_pose_keep">请保持内容在框内</string>
    <string name="ocr_auto_timeout">自动捕获超时</string>
    <string name="ocr_switch_to_auto">自动捕获</string>
    <string name="ocr_switch_to_manual">手动捕获模式，请点击拍照按钮</string>
    <string name="ocr_cam_begin_focus">自动调整焦距</string>
    <string name="ocr_cam_end_focus">调整焦距结束</string>
</resources>
```


### [IdCardOcrResult](id:IdCardOcrResult)

身份证 OCR 识别的结果实体对象

| 类型   | 名称      | 含义     |
| ------ | --------- | -------- |
| String | name      | 姓名     |
| String | sex       | 性别     |
| String | nation    | 民族     |
| String | birth     | 出生日期 |
| String | address   | 住址     |
| String | idNum     | 身份证号 |
| String | authority | 发证机关 |
| String | validDate | 有效日期 |
| String | requestId | 请求 id   |
| String | advancedInfo | 扩展字段内容 [参考官网](https://cloud.tencent.com/document/product/866/33524) |



### [BankCardOcrResult](id:BankCardOcrResult)

银行卡 OCR 识别的结果实体对象

| 类型   | 名称      | 含义     |
| ------ | --------- | -------- |
| String | bankInfo       | 银行信息                   |
| String | cardNo         | 银行卡号                   |
| String | validDate      | 有效日期                   |
| String | requestId      | 请求id                     |
| String | cardType       | 银行卡类型                 |
| String | cardName       | 银行卡名称                 |
| String | borderCutImage | 切片图片数据，取不到为null |
| String | cardNoImage | 卡号图片数据，取不到为null |



### [BusinessCardOcrResult](id:BusinessCardOcrResult)

名片 OCR 识别的结果实体对象，主要包含一些列的 [BusinessCardItems](#BusinessCardItems) 对象。

| 类型                                            | 名称              | 含义         |
| ----------------------------------------------- | ----------------- | ------------ |
| List< [BusinessCardItems](#BusinessCardItems) > | businessCardInfos | 名片元素列表 |
| String                                          | requestId         | 请求 id       |



### [BusinessCardItems](id:BusinessCardItems)

名片 OCR 识别的基本元素，包括名称与信息。

| 类型   | 名称  | 含义     |
| ------ | ----- | -------- |
| String | name  | 子项名称 |
| String | value | 子项内容 |



### [VinOcrResult](id:VinOcrResult)

车辆的 VIN 的识别的结果实体对象

| 类型   | 名称 | 含义        |
| ------ | ---- | ----------- |
| String | vin  | 车辆的 VIN 码 |



### [CarLicensePlateResult](id:CarLicensePlateResult)

| 类型                | 名称       | 含义                         |
| ------------------- | ---------- | ---------------------------- |
| String              | number     | 车牌的字符串信息             |
| int                 | confidence | 本次识别的置信度             |
| [OcrRect](#OcrRect) | rect       | 文本行在原图片中的像素坐标框 |



### [OcrRect](id:OcrRect)

矩形坐标

| 类型 | 名称   | 含义          |
| ---- | ------ | ------------- |
| int  | x      | 左上角x的坐标 |
| int  | y      | 左上角y的坐标 |
| int  | width  | 宽度          |
| int  | height | 高度          |



### [DriverLicenseCardResult](id:DriverLicenseCardResult)

驾驶证识别的结果实体类

| 类型            | 名称              | 含义             |
| --------------- | ----------------- | ---------------- |
| String          | name              | 姓名             |
| String          | sex               | 性别             |
| String          | nationality       | 国籍             |
| String          | address           | 地址             |
| String          | dateOfBirth       | 出生日期         |
| String          | dateOfFirstIssue  | 初次领证日期     |
| String          | classType         | 准驾车类型       |
| String          | startDate         | 有效期开始的时间 |
| String          | endDate           | 有效期截止日期   |
| String          | cardCode          | 证件号           |
| String          | archivesCode      | 档案编号         |
| String          | record            | 记录             |
| String          | issuingAuthority  | 发证单位         |
| List< Integer > | recognizeWarnCode | 识别的警告码列表 |
| List< String >  | recognizeWarnMsg  | 识别的警告码说明 |



### [VehicleLicenseCardResult](id:VehicleLicenseCardResult)

行驶证识别的结果实体类

| 类型                                  | 名称              | 含义                       |
| ------------------------------------- | ----------------- | -------------------------- |
| [VehicleFrontInfo](#VehicleFrontInfo) | vehicleFrontInfo  | 行驶证的主页信息           |
| [VehicleBackInfo](#VehicleBackInfo)   | vehicleBackInfo   | 行驶证的副页信息           |
| List< Integer >                       | recognizeWarnCode | 识别的 Code 告警码列表和释义 |
| List< String >                        | recognizeWarnMsg  | 识别的警告码说明           |



### [VehicleFrontInfo](id:VehicleFrontInfo)

行驶证的主页的识别结果实体类

| 类型   | 名称         | 含义         |
| ------ | ------------ | ------------ |
| String | plateNo      | 号牌号码     |
| String | vehicleType  | 车辆类型     |
| String | owner        | 所有人       |
| String | address      | 住址         |
| String | useCharacter | 使用性质     |
| String | model        | 品牌型号     |
| String | vin          | 车辆识别代号 |
| String | engineNo     | 发动机编号   |
| String | registerDate | 注册日期     |
| String | IssueDate    | 发证日期     |
| String | seal         | 印章         |



### [VehicleBackInfo](id:VehicleBackInfo)

行驶证副页的识别结果实体类

| 类型   | 名称           | 含义         |
| ------ | -------------- | ------------ |
| String | plateNo        | 号牌号码     |
| String | fileNo         | 档案编号     |
| String | allowNum       | 核定人数     |
| String | totalMass      | 总质量       |
| String | curbWeight     | 整备质量     |
| String | loadQuality    | 核定载的质量 |
| String | externalSize   | 外廓尺寸     |
| String | marks          | 备注         |
| String | record         | 检验记录     |
| String | totalQuasiMass | 总牵引质量   |



### [HKIDCardOcrResult](id:HKIDCardOcrResult)

香港身份证03与18版的共同识别结果实体类

| 类型          | 名称             | 含义                                                         |
| ------------- | ---------------- | ------------------------------------------------------------ |
| String        | cnName           | 中文姓名                                                     |
| String        | enName           | 英文姓名                                                     |
| String        | telexCode        | 中文姓名对应电码                                             |
| String        | sex              | 性别 ：“男M”或“女F”                                          |
| String        | birthday         | 出生日期                                                     |
| String        | permanent        | 永久性居民身份证。<br/>0：非永久；<br/>1：永久；<br/>-1：未知。 |
| String        | idNum            | 身份证号码                                                   |
| String        | symbol           | 证件符号，出生日期下的符号，例如"***AZ"                      |
| String        | firstIssueDate   | 首次签发日期                                                 |
| String        | currentIssueDate | 最近领用日期                                                 |
| String        | fakeDetectResult | 真假判断。<br/>0：无法判断（图像模糊、不完整、反光、过暗等导致无法判断）；<br/>1：假；<br/>2：真。<br/>注意：此字段可能返回 null，表示取不到有效值。 |
| List<Integer> | warningCode      | 多重告警码，当身份证是翻拍、复印、PS件时返回对应告警码。<br/>-9102：证照复印件告警<br/>-9103：证照翻拍告警<br/>-9104：证照PS告警<br/>-9105：证照防伪告警 |



### [PermitOcrResult](id:PermitOcrResult)

港澳通行证的识别结果实体类

| 类型   | 名称           | 含义     |
| ------ | -------------- | -------- |
| String | name           | 姓名     |
| String | englishName    | 英文姓名 |
| String | number         | 证件号   |
| String | sex            | 性别     |
| String | validDate      | 有效期限 |
| String | issueAuthority | 签发机关 |
| String | issueAddress   | 签发地点 |
| String | birthday       | 出生日期 |



### [MLIDPassportOcrResult](id:MLIDPassportOcrResult)

国际护照识别结果对应的实体类

| 类型          | 名称             | 含义                                                         |
| ------------- | ---------------- | ------------------------------------------------------------ |
| String        | id               | 护照ID                                                       |
| String        | name             | 姓名                                                         |
| String        | issuingCountry   | 证件号                                                       |
| String        | nationality      | 性别                                                         |
| String        | dateOfBirth      | 出生日期                                                     |
| String        | sex              | 性别（F女，M男）                                             |
| String        | dateOfExpiration | 有效期                                                       |
| List<Integer> | warn             | 告警码<br/>-9103 证照翻拍告警<br/>-9102 证照复印件告警<br/>-9106 证件遮挡告警 |
| String        | image            | 证件图片                                                     |
| String        | advancedInfo     | 扩展字段:<br/>{<br/>ID:{<br/>Confidence:0.9999<br/>},<br/>Name:{<br/>Confidence:0.9996<br/>}<br/>} |
| String        | codeSet          | 最下方第一行 MRZ Code 序列                                   |
| String        | codeCrc          | 最下方第二行 MRZ Code 序列                                   |



### [HmtResidentPermitOcrResult](id:HmtResidentPermitOcrResult)

港澳台居住证识别结果的实体类

| 类型   | 名称      | 含义              |
| ------ | --------- | ----------------- |
| String | name      | 证件姓名          |
| String | sex       | 性别              |
| String | birth     | 出生日期          |
| String | address   | 地址              |
| String | idCardNo  | 身份证号          |
| int    | cardType  | 0-正面<br/>1-反面 |
| String | validDate | 证件有效期限      |
| String | authority | 签发机关          |
| String | visaNum   | 签发次数          |
| String | passNo    | 通行证号码        |




### [ISDKKitResultListener](id:ISDKKitResultListener)

文字识别 OCR 识别结果的回调类，用于接收识别结果以及错误异常。

```java
/**
 * OCR识别结果的回调类
 */
public interface ISDKKitResultListener {

    /**
     * orc识别成功结果
     *
     * @param response 识别结果Json信息
     * @param ocrProcessResult Ocr的识别结果，附带的额外信息
     */
    void onProcessSucceed(String response, OcrProcessResult ocrProcessResult);

    /**
     * orc识别异常
     *
     * @param errorCode 错误码
     * @param message 异常信息
     * @param ocrProcessResult Ocr的识别结果，附带的额外信息
     */
    void onProcessFailed(String errorCode, String message, OcrProcessResult ocrProcessResult);
}
```

[OcrProcessResult](#OcrProcessResult) 是识别结果额外的带的内容。

### [OcrProcessResult](id:OcrProcessResult)

OCR识别完成后，额外携带的数据内容。

| 类型   | 名称           | 含义                                                         | 默认值 |
| ------ | -------------- | ------------------------------------------------------------ | ------ |
| String | requestId      | 本次识别请求对应的requestId（如果没有进行网络请求，就失败了为空） | 空     |
| String | imageBase64Str | 本次识别所使用的图片base64                                   | 空     |



身份证正面请求返回 response 结果示例：

```json
{
    "Name": "李明",
    "Sex": "男",
    "Nation": "汉",
    "Birth": "1987/1/1",
    "Address": "北京市石景山区高新技术园腾讯大楼",
    "IdNum": "440524******010014",
    "Authority": "",
    "ValidDate": "",
    "AdvancedInfo": "{}",
    "RequestId": "ab2c132e-9e1c-43d3-b0ef-9b4d80f00330"
 }
```

身份证反面请求返回 response 结果示例：

```json
{
    "Name": "",
    "Sex": "",
    "Nation": "",
    "Birth": "",
    "Address": "",
    "IdNum": "",
    "Authority": "赵县公安局",
    "ValidDate": "2010.07.21-2020.07.21",
    "AdvancedInfo": "{}",
    "RequestId": "0d394478-6d4d-48fc-8b19-552415bf46de"
 }
```

银行卡请求返回 response 结果示例：

```json
{
    "BankInfo": "招商银行(03080000)",
    "ValidDate": "07/2023",
    "CardType": "贷记卡",
    "CardName": "招商银行信用卡",
    "BorderCutImage": null,
    "CardNoImage": null,
    "WarningCode": [
      -9110
    ],
    "CardNo": "6225768888888888",
    "RequestId": "68f8fcbf-6004-0111a-ac18-6f1a9308fs100mab"
  }
```

名片请求结果返回 response 结果示例：

 ```json
{
    "BusinessCardInfos": [
      {
        "Name": "姓名",
        "Value": "艾米"
      },
      {
        "Name": "职位",
        "Value": "视觉设计师"
      },
      {
        "Name": "部门",
        "Value": "社交平台部"
      },
      {
        "Name": "公司",
        "Value": "Tencent腾讯"
      },
      {
        "Name": "地址",
        "Value": "深圳市南山区高新技术园科技中一路腾讯大厦"
      },
      {
        "Name": "邮箱",
        "Value": "ab***fg@tencent.com"
      },
      {
        "Name": "手机",
        "Value": "+86-133****5678"
      },
      {
        "Name": "QQ",
        "Value": "1234567"
      },
      {
        "Name": "微信",
        "Value": "amy001"
      }
    ],
    "RetImageBase64": "",
    "RequestId": "98f8fcbf-933a-4e95-ac48-6f1a9308fs6h"
 }
 ```

车辆的 VIN 返回 response 结果示例：

```json
{
  "Response": {
    "Vin": "LBV2B25G2E5069977",
    "RequestId": "c59d9002-6c8c-426d-b57f-a8837dee2c7c"
  }
}
```

车辆的车牌返回 response 结果示例：

```json
{
  "Response": {
    "Number": "京N0L9U8",
    "Confidence": 99,
    "Rect": {
      "X": 217,
      "Y": 233,
      "Width": 170,
      "Height": 21
    },
    "RequestId": "210103d3-db06-4691-abe0-c0853aae606b"
  }
}
```

驾驶证识别的response结果示例：

```json
{
    "Name": "李明",
    "Sex": "男",
    "Nationality": "中国",
    "Address": "上海市徐汇区田林路397号腾云大厦6F",
    "DateOfBirth": "1987-01-01",
    "IssuingAuthority": "上海市公安局交通警察总队",
    "DateOfFirstIssue": "2011-10-01",
    "Class": "C1",
    "StartDate": "2011-10-01",
    "EndDate": "2017-10-01",
    "CardCode": "440524198701010014",
    "ArchivesCode": "",
    "Record": "",
    "RecognizeWarnCode": [
      -9106
    ],
    "RecognizeWarnMsg": [
      "WARN_DRIVER_LICENSE_PS_CARD"
    ],
    "RequestId": "4ba2958b-e7cf-41c2-aafe-fdc985307f63"
  }
```

行驶证识别主页识别的response结果示例：

```json
{
    "FrontInfo": {
      "PlateNo": "沪AA1234",
      "VehicleType": "小型轿车",
      "Owner": "李明",
      "Address": "上海市徐汇区田林路397号腾云大厦6F",
      "UseCharacter": "非营运",
      "Model": "别克牌SGM7151LAAA",
      "Vin": "ABCDEFGH123456789",
      "EngineNo": "8B54321",
      "RegisterDate": "2011-10-10",
      "IssueDate": "",
      "Seal": "上海市公安局交通警寨总队"
    },
    "BackInfo": null,
    "RecognizeWarnCode": [
      -9106
    ],
    "RecognizeWarnMsg": [
      "WARN_DRIVER_LICENSE_PS_CARD"
    ],
    "RequestId": "820916b4-b391-40a8-9203-7ae87e3f1954"
  }
```

行驶证识别副页识别的response结果示例：

```json
{
    "FrontInfo": null,
    "BackInfo": {
      "PlateNo": "皖AC4L50",
      "FileNo": "A00-00476807",
      "AllowNum": "5人",
      "TotalMass": "1837kg",
      "CurbWeight": "1431kg",
      "LoadQuality": "--",
      "ExternalSize": "4620×1780×1498mm",
      "TotalQuasiMass": "--",
      "Marks": "",
      "Record": "检验有效期至2015年11月皖A(4S)"
    },
    "RecognizeWarnCode": [
      -9106
    ],
    "RecognizeWarnMsg": [
      "WARN_DRIVER_LICENSE_PS_CARD"
    ],
    "RequestId": "e2ebfaa0-19d3-4d2b-9ed8-7c7c21eb2b74"
  }
```

港澳台居住证识别的response结果示例：

```json
{
  "Response": {
    "Name": "李优优",
    "Sex": "女",
    "Birth": "1997/6/2",
    "Address": "上海市徐汇区古美路1528号A1栋腾讯优图1号",
    "IdCardNo": "830000199706020042",
    "CardType": 0,
    "ValidDate": "",
    "Authority": "",
    "VisaNum": "0",
    "PassNo": "000",
    "RequestId": "f72e7048-f1e0-42f3-b0bf-f8730d48bb5c"
  }
}
```

中国香港身份证识别的response结果示例：

```json
{
  "Response": {
    "CnName": "申能",
    "EnName": "SAN, Nan",
    "TelexCode": "300000000000",
    "Sex": "女F",
    "Birthday": "01-01-2001",
    "Permanent": 1,
    "IdNum": "C000000(E)",
    "Symbol": "***AZ",
    "FirstIssueDate": "(09-99)",
    "CurrentIssueDate": "23-09-10",
    "FakeDetectResult": 1,
    "WarningCode": [
      -9102,
      -9103
    ],
    "HeadImage": "xx",
    "RequestId": "fba1c9ad-aeb3-4418-9ecf-80ab1b5fc875"
  }
}
```

港澳台通行证识别的response结果示例：

```json
{
  "Response": {
    "Name": "李明",
    "EnglishName": "LIMING",
    "Number": "C00000000",
    "Sex": "男",
    "ValidDate": "2018.10.09-2028.10.08",
    "IssueAuthority": "公安部出入境管理局",
    "IssueAddress": "广东",
    "Birthday": "1981.08.03",
    "RequestId": "3090debe-3662-4ef1-8784-6ef2fb59f75e"
  }
}
```

国际护照识别的response结果示例：

```json
{
  "Response": {
    "ID": "E6918C",
    "Name": "LIM HEG CHUN STEE",
    "IssuingCountry": "SGP",
    "Nationality": "SGP",
    "DateOfBirth": "",
    "Sex": "M",
    "DateOfExpiration": "230414",
    "Warn": [],
    "Image": "",
    "AdvancedInfo": "{\"IssuingCountry\":{\"Confidence\":\"0.9500\"},\"Name\":{\"Confidence\":\"0.9500\"},\"ID\":{\"Confidence\":\"0.9500\"},\"Nationality\":{\"Confidence\":\"0.9500\"},\"Sex\":{\"Confidence\":\"0.9500\"},\"DateOfExpiration\":{\"Confidence\":\"0.9500\"}}",
    "CodeSet": "P<CANBROWN<<BENJAMIN<<<<<<<<<<<<<<<<<<<<<<<<",
    "CodeCrc": "JK123488<3CAN8510168M2603298<<<<<<<<<<<<<<04",
    "RequestId": "0ee989d3-d064-45ec-bccb-63f5064247b4"
  }
}
```



对于返回的错误码以及错误信息，可以参考 [错误码](https://cloud.tencent.com/document/product/866/33528) 。

<span id="ISdkOcrEntityResultListener"></span>

### ISdkOcrEntityResultListener

文字识别 OCR 识别结果的回调类，用于接收识别结果的实体类以及错误异常。

```java
public interface ISdkOcrEntityResultListener<T> {

    /**
     * orc识别成功结果
     *
     * @param t 返回实体信息
     * @param ocrProcessResult Ocr的识别结果，附带的额外信息
     */
    void onProcessSucceed(T t, OcrProcessResult ocrProcessResult);

    /**
     * orc识别异常
     *
     * @param errorCode 错误码
     * @param message 异常信息
     * @param ocrProcessResult Ocr的识别结果，附带的额外信息
     */
    void onProcessFailed(String errorCode, String message, OcrProcessResult ocrProcessResult);
}
```

[OcrProcessResult](#OcrProcessResult) 是识别结果额外的带的内容。



### 错误码

#### 公共错误码

| 错误码                            | 说明                                                         |
| :-------------------------------- | :----------------------------------------------------------- |
| UnsupportedOperation              | 操作不支持。                                                 |
| ResourceInUse                     | 资源被占用。                                                 |
| InternalError                     | 内部错误。                                                   |
| RequestLimitExceeded              | 请求的次数超过了频率限制。                                   |
| AuthFailure.SecretIdNotFound      | 密钥不存在。 请在控制台检查密钥是否已被删除或者禁用，如状态正常，请检查密钥是否填写正确，注意前后不得有空格。 |
| LimitExceeded                     | 超过配额限制。                                               |
| NoSuchVersion                     | 接口版本不存在。                                             |
| ResourceNotFound                  | 资源不存在。                                                 |
| AuthFailure.SignatureFailure      | 签名错误。 签名计算错误，请对照调用方式中的签名方法文档检查签名计算过程。 |
| AuthFailure.SignatureExpire       | 签名过期。Timestamp 和服务器时间相差不得超过五分钟，请检查本地时间是否和标准时间同步。 |
| UnsupportedRegion                 | 接口不支持所传地域。                                         |
| UnauthorizedOperation             | 未授权操作。                                                 |
| InvalidParameter                  | 参数错误。                                                   |
| ResourceUnavailable               | 资源不可用。                                                 |
| AuthFailure.MFAFailure            | MFA 错误。                                                   |
| AuthFailure.UnauthorizedOperation | 请求未授权。请参考 [CAM](https://cloud.tencent.com/document/product/598) 文档对鉴权的说明。 |
| AuthFailure.InvalidSecretId       | 密钥非法（不是云 API 密钥类型）。                            |
| AuthFailure.TokenFailure          | token 错误。                                                 |
| DryRunOperation                   | DryRun 操作，代表请求将会是成功的，只是多传了 DryRun 参数。  |
| FailedOperation                   | 操作失败。                                                   |
| UnknownParameter                  | 未知参数错误。                                               |
| UnsupportedProtocol               | HTTP(S)请求协议错误，只支持 GET 和 POST 请求。               |
| InvalidParameterValue             | 参数取值错误。                                               |
| InvalidAction                     | 接口不存在。                                                 |
| MissingParameter                  | 缺少参数错误。                                               |
| ResourceInsufficient              | 资源不足。                                                   |

#### 业务错误码

| 错误码                                           | 说明                                                   |
| :----------------------------------------------- | :----------------------------------------------------- |
| FailedOperation.ArrearsError                     | 账号已欠费。                                           |
| FailedOperation.CountLimitError                  | 今日次数达到限制。                                     |
| FailedOperation.DetectFailed                     | 检测失败。                                             |
| FailedOperation.DownLoadError                    | 文件下载失败。                                         |
| FailedOperation.EmptyImageError                  | 图片内容为空。                                         |
| FailedOperation.EngineRecognizeTimeout           | 引擎识别超时。                                         |
| FailedOperation.IdCardInfoIllegal                | 身份证信息不合法（身份证号、姓名字段校验非法等）。     |
| FailedOperation.ImageBlur                        | 图片模糊。                                             |
| FailedOperation.ImageDecodeFailed                | 图片解码失败。                                         |
| FailedOperation.ImageNoBusinessCard              | 照片未检测到名片。                                     |
| FailedOperation.ImageNoIdCard                    | 图片中未检测到身份证。                                 |
| FailedOperation.ImageNoText                      | 图片中未检测到文本。                                   |
| FailedOperation.ImageSizeTooLarge                | 图片尺寸过大，请参考输出参数中关于图片大小限制的说明。 |
| FailedOperation.InvoiceMismatch                  | 发票数据不一致。                                       |
| FailedOperation.LanguageNotSupport               | 输入的 Language 不支持。                                 |
| FailedOperation.MultiCardError                   | 照片中存在多张卡。                                     |
| FailedOperation.OcrFailed                        | OCR 识别失败。                                          |
| FailedOperation.UnKnowError                      | 未知错误。                                             |
| FailedOperation.UnOpenError                      | 服务未开通。                                           |
| InvalidParameter.ConfigFormatError               | Config 不是有效的 JSON 格式。                             |
| InvalidParameter.EngineImageDecodeFailed         | 图片解码失败。                                         |
| InvalidParameter.InvalidGTINError                | 无效的 GTIN。                                           |
| InvalidParameterValue.InvalidParameterValueLimit | 参数值错误。                                           |
| LimitExceeded.TooLargeFileError                  | 文件内容太大。                                         |
| ResourceNotFound.NoInvoice                       | 发票不存在。                                           |
| ResourcesSoldOut.ChargeStatusException           | 计费状态异常。                                         |

#### SDK 本地错误码

<table>
<thead>
<tr>
<th>错误码</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>OcrSdk.UserCancelOcr</td>
<td>用户主动停止文字识别</td>
</tr>
<tr>
<td>OcrSdk.InnerOcrError</td>
<td>文字识别内部错误，请重试</td>
</tr>
<tr>
<td>OcrSdk.CallInitFirst</td>
<td>SDK需要先调用init</td>
</tr>
<tr>
<td>FailedOperation.OcrFailed</td>
<td>服务识别OCR结果异常</td>
</tr>
<tr>
<td>OcrSdk.InnerOcrErrorClipError</td>
<td>SDK内部选图裁剪逻辑失败</td>
</tr>
<tr>
<td>OcrSdk.PermissionError</td>
<td>用户拒绝权限的回调</td>
</tr>
<tr>
<td>OcrSdk.PermissionError_GoSetting</td>
<td>用户拒绝权限的回调并且主动前往Setting界面</td>
</tr>
</tbody></table>
