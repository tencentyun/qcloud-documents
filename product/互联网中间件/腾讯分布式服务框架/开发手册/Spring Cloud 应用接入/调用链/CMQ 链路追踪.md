CMQ 调用链组件目前支持使用 cmq-http-client 和 cmq-tcp-client 两种方式。

## cmq-http-client 方式

1. 引入 CMQ 的依赖1.0.7.4以上版本（低版本不支持）：
```xml
<dependency>
	<groupId>com.qcloud</groupId>
	<artifactId>cmq-http-client</artifactId>
	<version>1.0.7.4</version>
</dependency>
```
2. 直接使用已经构建好的 bean：
@Autowired
private Account account;        

3. CMQ 接入配置：
```
cmq:
  server:
    endpoint: http://ocloud-cmq-queue-nameserver # cmq的端点地址
    secret-id: ******* # 获取账号secret-id
    secret-key: ****** # 获取账号secret-key
```

## cmq-tcp-client 方式

1. 在 pom 中引入 tcp 的依赖，版本要求1.1.2以上（低版本不支持）：
```xml
<dependency>
	<groupId>com.qcloud</groupId>
	<artifactId>cmq-tcp-client</artifactId>
	<version>1.1.2</version>
</dependency>
```
2. 直接使用已经构建好的 bean：
	@Autowired
	private Consumer consumer;

	@Autowired
	private Producer producer;        

3. CMQ 接入配置：
```
cmq:
  server:
    endpoint: http://ocloud-cmq-queue-nameserver # CMQ 的端点地址
    secret-id: ******* # 获取账号 SecretId
    secret-key: ****** # 获取账号 SecretKey
```

## 注意事项
- TSF SDK 1.21.10-Finchley 以及 1.21.x后续版本支持。
- TSF SDK 1.28.1-Finchley 以及上版本提供支持。
- 单条接收的调用链信息在同个线程中自动传递，批量接收的场景在接收之后的流程里面需要继续传递调用链则需要使用如下方法将调用链信息注入：
```
@Autowired
private JoinSapn joinSapn;

joinSapn.joinBatchReceiveSpan(message);
```

