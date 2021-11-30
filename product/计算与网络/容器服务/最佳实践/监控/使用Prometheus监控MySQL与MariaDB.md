## 操作场景

MySQL 是常用的关系型数据库，MariaDB 作为 MySQL 的分支版本，兼容 MySQL 协议，也越来越流行。在 Kubernetes 环境中，可借助开源的 [mysqld-exporter](https://github.com/prometheus/mysqld_exporter) 来使用 Prometheus 监控 MySQL 与 MariaDB。您可通过本文了解 Prometheus 并开始使用。


## mysqld-exporter 简介

[mysqld-exporter](https://github.com/prometheus/mysqld_exporter) 通过读取 MySQL 或 MariaDB 中某些数据库状态的数据，将其转换为 Prometheus 的指标格式并暴露为 HTTP 接口被 Prometheus 采集，让原本不支持 Prometheus 指标的 MySQL 和 MariaDB 能够被 Prometheus 监控起来。如下图所示：
<img style="width:80%" src="https://main.qcloudimg.com/raw/5b8918c8804589aa0b7cc947a6481d11.png" data-nonescope="true">

## 操作步骤

### 部署 mysqld-exporter[](id:mysqld-exporter">

>! 在部署 mysqld-exporter 之前需确保已在集群内、集群外或使用已有的云服务中部署 MySQL 或 MariaDB。

#### 部署 MySQL[](id:MySQL)
以从应用市场部署 MySQL 到集群为例。步骤如下：
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，在左侧导航栏选择**应用市场**。
2. 在“应用市场”页面，搜索并单击**MySQL**。
3. 在“应用详情”页面，单击**创建应用**。
4. 在“创建应用”页面，填写信息后单击**创建**即可。
5. 执行以下命令，查看 MySQL 是否正常运行。示例如下：
``` bash
$ kubectl get pods
NAME                     READY   STATUS        RESTARTS   AGE
mysql-698b898bf7-4dc5k   1/1     Running       0          11s
```
6. 执行以下命令，获取 root 密码。示例如下：
``` bash
$ kubectl get secret -o jsonpath={.data.mysql-root-password} mysql
6ZAj33yLBo
```
 
#### 部署 mysqld-exporter

[部署 MySQL](#MySQL) 后，可以开始部署 mysqld-exporter。步骤如下：
1. 依次执行以下命令，创建 mysqld-exporter 账号并登录 MySQL。示例如下：
```
$ kubectl exec -it mysql-698b898bf7-4dc5k bash
```
```
$ mysql -uroot -p6ZAj33yLBo
```
2. 执行以下命令，输入 SQL 语句创建账号。以 `mysqld-exporter/123456` 为例，示例如下：
``` bash
CREATE USER 'mysqld-exporter' IDENTIFIED BY '123456' WITH MAX_USER_CONNECTIONS 3;
GRANT PROCESS, REPLICATION CLIENT, REPLICATION SLAVE, SELECT ON *.* TO 'mysqld-exporter';
flush privileges;
```
3. 使用 yaml 文件部署 mysqld-exporter。示例如下：
> ! 需根据实际情况替换 DATA_SOURCE_NAME 中的账号密码，以及 MySQL 的连接地址。
> 
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysqld-exporter
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysqld-exporter
  template:
    metadata:
      labels:
        app: mysqld-exporter
    spec:
      containers:
      - name: mysqld-exporter
        image: prom/mysqld-exporter:v0.12.1
        args:
        - --collect.info_schema.tables
        - --collect.info_schema.innodb_tablespaces
        - --collect.info_schema.innodb_metrics
        - --collect.global_status
        - --collect.global_variables
        - --collect.slave_status
        - --collect.info_schema.processlist
        - --collect.perf_schema.tablelocks
        - --collect.perf_schema.eventsstatements
        - --collect.perf_schema.eventsstatementssum
        - --collect.perf_schema.eventswaits
        - --collect.auto_increment.columns
        - --collect.binlog_size
        - --collect.perf_schema.tableiowaits
        - --collect.perf_schema.indexiowaits
        - --collect.info_schema.userstats
        - --collect.info_schema.clientstats
        - --collect.info_schema.tablestats
        - --collect.info_schema.schemastats
        - --collect.perf_schema.file_events
        - --collect.perf_schema.file_instances
        - --collect.perf_schema.replication_group_member_stats
        - --collect.perf_schema.replication_applier_status_by_worker
        - --collect.slave_hosts
        - --collect.info_schema.innodb_cmp
        - --collect.info_schema.innodb_cmpmem
        - --collect.info_schema.query_response_time
        - --collect.engine_tokudb_status
        - --collect.engine_innodb_status
        ports:
        - containerPort: 9104
          protocol: TCP
        env:
        - name: DATA_SOURCE_NAME
          value: "mysqld-exporter:123456@(mysql.default.svc.cluster.local:3306)/"
--
apiVersion: v1
kind: Service
metadata:
  name: mysqld-exporter
  labels:
    app: mysqld-exporter
spec:
  type: ClusterIP
  ports:
  - port: 9104
    protocol: TCP
    name: http
  selector:
    app: mysqld-exporter
```


### 添加监控采集配置

[部署 mysqld-exporter](#mysqld-exporter) 后，添加监控采集配置，让 mysqld-exporter 暴露的数据可被采集。
ServiceMonitor 定义示例如下（需要集群中支持）：
```
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: mysqld-exporter
spec:
  endpoints:
    interval: 5s
    targetPort: 9104
  namespaceSelector:
    matchNames:
    - default
  selector:
    matchLabels:
      app: mysqld-exporter
```
Prometheus 原生配置示例如下：
```
    - job_name: mysqld-exporter
      scrape_interval: 5s
      kubernetes_sd_configs:
      - role: endpoints
        namespaces:
          names:
          - default
      relabel_configs:
      - action: keep
        source_labels:
        - __meta_kubernetes_service_label_app_kubernetes_io_name
        regex: mysqld-exporter
      - action: keep
        source_labels:
        - __meta_kubernetes_endpoint_port_name
        regex: http
```

### 添加监控面板

监控采集配置能正常采集数据之后，还需要为 Grafana 添加监控面板进行展示。
- 如果只需观察 MySQL 或 MariaDB 的概览情况，可导入面板 [grafana.com](https://grafana.com/grafana/dashboards/7362)。如下图所示：
<img style="width:80%" src="https://main.qcloudimg.com/raw/0ddd9f644530e96c7d05bfe4acc3c2d7.png" data-nonescope="true">
- 如果需要更丰富的面板，导入 [percona 开源面板](https://github.com/percona/grafana-dashboards/tree/master/dashboards) 中 `MySQL_` 开头的 json 文件中的内容即可。
