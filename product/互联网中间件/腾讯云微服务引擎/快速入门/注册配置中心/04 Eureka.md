为了帮助您快速体验如何将应用接入 TSE Eureka 注册中心，本文以一对 Demo 示例（包含一个 provider 应用和一个 consumer 应用）介绍如何将通过 CVM 部署的 Spring Cloud 应用接入微服务引擎托管的 Eureka 注册中心，并实现简单的服务访问。



## 前提条件

- 已 [获取访问授权](https://cloud.tencent.com/document/product/1364/56268)
- 已 [购买云服务器](https://buy.cloud.tencent.com/cvm)



## 步骤1：创建 Eureka 引擎实例

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在左侧导航栏，单击 **eureka**，进入 Eureka 注册中心页面，单击**新建**。
3. 根据自身业务需求选择购买信息。
   <table>
   <thead>
   <tr>
   <th>参数</th>
   <th>说明</th>
   </tr>
   </thead>
   <tbody><tr>
   <td>注册中心名称</td>
   <td>最长60个字符，支持中英文大小写，-，_。</td>
   </tr>
   <tr>
   <td>类型</td>
   <td>eureka</td>
   </tr>
   <tr>
   <td>版本</td>
   <td>支持 1.10.11。</td>
   </tr>
   <tr>
   <td>规格</td>
   <td>可选1C1G，1C2G，2C4G，4C8G，8C16G，16C32G。</td>
   </tr>
   <tr>
   <td>节点数</td>
   <td>即一个集群需要多少台上述规格的节点组成，可选3、4、5。</td>
   </tr>
   <tr>
   <td>引擎所在地域</td>
   <td>选择最靠近您目标客户的地域。</td>
   </tr>
   <tr>
   <td>集群网络</td>
   <td>所选择的私有网络必须和已购买的云服务器 CVM 所在的私有网络一致。所选择的子网不用和云服务器所在的私有网络一致。</td>
   </tr>
   <tr>
   <td>开启公网访问</td>
   <td>TSE 外网访问仅用于开发调试或辅助管理，业务访问请使用内网访问，避免外网访问的潜在安全风险。</td>
   </tr>
   <tr>
   <td>标签管理</td>
   <td>用于分类管理资源，选填，具体使用方法可参见 <a href="https://cloud.tencent.com/document/product/1364/74387">标签管理</a></td>
   </tr>
   </tbody></table>
4. 单击**创建**，完成引擎创建。创建完成后单击引擎实例的“ID”，在基本信息页面的接入方式栏可以获取 Eureka 注册中心实例访问 IP。
   ![](https://qcloudimg.tencent-cloud.cn/raw/5c8c38057973e961cceb90a37eaee475.png)



## 步骤2：应用接入

> ?此处以云服务器 CVM 部署的 Spring Cloud 应用为例介绍接入 TSE Eureka 注册中心实例的流程，其他使用场景如 TKE、TEM 部署请参见 [Spring Cloud 应用接入]()。

1. 下载 Github 的 [Demo 源码](https://github.com/tencentyun/tse-simple-demo) 到本地并解压。
2. 打包 demo 源码成 jar 包。在`tse-simple-demo-main`源码根目录下，打开终端窗口，执行 mvn clean package 命令，对项目进行打包编译。编译成功后，可以在如下目录看到生成如下表所示的2个 Eureka Jar 包。
<table>
<thead>
<tr>
<th align="left">软件包所在目录</th>
<th align="left">软件包名称</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">\tse-simple-demo-main\tse-eureka-provider-demo\target</td>
<td align="left">tse-eureka-provider-demo-1.0-SNAPSHOT.jar</td>
<td align="left">服务生产者</td>
</tr>
<tr>
<td align="left">\tse-simple-demo-main\tse-eureka-consumer-demo\target</td>
<td align="left">tse-eureka-consumer-demo-1.0-SNAPSHOT.jar</td>
<td align="left">服务消费者</td>
</tr>
</tbody></table>
3. 将编译好的 jar 包上传至云服务器，详细操作请参见 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。
4. 登录云服务器，进入到刚刚上传 jar 文件所在的目录，可看到文件已上传到云服务器。
   ![](https://qcloudimg.tencent-cloud.cn/raw/d965c1c42e5cf0bf84f5e828150754ff.png)
5. 执行如下命令指定注册中心地址参数并运行该应用。
   ```java
   nohup java -Deureka.client.serviceUrl.defaultZone=http://[TSE Eureka注册中心实例访问IP:8761]/eureka/ -jar [jar包名称] &
   ```



## 步骤3：验证服务注册成功

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在左侧导航栏选择 **eureka**，单击目标实例的 ID，进入基本信息页面。
3. 在页面上方选择**服务管理**页签，可以看到注册成功的服务。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4370ee6adfad687289c3d48f35f2e5ac.png)
4. 登录云服务器，执行如下命令，调用 consumer 接口访问 provider 服务。
   ```curl
   curl localhost:18082/ping-provider/test
   ```
   运行结果如下：
   ![](https://qcloudimg.tencent-cloud.cn/raw/bee048fd516134a165f7ee3dc23b1de1.png)
