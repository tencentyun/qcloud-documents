
> ?
> 尊敬的用户您好，TSF Serveless 进行了能力升级，全新推出独立产品**弹性微服务 TEM**。 弹性微服务是微服务应用托管 Serverless 平台，主要提供微服务应用的应用托管、发布管理、弹性伸缩、云资源（如微服务、中间件）的联结插拔等能力。
>
> 我们建议您开通弹性微服务并进行能力迁移，有关更多弹性微服务的信息，您可以查看 [弹性微服务](https://cloud.tencent.com/product/tem) 官网。
>
> [点击体验弹性微服务 >>](https://console.cloud.tencent.com/tem)
>
> 若您有其他疑问，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们，将有工程师为您服务。

## 监听端口

- 如果您的业务是微服务（Spring、Mesh），则无需考虑端口监听问题。
- 如果您的业务是 Web 服务，您的服务需要**主动监听8080端口**。

## 上传程序包要求

目前 Serverless 应用支持的程序包格式包括 **jar、war、tar.gz 和 zip**。

- jar： FatJar 格式的程序包，用户可以参考 [如何打 FatJar 包](https://cloud.tencent.com/document/product/649/16934)。
- war： war 格式的程序包，在部署 war 包时，TSF 会自动安装 Tomcat 环境。示例 [demo 下载](https://alon-deployment-gz-1257356411.cos.ap-guangzhou.myqcloud.com/sample.war) ，示例 demo 部署成功后，使用 `http://<IP>:8080/sample` 访问，其中 IP 可以是实例的外网 IP。
- tar.gz 、zip ： 压缩包中**必须**包含三个文件，**确保文件名正确**：
  - start.sh：启动脚本
  - stop.sh：停止脚本
  - cmdline：用于检查应用进程是否存在，**没有**`.sh`后缀

| 文件类型 | 启动方式                                                     |
| -------- | ------------------------------------------------------------ |
| war      | 云服务器上的 agent 会使用`java -jar`命令启动程序。           |
| jar      | 云服务器上的 agent 会使用`java -jar`命令启动程序。           |
| tar.gz   | 云服务器上的 agent 会解压压缩包，使用解压目录下的`start.sh`脚本启动应用程序。 |
| zip      | 云服务器上的 agent 会解压压缩包，使用解压目录下的`start.sh`脚本启动应用程序。 |

更多说明请参考 [上传程序包要求](https://cloud.tencent.com/document/product/649/30359)。

## 本地临时存储

- 如果您需要在本地写临时文件，推荐写到`/tmp`路径下，其他任意路径均可。
- `/tmp`路径下空间有限，您需要定时清理。

## 旧版部署组/应用迁移说明

为提供更好的服务并全面支持微服务平台相关能力，我们在 [1.19.0](https://cloud.tencent.com/document/product/649/19020) 版本中对 Serverless 应用及部署组进行了升级。关于历史部署组，您需要关注以下几点：

- 历史部署组上的业务可照常运行。但为了保证您能享受新版本功能，我们强烈建议您重新创建部署组，并对旧版部署组做迁移。具体操作请参考 [部署组迁移指引](#migrate)。
- [1.19.0](https://cloud.tencent.com/document/product/649/19020) 版本后默认历史集群不可新建部署组，请重新创建并选择新的集群进行操作。
- [1.19.0](https://cloud.tencent.com/document/product/649/19020) 版本后的访问管理入口将从**应用**迁移到**部署组**。
- 如果需要查看历史部署组的域名，您可以通过登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，基于 TSF 应用名查找对应 API 网关。
  例如：旧版应用名为 demo ，则对应 API 网关的默认域名为 `demo-<appid>.<region>.apigw.tencentcs.com`。
- [1.19.0](https://cloud.tencent.com/document/product/649/19020) 版本后 Serverless 应用的程序包需同时包含 start.sh、stop.sh、cmdline 三个文件，详见 [上传程序包要求](https://cloud.tencent.com/document/product/649/30359) 。

<span id="migrate"></span>

#### 部署组迁移指引

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index?rid=1)，在左侧导航栏单击**集群**，新建一个集群。详细操作可参考 [集群](https://cloud.tencent.com/document/product/649/13684) 文档。
   ![](https://main.qcloudimg.com/raw/ff452959fb414689c1f615d87dba5bd8.png)
2. 单击**部署组**，创建 Serverless 应用部署组。
   具体操作可参考 [Serverless 应用部署组](https://cloud.tencent.com/document/product/649/41099) 文档。**历史部署组不可直接创建 Serverless 集群**。
   ![](https://main.qcloudimg.com/raw/ad71fa4a932703ee598aa0f7419eba8a.png)
3. 部署 Serverless 应用。具体操作可参考 [Serverless 应用部署组](https://cloud.tencent.com/document/product/649/41099) 文档。
   ![](https://main.qcloudimg.com/raw/92c0af5aa842287b6152cb89c802b2ea.png)
4. 上传程序包。
   本次程序包上传必须同时**包含 start.sh、stop.sh、cmdline**，详情请参考 [上传程序包要求](https://cloud.tencent.com/document/product/649/30359)。
5. 开启外网访问。
   单击部署组 ID，在部署组详情页开启外网访问，即可在外网访问已迁移至部署组的服务。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/16f542ea30944c4bca95f4b15607a965.png)
