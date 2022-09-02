为了帮助您快速体验如何将应用接入 TSE Nacos 注册中心，本文以一对 Demo 示例（包含一个 provider 应用和一个 consumer 应用）介绍如何将通过 CVM 部署的 Spring Cloud 应用接入微服务引擎托管的 Nacos 注册中心，并实现简单的服务访问。



## 前提条件

- 已 [获取访问授权](https://cloud.tencent.com/document/product/1364/56268)
- 已 [购买云服务器](https://buy.cloud.tencent.com/cvm)



## 步骤1：创建 Nacos 引擎实例

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在左侧导航栏，单击 **nacos**，进入 Nacos 注册中心页面，单击**新建**进入购买页。
3. 在实例购买页，根据自身业务需求选择购买信息。
   <table>
   <thead>
   <tr>
   <th>参数</th>
   <th>说明</th>
   </tr>
   </thead>
   <tbody><tr>
   <td>计费模式</td>
   <td>支持<b>包年包月</b>和<b>按量付费</b>两种计费方式，如果您的服务注册中心使用时间在一个月以上，建议采用预付费（包年包月）模式。具体价格请参见 <a href="https://cloud.tencent.com/document/product/1364/75459">Nacos 产品版本和价格说明</a>。</td>
   </tr>
   <tr>
   <td>地域</td>
   <td>选择与您部署业务最靠近的地域。</td>
   </tr>
   <tr>
   <td>开源版本</td>
   <td>支持 2.0.3，版本兼容性说明请参见 <a href="https://cloud.tencent.com/document/product/1364/78717">Nacos 版本兼容性说明</a>。</td>
   </tr>
   <tr>
   <td>产品版本</td>
   <td>根据需要选择专业版或开发版，开发版用于开发自测或产品体验场景，不可用于生产环境。关于开发版，标准版的区别请参见 <a href="https://cloud.tencent.com/document/product/1364/75459#.E4.BA.A7.E5.93.81.E7.89.88.E6.9C.AC">版本对比</a>。</td>
   </tr>
   <tr>
   <td>规格</td>
   <td><ul><li>开发版：支持1C1G。建议仅用于体验。开发版没有容灾能力。</li>
   <li>标准版：支持1C2G、2C4G、4C8G、8C16G、16C32G。可用于测试、生成环境。支持多节点部署。</li></ul>请您根据实际情况选择合适的组件规格，关于组件的评估方法，请参见 <a href="https://cloud.tencent.com/document/product/1364/75460">Nacos 性能评估</a>。</td>
   </tr>
   <tr>
   <td>节点数</td>
   <td>即一个集群需要多少台上述规格的节点组成。<ul><li>开发版：1节点。</li>
   <li>标准版：可选3、5、7节点。</li></ul></td>
   </tr>
   <tr>
   <td>部署架构</td>
   <td><ul><li>开发版：同城单可用区。</li>
   <li>标准版：同城三可用区，提供高可用版注册中心，默认支持同城多活。</li></ul></td>
   </tr>
   <tr>
   <td>集群网络</td>
   <td>所选择的私有网络必须和已购买的云服务器 CVM 所在的私有网络一致。所选择的子网不用和云服务所在的私有网络一致。</td>
   </tr>
   <tr>
   <td>名称</td>
   <td>最长60个字符，支持中英文大小写、-、_，名称一旦创建后不支持修改。</td>
   </tr>
   <tr>
   <td>资源标签</td>
   <td>用于分类管理资源，选填，具体使用方法可参见 <a href="https://cloud.tencent.com/document/product/1364/74387">标签管理</a>。</td>
   </tr>
   </tbody></table>
4. 单击**创建**，完成引擎创建。创建完成后单击引擎实例的“ID”，进入基本信息页面，选择**访问控制**页签可以获取 Nacos 注册中心实例访问 IP。
   ![](https://qcloudimg.tencent-cloud.cn/raw/e9a4b2e4430d337c153abc09a6bccf32.png)



## 步骤2：应用接入

> ?此处以云服务器 CVM 部署的 Spring Cloud 应用为例介绍接入 TSE Nacos 注册中心实例的流程，其他使用场景如 TKE、TEM 部署请参见 [Spring Cloud 应用接入]()。

1. 下载 Github 的 [Demo 源码](https://github.com/tencentyun/tse-simple-demo) 到本地并解压。
2. 打包 demo 源码成 jar 包。在`tse-simple-demo-main`源码根目录下，打开终端窗口，执行 mvn clean package 命令，对项目进行打包编译。编译成功后，可以在如下目录看到生成如下表所示的2个 Nacos Jar 包。
<table>
<thead>
<tr>
<th align="left">软件包所在目录</th>
<th align="left">软件包名称</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">\tse-simple-demo-main\nacos-spring-cloud-provider-example\target</td>
<td align="left">nacos-provider-demo.jar</td>
<td align="left">服务生产者</td>
</tr>
<tr>
<td align="left">\tse-simple-demo-main\nacos-spring-cloud-consumer-example\target</td>
<td align="left">nacos-consumer-demo.jar</td>
<td align="left">服务消费者</td>
</tr>
</tbody></table>
3. 将编译好的 jar 包上传至云服务器，详细操作请参见 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。
4. 登录云服务器，进入到刚刚上传 jar 文件所在的目录，可看到文件已上传到云服务器。
   ![](https://qcloudimg.tencent-cloud.cn/raw/3b9493990f93e9bc46c8b4d55a3c5ccd.png)
5. 执行如下命令指定注册中心地址参数并运行该应用。
<dx-codeblock>
:::  java
nohup java -Dspring.cloud.nacos.discovery.server-addr=[TSE Zookeeper注册中心实例访问IP:8848] -jar [jar包名称] &
:::
</dx-codeblock>



## 步骤3：验证服务注册成功

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在左侧导航栏选择 **nacos**，单击目标实例的 ID，进入基本信息页面。
3. 在页面上方选择**访问控制**页签，找到控制台访问的公网地址和登录用户名密码，通过 web 访问 Nacos 原生控制台。
   ![](https://qcloudimg.tencent-cloud.cn/raw/c23a003df4bf59c8ae9dc47bc319a169.png)
4. 在 Nacos 原生控制台页面，选择**服务管理** > **服务列表**，可以看到注册成功的服务。
   ![](https://qcloudimg.tencent-cloud.cn/raw/5427e1686636a78f81f713d145342e19.png)
5. 登录云服务器，执行如下命令，调用 consumer 接口访问 provider 服务。
<dx-codeblock>
:::  curl
 curl localhost:8080/echo/str
:::
</dx-codeblock>
   运行结果如下：
<img src="https://qcloudimg.tencent-cloud.cn/raw/bd57a6f417e29dcd063081217e267180.png" alt=""> 
