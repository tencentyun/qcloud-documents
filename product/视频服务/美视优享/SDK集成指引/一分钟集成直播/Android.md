## 集成准备[](id:ready)
1. 解压 [Demo 包](待定)。将 Demo ⼯程中的 X - magic 模块引⼊到实际项⽬⼯程中。
2. 授权：
<dx-tabs>
::: 方法一
1. 将测试授权的 lic ⽂件添加到 `xmagic/src/main/assets/` ⽬录下。
2. 打开 `xmagic/src/main/java/com.tencent.xmagic/XMagicImpl.java`  在 initAuth 方法中，将授权⽂件的 lic 添加到接⼝ `Auth.auth` 中。
:::
::: 方法二
1. 在 MLVBApplication 中获取正确的的 Key 和 URL， 然后在 onCreate 方法中设置  `XMagicLicenseInit.setLicense(context,url,key)` 方法。
2. 打开 `xmagic/src/main/java/com.tencent.xmagic/XMagicImpl.java` 在 initAuth 方法中获取 licenseInfo 然后把 licenseInfo 添加到 `Auth.authByBase6`4 中。
:::
</dx-tabs>
3. 打开 app 模块的 build.gradle。
将 applicationId 修改成与申请的测试授权⼀致的包名，添加 gson 依赖设置。
```
configurations{
	all*.exclude group：'com.google.code.gson'
}
```

## SDK 接口集成[](id:step)

可参考 Demo ⼯程的 ThirdBeautyActivity 类。

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
4. 预览界面开启第三方推流设置。
```
mLivePusher.enableCustomVideoProcess(true,
V2TXLiveDef.V2TXLivePixelFormat.V2TXLivePixelFormatTexture2D, V2TXLiveDef.
V2TXLiveBufferType.V2TXLiveBufferTypeTexture);
```
5. 将 textureId 传入到 SDK 内做渲染处理。
```
v2TXLiveVideoFrame1.texture.textureId  = 
mXMagic.process(v2TXLiveVideoFrame.texture.textureId,
v2TXLiveVideoFrame.width,v2TXLiveVideoFrame.height);
```
6. 暂停/关闭 SDK。
```
mXMagic.pauseAudio();
mXMagic.onPause();
```
7. 布局中添加 SDK 美颜面板。
```	
<include
	layout="@layout/xmagic_panel"
	android:id="@+id/livepusher_bp_beauty_pannel"
	android:layout_width="match_parent"
	android:layout_height="wrap_content"
	android:layout_alignParentBottom="true"
	android:visibility="gone"  />
```
8. 初始化面板与美颜设置回调接口，请参见 [Demo⼯程]() 的 `ThirdBeautyActivity.initXMagic();` ⽅法。





