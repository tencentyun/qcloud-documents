## 操作场景
本文介绍如何基于容器服务 TKE Kubeflow 提供的 AI 组件 [MPI Operator](https://cloud.tencent.com/document/product/457/62634) 搭建 TACO Train 分布式训练集群。



## 操作步骤


### 准备环境[](id:Step1)
1. 创建 TKE 集群，其中节点、操作系统请参考以下信息选择，其余配置可参考 [创建集群](https://cloud.tencent.com/document/product/457/32189) 按需选择。
 - **Node节点**：8卡V100（GN10Xp.20XLARGE320 + 25G 网络）或8卡A100（GT4.41XLARGE948 + 50G 网络）。
 - **操作系统**：目前已验证的操作系统为 Ubunut Server 18.04、CentOS 7.8、 Tencent Linux 2.4，请按需选择。
本文示例配置如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/bab40aa4aa80ed6ea0c430ccbb7574ff.png)
2. 登录 [容器服务器控制台](https://console.cloud.tencent.com/tke2/cluster)，选择左侧导航栏中的**云原生AI**。
3. 在 “AI环境” 页面单击**新建**，根据页面提示创建 AI 环境，并为集群安装 Kubeflow 组件 mpi-operator。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/69eb6953c9285d21d0ffc5b40bb5286c.png)
安装成功后，可登录 worker 节点查看存在如下图所示 pod：
<img src="https://qcloudimg.tencent-cloud.cn/raw/bac9d596994435435fe5c23768aa9f01.png" width="918px"/>
4. 参考 [配置 HARP 分布式训练环境](https://cloud.tencent.com/document/product/1573/74099) 配置环境，实现在多机多卡训练场景中使用 HARP 协议栈进行数据交换。



### 创建 Pod[](id:Step2)
1. 使用 yaml 创建 Pod，`taco.yaml` 示例文件如下：
```yaml
apiVersion: kubeflow.org/v1
kind: MPIJob
metadata:
  name: taco-bench
spec:
  slotsPerWorker: 1
  runPolicy:
    cleanPodPolicy: Running
  mpiReplicaSpecs:
    Launcher:
      replicas: 1
      template:
        spec:
          containers:
          - image: ccr.ccs.tencentyun.com/qcloud/taco-train:ttf115-cu112-cvm-0.4.1
            name: mpi-launcher
            command: ["/bin/sh", "-ec", "sleep infinity"]
            resources:
              limits:
                cpu: 1
                memory: 2Gi
    Worker:
      replicas: 4
      template:
        spec:
          containers:
          - image: ccr.ccs.tencentyun.com/qcloud/taco-train:ttf115-cu112-cvm-0.4.1
            name: mpi-worker
            securityContext:
              privileged: true
            volumeMounts:
              - mountPath: /sys/
                name: sys
              - mountPath: /dev/hugepages
                name: dev-hge
              - mountPath: /usr/local/tfabric/tools
                name: tfabric
            resources:
              limits:
                hugepages-1Gi: "50Gi"
                memory: "100Gi"
                nvidia.com/gpu: 8 # requesting 1 GPU
          volumes:
            - name: sys
              hostPath:
                path: /sys/
            - name: dev-hge
              hostPath:
                path: /dev/hugepages/
            - name: tfabric
              hostPath:
                path: /usr/local/tfabric/tools/
```
说明如下：
 - 主机侧一些设备节点和配置文件需要 bind mount 到 Pod 中供 HARP 使用。
 - Pod 需要配置 privileged 权限，否则 HARP 无法读取配置文件。
 - 需要给 Pod 配置大页内存 `hugepages-1Gi`。针对八卡机器可配置 `hugepages=50`，其他机型建议按照 `hugepages=（卡数 × 5+10）`进行配置。
 - `ccr.ccs.tencentyun.com/qcloud/taco-train:ttf115-cu112-cvm-0.4.1` 是 taco-train 的官方 demo 镜像，基于 Ubunut 18.04/python 3.6.9/CUDA 11.2.152/CUDNN 8.1.1/NCCL 2.8.4编译产生，如果有其他的版本需求，请 [联系我们](https://cloud.tencent.com/document/product/1573/74090) 并通过腾讯云售后获取特定版本的加速组件。
2. 执行以下命令，创建 Pod。
```plaintext
kubectl create -f taco.yaml
```
创建成功后，可执行以下命令进行查看：
```plaintext
kubectl get pod
```
返回结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/167f9b5588bd3a58eeec069cfeb4ebdc.png)


### 开始测试[](id:Step3)

1. 执行以下命令，登录 launcher pod。
```plaintext
kubectl exec -it taco-bench-launcher -- bash
```
2. 执行以下命令，执行训练 benchmark。
<dx-alert infotype="explain" title="">
为测试不同的网络模型和节点数量下的性能，mpi launcher pod 未配置为直接启动训练脚本方式。
</dx-alert>
```plaintext
/usr/local/openmpi/bin/mpirun -np 32 -H taco-bench-worker-0:8,taco-bench-worker-1:8,taco-bench-worker-2:8,taco-bench-worker-3:8 --allow-run-as-root -bind-to none -map-by slot -x NCCL_ALGO=RING -x NCCL_DEBUG=INFO -x HOROVOD_MPI_THREADS_DISABLE=1 -x HOROVOD_FUSION_THRESHOLD=0  -x HOROVOD_CYCLE_TIME=0 -x LIGHT_2D_ALLREDUCE=1 -x LIGHT_TOPK_ALLREDUCE=1 -x LIGHT_TOPK_THRESHOLD=2097152 -x LIGHT_INTRA_SIZE=8 -x LD_LIBRARY_PATH -x PATH -mca btl_tcp_if_include eth0 python3 /mnt/tensorflow_synthetic_benchmark.py --model=VGG16 --batch-size=128
```
如需切换到 Horovod 进行对比测试，则请执行如下命令删除 TACO 相关组件，安装开源 Horovod：
```plaintext
// 卸载HARP加速库
for i in `kubectl get pods | grep worker | awk '{print $1}'`; do kubectl exec $i -- bash -c 'mv /usr/lib/x86_64-linux-gnu/libnccl-net.so /mnt/'; done
```
```plaintext
// 卸载LightCC
for i in `kubectl get pods | grep worker | awk '{print $1}'`; do kubectl exec $i -- bash -c 'pip uninstall -y light-horovod;echo'; done
```
```plaintext
// 安装horovod(耗时8分钟左右)
for i in `kubectl get pods | grep worker | awk '{print $1}'`; do kubectl exec $i -- bash -c 'export PATH=/usr/local/openmpi/bin:$PATH;HOROVOD_WITH_MPI=1 HOROVOD_GPU_OPERATIONS=NCCL HOROVOD_WITH_TENSORFLOW=1 HOROVOD_NCCL_LINK=SHARED pip3 install --no-cache-dir horovod==0.21.3'; done
```
```plaintext
// 检查确认所有的worker都已经成功horovod
for i in `kubectl get pods | grep worker | awk '{print $1}'`; do kubectl exec $i -- bash -c 'pip show horovod;echo'; done
```



### 测试结果[](id:Step4)
- 下图展示了在 CVM GPU 训练集群下，各开源模型使用 TACO train 进行分布式训练的加速效果：
![](https://qcloudimg.tencent-cloud.cn/raw/2712ee9e78aa4b47c56deb46541189e8.png)
![](https://qcloudimg.tencent-cloud.cn/raw/e60c3e98ad406fb2b925321a53f7f405.png)
参数值如下：
<table>
<thead>
<tr>
<th><strong>network</strong></th>
<th><strong>参数量（millions）</strong></th>
</tr>
</thead>
<tbody><tr>
<td><strong>inceptionv3</strong></td>
<td>25</td>
</tr>
<tr>
<td><strong>resnet101</strong></td>
<td>44</td>
</tr>
<tr>
<td><strong>vgg16</strong></td>
<td>138</td>
</tr>
<tr>
<td><strong>transformer-xl</strong></td>
<td>257</td>
</tr>
</tbody></table>
可发现，随着网络模型参数量的增加，TACO 相比 Horovod 的提升效果愈加明显，Transformer-XL 上甚至有高达两倍多的性能提升。
- 下图表明无论是 ResNet50 还是Transformer-XL，在双机16卡 A100的训练环境下，CVM 实例（GT4.41XLARGE948 + 50G VPC）通过 HARP 加速后，能够提供接近裸金属云服务器100G RDMA 产品（HCCPNV4h ）的性能。
![](https://qcloudimg.tencent-cloud.cn/raw/963414f3122f18f61fb15655b46adf62.png)
![](https://qcloudimg.tencent-cloud.cn/raw/6440479d100566a1dd1f9935099f561c.png)


## 总结
- 在相同的25G VPC 环境下，相比于业内开源方案 Horovod，TACO 可以提供20% - 200%左右的性能提升。原理上模型参数越多，性能提升越明显。
- 在50G的 VPC 环境下，TACO 可以提供类似100G RDMA 的训练性能。

