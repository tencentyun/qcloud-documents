## 操作场景
本文介绍如何基于裸金属服务器搭建 torch+Taco Train 分布式训练集群。


## 操作步骤


### 购买实例[](id:Step1)
购买实例，其中实例、存储及镜像请参考以下信息选择，其余配置请参考 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855) 按需选择。
- **实例**：选择 [GPU 型 HCCG5v](https://cloud.tencent.com/document/product/386/63405#HCCG5v)、[GPU 型 HCCG5vm](https://cloud.tencent.com/document/product/386/63405#HCCG5vm) 或 [GPU 型 HCCPNV4h](https://cloud.tencent.com/document/product/386/63405#HCCPNV4h)。
- **系统盘**：配置容量不小于50GB的云硬盘。您也可在创建实例后使用文件存储，详情参见 [在 Linux 客户端上使用 CFS 文件系统](https://cloud.tencent.com/document/product/582/11523)。
- **镜像**：建议选择**公共镜像**，公共镜像当中已安装 RDMA 网卡驱动，且支持自动安装 GPU 驱动。若您选择**自定义镜像**，则需要自行安装 RDMA 网卡驱动和 GPU 驱动，请通过 [联系我们](https://cloud.tencent.com/document/product/1573/74090) 获取腾讯云售后支持。
 - 操作系统请使用 CentOS 7.6。
 - 若您选择**公共镜像**，则请勾选“后台自动安装GPU驱动”，实例将在系统启动后预装对应版本驱动。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a2ec816632fb9ac930dd60b2a2897a95.png)


### 安装 nv_peer_mem（可选）[](id:Step2)


多机通信的过程中，GPU 显存中的数据需要首先拷贝到内存中，然后通过网卡发出。通过  [GPU Direct RDMA 协议](https://docs.nvidia.com/cuda/gpudirect-rdma/index.html#how-gpudirect-rdma-works)，可利用 GPU 和网卡直接通过 PCIe 进行 Peer2Peer 的数据交换这条更快速的路径，无需借助内存来进行数据的传递。

如需使用 GDR 进行数据传输，请在实例中执行以下命令，安装如下驱动。
```plaintext
git clone https://github.com/Mellanox/nv_peer_memory.git
cd ./nv_peer_memory/ && git checkout 1.0-9
make && insmod ./nv_peer_mem.ko
// 如果服务器发生了重启，nv_peer_mem驱动需要重新insmod
```

### 安装 docker 和 nvidia docker[](id:Step3)
1. 参考 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，登录实例。
2. 执行以下命令，安装 docker。
```shellsession
curl -s -L http://mirrors.tencent.com/install/GPU/taco/get-docker.sh | sudo bash
```
若您无法通过该命令安装，请尝试多次执行命令，或参考 Docker 官方文档 [Install Docker Engine](https://docs.docker.com/engine/install/) 进行安装。
本文以 CentOS 为例，安装成功后，返回结果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/7a513693ec3cf6a0bc17ef1edf8a88cd.png" width="918px"/>
2. 执行以下命令，安装 nvidia-docker2。
```shellsession
curl -s -L http://mirrors.tencent.com/install/GPU/taco/get-nvidia-docker2.sh | sudo bash
```
若您无法通过该命令安装，请尝试多次执行命令，或参考 NVIDIA 官方文档 [Installation Guide & mdash](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) 进行安装。
本文以 CentOS 为例，安装成功后，返回结果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/efd41192c5062e8806632ab9aa23a136.png" width="918px"/>


### 下载 docker 镜像[](id:Step4)
执行以下命令，下载 docker 镜像。
```shellsession
docker pull ccr.ccs.tencentyun.com/qcloud/taco-train:torch111-cu113-bm-0.4.1
```
该镜像包含的软件版本信息如下：
- OS：Ubuntu 20.04.4 LTS
- ofed: MLNX_OFED_LINUX-5.4-3.1.0.0
- python：3.8.10
- cuda toolkits：V11.3.109
- cudnn library：8.2.0
- nccl library：2.9.9
- **tencent-lightcc ：3.1.1**
- **torch：1.11.0+cu113**



其中：
- LightCC 是腾讯云提供的基于 Horovod 深度定制优化的通信组件，完全兼容 Horovod API，不需要任何业务适配。
- torch 为官方版本。


### 启动 docker 镜像[](id:Step5)
执行以下命令，启动 docker 镜像。
```shellsession
docker run -itd --rm --gpus all --shm-size=32g --ulimit memlock=-1 --ulimit stack=67108864 --net=host --privileged ccr.ccs.tencentyun.com/qcloud/taco-train:torch111-cu113-bm-0.4.1
```
<dx-alert infotype="notice" title="">
`--privileged` 选项使容器能够访问主机上的 RDMA 设备。
</dx-alert>


### 分布式训练 benchmark 测试

<dx-alert infotype="explain" title="">
docker 镜像中的文件 `/mnt/pytorch_synthetic_benchmark.py` 来自 [horovod example](https://github.com/horovod/horovod/blob/master/examples/pytorch/pytorch_synthetic_benchmark.py)。
</dx-alert>


<dx-accordion>
::: 单卡
执行以下命令，进行测试。
```plaintext
/usr/local/openmpi/bin/mpirun -np 1 --allow-run-as-root -bind-to none -map-by slot -x NCCL_DEBUG=INFO -x NCCL_IB_DISABLE=0 -x NCCL_SOCKET_IFNAME=bond0 -x NCCL_IB_GID_INDEX=3 -x NCCL_NET_GDR_LEVEL=0 -x LD_LIBRARY_PATH -x PATH -mca pml ob1 -mca btl_tcp_if_include bond0 -mca btl ^openib python3 /mnt/pytorch_synthetic_benchmark.py --model resnet50 --batch-size=256
```
下图为 HCCPNV4h/A100的单卡 benchmark 结果：
![](https://qcloudimg.tencent-cloud.cn/raw/80218f77696f61d1de78c4eee2d39bcd.png)

:::
::: 单机多卡


执行以下命令，进行测试。
```plaintext
/usr/local/openmpi/bin/mpirun -np 8 --allow-run-as-root -bind-to none -map-by slot -x NCCL_DEBUG=INFO -x NCCL_IB_DISABLE=0 -x NCCL_SOCKET_IFNAME=bond0 -x NCCL_IB_GID_INDEX=3 -x NCCL_NET_GDR_LEVEL=0 -x LD_LIBRARY_PATH -x PATH -mca pml ob1 -mca btl_tcp_if_include bond0 -mca btl ^openib python3 /mnt/pytorch_synthetic_benchmark.py --model resnet50 --batch-size=256
```
下图为 HCCPNV4h/A100的8卡 benchmark 结果：
![](https://qcloudimg.tencent-cloud.cn/raw/6a542fc58a3a0cdbf2bf84660e4dba51.png)


:::
::: 多机多卡

1. 参考 [购买实例](#Step1) - [启动 docker 镜像](#Step5) 步骤，购买和配置多台训练机器。
2. 配置多台服务器 docker 间相互免密访问，详情请参见 [配置容器 SSH 免密访问](https://cloud.tencent.com/document/product/1573/74100)。
3. 执行以下命令，使用 TACO Train 进行多机训练加速。
```plaintext
/usr/local/openmpi/bin/mpirun -np 16 -H gpu1:8,gpu2:8 --allow-run-as-root -bind-to none -map-by slot -x NCCL_DEBUG=INFO -x NCCL_IB_DISABLE=0 -x NCCL_SOCKET_IFNAME=bond0 -x NCCL_IB_GID_INDEX=3 -x NCCL_NET_GDR_LEVEL=0 -x HOROVOD_FUSION_THRESHOLD=0  -x HOROVOD_CYCLE_TIME=0 -x LIGHT_INTRA_SIZE=8 -x LIGHT_2D_ALLREDUCE=1 -x LIGHT_TOPK_ALLREDUCE=1 -x LIGHT_TOPK_THRESHOLD=2097152 -x LD_LIBRARY_PATH -x PATH -mca pml ob1 -mca btl_tcp_if_include bond0 -mca btl ^openib python3 /mnt/pytorch_synthetic_benchmark.py --model resnet50 --batch-size=256
```
下图为 HCCPNV4h/A100 2机16卡 benchmark 结果：
![](https://qcloudimg.tencent-cloud.cn/raw/932abda02bf8e29a30b5286b2b1eb7aa.png)
LightCC 的环境变量说明如下表：
<table>
<thead>
<tr>
<th>环境变量</th>
<th>默认值</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>LIGHT_2D_ALLREDUCE</td>
<td>0</td>
<td>是否使用2D-Allreduce 算法</td>
</tr>
<tr>
<td>LIGHT_INTRA_SIZE</td>
<td>8</td>
<td>2D-Allreduce 组内 GPU 数</td>
</tr>
<tr>
<td>LIGHT_HIERARCHICAL_THRESHOLD</td>
<td>1073741824</td>
<td>2D-Allreduce 的阈值，单位是字节，小于等于该阈值的数据才使用2D-Allreduce</td>
</tr>
<tr>
<td>LIGHT_TOPK_ALLREDUCE</td>
<td>0</td>
<td>是否使用 TOPK 压缩通信</td>
</tr>
<tr>
<td>LIGHT_TOPK_RATIO</td>
<td>0.01</td>
<td>使用 TOPK 压缩的比例</td>
</tr>
<tr>
<td>LIGHT_TOPK_THRESHOLD</td>
<td>1048576</td>
<td>TOPK 压缩的阈值，单位是字节，大于等于该阈值的数据才使用 TOPK 压缩通信</td>
</tr>
<tr>
<td>LIGHT_TOPK_FP16</td>
<td>0</td>
<td>压缩通信的 value 是否转成 FP16</td>
</tr>
</tbody></table>
4. 执行以下命令，关闭 TACO LightCC 加速进行测试。
```plaintext
# 去掉LIGHT_xx的环境变量，即可使用Horovod进行多机Allreduce
/usr/local/openmpi/bin/mpirun -np 16 -H gpu1:8,gpu2:8 --allow-run-as-root -bind-to none -map-by slot -x NCCL_DEBUG=INFO -x NCCL_IB_DISABLE=0 -x NCCL_SOCKET_IFNAME=bond0 -x NCCL_IB_GID_INDEX=3 -x NCCL_NET_GDR_LEVEL=0 -x LD_LIBRARY_PATH -x PATH -mca pml ob1 -mca btl_tcp_if_include bond0 -mca btl ^openib python3 /mnt/pytorch_synthetic_benchmark.py --model resnet50 --batch-size=256
```
下图为 HCCPNV4h/A100 2机16卡，关闭 LightCC 之后的 benchmark 结果：
![](https://qcloudimg.tencent-cloud.cn/raw/cef86ccd677c4c109990069a53ff2dbb.png)
:::
::: 多机多卡 GDR
执行以下命令，使用 GDR 进行测试。
<dx-alert infotype="notice" title="">
使用 GDR 需安装 nv_peer_mem，详情请参见 [安装 nv_peer_mem](#Step2)。
</dx-alert>
```plaintext
/usr/local/openmpi/bin/mpirun -np 16 -H gpu1:8,gpu2:8 --allow-run-as-root -bind-to none -map-by slot -x NCCL_DEBUG=INFO -x NCCL_IB_DISABLE=0 -x NCCL_SOCKET_IFNAME=bond0 -x NCCL_IB_GID_INDEX=3 -x NCCL_NET_GDR_LEVEL=2 -x HOROVOD_FUSION_THRESHOLD=0  -x HOROVOD_CYCLE_TIME=0 -x LIGHT_INTRA_SIZE=8 -x LIGHT_2D_ALLREDUCE=1 -x LIGHT_TOPK_ALLREDUCE=1 -x LIGHT_TOPK_THRESHOLD=2097152 -x LD_LIBRARY_PATH -x PATH -mca pml ob1 -mca btl_tcp_if_include bond0 -mca btl ^openib python3 /mnt/pytorch_synthetic_benchmark.py --model resnet50 --batch-size=256
```
GDR 通常在大模型或者集群规模较大时有显著的加速效果，测试结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f771a01d63ca572cf7a5b1078af44d84.png)



:::
</dx-accordion>



## 总结
本文使用环境及测试数据如下：
<table>
<tr>
<th colspan=6>
机器：HCCPNV4h（A100 * 8）+ 100G RDMA + 25G VPC<br>
容器：ccr.ccs.tencentyun.com/qcloud/taco-train:torch111-cu113-bm-0.4.1<br>
网络模型：ResNet50<br>
Batch：256<br>
数据：synthetic data
</th>
</tr>
<tr>
<th rowspan=2>机型</th>
<th rowspan=2>#GPUs</th>
<th colspan=2>Horovod+RDMA</th>
<th colspan=2>LightCC+RDMA</th>
</tr>
<tr>
<th>性能（img/sec）</th>
<th>线性加速比</th>
<th>性能（img/sec）</th>
<th>线性加速比</th>
</tr>
<tr>
<td rowspan=3>HCCPNV4h A100</td>
<td>1</td>
<td>819</td>
<td>-</td>
<td>819</td>
<td>-</td>
</tr>
<tr>
<td>8</td>
<td>6469</td>
<td>98.73%</td>
<td>6469</td>
<td>98.73%</td>
</tr>
<tr>
<td>16</td>
<td>12299</td>
<td>93.85%</td>
<td>12532</td>
<td>95.63%</td>
</tr>
</table>

说明如下：
- 对于 HCCPNV4h/A100，相比开源方案，2机16卡通过 LightCC 可将线性加速比从93.85%提升到95.63%。
- 上述 benchmark 也支持除 ResNet50之外的其他模型，ModelName 请参考 [Keras Applications](https://keras.io/api/applications/)。
- 上述 docker 镜像仅用于 demo，若您需使用自己的 docker 开发环境，请参考 [容器安装用户态 RDMA 驱动](https://cloud.tencent.com/document/product/1573/74101) 安装网卡驱动。
- 如需特定 OS/python/CUDA/tensorflow 版本的 LightCC 加速组件，请联系腾讯云售后获取。




