虚拟机场景下Spring Cloud服务注册-以Consul注册中心为例
## 概述
本文以Consul注册中心为例，为您介绍如何在虚拟机场景下进行服务注册与发现。
## 流程
### 第一步：服务部署
#### 1.准备demo
可以下载我们为您准备的tse-consul-provider-demo工程及tse-consul-consumer-demo工程完成快速入门教程。

demo代码仓库：https://github.com/tencentyun/tse-simple-demo

#### 2.编译Jar包

在工程的主目录下，使用 maven 命令 mvn clean package 进行打包，即可在 target 目录下找到打包好的 Jar 文件。

#### 3.上传至CVM

上传Jar文件至和Consul注册中心处于同一私有网络下的CVM实例。若没有，则需创建一个和Consul注册中心处于同一私有网络下的CVM实例。

#### 4.配置注册中心地址并运行服务

（1）获取 TSE Consul注册中心访问地址（可从微服务引擎TSE控制台界面上复制）。

（2）设置注册中心地址参数并运行服务

登陆至工程 Jar 文件上传的CVM实例中，运行以下命令：

<dx-codeblock>
:::  plaintext
nohup java -Dspring.cloud.consul.host=[TSE Consul注册中心IP] -Dspring.cloud.consul.port=[TSE Consul注册中心端口] -jar [jar包名称] &
:::
</dx-codeblock>


### 第二步：验证服务注册

点击进入注册中心实例的服务管理页面，若出现以下页面，则证明服务注册成功。

![](https://main.qcloudimg.com/raw/e46b4e04c25fee2fd492c5915add4e3a.png)

### 第三步：验证服务发现

登陆至tse-consul-consumer-demo工程 Jar 文件上传的CVM实例中，运行以下命令：

<dx-codeblock>
:::  plaintext
curl 127.0.0.1:18084/ping-provider/test
:::
</dx-codeblock>

若出现以下返回结果，则证明服务发现成功。
<dx-codeblock>
:::  plaintext
request param: test, response from consul-demo-provider
:::
</dx-codeblock>
