云监控 Prometheus 服务在继承开源 Prometheus 监控能力的同时 ，还提供高可用的 Prometheus 托管服务及与开源可视化的 Grafana，为您减少用户的开发及运维成本。

## Prometheus 简介

Prometheus 是一个开源监控系统。与 Kubernetes的相似，Prometheus 受启发于 Google 的 Borgman 监控系统，而 Kubernetes 也是从 Google 的 Borg 演变而来的。Prometheus 始于2012年，并由 SoundCloud 内部工程师开发，于2015年1月发布。2016年5月，其成为继 Kubernetes 之后第二个正式加入 [Cloud Native Computing Foundation（CNCF）](https://www.cncf.io/) 基金会的项目。现最常见的 Kubernetes 容器管理系统中，通常会搭配 Prometheus 进行监控。


Prometheus 具有如下特性：
- 自定义多维数据模型（时序列数据由 Metric 和一组 Key/Value Label 组成）。
- 灵活而强大的查询语言 PromQL，可利用多维数据完成复杂的监控查询。
- 不依赖分布式存储，支持单主节点工作。
- 通过基于 HTTP 的 Pull 方式采集时序数据。
- 可通过 PushGateway 的方式来实现数据 Push 模式。
- 可通过动态的服务发现或者静态配置去获取要采集的目标服务器。
- 结合 Grafana 可方便的支持多种可视化图表及仪表盘。

## 云监控 Prometheus 服务优势

<img src="https://main.qcloudimg.com/raw/ef425686ad7ec73919b38278faeca488.png" data-nonescope="true"></img>


与开源的 Prometheus 对比，云监控 Prometheus 服务有哪些优势？
- 更轻量、更稳定、可用性更高。
- 完全兼容开源 Prometheus 生态。
- 无需您手动搭建，节省开发成本。
- 与腾讯云容器服务高度集成，节省与 Kubernetes 集成的开发成本。
- 与云监控告警体系打通，节省开发告警通知成本。
- 同时也集成了常用的 Grafana Dashboard 及告警规则模板。

### 更轻量、更稳定、可用性更高
- 与开源 Prometheus 监控相比，云监控 Prometheus 托管服务的整体结构更加轻量化，您在云监控创建 Prometheus 实例后，即可拥有 Prometheus 服务。
- 在系统稳定性方面，开源 Prometheus 一般会占用几十 GB 的内存，云监控 Prometheus 只会占用 MB 级别的用户资源，为您提供了更低资源占用的 Prometheus 服务。
- Prometheus 托管服务结合腾讯云云存储服务及自身的副本能力，为您提供了可用性更强的 Prometheus 监控服务，减少系统中断运行次数。

### 节省开发运维成本
- 云监控提供了原生的 Prometheus 一站式服务，在您购买 Prometheus 实例之后，可以快速与腾讯云容器服务 TKE 集成，Prometheus 为运行在 Kubernetes 之上的服务提供监控服务，免去用户搭建运维及开发成本。
- 配合 Prometheus，云监控提供了开通即可使用的 Grafana 服务，同时也集成了丰富的 Kubernetes 基础监控的 Dashboard，以及常用服务监控的 Dashboard，用户开通后即可快速使用，免去自己维护 Dashboard 到成本。
- 基于云监控告警通道的能力，打通 Prometheus Alertmanager，同时提供丰富的报警规则模板，免去用户学习告警配置的成本。
