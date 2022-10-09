## 操作场景

本文以一对 Demo 示例（包含一个 provider 应用和一个 consumer 应用）介绍如何将通过 CVM 部署的 Spring Cloud 应用接入微服务引擎托管的 Nacos 注册中心，并实现简单的服务访问。帮助您快速了解如何使用 TSE Nacos 注册中心。





## 前提条件

- 已创建 TSE Nacos 注册中心，请参见 [引擎管理](https://cloud.tencent.com/document/product/1364/63997)。
- 已 [购买云服务器 CVM](https://buy.cloud.tencent.com/cvm)，且云服务器所在的私有网络 VPC 与 Nacos 注册中心所在的 VPC 相同。
- 下载 Github 的 [Demo 源码](https://github.com/tencentyun/tse-simple-demo) 到本地并解压。
- 本地编译构建打包机器环境已安装了Java JDK、Maven，并且能够访问 Maven 中央库。

  

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 单击已创建好的 Nacos 引擎实例的“ID”，进入基本信息页面.
3. 在页面上方选择"访问控制"页签，可以获取 Nacos 注册中心实例访问 IP。
   ![](https://qcloudimg.tencent-cloud.cn/raw/ad047b6e0ddd98dc00ac83056e265a0c.png)
4. 进入下载好的 Demo 源码目录。
5. 打包 Demo 源码成 jar 包。在`tse-simple-demo-main`源码根目录下，打开终端窗口，执行 `mvn clean package` 命令，对项目进行打包编译。编译成功后，可以在如下目录看到生成如下表所示的2个 Nacos Jar 包。
<table>
<thead>
<tr>
<th align="left">软件包所在目录</th>
<th align="left">软件包名称</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">tse-nacos-spring-cloud-provider-demo\target</td>
<td align="left">tse-nacos-spring-cloud-provider-demo-2.0.1.RELEASE.jar</td>
<td align="left">服务生产者</td>
</tr>
<tr>
<td align="left">tse-nacos-spring-cloud-consumer-demo\target</td>
<td align="left">tse-nacos-spring-cloud-consumer-demo-2.0.1.RELEASE.jar</td>
<td align="left">服务消费者</td>
</tr>
</tbody></table>
6. 将编译好的 jar 包上传至云服务器，详细操作请参见 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。
7. 登录云服务器，进入到刚刚上传 jar 文件所在的目录，可看到文件已上传到云服务器。
   ![](https://qcloudimg.tencent-cloud.cn/raw/3b9493990f93e9bc46c8b4d55a3c5ccd.png)
8. 执行如下命令指定注册中心地址参数并运行该应用。
   ```java
   nohup java -Dspring.cloud.nacos.discovery.server-addr=[TSE Zookeeper注册中心实例访问IP:8848] -jar [jar包名称] &
   ```
9. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)，在左侧导航栏选择 **nacos**，单击目标实例的 ID，进入基本信息页面。
10. 在页面上方选择**访问控制**页签，找到控制台访问的公网地址和登录用户名密码，通过 web 访问 Nacos 原生控制台。
![](https://qcloudimg.tencent-cloud.cn/raw/c23a003df4bf59c8ae9dc47bc319a169.png)
11. 在 Nacos 原生控制台页面，选择**服务管理** > **服务列表**，可以看到注册成功的服务。
      ![](https://qcloudimg.tencent-cloud.cn/raw/5427e1686636a78f81f713d145342e19.png)
12. 登录云服务器，执行如下命令，调用 consumer 接口访问 provider 服务。
    ```curl
    curl localhost:8080/echo/str
    ```
       运行结果如下：
       ![img](https://qcloudimg.tencent-cloud.cn/raw/bd57a6f417e29dcd063081217e267180.png)






