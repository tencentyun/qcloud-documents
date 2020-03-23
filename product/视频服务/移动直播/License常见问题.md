### 测试版 License 到期后是否可以延期？
测试 License 试用期最多28天，初次申请满14天后可延期一次，不支持二次延期，到期后请尽快 [购买正式 License](https://cloud.tencent.com/document/product/454/34750)。

### 测试版 License 能否更改 Android 的 Package Name 和 iOS 的 Bundle ID?
测试版 License 能更改 Android 的 Package Name 和 iOS 的 Bundle ID。
具体操作：登录控制台，单击测试版 License 信息右侧的【编辑】，进入编辑页面即可修改 Android 的 Package Name 和 iOS 的 Bundle ID。

### 正式版 License 能否更改 Android 的 Package Name 和 iOS 的 Bundle ID?
正式版 License 不能更改 Package Name 和 Bundle ID。

### License 可以同时支持多个 App 吗？
一个 License 只能对应一个 Package Name 和一个 Bundle ID，若多个 App 使用 SDK 功能，需要购买多个资源包新增多个 License。

### 如何获取 bundle ID 和 package name？

- 您可在 iOS 工程配置中的 `General->Identity` 中获取 bundle ID，如下所示：
>![](https://main.qcloudimg.com/raw/006d8b87e69b5e52ddabeb4d904cbb75.png) 
- 您可在 Android 工程下的 `Mainfest.xml` 文件中获取**应用包名称（package name）**，如下所示：
```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.huawei.player"
    android:versionCode="20181111"
    android:versionName="1.0">
```
