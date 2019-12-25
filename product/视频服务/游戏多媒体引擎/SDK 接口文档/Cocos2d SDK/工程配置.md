为方便 Cocos2D 开发者调试和接入腾讯云游戏多媒体引擎产品 API，本文档主要为您介绍适用于 Cocos2D 开发的工程配置指引。



## SDK 准备
1. 请下载相关 Demo 及 SDK，详情请参见 [下载指引](https://cloud.tencent.com/document/product/607/18521)。
2. 解压获取到的 SDK 资源。
3. 文件夹内容如下：
 - GMESDK：游戏音视频 SDK framework 文件。
 - GMECocosDemo：游戏音视频 SDK 示例工程。

>?SDK 支持在 Mac 系统上编译。




## iOS Xcode 配置

1. 将 framework 添加到 Xcode 工程中并设置头文件引用位置。（GMESDK 文件夹中的 framework 文件，必须添加到工程中）
2. 添加依赖库，参考下图进行：
![](https://main.qcloudimg.com/raw/b6156b8c7a596248c148607070e38f67.png)

## Android 配置

1. 将 gmesdk.jar 加入到 libs 库中。
![](https://main.qcloudimg.com/raw/167b3fb575b65539aeaf9c700383e7c8.png)
2. 在 Activity 中导入 so 文件。示例如下：
```
public class AppActivity extends Cocos2dxActivity {
    static final String TAG = "AppActivity";
    static OpensdkGameWrapper gameWrapper ;
    static {
        OpensdkGameWrapper.loadSdkLibrary();
    }
}
```
3. 在 oncreate 函数中进行初始化，顺序不能出错。
```
protected void onCreate(Bundle savedInstanceState) {
        super.setEnableVirtualButton(false);
        super.onCreate(savedInstanceState);

        //初始化， 顺序不能错
        gameWrapper = new OpensdkGameWrapper(this);
        runOnGLThread(new Runnable() {
            @Override
            public void run() {
                gameWrapper.initOpensdk();
            }
        });
}
```
4. 将自己的工程进行编译选项配置。请参考 GME Cocos Demo 中的 Android.mk。
 - 路径：GMECocos/GMECocosDemo/proj.android-studio/app/jni/Android.mk
 - preBuild.mk 文件的路径：/Users/username/Downloads/GMECocos/GMESDK/android/bin/preBuild.mk


## 导出不同平台

从 Cocos2D 引擎导出不同平台，需要做相应的工程配置：

|平台       | 工程配置           
| ------------- |:-------------:|
| Android |[Android 工程配置文档](https://cloud.tencent.com/document/product/607/15203)|
| iOS     	|[iOS 工程配置文档](https://cloud.tencent.com/document/product/607/15219)|
| macOS     	|[macOS 工程配置文档](https://cloud.tencent.com/document/product/607/18617)|





