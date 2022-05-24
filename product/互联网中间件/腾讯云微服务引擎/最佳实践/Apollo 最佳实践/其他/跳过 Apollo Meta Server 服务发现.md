## 操作场景
Apollo支持应用在不同的环境有不同的配置，所以需要在运行提供给Apollo客户端当前环境的Apollo Meta Server信息。默认情况下，meta server和config service是部署在同一个JVM进程，所以meta server的地址就是config service的地址。
一般情况下都建议使用Apollo的Meta Server机制来实现Config Service的服务发现，从而可以实现Config Service的高可用。不过apollo-client也支持跳过Meta Server服务发现，主要用于以下场景：
1. Config Service部署在公有云上，注册到Meta Server的是内网地址，本地开发环境无法直接连接。
  - 如果通过公网 SLB 对外暴露 Config Service的话，记得要设置 IP 白名单，避免数据泄露。
2. Config Service部署在docker环境中，注册到Meta Server的是docker内网地址，本地开发环境无法直接连接。
3. Config Service部署在kubernetes中，希望使用kubernetes自带的服务发现能力（Service）。

## 操作说明
您可以通过直接指定Config Service地址的方式来跳过Meta Server服务发现，按照优先级从高到低分别为：
1. 通过Java System Property apollo.config-service(1.9.0+) 或者 apollo.configService(1.9.0之前)
- 可以通过Java的System Property apollo.config-service(1.9.0+) 或者 apollo.configService(1.9.0之前)来指定
- 在Java程序启动脚本中，可以指定-Dapollo.config-service=http://config-service-url:port
  - 如果是运行jar文件，需要注意格式是java -Dapollo.configService=http://config-service-url:port -jar xxx.jar
- 也可以通过程序指定，如System.setProperty("apollo.config-service", "http://config-service-url:port");
2. 通过操作系统的System Environment APOLLO_CONFIG_SERVICE(1.9.0+) 或者 APOLLO_CONFIGSERVICE(1.9.0之前)
- 可以通过操作系统的System Environment APOLLO_CONFIG_SERVICE(1.9.0+) 或者 APOLLO_CONFIGSERVICE(1.9.0之前)来指定
- 注意key为全大写，且中间是_分隔
3. 通过server.properties配置文件
- 可以在server.properties配置文件中指定apollo.config-service=http://config-service-url:port(1.9.0+) 或者 apollo.configService=http://config-service-url:port(1.9.0之前)
- 对于Mac/Linux，默认文件位置为/opt/settings/server.properties
- 对于Windows，默认文件位置为C:\opt\settings\server.properties
