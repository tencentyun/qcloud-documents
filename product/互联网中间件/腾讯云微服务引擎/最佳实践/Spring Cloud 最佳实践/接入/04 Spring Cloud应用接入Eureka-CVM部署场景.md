## 操作场景

本文以一对 Demo 示例（包含一个 provider 应用和一个 consumer 应用）介绍如何将通过 CVM 部署的 Spring Cloud 应用接入微服务引擎托管的 Eureka 注册中心，并实现简单的服务访问。帮助您快速了解如何使用 TSE Eureka 注册中心。





## 前提条件

- 已创建 TSE Eureka 注册中心，请参见 [引擎管理](https://cloud.tencent.com/document/product/1364/58408)。

- 已 [购买云服务器 CVM](https://buy.cloud.tencent.com/cvm)，且云服务器所在的私有网络 VPC 与 Eureka 注册中心所在的 VPC 相同。

- 下载 Github 的 [Demo 源码](https://github.com/tencentyun/tse-simple-demo) 到本地并解压。

- 本地编译构建打包机器环境已安装了 Java JDK、Maven，并且能够访问 Maven 中央库。

  

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。

2. 单击已创建的引擎实例的“ID”，进入基本信息页面，可以获取 Eureka 注册中心实例访问 IP。

   ![](https://qcloudimg.tencent-cloud.cn/raw/5c8c38057973e961cceb90a37eaee475.png)

3. 进入下载好 Demo 源码目录。

4. 打包 demo 源码成 jar 包。在`tse-simple-demo-main`源码根目录下，打开终端窗口，执行 mvn clean package 命令，对项目进行打包编译。编译成功后，可以在如下目录看到生成如下表所示的2个 Eureka Jar 包。

   | 软件包所在目录                                        | 软件包名称                                | 说明       |
   | :---------------------------------------------------- | :---------------------------------------- | :--------- |
   | \tse-simple-demo-main\tse-eureka-provider-demo\target | tse-eureka-provider-demo-1.0-SNAPSHOT.jar | 服务生产者 |
   | \tse-simple-demo-main\tse-eureka-consumer-demo\target | tse-eureka-consumer-demo-1.0-SNAPSHOT.jar | 服务消费者 |

5. 将编译好的 jar 包上传至云服务器，详细操作请参考[如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。

6. 登录云服务器，进入到刚刚上传 jar 文件所在的目录，可看到文件已上传到云服务器。

   ![](https://qcloudimg.tencent-cloud.cn/raw/d965c1c42e5cf0bf84f5e828150754ff.png)

7. 执行如下命令指定注册中心地址参数并运行该应用。

   ```java
   nohup java -Deureka.client.serviceUrl.defaultZone=http://[TSE Eureka注册中心实例访问IP:8761]/eureka/ -jar [jar包名称] &
   ```

8. 运行成功后，登录 [TSE 控制台](https://console.cloud.tencent.com/tse)，在左侧导航栏选择 **eureka**，单击目标实例的 ID，进入基本信息页面。

9. 在页面上方选择**服务管理**页签，若出现以下页面，则证明服务注册成功。

   ![](https://qcloudimg.tencent-cloud.cn/raw/4370ee6adfad687289c3d48f35f2e5ac.png)

10. 登录云服务器，执行如下命令，调用 consumer 接口访问 provider 服务。

       ```
    curl localhost:18082/ping-provider/test
       ```

       运行结果如下：

       ![](https://qcloudimg.tencent-cloud.cn/raw/bee048fd516134a165f7ee3dc23b1de1.png)






## 注意事项

Spring Cloud 应用接入 eureka 注册中心，配置文件格式需如下所示：
<dx-codeblock>
:::  PLAINTEXT
eureka:
  client:
    serviceUrl:
      defaultZone: http://[TSE Eureka注册中心实例访问IP:8761]/eureka/
  instance:
    prefer-ip-address: true
:::
</dx-codeblock>



