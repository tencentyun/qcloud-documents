## 概述

MySQL 是常用的关系型数据库，MariaDB 作为 MySQL 的分支版本，兼容 MySQL 协议，也越来越流行。在 Kubernetes 环境中如何使用 Prometheus 来对它们进行监控呢？通常是借助开源的 [mysqld-exporter](https://github.com/prometheus/mysqld_exporter) 来实现，本文将围绕这个主题展开详细介绍下。

## mysqld-exporter 原理介绍

[mysqld-exporter](https://github.com/prometheus/mysqld_exporter) 通过读取 MySQL 或 MariaDB 中的一些数据库状态的数据，并将其转换为 Prometheus 的指标格式并暴露成 http 接口被 Prometheus 所采集，来实现让原本不支持 Prometheus 指标的 MySQL 和 MariaDB 能够被 Prometheus 监控起来:

<img style="width:80%" src="https://main.qcloudimg.com/raw/5b8918c8804589aa0b7cc947a6481d11.png" data-nonescope="true">

## 操作步骤

### 部署 mysqld-exporter

在部署 mysqld-exporter 之前首先保证 MySQL 或 MariaDB 已经部署，可以在集群内，也可以在集群外，或者使用现成的云服务。如果还没有，这里以从应用市场部署到集群为例来部署一个 MySQL:

1. 在应用市场中找到 MySQL，点击 `创建应用-创建`。

<img style="width:80%" src="https://main.qcloudimg.com/raw/054fca3216eb14acb42b3ffb3015a100.png" data-nonescope="true">

2. 查看 mysql 是否正常运行:

``` bash
$ kubectl get pods
NAME                     READY   STATUS        RESTARTS   AGE
mysql-698b898bf7-4dc5k   1/1     Running       0          11s
```

3. 获取 root 密码:

``` bash
$ kubectl get secret -o jsonpath={.data.mysql-root-password} mysql
6ZAj33yLBo
```

有了 MySQL 后，我们开始准备部署 mysqld-exporter，首先为 mysqld-exporter 创建一个账号，登录 MySQL:

```
$ kubectl exec -it mysql-698b898bf7-4dc5k bash
$ mysql -uroot -p6ZAj33yLBo
```

然后输入 SQL 来创建账号，这里以 `mysqld-exporter/123456` 为例:

``` bash
CREATE USER 'mysqld-exporter' IDENTIFIED BY '123456' WITH MAX_USER_CONNECTIONS 3;
GRANT PROCESS, REPLICATION CLIENT, REPLICATION SLAVE, SELECT ON *.* TO 'mysqld-exporter';
flush privileges;
```

然后使用以下 yaml 来部署 mysqld-exporter:

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

---

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

> ! 注意根据实际情况替换 DATA_SOURCE_NAME 中的账号密码，以及 MySQL 的连接地址

### 添加监控采集配置

有了 mysqld-exporter 后，我们就可以配置监控的采集，让 mysqld-exporter 暴露的数据被采集起来，ServiceMonitor 定义示例 (需要集群中支持):

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

Prometheus 原生配置示例:

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

采集配置好，正常采集有了数据之后，还需要为 Grafana 添加监控面板进行展示，如果只是看 MySQL 或 MariaDB 的一些概览情况，可以导入 `grafana.com` 的这个面板: https://grafana.com/grafana/dashboards/7362

<img style="width:80%" src="https://main.qcloudimg.com/raw/0ddd9f644530e96c7d05bfe4acc3c2d7.png" data-nonescope="true">

如果需要更丰富的面板，可以导入 percona 开源的一些面板，地址: https://github.com/percona/grafana-dashboards/tree/master/dashboards (导入 `MySQL_` 开头的 json 文件中的内容即可)。