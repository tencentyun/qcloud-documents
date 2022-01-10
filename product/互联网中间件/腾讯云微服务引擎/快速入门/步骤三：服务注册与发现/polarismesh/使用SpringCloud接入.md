## 操作场景

本文通过一个 demo 进行 Spring Cloud 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建 PolarisMesh 服务治理中心，请参见 [创建 PolarisMesh 治理中心](https://cloud.tencent.com/document/product/1364/65866)。
- 下载 Github 的 [demo 源码](https://github.com/Tencent/spring-cloud-tencent/tree/main/spring-cloud-tencent-examples/polaris-quickstart-example) 到本地并解压。
- 本地编译构建打包机器环境已安装了Java JDK、Maven，并且能够访问 Maven 中央库。
- 根据您自身的业务，已准备好业务部署的资源，```虚拟机部署```、```容器化部署```和```TEM部署```选择其中一种方式即可。
  - **虚拟机部署**已创建 CVM 虚拟机，请参见 [创建 CVM 虚拟机](https://cloud.tencent.com/document/product/213/2936)。
  - **容器化部署**已创建 TKE 容器集群，请参见 [创建 TKE 集群](https://cloud.tencent.com/document/product/457/32189)。
  - **TEM部署**已创建TEM环境，请参见[创建TEM环境](https://cloud.tencent.com/document/product/1371/53293)。

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**治理中心**下的 **polarismesh** 页面，单击页面左上方下拉列表，选择目标地域。
3. 单击目标引擎的“ID”，进入基本信息页面。
4. 查看访问地址，Spring Cloud 应用访问使用 gRPC 端口（8091）：
![](https://qcloudimg.tencent-cloud.cn/raw/e7dc5ac5f7c76a316ae68b667d8a365f.png)
5. 修改 demo 中的注册中心地址。
  1. 在下载到本地的 [demo 源码目录](https://github.com/Tencent/spring-cloud-tencent/tree/main/spring-cloud-tencent-examples/polaris-quickstart-example) 下，分别找到
    `spring-cloud-tencent-examples\polaris-quickstart-example\quickstart-provider\src\main\resources\bootstrap.yml`和`spring-cloud-tencent-examples\polaris-quickstart-example\quickstart-consumer\src\main\resources\bootstrap.yml`两个文件。
  - 添加微服务引擎服务治理中心地址到项目配置文件中（以`\polaris-quickstart-example\quickstart-provider\src\main\resources\bootstrap.yml`为例）。
<dx-codeblock>
:::  yaml
server:
  port: 0
spring:
  application:
    name: EchoServer
  cloud:
    polaris:
      address: grpc://10.0.4.6:8091
:::
</dx-codeblock>
6. 打包 demo 源码成jar包。
  1. 在 polaris-quickstart-example 源码根目录下，打开 cmd 命令，执行 mvn clean package 命令，对项目进行打包编译。
  - 编译成功后，生成如下表所示的2个 Jar 包。
<table>
<tr>
<th>软件包所在目录</th>
<th>软件包名称</th>
<th>说明</th>
</tr>
<tr>
<td>\polaris-quickstart-example\quickstart-provider\target</td>
<td>quickstart-provider-${version}-SNAPSHOT.jar</td>
<td>服务生产者</td>
</tr>
<tr>
<td>\polaris-quickstart-example\quickstart-consumer\target</td>
<td>quickstart-consumer-${version}-SNAPSHOT.jar</td>
<td>服务消费者</td>
</tr>
</table>    
7. 部署 provider 和 consumer 微服务应用，虚拟机部署方式和容器化部署根据您业务实际的部署方式选择一种即可。
 1. **虚拟机部署**部署 provider 和 consumer 微服务应用。
      - 上传 Jar 包至 CVM 实例。
      - 执行启动命令进行启动：
<dx-codeblock>
:::  shell
    nohup java -Djava.security.egd=file:/dev/./urandom -jar [jar包名称] &
:::
</dx-codeblock>        
 2. **容器化部署**部署provider和consumer微服务应用。
      - 编写dockerfile生成镜像，参考：
<dx-codeblock>
:::  shell
     FROM java:8
     ADD quickstart-consumer-${version}-SNAPSHOT.jar /root/app.jar
     ENTRYPOINT  ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/root/app.jar"]
:::
</dx-codeblock>        
      - 通过TKE部署并运行镜像

 3. **TEM部署**部署provider和consumer微服务应用。
   
     - 选择TEM环境，注意所选择的环境，其依赖的VPC，必须和上面已经创建的治理中心实例所依赖的VPC一致：
       ![](https://qcloudimg.tencent-cloud.cn/raw/15e364b650b20f0ea13943b3943b2a31.png)
   
     - 在已选择的环境中，新建TEM应用，相关参数填写参考：
       ![](https://qcloudimg.tencent-cloud.cn/raw/b9c236e4b0182b7f1c51cf3a4a51e0ab.png)
     
     - 部署应用，相关参数填写请参考（端口号映射，需要填写bootstrap.yml中声明的端口号）：
       ![](https://qcloudimg.tencent-cloud.cn/raw/b61962317531b128b15361c13291dbdf.png)
       
     - 查看访问路径，consumer应用部署完后，可以在**基本信息** > **访问配置**中查看访问地址，如需公网访问，可以**编辑并更新**开启公网访问。
       ![](https://qcloudimg.tencent-cloud.cn/raw/ca59fd27f26e437d7715e1d3299b50bc.png)


8. 确认部署结果。
 1. 进入前面提到的微服务治理中心实例页面。
 - 选择**服务管理** > **服务列表**，查看微服务 EchoServer（quickstart-provider）和 EchoClient（quickstart-consumer）的实例数量：
    - 若实例数量值不为0，则表示已经成功接入微服务引擎。
    - 若实例数量为0，或者找不到 EchoServer 和 EchoClient 服务名，则表示微服务应用接入微服务引擎失败。
![echo_service_list](https://qcloudimg.tencent-cloud.cn/raw/7a14162d53b611fcbec6d05c7986e751.png)

 2. 调用consumer的HTTP接口
 - 执行http调用，其中${app.port}替换为consumer的监听端口，${add.address}则替换为consumer暴露的地址：
<dx-codeblock>
:::  shell
    curl -L -X GET 'http://${add.address}:${app.port}/echo?value="hello-world'
    预期返回值：hello-world
:::
</dx-codeblock>
