您可以配置服务网格数据面访问日志 Access Log 输出（容器标准输出）的开启范围，输出格式，以及开启 Access Log 日志自动采集对接到云日志服务产品 CLS 的日志集-日志主题。您可以在创建网格时配置访问日志，网格创建后您也可以在基本信息页面修改访问日志配置。

## 访问日志配置

当前支持的访问日志配置如下表：

| 配置项 | 描述 |
| ----- | ----- |
| 开启范围 | 配置开启访问日志输出的数据面（边缘代理网关 和 istio-proxy sidecar），可以开启指定边缘代理网关、指定 namespace 下所有数据面、或网格所有数据面的访问日志到容器标准输出 |
| 输出格式 | 配置访问日志输出的字段和格式模版，默认格式输出的字段为 Istio 默认输出的字段，增强格式在默认格式基础上增加了 Trace ID 输出 |
| 消费端 | 配置将数据面容器标准输出的访问日志采集到日志服务 CLS。需要选择存储访问日志的 CLS 日志集与日志主题，可以选择自动创建日志集/主题，或关联已有的日志集/主题。自动创建的日志集命名规则为 `{mesh ID}`，自动创建的日志主题带有 TCM 标识，命名规则为 `{mesh ID}-accesslog`。开启访问日志采集到 CLS 提交后，会开启网格管理集群的日志采集功能，在网格管理的集群中部署日志采集组件 tke-log-agent (DaemonSet)，并配置 TCM 访问日志的采集规则与索引。该功能是基于容器服务的 [日志采集功能](https://cloud.tencent.com/document/product/457/36771)，请确保已开通 [日志服务 CLS](https://cloud.tencent.com/document/product/614)，并且容器服务的服务角色 `TKE_QCSRole` 已关联日志服务运维管理的预设策略`QcloudAccessForTKERoleInOpsManagement`，更多说明请参见 [容器服务角色权限说明](https://cloud.tencent.com/document/product/457/43416)|

- 创建网格时配置 Access Log：
![](https://qcloudimg.tencent-cloud.cn/raw/a2359be19e965f4a21f4487f480ba867.png)
- 网格创建完成后配置 Access Log：
![](https://qcloudimg.tencent-cloud.cn/raw/574127fd715b5ff4a798ba67718a1b97.png)

## 访问日志查看

### 通过容器标准输出查看

TCM 的数据面访问日志 Access Log 是输出到容器标准输出，您可以通过您的 Kubernetes 集群 API Server 查看 istio-proxy 容器标准输出的访问日志：
```
kubectl -n {命名空间} logs {Pod 名称} -c istio-proxy  --tail 5
```

### 通过日志服务 CLS 日志检索查看

如您开启了访问日志的消费端配置，将 TCM 数据面访问日志 Access Log 采集到了日志服务 CLS，则您可以在 CLS 控制台检索分析处选择对应日志主题查看 TCM 数据面访问日志。CLS 日志检索语法，请参见 [CLS 日志检索语法与规则](https://cloud.tencent.com/document/product/614/47044)。
![](https://qcloudimg.tencent-cloud.cn/raw/a7f9f1ad433011166049977adff7061d.png)


