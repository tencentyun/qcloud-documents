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

#### 1. `#import` SDK

在项目需要使用 SDK API 的文件里，引入具体的头文件

```objc
#import <TEduBoard/TEduBoard.h>
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
