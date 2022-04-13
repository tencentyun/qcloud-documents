## 操作场景

在使用 [TKE 容器服务](https://console.cloud.tencent.com/tke2) 时，先前通常使用如下方法，来获取并查询部署的组件服务日志：

1. 从 **TKE 控制台** 登录容器节点，切换到日志所在文件夹并查看日志。
2. 从 **TKE 控制台** 查询重定向至标准输出的容器日志。
3. **SSH 终端** 登录集群节点，查询挂载在宿主机上的日志，或使用 Kubectl 登录容器查询日志。
4. 使用 **CLS 采集器** 采集日志，并在 [日志服务](https://console.cloud.tencent.com/cls) 的控制台查询。

与以上方法相比，采用 Kafka 采集器采集日志消息投递到 CKafka，进而对消息使用 DataHub 进行数据处理后，投递到 Elasticsearch Service 进行日志解析的方法，具有以下显著优势：

- 多点灾备：Kafka 原生提供数据持久化及灾备能力，不会因单节点宕机导致日志丢失。
- 日志区分：在每条日志消息中添加 [Metadata 信息](https://cloud.tencent.com/document/product/457/36771) ，增加解析信息能力。
- 精细解析：DataHub 提供 [数据处理](https://console.cloud.tencent.com/ckafka/datahub-process) 功能，能够结构化精细解析原始日志数据。
- 多元输出：DataHub 提供多种输出目标源，例如可以将 CKafka 的消息同时投递至 ElasticSearch 及 MongoDB，冷热数据分离节约成本。

## 运行原理

整个采集投递过程如下图所示，各个组件结构说明如下：
![](https://qcloudimg.tencent-cloud.cn/raw/dd61aad005a133c9723016c4782df96b.svg)

- TKE Kafka 采集器基于 Kubernetes 友好的开源 [fluent-bit](https://fluentbit.io/) 采集器编写，监听日志文件变动并投递到目标 Kafka。
- CKafka 数据处理组件采用自研架构，通过建立内置消费者订阅源主题数据，经过消息处理器清洗后投递到目标主题中。
- 数据流出 ES 基于 Kafka 原生 [Connect](https://kafka.apache.org/documentation.html#connect) 定制，通过实现 Connect 插件将消息流出至指定的 Elasticsearch Service。

## 前提条件

- 需开通 TKE 服务。
- 需开通 CKafka 服务。
- 需开通  Elasticsearch Service 服务。

## 操作步骤

### 步骤1：启用 TKE 日志采集投递

#### 启用日志采集

1. 登录 [TKE 控制台](https://console.cloud.tencent.com/tke2/cluster)。
2. 在左侧导航栏选择 **运维功能管理**，点击目标实例操作栏的**设置**按钮。
3. 勾选 **开启日志采集**，启用日志采集功能后确认。具体操作步骤可参考[配置日志采集文档](https://cloud.tencent.com/document/product/457/36771)。
   ![](https://qcloudimg.tencent-cloud.cn/raw/7e8c996db32b82e0f6f11a7c219b9049.png)
> ?
>
> 如果先前已经启用日志采集，需要将采集器版本更新到 `1.0.8.1` 及以上，更新后控制台展示信息如下所示：
> ![](https://qcloudimg.tencent-cloud.cn/raw/7a15303ed52bf1cb38ba6fbf0e7f7e13.png)

#### 创建日志规则

1. 在控制台选择左侧导航栏中的**运维功能管理** > **日志规则**。
2. 在**日志采集**页面上方选择地域和需要配置日志采集规则的集群，单击**新建**，随后进行日志规则的配置。
>?以容器内文件日志为例，下图表示创建了一个采集 nginx 容器中，路径为 `/var/log/test` 的文件夹下，所有后缀为 `.log` 的采集配置。
![](https://qcloudimg.tencent-cloud.cn/raw/fa548e5e10177b3f89b0c301c788cced.png)
3. 编辑采集配置后，选择投递到 Kafka 相应的实例及主题即可。

#### 查看采集结果

1. 以采集 Java 堆栈日志信息为例，在 TKE 控制台查看 kafkaListener 容器的标准输出。
![](https://qcloudimg.tencent-cloud.cn/raw/4d1f1ddc6e785c7e6bed63dbf4a3a62b.png)
发现有数据成功投递到目标 Kafka 的主题中，证明投递成功。
![](https://qcloudimg.tencent-cloud.cn/raw/a8d195069442acfcebc92229ab381b35.png)
2. 查看 CKafka 实例监控，可以得到当前日志采集的速度。
![](https://qcloudimg.tencent-cloud.cn/raw/0673bbf8e40229c708e5c3e11c5c5fe5.png)
3. 查看 CKafka 的目标主题 offset，可以得到当前消息投递的总数量。
![](https://qcloudimg.tencent-cloud.cn/raw/09bf73a61f8a8bc5ff78db1168c21615.png)
4. 在 CKafka 的 [消息查询](https://console.cloud.tencent.com/ckafka/message) 界面，输入主题的分区数和时间，得到完整的日志采集消息，可以发现消息中已添加关于集群的 Metadata 信息。
![](https://qcloudimg.tencent-cloud.cn/raw/6de44da536ee3b827abdb327d6a2fc4e.png)
	 

### 步骤2：DataHub 数据简单处理

#### 创建数据处理

DataHub 能够涵盖绝大部分的数据处理场景，由于数据处理方式取决于采集的源消息格式，因此此处仅使用简单的数据处理进行展示。

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka/)。
2. 在左侧导航栏选择 **数据处理**，单击 **新建任务**，在任务界面选择 **Json 解析模式**，将所需的嵌套 Metadata 信息转换为单层 Json 格式。
   ![](https://qcloudimg.tencent-cloud.cn/raw/26b40b081c3104d42d27c42e518e3a32.png)
3. 创建后，当数据处理概览页面中显示当前任务为健康状态时，代表数据处理处理正常。
![](https://qcloudimg.tencent-cloud.cn/raw/1a6fccc04d047ed4d933cc6b3901eccf.png)

#### 查看处理结果

1. 在消息处理概览页面进入任务界面，点击 **监控** 按钮，可以查询得到当前消息处理的速度。
![](https://qcloudimg.tencent-cloud.cn/raw/e2530ad10bec2328d6a8ac866df8bd7e.png)
2. 在 [消息查询](https://console.cloud.tencent.com/ckafka/message) 界面，查询目标主题消息如下图所示。从图中可见，处理后的消息，从复杂的 Metadata 中成功提取出了所需的关键部分。
![](https://qcloudimg.tencent-cloud.cn/raw/a8b95db5481a33782f0417505f6c5d3b.png)



### 步骤3：DataHub 数据投递

1. 在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka/) 左侧导航栏选择 **数据流出**。
2. 单击**新建任务**，目标类型选择 **Elasticsearch Service**，随后填写投递实例名称等信息。
3. 创建完成后，在数据流出任务列表如下图所示数据流出状态为健康时，代表任务创建成功。
![](https://qcloudimg.tencent-cloud.cn/raw/e8718cfa182e1f825b6fda29c6b4a5e9.png)
4. 在数据流出任务监控界面，可以获取当前投递到 Elasticsearch 的速度。
![](https://qcloudimg.tencent-cloud.cn/raw/0381fbb848c8ab931d3b580534c284f4.png)

### 步骤4：Elasticsearch 日志解析

1. 登录 [Elasticsearch 控制台](https://console.cloud.tencent.com/es) ，打开 Kibana 的公网访问功能，以便于设置索引。
![](https://qcloudimg.tencent-cloud.cn/raw/ee0c133ebd0729c030f851faf2b43a27.png)
2. 打开 Kibana 界面，在左侧导航栏中依次选择 **Kibana** > **Discover**，进入 **Index Pattern**界面。
3. 在索引页面创建能够匹配先前数据流出的索引，索引的数据类型由 Kibana 自动解析生成。
<dx-alert infotype="notice" title="">
通过 **消息流出** 导入 Elasticsearch 中的消息，索引为消息所对应的 CKafka 实例的 **主题名称**。 
</dx-alert>
<img src = "https://qcloudimg.tencent-cloud.cn/raw/81483a09c2c147d740f73eba2eec71af.png"> 
4. 创建索引后，即可在 **Discover** 界面查询 Elasticsearch 解析后的日志，如下图所示。至此完成了由 TKE 日志到 Elasticsearch 整条链路的打通。
![](https://qcloudimg.tencent-cloud.cn/raw/7e414f7f98eb46b1636e77f118a0f73c.png)
