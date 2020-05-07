## 简介

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

## CronJob 控制台操作指引

### 创建 CronJob

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要创建 CronJob 的集群 ID，进入待创建 CronJob 的集群管理页面。
4. 选择 “工作负载” > “CronJob”，进入 CronJob 信息页面。如下图所示：
![CronJob](https://main.qcloudimg.com/raw/521279f6e09ab9c9efc62675e3a7376f.png)
5. 单击【新建】，进入 “新建Workload” 页面。如下图所示：
![新建Workload](https://main.qcloudimg.com/raw/6ea173c38411103881736060f8394440.png)
6. 根据实际需求，设置 CronJob 参数。关键参数信息如下：
 - 工作负载名：自定义。
 - 命名空间：根据实际需求进行选择。
 - 类型：选择 “CronJob（按照Cron的计划定时运行）”。
 - 执行策略：根据 Cron 格式设置任务的定期执行策略。
 - Job设置
    - 重复次数：Job 管理的 Pod 需要重复执行的次数。
    - 并行度：Job 并行执行的 Pod 数量。
    - 失败重启策略：Pod下容器异常推出后的重启策略。
        - Never：不重启容器，直至 Pod 下所有容器退出。
        - OnFailure：Pod 继续运行，容器将重新启动。
 - 实例内容器：根据实际需求，为 CronJob 的一个 Pod 设置一个或多个不同的容器。
    - 名称：自定义。
    - 镜像：根据实际需求进行选择。
    - 镜像版本：根据实际需求进行填写。
    - CPU/内存限制：可根据 [Kubernetes 资源限制](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) 进行设置 CPU 和内存的限制范围，提高业务的健壮性。
    - 高级设置：可设置 “**工作目录**”，“**运行命令**”，“**运行参数**”，“**容器健康检查**”，“**特权级**”等参数。
7. 单击【创建Workload】，完成创建。

### 查看 CronJob 状态

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要查看 CronJob 状态的集群 ID，进入待查看 CronJob 状态的集群管理页面。
4. 选择 “工作负载” > “CronJob”，进入 CronJob 信息页面。如下图所示：
![CronJob](https://main.qcloudimg.com/raw/521279f6e09ab9c9efc62675e3a7376f.png)
5. 单击需要查看状态的 CronJob 名称，即可查看 CronJob 详情。

## Kubectl 操作 CronJob 指引

<span id="YAMLSample"></span>
### YAML 示例

```Yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox
            args:
            - /bin/sh
            - -c
            - date; echo Hello from the Kubernetes cluster
          restartPolicy: OnFailure
```
- kind：标识 CronJob 资源类型。
- metadata：CronJob 的名称、Label等基本信息。
- metadata.annotations：对 CronJob 的额外说明，可通过该参数设置腾讯云 TKE 的额外增强能力。
- spec.schedule：CronJob 执行的 Cron 的策略。
- spec.jobTemplate：Cron 执行的 Job 模板。

### 创建 CronJob

#### 方法一
1. 参考 [YAML 示例](#YAMLSample)，准备 CronJob YAML 文件。
2. 安装 Kubectl，并连接集群。操作详情请参考 [通过 Kubectl 连接集群](https://cloud.tencent.com/document/product/457/8438)。
3. 执行以下命令，创建 CronJob YAML 文件。
```shell
kubectl create -f CronJob YAML 文件名称
```
例如，创建一个文件名为 cronjob.yaml 的 CronJob YAML 文件，则执行以下命令：
```shell
kubectl create -f cronjob.yaml
```

#### 方法二
1. 通过执行`kubectl run`命令，快速创建一个 CronJob。
例如，快速创建一个不需要写完整配置信息的 CronJob，则执行以下命令：
```shell
kubectl run hello --schedule="*/1 * * * *" --restart=OnFailure --image=busybox -- /bin/sh -c "date; echo Hello"
```
2. 执行以下命令，验证创建是否成功。
```shell+-
kubectl get cronjob [NAME]
```
返回类似以下信息，即表示创建成功。
```
NAME      SCHEDULE    SUSPEND   ACTIVE    LAST SCHEDULE   AGE
cronjob   * * * * *   False     0         <none>          15s
```

### 删除 CronJob
>!
> - 执行此删除命令前，请确认是否存在正在创建的 Job，否则执行该命令将终止正在创建的 Job。
> - 执行此删除命令时，已创建的 Job 和已完成的 Job 均不会被终止或删除。
> -  如需删除 CronJob 创建的 Job，请手动删除。
> 
执行以下命令，删除 CronJob。
```
kubectl delete cronjob [NAME]
```


