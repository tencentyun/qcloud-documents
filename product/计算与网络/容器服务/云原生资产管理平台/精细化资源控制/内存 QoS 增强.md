
内存 QoS 增强能力提供了一系列功能，保证业务内存方面的服务质量保证。全方位提升内存表现，以及灵活限制容器对内存的使用。

## 功能一：异步回收

### 功能介绍

内存异步回收允许容器内部设置一个阈值，超过该阈值则会触发后台异步回收，保证对应 memcg 内使用维持一定量的空闲内存；对后续的内存分配提供保障，减少其进入直接内存回收的次数。

### 使用方式

1. 部署 [QoS Agent](https://cloud.tencent.com/document/product/457/79774)。
2. 在集群里的“扩展组件”页面，找到部署成功的 QoS Agent，单击右侧的**更新配置**。
3. 在修改 QoS Agent 的组件配置页面，勾选 **内存 QoS 增强**。
4. 单击**完成**。
5. 部署业务。
6. 部署关联该业务的 PodQOS 对象，选择需要作用的业务，示例如下：
```yaml
apiVersion: ensurance.crane.io/v1alpha1
kind: PodQOS
metadata:
  name: sql
spec:
  resourceSelectors:
    - kind: Deployment
      apiVersion: apps/v1
      name: mysql	# 选择作用的业务
      nameSpace: default
  resourceQOS:
    memoryQOS:
      memAsyncReclaim:
        asyncRatio: 90	# asyncRatio代表异步回收水位线，当 cgroup 中内存用量超过这个比例开始回收，取值[0-100], 建议设置90以上；默认为0，表示关闭
        asyncDistanceFactor: 200	# asyncDistanceFactor 控制每次触发异步回收的时候，尝试回收的页面总数，默认为1。取值范围为[1, 150000]
```



## 功能二：全局水位分级

### 功能介绍

内存全局水位分级是指针对不同优先级的 cgroup，拥有不同的全局内存水位线；高优先级容器拥有更低的水位先，同等条件下更容易获得内存；低优先级的容器拥有更高的水位先，同等条件下更容易触发回收，进入直接回收流程。

### 使用方式

1. 部署 [QoS Agent](https://cloud.tencent.com/document/product/457/79774)。
2. 在集群里的“扩展组件”页面，找到部署成功的 QoS Agent，单击右侧的**更新配置**。
3. 在修改 QoS Agent 的组件配置页面，勾选 **内存 QoS 增强**。
4. 单击**完成**。
5. 部署业务。
6. 部署关联该业务的 PodQOS 对象，选择需要作用的业务，示例如下：
```yaml
apiVersion: ensurance.crane.io/v1alpha1
kind: PodQOS
metadata:
  name: test
spec:
  labelselector:
    matchLabels:
      k8s-app: low	# 选择作用的业务 Label 
  resourceQOS:
    memoryQOS:
      memWatermark:
        watermarkRatio: 50	# watermarkRatio 取值范围为[-75,75]；负值表示降低水位，主要针对在线容器；正值表示抬升水位；主要针对离线容器；
```
针对离线业务创建 PodQOS 对象：
```
apiVersion: ensurance.crane.io/v1alpha1
kind: PodQOS
metadata:
  name: sql
spec:
  labelselector:
    matchLabels:
      k8s-app: mysql
  resourceQOS:
    memoryQOS:
      memWatermark:
        watermarkRatio: -50
```











## 功能三：pagecache limit

### 功能介绍

进行容器级别的 pagecache 隔离。

### 使用方式

1. 部署 [QoS Agent](https://cloud.tencent.com/document/product/457/79774)。
2. 在集群里的“扩展组件”页面，找到部署成功的 QoS Agent，单击右侧的**更新配置**。
3. 在修改 QoS Agent 的组件配置页面，勾选 **内存 QoS 增强**。
4. 单击**完成**。
5. 部署业务。
6. 部署关联该业务的 PodQOS 对象，选择需要作用的业务，示例如下：
```yaml
apiVersion: ensurance.crane.io/v1alpha1
kind: PodQOS
metadata:
  name: sql
spec:
  labelselector:
    matchLabels:
      k8s-app: mysql-pi-000006	# 选择作用的业务 Label 
  resourceQOS:
    memoryQOS:
      memPageCacheLimit:
        pageCacheMaxRatio: 20	# pageCacheMaxRatio 代表 pagecache 占用内存限额的最大比例，基于当前 memory 的限制值，所以如果要使用这个特性，limits 中必须有 memory 的限制。比如 Pod 内存限制10GB，pageCacheMaxRatio 占20%，就是限制 pagecache 最多使用2GB。
        pageCacheReclaimRatio: 5	# pageCacheReclaimRatio 代表 pagecache 超额后的回收比例，具体是指占 pagecache 最多使用量的比例。
```
