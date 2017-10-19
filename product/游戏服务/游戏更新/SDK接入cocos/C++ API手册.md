## 1 更新回调接口
    请继承实现
    
    Namespace GCloud
    Class GCloudDolphinCallBack
    
    (1) virtual void OnDolphinVersionInfo(dolphinVersionInfo& newVersinInfo) = 0;
    回调时机：查询版本服务后返回
    参数：newVersinInfo 版本信息
    newVersinInfo. isAppUpdating是否是程序更新
    newVersinInfo.isNeedUpdating是否需要更新
    newVersinInfo.isForcedUpdating是否强制更新
    newVersinInfo.versionNumberOne新版本版本号第一位（左起）
    newVersinInfo.versionNumberTwo新版本版本号第二位（左起）
    newVersinInfo.versionNumberThree新版本版本号第三位（左起）
    newVersinInfo.versionNumberFour新版本版本号第四位（左起）
    newVersinInfo.needDownloadSize版本更新需要的下载大小
    newVersinInfo.versionDescrition新版本版本描述
    newVersinInfo.userDefineStr新版本用户自定义信息
    
    (2) virtual void OnDolphinProgress(dolphinUpdateStage curVersionStage, cu_uint64 totalSize, cu_uint64 nowSize) = 0;
    回调时机：进度，定期回调
    参数：curVersionStage当前更新状态
    dolphinUpdateStage.VS_GetVersionInfo(3)正在获取版本信息
    dolphinUpdateStage.VS_FirstExtract(10)首包解压
    dolphinUpdateStage.VS_ApkUpdate(70)apk更新
    dolphinUpdateStage.VS_ApkUpdateDownConfig(71)apk更新下载配置文件
    dolphinUpdateStage.VS_ApkUpdateDownDiffFile(72)apk更新下载差异文件
    dolphinUpdateStage.VS_ApkUpdateDownFullApk(73)apk更新下载全量文件
    dolphinUpdateStage.VS_ApkUpdateCheckCompletedApk(74) apk更新校验完成文件
    dolphinUpdateStage.VS_ApkUpdateCheckLocalApk(75)apk更新校验本地apk
    dolphinUpdateStage.VS_ApkUpdateCheckConfig(76)apk更新校验配置文件
    dolphinUpdateStage.VS_ApkUpdateCheckDiff(77)apk更新校验差异文件
    dolphinUpdateStage.VS_ApkUpdateMergeDiff(78)apk更新合并差异
    dolphinUpdateStage.VS_ApkUpdateCheckFull(79)apk更新校验全量文件
    dolphinUpdateStage.VS_SourceUpdateCures(90)资源更新
    dolphinUpdateStage.VS_SourceUpdateDownloadList(91)资源更新下载配置
    dolphinUpdateStage.VS_SourcePrepareUpdate(92)资源更新准备更新
    dolphinUpdateStage.VS_SourceAnalyseDiff(93)资源更新分析差异
    dolphinUpdateStage.VS_SourceDownload(94)资源更新下载资源
    dolphinUpdateStage.VS_SourceExtract(95)资源更新解压资源
    totalSize总进度
    nowSize当前进度
    (3) virtual void OnDolphinError(dolphinUpdateStage curVersionStage, cu_uint32 errorCode) = 0;
    回调时机：出错时
    参数：  
    curVersionStage 出错是状态，参照OnDolphinProgress
    errorCode 错误码，定位问题
    
    (4) virtual void OnDolphinSuccess() = 0;
    回调时机：更新流程执行成功
    
    (5) virtual void OnDolphinNoticeInstallApk(char* apkurl) = 0;
    回调时机：当需要apk更新时，更新成功，通知安装apk，游戏收到后退出更新模块拉起apk安装
    
    (6) virtual void OnDolphinFirstExtractSuccess() = 0;
    回调时机：当需要首包解压时，解压成功


## 2 更新对象接口


    Namespace GCloud
    
    (1) GCloudDolphinInterface* CreateDolphin();
    功能：创建更新对象
    
    (2) void ReleaseDolphin(GCloudDolphinInterface** dolphin);
    功能：删除更新对象

## 3 更新功能接口
    Namespace GCloud
    Class GCloudDolphinInterface
    
    (1)virtual bool Init(const dolphinInitInfo* initInfo, const dolphinPathInfo* pathInfo,const dolphinGrayInfo* grayInfo, 
    const dolphinFirstExtractInfo* feInfo,
    GCloudDolphinCallBack* callBack) = 0;
    功能：初始化更新对象
    参数：  
    initInfo 初始化信息
    initInfo. channelId;渠道号
    initInfo. updateType;更新类型
    initInfo. isGrayUpdate;是否是灰度更新
    initInfo. openDebugLog;是否打开debug日志
    initInfo. openErrorLog;是否打开error日志
    initInfo. updateUrl;更新地址
    initInfo. appVersion;当前程序版本
    initInfo. srcVersion当前资源版本
    pathInfo更新路径信息
    pathInfo.updatePath;更新路径，可写并存在
    pathInfo.dolphinPath;更新模块信息路径，可写并存在
    pathInfo.curApkPath当前apk的路径，apk更新使用
    grayInfo灰度信息
    grayInfo.userID;用户id
    char worldID用户登录区服id
    feInfo首包解压信息，传null，不需要首包解压
    feInfo. ifsPath首包解压资源包绝对路径
    返回：是否执行成功
    
    (2)virtual bool Uninit() = 0;
    功能：反初始化
    返回：是否执行成功
    
    (3)virtual void ContinueUpdate(bool bContinue) = 0;
    功能：继续更新，在回调OnDolphinVersionInfo之后，如果需要更新调用
    
    (4)virtual void CheckAppUpdate() = 0;
    功能：启动版本更新流程
    
    (5)virtual void CancelUpdate() = 0;
    功能：取消更新
    
    (6)virtual cu_uint32 GetLastError() = 0;
    功能：获取错误码，暂时未完善
    
    (7)virtual bool PollCallback() = 0;
    功能：驱动更新，定期调用，在此函数中执行回调
    返回：是否执行成功，失败退出更新