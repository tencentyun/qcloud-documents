## Overview
Welcome to Tencent Cloud Game Multimedia Engine (GME) SDK. To help Unreal Engine developers debug and connect to Tencent GME API, here we introduce the project configuration suitable for Unreal Engine development.

## Preparation for SDK
Contact us to obtain SDK.
Open the Plugins folder under the Unreal Engine project directory (create one if no directory exists), and copy SDK to the folder. The SDK directory is shown as follows:
![](https://main.qcloudimg.com/raw/751894ab16c5262b7a99370cc7efd52c.png)
Compile the imported plug-in in the Unreal Engine.
![](https://main.qcloudimg.com/raw/d7c23f8c850c814f1758eabc7f8ba686.png)
After the compiling is completed, a directory can be found in VS2015 as follows.
![](https://main.qcloudimg.com/raw/3005bc887e0179bdc45719b07a61f778.png)
Open the Unreal Engine again, click the edit button and then the Plugins button, and you can see the GME plug-in.
![](https://main.qcloudimg.com/raw/b14824ae09efbf014af246866b79dc48.png)
## Preparation in Android

### Initialization
Initialize the SDK in the onLogin function of AUEDemoLevelScriptActor.
**Instance code**
```
//AUEDemoLevelScriptActor.cpp
void AUEDemoLevelScriptActor::onLogin()
{
    TryInitEnv();
}

static void TryInitEnv()
{
#if PLATFORM_ANDROID
    JNIEnv* JEnv = AndroidJavaEnv::GetJavaEnv();
    if (nullptr != JEnv)
    {
        jclass Class = AndroidJavaEnv::FindJavaClass("com/epicgames/ue4/GameActivity");
        if (nullptr != Class)
        {
            jmethodID getAppPackageNameMethodId = JEnv->GetStaticMethodID(Class, "OnInitGMEJnv", "()Ljava/lang/String;");
            jstring JPackageName = (jstring)JEnv->CallStaticObjectMethod(Class, getAppPackageNameMethodId, nullptr);
            const char * NativePackageNameString = JEnv->GetStringUTFChars(JPackageName, 0);
            FString PackageName = FString(NativePackageNameString);
            JEnv->ReleaseStringUTFChars(JPackageName, NativePackageNameString);
            JEnv->DeleteLocalRef(JPackageName);
            JEnv->DeleteLocalRef(Class);
        }
    }
#endif
}
```
