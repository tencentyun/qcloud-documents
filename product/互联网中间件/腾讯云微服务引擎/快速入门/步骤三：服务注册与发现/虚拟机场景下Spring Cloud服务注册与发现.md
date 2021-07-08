## 操作场景
本文为您介绍如何在虚拟机场景下进行服务注册与发现。


## 操作步骤
### 步骤1：服务部署
#### 1. 准备Spring Cloud 应用
Spring Cloud 应用使用如下的配置接入 Consul / Eureka /Zookeeper 注册中心：
>?
>- 您可以点击以下页签，查看对应配置。
>- 您需要将配置中的 x.x.x.x 替换为您 TSE 实例的 【访问方式】 中的 IP 地址。
<dx-tabs>
::: Consul 
<dx-codeblock>
:::  plaintext
spring:
  cloud:
    consul:
      host: x.x.x.x
      port: 8500
      discovery:
        prefer-ip-address: true
:::
</dx-codeblock>
:::
::: Eureka
<dx-codeblock>
:::  plaintext
eureka:
  client:
    serviceUrl:
      defaultZone: http://x.x.x.x:8761/eureka/
  instance:
    prefer-ip-address: true
:::
</dx-codeblock>
:::
::: Zookeeper
<dx-codeblock>
:::  plaintext
spring:
  cloud:
    zookeeper:
      connect-string: x.x.x.x:2181
      discovery:
        register: true
        enabled: true
        prefer-ip-address: true
:::
</dx-codeblock>
:::
</dx-tabs>




您可以下载我们提供的demo，快速完成快速入门教程。

[Demo 代码仓库 >>](https://github.com/tencentyun/tse-simple-demo)



#### 2. 编译 Jar 包

在工程的主目录下，使用 maven 命令 `mvn clean package` 进行打包，即可在 target 目录下找到打包好的 Jar 文件。

#### 3. 上传至 CVM

上传 Jar 文件至和注册中心实例处于同一私有网络下的 CVM 实例。若没有，则需创建一个和注册中心实例处于同一私有网络下的 CVM 实例。


#### 4. 配置注册中心地址并运行服务

4.1 获取 TSE 注册中心实例访问地址（可从微服务引擎 [TSE 控制台](https://console.cloud.tencent.com/tse) 界面复制）。

4.2 设置注册中心地址参数并运行服务。
登录至工程 Jar 文件上传的 CVM 实例中，运行以下命令：
<dx-tabs>
::: Consul 
<dx-codeblock>
:::  plaintext
nohup java 
-Dspring.cloud.consul.host=[TSE Consul注册中心IP] 
-Dspring.cloud.consul.port=[TSE Consul注册中心端口] 
-jar [jar包名称] &
:::
</dx-codeblock>
:::
::: Eureka
<dx-codeblock>
:::  plaintext
java 
-Deureka.client.serviceUrl.defaultZone=http://localhost:8761/eureka/ 
-jar [jar包名称]
:::
</dx-codeblock>
:::
::: Zookeeper
<dx-codeblock>
:::  plaintext
java 
-Dspring.cloud.zookeeper.connect-string=[TSE Zookeeper注册中心IP]:[TSE Zookeeper注册中心端口] 
-jar [jar包名称]
:::
</dx-codeblock>
:::
</dx-tabs>




### 步骤2：验证服务注册

点击进入注册中心实例的服务管理页面，若出现以下页面，则证明服务注册成功。
<img src="https://main.qcloudimg.com/raw/634875f23e5d4841095fe512d2809446.png">


### 步骤3：验证服务发现

登录Spring Cloud 应用工程 Jar 文件上传的 CVM 实例，运行以下命令：

<dx-codeblock>
:::  plaintext
curl 127.0.0.1:18084/ping-provider/test
:::
</dx-codeblock>

若出现以下返回结果，则证明服务发现成功。
<dx-codeblock>
:::  plaintext
request param: test, response from [应用名]
:::
</dx-codeblock>
