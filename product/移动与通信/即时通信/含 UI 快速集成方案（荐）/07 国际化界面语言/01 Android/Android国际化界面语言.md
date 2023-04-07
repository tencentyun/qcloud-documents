## 功能描述

Android 端 `TUIKit` 默认自带 **简体中文** 和 **英语** 语言包，作为界面展示语言。

根据此文档指引，您可以使用默认语言包，也可自定义语言翻译表述和增加其他语言包。

<table style="text-align:center;vertical-align:middle;width:600px">
  <tr>
    <th style="text-align:center;" width="300px">简体中文<br></th>
    <th style="text-align:center;" width="300px">英文<br></th>
  </tr>
  <tr>
    <td style="text-align:center;"><img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/d4ff4c9f9d245f9c015b5e59e7d88f6b.jpeg"  />    </td>
    <td style="text-align:center;"><img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/1bca636bdfe402d4054485b285d20fd0.jpeg" />     </td>
	 </tr>
</table>


## 使用自带语言

如果您的 App 需要的语言仅包括 **简体中文** 和 **英语**，请参考本部分。

### 跟随系统语言

直接使用 `TUIKit` 即可，无需额外步骤。组件内部语言会跟随系统语言。

### 指定显示的语言

如果您需要指定 TUIKit 界面的语言，需要在 Appliction 初始化时调用以下代码进行设置，例如设置为英文：

```java
public class MyApplication extends Application {
    @Override
    protected void onCreate() {
        super.onCreate();
        TUIThemeManager.getInstance().changeLanguage(this, TUIThemeManager.LANGUAGE_EN);
    }

    /**
    * 语言可选枚举为：
    * TUIThemeManager.LANGUAGE_EN        ---- 英文
    * TUIThemeManager.LANGUAGE_ZH_CN     ---- 简体中文
    */
}
```

>!调用 `changeLanguage` 方法并不会自动刷新 UI，需要获取字符串之后重新设置到控件上才能生效。


### 实时动态修改

您可以参考 `TUIKitDemo` 的 [LanguageSelectActivity.java](https://github.com/TencentCloud/TIMSDK/blob/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/login/LanguageSelectActivity.java) 文件中的代码。也可以使用如下方法切换语言，例如切换为英文：

```java
TUIThemeManager.getInstance().changeLanguage(context, TUIThemeManager.LANGUAGE_EN);
System.exit(0);
Intent intent = context.getPackageManager().getLaunchIntentForPackage(context.getPackageName());
context.startActivity(intent);
```


### 使用 WebView 之后发现语言切换失败处理方法

使用 WebView 之后导致语言切换失败是 Android 7 及以后版本的 bug，原因是 WebView 初始化时会修改 App 的语言为手机系统语言。需要在 [TUIThemeManager.java](Android/TUIKit/TUICore/tuicore/src/main/java/com/tencent/qcloud/tuicore/TUIThemeManager.java) 的 `setThemeInternal` 方法中调用以下代码解决此问题：

```java
setWebViewLanguage(appContext);
```

添加之后：

```java
private void setThemeInternal(Context context) {
    if (context == null) {
        return;
    }

    Context appContext = context.getApplicationContext();
    if (!isInit) {
        isInit = true;
        if (appContext instanceof Application) {
            ((Application) appContext).registerActivityLifecycleCallbacks(new ThemeAndLanguageCallback());
        }

        /**
        * 在此处添加代码  begin
        */
        setWebViewLanguage(appContext);
        /**
        * 在此处添加代码  end
        */
        Locale defaultLocale = getLocale(appContext);
        SPUtils spUtils = SPUtils.getInstance(SP_THEME_AND_LANGUAGE_NAME);
        currentLanguage = spUtils.getString(SP_KEY_LANGUAGE, defaultLocale.getLanguage());
        currentThemeID = spUtils.getInt(SP_KEY_THEME, THEME_LIGHT);

        // The language only needs to be initialized once
        applyLanguage(appContext);
    }
    // The theme needs to be updated multiple times
    applyTheme(appContext);
}
```

## 使用更多语言/自定义翻译表述

如果您的 App 需要支持更多语言，或更改部分词条的翻译，请参考本部分。

>? 本方案仅适用于新增语言的阅读方向为从左至右（LTR）的情况。对于阅读方向从右至左（RTL）的语言，如阿拉伯语，请自行在 [GitHub](https://github.com/TencentCloud/TIMSDK) 下载源码，完成 RTL 适配。

本章节以 `TUIGroup` 组件添加韩语语言包为例，讲解新增语言包和自定义翻译的流程。

### 新增语言资源文件

在 Android Studio 中的 `TUIGroup` 组件目录下，右键菜单中新增 Android Resource File：

 <img style="width:600px" src="https://qcloudimg.tencent-cloud.cn/raw/93e2873ce99085e642932443aad91d51.png" />

输入文件名 `strings`，由 `Locale` 维度创建资源目录：

 <img style="width:600px" src="https://qcloudimg.tencent-cloud.cn/raw/acfe4f635154a527eeb7946358fe8d20.png" />

语言选择为韩语（"ko: Korean"），地区选为"KR: South Korea" ，点击确定，这样就创建好了韩语资源文件 `values-ko-rKR/strings.xml`。

 <img style="width:600px" src="https://qcloudimg.tencent-cloud.cn/raw/8d08a6ba7738bdadc21e9e5278a217fe.png" />


### 个性化自定义翻译

上一步已经创建好了韩语资源文件 `values-ko-rKR/strings.xml`，现在把 `values/strings.xml` 文件中的内容复制到 `values-ko-rKR/strings.xml`，用韩语替换对应的英文，如图所示：

 <img style="width:600px" src="https://qcloudimg.tencent-cloud.cn/raw/19b4f0ca2023c05e33c176446dc4cb78.png" />

不同语言资源文件中语言的 `name` 是相同的，具体内容可以自定义翻译。

### 跟随系统语言

直接使用 `TUIKit` 即可，将手机默认语言设置为韩语后启动 App ，App 语言可以自动显示为韩语。

### 指定显示的语言

如果您需要指定 `TUIKit` 界面的语言为韩语，应该先在 `Appliction` 初始化时向语言管理器中添加韩语，然后再设置 `TUIKit` 界面的语言为韩语：

```java
public class MyApplication extends Application {
    @Override
    protected void onCreate() {
        super.onCreate();
        // 添加韩语
        TUIThemeManager.addLanguage("ko-rKR", Locale.KOREA);
        // 应用语言改为韩语
        TUIThemeManager.getInstance().changeLanguage(this, "ko-rKR");
    }
}
```

效果如图所示：
<img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/0969ee07a0e552c3566b9b7be75f7674.png" />


## 交流与反馈
欢迎加入 QQ 群进行技术交流和反馈问题。
<img src="https://im.sdk.qcloud.com/tools/resource/officialwebsite/pictures/doc_tuikit_qq_group.jpg" style="zoom:50%;"/> 
