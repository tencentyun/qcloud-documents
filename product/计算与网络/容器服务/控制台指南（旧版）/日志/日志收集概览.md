## 简介

日志收集功能是容器服务为用户提供的集群内日志收集工具，可以将集群内服务或集群节点特定路径文件的日志发送至 Kafka 的指定 topic 或者 日志服务 CLS 的指定日志主题。

日志收集功能适用于需要对 Kubernetes 集群内服务日志进行存储和分析的用户。用户可以通过配置日志收集规则进行集群内日志的收集并将收集到的日志发送至 Kafka 的指定 Topic 或 日志服务 CLS 的指定日志主题以供用户的其它基础设施进行消费。

日志收集功能需要为每个集群手动开启。日志收集功能开启后，日志收集 Agent 会在集群内以 Daemonset 的形式运行。用户可以通过日志收集规则配置日志的采集源和消费端，日志收集 Agent 会从用户配置的采集源进行日志收集，并将日志内容发送至用户指定的消费端。

需要注意的是，使用日志收集功能需要您确认 Kubernetes 集群内节点能够访问日志消费端。

## 使用场景

- [采集容器标准输出日志](https://cloud.tencent.com/document/product/457/13662)
- [采集主机文件日志](https://cloud.tencent.com/document/product/457/13660)
- [采集容器内文件日志](https://cloud.tencent.com/document/product/457/13661)
- [配置所采集日志的消费端](https://cloud.tencent.com/document/product/457/13659)

## 最佳实践

基于日志收集功能，使用 Logstash 和 Elasticsearch 进行集群服务日志的可视化检索。

为提供日志的可视化能力，建议用户使用 logstash 消费 kafka 的日志数据，并将日志数据发送到 elasticsearch 集群，查看[日志收集最佳实践](https://cloud.tencent.com/document/product/457/13657)提供 elasticsearch 和 logstash 集群的搭建模板。
 
## 概念

- 日志收集 Agent：TKE 用于收集日志信息的 Agent，基于 Fluentd 开发，在集群内以 Daemonset 的方式运行。

- 日志收集规则：用户可以使用日志收集规则指定日志的采集源以及将采集的日志发送至何处，日志收集 Agent 会监测日志收集规则的变化，变化或新增的规则会在最多 10s 内生效，多条日志收集规则不会创建多个 Daemonset，但过多的日志收集规则会使得日志收集 Agent 占用的资源增加。

- 日志源：包含指定容器日志以及主机路径日志。在需要收集集群内服务打印到标准输出的日志时，用户可以设定日志的采集源为指定容器日志，包括设置收集所有 Namespace 服务的日志、采集若干个指定 Namespace 内的服务日志。在需要收集集群内节点特定路径的日志时，用户可以设定日志的采集源为主机路径日志，例如当需要收集所有路径形式为 `/var/lib/docker/containers/<container-id>/<container-id>.json-log` 的日志时，可以指定日志收集路径为 `/var/lib/docker/containers/*/*.json-log`。

- 消费端：日志收集 Agent 在采集指定采集源的日志后，会将收集到的日志发送至用户指定的消费端。当前日志收集服务支持用户自建的 Kakfa 、腾讯云的 Ckafka 服务和腾讯云的 日志服务 CLS 作为日志的消费端，用户只需配置消费端 Kafka 或者 CLS ，日志收集 Agent 会将收集到的日志以 json 的形式发送至用户指定的消费端。


## 功能

日志收集功能主要提供以下功能：

- 容器日志收集：收集 kubernetes 集群中指定服务的标准输出日志
![容器日志收集器][1]

- 主机日志收集：收集 kubernetes 集群节点上指定路径的文件日志
![主机日志收集器][2]

- 将收集的日志推送至腾讯云的 CKafka 服务
![配图-Ckafka配置图][3]

- 将收集的日志推送至用户自建 Kafka 的指定 Topic
![配图-kafka配置图][4]

- 将收集的日志推送至腾讯云的日志服务 CLS
![配图-日志服务CLS配置图][5]

[1]:https://mc.qcloudimg.com/static/img/1876f68db6e7f0282c1289d1a7411211/image.png
[2]:https://mc.qcloudimg.com/static/img/45465494725a520f963be72ae3fb9aca/image.png
[3]:https://mc.qcloudimg.com/static/img/2247389b857b20cceabd0c6dccdbcc8a/ckafa.png
[4]:https://mc.qcloudimg.com/static/img/9fb478a794d258a0609db74ae3ede544/kafka.png
[5]:https://mc.qcloudimg.com/static/img/4d52a836e1c50cbe46fb7d8d4049bf8a/%7BF5CD3AB9-4732-44E0-85BF-1103EB970862%7D.png
