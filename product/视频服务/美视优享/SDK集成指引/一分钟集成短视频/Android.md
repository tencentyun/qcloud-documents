## 集成准备[](id:ready)
1. 解压 Demo 包。将 Demo ⼯程中的 xmagic 模块引⼊到实际项⽬⼯程中。
2. 授权：
<dx-tabs>
::: 方法一
1.  将测试授权的 lic ⽂件添加到 `xmagic/src/main/assets/` ⽬录下。
2.  打开 `xmagic/src/main/java/com.tencent.xmagic/XMagicImpl.java` 的 initAuth 方法，将授权⽂件的 lic 添加到接⼝ `Auth.auth` 中。
:::
::: 方法二
1.  在 TCApplication 中设置正确的 Key 和 URL，然后在 onCreate 方法中设置 `XMagicLicenseInit.setLicense(context,url,key)` 方法。
2.  打开 `xmagic/src/main/java/com.tencent.xmagic/XMagicImpl.java` 在 initAuth 方法中获取 licenseInfo 然后把 licenseInfo 添加到 `Auth.authByBase64` 中。
:::
</dx-tabs>
3. 打开 app 模块的 `build.gradle`。
将 applicationId 修改成与申请的测试授权⼀致的包名，添加 gson 依赖设置。
```
configurations{
	all*.exclude group:'com.google.code.gson'
}
```

## SDK 接口集成[](id:step)
可参考 [Demo]() ⼯程的 TCVideoRecoredActivity 类。

1. 初始化授权。
```
XMagicImpl.getInstance().initAuth(getApplicationContext());
```
2. 设置 SDK 素材资源路径。
```
XMagicImpl.getInstance().setResPath(getApplicationContext(),"xmagic");
```
3. 初始化素材。
>! 耗时操作需要在⼦线程完成。
>
```
XMagicImpl.getInstance().copyRes(getApplicationContext());
```
4. 将 textureId 传入到 SDK 内做渲染处理。
```
TXUGCRecord.VideoCustomProcessListener监听中 Int mXmagicId=mXMagic.process(textureId, width, height);return mXmagicId;
```
5. 暂停/关闭 SDK。
```
mXMagic.pauseAudio();
mXMagic.onPause();
```
6. 布局中添加 SDK 美颜面板。
```
<include
	layout="@layout/xmagic_panel"
	android:id="@+id/livepusher_bp_beauty_pannel"
	android:layout_width="match_parent"
	android:layout_height="wrap_content"
	android:layout_alignParentBottom="true"
	android:visibility="gone"  />
```
7. 初始化面板与美颜设置回调接口，具体实现方法请参见 [Demo ⼯程](待定) 中的 `TCVideoRecoredActivity.initXMagic();` ⽅法。

