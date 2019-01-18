
本文将指导您在客户端将通过仓库集成 iLiveSDK，并向腾讯云完成登录过程。
## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/Android/demo_login.zip)

## 前提条件
要求用户在[ 实时音视频官网 ](https://cloud.tencent.com/product/trtc)完成服务开通及应用创建。

## 相关概念
 - [实时音视频应用](https://cloud.tencent.com/document/product/647/16792#.E5.AE.9E.E6.97.B6.E9.9F.B3.E8.A7.86.E9.A2.91.E5.BA.94.E7.94.A8)
 - [应用标识( sdkAppId )](https://cloud.tencent.com/document/product/647/16792#.E5.BA.94.E7.94.A8.E6.A0.87.E8.AF.86.EF.BC.88-sdkappid-.EF.BC.89)
 - [帐号类型( accountType )](https://cloud.tencent.com/document/product/647/16792#.E5.B8.90.E5.8F.B7.E7.B1.BB.E5.9E.8B.EF.BC.88-accounttype-.EF.BC.89)
 - [用户标识( userId )](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E6.A0.87.E8.AF.86.EF.BC.88-userId-.EF.BC.89)
 - [用户签名( userSig )](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E7.AD.BE.E5.90.8D.EF.BC.88-usersig-.EF.BC.89)

## 获取 userSig
客户端的每一个用户都需要一个独立的 userSig，userSig 是有效期的( 在生成时设置，一般为三个月 )，如果 userSig 过期，用户登录时会收到错误码 8051，这时用户需要重新生成 userSig，拿到新的 userSig 再登录。

```java
    /** 票据过期(需更新票据userSig) */
    public static final int ERR_EXPIRE              = 8051;
```

> 注意： 关于 userSig 的获取请参考[ 用户鉴权 ](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E7.AD.BE.E5.90.8D.EF.BC.88-usersig-.EF.BC.89)。 在调试期间您可以直接使用控制台的开发辅助工具生成 userSig。

## 添加依赖( 集成 SDK )
修改 build.gradle 文件，在 dependencies 中添加 iLiveSDK 的依赖：
```
compile 'com.tencent.ilivesdk:ilivesdk:latest.release'  //其中latest.release指代最新iLiveSDK版本号
```

## 初始化 iLiveSDK
首先添加 DemoApp.java 并继承 Application：
```Java
public class DemoApp extends Application {
    @Override
    public void onCreate() {
        super.onCreate();

        // 判断仅在主线程进行初始化
        if (MsfSdkUtils.isMainProcess(this)) {
            // 初始化iLiveSDK
            ILiveSDK.getInstance().initSdk(this, Constants.SDKAPPID, Constants.ACCOUNTTYPE);
            // 初始化iLiveSDK房间管理模块
            ILiveRoomManager.getInstance().init(new ILiveRoomConfig());
        }
    }
}
```
并在 AndroidManifest.xml 的 application 中申明：
```
<application
        ......
        android:name=".DemoApp">
        ......
    </application>
```

## 创建登录模块
首先创建一个登录模块与 Activity 通讯的接口：
```Java
public interface ILoginView {
    // 登录成功
    void onLoginSDKSuccess();
    // 登录失败
    void onLoginSDKFailed(String module, int errCode, String errMsg);
}
```
同时创建一个 LoginHelper.java 用于登录操作：
```Java
public class LoginHelper {
    private ILoginView loginView;

    public LoginHelper(ILoginView view){
        loginView = view;
    }

    public void loginSDK(String userId, String userSig){
        ILiveLoginManager.getInstance().iLiveLogin(userId, userSig, new ILiveCallBack() {
            @Override
            public void onSuccess(Object data) {
                loginView.onLoginSuccess();
            }

            @Override
            public void onError(String module, int errCode, String errMsg) {
                loginView.onLoginFailed(module, errCode, errMsg);
            }
        });
    }
}
```
## 监听帐户状态
用户在登录后，也是有可能强制下线的( 帐号重复登录被踢，userSig 过期 )，所以应用需要监听这个状态。
为了全局监听，可以创建一个观察者：
```Java
/**
 * 状态观察者
 */
public class StatusObservable implements ILiveLoginManager.TILVBStatusListener {

    // 消息监听链表
    private LinkedList<ILiveLoginManager.TILVBStatusListener> listObservers = new LinkedList<>();
    // 句柄
    private static StatusObservable instance;


    public static StatusObservable getInstance(){
        if (null == instance){
            synchronized (StatusObservable.class){
                if (null == instance){
                    instance = new StatusObservable();
                }
            }
        }
        return instance;
    }


    // 添加观察者
    public void addObserver(ILiveLoginManager.TILVBStatusListener listener){
        if (!listObservers.contains(listener)){
            listObservers.add(listener);
        }
    }

    // 移除观察者
    public void deleteObserver(ILiveLoginManager.TILVBStatusListener listener){
        listObservers.remove(listener);
    }

    // 获取观察者数量
    public int getObserverCount(){
        return listObservers.size();
    }

    @Override
    public void onForceOffline(int error, String message) {
        // 拷贝链表
        LinkedList<ILiveLoginManager.TILVBStatusListener> tmpList = new LinkedList<>(listObservers);
        for (ILiveLoginManager.TILVBStatusListener listener : tmpList){
            listener.onForceOffline(error, message);
        }
    }
}
```
并在登录成功后调用接口设置监听：
```Java
ILiveLoginManager.getInstance().setUserStatusListener(StatusObservable.getInstance());
```
这样用户在收到 onForceOffline 事件就知道自己被踢下线了。

## UI 开发
客户端需要登录，所以可能需要单独一个页面来输入用户名，密钥，这些都是 Android 开发基础知识，就不一一讲解了。

登录应用的 onCreated 事件中，可以创建上面定义的模块：
```Java
loginHelper = new LoginHelper(this);
```
然后在单击登录事件后，获取用户输入的 userId 和 userSig，调用 loginHelper 的登录接口进行登录：
```Java
loginHelper.loginSDK(userId, userSig);
```

## 常见问题
- 下载 aar 失败
```
Error:Could not resolve all files for configuration ':app:debugCompileClasspath'.
> Could not resolve com.tencent.ilivesdk:ilivesdk:1.8.3.
 Required by:
   project :app
 > Could not resolve com.tencent.ilivesdk:ilivesdk:1.8.3.
  > Could not get resource 'https://jcenter.bintray.com/com/tencent/ilivesdk/ilivesdk/1.8.3/ilivesdk-1.8.3.pom'.
   > Could not GET 'https://jcenter.bintray.com/com/tencent/ilivesdk/ilivesdk/1.8.3/ilivesdk-1.8.3.pom'.
    > Connect to jcenter.bintray.com:443 [jcenter.bintray.com/75.126.118.188] failed: Connection timed out: connect
```
先检测网络是否正常，并通过上面链接，确认可以访问 jcenter 网站，同时如果网络需要代理检测是否有在 gradle.properties 中配置。

- 登录未返回错误模块 IMSDK, 错误码 70009, 错误描述：tls_check_signature failed decrypt sig failed failed iRet:-2 sdkappid:14000xxxxx,acctype:xxxx,identifier:guest sig:E9vB6Ocs42J8A5lZW6s_

> 这种问题一般为登录的 userSig 与 id 不匹配引起，需要生成 userSig 的密钥与初始化时使用的 sdkAppId 是否对应
