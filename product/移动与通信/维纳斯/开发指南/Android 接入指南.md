## Sdk 目录结构说明
WnsSDKDemo：示例工程，演示了如何使用 WnsSDK 
获取应用签名的 md5 工具：用来获取打了正式签名的正式包的 md5
Doc：
    WnsSDK 使用说明：本文档


## 系统环境要求和限制
适用于 Android 2.3.3 及以上的系统版本。
sdk 接口字符类型参数限制长度为 256 字节
sdk 发送数据限制长度为 512K 字节
sdk 接受数据限制长度为 512K 字节

## 名词解释
- **appid**： wns 为接入 App 分配的标识。
- **appVersion**：  App 版本号。
- **channelId**： App 渠道号，与 appVersion 一起在 wns 监控系统中提供统计信息，
来区分各种下载渠道，例如应用宝,百度手机助手。
- **uid**：业务用户的唯一标识。
- **wid**：wns 为每个终端分配的唯一标识。

## Sdk 配置和初始化说明
### 引入 Wns Sdk
将 /libs 下的 assets 和 libs 目录分别复制到工程根目录对应的目录中。


>!需要将 jar 文件和对应的 so 添加 到工程中。

这里的 armeabi 的 so 文件夹是必须添加，其它 so 文件夹可以按需添加，如果您的工程中有对应的 so 文件夹就必须加入相应文件夹的 so。例如工程 libs 目录下已经有 arm64-v8a 目录，则需要添加到 WNSsdk 中相关的  arm64-v8a 文件夹下的 64 位系统的相关 so，否则 64 位上的机器会崩溃。

### 配置 AndroidManifest.xml
wns_SDK  需要使用的系统权限如下图（可参考示例工程）：

加到根目录 manifest 下面。

```
<!-- demo中使用某些高级API简化编程，使用者需要根据自己情况设置sdk version -->
<uses-sdk
    android:minSdkVersion="10"
    android:targetSdkVersion="18" />

<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>

```

### 配置 WnsSdk 服务
注册 Service：

```
<!-- service -->

<!-- WNS service,注意进程名为  :wns ，其它组件请不要使用这个进程名 -->
<service
        android:name="com.tencent.wns.service.WnsMain"
        android:exported="false"
        android:process=":wns">
    <intent-filter>
        <action android:name="com.tencent.wns.service.WnsMain"/>
    </intent-filter>
</service>

<!-- 注册WNS心跳接收器 -->
<receiver
        android:name="com.tencent.base.os.clock.AlarmClockReceiver"
        android:exported="false"
        android:process=":wns">
    <intent-filter>
        <action android:name="wns.heartbeat"/>
    </intent-filter>
</receiver>

```
>!
- 进程名“:wns”为 wns 服务使用，请不要占用。
- 以上部分位于 application 分支下。


### 初始化 App 信息并启动服务
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
<application android:name=".MyBaseApplication" .... 
```

### 代码混淆
sdk 已经混淆，建议不要再次混淆。如果需要混淆，请务必在脚本中加入以下配置

```
-keep class com.tencent.wns.openssl.OpenSSLNative
{ private long pkey;
}
-keep class com.tencent.wns.network.ConnectionImpl  {*;
}
-keep class * implements com.qq.taf.jce.JceStruct {
}
-keep class com.tencent.wns.service.WnsMain

