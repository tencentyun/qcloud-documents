## 操作场景

TDMQ 现已支持 Pulsar 社区版 Go SDK。本文介绍如何使用 Pulsar 社区版 Go SDK 完成接入。

## 前提条件[](id:前提条件)
- 获取路由 ID 和接入点地址
在 TDMQ 控制台【[集群管理](https://console.cloud.tencent.com/tdmq/cluster)】接入点页面，复制路由 ID 和接入点地址。

- 获取密钥
已参考 [角色与鉴权](https://cloud.tencent.com/document/product/1179/47543) 文档配置好了角色与权限，并获取到了对应角色的密钥（Token）。

## 操作步骤

1. 按照 [Pulsar 官方文档](http://pulsar.apache.org/docs/en/client-libraries-go/) 在您客户端所在的环境中安装 Go Client。
```sh
$ go get -u "github.com/apache/pulsar-client-go/pulsar"
```

2. 安装完成后，即可通过以下代码引用到您的 Go工程文件中。
```go
import "github.com/apache/pulsar-client-go/pulsar"
```

3. 在创建 Go Client 的代码中，配置准备好的 [路由 ID 和密钥](#前提条件)。
<dx-codeblock>
:::  go
client, err := pulsar.NewClient(pulsar.ClientOptions{
	 URL:               "pulsar://*.*.*.*:6000/", //更换为接入点地址
	 ListenerName:      "custom:1300*****0/vpc-******/subnet-********", //更换为路由 ID
	 Authentication:    pulsar.NewAuthenticationToken("eyJh****"), //更换为密钥
	 OperationTimeout:  30 * time.Second,
	 ConnectionTimeout: 30 * time.Second,
})
if err != nil {
	 log.Fatalf("Could not instantiate Pulsar client: %v", err)
}
:::
</dx-codeblock>
  
关于 Pulsar 社区版 Go SDK 各种功能的使用方式，请参考 [Pulsar官方文档](http://pulsar.apache.org/docs/en/client-libraries-go/)。

