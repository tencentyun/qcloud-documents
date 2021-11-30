TDMQ SDK 已经支持 C++ 用户 生产和消费消息，该 SDK **线程安全**。

## 支持的平台

TDMQ SDK 支持 Linux 和 MacOS 平台。   
Doxygen 为 C++ 客户端生成的 API 文档可在 [此处获得](http://pulsar.apache.org/api/cpp/2.5.0-SNAPSHOT/)。

## 下载地址（地址访问不了！！！）

C++ SDK [下载地址 >> ](http://127.0.0.1/TDMQ-cpp-sdk)  


## 注意事项

C++ SDK 依赖于 C++11 标准, 要求 用户使用的编译器版本 支持 C++11标准。

## 连接 URL

要使用 SDK 连接到 TDMQ，您需要指定 TDMQ 协议 URL。

TDMQ 集群会被赋予 一个协议 URL，默认端口为6650，下面是本机示例：
```
pulsar://localhost:6650
```

生产环境示例：
```
pulsar://pulsar.us-west.example.com:6650
```

如果使用 TLS 身份验证，需要添加 SSL，默认端口为6651，示例如下：
```
pulsar+ssl://pulsar.us-west.example.com:6650
```

## 生产 Demo 核心代码
```C++
//连接 client 配置属性 config
ClientConfiguration config;
/*
使用 config 设置 client 属性，具体可参考对应的文档或者头文件查看哪些属性可以设置

//下面是使用身份验证相关的设置
config.setUseTls(true);
config.setTlsTrustCertsFilePath("/path/to/cacert.pem");
config.setTlsAllowInsecureConnection(false);
config.setAuth(pulsar::AuthTls::create(
            "/path/to/client-cert.pem", "/path/to/client-key.pem");

Client client("pulsar+ssl://my-broker.com:6651", config);
*/

//使用 config 创建 client
Client client("pulsar://localhost:6650", config);

//使用 client 创建 生产者句柄
Producer producer;
Result result = client.createProducer("my-topic", producer);
if (result != ResultOk) {
    LOG_ERROR("Error creating producer: " << result);
    return -1;
}

// 生产10条消息
for (int i = 0; i < 10; i++){
    Message msg = MessageBuilder().setContent("my-message").build();
    Result res = producer.send(msg);
    LOG_INFO("Message sent: " << res);
}

//关闭client连接
client.close();
```

## 消费 Demo 核心代码
```C++
//创建连接 client

Client client("pulsar://localhost:6650");

Consumer consumer;
Result result = client.subscribe("my-topic", "my-subscription-name", consumer);
if (result != ResultOk) {
    LOG_ERROR("Failed to subscribe: " << result);
    return -1;
}

Message msg;

while (true) {
    consumer.receive(msg);
    LOG_INFO("Received: " << msg
            << "  with payload '" << msg.getDataAsString() << "'");

    consumer.acknowledge(msg);
}

client.close();
```
