## 操作场景
Apollo 支持应用在不同的环境有不同的配置，所以需要在运行提供给 Apollo 客户端当前环境的 Apollo Meta Server 信息。默认情况下，meta server 和 config service 是部署在同一个 JVM 进程，所以 meta server 的地址就是 config service 的地址。
一般情况下都建议使用 Apollo 的 Meta Server 机制来实现 Config Service 的服务发现，从而可以实现 Config Service 的高可用。不过 apollo-client 也支持跳过 Meta Server 服务发现，主要用于以下场景：
1. Config Service 部署在公有云上，注册到 Meta Server 的是内网地址，本地开发环境无法直接连接。
>?如果通过公网 SLB 对外暴露 Config Service 的话，记得要设置 IP 白名单，避免数据泄露。
2. Config Service 部署在 docker 环境中，注册到 Meta Server 的是 docker 内网地址，本地开发环境无法直接连接。
3. Config Service 部署在 kubernetes 中，希望使用 kubernetes 自带的服务发现能力（Service）。

## 操作说明
您可以通过直接指定 Config Service 地址的方式来跳过 Meta Server 服务发现，按照优先级从高到低分别为：
1. 通过 Java System Property apollo.config-service(1.9.0+) 或者 apollo.configService(1.9.0之前)
 - 可以通过 Java 的 System Property apollo.config-service(1.9.0+) 或者 apollo.configService(1.9.0之前)来指定
 - 在 Java 程序启动脚本中，可以指定 `-Dapollo.config-service=http://config-service-url:port`
    - 如果是运行 JAR 文件，需要注意格式是 `java -Dapollo.configService=http://config-service-url:port -jar xxx.jar`
    - 也可以通过程序指定，如 `System.setProperty("apollo.config-service", "http://config-service-url:port");`
2. 通过操作系统的 System Environment APOLLO_CONFIG_SERVICE(1.9.0+) 或者 APOLLO_CONFIGSERVICE(1.9.0之前)
  - 可以通过操作系统的 System Environment APOLLO_CONFIG_SERVICE(1.9.0+) 或者 APOLLO_CONFIGSERVICE(1.9.0之前)来指定
  - 注意 key 为全大写，且中间是 `_` 进行分隔
3. 通过 server.properties 配置文件
 - 可以在 server.properties 配置文件中指定 apollo.config-service=http://config-service-url:port(1.9.0+) 或者 apollo.configService=http://config-service-url:port(1.9.0之前)
 - 对于 Mac/Linux，默认文件位置为 `/opt/settings/server.properties`
 - 对于 Windows，默认文件位置为 `C:\opt\settings\server.properties`
