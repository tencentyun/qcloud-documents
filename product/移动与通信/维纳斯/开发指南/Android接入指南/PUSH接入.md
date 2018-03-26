
#### 在 AndroidManifest.xml 中注册接收 push 的 service
 <!-- 注册 WNS push 接收器 -->

<service    
        android:name="com.example.cloudwns.push.MyPushService" android:exported="false">

        <intent-filter>

              <!-- 注意 action 需要修改为    wns.push.to.<package name> -->
                <action android:name="wns.push.to.com.example.cloudwns" /> 
         </intent-filter>

</service>
其中 com.example.cloudwns.push.MyPushService （类名可修改）是应用自定义的 push 处 理 类 型 ， 继 承 自 WNS SDK 提 供 的 抽 象 类 com.tencent.wns.ipc.AbstractPushService。

#### 自定义处理 Push 的Service
假设类名是 com.example.cloudwns.push.MyPushService（应用可自定义名称），应用只需要实现 onPushReceived 这个方法即可。如下：

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