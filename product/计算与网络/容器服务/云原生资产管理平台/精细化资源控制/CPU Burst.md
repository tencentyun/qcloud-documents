## 功能介绍

部分业务使用 Quota 限制 cgroup 占用 CPU 的份额，在有的场景下，cgoup 会达到 Quota 的限制，此时会导致业务的性能收到影响。CPU Burst，可以让 cgroup 中的进程在达到 Quota 限制时，可以超出一定的 Quota 限额，从而达到提高业务性能的目的。

## 基本原理

因为 cgroup 配置一定的 Quota 比例之后，并不一定每个周期都100%的使用了 Quota 配额，当有的周期没有使用完 Quota 时，将对应的 Quota 收集起来，在该 cgroup 消耗完 Quota 时，能继续使用之前收集的 Quota，CPU Burst 功能就是利用之前周期未使用的 Quota，这样长时间来看，该 cgroup 是并没有超过整体的 Quota 的。能在需要更多的 CPU 时间的某些周期里边，突破 Quota 的限制，达到提升业务性能的目的。



## 使用方式

1. 部署 [QoS Agent](https://cloud.tencent.com/document/product/457/79774)。
2. 在集群里的“扩展组件”页面，找到部署成功的 QoS Agent，单击右侧的**更新配置**。
3. 在修改 QoS Agent 的组件配置页面，勾选 **CPU Burst**。
4. 单击**完成**。

部署 PodQOS 对象，选择作用的 Pod 和 burstQuota，示例如下：

```yaml
apiVersion: ensurance.crane.io/v1alpha1
kind: PodQOS
metadata:
  name: burst
spec:
  labelselector:
    matchLabels:
      k8s-app: mysql # 作用的 Pod
  resourceQOS:
    cpuQOS:
      cpuBurst:
        burstQuota: "40.0" # burstQuota 表示该 Pod 能 Burst 到的最大核数
```

## 最佳实践

部署业务：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    k8s-app: mysql
    qcloud-app: mysql
  name: mysql
spec:
  progressDeadlineSeconds: 600
  replicas: 1
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      k8s-app: mysql
      qcloud-app: mysql
  strategy:
    type: Recreate
  template:
    metadata:
      creationTimestamp: null
      labels:
        k8s-app: mysql
        qcloud-app: mysql
    spec:
      containers:
      - env:
        - name: MYSQL_ROOT_PASSWORD
          value: mysql
        image: mysql:5.6.51
        imagePullPolicy: Always
        name: mysql
        resources:
          limits:
            cpu: "2"
            memory: 8Gi
          requests:
            cpu: "2"
            memory: 8Gi
        securityContext:
          privileged: false
        volumeMounts:
        - mountPath: /var/lib/mysql
          name: data
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      imagePullSecrets:
      - name: qcloudregistrykey
      restartPolicy: Always
      hostNetwork: true
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
      volumes:
      - hostPath:
          path: /data2/mysql
          type: DirectoryOrCreate
        name: data
```

```shell
# 登陆 mysql，IP 为高优 Pod 的 IP
mysql -u root -h $IP  -pmysql

# 创建对应的数据库
CREATE DATABASE sbtest

# 在主机上执行
sysbench oltp_read_only --tables=10 --table_size=3000000 --mysql-host=$IP --mysql-user=root --mysql-password=mysql --threads=10 --mysql-db=sbtest prepare
```

```shell
# 另一台主机上执行如下命令进行压测，mysql-host是高优pod的ip
# 1. 长期压力
sysbench oltp_read_only --tables=10 --table_size=3000000 --mysql-host=$IP --mysql-user=root --mysql-password=mysql --mysql-db=sbtest --time=300 --threads=2 --report-interval=1 run

# 2. 突发压力
#!/bin/bash
while [ 1 ]
do
    sysbench oltp_read_only --tables=10 --table_size=3000000 --mysql-host=$IP --mysql-user=root --mysql-password=mysql --mysql-db=sbtest --time=1 --events=800 --threads=20 --report-interval=1 run
    sleep 10
done

# 压测结束会获取 Latency 信息
```

开启 Burst：

```yaml
apiVersion: ensurance.crane.io/v1alpha1
kind: PodQOS
metadata:
  name: burst
spec:
  labelselector:
    matchLabels:
      k8s-app: mysql
  resourceQOS:
    cpuQOS:
      cpuBurst:
        burstQuota: "40.0"
```

查看 Pod annotation， burstQuota 设置成功：

![](https://qcloudimg.tencent-cloud.cn/raw/5ba693147ed4e583602cdd3ed3efe02f.png)

再次用上文提到的长期压力和突发压力进行压测，获取 Latency 信息。
