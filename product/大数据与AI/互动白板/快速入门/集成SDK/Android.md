## 集成 SDK

本文主要介绍如何快速的将腾讯云 TEduBoard SDK 集成到您的项目中。

## 开发环境

- Android Studio 2.0+
- Android 4.2 （SDK API 17）及以上系统


## 集成 TEduBoard SDK

您可以选择使用 Gradle 自动加载的方式，或者手动下载 aar 再将其导入到您当前的工程项目中。由于TEduBoard SDK 内部使用 TIMSDK 作为内部信令通道，您还需自动或手动添加 TIMSDK 依赖项。



### 自动加载（aar）

TEduBoard SDK 和 TIMSDK 已经发布到 jcenter 库，您可以通过配置 gradle 自动下载更新。

![](https://main.qcloudimg.com/raw/13352150cb8bb0a729c28500a05c338f.png)

#### 1. 添加 SDK 依赖

```java
dependencies {
    implementation 'com.tencent.teduboard:TEduBoardSdk:latest.release'
    implementation 'com.tencent.imsdk:imsdk:latest.release'
}
```

#### 2. 同步 SDK

单击 Sync Now 按钮，如果您的网络连接 jcenter 没有问题，很快 SDK 就会自动下载集成到工程里。

### 手动下载（aar）

如果您的网络连接 jcenter 有问题，也可以手动下载 SDK 集成到工程里.

#### 1. 下载 SDK

单击下载最新版 [TEduBaord SDK](https://tic-res-1259648581.cos.ap-shanghai.myqcloud.com/sdk/Android.zip)。前往 [即时通讯官网](https://cloud.tencent.com/document/product/269/36887) 下载 TIMSDK。


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
}
```

![](https://main.qcloudimg.com/raw/273228f9f82fa23c7ec0ff8ce20cc8bf.png)

#### 5. 同步 SDK

单击 Sync Now 按钮，完成 TEduBoard SDK 集成。


## 配置 App 权限

在 AndroidManifest.xml 中配置 App 的权限，TEduBoard SDK 需要以下权限：

```java
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```



## 使用 TEduBoard SDK

#### 1. 初始化 SDK

继承 Application ，并在 onCreate 生命周期里初始化。如果您的 App 使用了多进程，注意在主进程进行操作，避免重复初始化。

```java

private TICManager mTIC;
...

public void onCreate() {
        super.onCreate();

        if (isMainProcess(...)) {    // 仅在主线程初始化
            // 初始化TIC
            mTIC = TICManager.getInstance();
            mTIC.init(this, sdkAppId);
        }
}
```

然后在 AndroidManifest.xml 文件中，使用以上定义的 Application。

``` xml 
<application
        android:name="您定义的 Application 类"
        android:allowBackup="true"
        android:icon="@mipmap/ic_icon"
        android:label="@string/app_name"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        
        ....

</application>

```

#### 2. 创建白板控制器

使用如下代码创建并初始化白板控制器：

```java
// 创建并初始化白板控制器
//（1）鉴权配置
TEduBoardController.TEduBoardAuthParam authParam = new TEduBoardController.TEduBoardAuthParam(sdkAppId, userId, userSig);

//（2）白板默认配置
TEduBoardController.TEduBoardInitParam initParam = new TEduBoardController.TEduBoardInitParam(); 
mBoard = new TEduBoardController(context);
mBoard.init(authParam, classId, initParam);
//（3）添加白板事件回调
mBoard.addCallback(callback);
```

其中 `sdkAppId`、`userId`、`userSig`、`classId`为需要您自己填写的参数。

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

白板在使用过程中，需要在不同的用户之间进行数据同步（涂鸦数据等），SDK 支持两种不同的数据同步模式。

**使用腾讯云 IMSDK 同步数据**

如果您在使用白板的同时使用了腾讯云 IMSDK，则只需要在初始化白板控制器时进行指定 initParam 参数的 timSync 字段为 true 即可实现数据同步。
```java
// 使用腾讯的 IM 进行消息传递，前提是您的项目中已经集成 TIM。
// TEduBoardInitParam 的 timSync 的默认值为 true
TEduBoardController.TEduBoardInitParam initParam = new TEduBoardController.TEduBoardInitParam(); 
initParam.timSync = true;
```

>! 您需要自行实现 IMSDK 的登录、加入群组等操作，确保白板初始化时，IMSDK 已处于所指定的群组内。

步骤一、初始化 IMSDK

```java
TIMSdkConfig timSdkConfig = new TIMSdkConfig(appId)
    .enableLogPrint(true)
    .setLogLevel(TIMLogLevel.DEBUG); 
    //TODO::在正式发布时，设TIMLogLevel.OFF
TIMManager.getInstance().init(context, timSdkConfig);
```

如果您有其他业务使用了 IMSDK 并期望 IMSDK 的生命周期与 App 的生命周期保持一致，请在 Application 的 onCreate 方法中初始化 IMSDK，否则请在登录前初始化 IMSDK，在登出后反初始化 IMSDK。

步骤二、登录 IMSDK

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
```

步骤三、加入群组

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

注意事项

1. 推荐业务后台使用 [IM REST API](https://cloud.tencent.com/document/product/269/1615) 提前创建群组。
2. 不同的群组类型，群组功能以及成员数量有所区别，具体请查看 [IM 群组系统](https://cloud.tencent.com/document/product/269/1502)。

**使用自定义的数据通道同步数据**

如果使用自已的通道进行消息传递，则需要按下面步骤进行：

```java
//（1）将 TEduBoardInitParam 的 timSync 参数初始为 NO
TEduBoardController.TEduBoardInitParam initParam = new TEduBoardController.TEduBoardInitParam(); 
initParam.timSync = false;

//（2）TEduBoard 有数据要同步给其他用户时，将调用 TEduBoardDelegate 接口中的 onTEBSyncData 函数
 @Override
 public void onTEBSyncData(String data) {
   // 使用自定义的通道，发送 data 数据给其他白板用户。
 }

//（3）在收到其他用户的信息时，将消息传递给 TEduBoard.
mBoard.addSyncData(data);
```

>! 实时录制功能在自定义数据通道模式下不可用


#### 5. 销毁白板

调用 `unInit` 方法后，内部将彻底销毁白板并停止计费，请您确保此接口的调用。

```java
mBoard.uninit();
```

如果您使用IMSDK作为信令通道，请根据业务的需要决定是否退出群组、退出登录并反初始化。

步骤一、退出群组

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

步骤二、登出 IMSDK

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

步骤三、反初始化 IMSDK

```java
TIMManager.getInstance().unInit();
```

如果您有其他业务使用了 IMSDK 并期望 IMSDK 的生命周期与 App 的生命周期保持一致，无需调用此接口。
