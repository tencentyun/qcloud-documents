## 操作场景
在面对大规模分布式应用或者当一个服务的负载分布在多个服务器上时，您可使用 Linux 命令逐一查看应用日志，但此方式的效率较为低下。使用容器部署服务时，相比普通的分布式应用更复杂。容器在上层编排系统的管理下，和服务器的关联关系不固定，没有日志统一收集展示的服务，应用程序的日志更难阅览。

为此，腾讯云容器服务集成腾讯云日志服务，支持配置收集规则将容器服务日志自动收集上报，支持用户使用 ELK （Elasticsearch＋Logstash＋Kibana）自建可视化日志收集服务。本文档使用腾讯云容器服务提供的基础模版，以部署一套从 Kafka 读取日志数据的 ELK 为例，介绍如何在容器服务里部署 ELK。

## 前提条件
- 已创建集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。
- 部署前请保证集群有足够资源。
- 已登录节点。

## 操作步骤
### 部署 Elasticsearch + Kibana 进行日志展示与检索
Elasticsearch 是基于 Apache Lucene（TM）的分布式，提供 RESTful API 的开源搜索引擎，在 ELK 框架中提供数据存储和快速查询的能力。Kibana 则是一个针对 Elasticsearch 的开源的数据分析以及可视化平台，用来搜索、展示存储在 Elasticsearch 索引中的数据。
以下操作步骤直接使用容器服务提供的 ELK 基础模板搭建 Elasticsearch 集群和 Kibana。

>!如果节点没有 git，请先执行 `yum install git` 命令，安装 git。
>
1. 执行以下命令，把所需 yaml 文件下载到 TKE 集群内节点上。
```
git clone https://github.com/tencentyun/ccs-elasticsearch-template.git /tmp/kubernetes-elasticsearch
```

2. 执行以下命令，部署 Elasticsearch Deployment。
```
cd /tmp/kubernetes-elasticsearch
kubectl create -f es-svc.yaml
kubectl create -f es-client.yaml
kubectl create -f es-data.yaml
kubectl create -f es-discovery-svc.yaml
kubectl create -f es-master.yaml
```
3. 执行以下命令，部署 Kibana Deployment。
```
cd /tmp/kubernetes-elasticsearch
kubectl create -f kibana-svc.yaml
kubectl create -f kibana.yaml
```


### 搭建 Logstash 收集 Kafka 指定 Topic 数据
Logstash 是开源的日志分析处理程序，能够从多种源采集转换数据，例如 Syslog、Filebeat、Kafka 等，并支持将数据发送到 Elasticsearch。
本示例搭建的 Logstash 默认从配置的 Kafka 中读取数据并将其发送至已部署的 Elasticsearch 服务。
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击已部署 Elasticsearch + Kibana 的集群，进入集群 Deployment 页面。
2. [](id:step2)选择**服务** > **Service**，进入 Service 详情页，即可查看已创建 Elasticsearch 的服务 IP。如下图所示：
![](https://main.qcloudimg.com/raw/f9671468af487a04b6e5871b5d968a71.png)
3. 依次执行以下命令，修改 `/tmp/kubernetes-elasticsearch/logstash-config.yaml`。
```
cd /tmp/kubernetes-elasticsearch
vim logstash-config.yaml
```
4. 按 “**i**” 或 “**Insert**” 切换至编辑模式，修改 Kafka 和 Elasticsearch 地址。如下图所示：
>? 
>- Kafka 地址：可从已搭建好的 Kafka 服务或已创建的 [Ckafka](https://cloud.tencent.com/product/ckafka) 获取。
>-  Elasticsearch 地址：可从 [步骤2](#step2) 获取。
>
![](https://main.qcloudimg.com/raw/3a4f6c4ed288c4b5f80a720254751f74.png)
5. 修改完成后，按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
6. 执行以下命令，部署 Logstash。
```
kubectl create -f logstash-config.yaml
kubectl create -f logstash-consumer.yaml
```

### 在 Kibana 页面查看日志数据
本文以在 TKE 集群中部署 ELK 并从 Kafka 读取日志数据为例，ELK 更多使用说明以及问题指导请查阅网络资料。
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击已部署服务的集群，进入集群 Deployment 页面。
2. 选择**服务** > **Service**，进入 Service 详情页，可获取已创建 Kibana 服务负载均衡 IP。如下图所示：
![](https://main.qcloudimg.com/raw/45d534ce91f072c963fc27ea1f9d803f.png)
3. 访问其公网负载均衡 IP ，即可打开 Kibana dashboard 进行日志查阅。如下图所示：
![](https://mc.qcloudimg.com/static/img/a233130efb256ef5836b294e9ec65a35/ccs-log-visual.jpeg)
使用 Kibana 进行日志检索前，需确保 Elasticsearch 内有相应 index pattern 的数据。如下图所示：
![](https://mc.qcloudimg.com/static/img/da4ea19aa75ffbf94b38e39a6e781082/ccs-log.jpeg)




