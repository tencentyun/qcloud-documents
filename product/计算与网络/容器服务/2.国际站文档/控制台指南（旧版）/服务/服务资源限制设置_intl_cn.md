## 请求 ( Request ) 与 限制 ( Limit )
**Request**：容器使用的最小资源需求，作为容器调度时资源分配的判断依赖。只有当节点上可分配资源量 >= 容器资源请求数时才允许将容器调度到该节点。但 Request 参数不限制容器的最大可使用资源值。
**Limit**： 容器能使用的资源最大值，设置为 0 表示使用资源无上限。
>**注意：**
>更多 `Limit` 和 `Request` 参数介绍，点击 [查看详情](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/)。

## CPU 限制说明
CPU 资源允许设置 CPU 请求和 CPU 限制的资源量，以核 ( U ) 为单位，允许为小数。
>**注意：**
>1. CPU Request 作为调度时的依据，在创建时为该容器在节点上分配 CPU 使用资源，称为 “已分配 CPU” 资源。
>2. CPU Limit 限制容器 CPU 资源的上限，设置为 0 表示不做限制 ( CPU Limit >= CPU Request )。

## 内存限制说明
内存资源只允许限制容器最大可使用内存量。以 MiB 为单位，允许为小数。
>**注意：**
>1. 由于内存资源为不可伸缩资源，在容器使用内存量超过内存 Request 时，容器就存在被 Kill 掉的风险。因此为了保证容器的正常运作限制 Request = Limit。
>2. 内存 Request ( = Limit ) 作为调度时的依据，在创建时为该容器在节点上分配内存使用资源，称为 “已分配内存” 资源。
 
## CPU 使用量 VS CPU 使用率
>**注意：**
>1. CPU 使用量为绝对值，表示实际使用的 CPU 的物理核数，CPU 资源请求和 CPU 资源限制的判断依据都是 CPU 使用量。
>2. CPU 使用率为相对值，表示 CPU 的使用量与 CPU 单核的比值 (或者与节点上总 CPU 核数的比值)。

## 使用示例
一个简单的示例说明 Request 和 Limit 的作用，测试集群包括 1 个 4U4G 的节点、已经部署的两个 Pod ( Pod1，Pod2 )，每个 Pod 的资源设置为（ CPU Requst，CPU Limit，Memory Requst，Memory Limit ）= ( 1U，2U，1G，1G )。( 1.0 G = 1000 MiB )
节点上 CPU 和内存的资源使用情况如下图所示：
![Alt text](https://mc.qcloudimg.com/static/img/b021e644c31ddcacf13930a412c51e5a/image.png)
已经分配的 CPU 资源为：1U (分配 Pod1 ) + 1U (分配 Pod2 ) = 2U，剩余可以分配的 CPU 资源为 2U。
已经分配的内存资源为：1G (分配 Pod1 ) + 1G (分配 Pod2 ) = 2G，剩余可以分配的内存资源为 2G。
所以该节点可以再部署一个 ( CPU Requst， Memory Requst ) =( 2U，2G )的 Pod 部署，或者部署 2 个 ( CPU Requst， Memory Requst ) = ( 1U，2G ) 的 Pod 部署。

在资源限制方面，每个 Pod1 和 Pod2 使用资源的上限为 ( 2U，1G )，即在资源空闲的情况下，Pod 使用 CPU 的量最大能达到 2U。
