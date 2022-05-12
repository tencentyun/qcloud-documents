## 操作场景
本文档指导您通过 TSF 的微服务网关配置 HTTPS 访问。

## 操作步骤
### 步骤1：准备 SSL 证书
您可以通过以下任一种方式准备一个 SSL 证书：
- 方式一：购买（通过证书授权机构购买）
- 方式二：自己生成（通过 keytool 或 openssl 工具生成）

### 步骤2：配置证书信息
1. 将 SSL 证书放到 resources下 的 https 文件夹（可自定义名称）中：
<img src="https://main.qcloudimg.com/raw/4aa46a1a1b0c8e37aef79246fb502cd3.png" width = "60%" />
2. 在配置文件 application.yml 中设置证书的基本信息。如下：
```
#  ssl证书相关配置
server：
  ssl:
    #启用ssl
    enabled: true
    #证书地址
    key-store: classpath:https/keystore.p12
    #证书密码
    key-store-password: 123456
    #证书类型
    key-store-type: JKS     
```
>?SpringCloudZuul 与 SpringCloudGateway 配置方式一致，是因为 SpringBoot 服务使用 SSL-HTTPS 的通用方式。

### 步骤3：访问验证

zuul application.yml 配置如下：
```
server:
  port: 18000
  ssl:
    enabled: true
    key-store: classpath:https/keystore.p12
    key-store-password: 123456
    key-alias: tomcathttps
    key-store-type: JKS
spring:
  application:
    name: zuul-demo
  cloud:
    consul:
      host: 127.0.0.1
      port: 8500
      discovery:
        heartbeat:
          enabled: true
          ttl-value: 5
          ttl-unit: s
        preferIpAddress: true
ribbon:
  ReadTimeout: 10000
  ConnectTimeout: 5000
zuul:
  max:
    host:
      connections: 500
  host:
    socket-timeout-millis: 10000
    connect-timeout-millis: 5000
  routes:
    api-v1:
      path: /v1/**
      serviceId: provider-demo
      stripPrefix: true
    api-v2:
      path: /v2/**
      url: http://127.0.0.1:18081
      stripPrefix: true
    api-v3:
      path: /*/v3/**
      serviceId: provider-demo
      stripPrefix: true
  ignored-patterns: /**/ignore/**
hystrix:
  command:
    default:
      execution:
        timeout:
          enabled: true
        isolation:
          thread:
            timeoutInMilliseconds: 30000
```
HTTPS 访问网关成功的显示如下：
![](https://main.qcloudimg.com/raw/37a8d18a39e30053f100791f35512328.png)

scg application.yml 配置如下：
```
server:
  port: 8080
  ssl:
    enabled: true
    key-store: classpath:https/keystore.p12
    key-store-password: 123456
    key-alias: tomcathttps
    key-store-type: JKS
  error:
    include-exception: true
spring:
  application:
    name: sc-gateway
  cloud:
    gateway:
      discovery:
        locator:
          enabled: true
          lower-case-service-id: false
      httpclient:
        connectTimeout: 10
        responseTimeout: 20s
      routes:
        - id: api-v1
          uri: lb://PROVIDER-DEMO
          order: 0
          predicates:
           - Path=/provider/**
          filters:
           - StripPrefix=1
#    consul:
#        host: 127.0.0.1
#        port: 8500
#        enabled: true
#        scheme: HTTP
logging:
  file: /var/logs/${spring.application.name}/${spring.application.name}.log
  level:
    root: INFO
    com.tencent.tsf: INFO
```
HTTPS 访问网关成功的显示如下：
![](https://main.qcloudimg.com/raw/330b310f5c48c84d9a734f042c2353b9.png)

## 常见问题
**问题描述**：当使用自签名证书时，Chrome 会拦截请求，并展示 ERR_CERT_INVALID，旧版本可以选择跳过，继续访问，但是新版本 Chrome 不允许继续，且提示：您的连接不是私密连接攻击者可能会试图从 XX.XX.XX.XX 窃取您的信息（例如：密码、通讯内容或信用卡信息）。

**解决方案**：在 Chrome 该页面上，输入 thisisunsafe，即可进行访问，用来验证 HTTPS 配置是否成功。线上环境不推荐使用自签名证书。
