## 操作场景

TDMQ Pulsar 版提供和原生 Pulsar 一样的 JWT 鉴权方式，用户可以通过在客户端参数中配置 Token 的方式来访问对应的 TDMQ Pulsar 版资源。关于如何配置不同角色 Token 与 TDMQ Pulsar 版资源的关系，需要在控制台上进行操作，详细步骤请参考 [角色与权限](https://cloud.tencent.com/document/product/1179/47543)。

本文主要讲述如何在 TDMQ Pulsar 版客户端中配置 JWT 鉴权，以方便您安全地使用 TDMQ Pulsar 版的 Client 对接 TDMQ Pulsar 版进行消息的生产消费（您可以在创建 Client 的时候添加密钥）。

## 鉴权配置

### Java 客户端

在 Java 客户端中配置 JWT 鉴权：
<dx-tabs>
::: 2.7.1版本及以上集群接入示例
```  java
PulsarClient client = PulsarClient.builder()
     //接入地址，在集群管理操作栏接入地址处复制
     .serviceUrl("http://*") 
		//替换成角色密钥，位于角色管理页面
     .authentication(AuthenticationFactory.token("eyJh****")) 
     .build();
```
:::
::: 2.6.1版本集群接入示例
```  java
PulsarClient client = PulsarClient.builder()
      //接入地址，在集群管理-接入点列表完整复制
		 .serviceUrl("pulsar://*.*.*.*:6000/")
		 //替换成角色密钥，位于角色管理页面
      .authentication(AuthenticationFactory.token("eyJh****")) 
		 //custom:替换成路由ID，位于集群管理-接入点列表
      .listenerName("custom:1********0/vpc-******/subnet-********")
      .build();
```
:::
</dx-tabs>





### Go 客户端

在 Go 客户端中配置 JWT 鉴权：
<dx-tabs>
::: 2.7.1版本及以上集群接入示例
```  go
client, err := NewClient(ClientOptions{
      //接入地址，在集群管理-接入点列表完整复制
		 URL:            "http://*",  
		 //替换成角色密钥，位于角色管理页面
      Authentication: NewAuthenticationToken("eyJh****"),  
})
```
:::
::: 2.6.1版本集群接入示例
```  go
client, err := NewClient(ClientOptions{
      //接入地址，在集群管理-接入点列表完整复制
		 URL:            "pulsar://*.*.*.*:6000",  
		 //替换成角色密钥，位于角色管理页面
      Authentication: NewAuthenticationToken("eyJh****"),  
		 //custom:替换成路由ID，位于集群管理-接入点列表
      ListenerName:   "custom:1300*****0/vpc-******/subnet-********",  
})
```
:::
</dx-tabs>











