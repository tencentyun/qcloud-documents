## 概述

Kubernetes 作为 IaaS 和 PaaS 的中间层，当前对于资源的计费依托于 IaaS 层的资源计费。一个 Kubernetes 的集群，按照其购买的节点实例 CVM 计费。而用户则使用的是 Pod，在实际场景中，通常需要面临这些问题，一个 Pod 如何承担成本、如何评估集群的成本、如何进行成本预测和优化建议。针对上述问题，我们推荐用户使用 Kubecost 进行解决。

Kubecost 是一款成本分析工具，可以为集群成本提供洞察、分析、推荐和建议。作为您优化集群成本的财务分析师，Kubecost 可以为您提供全面的成本分析报告。本文将介绍 Kubecost 使用场景、优化建议、详细的功能说明以及如何安装使用。


## 使用场景

### 评估每种资源消耗的成本

成本支出，即为计算 Pod 资源请求（Request）或者使用量（Usage）消耗的成本。根据不同类型的资源，按照 Pod 所在 Node 的 IaaS 计价方式作为基本参考，来计算 Pod 所使用的成本费用。

目前云厂商的 Node 计费模式一般是**包年包月（Month）**、**按量计费（Hour）**和**竞价实例**。当 Kubecost 计算 Pod 成本时，即使是相同请求量的 Container，在不同类型的 Node 上成本消耗也不一致。

上述三种计费模式中，由于用户购买的是一个整体实例，因此按照实例计费，不针对单独一个资源计费。而通过使用 Kubecost，可以参照模型分析资源类型分摊成本、每种资源分摊成本。

例如，一个云厂商提供的某种 Node（虚拟机、物理机），CPU 为1核(C)，内存 Mem 为1G，价格为20元/月。


通过使用 Kubecost，需要添加云厂商说明的每种资源的基础价格，例如 CPU、Mem 价格。或者按照业务需要配置对应的比例，例如1C:1G 的价格比是3:1，CPU/Mem=3:1等。可以得知分摊到每种资源（CPU/GPU/Mem/PV/Network）的计费。

具体计算公式如下：
**sum (normalized_resource_price[i] × resource_quantity[i]) = node_price**

因此得到，整个 Node 的价格为20元/月，按照 CPU 15元/月、Mem 5元/月进行分摊成本。



### 评估成本效率

成本加权平均评估效率，由于每一种资源的成本权重不同（成本权重即为不同类型的资源，售卖的价格不同。例如 CPU 和 GPU 等计算资源价格相对较高，Mem 价格相对较低，而 Disk 价格则更低），相同的资源利用效率，不同资源对成本的贡献度也不一样。

例如，100%的 Disk 利用率，但是由于磁盘相对便宜，对最终的成本控制的贡献就较低。但如果是 CPU 资源，即使资源利用率为30%，由于 CPU 资源价格相对昂贵，最终可能对成本起到关键作用，因此需要用加权平均来评估成本效率，例如：

- Mem 的效率：MemEfficiency = MemUsage / MemRequest
- CPU 的效率：CPUEfficiency = cpuUsage / cpuRequest
- Mem 的成本效率：MemCostEff = a.MemEfficiency() × a.MemTotalCost()
- CPU 的成本效率：cpuCostEff = a.CPUEfficiency() × a.CPUTotalCost()
- **总成本效率**：totalEff=（MemCostEff + cpuCostEff) / (a.CPUTotalCost() + a.MemTotalCost())

### 优化建议

在判断哪些业务需要优化以及如何优化成本结构，可以先查找 TOP 10 的某种资源浪费，例如资源的 Usage 和 Request 差别较大，可以根据应用监控画像给出推荐的 Request，最后计算出每种资源可节省的成本。


### 评估经济学边际成本

关于节点自动扩容部分，可以衡量一个集群中每个节点，假设 CPU 和 Mem 每增加 1C1G，最终成本达到多少，是否会出现规模效应（规模效应即为资源数量增加，成本并不会爆炸，但是却可以解决装箱问题）。



如有上述需求和问题，您都可以使用 Kubecost 来分析自己的集群成本趋势。


## 前提条件

