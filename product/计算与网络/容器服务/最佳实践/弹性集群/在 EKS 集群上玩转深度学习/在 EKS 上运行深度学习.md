## 操作场景

本系列文章将记录在 EKS 上部署深度学习的一系列实践，从直接部署 TensorFlow 到后续实现 Kubeflow 的部署，旨在提供一个较完整的容器深度学习实践方案。


## 前提条件


本文将在上一篇文档 [构建深度学习容器镜像](https://cloud.tencent.com/document/product/457/60220) 基础上继续操作，利用自建集群，在 EKS 上运行深度学习任务。
自建镜像已上传到镜像仓库中：`ccr.ccs.tencentyun.com/carltk/tensorflow-model`，无需重新构建，可以直接拉取使用。



## 操作步骤


### 创建 EKS 集群

请参见 [创建集群](https://cloud.tencent.com/document/product/457/39813) 文档创建 EKS 集群。
>?由于需要运行 GPU 训练任务，在创建集群时，请注意选择的容器网络所在区的支持资源，选择支持 GPU 的可用区，如下图所示：
![](https://main.qcloudimg.com/raw/58034799229973690611ef067cec37b5.png)


### 创建 CFS 文件系统（可选）

容器将在任务结束后，自动删除容器并且释放资源。因此为了实现对模型和数据的持久化存储，建议通过挂载外部存储的方式持久存储数据。目前支持 [云硬盘 CBS](https://cloud.tencent.com/document/product/362)、[文件存储 CFS](https://cloud.tencent.com/document/product/582)、[对象存储 COS](https://cloud.tencent.com/document/product/436) 等方式。

本文示例将利用 NFS 盘的方式，使用 CFS，实现于多读多写的持久化存储。

#### 创建文件存储

1. 登录 [文件存储 CFS](https://console.cloud.tencent.com/cfs/fs) 控制台，进入“文件系统”页面。
2. 单击**创建**，在弹出的“新建文件系统”页面中，选择文件系统类型，并单击**下一步:详细设置**。
3. 在“详细设置”页面进行相关配置，CFS 类型信息与配置细节可参见 [创建文件系统及挂载点](https://cloud.tencent.com/document/product/582/9132) 文档。如下图所示：
![](https://main.qcloudimg.com/raw/60f6718380420de728392c6a93cf6fd9.png)
>!创建的 CFS 地域，需确保与集群在同一地域。
4. 确认无误之后单击**立即购买**并完成付费即可创建文件存储。


#### 获取文件系统挂载信息

1. 在“文件系统”页面，单击需获取子目标路径的文件系统 ID，进入该文件系统详情页。
2. 选择**挂载点信息**页签，从 “Linux下挂载” 获取该文件系统挂载信息。如下图所示：
![](https://main.qcloudimg.com/raw/ff3df7a80f7a5755b0dc54062b661056.png)
>?在挂载点详细中需要记住 IPv4 地址，IPv4 将作为 NFS 路径，后续配置挂载时需要，例如 `10.0.0.161:/`。



### 创建训练任务

本文任务以 MNIST 手写数字识别数据集，加两层 CNN 为例，相关示范镜像为上一章 [自建镜像](https://console.cloud.tencent.com/tke2/registry/user/self/detail/tag?rid=5&reponame=carltk%2Ftensorflow-model)，如需自定义镜像，请参见 [深度学习容器镜像构建](https://cloud.tencent.com/document/product/457/60220) 文档。以下提供两种创建任务的方式。


<dx-tabs>
::: 控制台操作指引
由于深度学习任务的性质，本文以部署 Job 节点为例。如何部署 Job 请参见 [Job 管理](https://cloud.tencent.com/document/product/457/31708) 文档。
以下提供控制台的部署范例：
1. 在**数据卷（选填）**配置项中，选择 NFS 盘，并输入上述步骤创建的 CFS 名称和 IPv4地址。如下图所示：
![](https://main.qcloudimg.com/raw/88778dcc49791bb5114b24b987152d51.png)
2. 在**实例内容器**中的**挂载点**配置项里，选择数据卷，并配置挂载点。如下图所示：
![](https://main.qcloudimg.com/raw/d433dada54f0f2bd3c186e0c2e039268.png)
[](id:precautions)
>!
>- 因为数据集可能需要联网下载，所以需要配置对集群的外网访问。详情请参见常见问题 [公网访问相关](https://cloud.tencent.com/document/product/457/60222)。
>- 选择 GPU 型号后，在填写 request 和 limit 时需要为容器分配符合 [资源规格](https://cloud.tencent.com/document/product/457/39808) 的 CPU 和内存，实际填写并不严格要求精确到个位。
  在控制台中配置，也可以选择删除默认配置以留空，即为“不限制”，也会有对应的计费规格；更推荐这种做法。
>- 容器运行命令 command 继承 Docker 的 CMD 字段，而 CMD 指令首选 exec 形式，不调用 shell 命令。这意味着不会发生正常的 shell 处理。因此命令需要 shell 形式运行，就需要在前面添加 `"sh","-c"`。
  在控制台输入多个命令和参数时，每个命令单独一行（以换行为准）。
:::
::: Kubectl 操作指引
您还可以使用 YAML 文件创建任务。
1. 准备 YAML 文件，示例 gpu_pod.yaml 如下：
<dx-codeblock>
:::  yaml
apiVersion: v1
kind: Pod
metadata: 
  name: tf-cnn
  annotations: 
    #eks.tke.cloud.tencent.com/cpu: "8"
    #eks.tke.cloud.tencent.com/gpu-count: "1"
    eks.tke.cloud.tencent.com/gpu-type: T4
    #eks.tke.cloud.tencent.com/mem: 32Gi
spec: 
  containers: 
  - name: tf-cnn
    image: hkccr.ccs.tencentyun.com/carltk/tensorflow-model:latest # 训练任务的镜像
    env:  
    - name: MODEL_DIR
      value: /tf/model
    - name: DATA_DIR
      value: /tf/data
    command: 
      - "sh"
      - "-c"
      # 触发训练任务的脚本
      - "python3 official/vision/image_classification/mnist_main.py \ 
        --model_dir=$MODEL_DIR \
        --data_dir=$DATA_DIR \
        --train_epochs=5 \
        --distribution_strategy=one_device \
        --num_gpus=1 \
        --download"
    resources: 
      limits: 
        #cpu: "8" 
        #memory: 32Gi
        nvidia.com/gpu: "1" 
      requests: 
        #cpu: "8"
        #memory: 32Gi
        nvidia.com/gpu: "1" 
    volumeMounts: 
    - name: tf-model-cfs
      mountPath: /tf
  volumes:  
  - name: tf-model-cfs   #训练结果持久化，保存到CFS
    nfs:  
      path: /            #此处填写CFS保存的根目录
      server: 10.0.1.8   #此处填写之前创建的CFS的IPv4地址
  restartPolicy: OnFailure
:::
</dx-codeblock>
2. 执行以下命令完成部署。
```sh
kubectl create -f [yaml_name]
```
<dx-alert infotype="notice" title="">
除了控制台操作指引中提到的 [注意事项](#precautions)，还需注意：
- 在 YAML 文件中需使用 Annotations 声明资源分配，详情请参见 [Annotation 说明](https://cloud.tencent.com/document/product/457/44173)。同样需要注意的是不同 GPU 对应不同的 CPU、内存选项，建议按需填写。
- 此处数据卷使用的是 NFS 。若需使用其他数据卷进行持久化存储，请参见 [其他存储卷使用说明](https://cloud.tencent.com/document/product/457/31713)。
- Annotation 可以**只保留** `eks.tke.cloud.tencent.com/gpu-type` ，**不需要其他项**。如果写上了 `/gpu-count`，那么 `cpu` 和 `mem` 也需要一起写上（本文**不推荐加上其他项**。不加不会影响实际效果，加了之后未按规格填写可能会报 OOM 错误）。
- 在 GPU 的调度中，对 `nvidia.com/gpu` 而言，**limits 是必须且仅需填写**。如果只写 Annotation ，将出现找不到卡的报错。如果只填 limits ，该值将被作为 request 。如果也写上 request ，二者值必须相等。详情请参见 K8S 文档 [调度 GPUs](https://kubernetes.io/zh/docs/tasks/manage-gpus/scheduling-gpus/)（这里同样**不推荐在 request 和 limits 中加上 cpu 和 memory 的设置**，理由同上）。
</dx-alert>
:::
</dx-tabs>





### 查看运行结果

以下提供控制台和命令行两种方式查看运行结果：

<dx-tabs>
::: 控制台查看
在创建 Job 之后，默认进入 Job 管理页面。您也可以通过以下步骤进入 Job 管理页面：
1. 登录容器服务控制台，在左侧导航栏中单击**弹性容器** > **[弹性集群](https://console.cloud.tencent.com/tke2/ecluster)**。
2. 在弹性集群列表中，单击需要查看的事件集群 ID，进入集群管理页面。
3. 选择**工作负载** > **Job**，在 Job 列表中单击上述步骤创建的 Job。
	- 选择**事件**页签在查看事件，如下图所示：
	![](https://main.qcloudimg.com/raw/95eb57fa00729e0a4362fad69922ea0c.png)
	- 选择**日志**页签查看日志，如下图所示：
	![](https://main.qcloudimg.com/raw/7b426961d27dbc10a4c3e9df82a7dcc8.png)
	![](https://main.qcloudimg.com/raw/1c62f6739885af581885ad43a55c15d7.png)
:::
::: 命令行查看
您可以使用命令查看事件或日志：
- 执行以下命令查看事件：
```sh
kubectl describe pod [name]
```
如下图所示：
![](https://main.qcloudimg.com/raw/65020975db4da78481d1453034346ede.png)
- 执行以下命令持续输出日志：
```sh
kubectl logs -f [pod_name]
```
如下图所示：
![](https://main.qcloudimg.com/raw/f38ed0501b8a0fdda2049d11b9c477e4.png)
![](https://main.qcloudimg.com/raw/1cc1ffe53e8c03951fe70ccf53b8d8c6.png)
因为 EKS 即用即消的特性，导致如果需要查看日志，必须当且仅当 Pod 处于 Running 状态时才可查看。解决方法请参见常见问题 [日志采集相关](https://cloud.tencent.com/document/product/457/60223)。

#### 查看存储
如果已经按照前面的配置 NFS ，此时可以前往挂载点，查看 NFS 内存储：
1. 执行以下命令进入相关挂载目录，查看是否存在相关目录。
```shell
cd /mound_data
```
如下图所示：
![](https://main.qcloudimg.com/raw/dc20d01b4b200e12520d901c5c087305.png)
2. 进入 model 目录，查看目录下是否有相关数据。如下图所示：
![](https://main.qcloudimg.com/raw/7850fee6d7bffdfb7aa25c96b2f6dee7.png)
3. 进入 data 目录，查看目录下是否有相关数据。如下图所示：
![](https://main.qcloudimg.com/raw/c70c91fe9911cc71234740905f233616.png)
:::
</dx-tabs>





## 相关操作

### 在 TKE 上使用 GPU 部署深度学习任务

在 TKE 上部署和 EKS 的部署几乎没有区别。以 kubectl 通过 YAML 部署为例，有以下两点改动：

- 创建 TKE 节点时，选择带有 GPU 的节点。详情请参见 [新建 GPU 云服务器](https://cloud.tencent.com/document/product/457/32207#newGPUService) 文档。
- 因为节点自带 GPU 资源，因此无需 Annotations 和 Resources。在实践操作汇总，您可以保留 Annotations，TKE 不会处理这部分。Resources 则建议注释掉，因为在某些情况下可能会导致不合理的资源需求。




## 常见问题

在进行本实践过程中遇到的问题，请参见 [常见问题](https://cloud.tencent.com/document/product/457/60226) 文档进行排查解决。
