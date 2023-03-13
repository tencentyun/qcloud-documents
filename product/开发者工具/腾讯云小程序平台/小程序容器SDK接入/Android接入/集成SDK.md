## 前提条件

> 搭载 minSdkVersion 21 环境
> 


## 集成方式

### 集成 SDK
1. 工程根目录添加如下仓库

   ``` html
   buildscript {
       dependencies {
               classpath 'org.jetbrains.kotlin:kotlin-gradle-plugin:1.4.32'
                   }
               }
   allprojects {
       repositories {
               maven {
                   url 'https://tmf-work-maven.pkg.coding.net/repository/tmf/android/'
                 }
           }
   }
   ```
2. 项目中添加如下依赖：

   ``` cpp
   
   apply plugin: 'kotlin-android'
   apply plugin: 'kotlin-kapt'
     android {
         defaultConfig {
                 packagingOptions {
                      pickFirst 'lib/arm64-v8a/libc++_shared.so'
                      pickFirst 'lib/armeabi/libc++_shared.so'            
                      pickFirst 'lib/armeabi-v7a/libc++_shared.so'            
                      pickFirst 'lib/arm64-v8a/libmarsxlog.so'            
                      pickFirst 'lib/armeabi/libmarsxlog.so'            
                      pickFirst 'lib/armeabi-v7a/libmarsxlog.so'			
                      pickFirst 'lib/arm64-v8a/libv8jni.so'        
                      }    
               }
    }
   dependencies {
   	implementation "com.google.android.material:material:1.3.0-alpha03"
      implementation 'androidx.core:core-ktx:1.6.0'    
      //gosn    
      implementation 'com.google.code.gson:gson:2.8.6'    
      // ok-http    
      implementation "com.squareup.okhttp3:okhttp:3.12.13"    
      //x5内核    
      implementation 'com.tencent.tbs.tbssdk:sdk:43903'    
      // mini app start    
      kapt 'com.tencent.tmf.android:mini_annotation_processor:x.x.x'    
      implementation 'com.tencent.tmf.android:mini_core:x.x.x'
   }
   ```
- **如果开发者原来的工程中使用了 annotationProcessor 注解处理器，需要将所有 annotationProcessor 改为 kapt**。

- 如果开发者原来的工程中已集成了腾讯 X5 内核，则需要去除如下依赖

   ``` cpp
   implementation 'com.tencent.tbs.tbssdk:sdk:43903'
   ```
- 集成过程可能会遇到如下问题：

   ``` cpp
   AAPT: error: attribute android:requestLegacyExternalStorage not found.
   ```

   在 application 标签下添加如下代码：

   ``` cpp
   <application
       android:theme="@style/AppTheme"
       tools:replace="android:icon"
     	tools:remove="android:requestLegacyExternalStorage">
    /application>
   ```
- 集成过程中可能会出现如下错误
   

   > Duplicate class android.support.v4.app.INotificationSideChannel found in modules core-1.3.1-runtime (androidx.core:core:1.3.1) and support-v4-21.0.3-runtime (com.android.support:support-v4:21.0.3)
   > 


   在 `gradle.properties` 中添加如下代码

   ``` html
   android.useAndroidX=true
   android.enableJetifier=true
   ```   

   > **说明：**
   > 

   > x.x.x.x为版本号，参考 demo 工程中最新 SDK 版本。
   > 


### 扫码能力

开发者小程序如果使用了小程序扫码能力，需要添加如下 SDK 支持扫码功能；如未使用，无需添加，这样可以减小 App 包大小。
``` html
//扫码扩展组件
implementation 'com.tencent.tmf.android:mini_extra_qrcode:x.x.x'
```

> **说明：**
> 

> x.x.x.x为版本号，参考 demo 工程中最新 SDK 版本。
> 


### 腾讯定位地图能力

