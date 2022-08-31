## 操作场景

本文以一对 Demo 示例（包含一个 provider 应用和一个 consumer 应用）介绍如何将通过 CVM 部署的 Spring Cloud 应用接入微服务引擎托管的 ZooKeeper 注册中心，并实现简单的服务访问。帮助您快速了解如何使用 TSE ZooKeeper 注册中心。





## 前提条件

- 已创建 TSE ZooKeeper 注册中心，请参见 [引擎管理](https://cloud.tencent.com/document/product/1364/58416)。
- 已 [购买云服务器 CVM](https://buy.cloud.tencent.com/cvm)，且云服务器所在的私有网络 VPC 与 ZooKeeper 注册中心所在的 VPC 相同。
- 下载 Github 的 [Demo 源码](https://github.com/tencentyun/tse-simple-demo) 到本地并解压。
- 本地编译构建打包机器环境已安装了Java JDK、Maven，并且能够访问 Maven 中央库。

  

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 单击已创建的引擎实例的“ID”，进入基本信息页面。
3. 在页面上方选择“访问管理”页签，可以获取 Zookeeper 注册中心实例访问 IP。
   ![](https://qcloudimg.tencent-cloud.cn/raw/ad047b6e0ddd98dc00ac83056e265a0c.png)
4. 进入下载好 Demo 源码目录。
5. 打包 Demo 源码成 jar 包。在`tse-simple-demo-main`源码根目录下，打开终端窗口，执行 mvn clean package 命令，对项目进行打包编译。编译成功后，可以在如下目录看到生成如下表所示的2个ZooKeeper Jar 包。
<table>
<thead>
<tr>
<th align="left">软件包所在目录</th>
<th align="left">软件包名称</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">\tse-simple-demo-main\tse-zookeeper-provider-demo\target</td>
<td align="left">tse-zookeeper-provider-demo-1.0-SNAPSHOT.jar</td>
<td align="left">服务生产者</td>
</tr>
<tr>
<td align="left">\tse-simple-demo-main\tse-zookeeper-consumer-demo\target</td>
<td align="left">tse-zookeeper-consumer-demo-1.0-SNAPSHOT.jar</td>
<td align="left">服务消费者</td>
</tr>
</tbody></table>
6. 将编译好的 jar 包上传至云服务器，详细操作请参见 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。
7. 登录云服务器，进入到刚刚上传 jar 文件所在的目录，可看到文件已上传到云服务器。
   ![](https://qcloudimg.tencent-cloud.cn/raw/df475b80a342dd4b47785a2c9f406973.png)
8. 执行如下命令指定注册中心地址参数并运行该应用。
   ```java
   nohup java -Dspring.cloud.zookeeper.connect-string=[TSE Zookeeper注册中心实例访问IP:2181] -jar [jar包名称] &
   ```
9. 运行成功后，登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。进入注册中心实例的服务管理页面，若出现以下页面，则证明服务注册成功。
   ![](https://qcloudimg.tencent-cloud.cn/raw/b142bd6968d9d074821b464cb4d8e7e2.png)
10. 登录云服务器，执行如下命令，调用 consumer 接口访问 provider 服务。
       ```curl
    curl localhost:19001/ping/test
       ```
       返回结果如下：
       ![](https://qcloudimg.tencent-cloud.cn/raw/1d72b1c1c20c12c4b31cf0c11ad14a04.png)


## 注意事项

Spring Cloud 应用接入 Zookeeper 注册中心，配置文件格式需如下所示：
<dx-codeblock>
:::  plaintext
spring:
  cloud:
    zookeeper:
      connect-string: [zookeeper注册中心IP:2181]
      discovery:
        register: true
        enabled: true
        prefer-ip-address: true
:::
</dx-codeblock>
