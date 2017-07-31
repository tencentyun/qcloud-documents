## 1 更新回调接口
    用户需继承实现
    
    Namespace：GCloud.Dolphin
    Interface：DolphinCallBackInterface
    
    (1) void OnNoticeNewVersionInfo(NewVersionInfo newVersionInfo);
    回调时机：查询版本服务后返回
    参数：NewVersionInfo newVersionInfo
    newVersionInfo. versionStr最新版本号
    newVersionInfo. needDownloadSize更新需要下载的大小
    newVersionInfo. isForce是否强制更新
    newVersionInfo. updateType更新类型（资源、程序）
    newVersionInfo. userDefineStr用户自定义信息，json格式，对应改版本下用户配置的版本描述和
    
    自定义字符串
    newVersionInfo. isCurrentNewest当前版本是否是最新的，如果是最新的表示不需要更新，否则看isForce，判断是强
    
    制还是可选
    
    (2) void OnUpdateProgressInfo(string msg, System.UInt32 nowSize, System.UInt32 totalSize, bool isDownloading);
    回调时机：进度定期回调
    参数：msg提示信息
    Nowsize当前进度
    Totalsize总进度
    isDownloading 当前是否是下载，如果是size的单位是B；不是size仅仅为数值，没有单位
    
    (3) void OnUpdateMessageBoxInfo(string msg, MessageBoxType msgBoxType, bool isError, System.UInt32 errorCode);
    回调时机：更新服务需要提示用户的时候，如果内部错误
    参数：msg提示信息
    msgBoxType提示框类型
    isError是否是错误提示
    errorCode错误码，定位问题使用
    
    (4) void OnNoticeInstallApk(string apkPath);
    回调时机：当需要更新apk的时候，apk下载完成通知，可等价于更新成功，用户收到此回调后退出更新模块安装游戏
    参数：apkPathapk所在路径
    
    (5) void OnNoticeUpdateSuccess();
    回调时机：更新成功
    
    (6) void OnNoticeChangeSourceVersion(string newVersionStr);
    回调时机：资源更新成功，通知修改当前资源版本号
    参数：newVersionStr更新完成新的资源版本号
    
    (7) void OnNoticeFirstExtractSuccess();
    回调时机：初始化需要首包解压，首包解压完成时


## 2 更新数据接口

    用户需继承实现
    
    Namespace：GCloud.Dolphin
    Interface：DolphinCallBackInterface
    
    (1) string GetUpdateTempPath();
    返回一个存在并可写目录，当资源被清空的时候，需要清空此目录，此目录中有一个flist文件记录本地的资源列表
    
    (2) string GetUpdateSourceSavePath();
    返回一个存在并可写的目录，资源读取目录，游戏更新的资源全在此目录，资源更新依赖此目录更新
    
    (3) string GetUserDateString();
    返回用户自定义信息，可返回用户的机器信息等
    
    (4) string GetCurrentSourceVersion();
    返回当前的资源版本号
    
    (5) string GetCurrentProgramVersion();
    返回当前的程序版本号
    
    (6) string GetUpdateApolloPath();
    返回一个存在并可写的目录，不要删除修改此目录中的内容


## 3 更新模块创建接口

    Namespace：GCloud.Dolphin
    Interface：DolphinFactory
    
    CreateDolphinMgr(DolphinCallBackInterface callBackImp, DolphinDateInterface dateMgr)
    功能：创建更新对象，更新对象不能重复使用
    参数：callBackImp 更新回调对象
    dateMgr更新数据对象
    返回：更新对象

## 4 更新功能接口

    Namespace：GCloud.Dolphin
    Interface：DolphinFactory
    
    (1) bool InitUpdateMgr(UpdateInitInfo updateInfo, bool needFirstExtract);
    功能：初始化更新对象
    参数：updateInfo初始化参数
    needFirstExtract是否需要首包解压
    返回：执行是否成功
    
    (2) bool UninitUpdateMgr();
    功能：反初始化更新对象
    返回：是否执行成功
    
    (3) bool StartUpdateService();
    功能：启动更新流程
    返回：是否执行成功
    
    (4) bool Continue();
    功能：继续更新流程，在回调了OnNoticeNewVersionInfo和OnUpdateMessageBoxInfo之后，调用继续更新或重试更新
    返回：是否执行成功
    
    (5) bool StopUpdateService();
    功能：停止更新流程
    返回：是否执行成功
    
    (6) void DriveUpdateService();
    功能：驱动更新，定期调用，此函数中执行回调
    
    (7) System.UInt32 GetCurrentDownSpeed();
    功能：获取当前的下载速度
    
    (8) void SetNeedFirstExtract(bool needFirstExtract);
    功能：设置是否需要首包解压