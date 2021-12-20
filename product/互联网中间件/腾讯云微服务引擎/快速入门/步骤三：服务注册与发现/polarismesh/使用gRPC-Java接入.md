## 操作场景

本文通过一个demo进行 gRPC-Java 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何使用服务治理中心。

## 前提条件

- 已创建PolarisMesh服务治理中心，请参考[创建PolarisMesh治理中心](https://cloud.tencent.com/document/product/1364/65866)。
- 下载github的[demo源码](https://github.com/polarismesh/grpc-java-polaris/tree/main/grpc-java-polaris-examples/quickstart-example)到本地并解压。
- 本地编译构建打包机器环境已安装了Java JDK、Maven，并且能够访问Maven中央库。
- 根据您自身的业务，已准备好业务部署的资源，虚拟机部署和容器化部署选择其中一种方式即可。
  - 【虚拟机部署】已创建CVM虚拟机，请参考[创建CVM虚拟机](https://cloud.tencent.com/document/product/213/2936)
  - 【容器化部署】已创建TKE容器集群，请参考[创建 TKE 集群](https://cloud.tencent.com/document/product/457/32189)。

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**治理中心**下的 **polarismesh** 页面，点击页面上方下拉列表，选择目标地域：![region_icon](https://qcloudimg.tencent-cloud.cn/raw/b5153fa452844ee19e24436e11b2376e.png)
3. 单击目标引擎的“ID”，进入基本信息页面。
4. 查看访问地址，Spring Cloud应用访问使用gRPC端口（8091）：
   ![access](https://qcloudimg.tencent-cloud.cn/raw/561460943b0404c44c29d2c0dd09c56f.png)
5. 修改demo中的注册中心地址。
  - 在下载到本地的[demo源码](https://github.com/polarismesh/grpc-java-polaris/tree/main/grpc-java-polaris-examples/quickstart-example)目录下，分别找到
“\grpc-java-polaris-examples\quickstart-example\provider\src\main\resources\polaris.yml”和“\grpc-java-polaris-examples\quickstart-example\consumer\src\main\resources\polaris.yml”两个文件。
  - 添加微服务引擎服务治理中心地址到项目配置文件中（以“\grpc-java-polaris-examples\quickstart-example\provider\src\main\resources\polaris.yml”为例）。
```yml
global:
  serverConnector:
    addresses:
    - 192.168.100.9:8091
```

6. 将源码编译成可执行程序。

  - 在quickstart-example源码根目录下，打开cmd命令，执行mvn clean package命令，对项目进行打包编译。
  - 编译成功后，生成如表1所示的2个二进制包。
    表1 软件包列表

| 软件包所在目录                                         | 软件包名称                                  | 说明       |
| ------------------------------------------------------ | ------------------------------------------- | ---------- |
| \grpc-java-polaris-examples\quickstart-example\provider\target | quickstart-provider | 服务生产者 |
| \grpc-java-polaris-examples\quickstart-example\consumer\target | Quickstart-consumer | 服务消费者 |

7. 部署provider和consumer微服务应用，虚拟机部署方式和容器化部署根据您业务实际的部署方式选择一种即可。

    （1）【虚拟机部署】部署provider和consumer微服务应用。

     - 上传  Jar 包至 CVM 实例。

     - 执行启动命令进行启动：

    ```shell
    nohup java -Djava.security.egd=file:/dev/./urandom -jar [jar包名称] &
    ```

    （2）【容器化部署】部署provider和consumer微服务应用。

    - 编写dockerfile生成镜像，参考：
    ```
    FROM java:8
    ADD quickstart-provider-${version}-SNAPSHOT.jar /root/app.jar
    ENTRYPOINT  ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/root/app.jar"]
    ```
     - 通过TKE部署并运行镜像

8. 确认部署结果。

 - 进入前面提到的微服务治理中心实例页面。

 - 选择“服务管理 > 服务列表”，查看微服务EchoServerGRPCJava的实例数量：

 - 若实例数量值不为0，则表示已经成功接入微服务引擎。

 - 若实例数量为0，或者找不到EchoServerGRPCJava服务名，则表示微服务应用接入微服务引擎失败。

   ![](https://qcloudimg.tencent-cloud.cn/raw/86d397ddba81b5dfdb54a6771e5e53c2.png)

 - 调用consumer的HTTP接口
   - 执行http调用，其中${app.port}替换为consumer的监听端口（默认为40041），${add.address}则替换为consumer暴露的地址。
    ```
    curl -L -X GET 'http://${add.address}:${app.port}/polaris/grpc/quickstart/consumer?value="hello-polaris'
    预期返回值：hello-polaris
    ```

