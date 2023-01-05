# Android应用接入-Gradle方式

## 1、创建工程并导入配置文件

1. Android Studio创建项目，注意项目包名需与控制台应用包名一致，否则初始化校验无法通过。

2. 将tmf-android-configurations.json拷贝到app/src/main/assets目录，完成配置文件导入。配置文件下载请参见[下载配置文件](../../在控制台创建应用/下载配置文件.md)

   > ![说明](../img/说明.png)说明：如果您在初始TMFBase时不指定配置文件名字，那么请保证配置文件的名字是tmf-android-configurations.json，放置在assets根目录下，不能放置在asset子目录。

## 2、配置Gradle依赖

1. 在工程build.gradle下面配置仓库地址

   ```groovy
   buildscript {
      repositories {
      maven {
         url 'https://t.pinpad.qq.com/fHKFBbEjd/repository/mavenpublic/'
         credentials {
            username ''
            password ''
      }
   }
   ```

   > ![说明](/Users/pekinglin/Code/tmf/TMF_MD/03开发指南/接入Android/接入指南/images/说明.png)说明：仓库用户名和密码请向管理员获取。

2. 在app/build.gradle下面配置组件依赖，框架最小依赖项如下

   ```groovy
   implementation 'com.tencent.tmf.android:base-core:+'
   implementation 'com.tencent.tmf.android:base:+'
   ```

3. TMF内部组件使用了libc++_shared.so, 为了避免与其他三方库冲突，请在app/build.gradle中增加如下配置：

   ```groovy
   android{
      ...
      packagingOptions {
   	   pickFirst 'lib/arm64-v8a/libc++_shared.so'
   	   pickFirst 'lib/armeabi/libc++_shared.so'
   	   pickFirst 'lib/armeabi-v7a/libc++_shared.so'
      }
      ...
   }
   ```

4. 在app/build.gradle中配置Java编译选项

   ```goovy
   android{
   	   compileOptions {
           sourceCompatibility JavaVersion.VERSION_1_8
           targetCompatibility JavaVersion.VERSION_1_8
       }
   }
   ```