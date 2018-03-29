## Sdk目录结构说明
WnsSDKDemo:示例工程,演示了如何使用WnsSDK
获取应用签名的md5工具:用来获取打了正式签名的正式包的md5
Doc:
    WnsSDK使用说明:本文档


## 系统环境要求和限制
适用于Android 2.3.3及以上的系统版本。
sdk接口字符类型参数限制长度为256字节
sdk发送数据限制长度为512K字节
sdk接受数据限制长度为512K字节

## 名词解释
appid:  wns 为接入 app 分配的标识。
appVersion:   app 版本号。
channelId: app 渠道号，与 appVersion 一起在 wns 监控系统中提供统计信息，
来区分各种下载渠道，比如应用宝,百度手机助手。
uid:业务用户的唯一标识。
wid:wns为每个终端分配的唯一标识

## Sdk配置和初始化说明
### 引入Wns Sdk
将/libs 下的 assets 和 libs 目录分别复制到工程根目录对应的目录中，如下图
![](https://mccdn.qcloud.com/static/img/dca5498f8a97efd6050f0ac4e3610ab9/wns_and_lib.png)
**注意：需要将 jar 文件和对应的so 添加 到工程中。
这里的armeabi的so文件夹是必须添加，其它so文件夹可以按需添加，如果你的工程中有对应的so文件夹就必须加入相应文件夹的so。例如工程libs目录下已经有arm64-v8a目录，则需要添加到WNSsdk中相关的 arm64-v8a文件夹下的64位系统的相关so，否则64位上的机器会崩溃。**

### 配置 AndroidManifest.xml
wns_SDK  需要使用的系统权限如下图（可参考示例工程）：
注意：加到根目录 manifest 下面。
```












```

### 配置 WnsSdk服务
注册 Service：

```




    
        
    




    
        
    


```
注意:
  (1)  进程名“:wns”为 wns 服务使用，请不要占用
  (2)  以上部分位于 application 分支下。

### 初始化 APP 信息并启动服务
修改 MyBaseApplication，onCreate（）变为如下内容：

```
public class MyBaseApplication extends Application
{
    private final static String TAG = "BaseApplication";

    private WnsService wns = WnsClientFactory.getThirdPartyWnsService();;

    @Override
    public void onCreate()
    {
        super.onCreate();

        WnsAppInfo info = new WnsAppInfo()
             //[修改] 云平台上申请获取的APPID
              .setAppId(1000244)  
               //[修改] App的版本信息 - 建议填写，方便以后提供详细细分统计（这里的“1.0.0”代表版本                                 号，业务可以按照自己规则填写）
              .setAppVersion("1.0.0") 
              //[修改] APP的渠道信息 - 建议填写，方便以后提供详细细分统计。（这里的“yyb”代表应用宝，业务可以按照自己规则填写）
                .setChannelId("yyb"); 
         wns.initAndStartWns(this, info);
     }
}

```

同时在 AndroidManifes.xml 中配置实现：

```


        

              
                 
		 


```

其中 com.example.cloudwns.push.MyPushService （类名可修改）是应用自定义的push	处	理	类	型	，	继	承	自	WNS	SDK	提	供	的	抽	象	类com.tencent.wns.ipc.AbstractPushService。

### 自定义处理 Push 的Service

假设类名是 com.example.cloudwns.push.MyPushService（应用可自定义名称），应用只需要实现 onPushReceived 这个方法即可。如下：

```
package com.example.cloudwns.push;


import android.util.Log;

import com.tencent.wns.client.data.PushData; import com.tencent.wns.ipc.AbstractPushService;


public class MyPushService extends AbstractPushService{

      public static final String TAG = "MyPushService";
      /**

      *子类实现的接受消息推送的方法


       *


      *这将在主线程执行，若要处理耗时操作，请异步。

      *

      *@param pushes 消息内容

      *@return 是否消费。暂时返回 true，保留字段。

      */

     @Override

      public boolean onPushReceived(PushData[] pushes)
      {
           long begin = System.currentTimeMillis(); for (PushData pushData : pushes)
      {
          Log.i(TAG,"push data = " + pushData);
      }

       long end = System.currentTimeMillis();

       Log.i(TAG, "onPushReceived timecost = " + (end - begin)); return true;

     }

}
```


## 调试类接口
在接入Wns的过程中, 当遇上某些问题需要和Wns侧一起定位问题时, 可以通过以下接口设置客户端连接到Wns的测试环境，Wns的测试环境也可以连接到开发商的测试服务器环境中，这样便于快速的定位到具体的问题。
要使用测试环境，开发商必须按下面来要求来设置
1、终端调用Wns Sdk接口：setDebugIP，确保连接到Wns测试环境。
2、开发商必须在Wns控制台配置好，开发商测试环境服务器路由信息。

另外, 如果出现Wns连接或者收发出错的问题时, 可以通过Sdk接口keyLog拿到提示信息并打印出来, 提供给相关工作人员查看, 以方便查找问题。

## Wns快速验证模式
Wns提供快速验证模式，开发商可以先集成Wns的Sdk，但是通信接口暂时不切换到Wns通道，该模式下，Wns Sdk会自动发一些探测包到Wns的接入服务器（探测包不会转发到开发商服务器）。这样开发商可以在控制台上看到探测包的统计数据。可以准确的评估出实际接入Wns后的服务质量。如果效果明显，开发商再后续版本才正式将服务切换到Wns通道。

使用Wns快速验证模式，开发商只需要下面的几个步骤
1、Wns控制台注册App和签名信息
2、终端集成Wns Sdk
3、终端在初始化阶段调用Sdk接口initWithAppID


## 常见问题

i）问：为什么 WNS SDK 中有些 so 放在 assets 目录下，有些 so 放在 libs 目录下？
答：通过 System.loadLibrary 方法加载 so 都会去 libs 目录找相应 cpu 架构的 so，根据以 往经验，一些低端机型无法加载到 so 导致 WNS 启动失败。
因此 WNS 会在 assets 目录 下也放了一份 so，当 loadLibraray 方法加载失败会尝试将 assets 目录下的 so 复制到 app 运行目录中，通过 System.load 
方法加载 so，提高启动 WNS 的成功率。

i）问：怎么样获取应用的签名
答：我们提供的 sdk  zip 包中包含获取应用签名的 app 工具，安装到手机后，输入您的app 包名即可获取到签名
![](https://mccdn.qcloud.com/static/img/bde9d37a48d969ead313cbbe6f2b1e9a/wns_and_tool.png)

