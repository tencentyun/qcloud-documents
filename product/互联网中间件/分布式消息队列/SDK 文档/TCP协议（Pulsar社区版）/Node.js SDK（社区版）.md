## 操作场景

TDMQ Pulsar 版2.7.1及以上版本的集群已支持 Pulsar 社区版 Node.js SDK。本文介绍如何使用 Pulsar 社区版 Node.js SDK 完成接入。

## 前提条件

- 获取接点地址
  在 TDMQ Pulsar 版控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/cluster)** 页面复制接入地址。
	
- 获取密钥
  已参考 [角色与鉴权](https://cloud.tencent.com/document/product/1179/47543) 文档配置好了角色与权限，并获取到了对应角色的密钥（Token）。


## 操作步骤

1. 按照 [Pulsar 官方文档](http://pulsar.apache.org/docs/zh-CN/client-libraries-node/) 在您客户端所在的环境中安装 Node.js Client。
   ```go
   $ npm install pulsar-client
   ```

2. 在创建 Node.js Client 的代码中，配置准备好的接入地址和密钥。
```go
const Pulsar = require("pulsar-client");

(async () => {
  const client = new Pulsar.Client({
    serviceUrl: "http://*",   //更换为接入地址（控制台集群管理页完整复制）
    authentication: new Pulsar.AuthenticationToken({
      token: "eyJh**",       //更换为密钥
    }),
  });
  await client.close();
})();
```


关于 Pulsar 社区版 Node.js SDK 各种功能的使用方式，请参考 [Pulsar 官方文档](http://pulsar.apache.org/docs/zh-CN/client-libraries-node/)。

