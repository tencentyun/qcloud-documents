## Windows 端 LiteAV 和 iLive 兼容方案

### 工程结构及初始化方法
由于 LiteAV 和 iLive 都用到了 TRAE 库，但是使用的版本在功能上有差异，因此不能直接互相替换。所以工程上建议采用如下结构：

	|- 主程序.exe
	|- 主程序.exe 依赖的其他文件
	|- iLiveSDK.dll
	|- iLiveSDK.dll 依赖的其他文件
	|- LiteAV
	|   |- liteav.dll
	|   |- liteav.dll 依赖的其他文件

使用时，iLiveSDK 可以直接用 .lib 链接，也可以使用如下代码动态加载：
```cpp
HMODULE hiLive = LoadLibrary("iLiveSDK.dll");
```

当需要使用 LiteAV 时，使用如下代码加载并初始化：
```cpp
typedef ITRTCCloud* (*getTRTCShareInstanceMtd)();
typedef void(*destroyTRTCShareInstanceMtd)();

TCHAR dllPath[MAX_PATH];
GetModuleFileName(nullptr, dllPath, MAX_PATH);
PathRemoveFileSpec(dllPath);
wcscat(dllPath, L"\\LiteAV\\");
SetDllDirectory(dllPath);
HMODULE hLiteAV = LoadLibrary(L"liteav.dll");
if (!hLiteAV) {
    printf("载入liteav.dll失败: %d", GetLastError());
    return;
}

getTRTCShareInstanceMtd pGetTRTCShareInstance = (getTRTCShareInstanceMtd)GetProcAddress(hLiteAV, "getTRTCShareInstance");
if (!pGetTRTCShareInstance) {
    printf("载入函数getTRTCShareInstance失败");
    return;
}

destroyTRTCShareInstanceMtd pDestroyTRTCShareInstance = (destroyTRTCShareInstanceMtd)GetProcAddress(hLiteAV, "destroyTRTCShareInstance");
if (!pDestroyTRTCShareInstance) {
    printf("载入函数destroyTRTCShareInstance失败");
    return;
}

ITRTCCloud *pTrtcCloud = m_pGetTRTCShareInstance();
if (!pTrtcCloud) {
    printf("创建TRTC实例失败");
    return;
}
SetDllDirectory(nullptr);

pTrtcCloud->enterRoom(...);
```


## Android 端 LiteAV 和 iLive 兼容方案

iLiveSDK 和 LiteAV 都是用了 TRAE 库，LiteAV 中使用的 TRAE 版本较新，包含 iLiveSDK 中使用的 TRAE，只选用 LiteAV 中的 TRAE 库。

aar 方式集成工程配置如下：
>?在 app 目录下的 build.gradle， android{} 节点中进行配置。
>
```java
android{
    //1、在 gradle 配置 packagingoptions
    packagingOptions {
        pickFirst 'lib/armeabi-v7a/libTRAECodec.so'
        pickFirst 'lib/armeabi-v7a/libstlport_shared.so'
        pickFirst 'lib/armeabi/libTRAECodec.so'
        pickFirst 'lib/armeabi/libstlport_shared.so'
    }
    //2、引入 dempendencies
    implementation(name:'LiteAVSDK_TRTC_6.4.7108', ext:'aar')  // 注意，TRTC 要在 ilivesdk 前面
    implementation 'com.tencent.ilivesdk:ilivesdk:1.9.4.6.4'
}
```

## iOS 端 LiteAVSDK + iLiveSDK + BeautySDK 兼容方案
LiteAVSDK 内已集成 BeautySDK，无需再次集成。如果同时集成的 iLiveSDK 需要用到 BeautySDK，则在工程中引入 BeautySDK，仅需在 xCode 工程配置 BeautySDK 的头文件搜索路径，并取消链接 BeautySDK。
>! 若 BeautySDK 用的是带 P 图版本，LiteAVSDK 要使用商用企业版。




