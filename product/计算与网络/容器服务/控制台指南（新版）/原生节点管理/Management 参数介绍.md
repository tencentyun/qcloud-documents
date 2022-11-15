## 功能概览

Management 参数为节点常用自定义配置提供了统一的入口，您可通过该入口为原生节点底层的内核参数 KernelArgs 进行调优，同时支持设置 Nameservers\Hosts 来满足业务部署的环境要求。

## Management 参数项

| 参数项 | 描述 | 
|---------|---------|
| Nameservers | 设置业务部署环境需要 DNS 服务器地址。 |
| Hosts | 设置业务部署环境所需要的 Hosts。 |
| [KernelArgs](#KernelArgs) | 设置内核参数对业务进行性能调优（该功能目前白名单开放，可 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请）。 |

>? 为确保系统组件的正常安装，原生节点默认注入腾讯云官方资料库地址 `nameserver = 183.60.83.19`、`nameserver = 183.60.82.98`。


[](id:KernelArgs)
### KernelArgs 参数
下面列出了支持调整的 OS 参数和接受的值。

#### 套接字和网络优化：
对于预期会处理大量并发会话的代理节点，您可以使用下面的 TCP 和网络选项调整。

| 编号 | 参数 | 默认值 | 允许的值 / 范围 | 参数类型 | 范围 |
|---------|---------|---------|---------|---------|---------|
| 1 | "net.core.somaxconn" | 32768 | 4096 - 3240000 | int | The maximum length of the listening queue for each port in the system. |
| 2 | "net.ipv4.tcp_max_syn_backlog" | 8096 | 1000 - 3240000 | int | The maximum length of tcp SYN queue length. |
| 3 | "net.core.rps_sock_flow_entries" | 8192 | 1024 - 536870912 | int | The maximum size of hash table for RPS. |
| 4 | "net.core.rmem_max" | 16777216 | 212992 - 134217728 | int | The maximum size, in bytes, of the receive socket buffer. |
| 5 | "net.core.wmem_max" | 16777216 | 212992 - 134217728 | int | The maximum size, in bytes, of the send socket buffer. |
| 6 | "net.ipv4.tcp_rmem" | \"4096 12582912 16777216\" | 1024 - 2147483647 | string | The min/default/max size of tcp socket receive buffer. |
| 7 | "net.ipv4.tcp_wmem" | \"4096 12582912 16777216\" | 1024 - 2147483647 | string | The min/default/max size of tcp socket send buffer. |
| 8 | "net.ipv4.neigh.default.gc_thresh1" | 2048 | 128 - 80000 | int | The minimum number of entries that can be retained. If the number of entries is less than this value, the entries will not be recycled. |
| 9 | "net.ipv4.neigh.default.gc_thresh2" | 4096 | 512 - 90000 | int | When the number of entries exceeds this value, the GC will clear the entries longer than 5 seconds. |
| 10 | "net.ipv4.neigh.default.gc_thresh3" | 8192 | 1024 - 100000 | int | Maximum allowable number of non-permanent entries. |
| 11 | "net.ipv4.tcp_max_orphans" | 32768 | 4096 - 2147483647 | int | Maximal number of TCP sockets not attached to any user file handle, held by system. Increase this parameter properly to avoid the 'Out of socket memory' error when the load is high. |
| 12 | "net.ipv4.tcp_max_tw_buckets" | 32768 | 4096 - 2147483647 | int | Maximal number of timewait sockets held by system simultaneously. Increase this parameter properly to avoid \"TCP: time wait bucket table overflow\" error. |

#### 文件句柄限制：
在为大量流量提供服务时，所服务的流量通常来自大量本地文件。 您可以略微调整以下内核设置和内置限制，以便只占用部分系统内存来处理更大的量。

| 编号 | 参数 | 默认值 | 允许的值 / 范围 | 参数类型 | 范围 |
|---------|---------|---------|---------|---------|---------|
| 1 | "fs.file-max" | 3237991 | 8192 - 12000500 | int | Limit on the total number of fd, including socket, in the entire system. | 
| 2 | "fs.inotify.max_user_instances" | 8192 | 1024 - 2147483647 | int | Limit on the total number of inotify instances. | 
| 3 | "fs.inotify.max_user_watches" | 524288 | 781250 - 2097152 | int | The total number of inotify watches is limited. Increase this parameter to avoid \"Too many open files\" errors. | 

#### 虚拟内存：
以下设置可用于调整 Linux 内核虚拟内存 (VM) 子系统的操作以及向磁盘进行脏数据的 writeout。

| 编号 | 参数 | 默认值 | 允许的值 / 范围 | 参数类型 | 范围 |
|---------|---------|---------|---------|---------|---------|
| 1 | "vm.max_map_count" | 262144 | 65530 - 262144 | int | The maximum number of memory map areas a process may have. |

#### 工作线程限制：

| 编号 | 参数 | 默认值 | 允许的值 / 范围 | 参数类型 | 范围 |
|---------|---------|---------|---------|---------|---------|
| 1 | "kernel.threads-max" | 4194304 | 4096 - 4194304 | int | The system-wide limit on the number of threads (tasks) that can be created on the system. |
| 2 | "kernel.pid_max" | 4194304 | 4096 - 4194304 | int | PIDs greater than this value are not allocated; thus, the value in this file also acts as a system-wide limit on the total number of processes and threads. |

## 为节点设置 Management 参数
### 通过控制台操作
#### 方式1：为新增节点设置 Management 参数
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，参考 [新建原生节点](https://cloud.tencent.com/document/product/457/78198#.E9.80.9A.E8.BF.87.E6.8E.A7.E5.88.B6.E5.8F.B0.E5.88.9B.E5.BB.BA) 文档创建原生节点。
2. 在“新建节点池”页面，单击**更多设置**，为节点设置 Management 参数。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a189e7e378a3820974698887266ce345.png)
3. 单击**创建节点池**即可。

 

#### 方式2：为已有节点设置 Management 参数

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在集群列表页中，单击集群 ID，进入该集群详情页。
3. 选择左侧菜单栏中的**节点管理 > 节点池**，进入“节点池列表”页面。
4. 单击节点池 ID，进入“节点列表”页面。
5. 在“详情”页签中，单击**参数设置 > 编辑**，修改 Management 参数。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/44728c9bf174135eb175c59105e34ede.png)




### 通过 YAML 操作

```
apiVersion: node.tke.cloud.tencent.com/v1beta1
kind: MachineSet
spec:
  type: Native
  displayName: mstest
  replicas: 2
  autoRepair: true
  deletePolicy: Random
  instanceTypes:
  - C3.LARGE8
  subnetIDs:
  - subnet-xxxxxxxx
  template:
    spec:
      displayName: mtest
      providerSpec:
        type: Native
        value:
          instanceChargeType: PostpaidByHour
          # 在此处填写 management 参数信息
          management:
            hosts:
            - Hostnames:
              - static.fake.com
              IP: 192.168.2.42
            - Hostnames:
              - common.fake.com
              IP: 192.168.2.45
            nameservers:
            - 183.60.83.19
            - 183.60.82.98
            - 8.8.8.8
            kernelArgs:
            - kernel.pid_max=65535
            - fs.file-max=400000
            - net.ipv4.tcp_rmem="4096 12582912 16777216"
            - vm.max_map_count="65535"

```
