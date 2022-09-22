本文主要介绍如何快速的将腾讯云 TEduBoard SDK 集成到您的项目中。如果您使用互动课堂方案，请前往 [互动课堂集成](https://github.com/tencentyun/TIC/blob/master/Android/%E6%8E%A5%E5%85%A5%E6%96%87%E6%A1%A3.md)。

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

单击下载最新版 [TEduBaord SDK](https://cloud.tencent.com/document/product/1137/43150) 。前往 [即时通信 IM](https://cloud.tencent.com/document/product/269/36887) 下载 TIMSDK。

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
    implementation (name: "imsdk-plus-6.6.3002", ext: "aar") // IM的版本请尽量用新版本，具体请查阅IM的更新日志 https://cloud.tencent.com/document/product/269/1606
    implementation 'com.tencent.edu:TIWLogger:1.0.1.76'
    implementation 'com.tencent.edu:TIWCache:1.0.0.91'
}
```

![](https://main.qcloudimg.com/raw/273228f9f82fa23c7ec0ff8ce20cc8bf.png)

#### 5. 同步 SDK

单击 Sync Now，完成 TEduBoard SDK 集成。

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

- [onTEBError 错误详情](https://cloud.tencent.com/document/product/1137/39970#teduboardcontroller.teduboarderrorcode)
- [onTEBWarning 警告详情](https://cloud.tencent.com/document/product/1137/39970#teduboardcontroller.teduboardwarningcode)

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
在 onTEBInit 回调方法内，使用如下代码获取并显示白板视图：

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

V2TIMSDKConfig timSdkConfig = new V2TIMSDKConfig();
boolean result = V2TIMManager.getInstance().initSDK(context, sdkAppID, timSdkConfig);

```

如果您有其他业务使用了 IMSDK 并期望 IMSDK 的生命周期与 App 的生命周期保持一致，请在 Application 的 onCreate 方法中初始化 IMSDK，否则请在登录前初始化 IMSDK，在登出后反初始化 IMSDK 。

步骤2：登录 IMSDK

```java
TIMGroupManager.getInstance().login(userId, userSig, new TIMCallBack() {
      @Override
      public void onSuccess(String s) {
        
      }

      @Override
      public void onError(int errCode, String errMsg) {
        // 创建 IM 群组失败        
});

V2TIMManager.getInstance().login(userId, userSig, new V2TIMCallback() {
    @Override
    public void onSuccess() {
      // 登录成功
    }

    @Override
    public void onError(int errCode, String errMsg) {
      // 登录失败
    }
});

```

步骤3：加入群组

登录 IMSDK 成功后加入白板所在的群组。

```java
V2TIMManager.getInstance().joinGroup(classId, "board group" + classId, new V2TIMCallback() {
    @Override
    public void onSuccess() {
      // 加群成功
    }

    @Override
    public void onError(int i, String s) {
      // 加群失败
    }
});
```

如果 IM 群组不存在，请先创建群组。

```java
V2TIMManager.getGroupManager().createGroup(groupInfo, null, new V2TIMValueCallback<String>() {
    @Override
    public void onError(int errCode, String errMsg) {
        
    }

    @Override
    public void onSuccess(String s) {
        
    }
});
```

>!1. 推荐业务后台使用 [IM REST API](https://cloud.tencent.com/document/product/269/1615) 提前创建群组。<br>2. 不同的群组类型，群组功能以及成员数量有所区别，具体请查看 [IM 群组系统](https://cloud.tencent.com/document/product/269/1502)。


#### 5. 销毁白板

调用 unInit 方法后，内部将彻底销毁白板并停止计费，请您确保此接口的调用。

```java
mBoard.uninit();
```

如果您使用 IMSDK 作为信令通道，请根据业务的需要决定是否退出群组、退出登录并反初始化。

步骤1：退出群组

```java
V2TIMManager.getInstance().quitGroup(classId, new V2TIMCallback() {
  @Override
  public void onSuccess() {
      
  }

  @Override
  public void onError(int i, String s) {
      
  }
});
```

步骤2：登出 IMSDK

```java
// IM登出
public void logout(final IMCallBack callBack) {
    V2TIMManager.getInstance().logout(new V2TIMCallback(){
        @Override
        public void onSuccess() {
            
        }

        @Override
        public void onError(int errCode, String errMsg) {
            
        }
    });
}
```

步骤3：反初始化 IMSDK

```java
V2TIMManager.getInstance().unInitSDK();
```

如果您有其他业务使用了 IMSDK 并期望 IMSDK 的生命周期与 App 的生命周期保持一致，无需调用此接口。