```
## SDK 数据收发接口
### Http 数据收发
#### 使用 HttpClient 请求

HttpClent 实例使用 WnsService.getWnsHttpClient()来获取，然后使用HttpClient.execute(HttpUriRequest httpUriRequest )来发起 http 请求

>!
- 发送和接受数据大小限制为512KB。
- 业务侧最好打印出 response.getFirstHeader  (WnsService.KEY_HTTP_RESULT)中的数据，以便于 bug 定位。

此模式下，sdk会自动将url设置为命令字，wns会统计每个命令字的成功率等信息，对应的，需要在控制台配置url域名对应的路由。

```
//[必须] 定义wns的引用，从而使用其内部方法
private final WnsService wns = WnsClientFactory.getThirdPartyWnsService(); 
//[注意] HTTP的收发包样例. 发送数据&接收数据大小限制为512KB
private void sendHttpReq() {
    Runnable run = new Runnable() {
        @Override
        public void run() {
          // [修改] 请求的url地址，完整地址。
          String url = "http://user.qzone.qq.com/xunren?a=b";    //控制台上需要配置user.qzone.qq.com对应的路由
          //[必须] 用wns的接口替换系统HttpClient
            HttpClient client = wns.getWnsHttpClient();      
            //[两个超时总和的请求，建议60秒         client.getParams().setParameter(CoreConnectionPNames.CONNECTION_TIMEOUT,30*1000);
            client.getParams().setParameter(CoreConnectionPNames.SO_TIMEOUT, 30*1000);
            HttpUriRequest request = new HttpGet(URI.create(url));
            try {
                //[必须] 同样的execute方法，发起http请求。
                HttpResponse response = client.execute(request);
                if (response.getStatusLine().getStatusCode() == HttpURLConnection.HTTP_OK)
                {
                    //[参考] 常见http回包解析方式，业务端可以保持自己代码不变
                    InputStream in = response.getEntity().getContent();
                    ByteArrayOutputStream out = new ByteArrayOutputStream();
                    byte[] buff = new byte[1024];
                    int len = -1;
                    while ((len = in.read(buff)) != -1) {
                        out.write(buff, 0, len);
                    }
                    in.close();

                     Log.d(“wns”,"http code " + response.getStatusLine().toString());
                     Log.d(“wns”,"http data " + out.toString().trim());
                }
                else
                {
                    Header header = response.getFirstHeader(WnsService.KEY_HTTP_RESULT);
                    String wnsCode = "";
                    if (header != null)
                    {
                        wnsCode = header.getValue();
                    }
                    Log.d(“wns”,"http code " + response.getStatusLine().toString() + ", wnscode " + wnsCode);
                }

            } catch (ClientProtocolException e) {
                e.printStackTrace();
                Log.e(TAG,"catch error:"+e.toString());
            } catch (IOException e) {
                e.printStackTrace();
                Log.e(TAG,"catch error:"+e.toString());
            }
        }
    };
    new Thread(run).start();
}
```

#### 使用 HttpUrlConnection 请求
使用 wns.getWnsHttpUrl()获取 URL 实例

发送和接受数据大小限制为 512KB。
此模式下，sdk 会自动将 url 设置为命令字，wns 会统计每个命令字的成功率等信息，对应的，需要在控制台配置 url 域名对应的路由。
```
 //[必须] 定义 wns 的引用，从而使用其内部方法
private final WnsService wns = WnsClientFactory.getThirdPartyWnsService(); 
//[注意] HTTP的收发包样例. 发送数据&接收数据大小限制为 512KB
private void sendHttpUrlConnReq(final String url)
{
    Runnable run = new Runnable()
    {
        @Override
        public void run()
        {
            try
            {
                 //1.构造 URL，底层网络走 wns 通道,使用起来和 URL 是一样的。
                URL u = wns.getWnsHttpUrl(url);                   //需要在控制台上配置 url 对应域名的路由
                HttpURLConnection conn = (HttpURLConnection) u.openConnection();
                conn.addRequestProperty("User-Agent", "");

                //[两个超时总和的请求，建议60秒  
                conn.setConnectTimeout(30*1000);
                conn.setReadTimeout(30*1000);

                //如果是post方法，需要设置一下post参数,可选
                //conn.setDoOutput(true);
                //conn.getOutputStream().write("a=10&b=99".getBytes());
                //获取页面内容
                int rspcode = conn.getResponseCode();
                Log.d(TAG, "rspcode = " + rspcode);
                if (HttpURLConnection.HTTP_OK == rspcode)
                {
                    InputStream in = conn.getInputStream();
                    if (in == null)
                    {
                          return;
                    }
                    byte[] buff = new byte[1024];
                    ByteArrayOutputStream out = new ByteArrayOutputStream();
                    int len = -1;
                    while ((len = in.read(buff)) != -1)
                    {
                        out.write(buff, 0, len);
                    }
                    in.close();
                    final String content = out.toString().trim();
                    Log.w(TAG, content.substring(0, 100 > content.length() ? content.length() : 100));
                    Log.w(TAG, content.substring(content.length() > 100 ? content.length() - 100 : content.length()));

                } 
            } catch (MalformedURLException e)
            {
                e.printStackTrace();
            } catch (IOException e)
            {
                e.printStackTrace();
            }
        }
    };
    new Thread(run).start();
}```

### 调用接口 sendRequest 来收发二进制数据。
发送二进制数据的接口和发送 http 的比较类似，开发商终端需要修改原来的代码，将收发接口替换为 Wns 的 Sdk
1. 发送和接受数据大小限制为 512KB。
2. 命令字禁止使用“wnscloud”作为前缀。


>!cmd 必须是细化到接口，wns 会统计每个 cmd 的成功率等信息，对应的，需要在控制台配置模块 wnsdemo 对应的路由。

```
 private final WnsService wns = WnsClientFactory.getThirdPartyWnsService(); //[必须] 定义wns的引用，从而使其内部方法


