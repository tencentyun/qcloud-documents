### CMQ HTTP SDK 1.0.7（2020-03-25）
- 新版的 artifactId 改为"cmq-http-client"。
- 修复异常信息被吞的 Bug。
- 移除掉了未使用 Client，同时修复了 issue#6、#7。

[代码仓库地址 >>](https://github.com/tencentyun/cmq-java-sdk/tree/1.0.7) 



### CMQ TCP SDK 1.1.1（2020-02-12）
#### 新特性
- 添加管理流相关接口，如创建队列、创建订阅等。
- 补全相关单元测试，默认构建时不开启。
- pom 文件兼容 maven 3.0+。

#### Bug 修复
- 修复事务消息异常被吞问题。
- 修复配置中超时时间对 TCP 无效的问题。
- 修复并发场景中出现“重复鉴权”的异常。

[代码仓库地址 >>](https://github.com/tencentyun/cmq-java-tcp-sdk/tree/v1.1.1) 


### CMQ HTTP SDK 1.0.6（2019-11-12）
#### 新特性
- SDK 的配置对象化，增加超时时间、是否打印慢操作日志等参数，详情见 CmqConfig 对象。
- 新接收消息、发送接口性能提升6倍。
- 新增自动慢操作、异常日志打印（需用户配置日志文件）。
- 新发送接口增加 requestId 的返回，方便客户问题追踪。

#### Bug 修复
- 修复偶发 JSON 序列化异常问题。
- 其他代码规范问题的修复。
- 日志配置操作。
- SDK 已经使用 slf4j 打印日志，但没有具体的日志配置文件，用户在 classpath 中添加 log4j 或 logback 等日志框架的配置文件即可。

#### 使用建议
- 使用新的（batch）receiveMessage 接口接收消息（长轮询等待时间由队列的设置决定）。
- 使用新的（batch）send 接口发送消息（可以返回 requestId）。

[代码仓库地址 >>](https://github.com/tencentyun/cmq-java-sdk/tree/1.0.6)     


### CMQ SDK 1.05（2019-06-28）
CMQ 支持基于 TCP 协议的 SDK 调用，使用更少的计算资源、更安全的客户端线程、更高效的传输效率、更优的使用体验、更多样的特性支持。

### CMQ SDK 1.0.4（2017-04-07）
- CMQ SDK 支持 sha256 签名，您可在初始化 Account 中调用 setSignMethod（具体方法名可参考代码说明）设置签名方法。
- 修复已知 Bug。

### CMQ SDK 1.0.3（2017-03-13）
CMQ 新增特性：消息回溯、消息延时、订阅路由功能。

### CMQ SDK 1.0.2（2016-12-01）
- SDK 支持主题和订阅模式。
- C++ SDK 改用 cmake 管理项目。
- Java SDK 改用 maven 管理项目。

###   CMQ SDK 1.0.1（2016-10-12） 
- 优化客户端超时体验。
- 修复 PHP SDK 鉴权失败 Bug。
- 修复 PHP 发送消息 Bug。

### CMQ SDK 1.0.0（2016-09-07） 
- 同时上线 C++、Java、Python、PHP 四个语言版本。
- SDK 封装了发送消息、接收消息、删除消息等操作接口。


