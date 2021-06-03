通过 TAPM，您可以对腾讯云 Kubernetes 集群的应用进行应用拓扑、接口调用、异常、慢事务、SQL 分析等监控。本篇文章会帮助您将腾讯云 Kubernetes 集群中的应用接入 TAPM 系统。

## 前提条件
- 请确保您集群中部署的应用系统满足 Java 应用探针的 [Java 应用探针的相关限制](https://cloud.tencent.com/document/product/1349/52912)。
- 确保您的集群连通公网。
- 了解 K8s&Docker 运行原理、镜像创建等基本操作。
- 在部署探针前，需要先确保本地浏览器时间与服务器时区、时间都一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 如果您配置了防火墙，需要将 Agent Collector 的 IP 地址和端口添加到许可列表。如果涉及高可用部署，请务必将所有的 IP 地址和端口都配入。
- 如果您的 host 或者 collector.addresses 配置的是域名，可以使用 dig 命令查看 IP，请在 Linux 控制台输入以下命令：
  ```
  dig ap-guangzhou.tapm.tencentcs.com
  ```
  >?如果 **dig** 命令无法使用，可能是还没有安装该命令。 **dig** 是 **bind** 的一部分，您可以尝试安装一下 bind-utils 。如果您使用的是 yum ，请运行 **yum install bind-utils** 命令。

## 操作步骤
- 以下部署过程的介绍，是基于 Tomcat 服务开发的一个项目，而非单纯的 Tomcat 服务。
- 以下介绍中，基础镜像所在环境系统为 CentOS 。其他操作系统如 RedHat、Ubuntu、Debian 同样可基于以下步骤作为参考。

在腾讯云 K8s 的容器中部署 Java 应用探针的步骤如下：
1. 登录容器所在的云服务器。
2. 通过 Wget 方式下载探针。
	```
	 wget https://tapm-agent-1303913924.cos.ap-guangzhou.myqcloud.com/tapm-agent-java-3.5.3.zip
	 ```
3. 解压缩安装文件包到您的应用服务器的指定目录。
 ```
 unzip tapm-agent-java-xxx.zip -d /{workspace}/
 ```
4. 修改放在服务器解压的 tapm 目录下 tapm.properties 文件。
   修改文件中的 license_key、app_name 和 collector.addresses 配置项，否则探针无法进行数据采集也无法启动探针。对于其他配置项，请根据实际需要进行配置。
   - license_key：与您的应用性能监控 TAPM 账号关联。探针采集到的数据，会上传到该 LicenseKey 绑定的账号下。
   - app_name：缺省应用名称，建议配置为应用的业务名称。
   - collector.addresses：Agent Collector 服务器的地址和端口号，例如：tapm.ap-guangzhou.api.tencentyun.com。
5. 将 {workspace} 挂载到容器中，并且在应用镜像的 YAML 配置文件中配置 `-javaagent` 。
   ```
   -javaagent:{workspace}/tapm/tapm-agent-java.jar
   ```
   ![](https://main.qcloudimg.com/raw/f46705ca9fa800f36dd54532aaff5ba4.png)
6. 重启腾讯云容器服务，查看探针日志和控制台，观察性能数据上传是否正常。
>?大约5分钟后，若您的应用出现在 TAPM 控制台的业务系统列表或应用列表中且有数据上报，则说明接入成功。
