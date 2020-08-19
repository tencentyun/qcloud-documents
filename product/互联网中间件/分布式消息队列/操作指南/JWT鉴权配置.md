## 操作场景
TDMQ 提供和原生 Pulsar 一样的 JWT 鉴权方式，用户可以通过在客户端参数中配置 Token 的方式来访问对应的 TDMQ 资源。关于如何配置不同角色 Token 与 TDMQ 资源的关系，需要在控制台上进行操作，详细步骤请参考 [角色与权限](https://cloud.tencent.com/document/product/1179/47543)。

本文主要讲述如何在 Pulsar 原生客户端中配置 JWT 鉴权，以方便您安全地使用 Pulsar 社区版的 Client 对接 TDMQ 进行消息的生产消费（您可以在创建 Client 的时候添加密钥）。

>?您可以通过 [Pulsar 官方文档](http://pulsar.apache.org/docs/zh-CN/client-libraries/) 查看各语言客户端依赖的安装方式。


## 鉴权配置
### Java 客户端
在 Java 客户端中配置 JWT 鉴权：
```java
PulsarClient client = PulsarClient.builder()
    .serviceUrl("pulsar://*.*.*.*:6000/")
    .authentication(
      AuthenticationFactory.token("eyJh****"))
    .build();
```

### Go 客户端
在 Go 客户端中配置 JWT 鉴权：
```go
client, err := NewClient(ClientOptions{
    URL:            "pulsar://*.*.*.*:6000",
    Authentication: NewAuthenticationToken("eyJh****"),
})
```

### Python 客户端
在 Python 客户端中配置 JWT 鉴权：
```python
from pulsar import Client, AuthenticationToken

client = Client('pulsar://*.*.*.*:6000/'
                authentication=AuthenticationToken('eyJh****'))
```

或者，您也可以在创建好本地 Token 文件后，通过 `Supplier`创建：
```python
def read_token():
    with open('/path/to/token.txt') as tf:
        return tf.read().strip()

client = Client('pulsar://*.*.*.*:6000/'
                authentication=AuthenticationToken(read_token))
```

### C++ 客户端
在 C++ 客户端中配置 JWT 鉴权：
```c++
#include <pulsar/Client.h>

pulsar::ClientConfiguration config;
config.setAuth(pulsar::AuthToken::createWithToken("eyJh****"));

pulsar::Client client("pulsar://*.*.*.*:6000/", config);
```

### C# 客户端
在 C# 客户端中配置 JWT 鉴权：
```c#
var client = PulsarClient.Builder()
                         .AuthenticateUsingToken("eyJh****")
                         .Build();
```

