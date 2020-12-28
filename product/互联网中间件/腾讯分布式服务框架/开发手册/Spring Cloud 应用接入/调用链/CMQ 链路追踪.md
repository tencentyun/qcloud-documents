CMQ 调用链组件目前支持使用cmq-http-client的方式，目前仅支持单条消息收发的调用链，使用配置即可支持。

```
配置参考：
```plaintext
cmq:
  server:
    endpoint: http://ocloud-cmq-queue-nameserver # cmq的端点地址
    secret-id: ******* # 获取账号secret-id
    secret-key: ****** # 获取账号secret-key
```
