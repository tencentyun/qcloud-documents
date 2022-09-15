UGCKit 是封装好的一整套 UI 交互界面，默认为小视频主题风格。如果您想简单定制自己的主题风格，只需要简单修改主题样式即可实现换图标、换文字、换颜色。

## 定制录制主题
录制界面包括右侧的图标工具栏、底部的工具栏、音乐面板、美颜面板、音效面板等。

![图片描述](https://main.qcloudimg.com/raw/7aadc42dc6bb53a4113afdf2dc5bc135.png)

1.  在 `app/res/values/style.xml` 中声明一个 `<style>`，父主题指定为 `RecordStyle`，重写您需要替换的样式，这些可替换的样式在 `app/ugckit/res/values.theme_style.xml` 中可找到。
如下所示，替换录制界面的音乐图标和美颜图标：
```java
<style name="RecordActivityTheme" parent="RecordStyle">
	<item name="recordMusicIcon">@drawable/ic_music</item>
	<item name="recordBeautyIcon">@drawable/ic_beauty</item>
</style>
```
2.  在 `AndroidManifest.xml` 中声明您定制的主题：
```java
<activity
    android:name="com.tencent.qcloud.xiaoshipin.videorecord.TCVideoRecordActivity"
    android:launchMode="singleTop"
    android:screenOrientation="portrait"
    android:theme="@style/RecordActivityTheme"
    android:windowSoftInputMode="adjustNothing" />
```

## 定制编辑主题
编辑界面包括编辑裁剪界面、动态滤镜特效面板、速度面板、滤镜面板、贴纸面板、气泡字幕面板。

![图片描述](https://main.qcloudimg.com/raw/4f2b40482068a2d749ac0bc15922606a.png)
1. 在 `app/res/values/style.xml` 中声明一个 `<style>`，父主题指定为 `EditerStyle`，重写您需要替换的样式，这些可替换的样式在 `app/ugckit/res/values.theme_style.xml` 中可找到。
如下所示，替换编辑界面的播放图标和暂停图标：
```java
<style name="EditerActivityTheme" parent="EditerStyle">
	<item name="editorPlayIcon">@drawable/ic_play</item>
	<item name="editorPauseIcon">@drawable/ic_pause</item>
</style>
```
2. 在 `AndroidManifest.xml` 中声明您定制的主题：
```java
<activity
    android:name=".videoeditor.TCVideoEffectActivity"
    android:screenOrientation="portrait"
    android:theme="@style/EditerActivityTheme" />
```