//[注意] 二进制的收发包样例. 发送数据&接收数据大小限制为512KB
private int sendReq()
{
    final String cmd = "wnsdemo/transfer";   //需要在控制台配置wnsdemo对应的路由
    final int timeout = 60 * 1000;
    final byte[] buff = "this is buff".getBytes();
    showLoading();
    int seqNo = wns.sendRequest(cmd, timeout, buff, new WnsTransferCallback()
    {

        @Override
        public void onTransferFinished(IWnsTransferResult re)
        {
           int mainErrCode=re.getWnsCode();
           int subErrCode=re.getWnsSubCode();
           int bizErrCode=re.getBizCode();
           String errMsg=re.getErrMsg();
           //mainErrCode,bizErrCode可用于提示用户，提示语需要业务自定义，subErrCode需要查问题时向wns提供
            Log.d("wns","send request result " + re + ", msg :" + errMsg);
            stopLoading();
        }

    });
    Log.d("wns","send request seqNo=" + seqNo);

    return seqNo;
}```

## PUSH 接入

### 在 AndroidManifest.xml 中注册接收 push 的 service
 <!-- 注册 WNS push 接收器 -->

<service    
        android:name="com.example.cloudwns.push.MyPushService" android:exported="false">

        <intent-filter>

              <!-- 注意 action 需要修改为    wns.push.to.<package name> -->
                <action android:name="wns.push.to.com.example.cloudwns" /> 
         </intent-filter>

</service>
其中 com.example.cloudwns.push.MyPushService （类名可修改）是应用自定义的 push 处 理 类 型 ， 继 承 自 WNS SDK 提 供 的 抽 象 类 com.tencent.wns.ipc.AbstractPushService。

### 自定义处理 Push 的Service
假设类名是 com.example.cloudwns.push.MyPushService（应用可自定义名称），应用只需要实现 onPushReceived 这个方法即可。如下：
```
 package com.example.cloudwns.push;


import android.util.Log;

import com.tencent.wns.client.data.PushData; import com.tencent.wns.ipc.AbstractPushService;


public class MyPushService extends AbstractPushService{

      public static final String TAG = "MyPushService";
      /**

      *子类实现的接受消息推送的方法<br>

       *<br>

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

在接入 Wns 的过程中， 当遇上某些问题需要和 Wns 侧一起定位问题时， 可以通过以下接口设置客户端连接到Wns的测试环境，Wns 的测试环境也可以连接到开发商的测试服务器环境中，这样便于快速的定位到具体的问题。
要使用测试环境，开发商必须按下面来要求来设置
1. 终端调用 Wns Sdk 接口：setDebugIP，确保连接到 Wns 测试环境。
2. 开发商必须在 Wns 控制台配置好，开发商测试环境服务器路由信息。

另外，如果出现 Wns 连接或者收发出错的问题时，可以通过 Sdk 接口 keyLog 拿到提示信息并打印出来，提供给相关工作人员查看，以方便查找问题。


## Wns 快速验证模式

Wns 提供快速验证模式，开发商可以先集成 Wns 的 Sdk，但是通信接口暂时不切换到 Wns 通道，该模式下，Wns Sdk 会自动发一些探测包到 Wns       的接入服务器（探测包不会转发到开发商服务器）。这样开发商可以在控制台上看到探测包的统计数据。可以准确的评估出实际接入 Wns 后的服务质量。如果效果明显，开发商再后续版本才正式将服务切换到 Wns 通道。

使用 Wns 快速验证模式，开发商只需要下面的几个步骤：
1. Wns 控制台注册 App 和签名信息。
2. 终端集成 Wns Sdk。
3. 终端在初始化阶段调用 Sdk 接口 initWithAppID。

## 常见问题
 
通过 System.loadLibrary 方法加载 so 都会去 libs 目录找相CPU  架构的 so，一些低端机型无法加载到 so 导致 WNS 启动失败。
因此 WNS 会在 assets 目录下也放了一份 so，当 loadLibraray 方法加载失败会尝试将 assets 目录下的 so 复制到 App 运行目录中，通过 System.load 
方法加载 so，提高启动 WNS 的成功率。

我们提供的 sdk  zip 包中包含获取应用签名的 App 工具，安装到手机后，输入您的 App 包名即可获取到签名。

