## 操作场景

本文以调用 Go SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装 Go](https://golang.org/dl/)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-go-sdk-demo.zip)

## 操作步骤
### 步骤1：准备环境
在客户端环境执行如下命令下载 RocketMQ 客户端相关的依赖包。
<dx-codeblock>
:::  go
   go get github.com/apache/rocketmq-client-go/v2
:::
</dx-codeblock>


### 步骤2：生产消息

1. 创建并编译运行生产消息程序。
<dx-codeblock>
:::  go
   // 服务接入地址  (注意：需要在接入地址前面加上  http:// 或 https:// 否则无法解析)
   var serverAddress = "https://rocketmq-xxx.rocketmq.ap-bj.public.tencenttdmq.com:9876"
   // 授权角色名
   var secretKey = "admin"
   // 授权角色密钥
   var accessKey = "eyJrZXlJZC...."
   // 命名空间全称
   var nameSpace = "rocketmq-xxx|namespace_go"
   // 生产者组名称
   var groupName = "group1"
   // 创建消息生产者
   p, _ := rocketmq.NewProducer(
       // 设置服务地址
       producer.WithNsResolver(primitive.NewPassthroughResolver([]string{serverAddress})),
       // 设置acl权限
       producer.WithCredentials(primitive.Credentials{
           SecretKey: secretKey,
           AccessKey: accessKey,
       }),
       // 设置生产组
       producer.WithGroupName(groupName),
       // 设置命名空间名称
       producer.WithNamespace(nameSpace),
       // 设置发送失败重试次数
       producer.WithRetry(2),
   )
   // 启动producer
   err := p.Start()
   if err != nil {
       fmt.Printf("start producer error: %s", err.Error())
       os.Exit(1)
   }
:::
</dx-codeblock>
<table>
    <tr>
        <th>参数</th>
        <th>说明</th>
    </tr>
    <tr>
        <td>groupName</td>
        <td>生产者组名称，在控制台集群管理 Group 页签中获取。</td>
    </tr>
    <tr>
        <td>serverAddress</td>
				<td>集群接入地址，在控制台<b>集群管理</b>页面操作列的<b>接入地址</b>获取。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/88046dcc0b052e11dc5c7c2ee8a901e4.png" style="width: 100%">
						<b>注意：</b>需要在接入地址前面加上 <code>http://</code> 或 <code>https://</code> 否则无法解析。
        </td>
    </tr>
    <tr>
        <td>secretKey</td>
        <td>角色名称，在 <a href = "https://console.cloud.tencent.com/tdmq/role"><b>角色管理</b></a> 页面复制。</td>
    </tr>
    <tr>
        <td>accessKey</td>
        <td>角色密钥，在 <a href = "https://console.cloud.tencent.com/tdmq/role"><b>角色管理</b></a> 页面复制<b>密钥</b>列复制。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/738800581043835d6123385964281f37.png" style="width: 100%">
        </td>
    </tr>
    <tr>
        <td>nameSpace</td>
        <td>命名空间全称可在控制台集群管理 Topic 页签中复制，格式是<code>集群 ID</code> +<code>｜</code>+<code>命名空间</code>。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/c483d23c09d2f728aaa08b195d9ddd40.png" style="width: 100%">
        </td>
    </tr>
</table>
2. 发送消息（以同步发送方式为例）。
<dx-codeblock>
:::  go
   // topic名称
   var topicName = "topic1"
   // 构造消息内容
   msg := &primitive.Message{
       Topic: topicName, // 设置topic名称
       Body:  []byte("Hello RocketMQ Go Client! This is a new message."),
   }
   // 设置tag
   msg.WithTag("TAG")
   // 设置key
   msg.WithKeys([]string{"yourKey"})
   // 发送消息
   res, err := p.SendSync(context.Background(), msg)
   
   if err != nil {
       fmt.Printf("send message error: %s\n", err)
   } else {
       fmt.Printf("send message success: result=%s\n", res.String())
   }
:::
</dx-codeblock>
<table>
    <tr>
        <th>参数</th>
        <th>说明</th>
    </tr>
    <tr>
        <td>topicName</td>
        <td>Topic 名称在控制台集群管理 Topic 页签中复制具体 Topic 名称。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/4b096254ae2fa8db0f45c1f864718915.png" style="width: 100%">
        </td>
    </tr>
    <tr>
        <td>TAGS</td>
        <td>用来设置消息的 TAG。</td>
    </tr>
    <tr>
        <td>yourKey</td>
        <td>设置消息业务 key。</td>
    </tr>
</table>
3. 资源释放。
<dx-codeblock>
:::  go
   // 关闭生产者
   err = p.Shutdown()
   if err != nil {
       fmt.Printf("shutdown producer error: %s", err.Error())
   }
:::
</dx-codeblock>
 

<dx-alert infotype="explain" title="">
异步发送、单向发送等，可参见 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-go-sdk-demo.zip) 示例或参见 [rocketmq-client-go 示例](https://github.com/apache/rocketmq-client-go/tree/master/examples)。

</dx-alert>

### 步骤3：消费消息
1.创建消费者。
<dx-codeblock>
:::  go
   // 服务接入地址  (注意：需要在接入地址前面加上  http:// 或 https:// 否则无法解析)
   var serverAddress = "https://rocketmq-xxx.rocketmq.ap-bj.public.tencenttdmq.com:9876"
   // 授权角色名
   var secretKey = "admin"
   // 授权角色密钥
   var accessKey = "eyJrZXlJZC...."
   // 命名空间全称
   var nameSpace = "rocketmq-xxx|namespace_go"
   // 生产者组名称
   var groupName = "group11"
   // 创建consumer
   c, err := rocketmq.NewPushConsumer(
       // 设置消费者组
       consumer.WithGroupName(groupName),
       // 设置服务地址
       consumer.WithNsResolver(primitive.NewPassthroughResolver([]string{serverAddress})),
       // 设置acl权限
       consumer.WithCredentials(primitive.Credentials{
           SecretKey: secretKey,
           AccessKey: accessKey,
       }),
       // 设置命名空间名称
       consumer.WithNamespace(nameSpace),
       // 设置从起始位置开始消费
       consumer.WithConsumeFromWhere(consumer.ConsumeFromFirstOffset),
       // 设置消费模式（默认集群模式）
       consumer.WithConsumerModel(consumer.Clustering),
   )
   if err != nil {
       fmt.Println("init consumer2 error: " + err.Error())
       os.Exit(0)
   }
:::
</dx-codeblock>
<table>
    <tr>
        <th>参数</th>
        <th>说明</th>
    </tr>
    <tr>
        <td>groupName</td>
        <td>消费者组名称，在控制台集群管理 Group 页签中获取。</td>
    </tr>
    <tr>
        <td>serverAddress</td>
				<td>集群接入地址，在控制台<b>集群管理</b>页面操作列的<b>接入地址</b>获取。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/88046dcc0b052e11dc5c7c2ee8a901e4.png" style="width: 100%">
						<b>注意：</b>需要在接入地址前面加上 <code>http://</code> 或 <code>https://</code> 否则无法解析。
        </td>
    </tr>
    <tr>
        <td>secretKey</td>
        <td>角色名称，在 <a href = "https://console.cloud.tencent.com/tdmq/role"><b>角色管理</b></a> 页面复制。</td>
    </tr>
    <tr>
        <td>accessKey</td>
        <td>角色密钥，在 <a href = "https://console.cloud.tencent.com/tdmq/role"><b>角色管理</b></a> 页面复制<b>密钥</b>列复制。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/738800581043835d6123385964281f37.png" style="width: 100%">
        </td>
    </tr>
    <tr>
        <td>nameSpace</td>
        <td>命名空间全称可在控制台集群管理 Topic 页签中复制，格式是<code>集群 ID</code> +<code>｜</code>+<code>命名空间</code>。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/c483d23c09d2f728aaa08b195d9ddd40.png" style="width: 100%">
        </td>
    </tr>
</table>
2. 发送消息。
<dx-codeblock>
:::  go
   // topic名称
   var topicName = "topic1"
   // 设置订阅消息的tag
   selector := consumer.MessageSelector{
       Type:       consumer.TAG,
       Expression: "TagA || TagC",
   }
   // 设置重新消费的延迟级别，共支持18种延迟级别。下面是延迟级别与延迟时间的对应关系
   // 1   2   3    4    5   6   7   8   9   10  11  12  13  14   15   16   17  18
   // 1s, 5s, 10s, 30s, 1m, 2m, 3m, 4m, 5m, 6m, 7m, 8m, 9m, 10m, 20m, 30m, 1h, 2h
   delayLevel := 1
   err = c.Subscribe(topicName, selector, func(ctx context.Context,
                                                                 msgs ...*primitive.MessageExt) (consumer.ConsumeResult, error) {
       fmt.Printf("subscribe callback len: %d \n", len(msgs))
   	// 设置下次消费的延迟级别
       concurrentCtx, _ := primitive.GetConcurrentlyCtx(ctx)
       concurrentCtx.DelayLevelWhenNextConsume = delayLevel // only run when return consumer.ConsumeRetryLater
   
       for _, msg := range msgs {
           // 模拟重试3次后消费成功
           if msg.ReconsumeTimes > 3 {
               fmt.Printf("msg ReconsumeTimes > 3. msg: %v", msg)
               return consumer.ConsumeSuccess, nil
           } else {
               fmt.Printf("subscribe callback: %v \n", msg)
           }
       }
       // 模拟消费失败，回复重试
       return consumer.ConsumeRetryLater, nil
   })
   if err != nil {
       fmt.Println(err.Error())
   }
:::
</dx-codeblock>
<table>
    <tr>
        <th>参数</th>
        <th>说明</th>
    </tr>
    <tr>
        <td>topicName</td>
        <td>Topic 名称在控制台集群管理 Topic 页签中复制具体 Topic 名称。
            <img src = "https://qcloudimg.tencent-cloud.cn/raw/4b096254ae2fa8db0f45c1f864718915.png" style="width: 100%">
        </td>
    </tr>
    <tr>
        <td>Expression</td>
        <td>消息 TAG 标识。</td>
    </tr>
    <tr>
        <td>delayLevel</td>
        <td>设置重新消费的延迟级别，共支持18种延迟级别。</td>
    </tr>
</table>
3. 资源释放 （消费者消费消息必须在订阅之后）。
<dx-codeblock>
:::  go
   // 开始消费
   err = c.Start()
   if err != nil {
       fmt.Println(err.Error())
       os.Exit(-1)
   }
   time.Sleep(time.Hour)
   // 资源释放
   err = c.Shutdown()
   if err != nil {
       fmt.Printf("shundown Consumer error: %s", err.Error())
   }
:::
</dx-codeblock>


### 步骤4：查看消费详情
登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，在**集群管理** > **Group** 页面，可查看与 Group 连接的客户端列表，单击操作列的**查看详情**，可查看消费者详情。
![](https://qcloudimg.tencent-cloud.cn/raw/924898b7a5568be778449bf51034396d.png)

   

>?本文简单介绍了使用 Go 客户端进行简单的收发消息，更多操作可参见 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-go-sdk-demo.zip) 或 [rocketmq-client-go 示例](https://github.com/apache/rocketmq-client-go/tree/master/examples)。

