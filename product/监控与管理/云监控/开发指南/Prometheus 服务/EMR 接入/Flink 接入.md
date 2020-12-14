在使用 Flink 过程中需要对 Flink 任务运行状态进行监控，以便了解 Flink 任务是否正常运行，排查 Flink 故障等。云监控的 Prometheus 服务对 push gateway 做了集成，支持 Flink 写入 metrics，并提供了开箱即用的 Grafana 监控大盘。


## 前提条件

1. 购买的腾讯云弹性 MapReduce（以下简称 EMR）产品包含 Flink 组件，并在实例上跑 Flink 任务。
2. 在 Prometheus 实例对应地域及私有网络 VPC 下，创建腾讯云容器服务 [托管版集群](https://cloud.tencent.com/document/product/457/32189#.E4.BD.BF.E7.94.A8.E6.A8.A1.E6.9D.BF.E6.96.B0.E5.BB.BA.E9.9B.86.E7.BE.A4.3Cspan-id.3D.22templatecreation.22.3E.3C.2Fspan.3E)。



## 产品接入

### 获取 PushGateway 访问配置


1. 从实例基本信息页获取 Pushgateway 地址和 Token，从 [账号信息](https://console.cloud.tencent.com/developer) 页面获取 APPID。

![](https://main.qcloudimg.com/raw/18db1ecae32baa8afb99a07394ca7483.png)


### 修改 Flink 配置

1. 选择要监控的 EMR 实例，依次选择集群服务-> Flink 操作->配置管理进入配置管理页
![](https://main.qcloudimg.com/raw/fe0aa3f27746ec8ebb791dccb2110b19.png)
![](https://main.qcloudimg.com/raw/e5d9375de888414cbba4dc2d7ff113fa.png)
2. 单击【修改配置】>【新增配置】项，依次添加以下配置。
<table>
<thead>
<tr>
<th>配置名</th>
<th align="center">默认</th>
<th align="center">类型</th>
<th>描述</th>
<th>建议</th>
</tr>
</thead>
<tbody><tr>
<td>metrics.reporter.promgateway.class</td>
<td align="center">无</td>
<td align="center">字符串</td>
<td>实现 metrics 导出到 push gateway 的 java 类名</td>
<td></td>
</tr>
<tr>
<td>metrics.reporter.promgateway.jobName</td>
<td align="center">无</td>
<td align="center">字符串</td>
<td>push 任务名</td>
<td>指定方便理解的字符串</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.randomJobNameSuffix</td>
<td align="center">true</td>
<td align="center">布尔</td>
<td>是否在任务名后添加随机字符串</td>
<td>要设置为 true，如果不添加 Flink 任务间 metrics 会相互覆盖</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.groupingKey</td>
<td align="center">无</td>
<td align="center">字符串</td>
<td>添加到每个 metrics 的全局 label，格式为 k1=v1;k2=v2</td>
<td>添加 EMR 实例 ID 方便区分不同实例的数据，instance_id=emr-xxx</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.interval</td>
<td align="center">无</td>
<td align="center">时间</td>
<td>推送 metrics 的时间间隔，比如 30 SECONDS</td>
<td>建议设置在1分钟左右，对于监控来说足够</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.host</td>
<td align="center">无</td>
<td align="center">字符串</td>
<td>push gateway 的服务地址</td>
<td>控制台上 prometheus 实例的服务地址</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.port</td>
<td align="center">-1</td>
<td align="center">整数</td>
<td>push gateway 服务端口</td>
<td>控制台上 prometheus 实例的服务端口</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.needBasicAuth</td>
<td align="center">false</td>
<td align="center">布尔</td>
<td>push gateway 服务是否需要认证</td>
<td>设置为 true，prometheus 托管服务的 push gateway 需要认证</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.user</td>
<td align="center">无</td>
<td align="center">字符串</td>
<td>认证的用户名</td>
<td>用户的 APPID</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.password</td>
<td align="center">无</td>
<td align="center">字符串</td>
<td>认证的密码</td>
<td>控制台上 prometheus 实例的访问 Token</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.deleteOnShutdown</td>
<td align="center">true</td>
<td align="center">布尔</td>
<td>Flink 任务执行完后是否删除 push gateway 上对应的 metrics</td>
<td>设置为 true</td>
</tr>
</tbody></table>

配置示例如下：
```plaintext
metrics.reporter.promgateway.class: org.apache.flink.metrics.prometheus.PrometheusPushGatewayReporter
metrics.reporter.promgateway.jobName: climatePredict
metrics.reporter.promgateway.randomJobNameSuffix:true
metrics.reporter.promgateway.interval: 60 SECONDS
metrics.reporter.promgateway.groupingKey:instance_id=emr-xxxx
metrics.reporter.promgateway.host: 172.xx.xx.xx
metrics.reporter.promgateway.port: 9090
metrics.reporter.promgateway.needBasicAuth: true
metrics.reporter.promgateway.user: appid
metrics.reporter.promgateway.password: token
```

### 安装 Flink PushGateway 插件

官方包中的 push gateway 插件目前还不支持配置认证信息，但是托管服务需要认证才允许写入，建议使用我们提供的 jar 包。我们也向 flink 官方提交了支持认证的 PR。
为防止类冲突，如果已经使用 Flink 官方插件，需要先删除。

```plaintext
cd /usr/local/service/flink/lib
rm flink-metrics-prometheus*jar
```

依次在 EMR 控制台上点击集群资源->资源管理-> Master 查看 Master 节点，点击实例 ID 进入 CVM 控制台，登录 CVM 执行如下命令安装插件。

```plaintext
cd /usr/local/service/flink/lib
wget https://rig-1258344699.cos.ap-guangzhou.myqcloud.com/flink/flink-metrics-prometheus_2.11-auth.jar -O flink-metrics-prometheus_2.11-auth.jar
```

### 验证

在 Master 节点上执行`flink run`命令提交新任务，查看任务日志。
```plaintext
grep metrics /usr/local/service/flink/log/flink-hadoop-client-*.log
```

日志中包含下图内容，表示配置加载成功。
![](https://main.qcloudimg.com/raw/316151abb6369f2e73081dc233b46fcd.png)
注意集群中已经提交的任务，由于使用的是老配置文件，不会上报 metrics。


## 查看监控
1. 在对应 Prometheus 实例 >【集成中心】中找到 `Flink` 监控，安装对应的 Grafana Dashboard 即可开启 Flink 监控大盘。
2. 进入 Grafana，单击【<img src="https://main.qcloudimg.com/raw/84bd9a98b230d2ebc32bfac82a108a87.png" height=16/>】展开 Flink 监控面板, 点击 Flink Job List 查看监控。

![](https://main.qcloudimg.com/raw/61741ec36dbbd56a6bb3c9072aa6f23f.png)

![](https://main.qcloudimg.com/raw/c37df281f6dbf8fea48df0de309e8be4.png)

3. 点击表格中的 Job 名或 Job ID 列值查看 Job 监控详情。

![](https://main.qcloudimg.com/raw/698fcea0aa974550aaaed11b96cab0d8.png)

4. 点击右上角的`Flink 集群`，查看 Flink 集群监控。

![](https://main.qcloudimg.com/raw/490df5dd2b54ab5abfc05abc9295bcb4.png)

5. 点击表格中的 Task 名列值查看 Task 监控详情。

![](https://main.qcloudimg.com/raw/8548259642643ca56bae8847b54d7ef3.png)




## 告警接入

在 [Prometheus 实例](https://console.cloud.tencent.com/monitor/prometheus) 列表，找到对应的  Prometheus 实例，点击实例进入实例详情，点击告警策略，可以添加相应的告警策略。
