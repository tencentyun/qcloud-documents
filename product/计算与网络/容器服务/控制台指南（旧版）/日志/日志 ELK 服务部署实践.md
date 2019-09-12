## 为什么部署容器服务需要配置日志收集功能？

通常我们习惯登录服务器使用 Linux 命令查看应用日志。但面对大规模分布式应用，一个服务的负载分布在多个服务器上，这种方式的效率就非常低下了，于是就产生了日志统一收集展示的需求。

当使用容器部署服务时情况就更复杂，因为相比普通的分布式应用，容器在上层编排系统的管理下，和服务器的关联关系并不固定。这种时候，如果没有统一收集展示日志的服务，应用程序的日志将很难阅览。

腾讯云容器服务已经集成了腾讯云日志服务，支持配置收集规则将容器服务日志自动收集上报。当然，我们也支持用户使用 ELK （Elasticsearch＋Logstash＋Kibana）自建可视化日志收集服务。本文档介绍如何在容器服务里部署 ELK。

## ELK 部署指导

本篇使用腾讯云容器服务提供的基础模版，以部署一套从 Kafka 读取日志数据的 ELK 为例。部署前请保证集群有足够资源。

### 第一步：部署 Elasticsearch + Kibana 进行日志展示与检索

Elasticsearch 是基于 Apache Lucene(TM) 的分布式，提供 RESTful API 的开源搜索引擎。在 ELK 框架中提供数据存储和快速查询的能力。Kibana 则是一个针对Elasticsearch 的开源的数据分析以及可视化平台，用来搜索、展示存储在 Elasticsearch 索引中的数据。

本示例直接使用容器服务提供的 ELK 基础模板搭建 Elasticsearch 集群和 Kibana。

首先把所需 yaml 文件下载到 TKE 集群内节点上。

	git clone https://github.com/tencentyun/ccs-elasticsearch-template.git /tmp/kubernetes-elasticsearch

部署 Elasticsearch Deployment。
	
	cd /tmp/kubernetes-elasticsearch
	kubectl create -f es-svc.yaml
	kubectl create -f es-client.yaml
	kubectl create -f es-data.yaml
	kubectl create -f es-discovery-svc.yaml
	kubectl create -f es-master.yaml
	
部署 Kibana Deployment。
	
	cd /tmp/kubernetes-elasticsearch
	kubectl create -f kibana-svc.yaml
	kubectl create -f kibana.yaml

> *注意：如果节点没有 git，请先执行 yum install git，安装 git 。

### 第二步：搭建 Logstash 收集 Kafka 指定 Topic 数据

Logstash 是开源的日志分析处理程序，能够从多种源采集转换数据，如 Syslog、Filebeat、Kafka 等，并支持将数据发送到 Elasticsearch 。

本示例搭建的 Logstash 默认从配置的 Kafka 中读取数据并将其发送至第一步部署的 Elasticsearch 服务。

	cd /tmp/kubernetes-elasticsearch
	vim logstash-config.yaml

搭建前请先修改 /tmp/kubernetes-elasticsearch/logstash-config.yaml 中的 Kafka 和 Elasticsearch 地址。

![][3]

修改完成后，部署 Logstash。

	kubectl create -f logstash-config.yaml
	kubectl create -f logstash-consumer.yaml


### 第三步：在 Kibana 页面查看日志数据

在 TKE 控制台可以看到刚创建的 Kibana 服务。

![][4]

访问其公网负载均衡 IP ，即可打开 Kibana dashboard 进行日志查阅。

![][2]

> *注意：使用 Kibana 进行日志检索前，需要先保证 Elasticsearch 内有相应 index pattern 的数据。

![][1]

本文以在 TKE 集群中部署 ELK 并从 Kafka 读取日志数据为例，ELK 更多使用说明以及问题指导请查阅网络资料。

[1]:https://mc.qcloudimg.com/static/img/da4ea19aa75ffbf94b38e39a6e781082/ccs-log.jpeg
[2]:https://mc.qcloudimg.com/static/img/a233130efb256ef5836b294e9ec65a35/ccs-log-visual.jpeg
[3]:https://main.qcloudimg.com/raw/3a4f6c4ed288c4b5f80a720254751f74.png
[4]:https://main.qcloudimg.com/raw/2ebaab9ee812eecbe5490c0b83cbf145.png
