## 操作场景

TDMQ Pulsar 版 2.7.1及以上版本的集群已支持 Pulsar 社区版 Python SDK。本文介绍如何使用 Pulsar 社区版 Python SDK 完成接入。

## 前提条件

- 获取接点地址
  在 TDMQ Pulsar 版控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/cluster)** 页面复制接入地址。

- 获取密钥
  已参考 [角色与鉴权](https://cloud.tencent.com/document/product/1179/47543) 文档配置好了角色与权限，并获取到了对应角色的密钥（Token）。

## 操作步骤

1. 按照 [Pulsar 官方文档](http://pulsar.apache.org/docs/zh-CN/client-libraries-python/) 在您客户端所在的环境中安装 Python Client。
   ```sh
   $ pip install pulsar-client==2.7.1
   ```

2. 在创建 consumer 或 producer 的代码中，配置准备好的接入地址和密钥。
<dx-codeblock>
:::  python
from pulsar import Client, AuthenticationToken

# 创建客户端
client = Client(‘http://***’
                authentication=AuthenticationToken('eyJh****')) # 更换为接入地址（控制台集群管理页完整复制）和密钥

# 新增一个生产者（单个client下可以创建多个生产者，请尽量复用）
producer = client.create_producer('persistent://pulsar-****/default/mytopic')
for i in range(10):
    producer.send((‘Message-%d’ % i).encode('utf-8'))
# 关闭客户端（长时间不使用一定要记得关闭客户端，及时回收连接池资源）
client.close()
:::
</dx-codeblock>


关于 Pulsar 社区版 Python SDK 各种功能的使用方式，请参考 [Pulsar 官方文档](http://pulsar.apache.org/docs/zh-CN/client-libraries-python/)。

