## 操作场景
本文介绍如何在弹性集群中选择多种工作负载形式来运行您的服务。
>!如果您需要通过 YAML 来创建和管理您的弹性容器工作负载，请务必阅读 [弹性容器服务 Annotation 说明](#workloadAnnotationDesc)。

## 前提条件
- 已创建状态为“运行中”的弹性集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/39813)。
- 集群有合适的且为 Active 状态的命名空间。

## 工作负载类型介绍
### Deployment
Deployment 声明了 Pod 的模板和控制 Pod 的运行策略，适用于部署无状态的应用程序。您可以根据业务需求，对 Deployment 中运行的 Pod 的副本数、调度策略、更新策略等进行声明。

### StatefulSet
StatefulSet 主要用于管理有状态的应用，创建的 Pod 拥有根据规范创建的持久型标识符。Pod 迁移或销毁重启后，标识符仍会保留。在需要持久化存储时，您可以通过标识符对存储卷进行一一对应。如果应用程序不需要持久的标识符，建议您使用 Deployment 部署应用程序。

### Job
Job 控制器会创建 1 - N 个 Pod，这些 Pod 按照运行规则运行，直至运行结束。Job 可用于批量计算及数据分析等场景，通过重复执行次数、并行度、重启策略等设置满足业务述求。
Job 执行完成后，不再创建新的 Pod，也不会删除已有 Pod，您可在“日志”中查看已完成的 Pod 的日志。如果您删除了 Job，Job 创建的 Pod 也会同时被删除，将查看不到该 Job 创建的 Pod 的日志。

### CronJob
一个 CronJob 对象类似于 crontab（cron table）文件中的一行。它根据指定的预定计划周期性地运行一个 Job，格式可以参考 Cron。
Cron 格式说明如下：
```
# 文件格式说明
#  ——分钟（0 - 59）
# |  ——小时（0 - 23）
# | |  ——日（1 - 31）
# | | |  ——月（1 - 12）
# | | | |  ——星期（0 - 6）
# | | | | |
# * * * * *
```

## 操作步骤
1. 登录容器服务控制台，选择左侧导航栏中的【[弹性集群](https://console.cloud.tencent.com/tke2/ecluster)】。
2. 在 “弹性集群” 列表页面，单击需创建工作负载的集群 ID，进入集群 “Deployment” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/25a9b8b66aabcc288cb71997c90f24f3.png)
3. 单击【新建】，进入 “新建Workload” 页面。
4. 填写工作负载名，并选择要创建的工作负载类型。
  - 各类型工作负载的具体参数设置请参考：
     - [Deployment 管理](https://cloud.tencent.com/document/product/457/31705)
     - [StatefulSet 管理](https://cloud.tencent.com/document/product/457/31707)
     - [CronJob 管理](https://cloud.tencent.com/document/product/457/31709)
     - [Job 管理](https://cloud.tencent.com/document/product/457/31708)
   - 其他操作指引请参考：
     - [设置工作负载的资源限制](https://cloud.tencent.com/document/product/457/32813)
     - [设置工作负载的调度规则](https://cloud.tencent.com/document/product/457/32814)
     - [设置工作负载的健康检查](https://cloud.tencent.com/document/product/457/32815)
    - [设置工作负载的运行命令和参数](https://cloud.tencent.com/document/product/457/32816)

<span id="workloadAnnotationDesc"></span>
## 弹性容器服务 Annotation 说明
<table>
<thead>
<tr>
<th width="">Annotation Key</th>
<th width="22%">Annotation Value</th>
<th>说明</th>
<th width="30%">是否必填</th>
</tr>
</thead>
<tbody><tr>
<td>eks.tke.cloud.tencent.com/cpu</td>
<td>请参考 <a href="https://cloud.tencent.com/document/product/457/39808" target="_blank">资源规格</a> 填写，默认单位为核，不需要注明</td>
<td>Pod 规格的 CPU 参数</td>
<td>是，不填或填写不存在的规格会报错。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/mem</td>
<td>请参考 <a href="https://cloud.tencent.com/document/product/457/39808" target="_blank">资源规格</a> 填写，需要注明单位，例如512Mi、0.5Gi、1Gi</td>
<td>Pod 规格的内存参数</td>
<td>是，不填或填写不存在的规格会报错。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/security-group-id</td>
<td><a href="https://console.cloud.tencent.com/cvm/securitygroup" target="_blank">安全组 ID</a>，可填写多个，以<code>,</code>分割，例如 <code>sg-id1,sg-id2</code></td>
<td>工作负载默认绑定的安全组</td>
<td>否，如果不填写会默认关联工作负载绑定同地域的 default 安全组。<br>如果填写请务必填写同地域存在的安全组 ID，否则会报错。</td>
</tr>
</tbody></table>

### 完整示例
```
apiVersion: apps/v1beta2
kind: Deployment
metadata:
  annotations:
    deployment.kubernetes.io/revision: "1"
    description: 测试
    eks.tke.cloud.tencent.com/cpu: "1"
    eks.tke.cloud.tencent.com/mem: 2Gi
    eks.tke.cloud.tencent.com/security-group-id: "sg-dxxxxxx5,sg-zxxxxxxu"
  creationTimestamp: "2019-10-11T03:47:55Z"
  generation: 1
  labels:
    k8s-app: nginx
    qcloud-app: nginx
  name: nginx
  namespace: default
  resourceVersion: "33796648"
  selfLink: /apis/apps/v1beta2/namespaces/default/deployments/nginx
  uid: e86f6533-ebd9-11e9-b061-4effc6de97a3
spec:
  minReadySeconds: 10
  progressDeadlineSeconds: 600
  replicas: 1
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      k8s-app: nginx
      qcloud-app: nginx
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
    type: RollingUpdate
  template:
    metadata:
      annotations:
        eks.tke.cloud.tencent.com/cpu: "1"
        eks.tke.cloud.tencent.com/mem: 2Gi
        eks.tke.cloud.tencent.com/wan: "true"
      creationTimestamp: null
      labels:
        k8s-app: nginx
        qcloud-app: nginx
    spec:
      containers:
      - env:
        - name: PATH
          value: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
        - name: NGINX_VERSION
          value: 1.17.4
        - name: NJS_VERSION
          value: 0.3.5
        - name: PKG_RELEASE
          value: 1~buster
        image: ccr.ccs.tencentyun.com/alex_lee/nginx:latest
        imagePullPolicy: Always
        name: nginxcontainer
        resources:
          limits:
            cpu: 500m
            memory: 1Gi
          requests:
            cpu: 250m
            memory: 256Mi
        securityContext:
          privileged: false
          procMount: Default
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /tmp
          name: vol
      dnsPolicy: ClusterFirst
      imagePullSecrets:
      - name: qcloudregistrykey
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
      volumes:
      - emptyDir: {}
        name: vol
```
