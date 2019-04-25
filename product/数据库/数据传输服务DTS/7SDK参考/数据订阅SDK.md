## 数据订阅 SDK 下载
单击下载 [数据订阅 SDK Version 2.8.0](https://main.qcloudimg.com/raw/2e471276a1609b488776ae57d9ea6f83/binlogsdk-2.8.0-official.jar)。

## 发布日志

### Version 2.8.0
1. 优化了内部鉴权逻辑。
2. 减少用户参数设置。

### Version 2.7.2
1. 在 DDL 语句返回值中填充 db 值。

### Version 2.7.0
1. 数据订阅通道后台的 HA 功能，秒级切换。
2. 添加 SDK 监控指标上报。

### Version 2.6.0
1. 支持单 SDK 订阅多个通道。
2. 支持订阅 Client 的 stop、start 等操作。
3. 支持 DataMessage.Record 的序列化。
4. 优化 SDK 的性能，降低资源消耗。

### Version 2.5.0
1. 修复高并发情况下小概率出现的 bug。
2. 支持事务中记录的全局唯一自增的 ID。

### Version 2.4.0
1. 配合后台优化了订阅的逻辑，可以精确显示 SDK 当前的消费时间点。
2. 修复了后台的少数特殊字符的编码问题。
3. **修复了多项兼容性问题，建议更老版本用户尽快升级至此版本**。

## 运行原理

### 拉取
SDK 的拉取和确认消息是两个异步的线程同时在做的，拉取是按顺序拉取的，两个线程的执行分别独立是严格有序，但这两个线程之间是异步的。

拉取到的消息会按顺序调用用户注册的 notify 函数，SDK 保证每一条消息会推送一次，且只有一次；如果没有调用 m.ackAsConsumed() 函数，消息还是会继续 notify，因为拉取和确认是异步的。

### 确认机制
SDK 采用的是增量确认机制，可以重复确认，但不可以漏确认任何一条消息，包括 BEGIN 和 COMMIT 消息。

- 例如客户端收到了1、2、3、4、5五条消息，但是客户端程序只对 1、2、5 这三条消息调用了 m.ackAsConsumed() 操作，那么 SDK 只会向服务器确认消费了1、2这两条消息，如果此时客户端程序出现故障，SDK 下次会从3这条消息开始获取。
由于 SDK 消息拉取和确认是异步的，所以如果中间有消息没确认，SDK 仍然会去拉取新消息并 notify 给客户端，但是超过一定的长度（目前为8000），就不会拉取新的消息。
- 每一个消息记录都有唯一的 record_id 和 checkpoint，SDK 其实是对消息的 checkpoint 进行确认。

## 运行环境要求
- Java 环境：JRE 1.6 及以上版本。
- SDK 需要运行在腾讯云的 CVM 主机上，与订阅实例在同地域的同一个 VPC 下（ 如果不在同一个 VPC，需要配置互通）。
- 如果要在公网上访问，可以用 CVM 做端口转发，不过这样**带宽和性能无法得到保证**，强依赖于外网带宽。

## 示例代码
使用腾讯云 Binlog 订阅示例代码如下：
```java
import com.qcloud.dts.context.SubscribeContext;
import com.qcloud.dts.message.ClusterMessage;
import com.qcloud.dts.message.DataMessage;
import com.qcloud.dts.subscribe.ClusterListener;
import com.qcloud.dts.subscribe.DefaultSubscribeClient;
import com.qcloud.dts.subscribe.SubscribeClient;

import java.util.List;

public class Main {

    public static void main(String[] args) throws Exception {
        //创建一个context
        SubscribeContext context=new SubscribeContext();

        //用户secretId、secretKey
        context.setSecretId("AKID-522dabxxxxxxxxxxxxxxxxxx");
        context.setSecretKey("AKEY-0ff4cxxxxxxxxxxxxxxxxxxxx");

        // 设置channel所在的region，2.8.0以后的SDK推荐设置region参数
        // region值参照：https://cloud.tencent.com/document/product/236/15833#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8
        context.setRegion("ap-beijing");
        // 订阅的serviceIp和servicePort
        // 注意：2.8.0以前的SDK需要设置Ip和Port两个参数，2.8.0以后的版本如果设置了region参数则可以省略
        // context.setServiceIp("10.108.112.24");
        // context.setServicePort(50120);

        //创建客户端
        SubscribeClient client=new DefaultSubscribeClient(context);
        //创建订阅listener
        ClusterListener listener= new ClusterListener() {
            @Override
            public void notify(List<ClusterMessage> messages) throws Exception {
                //消费订阅到的数据
                for(ClusterMessage m:messages){
                    for(DataMessage.Record.Field f:m.getRecord().getFieldList()){
                        if(f.getFieldname().equals("id")){
                            System.out.println("seq:"+f.getValue());
                        }
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
        client.askForGUID("dts-channel-B2eG8xbLvi472wV3");
        //启动客户端
        client.start();
    }
}
```

整个流程是个典型的生产者消费者模型，SDK 作为消费者不断地从服务器拉取订阅的 Binlog 数据，消费数据，消费完确认消费完数据，比较直观：
 1. 首先配置参数，创建消费客户端`SubscribeClient`。
 2. 然后创建一个监听器`ClusterListener`，消费收到的 Binlog 订阅数据，消费完之后返回确认消息。
 3. 最后启动客户端，开始流程。
在监听器`ClusterListener`中，可以根据用户自身的需求，对收到的数据进行操作，还可以对收到 Binlog 数据根据类型进行过滤，例如过滤掉所有`drop`语句等。
 
示例代码中，用户需要提供五个参数。
- 其中`secretId`和`secretKey`是跟用户腾讯云账号关联的密钥值，可以在控制台的【访问管理】>【访问密钥】>【API密钥管理】查看，SDK 用这两个参数来对用户操作进行鉴权。
>!数据订阅 SDK 已经接入了 CAM 权限控制，根账号默认有所有的权限，可以直接用根账号的云 API 密钥访问；子账号默认没有任何权限，需要根账号给子账号赋予`name/dts:AuthenticateSubscribeSDK`操作的权限，或者赋予 DTS 所有操作的权限`QcloudDTSFullAccess`。
- 另外三个参数`serviceIp`、`servicePort`、`channelId`都是与用户 Binlog 订阅相关的，在云数据库 MySQL 相应页面配置好订阅内容后，可在 [DTS 控制台](https://console.cloud.tencent.com/dtsnew/dss) 的【数据订阅】页查看。
>?`serviceIp`即数据订阅控制台【服务地址】里的 IP、`servicePort`即【服务地址】里的端口号、`channelId`即【通道ID】。
