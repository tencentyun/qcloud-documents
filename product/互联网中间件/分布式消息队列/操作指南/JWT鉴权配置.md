## 操作场景
TDMQ 提供和原生 Pulsar 一样的 JWT 鉴权方式，用户可以通过在客户端参数中配置 Token 的方式来访问对应的 TDMQ 资源。关于如何配置不同角色 Token 与 TDMQ 资源的关系，需要在控制台上进行操作，详细步骤请参考 [角色与权限](https://cloud.tencent.com/document/product/1179/47543)。

本文主要讲述如何在 TDMQ 客户端中配置 JWT 鉴权，以方便您安全地使用 TDMQ 的 Client 对接 TDMQ 进行消息的生产消费（您可以在创建 Client 的时候添加密钥）。

## 鉴权配置
### Java 客户端
在 Java 客户端中配置 JWT 鉴权：
```java
PulsarClient client = PulsarClient.builder()
    .serviceUrl("pulsar://*.*.*.*:6000/")
    .authentication(AuthenticationFactory.token("eyJh****"))
    .listenerName("custom:1********0/vpc-******/subnet-********")//custom:+路由ID
    .build();
```

### Go 客户端
在 Go 客户端中配置 JWT 鉴权：
```go
client, err := NewClient(ClientOptions{
    URL:            "pulsar://*.*.*.*:6000",
    Authentication: NewAuthenticationToken("eyJh****"),
    ListenerName:   "custom:1300*****0/vpc-******/subnet-********",
})
```
