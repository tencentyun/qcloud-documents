本文主要介绍如何快速的将腾讯云 TEduBoard SDK 集成到您的项目中。如果您使用互动课堂方案，请前往 [互动课堂集成文档](https://github.com/tencentyun/TIC/blob/master/Android/%E6%8E%A5%E5%85%A5%E6%96%87%E6%A1%A3.md) 。

## 开发环境

- Android Studio 2.0+
- Android 4.2（SDK API 17）及以上系统

## 集成 TEduBoard SDK

您可以选择使用 Gradle 自动加载的方式，或者手动下载 aar 再将其导入到您当前的工程项目中。由于 TEduBoard SDK  内部使用 TIMSDK 作为内部信令通道，您还需自动或手动添加 TIMSDK 依赖项。



### 自动加载（aar）

TEduBoard SDK 和 TIMSDK 已经发布到 Maven Central 库，您可以通过配置 gradle 自动下载更新。
![](https://main.qcloudimg.com/raw/13352150cb8bb0a729c28500a05c338f.png)

#### 1. 添加 SDK 依赖

```java
dependencies {
    implementation 'com.tencent.edu:TEduBoardSdk:latest.release'
    implementation 'com.tencent.imsdk:imsdk:latest.release'
}
```

#### 2. 同步 SDK

单击 Sync Now，如果您的网络连接 Maven Central 没有问题，SDK 会自动下载集成到工程里。

### 手动下载（aar）

如果您的网络连接 Maven Central 有问题，也可以手动下载 SDK 集成到工程里。

#### 1. 下载 SDK

单击下载最新版 [TEduBaord SDK](https://tic-res-1259648581.cos.ap-shanghai.myqcloud.com/sdk/Android.zip) 。前往 [即时通讯官网](https://cloud.tencent.com/document/product/269/36887) 下载 TIMSDK。

#### 2. 导入 SDK

将下载到的 aar 文件拷贝到工程的 app/libs 目录下。
![](https://main.qcloudimg.com/raw/904930451506c7a4339db9da55207908.jpg)

#### 3. 指定本地仓库路径

在工程根目录下的 build.gradle 中，添加 flatDir，指定本地仓库路径。
![](https://main.qcloudimg.com/raw/9d365fabfe1c752e46d6d57f74bb5a03.jpg)

#### 4.  添加 SDK 依赖

在 app/build.gradle 中，添加引用 aar 包的代码。

```java
dependencies {
    implementation (name: "TEduBoardSdk-release", ext: "aar")
    implementation (name: "imsdk-4.6.1", ext: "aar")  
    implementation 'com.tencent.edu:TIWLogger:1.0.1.29'
}
```

![](https://main.qcloudimg.com/raw/273228f9f82fa23c7ec0ff8ce20cc8bf.png)

#### 5. 同步 SDK

单击 Sync Now，完成 TEduBoard SDK 集成。


### Google Play 境外版本集成方式
互动白板默认使用了腾讯浏览服务提供的 TBS SDK 。为了 apk 包大小增量，及时动态发版解决安全隐患，TBS SDK 采用了后台动态下发内核的方案。由于 Google Play 禁止任何二进制代码的下发（包括 so、dex、jar ）和插件化技术的使用，如果您有多渠道打包能力，您可以在境外版本须接入仅保留接口的 TBS SDK ，保证编译通过。

集成方法如下：

#### 1.下载并导入精简版 TBS SDK
[下载地址](https://sdk-1259648581.cos.ap-nanjing.myqcloud.com/android/tbs/tbs_sdk_noimpl_43799.jar) TBS SDK 的 jar 文件并拷贝到工程的 app/libs 目录下。

![](https://main.qcloudimg.com/raw/a3a00d36964e50f3ec4605900d9c8ab1.png)

#### 2. 指定本地仓库路径

在工程 app/build.gradle 中，添加 flatDir 配置，指定本地仓库路径。

```grovy
    sourceSets {
        main {
            jniLibs.srcDirs = ['libs']
        }
    }
```
![](https://main.qcloudimg.com/raw/79dd734da4ab48a503a11765cf128894.png)

#### 3.  添加 SDK 依赖

在 app/build.gradle 中，添加引用 jar 包以及不带 TBS 模块的白板 SDK。

```grovy
dependencies {
    implementation fileTree(include: ['*.jar'], dir: 'libs')
    implementation ('com.tencent.teduboard:TEduBoardSdk:latest.release'){
        exclude group: 'com.tencent.tbs.tbssdk', module: 'sdk'
    }
    ...
}
```
![](https://main.qcloudimg.com/raw/233c90a563a5288e1654eb6e459f313a.png)

>!这种情况下不能依赖带 TBS 模块的白板 SDK，否则会导致依赖冲突，无法编译通过。

## 配置 App 权限

在 AndroidManifest.xml 中配置 App 的权限，TEduBoard SDK 需要以下权限：

```java
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```



## 使用 TEduBoard SDK

#### 1. 创建白板控制器

使用如下代码创建并初始化白板控制器：

```java
// 创建并初始化白板控制器
//（1）鉴权配置
TEduBoardController.TEduBoardAuthParam authParam = new TEduBoardController.TEduBoardAuthParam(sdkAppId, userId, userSig);

//（2）白板默认配置
TEduBoardController.TEduBoardInitParam initParam = new TEduBoardController.TEduBoardInitParam(); 
mBoard = new TEduBoardController(context);

//（3）添加白板事件回调 实现TEduBoardCallback接口  
TEduBoardCallback callback = new TEduBoardController.TEduBoardCallback();
mBoard.addCallback(callback);

//（4）进行初始化
mBoard.init(authParam, classId, initParam);

```

其中 `sdkAppId`、`userId`、`userSig`、`classId`为需要您自己填写的参数。

>!请在主进程中执行初始化操作，如果您的 App 使用了多进程，请注意注意避免重复初始化。

#### 2. 监听白板关键事件  

在 白板事件回调接口 `TEduBoardCallback`的`onTEBError`和`onTEBWarning` 回调方法内监听白板事件

- [onTEBError 错误详情](https://cloud.tencent.com/document/product/1137/60708#.E9.94.99.E8.AF.AF.E4.BA.8B.E4.BB.B6)
- [onTEBWarning 警告详情](https://cloud.tencent.com/document/product/1137/60708#.E8.AD.A6.E5.91.8A.E4.BA.8B.E4.BB.B6)

```java  
/**
  * 白板错误回调
  * 必须要监听的事件
  *
  * @param code 错误码
  * @param msg  错误信息，编码格式为 UTF8
  */
void onTEBError(int code, String msg);  

/**
  * 白板警告回调
  * @param code 警告码
  * @param msg  警告信息，编码格式为 UTF8
  */
void onTEBWarning(int code, String msg);
```

#### 3. 白板窗口获取及显示
在 `onTEBInit`  回调方法内，使用如下代码获取并显示白板视图：

```java
// （1）在 Activity 的布局 xml 文件中，用 FrameLayout 占位，将来放 board 的 View。
<FrameLayout  
  android:id="@+id/board_view_container"  
  android:layout_width="match_parent"  
  android:layout_height="200dp"/>
```

```java
//（2）获取白板 View
View boardview = mBoard.getBoardRenderView();
//（3）添加到父视图中
FrameLayout.LayoutParams layoutParams = new FrameLayout.LayoutParams(FrameLayout.LayoutParams.MATCH_PARENT, FrameLayout.LayoutParams.MATCH_PARENT);
FrameLayout container = findViewById(R.id.board_view_container);
container.addView(boardview, layoutParams);
```

SDK 所有回调都在主线程内执行，因此可以在回调里直接执行 UI 操作。

#### 4. 白板数据同步

白板在使用过程中，需要在不同的用户之间进行数据同步（涂鸦数据等），SDK 默认使用 IMSDK 作为信令通道，您需要自行实现 IMSDK 的初始化、登录、加入群组操作，确保白板初始化时，IMSDK 已处于所指定的群组内。

步骤1：初始化 IMSDK

```java
TIMSdkConfig timSdkConfig = new TIMSdkConfig(appId)
    .enableLogPrint(true)
    .setLogLevel(TIMLogLevel.DEBUG); 
    //TODO::在正式发布时，设TIMLogLevel.OFF
TIMManager.getInstance().init(context, timSdkConfig);
```

如果您有其他业务使用了 IMSDK 并期望 IMSDK 的生命周期与 App 的生命周期保持一致，请在 Application 的 onCreate 方法中初始化 IMSDK，否则请在登录前初始化 IMSDK，在登出后反初始化 IMSDK 。

步骤2：登录 IMSDK

```java
TIMGroupManager.getInstance().login(userId, userSig, new TIMCallBack() {
      @Override
      public void onSuccess(String s) {
        // 创建 IM 群组成功
      }

      @Override
      public void onError(int errCode, String errMsg) {
        // 创建 IM 群组失败        
});
```

步骤3：加入群组

登录 IMSDK 成功后加入白板所在的群组。

```java
TIMGroupManager.getInstance().applyJoinGroup(groupId, desc + groupId, new TIMCallBack() {
      @Override
      public void onSuccess(String s) {
        // 加入 IM 群组成功
        // 此时可以调用白板初始化接口创建白板
      }

      @Override
      public void onError(int errCode, String errMsg) {
        // 加入 IM 群组失败 
});
```

如果 IM 群组不存在，请先创建群组。

```java
TIMGroupManager.getInstance().createGroup(param, new TIMValueCallBack<String>() {
      @Override
      public void onSuccess(String s) {
        // 创建 IM 群组成功
      }

      @Override
      public void onError(int errCode, String errMsg) {
        // 创建 IM 群组失败        
});
```


>!1. 推荐业务后台使用 [IM REST API](https://cloud.tencent.com/document/product/269/1615) 提前创建群组。<br>2. 不同的群组类型，群组功能以及成员数量有所区别，具体请查看 [IM 群组系统](https://cloud.tencent.com/document/product/269/1502)。


#### 5. 销毁白板

调用 `unInit` 方法后，内部将彻底销毁白板并停止计费，请您确保此接口的调用。

```java
mBoard.uninit();
```

如果您使用 IMSDK 作为信令通道，请根据业务的需要决定是否退出群组、退出登录并反初始化。

步骤1：退出群组

```java
TIMGroupManager.getInstance().quitGroup(groupId, new TIMCallBack() {//NOTE:在被挤下线时，不会回调
    @Override
    public void onSuccess() {
      // 退出 IM 群组成功
    }
    @Override
    public void onError(int errorCode, String errInfo) {
      // 退出 IM 群组成功
    }

});
```

步骤2：登出 IMSDK

```java
TIMManager.getInstance().logout(new TIMCallBack() {
    @Override
    public void onSuccess() {
      // 登出 IMSDK 成功
    }
    @Override
    public void onError(int errorCode, String errInfo) {
      // 登出 IMSDK 失败
    }
});
```

步骤3：反初始化 IMSDK

```java
TIMManager.getInstance().unInit();
```

如果您有其他业务使用了 IMSDK 并期望 IMSDK 的生命周期与 App 的生命周期保持一致，无需调用此接口。

