TUIKit 从 5.7.1435 版本开始支持模块化集成，您可以根据自己的需求集成所需模块。
TUIKit 从 6.9.3557 版本开始新增了全新的简约版 UI，之前的 UI 依旧保留，我们称之为经典版 UI，您可以根据需求自由选择经典版或简约版 UI。

如果您还不了解各个界面库的功能，可以查阅文档 [TUIKit 界面库介绍](https://cloud.tencent.com/document/product/269/37190)。

下文将介绍如何集成 TUIKit 组件。 

## 开发环境要求
- Android Studio-Chipmunk 
- Gradle-6.7.1
- Android Gradle Plugin Version-4.2.0
- kotlin-gradle-plugin-1.5.31
  
## module 源码集成
1. 从 [GitHub 下载](https://github.com/tencentyun/TIMSDK/tree/master/Android) TUIKit 源码。使 TUIKit 文件夹跟自己的工程文件夹同级，例如：
<img src="https://qcloudimg.tencent-cloud.cn/raw/00bc0470857b850436663d9bf2ef9164.png" width="500"/> 
1. 根据实际业务需求在 settings.gradle 中添加对应的 TUI 组件。TUI 组件之间相互独立，添加或删除均不影响工程编译。
```groovy
// 引入上层应用模块
include ':app'

// 引入内部组件通信模块 (必要模块)
include ':tuicore'
project(':tuicore').projectDir = new File(settingsDir, '../TUIKit/TUICore/tuicore')

// 引入聊天功能模块 (基础功能模块)
include ':tuichat'
project(':tuichat').projectDir = new File(settingsDir, '../TUIKit/TUIChat/tuichat')

// 引入关系链功能模块 (基础功能模块)
include ':tuicontact'
project(':tuicontact').projectDir = new File(settingsDir, '../TUIKit/TUIContact/tuicontact')

// 引入会话功能模块 (基础功能模块)
include ':tuiconversation'
project(':tuiconversation').projectDir = new File(settingsDir, '../TUIKit/TUIConversation/tuiconversation')

// 引入搜索功能模块（需要购买旗舰版套餐）
include ':tuisearch'
project(':tuisearch').projectDir = new File(settingsDir, '../TUIKit/TUISearch/tuisearch')

// 引入群组功能模块
include ':tuigroup'
project(':tuigroup').projectDir = new File(settingsDir, '../TUIKit/TUIGroup/tuigroup')

// 引入离线推送功能模块
include ':tuiofflinepush'
project(':tuiofflinepush').projectDir = new File(settingsDir, '../TUIKit/TUIOfflinePush/tuiofflinepush')

// 引入社群话题功能模块（需要购买旗舰版套餐）
include ':tuicommunity'
project(':tuicommunity').projectDir = new File(settingsDir, '../TUIKit/TUICommunity/tuicommunity')

// 引入音视频通话功能模块
include ':tuicallkit'
project(':tuicallkit').projectDir = new File(settingsDir, '../TUIKit/TUICallKit/tuicallkit')
```
3. 在 APP 的 build.gradle 中添加：
```groovy
dependencies {
    api project(':tuiconversation')
    api project(':tuicontact')
    api project(':tuichat')
    api project(':tuisearch')
    api project(':tuigroup')
    api project(':tuiofflinepush')
    api project(':tuicommunity')
    api project(':tuicallkit')  
}
```
4. 在 gradle.properties 文件中加入下行，表示自动转换三方库以兼容 AndroidX：
```properties
android.enableJetifier=true
```
[](id:buildStep5)
5. 添加 maven 仓库 和 Kotlin 支持，在 root 工程的 build.gradle 文件（与 settings.gradle 同级）中添加：
```groovy
buildscript {
    ext.kotlin_version = '1.5.31'
    repositories {
        mavenCentral()
        maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:4.2.0'
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}
```
6. 同步工程，编译运行。工程结构预期效果如图所示：<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/454abb6051a7a94a08559d8404e5aec7.png" width="400"/> 
7. 裁剪不需要的 UI 文件（可选）
`经典版`和`简约版` UI 互不影响，可独立运行。`经典版`和`简约版`的 UI 文件都在各 TUI 组件中，放在不同的文件夹里，以 `TUIChat` 组件为例：
<img src="https://qcloudimg.tencent-cloud.cn/raw/179a15bb72b24a09cf7440c50e5c3442.png" width="400"/> 
classicui 文件夹中存放的是`经典版` UI 文件，minimalistui 文件夹中存放的是`简约版` UI 文件, 如果您要集成简约版 UI，可直接删除 classicui 文件夹，同时删除 AndroidManifest.xml 文件中经典版 UI 对应的 Activity 和 Service 。
> ?  经典版和简约版 UI 不能混用，集成多个组件时，您必须同时选择经典版 UI 或者 简约版 UI。

## 快速搭建
常用的聊天软件都是由会话列表、聊天窗口、好友列表、音视频通话等几个基本的界面组成，参考下面步骤，您仅需几行代码即可在项目中快速搭建这些 UI 界面。

### 步骤1：组件登录

```java
// 在用户 UI 点击登录的时候调用
TUILogin.login(context, sdkAppID, userID, userSig, new TUICallback() {
    @Override
    public void onError(final int code, final String desc) {
    }

    @Override
    public void onSuccess() {
    }
});
```
>! context 必须传 Application 对象，否则部分图片无法加载。

### 步骤2：创建 viewPager
1. 在 activity_main.xml 中添加界面布局：
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">
    
    <androidx.viewpager2.widget.ViewPager2
    android:id="@+id/view_pager"
    android:layout_width="match_parent"
    android:layout_height="0dp"
    android:layout_weight = "1"/>
</LinearLayout>
```
2. 创建 FragmentAdapter.java 用来配合 ViewPager2 展示会话和联系人界面。
```java
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentActivity;
import androidx.fragment.app.FragmentManager;
import androidx.lifecycle.Lifecycle;
import androidx.viewpager2.adapter.FragmentStateAdapter;


import java.util.List;

public class FragmentAdapter extends FragmentStateAdapter {
    private static final String TAG = FragmentAdapter.class.getSimpleName();

    private List<Fragment> fragmentList;

    public FragmentAdapter(@NonNull FragmentActivity fragmentActivity) {
        super(fragmentActivity);
    }

    public FragmentAdapter(@NonNull Fragment fragment) {
        super(fragment);
    }

    public FragmentAdapter(@NonNull FragmentManager fragmentManager, @NonNull Lifecycle lifecycle) {
        super(fragmentManager, lifecycle);
    }

    public void setFragmentList(List<Fragment> fragmentList) {
        this.fragmentList = fragmentList;
    }

    @NonNull
    @Override
    public Fragment createFragment(int position) {
        if (fragmentList == null || fragmentList.size() <= position) {
            return new Fragment();
        }
        return fragmentList.get(position);
    }

    @Override
    public int getItemCount() {
        return fragmentList == null ? 0 : fragmentList.size();
    }
}
```

### 步骤3：构建核心 Fragment

会话列表 `TUIConversationFragment` 以及联系人列表 `TUIContactFragment` 界面数据的获取、同步、展示以及交互均已在组件内部封装，UI 的使用与 Android 的普通 Fragment 一样方便。

在 MainActivity.java 的 onCreate 方法中添加以下代码：

<dx-tabs>
::: 经典版
```java
List<Fragment> fragments = new ArrayList<>();
// 添加 tuiconversation 组件提供的经典版会话界面
fragments.add(new TUIConversationFragment());

// 添加 tuicontact 组件提供的经典版联系人界面
fragments.add(new TUIContactFragment());

ViewPager2 mainViewPager = findViewById(R.id.view_pager);
FragmentAdapter fragmentAdapter = new FragmentAdapter(this);
fragmentAdapter.setFragmentList(fragments);
mainViewPager.setOffscreenPageLimit(2);
mainViewPager.setAdapter(fragmentAdapter);
mainViewPager.setCurrentItem(0, false);

```
:::

::: 简约版
```java
List<Fragment> fragments = new ArrayList<>();
// 添加 tuiconversation 组件提供的简约版会话界面
fragments.add(new TUIConversationMinimalistFragment());

// 添加 tuicontact 组件提供的简约版联系人界面
fragments.add(new TUIContactMinimalistFragment());

ViewPager2 mainViewPager = findViewById(R.id.view_pager);
FragmentAdapter fragmentAdapter = new FragmentAdapter(this);
fragmentAdapter.setFragmentList(fragments);
mainViewPager.setOffscreenPageLimit(2);
mainViewPager.setAdapter(fragmentAdapter);
mainViewPager.setCurrentItem(0, false);

```
:::

</dx-tabs>



### 步骤4：构建音视频通话功能
TUI 组件支持在聊天界面对用户发起音视频通话，仅需要简单几步就可以快速集成：

<table style="text-align:center;vertical-align:middle;width: 800px">
  <tr>
    <th style="text-align:center;" ><b>视频通话<br></b></th>
    <th style="text-align:center;"><b>语音通话</b><br></th>
  </tr>
  <tr>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/b9f362503d25179db6f75fc91cfd000a.jpg"/></td>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/2f037d7de8270c0edef68c0b829465ec.png"/></td>
	 </tr>
</table>

1. **开通音视频服务**
	1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片，进入应用的基础配置页面。
	2. 在开通腾讯实时音视频服务功能区，单击**免费体验**即可开通 TUICallKit 的 7 天免费试用服务。
	3. 在弹出的开通实时音视频 TRTC 服务对话框中，单击确认，系统将为您在 [实时音视频控制台](https://console.cloud.tencent.com/trtc) 创建一个与当前 IM 应用相同 SDKAppID 的实时音视频应用，二者帐号与鉴权可复用。
2. **集成 TUICallKit 组件**
在 APP 的 build.gradle 文件中添加对 `TUICallKit` 的依赖：
```groovy
api project(':tuicallkit')
```
3. **发起和接收视频或语音通话**
<table style="text-align:center;vertical-align:middle;width: 800px">
  <tr>
    <th style="text-align:center;" ><b>消息页发起通话<br></b></th>
    <th style="text-align:center;" ><b>联系人页发起通话<br></b></th>
  </tr>
  <tr>
        <td><img style="width:400px" src="https://qcloudimg.tencent-cloud.cn/raw/b7b6aca5e1f3f3e5d775cfa3316e30f4.png"  />    </td>
    <td><img style="width:400px" src="https://qcloudimg.tencent-cloud.cn/raw/31fd1d8fb263e953825cf5531a24ffca.png"  />    </td>
     </tr>
</table>
<ul>
<li>集成 TUICallKit 组件后，聊天界面和联系人资料界面默认会显示 “视频通话” 和 “语音通话” 两个按钮，当用户点击按钮时，TUIKit 会自动展示通话邀请 UI，并给对方发起通话邀请请求。</li>
<li>当用户<strong>在线并且应用在前台时</strong>收到通话邀请时，TUIKit 会自动展示通话接收 UI，用户可以选择同意或则拒绝通话。</li>
<li>当用户<strong>离线</strong>收到通话邀请时，如需唤起 App 通话，需要使用离线推送能力。离线推送的实现请参考下一步。</li>
</ul>
4. **添加离线推送：**[](id:Step5)
实现音视频通话的离线推送，请参考以下几个步骤：
	1. 配置 App 的 [离线推送](https://cloud.tencent.com/document/product/269/44516)。
	2. 集成 TUICallKit 组件。
	3. 通过 TUICallKit 发起通话邀请的时候，默认会生成一条离线推送消息。

5. **附加增值能力**
集成 TUIChat 和 TUICallkit 的组件后，在聊天界面发送语音消息时，即可**录制带 AI 降噪和自动增益的语音消息**。该功能需要购买 [音视频通话能力](https://cloud.tencent.com/document/product/1640/79968) 进阶版及以上套餐，仅 IMSDK 7.0 及以上版本支持。当套餐过期后，录制语音消息会切换到系统 API 进行录音。
下面是使用两台华为 P10 同时录制的语音消息对比：
<table style="text-align:center;vertical-align:middle;width: 800px">
  <tr>
    <th style="text-align:center;" ><b>系统录制的语音消息<br></b></th>
    <th style="text-align:center;" ><b>TUICallkit 录制的带 AI 降噪和自动增益的语音消息<br></b></th>
  </tr>
  <tr>
    <td>
      <audio id="audio" controls="" preload="none" >
	<source id="m4a" src="https://im.sdk.cloudcachetci.com/tools/resource/rain_system_record.m4a">
      </audio>
    </td>
		
    <td>
      <audio id="audio" controls="" preload="none">
	<source id="m4a" src="https://im.sdk.cloudcachetci.com/tools/resource/rain_tuicallkit_record_with_agc_aidenoise.m4a">
      </audio>
    </td>
  </tr>
</table>
	

>? 更多实操教学视频请参见：[极速集成 TUIKit（Android）](https://cloud.tencent.com/edu/learning/course-3130-56399)。

## 常见问题
#### 提示 "Manifest merger failed : Attribute application@allowBackup value=(true) from AndroidManifest.xml" 如何处理？
IM SDK 中默认 `allowBackup` 的值为 `false` ，表示关闭应用的备份和恢复功能。
您可以在您的 `AndroidManifest.xml` 文件中删除 `allowBackup` 属性，表示关闭备份和恢复功能；也可以在 `AndroidManifest.xml` 文件的 application 节点中添加 `tools:replace="android:allowBackup"` 表示覆盖 IM SDK 的设置，使用您自己的设置。 

例如：
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="com.tencent.qcloud.tuikit.myapplication">

    <application
        android:allowBackup="true"
        android:name=".MApplication"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.MyApplication"
        tools:replace="android:allowBackup">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

#### 提示 "NDK at /Users/***/Library/Android/sdk/ndk-bundle did not have a source.properties file" 如何处理？
只需要在 local.properties 文件中加入您的 NDK 路径，例如：
`ndk.dir=/Users/***/Library/Android/sdk/ndk/16.1.4479499`

#### 提示 "Cannot fit requested classes in a single dex file" 如何处理？
出现此问题可能是您的 API 级别设置比较低，需要在 App 的 build.gradle 文件中开启 `MultiDex` 支持, 添加 `multiDexEnabled true` 和对应依赖：
```groovy
android {
    defaultConfig {
        ...
        minSdkVersion 19
        targetSdkVersion 30
        multiDexEnabled true
    }
    ...
}
dependencies {
    implementation "androidx.multidex:multidex:2.0.1"
}
```
同时，在您的 Application 文件中添加以下代码：
```java
public class MyApplication extends SomeOtherApplication {
    @Override
    protected void attachBaseContext(Context base) {
        super.attachBaseContext(base);
        MultiDex.install(this);
    }
}
```

#### 提示 "Plugin with id 'kotlin-android' not found." 如何处理？
因为 `TUIChat` 组件使用了 Kotlin 代码，所以需要添加 Kotlin 构建插件。请参考 [module 源码集成第 5 步](#buildStep5)。

## 交流与反馈
欢迎加入 QQ 群进行技术交流和反馈问题。
<img src="https://im.sdk.qcloud.com/tools/resource/officialwebsite/pictures/doc_tuikit_qq_group.jpg" style="zoom:50%;"/> 
