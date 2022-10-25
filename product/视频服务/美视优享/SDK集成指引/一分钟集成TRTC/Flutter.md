## 步骤1：美颜资源下载与集成

1. 根据您购买的套餐 [下载 SDK](https://cloud.tencent.com/document/product/616/65876)。
2. 添加文件到自己的工程中：
<dx-tabs>
::: Android
1. 在 app 模块下找到 build.gradle 文件，添加您对应套餐的 maven 引用地址，例如您选择的是S1-04套餐，则添加如下：
```groovy
dependencies {
      implementation 'com.tencent.mediacloud:TencentEffect_S1-04:latest.release'
   }
```
**各套餐对应的 maven 地址，请参见[文档](https://cloud.tencent.com/document/product/616/65891)**。
2. 在 app 模块下找到 src/main/assets 文件夹，如果没有则创建，检查下载的 SDK 包中是否有 MotionRes 文件夹，如果有则将此文件夹拷贝到 `../src/main/assets` 目录下。
3. 在 app 模块下找到 AndroidManifest.xml 文件，在 application 表填内添加如下标签
```xml
 <uses-native-library
           android:name="libOpenCL.so"
           android:required="true" />
```
添加后如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/adca155b8fa60600465bdfc6e78ebb2b.png)
:::
::: iOS
1. 添加美颜资源到您的工程。添加后如下图（您的资源种类跟下图不完全一致）：
![](https://qcloudimg.tencent-cloud.cn/raw/e5cb4984aa2bfa14fd4f837acf465cfa.png)
2. 在 demo 中把 demo/lib/producer 里面的4个类：BeautyDataManager、BeautyPropertyProducer、BeautyPropertyProducerAndroid 和 BeautyPropertyProducerIOS 复制添加到自己的 Flutter 工程中，这4个类是用来配置美颜资源，把美颜类型展示在美颜面板中。
:::
</dx-tabs>


## 步骤2：引用 Flutter 版本 SDK

在工程的 pubspec.yaml 文件中添加如下引用：
```json
 tencent_effect_flutter:
   git:
     url: https://github.com/TencentCloud/tencenteffect-sdk-flutter
```

## 步骤3：与 TRTC 关联
<dx-tabs>
::: Android
在应用的 application 类的 oncreate 方法（或 FlutterActivity 的 onCreate 方法）中添加如下代码：
```jav
TRTCCloudPlugin.register(new XmagicProcesserFactory());
```
:::
::: iOS
在应用的 AppDelegate 类中的 didFinishLaunchingWithOptions 方法里面中添加如下代码：
```objective-c
XmagicProcesserFactory *instance = [[XmagicProcesserFactory alloc] init];
[TencentTRTCCloud registerWithCustomBeautyProcesserFactory:instance];
```
添加后如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/3f2de0a60696f18daedde2228d65076a.png)

:::
</dx-tabs>

## 步骤4：调用资源初始化接口
```dart
  String dir =  await BeautyDataManager.getInstance().getResDir();
   TXLog.printlog('文件路径为：$dir');
   TencentEffectApi.getApi()?.initXmagic(dir,(reslut) {
     _isInitResource = reslut;
     callBack.call(reslut);
     if (!reslut) {
       Fluttertoast.showToast(msg: "初始化资源失败");
     }
   }); TencentEffectApi.getApi()?.initXmagic((reslut) {
     if (!reslut) {
       Fluttertoast.showToast(msg: "初始化资源失败");
     }
   });
```

## 步骤5：进行美颜授权
```dart
TencentEffectApi.getApi()?.setLicense(licenseKey, licenseUrl,
           (errorCode, msg) {
         TXLog.printlog("打印鉴权结果 errorCode = $errorCode   msg = $msg");
         if (errorCode == 0) {
            //鉴权成功
         }
       });
```

## 步骤6：开启美颜
```dart
///开启美颜操作
 var enableCustomVideo = await trtcCloud.enableCustomVideoProcess(open);
```

## 步骤7：设置美颜属性

```dart
    TencentEffectApi.getApi()?.updateProperty(_xmagicProperty!);
///_xmagicProperty 可通过 BeautyDataManager.getInstance().getAllPannelData();获取所有的属性，需要使用美颜属性的时候可通过updateProperty方法设置属性。
```

## 步骤8：设置其他属性

- **暂停美颜音效**
```dart
 TencentEffectApi.getApi()?.onPause();  
```
- **恢复美颜音效**
```dart
TencentEffectApi.getApi()?.onResume();
```
- **监听美颜事件**
```dart
TencentEffectApi.getApi()
       ?.setOnCreateXmagicApiErrorListener((errorMsg, code) {
         TXLog.printlog("创建美颜对象出现错误 errorMsg = $errorMsg , code = $code");
   });   ///需要在创建美颜之前进行设置
```
- **设置人脸、手势、身体检测状态回调**
```dart
TencentEffectApi.getApi()?.setAIDataListener(XmagicAIDataListenerImp());
```
- **设置动效提示语回调函数**
```dart
TencentEffectApi.getApi()?.setTipsListener(XmagicTipsListenerImp());
```
- **设置人脸点位信息等数据回调（S1-05 和 S1-06 套餐才会有回调）**
```dart
TencentEffectApi.getApi()?.setYTDataListener((data) {
     TXLog.printlog("setYTDataListener  $data");
   });
```
- **移除所有回调**。在页面销毁的时候需要移除掉所有的回调：
```dart
 TencentEffectApi.getApi()?.setOnCreateXmagicApiErrorListener(null);
 TencentEffectApi.getApi()?.setAIDataListener(null);
 TencentEffectApi.getApi()?.setYTDataListener(null);
 TencentEffectApi.getApi()?.setTipsListener(null);
```

>? 接口详细可参考接口文档，其他可参考 Demo 工程。

## 步骤9：添加和删除美颜面板上的美颜数据
在 BeautyDataManager、BeautyPropertyProducer、BeautyPropertyProducerAndroid 和 BeautyPropertyProducerIOS这4个类中，您可以自主操作美颜面板数据的配置。
- **添加美颜资源**
把您的资源文件按照步骤一中的方法添加到对应的资源文件夹里面。例如，您需要添加2D动效的资源：
	1. 您应该把资源放在工程的 `android/xmagic/src.mian/assets/MotionRes/2dMotionRes` 目录下：
<img src="https://qcloudimg.tencent-cloud.cn/raw/7e91b97099e3d337de31c4893686759b.png" style="zoom:50%;" />
	2. 并且把资源添加到工程的 `ios/Runner/xmagic/2dMotionRes.bundle` 目录下。
<img src="https://qcloudimg.tencent-cloud.cn/raw/8c806cb1c77d9c49b787ab17f77a2f0d.png" style="zoom:50%;" />
- **删除美颜资源**
对于某些License没有授权美颜和美体的部分功能，美颜面板上不需要展示这部分功能，需要在美颜面板数据的配置中删除这部分功能的配置。
例如，删除口红特效：分别在 BeautyPropertyProducerAndroid 类和 BeautyPropertyProducerIOS 类中的 getBeautyData 方法中删除以下代码。
<img src="https://qcloudimg.tencent-cloud.cn/raw/730abb4688d9f9675cf1bef679b0b2c1.png" style="zoom:50%;" />

