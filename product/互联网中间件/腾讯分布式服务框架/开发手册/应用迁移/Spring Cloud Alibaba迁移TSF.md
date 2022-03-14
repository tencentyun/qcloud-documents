## 操作场景

应用迁移到 TSF 平台后即可享受平台一站式微服务解决方案：管理资源和应用更加便利、丰富的服务治理能力、多维度的监控和跨可用区高可用方案等。

本文介绍从 Spring Cloud Alibaba 迁移到 TSF 平台所需的改造工作，经过改造后，服务可以在 TSF 平台上成功注册和互相调用。现在就目前 Spring Cloud Alibaba 常见的 Restful 和 Dubbo 两类服务框架，分别说明改造方法。


## Restful 服务改造

这部分改造主要包括删除 Nacos 依赖和配置、添加 TSF 的依赖和启动类的注解。

### 步骤1：依赖调整

1. 以下 Nacos 配置中心、注册中心、Spring Boot、Spring Cloud 的依赖，在迁移的时候，需要删除。

	```xml
	<dependency>
					<groupId>org.springframework.boot</groupId>
					<artifactId>spring-boot-starter-web</artifactId>
	</dependency>
	<dependency>
					<groupId>com.alibaba.cloud</groupId>
					<artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
	</dependency>
	<dependency>
					<groupId>com.alibaba.cloud</groupId>
					<artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
	</dependency>
	<dependency>
					<groupId>org.springframework.boot</groupId>
					<artifactId>spring-boot-starter-actuator</artifactId>
	</dependency>
	<!-- Spring Cloud Open Feign -->
	<dependency>
					<groupId>org.springframework.cloud</groupId>
					<artifactId>spring-cloud-starter-openfeign</artifactId>
	</dependency>
	```

2. 添加 TSF 依赖，TSF SDK 已经包含 Spring Boot、Spring Cloud 的依赖。

	```xml
	<!-- TSF 启动器 -->
	<dependency>
					<groupId>com.tencent.tsf</groupId>
					<artifactId>spring-cloud-tsf-starter</artifactId>
					<version><!-- 调整为 SDK 版本号 --></version>
	</dependency>
	```
 <dx-alert infotype="explain" title="">
