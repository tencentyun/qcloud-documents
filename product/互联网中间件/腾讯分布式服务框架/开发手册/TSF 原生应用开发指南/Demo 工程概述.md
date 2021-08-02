## 获取 Demo

开发前，请确保：

* 已安装 Java 和 Maven
* （如果需要部署容器）已安装 Docker

下载 Demo 地址： [spring cloud demo](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/native-app-demo/spring-cloud-boot2.tar.gz)。README 中介绍了打包 jar 包和 Docker 镜像的方法。
>?原生应用不支持全局命名空间特性。

## Demo 目录结构

```
.
├── pom.xml           # parent pom.xml
├── consul-consumer   # 使用 consul 的 consumer
├── consul-provider   # 使用 consul 的 provider
├── eureka-consumer   # 使用 eureka 的 consumer
├── eureka-provider   # 使用 eureka 的 provider
├── eureka-server     # eureka server
├── gateway           # 使用 Spring Cloud Gateway 的网关应用
└── zuul1             # 使用 Zuul1 的网关应用
```

从 pom.xml 可以看出，只使用了开源的原生组件。

## 调用说明

Demo 提供的服务和监听端口为：

* consul-consumer:8001
* consul-provider:8002
* eureka-consumer:8003
* eureka-provider:8004

可以访问 consumer 来调用 provider，例如：

```
curl consul-consumer:8001/ping-provider # 会调用 consul-provider:8002/ping

curl eureka-consumer:8003/ping-provider # 会调用 eureka-provider:8004/ping
```
