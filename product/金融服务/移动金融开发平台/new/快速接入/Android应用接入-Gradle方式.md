### 步骤一：创建工程并导入配置文件
1. Android Studio 创建项目，注意项目包名需与控制台应用包名一致，否则初始化校验无法通过。
2. 将 `tmf-android-configurations.json` 拷贝到 `app/src/main/assets` 目录，完成配置文件导入。配置文件下载请在控制台应用接入处下载。
>?如果您在初始 TMFBase 时不指定配置文件名字，那么请保证配置文件的名字是 `tmf-android-configurations.json`，放置在 assets 根目录下，不能放置在 asset 子目录。

### 步骤二：配置 Gradle 依赖
1. 在工程 build.gradle 下面配置仓库地址。
```groovy
allprojects {
   repositories {
     maven {
        url 'https://tmf-work-maven.pkg.coding.net/repository/tmf/android/'
     }
   }
}
```
>?仓库用户名和密码请向管理员获取。
>

2. 在 `app/build.gradle` 下面配置组件依赖，框架最小依赖项如下：
```groovy
implementation 'com.tencent.tmf.android:base-core:+'
implementation 'com.tencent.tmf.android:base:+'
```
3. TMF 内部组件使用了 libc++_shared.so，为了避免与其他三方库冲突，请在 `app/build.gradle` 中增加如下配置：
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
4. 在 `app/build.gradle` 中配置 Java 编译选项：
```goovy
android{
	   compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}
```