SDK 版本请参考 [SDK 文档](https://cloud.tencent.com/document/product/649/49320)。
</dx-alert>




### 步骤2：配置调整

以下是 Nacos 服务注册中心和配置中心的配置项示例，在迁移时，要删除配置文件中这部分内容。

**Nacos 服务注册中心**

```yaml
spring.cloud.nacos.discovery.server-addr=127.0.0.1:8848
#spring.cloud.nacos.discovery.instance-enabled=true



spring.cloud.nacos.username=nacos
spring.cloud.nacos.password=nacos



management.endpoints.web.exposure.include=*
management.endpoint.health.show-details=always
```

**Nacos 配置中心**

```yaml
spring.cloud.nacos.config.server-addr=127.0.0.1:8848



#nacos certification information
spring.cloud.nacos.username=nacos
spring.cloud.nacos.password=nacos



#spring.cloud.nacos.config.refreshable-dataids=common.properties
#spring.cloud.nacos.config.shared-data-ids=common.properties,base-common.properties
spring.cloud.nacos.config.shared-configs[0]= common333.properties
spring.cloud.nacos.config.shared-configs[1].data-id= common111.properties
spring.cloud.nacos.config.shared-configs[1].group= GROUP_APP1
spring.cloud.nacos.config.shared-configs[1].refresh= true
spring.cloud.nacos.config.shared-configs[2]= common222.properties



#spring.cloud.nacos.config.ext-config[0]=ext.properties
spring.cloud.nacos.config.extension-configs[0].data-id= extension1.properties
spring.cloud.nacos.config.extension-configs[0].refresh= true
spring.cloud.nacos.config.extension-configs[1]= extension2.properties
spring.cloud.nacos.config.extension-configs[2].data-id= extension3.json
```

### 步骤3：代码调整

向应用启动类中添加`@EnableTsf`注解。

### 步骤4：应用部署

实现以上三步操作并且成功编译打包后，即完成改造，进入应用部署环节。TSF 平台支持多种应用类型，Restful 应用可以采用普通应用类型进行部署，更多信息请参考 [应用部署](https://cloud.tencent.com/document/product/649/16931)，按照文档指引操作即可。



## Dubbo 服务改造

TSF 平台纳管 Spring Cloud Alibaba Dubbo 应用采用的是 TSF Mesh 技术，TSF Mesh 支持 Dubbo、HTTP 等协议，通过 Sidecar 注册到服务注册中心、处理服务间通信。

改造主要涉及两方面内容：
- 一个是 Mesh 化，引入 Sidecar。
- 另一个是移除原有注册中心的依赖和配置。TSF 兼容双注册，在不移除原有注册中心的情况下，经过少量代码调整，也可以成功部署应用，但是为了降低程序包的大小，加快应用部署和启动速度，建议要移除原有注册中心的依赖和配置。

### 步骤1：Mesh 改造

**服务定义和注册（必选）**

创建 spec.yaml 文件，定义服务名、暴露的端口和协议，服务名和接口名相同。由于 Dubbo 2 采用的是接口级服务发现，所以需要每个接口都要进行定义，在最新版的 Dubbo 3 中，采用了应用级服务发现，操作会简化很多。

```yaml
apiVersion: v1
kind: Application
spec:
    services:
      - name: com.dubbo.service.UserService
        ports:
          - targetPort: 20881
            protocol: dubbo
        healthCheck:
          path:
```

**API 定义和上报（可选）**

创建 apis 目录，该目录放置服务的 API 定义。一个服务对应一个 yaml 文件，文件名即服务名，API 遵循 OPENAPI 3.0 规范。

```yaml
openapi: 3.0.0
info:
version: "1.0.0"
title: user service
paths:
/api/v6/user/create:
    get:
      responses:
        '200':
           description: OK
        '401':
           description: Unauthorized
        '402':
           description: Payment Required
        '403':
           description: Forbidden
/api/v6/user/account/query:
    get:
      responses:
        '200':
           description: OK
        '401':
           description: Unauthorized
        '402':
           description: Payment Required
        '403':
           description: Forbidden
/health:
    get:
      responses:
        '200':
           description: OK
        '401':
           description: Unauthorized
        '402':
           description: Payment Required
        '403':
           description: Forbidden
```

**调用链 Header 传递（可选）**

要实现 Mesh 应用调用链和服务依赖拓扑功能，需要在请求中带上9个相关 header。

```yaml
// 9个调用链相关的头，具体说明(https://www.envoyproxy.io/docs/envoy/v1.8.0/configuration/http_conn_man/headers.html?highlight=tracing)
traceHeaders = ['x-request-id',
			  		'x-trace-service',
				  	'x-ot-span-context',
				  	'x-client-trace-id',
				  	'x-b3-traceid',
					  'x-b3-spanid',
				  	'x-b3-parentspanid',
				  	'x-b3-sampled',
					  'x-b3-flags']
```

参考文档：[开发使用指引](https://cloud.tencent.com/document/product/649/19049)

### 步骤2：依赖调整

删除 Nacos 服务注册和配置的依赖，如下例：

```xml
<dependency>
			<groupId>com.alibaba.cloud</groupId>
			<artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
</dependency>
<dependency>
			<groupId>com.alibaba.cloud</groupId>
			<artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>
```

### 步骤3：配置调整

关闭 Dubbo 服务注册中心配置，如下例：

```yaml
spring.cloud.nacos.discovery.server-addr=127.0.0.1:8848
#spring.cloud.nacos.discovery.instance-enabled=true



spring.cloud.nacos.username=nacos
spring.cloud.nacos.password=nacos



management.endpoints.web.exposure.include=*
management.endpoint.health.show-details=always
```

删除 Nacos 配置中心的配置，如下例：

```yaml
spring.cloud.nacos.config.server-addr=127.0.0.1:8848



#nacos certification information
spring.cloud.nacos.username=nacos
spring.cloud.nacos.password=nacos



#spring.cloud.nacos.config.refreshable-dataids=common.properties
#spring.cloud.nacos.config.shared-data-ids=common.properties,base-common.properties
spring.cloud.nacos.config.shared-configs[0]= common333.properties
spring.cloud.nacos.config.shared-configs[1].data-id= common111.properties
spring.cloud.nacos.config.shared-configs[1].group= GROUP_APP1
spring.cloud.nacos.config.shared-configs[1].refresh= true
spring.cloud.nacos.config.shared-configs[2]= common222.properties



#spring.cloud.nacos.config.ext-config[0]=ext.properties
spring.cloud.nacos.config.extension-configs[0].data-id= extension1.properties
spring.cloud.nacos.config.extension-configs[0].refresh= true
spring.cloud.nacos.config.extension-configs[1]= extension2.properties
spring.cloud.nacos.config.extension-configs[2].data-id= extension3.json
```

删除 Hystrix 配置：

```yaml
feign:
  hystrix:
    enabled: true
```

### 步骤4：代码调整

1. 删除服务发现的注解 `@EnableDiscoveryClient`。
2. 服务消费端的 `@Reference` 注解添加 url 属性，属性值为 `dubbo：//服务名:端口`，添加 `check=false` 属性。在兼容双注册的场景下，这个代码需要额外添加。

### 步骤5：应用部署

代码改造完并且成功编译打包后，进入应用部署环节。在 TSF 平台创建 Mesh 应用类型进行部署，更多信息请参考 [应用部署](https://cloud.tencent.com/document/product/649/16931)，按照文档指引操作即可。
