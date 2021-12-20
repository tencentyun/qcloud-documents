## 简介

### 组件介绍

HPC（HorizontalPodCronscaler）是一种可以对 K8S workload 副本数进行定时修改的自研组件，配合 HPC CRD 使用，最小支持秒级的定时任务。

### 组件功能

- 支持设置“实例范围”（关联对象为 HPA）或“目标实例数量”（关联对象为 deployment 和 statefulset）。
- 支持开关“例外时间”。例外时间的最小配置粒度是日期，支持设置多条。
- 支持设置定时任务是否只执行一次。



### 部署在集群内的 Kubernetes 对象

在集群内部署 HPC , 将在集群内部署以下 Kubernetes 对象：

| Kubernetes 对象名称                                    | 类型                     | 默认占用资源           | 所属Namespaces |
| ------------------------------------------------------ | ------------------------ | ---------------------- | -------------- |
| horizontalpodcronscalers.autoscaling.cloud.tencent.com | CustomResourceDefinition | -                      | -              |
| hpc-leader-election-role                               | Role                     | -                      | kube-system    |
| hpc-leader-election-rolebinding                        | RoleBinding              | -                      | kube-system    |
| hpc-manager-role                                       | ClusterRole              | -                      | -              |
| hpc-manager-rolebinding                                | ClusterRoleBinding       | -                      | -              |
| cronhpa-controller-manager-metrics-service             | Service                  | -                      | kube-system    |
| hpc-manager                                            | ServiceAccount           | -                      | kube-system    |
| tke-hpc-controller                                     | Deployment               | 100mCPU/pod、100Mi/pod | kube-system    |




## 限制条件

#### 环境要求

<dx-alert infotype="explain" title="">
您在创建集群时选择1.12.4以上版本集群，无需修改任何参数，开箱可用。
</dx-alert>

- 仅支持1.12版本以上的 kubernetes。
- 需设置 kube-apiserver 的启动参数：`--feature-gates=CustomResourceSubresources=true`

#### 节点要求

- HPC 组件默认挂载主机的时区将作为定时任务的参考时间，因此要求节点存在 `/etc/localtime` 文件。
- HPC 默认安装2个 HPC Pod 在不同节点，因此节点数推荐为2个及以上。

#### 被控资源要求

在创建 HPC 资源时，被控制的 workload（K8S 资源）需要存在于集群中。


## 操作步骤

### 安装 HPC

1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，在左侧导航栏中选择**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 HPC。
5. 单击**完成**即可创建组件。


### 创建并使用 HPC 工作负载示例

#### 创建关联  Deployment 的定时任务资源
示例如下：
<dx-codeblock>
:::  yaml
apiVersion: autoscaling.cloud.tencent.com/v1
kind: HorizontalPodCronscaler
metadata:
  name: hpc-deployment
  namespace: default 
spec:
  scaleTarget:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx-deployment
    namespace: default 
  crons:
  - name: "scale-down"
    excludeDates:
      - "* * * 15 11 *"
      - "* * * * * 5"
    schedule: "30 */1 * * * *"
    targetSize: 1
  - name: "scale-up"
    excludeDates:
      - "* * * 15 11 *"
      - "* * * * * 5"
    schedule: "0 */1 * * * *"
    targetSize: 3
:::
</dx-codeblock>

#### 创建关联  StatefulSet 的定时任务资源
示例如下：
<dx-codeblock>
:::  yaml
apiVersion: autoscaling.cloud.tencent.com/v1
kind: HorizontalPodCronscaler
metadata:
  name: hpc-statefulset
  namespace: default
spec:
  scaleTarget:
    apiVersion: apps/v1
    kind: Statefulset
    name: nginx-statefulset
    namespace: default
  crons:
  - name: "scale-down"
    excludeDates:
      - "* * * 15 11 *"
    schedule: "0 */2 * * * *"
    targetSize: 1
  - name: "scale-up"
    excludeDates:
      - "* * * 15 11 *"
    schedule: "30 */2 * * * *"
    targetSize: 4
:::
</dx-codeblock>

#### 创建关联 HPA 的定时任务资源
示例如下：
<dx-codeblock>
:::  yaml
apiVersion: autoscaling.cloud.tencent.com/v1
kind: HorizontalPodCronscaler
metadata:
  labels:
    controller-tools.k8s.io: "1.0"
  name: hpc-hpa
spec:
  scaleTarget:
    apiVersion: autoscaling/v1
    kind: HorizontalPodAutoscaler
    name:  nginx-hpa
    namespace: default
  crons:
  - name: "scale-up"
    schedule: "30 */1 * * * *"
    minSize: 2
    maxSize: 6
  - name: "scale-down"
    schedule: "0 */1 * * * *"
    minSize: 1
    maxSize: 5
:::
</dx-codeblock>

### 定时时间设置参考

| 字段名称     | 是否必选 | 允许值范围          | 允许的特殊字符 |
| ------------ | -------- | ------------------- | -------------- |
| Seconds      | 是       | 0 - 59              | * / , -        |
| Minutes      | 是       | 0 - 59              | * / , -        |
| Hours        | 是       | 0 - 23              | * / , -        |
| Day of month | 是       | 1 - 31              | * / , - ?      |
| Month        | 是       | 1 - 12 或 JAN - DEC | * / , -        |
| Day of week  | 是       | 0 - 6 或 SUN - SAT  | * / , - ?      |
