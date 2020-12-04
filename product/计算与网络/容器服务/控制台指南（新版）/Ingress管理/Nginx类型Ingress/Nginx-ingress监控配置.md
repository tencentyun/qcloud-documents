## Nginx-ingress监控配置

### TKE Nginx-ingress 监控介绍

Nginx Controller已经提供了组件运行状态相关的监控数据，您可以通过配置Nginx-ingress监控, 开启Nginx-ingress监控能力。

#### 前置依赖

1. 集群已关联云原生监控Prometheus（提交工单申请）
2. 云原生监控Prometheus需要与Nginx在同一个网络平面。

#### 采集指标

TKE Nginx-ingress自动配置以下采集指标，您也可以根据业务需要自行配置监控采集指标：

```yaml
待补充
```

### Nginx-ingress 监控Grafana面板

TKE Nginx-ingress 开监控功能会关联一个云原生监控Prometheus，云原生监控Prometheus自带一个Grafana， 您可以在Nginx-ingress 组件页面直接跳转到对应的Grafana面板，如下图：

补充Grafana面板。

![](https://main.qcloudimg.com/raw/66ce3486814a46fa639a38807f51d607.png)


