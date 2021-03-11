CMQ 调用链组件目前支持使用cmq-http-client和cmq-tcp-client的方式

cmq-http-client方式

1. 需要引入cmq的依赖1.0.7.4以上版本，低版本不支持

```plaintext
        <dependency>
            <groupId>com.qcloud</groupId>
            <artifactId>cmq-http-client</artifactId>
            <version>1.0.7.4</version>
        </dependency>
```
2. 直接使用已经构建好的bean
@Autowired
private Account account;        

3. cmq接入配置：
```plaintext
cmq:
  server:
    endpoint: http://ocloud-cmq-queue-nameserver # cmq的端点地址
    secret-id: ******* # 获取账号secret-id
    secret-key: ****** # 获取账号secret-key
```

基于cmq-tcp-client

1.  在pom中引入tcp的依赖，版本要求1.1.2以上，低版本不支持

```plaintext
        <dependency>
	<groupId>com.qcloud</groupId>
	<artifactId>cmq-tcp-client</artifactId>
	<version>1.1.2</version>
</dependency>
```
2. 直接使用已经构建好的bean
@Autowired
private Consumer consumer;

@Autowired
private Producer producer;        

3. cmq接入配置：
```plaintext
cmq:
  server:
    endpoint: http://ocloud-cmq-queue-nameserver # cmq的端点地址
    secret-id: ******* # 获取账号secret-id
    secret-key: ****** # 获取账号secret-key
```


tips:
1. TSF SDK 1.21.10-Finchley 以及 1.21.x后续版本支持
2. TSF SDK 1.28.1-Finchley 以及上版本提供支持
3. 单条接收的调用链信息在同个线程中自动传递，批量接收的场景在接收之后的流程里面需要继续传递调用链则需要使用如下方法将调用链信息注入
```plaintext
@Autowired
private JoinSapn joinSapn;

joinSapn.joinBatchReceiveSpan(message);
```
