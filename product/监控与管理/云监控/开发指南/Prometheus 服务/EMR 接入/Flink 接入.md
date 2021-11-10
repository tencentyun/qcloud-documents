## 操作场景

在使用 Flink 过程中需要对 Flink 任务运行状态进行监控，以便了解 Flink 任务是否正常运行，排查 Flink 故障等。云监控的 Prometheus 服务对 push gateway 做了集成，支持 Flink 写入 metrics，并提供了开箱即用的 Grafana 监控大盘。


## 前提条件

1. 购买的腾讯云弹性 MapReduce（以下简称 EMR）产品包含 Flink 组件，并在实例上跑 Flink 任务。
2. 在 Prometheus 实例对应地域及私有网络 VPC 下，创建腾讯云容器服务 [托管版集群](https://cloud.tencent.com/document/product/457/32189#TemplateCreation)。


## 操作步骤
### 产品接入

#### 获取 PushGateway 访问配置

1. 前往**[弹性 MapReduce](https://console.cloud.tencent.com/emr)** > **选择对应的“实例”** > **基本信息** > **实例信息**页面，获取 Pushgateway 地址和 Token。
![](https://main.qcloudimg.com/raw/1853a917832e275511cfc7c537815941.png)
2. 在 [账号信息](https://console.cloud.tencent.com/developer) 页面获取 APPID。


#### 修改 Flink 配置

1. 进入**[弹性 MapReduce](https://console.cloud.tencent.com/emr)** > **选择对应的“实例”** > **集群服务**页面。
2. 找到**Flink**配置项，在右侧选择**操作** > **配置管理**，进入配置管理页面。
3. 在页面右侧单击**新增配置项**，依次添加以下配置。
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
<tbody>
<tr>
<td>metrics.reporter.promgateway.class</td>
<td align="center">无</td>
<td align="center" nowrap="nowrap">字符串</td>
<td>实现 metrics 导出到 push gateway 的 java 类名</td>
<td>-</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.<br>jobName</td>
<td align="center">无</td>
<td align="center">字符串</td>
<td>push 任务名</td>
<td>指定方便理解的字符串</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.<br>randomJobNameSuffix</td>
<td align="center">true</td>
<td align="center">布尔</td>
<td>是否在任务名后添加随机字符串</td>
<td>需设置为 true，如果不添加， Flink 任务间 metrics 会相互覆盖</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.<br>groupingKey</td>
<td align="center">无</td>
<td align="center">字符串</td>
<td>添加到每个 metrics 的全局 label，格式为 k1=v1;k2=v2</td>
<td>添加 EMR 实例 ID 方便区分不同实例的数据，例如 instance_id=emr-xxx</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.<br>interval</td>
<td align="center">无</td>
<td align="center">时间</td>
<td>推送 metrics 的时间间隔，例如30秒</td>
<td>建议设置在1分钟左右</td>
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
<td>metrics.reporter.promgateway.<br>needBasicAuth</td>
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
<td>用户的 <a href="https://console.cloud.tencent.com/developer">APPID</a></td>
</tr>
<tr>
<td>metrics.reporter.promgateway.<br>password</td>
<td align="center">无</td>
<td align="center">字符串</td>
<td>认证的密码</td>
<td>控制台上 prometheus 实例的访问 Token</td>
</tr>
<tr>
<td>metrics.reporter.promgateway.<br>deleteOnShutdown</td>
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

#### 安装 Flink PushGateway 插件

官方包中的 push gateway 插件目前还不支持配置认证信息，但是托管服务需要认证才允许写入，建议使用我们提供的 jar 包。我们也向 flink 官方提交了支持认证的 PR。

1. 为防止类冲突，如果已经使用 Flink 官方插件，需要先执行以下命令删除官方插件。
```plaintext
cd /usr/local/service/flink/lib
rm flink-metrics-prometheus*jar
```
2. 在** [弹性 MapReduce 控制台](https://console.cloud.tencent.com/emr)** > **选择对应的“实例”** > **集群资源** > **资源管理** > **Master**页面，查看 Master 节点。
3. 单击实例 ID 跳转至 CVM 控制台，登录 CVM 执行以下命令安装插件。
```plaintext
cd /usr/local/service/flink/lib
wget https://rig-1258344699.cos.ap-guangzhou.myqcloud.com/flink/flink-metrics-prometheus_2.11-auth.jar -O flink-metrics-prometheus_2.11-auth.jar
```



#### 验证

1. 在 Master 节点上执行 `flink run` 命令提交新任务，查看任务日志。
```plaintext
grep metrics /usr/local/service/flink/log/flink-hadoop-client-*.log
```
2. 日志中包含下图内容，表示配置加载成功：
![](https://main.qcloudimg.com/raw/316151abb6369f2e73081dc233b46fcd.png)
>!集群中已经提交的任务，由于使用的是旧配置文件，因此不会上报 metrics。


### 查看监控
1. 在对应 Prometheus 实例 >**集成中心**中找到 `Flink` 监控，安装对应的 Grafana Dashboard 即可开启 Flink 监控大盘。
2. 进入 Grafana，单击**<img src="https://main.qcloudimg.com/raw/84bd9a98b230d2ebc32bfac82a108a87.png" width="2%">**展开 Flink 监控面板。
![](https://main.qcloudimg.com/raw/61741ec36dbbd56a6bb3c9072aa6f23f.png)
3. 单击**Flink Job List**查看监控。
![](https://main.qcloudimg.com/raw/c37df281f6dbf8fea48df0de309e8be4.png)
3. 单击表格中的**Job 名**或**Job ID 列值**，查看 Job 监控详情。
![](https://main.qcloudimg.com/raw/698fcea0aa974550aaaed11b96cab0d8.png)
4. 单击右上角的**Flink 集群**，查看 Flink 集群监控。
![](https://main.qcloudimg.com/raw/490df5dd2b54ab5abfc05abc9295bcb4.png)
5. 单击表格中的**Task 名列值**，查看 Task 监控详情。
![](https://main.qcloudimg.com/raw/8548259642643ca56bae8847b54d7ef3.png)




### 告警接入

1. 登录 [云监控 Prometheus 控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 单击告警策略，可以添加相应的告警策略，详情请参见 [新建告警策略](https://cloud.tencent.com/document/product/248/48952)。

