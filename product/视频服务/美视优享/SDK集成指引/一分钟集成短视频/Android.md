[](id:step1)
## 步骤一：解压 Demo 工程
1. 下载集成了腾讯特效 TE 的 [UGSV Demo](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/2.4.1.115.vcube/UGSV_Demo.zip) 工程。本Demo基于腾讯特效SDK S1-04套餐构建。
2. 替换资源。由于本Demo工程使用的SDK套餐未必与你实际的套餐一致，因此要将本Demo中的相关SDK文件替换为你实际使用的套餐的SDK文件。具体操作如下：
   - 删除xmagic模块中libs目录下的 `.aar`文件，将SDK中libs目录下的 `.aar` 文件拷贝进xmagic模块中libs目录下。
   - 删除xmagic模块中assets目录下的所有文件，将 SDK 中的 assets/ 目录下的全部资源拷贝到 xmagic模块`../src/main/assets` 目录下，如果SDK包中的MotionRes文件夹内有资源，将此文件夹也拷贝到`../src/main/assets`目录下 。
   - 删除xmagic模块中jniLibs目录下的所有.so文件，在 SDK 包内的 jniLibs 中找到对应的.so文件（由于SDK中jinLibs文件夹下的arm64-v8a和armeabi-v7a的.so文件在压缩包中，所以需要先解压），拷贝到 xmagic模块中的 `../src/main/jniLibs` 目录下。
3. 将 Demo ⼯程中的 xmagic 模块引⼊到实际项⽬⼯程中。

[](id:step2)

## 步骤二：打开 app 模块的 build.gradle
1. 将 applicationId 修改成与申请的测试授权⼀致的包名。
2. 添加 gson 依赖设置。
```groovy
configurations{
    all*.exclude group:'com.google.code.gson'
}
```

[](id:step3)
## 步骤三：SDK 接口集成
可参考 Demo ⼯程的 TCVideoRecoredActivity 类。
1. **授权：**
```java
 //鉴权注意事项及错误码详情，请参考 https://cloud.tencent.com/document/product/616/65891#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E9.89.B4.E6.9D.83
XMagicImpl.checkAuth((errorCode, msg) -> {
            if (errorCode == TELicenseCheck.ERROR_OK) {
                showLoadResourceView();
            } else {
                TXCLog.e(TAG, "鉴权失败，请检查鉴权url和key" + errorCode + " " + msg);
            }
        });
```
2. **初始化素材：**
```java
 private void showLoadResourceView() {
        if (XmagicLoadAssetsView.isCopyedRes) {
            XmagicResParser.parseRes(getApplicationContext());
            initXMagic();
        } else {
            XmagicLoadAssetsView loadAssetsView = new XmagicLoadAssetsView(this);
            loadAssetsView.setOnAssetsLoadFinishListener(() -> {
                XmagicResParser.parseRes(getApplicationContext());
                initXMagic();
            });
        }
    }
```
3. **开启推流设置：**
```java
TXUGCRecord instance = TXUGCRecord.getInstance(this);
instance.setVideoProcessListener(new TXUGCRecord.VideoCustomProcessListener() {
    @Override
    public int onTextureCustomProcess(int textureId, int width, int height) {
        if (isPause == 0 && mXMagic !=null) {
            return mXMagic.process(textureId, width, height);
        }
        return 0;
    }
    @Override
    public void onDetectFacePoints(float[] floats) {
    }
    @Override
    public void onTextureDestroyed() {
        ...
    }
});
```
4. **将 textureId 传入到 SDK 内做渲染处理：**
在 VideoCustomProcessListener 接口的 `onTextureCustomProcess(int textureId, int width, int height)` 方法内添加如下代码。
```java
if (isPause == 0 && mXMagic !=null) {
    return mXMagic.process(textureId, width, height);
}
return 0;
```
5. **暂停/销毁 SDK：**
 onPause() 用于暂停美颜效果，可以在Activity/Fragment生命周期方法中执行， onDestroy 方法需要在 GL 线程调用（可以在 onTextureDestroyed 方法中调用 XMagicImpl 对象的 `onDestroy()`） ，更多使用请参考 Demo。
```java
mXMagic.onPause();   //暂停，与Activity的onPause方法绑定
mXMagic.onDestroy();  //销毁，需要在GL线程中调用
```
6. **布局中添加承载 SDK 美颜面板的布局：**
```xml
 <RelativeLayout
        android:id="@+id/panel_layout"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_alignParentBottom="true"
        android:visibility="gone"/>
```
7. **初始化面板**
```java
 private void initXMagic() {
        if (mXMagic == null) {
            mXMagic = new XMagicImpl(this, mBeautyPanel);
        }else{
           mXMagic.onResume();
        }
    }
```

具体操作请参见 Demo ⼯程的 `TCVideoRecordActivity.initXMagic();`⽅法。

