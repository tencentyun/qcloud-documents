
This document describes how to integrate iLiveSDK to your client using the repository and how to log in to Tencent Cloud.
## Downloading Source Code
You can download the complete demo code used in this document.
[Download Demo Code](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/Android/demo_login.zip)

## Prerequisites
You must have activated the service and created an application at the [TRTC official website](https://cloud.tencent.com/product/trtc).

## Concepts
 - [TRTC application](https://cloud.tencent.com/document/product/647/16792#.E5.AE.9E.E6.97.B6.E9.9F.B3.E8.A7.86.E9.A2.91.E5.BA.94.E7.94.A8)
 - [Application ID( sdkAppId )](https://cloud.tencent.com/document/product/647/16792#.E5.BA.94.E7.94.A8.E6.A0.87.E8.AF.86.EF.BC.88-sdkappid-.EF.BC.89)
 - [Account type( accountType )](https://cloud.tencent.com/document/product/647/16792#.E5.B8.90.E5.8F.B7.E7.B1.BB.E5.9E.8B.EF.BC.88-accounttype-.EF.BC.89)
 - [User ID( userId )](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E6.A0.87.E8.AF.86.EF.BC.88-userId-.EF.BC.89)
 - [User signature( userSig )](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E7.AD.BE.E5.90.8D.EF.BC.88-usersig-.EF.BC.89)

## Obtaining userSig
Each user at Client is provided with a userSig. It is valid for three months upon generation. If the userSig expires, the user cannot log in to TRTC and will receive the error code 8051. At this time, the user should generate a new userSig to log in to TRTC.

```java
    /** Ticket expired (Need to update ticket userSig) */
    public static final int ERR_EXPIRE              = 8051;
```

> Note: For more information on how to obtain a userSig, see [User Authentication](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E7.AD.BE.E5.90.8D.EF.BC.88-usersig-.EF.BC.89).. During debugging, you can directly use the development tools in the console to generate a userSig.

## Adding a Dependency (Integrating SDK)
Modify the build.gradle file and add the dependency of iLiveSDK in "dependencies":
```
compile 'com.tencent.ilivesdk:ilivesdk:latest.release'  //latest.release refers to the latest iLiveSDK version number
```

## Initializing iLiveSDK
Add DemoApp.java and inherit Application:
```Java
public class DemoApp extends Application {
    @Override
    public void onCreate() {
        super.onCreate();

        //Check whether initialization is only performed in the main thread
        if (MsfSdkUtils.isMainProcess(this)) {
            //Initialize iLiveSDK
            ILiveSDK.getInstance().initSdk(this, Constants.SDKAPPID, Constants.ACCOUNTTYPE);
            //Initialize iLiveSDK room management module
            ILiveRoomManager.getInstance().init(new ILiveRoomConfig());
        }
    }
}
```
In the application of AndroidManifest.xml, declare:
```
<application
        ......
        android:name=".DemoApp">
        ......
    </application>
```

## Creating the Login Module
Create a communication API for the login module and Activity:
```Java
public interface ILoginView {
    //Login successful
    void onLoginSDKSuccess();
    //Login failed
    void onLoginSDKFailed(String module, int errCode, String errMsg);
}
```
At the same time, create a LoginHelper.java for login:
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
## Listening for Account Status
The Listening feature of the application is used to listen for forced logout due to repeated login or expired userSig.
You can create an observer to listen globally:
```Java
/**
 * Status observer
 */
public class StatusObservable implements ILiveLoginManager.TILVBStatusListener {

    //Message listening linked list
    private LinkedList<ILiveLoginManager.TILVBStatusListener> listObservers = new LinkedList<>();
    //Handle
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


    //Add an observer
    public void addObserver(ILiveLoginManager.TILVBStatusListener listener){
        if (!listObservers.contains(listener)){
            listObservers.add(listener);
        }
    }

    //Remove an observer
    public void deleteObserver(ILiveLoginManager.TILVBStatusListener listener){
        listObservers.remove(listener);
    }

    //Obtain the number of observers
    public int getObserverCount(){
        return listObservers.size();
    }

    @Override
    public void onForceOffline(int error, String message) {
        //Copy the linked list
        LinkedList<ILiveLoginManager.TILVBStatusListener> tmpList = new LinkedList<>(listObservers);
        for (ILiveLoginManager.TILVBStatusListener listener : tmpList){
            listener.onForceOffline(error, message);
        }
    }
}
```
After successful login, call the API to set listening:
```Java
ILiveLoginManager.getInstance().setUserStatusListener(StatusObservable.getInstance());
```
In this way, you will know you are forced logout after receiving the OnForceOffline event.

## UI Development
A separate login page is required to enter the user name and password at the client. Such basic knowledge of Android development will not be discussed here.

Log in to the onCreated event in the application, and then you can create the module defined above:
```Java
loginHelper = new LoginHelper(this);
```
Click the login event to obtain the userId and userSig entered by the user. Call the login API of loginHelper to log in:
```Java
loginHelper.loginSDK(userId, userSig);
```

## FAQ
- Failed to download aar
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
Check the network first. Then, check whether the jcenter website is accessible by clicking on the above link. If a proxy is required, check if it is configured in gradle.properties.

- Log in to IMSDK, a module that does not return any error. Error code: 70009. Error description: tls_check_signature failed decrypt sig failed failed iRet:-2 sdkappid:14000xxxxx,acctype:xxxx,identifier:guest sig:E9vB6Ocs42J8A5lZW6s_

> This may be caused by mismatch between the userSig and ID. Check whether the key for generating the userSig matches the sdkAppId used in initialization.


## Email
If you have any questions, send us an email to trtcfb@qq.com.