针对国内 App 开发，开发者小程序如果使用了小程序地图能力，需要添加如下 SDK 支持腾讯地图功能；如未使用，无需添加，这样可以减小 App 包大小。
``` html
implementation 'com.tencent.tmf.android:mini_extra_map:1.4.0-SNAPSHOT'
implementation 'com.tencent.map:tencent-map-vector-sdk:4.5.10'
implementation 'com.tencent.map:sdk-utilities:1.0.7'
implementation 'com.tencent.map.geolocation:TencentLocationSdk-openplatform:7.4.7'
```

您需要在您的腾讯位置服务控制台配置项目，并获取访问腾讯地图服务所需要的 API 密钥，具体操作步骤请参考 [开发指南](https://lbs.qq.com/mobile/androidMapSDK/developerGuide/getKey)。

完成上述操作后，您需要在 Android 工程中配置您的 API 密钥。在 AndroidManifest.xml 文件中添加以下 meta-data，并将您的 API 密钥填入 (YOUR_API_KEY) 位置：
``` html
<application
    ...    
    <meta-data        
    android:name="TencentMapSDK"        
    android:value="(YOUR_API_KEY)" />    
    ...
</application>
```

### Google 及华为定位地图能力

针对海外 App 开发，开发者小程序如果使用了小程序地图能力，需要添加如下 SDK 支持 Google Map 功能；如未使用，无需添加，这样可以减小 App 包大小。
``` html
implementation 'com.tencent.tmf.android:mini_extra_google_map:1.4.0-SNAPSHOT'
implementation 'com.google.android.gms:play-services-maps:18.1.0'
implementation 'com.google.maps.android:android-maps-utils:2.3.0'
```

由于部分华为设备不支持内嵌 Google Map，可能导致地图无法显示。您可以额外接入 Petal Map 作为补充方案，小程序框架将在华为设备上优先使用 Petal Map。
``` html
implementation 'com.tencent.tmf.android:mini_extra_huawei_map:1.4.0-SNAPSHOT'
implementation 'com.huawei.hms:maps:6.9.0.300'
implementation 'com.huawei.hms:maps-basic:6.9.0.300'
implementation 'com.huawei.hms:site:6.5.1.300'
```

使用 Google Map 的情形，您需要在您的 Google Cloud Console 配置 Google Cloud 项目，并获取访问 Google 地图服务所需要的 API 密钥，具体操作步骤请参考 [在 Google Cloud Console 中进行设置](https://developers.google.com/maps/documentation/android-sdk/cloud-setup?hl=zh-cn) 以及 [使用 API 密钥](https://developers.google.com/maps/documentation/android-sdk/get-api-key?hl=zh-cn)。

完成上述操作后，您需要在 Android 工程中配置您的 API 密钥。在 AndroidManifest.xml 文件中添加以下 meta-data，并将您的 API 密钥填入 (YOUR_API_KEY) 位置：
``` html
<application
    ...
    <meta-data
        android:name="com.google.android.geo.API_KEY"
        android:value="(YOUR_API_KEY)" />
     ...
</application>
```

使用 Petal Map 的情形，您需要在您的华为管理控制台建立项目、开通地图以及位置服务并获取位置服务所使用的 API 秘钥，具体操作步骤参考[《配置AppGallery Connect》](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/android-sdk-config-agc-0000001061560289)。然后按照[《集成HMS Core SDK》](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/android-sdk-integrating-sdk-0000001061671869)的引导下载“agconnect-services.json”文件至您的项目中并配置华为 AGC 插件。

您需要在 AndroidManifest.xml 文件中添加以下 meta-data，并将您的 API 密钥填入 (YOUR_API_KEY) 位置以正常使用华为的位置服务：
``` html
<application
    ...
    <meta-data        
    android:name="HuaweiApiKey"        
    android:value="(YOUR_API_KEY)" />    
    ...
</application>
```

> **注意：**
> 

> 出于安全考虑，建议您为位置服务单独申请 API 密钥。
> 


