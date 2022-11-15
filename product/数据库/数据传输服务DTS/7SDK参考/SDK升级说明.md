腾讯云数据订阅目前正在推动 API 2.0 接口下线。数据订阅 SDK 2.8.0 及以下版本，在鉴权时使用的是 API 2.0 接口，因此 API 2.0 接口下线后，SDK 2.8.0 及以下的版本使用将受到影响。

请及时按照如下方法升级您通过 SDK 进行消费的程序，避免受到 API 2.0 接口下线影响。

## 步骤1：确认 SDK 版本
确认您之前在 [数据订阅 SDK](https://cloud.tencent.com/document/product/571/8776) 文档下载并已使用的 SDK 版本。
SDK 版本判断方法如下：
 - 查看使用的 SDK 压缩包名：包名类似于`binlogsdk-2.8.0-jar-with-dependencies.jar`，其中包含了版本号信息。
 - 查看 SDK_VERSION 版本号：若 SDK 包已被重命名，请使用解压命令`unzip` 将 SDK 包解压，再查看其中的`tencentSubscribe.properties`文件，`SDK_VERSION`标识了 SDK 版本号。

若数据订阅 SDK 版本为2.8.0及以下，请执行 [步骤2](#Step2)。

## [步骤2：升级 SDK 版本](id:Step2)
1. 在 [数据订阅 SDK](https://cloud.tencent.com/document/product/571/8776#.E6.95.B0.E6.8D.AE.E8.AE.A2.E9.98.85-sdk-.E4.B8.8B.E8.BD.BD) 下载最新的 SDK 版本，并替换2.8.0及以下版本的数据订阅 SDK。
2. 替换数据订阅 SDK 版本后，参考如下代码中“程序改动点”， 增加设置订阅 channel 所属 region 的一行代码即可。

```java
package com.qcloud.biz;
import com.qcloud.dts.context.NetworkEnv;
import com.qcloud.dts.context.SubscribeContext;
import com.qcloud.dts.message.ClusterMessage;
import com.qcloud.dts.message.DataMessage;
import com.qcloud.dts.subscribe.ClusterListener;
import com.qcloud.dts.subscribe.DefaultSubscribeClient;
import com.qcloud.dts.subscribe.SubscribeClient;
import java.util.List;
public class Main {
    public static void main(String[] args) throws Exception {

        SubscribeContext context=new SubscribeContext();

        context.setSecretId("AKID-522dabxxxxxxxxxxxxxxxxxx");
        context.setSecretKey("AKEY-0ff4cxxxxxxxxxxxxxxxxxxxx");
        /*****************程序改动点 BEGIN ****************/
        // API 2.0 接口下线后，如果不设置 region 参数，将会使用 API 2.0 做鉴权
        // API 2.0 下线后鉴权会失效，SDK 也不能正常使用。
        // 设置订阅 channel 所属的 region。
        context.setRegion("ap-chongqing");
        /*****************程序改动点 END ******************/


        //创建客户端
        SubscribeClient client=new DefaultSubscribeClient(context);
        //创建订阅 listener
        ClusterListener listener= new ClusterListener() {
            @Override
            public void notify(List<ClusterMessage> messages) throws Exception {
                //消费订阅到的数据
                for(ClusterMessage m:messages){
                    for(DataMessage.Record.Field f:m.getRecord().getFieldList()){
                        if(f.getFieldname().equals("id")){
                            System.out.println("seq:"+f.getValue());
                        }
                        DataMessage.Record record  = m.getRecord();
                    }
                    //消费完之后，确认消费
                    m.ackAsConsumed();
                }
            }
            @Override
            public void onException(Exception e){
                System.out.println("listen exception"+e);
            }};
        //添加监听者
        client.addClusterListener(listener);
        //设置请求的订阅通道
        client.askForGUID("dts-channel-r0M8kKsSyRZmSxQt");
        //启动客户端
        client.start();
    }
}
```
