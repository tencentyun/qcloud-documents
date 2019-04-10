# iOS

概述
业务通过通过简单的配置与接口调用，即可使用PCDN SDK在直播、点播场景获取加速服务。

系统版本要求：

## SDK集成步骤
1. 将PcdnSdk.framework导入工程
2. 在代码中导入#import "PcdnSdk/PcdnSdk.h”
3. 创建PcdnSdk对象实例，PcdnSdk是为单例模式，通过sharedInstance创建实例
4. 初始化PcdnSdk服务
   在程序启动的时候初始化PcdnSdk服务，以便后续更快的使用PcdnSdk服务
   接口
   (int)initSdk:(long)appId srvType:(int)srvType token:(NSString*)token tmpPath:(NSString*)tmpPath;
   参数说明
      appId： 业务的appId, 在申请PCDN服务的时候分配
      srvType：需要加速的服务类型，PcdnSdkSrvType.PSST_DOWNLOAD 下载服务 PcdnSdkSrvType.PSST_VOD 点播服务 PcdnSdkSrvType.PSST_LIVE 直播服务
      token：申请PCDN服务分配的token
      tmpPath: 用于缓存的目录(绝对路径)
   返回值
      0表示成功，其它值则失败

5. 转换url
   通过convertUrl接口把普通的url转换成加速后的url。然后使用加速后的url进行下载或者播放即可
   接口
      (NSString*)convertUrl:(NSString*)url;
   参数说明
      url: 需要加速的url
   返回值
      在PcdnSdk正常情况下，返回加速之后的url。否则返回原url。

6. 反初始化PcdnSdk服务
   在程序退出的时候，退出PcdnSdk服务
   接口
      (void)uninitSdk:(int)srvType
   参数说明
      srvType：需要加速的服务类型
   返回值
      无

7. 配置相关的接口
   获取配置信息 (NSString*)getConfig:(int)srvType key:(NSString*)key, defaultVal:(NSString*)defaultVal;
   设置配置信息 (void)setConfig:(int)srvType key:(NSString*)key, val:(NSString*)val;