- 已创建容器服务 TKE 集群。如果您还未创建集群，请参见 [快速创建一个标准集群](https://cloud.tencent.com/document/product/457/54231)。
- 已使用命令行工具 Kubectl 连接集群。如果您还未连接集群，请参见 [连接集群](https://cloud.tencent.com/document/product/457/32191)。

## 功能说明

- Kubecost 主要给出 cost 分析，包括 Service、Application、Pod、Workload 等各种标签类型维度分析。
- 资源分配和使用。
- 包含一个集群健康检查的功能，类似集群巡检和健康检查。

### Overview

![](https://main.qcloudimg.com/raw/5d189e38aab69d433a9a6bda3320e0e2.png)
**上述图中数字序号标示处相关说明可参考下文对应说明介绍**：
1. 月度预估可以节省的**金额**以及可以节省成本的**优化建议数量**。
2. **月度账单和成本效率**：
 - 月度账单：基于过去7天资源消耗的**预测值**。
 - 成本效率：基于过去2天的成本效率。
   计算方法：（每种资源利用率 × 各自的价格之和）/ 总价格
3. **月度集群账单**。账单维度包括 Total cost、Compute、Memory、Storage。
4. **资源效率**：
   - 基于当前的资源提供量和过去7天的资源使用量计算。
   - 资源分成三个维度： Compute、Memory、Storage。
   - 成本构成四个维度：空闲、系统、应用、其他。
5. **Controller Allocation**：按 Controller 分类，通过过去两天计算每个 Controller 的成本。
6. **Service Allocation**：按 Service 分类，通过过去两天计算每个 Service 的成本。
7. **Namespace Allocation**：按 Namespace 分类，通过过去两天计算每个 NS 的成本以及成本效率。
计算方法：每种资源利用率 × 各自的价格之和 / 总价格
8. **Infrastructure health**：集群基础架构状态评分，比较像我们的集群巡检，给出一些优化建议，例如：
   - Worker nodes 跨可用区部署。
   - Master 多副本。
   - 检测 CPU 被 throttling 的 Pod。



### Cost Allocation

![img](https://main.qcloudimg.com/raw/b9469008a0b87974c3796657ff505efd.png)
**上述图中数字序号标示处相关说明可参考下文对应说明介绍**：
1. **显示的指标**：
   - 累积成本：在选定时间窗口的实际/历史支出。
   - 费率指标：每小时、每天或每月的成本，基于所选时间窗口中的样本，也用于预计成本。
2. **聚合**：
   Cost Allocation 可以查看所有原生 Kubernetes 概念的分配支出，例如 NS、Label、Service。 Cost Allocation 还允许将成本分配给 team、product/project、department、or environment 等组织概念。
3. **时间窗口**：
   用于衡量成本的指定时间窗口。默认情况下会缓存 1d、2d、7d 和 30d 查询的结果。
4. **过滤**：
   按 NS、clusterId 、lable、Pod prefix 过滤资源，以更密切地查询成本支出的关键位置。
5. **Allocate idle costs（分配空闲成本）**：
   Allocate idle costs 按比例将空闲或空闲集群成本分配给租户。具体来说，这适用于已配置但未被租户完全使用或请求的资源。例如，如果您的集群的利用率仅为25%，以资源的最大使用量和 Request 来衡量，则 Allocate idle costs 会按比例增加每个 pod/NS/Deployment 的成本到原来的4倍。
6. **图表选择**：
   切换到条形图视图以查看所选窗口的汇总成本，或切换到时间序列视图以查看成本随时间的变化。
7. **附加选项**：
   查看其他选项以将成本数据导出为 CSV 或查看帮助文档。


### Assets

![img](https://main.qcloudimg.com/raw/275c22510f157d3b3710aa147eb2f69f.png)

Kubecost Assets 视图显示了按集群中单个资源细分的 Kubernetes 集群成本（例如，按节点、磁盘和其他资源划分的成本）。

### Savings

展示月度预估可以节省的金额以及可以节省成本的优化建议数量，即 Overview 页面里面第一个入口。

以 Request 推荐为例，如下面第二张图所示，这里提供了以下三种不同等级的推荐值，并且推荐值与给定的时间窗口也存在关系：

- **Development：**the aim is 80% resource utilization at 85th-percentile resource usage over the given window。
- **Production：**the aim is 65% resource utilization at 98th-percentile resource usage over the given window。
- **High-availability：**the aim is 50% resource utilization at 99.9th-percentile resource usage over the given window。

![img](https://main.qcloudimg.com/raw/1d5e1383cf4ffe108b4f2221f811e6e8.png)
![img](https://main.qcloudimg.com/raw/c17bd39a6b90666d88a99542552ffc2b.png)

### Health

集群基础架构状态评分，建议修复的会标识红色感叹号❗，如下图所示：
![img](https://main.qcloudimg.com/raw/def229e1eeb39af2abb6c029294329dd.png)

### Reports

Reports 主要保存一些观测数据，观测粒度和 Cost Allocation 里一致，支持按照某种方式聚合/观测数据之后，一键保存。如下图所示：
![](https://main.qcloudimg.com/raw/a550844cd1b0b3dfa866e46385dd0c04.png)

## 操作步骤

### 安装 helm

登录到某个 Node 节点，执行以下命令安装 helm：
```sh
curl https:``//raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
```

### 下载 Kubecost helm

执行以下命令下载 Kubecost helm：

```sh
wget https:``//qitian-1251707795.cos.ap-beijing.myqcloud.com/cost-analyzer-1.81.0.tgz
```

### 安装 Kubecost

1. 执行以下命令安装 Kubecost：
```sh
kubectl create ns kubecost``helm install cost-analyzer cost-analyzer-``1.81``.``0``.tgz -n kubecost
```
2. 执行以下命令，查看服务 Pod 是否都正常运行。示例如下：
```sh
kubectl get pods -n kubecost -o wide
```
 执行结果如下图所示：
![img](https://main.qcloudimg.com/raw/bff2c85ed8a62458d90a5b06580bb5ed.png)



### 更改服务访问方式

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster)。
2. 单击对应的集群 ID/名称，进入集群管理页面。
3. 单机**服务和路由** > **Service**进入 Service 页面。
4. 找到您想要更改的 Service，在其右侧操作栏下单击**更新访问方式**进入更新访问方式页面。
![](https://main.qcloudimg.com/raw/7949fd01702d5f779cb2ccb00b6efe3a.jpg)
5. service cost-analyzer-cost-analyzer 的访问方式为负载均衡方式，更新服务访问方式之后会得到一个公网 IPv4 地址，便可在公网进行访问。
 - 访问地址：` http://[服务公网地址]:9090`
 - 初始用户名和密码：admin、admin。

### 卸载

执行以下命令可卸载 kubecost：
```sh
helm uninstall cost-analyzer -n kubecost
```
