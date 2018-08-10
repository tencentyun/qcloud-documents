# Andorid
edit by xuanlong

概述
业务通过通过简单的配置与接口调用，即可使用PCDN SDK在直播、点播、文件下载等场景获取加速服务。

系统版本要求：

## SDK集成步骤
1. 工程导入PcdnSdk开发包
2. 配置PcdnSdk需要的权限
   在AndroidManifest.xml文件中增加以下三个权限
     INTERNET & WRITE_EXTERNAL_STORAGE & READ_EXTERNAL_STORAGE
3. 配置PcdnSdk的service
     <service android:name="com.teg.pcdnsdk.PcdnSdkService"
            android:process=":PcdnSdkService"/>

4. 初始化PcdnSdk服务
   在程序启动的时候初始化PcdnSdk服务（如OnCreate函数中），以便后续更快的使用PcdnSdk服务
   接口
      void PcdnSdk.init(Context cxt, Long appId, int srvType, String token)
   参数说明
      cxt： Application 的Context对象
      appId： 业务的appId, 在申请PCDN服务的时候分配
      srvType：需要加速的服务类型，PcdnSdkSrvType.PSST_DOWNLOAD 下载服务 PcdnSdkSrvType.PSST_VOD 点播服务 PcdnSdkSrvType.PSST_LIVE 直播服务
      token：申请PCDN服务分配的token
   返回值
      无

5. 转换url
   通过PcdnSdk.convertUrl接口把普通的url转换成加速后的url。然后使用加速后的url进行下载或者播放即可
   接口
      String PcdnSdk.convertUrl(String url)
   参数说明
      url: 需要加速的url
   返回值
      在PcdnSdk正常情况下，返回加速之后的url。否则返回原url。

6. 反初始化PcdnSdk服务
   在程序退出的时候，退出PcdnSdk服务
   接口
      void PcdnSdk.uninit(int srvType)
   参数说明
      srvType：需要加速的服务类型
   返回值
      无

7. 配置相关的接口
   获取配置信息 String PcdnSdk.getConfig:(int srvType, String key, String defaultVal);
   设置配置信息 void PcdnSdk.setConfig(int srvType, String key, String val);

