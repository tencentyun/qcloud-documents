CMQ 调用链组件目前支持使用 cmq-http-client 的方式，目前仅支持单条消息收发的调用链。

您需要引入 CMQ 的依赖1.0.7.4以上版本（低版本不支持）。

```plaintext
<dependency>
			<groupId>com.qcloud</groupId>
			<artifactId>cmq-http-client</artifactId>
			<version>1.0.7.4</version>
</dependency>
```


配置参考：
```plaintext
cmq:
  server:
    endpoint: http://ocloud-cmq-queue-nameserver # CMQ 的端点地址
    secret-id: ******* # 获取账号 SecretId
    secret-key: ****** # 获取账号 SecretKey
```

>?
>- TSF SDK 1.21.7-Finchley 以及 1.21.x后续版本支持。
>- TSF SDK 1.26.1-Finchley，1.26.1-Greenwich 以及上版本提供支持。
