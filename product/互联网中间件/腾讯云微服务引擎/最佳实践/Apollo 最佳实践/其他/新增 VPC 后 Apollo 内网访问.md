## 操作场景
本文指导您在 TSE 控制台新增接入到 Apollo 实例的 VPC 后，访问该 VPC 下的 Apollo 内网地址。

## 操作说明
您可以通过以下几种方式连接到新增 VPC 下的 Apollo 内网地址，按照优先级从高到低分别为：
1. 通过 Java System Property apollo.config-service(1.9.0+) 或者 apollo.configService(1.9.0之前)。在 Java 程序启动脚本中，可以指定 `-Dapollo.config-service=http://config-service-url:port`。
    - 如果是运行 JAR 文件，需要注意格式是 `java -Dapollo.configService=http://config-service-url:port -jar xxx.jar`
    - 也可以通过程序指定，如 `System.setProperty("apollo.config-service", "http://config-service-url:port");`
>? config-service-url:port 为新增 vpc 下的 Apollo 内网地址。
2. 通过操作系统的 System Environment APOLLO_CONFIG_SERVICE(1.9.0+) 或者 APOLLO_CONFIGSERVICE(1.9.0之前)。
>! key 为全大写，且中间是 `_` 进行分隔。
3. 通过 server.properties 配置文件，可以在 server.properties 配置文件中指定 apollo.config-service=http://config-service-url:port(1.9.0+) 或者 apollo.configService=http://config-service-url:port(1.9.0之前)。
>? config-service-url:port 为新增 vpc 下的 Apollo 内网地址。

## 附录
您可以参见 [Apollo 官方文档](https://www.apolloconfig.com/#/zh/usage/java-sdk-user-guide?id=_1222-%e8%b7%b3%e8%bf%87apollo-meta-server%e6%9c%8d%e5%8a%a1%e5%8f%91%e7%8e%b0) 获取更多详细信息。
