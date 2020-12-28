CMQ 调用链组件目前支持使用cmq-http-client的方式，目前仅支持单条消息收发的调用链。



配置参考：
```plaintext
cmq:
  server:
    endpoint: http://ocloud-cmq-queue-nameserver # cmq的端点地址
    secret-id: ******* # 获取账号secret-id
    secret-key: ****** # 获取账号secret-key
```

tips:
TSF SDK 1.26.1-Finchley，1.26.1-Greenwich 以及上版本提供支持
