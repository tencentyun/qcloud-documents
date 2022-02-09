目前 TI-ACC 处于公测阶段，请参考以下使用要求和步骤进行使用。

## 使用要求
TI-ACC 训练加速仅支持以下操作系统、Python 版本、设备类型、框架版本及镜像版本：
- 操作系统：Linux
- Python 版本：Python 3.6
- 设备类型：GPU 支持 CUDA 10.0、10.1、10.2、11.1
- 框架版本：Tensorflow1.15，PyTorch 1.7.1、1.8.1、1.9.0
- 镜像版本：

<table>
     <tr>
         <th>框架类型</th>  
         <th>仓库地址</th>  
         <th>镜像版本</th>  
     </tr>
  <tr>      
      <td rowspan="3">PyTorch</td>   
      <td rowspan="4">tiacc-test.tencentcloudcr.com/ti-acc/ti-accv1.0</td>   
      <td>tiacc-training-v1.0.0-torch1.7.1-cu101-py36-ubuntu18.04</td>   
     </tr> 
  <tr>
      <td>tiacc-training-v1.0.0-torch1.8.1-cu102-py36-ubuntu18.04</td>   
     </tr> 
  <tr>      
    <td>tiacc-training-v1.0.0-torch1.9.0-cu111-py38-ubuntu18.04</td>    
     </tr> 
	<tr>      
    <td>TensorFlow</td>    
		<td>tiacc-training-v1.0.0-tensorflow1.15.5-cu100-py36-ubuntu18.04</td>    
    </tr> 
</table>

## 使用步骤
### 步骤1：创建 TKE 集群

参考 [TKE 创建集群](https://cloud.tencent.com/document/product/457/54231) 的指南创建 TKE 集群实例。
![](https://qcloudimg.tencent-cloud.cn/raw/c3e76d577081bc2814df825f3d039a80.png)

### 步骤2：申请临时登录指令
线下 [申请](https://cloud.tencent.com/apply/p/vl6fzemdq1) 加速产品私有镜像仓库临时登录指令，并创建镜像拉取密钥imagePullSecrets，参考如下命令：

```
kubectl create secret docker-registry tiacc-reg --docker-server=
tiacc-test.tencentcloudcr.com --docker-username=<your-name> --docker-password=<your-pword>
```
>?`<your-pword>`为临时登录指令。


### 步骤3：使用 TI-ACC 训练加速

#### 使用训练加速
在自己的训练代码里使用 TI-ACC 提供的训练加速能力，训练加速中的通信加速能力通过兼容原生的 DDP 工具提供，用户无需修改原生的使用代码可直接进行使用，数据 IO 优化、自适应 FP16 都通过封装好的简单函数/类进行提供，用户仅需增加几行代码便可使用。


#### 使用 DDP 分布式训练通信优化（PyToch+DDP）
以兼容原生 DDP 的方式启动训练脚本，无需进行训练代码的修改，启动命令参考示例如下：
```
python3 -u -m tiacc_training.torch.distributed.launch --nproc_per_node $GPUS_PER_NODE --nnodes $NNODES --node_rank $NODE_RANK --master_addr $MASTER_ADDR --master_port $MASTER_PORT main.py
```

以 mpirun 的方式启动训练脚本，需要在原生 DPP 的训练代码里进行修改，在开头增加如下代码：
```
import tiacc_training.torch.distributed as tdist
tdist.init_tiacc_training()
```

mpirun 方式2机16卡训练脚本的启动命令，参考示例如下：
```
node_list=node1:8,node2:8   //node1和node2为服务器IP或主机名
gpu_num=16  //总的gpu卡数
mpirun --allow-run-as-root -np ${gpu_num} -H ${node_list} -map-by slot -mca btl_tcp_if_include eth0 -mca oob_tcp_if_include eth0 \
-x NCCL_DEBUG=INFO \
-x NCCL_SOCKET_IFNAME=eth0 \
-x NCCL_IB_DISABLE=1 \
-x LIGHT_2D_ALLREDUCE=1 \     //使用2D allreduce通信加速
-x TIACC_TRAINING_FUSION_THRESHOLD=25217728 \    //TIACC_Training会对小的包进行融合通信，TIACC_TRAINING_FUSION_THRESHOLD表示融合后桶的最大字节数
-x TIACC_TRAINING_NUM_NCCL_STREAMS=3 \
python3 \
/demo/TIACC-Training-Benchmarks/pytorch_native_ddp_demo.py  //训练脚本
```

DDP 分布式训练通信优化实测效果：
<table>
     <tr>
         <th>硬件环境</th>  
         <th>模型</th>  
         <th>GPU 卡数</th> 
				 <th>原生 DDP(examples/sec per V100)</th>
				 <th>TI-ACC 通信优化)examples/sec per V100)</th>
     </tr>
  <tr>      
      <td rowspan="3">腾讯云 GN10Xp.20XLARGE320</td>   
      <td rowspan="3">resnext50_32x4d<br>mmcls</td>   
      <td>1（单机）</td>   
			<td>227</td> 
			<td>227</td>
     </tr> 
		  <tr>        
      <td>8（单机）</td>   
      <td>215</td>   
			<td>215</td> 
     </tr>
		 <tr>        
      <td>16（双机）</td>   
      <td>116</td>   
			<td>158.6</td> 
     </tr>
</table>

#### 使用数据 IO 优化（PyToch）

```
#数据预处理，IO优化
import tiacc_training.torch
train_dataset = tiacc_training.torch.tiacc_torch_warp.IndexTFRDataset(tfrecored_dir, tfrecord_file, transform)
```

数据 IO 优化实测效果：

<table>
     <tr>
         <th>硬件环境</th>  
         <th>模型</th>  
         <th>GPU 卡数</th> 
				 <th>原生 DDP(examples/sec per V100)</th>
				 <th>TI-ACC 数据 IO 优化(examples/sec per V100)</th>
     </tr>
  <tr>      
      <td rowspan="2">腾讯云 GN10Xp.20XLARGE320</td>   
      <td>resnet50<br>mmcls</td>   
      <td>8（单机）</td>   
			<td>70.8</td> 
			<td>350.5</td>
     </tr> 
		  <tr>        
      <td>centernet<br>mmdet</td>   
      <td>8（单机）</td>   
			<td>26.4</td> 
			<td>28.6</td>
     </tr>
</table>

tfrecord_file 可使用 TI-ACC 提供的 tools 工具进行生成：

<table>
<thead>
<tr>
<th>工具名称</th>
<th>具体功能</th>
<th>输入参数</th>
<th>使用示例</th>
</tr>
</thead>
<tbody><tr>
<td>tiacc_training/tools/general_image_list.py</td>
<td>生成 tfrecord_file 需要的 image list</td>
<td><li>img_dir（必填）：图片存放路径，下面若干个文件夹，文件夹名为当前类别名<br></li><li>img_list（必填）：希望生成的 list 文件名，格式为 图片路径 当前图片类别标签，<a href="https://tiacc-1308240844.cos.ap-nanjing.myqcloud.com/list文件示例.txt">list文件示例</a><br></li><li>label_str2int（非必填）：类别名（str）到类别id（int）的映射关系文件，若不输入，则会自动生成；<a href="https://tiacc-1308240844.cos.ap-nanjing.myqcloud.com/label_str2int.pkl">label_str2int文件示例</a></li></td>
<td>
<pre style="color:white">
Python3 tiacc_training/tools/general_image_list.py --img_dir val_demo/ --img_list val_list
</pre>
</td>
</tr>
<tr>
<td>tiacc_training/tools/img2tfrecord.py</td>
<td>转 tfrecord 格式，生成数据 IO 优化需要的 tfrecord_file</td>
<td><li>img_dir：图片存放路径<br></li><li>img_list：1中生成 <br></li><li>tfrecords_name：生成数据名称<br></li><li>dataset_type：目前支持<br></li><li>ImageFold、coco 两种<br></li><li>workers（非必填）：默认为0，tfrecord 生成支持多线程，若需加速，可指定大于1的整数</li></td>
<td>
<pre style="color:white">
Python3tiacc_training/tools/img2tfrecord.py --img_dir val_demo --img_list val_list --tfrecords_name val_demo --dataset_type ImageFold
</pre>
</td>
</tr>
</tbody></table>

#### 使用自适应混合精度优化（PyToch）
```
import tiacc_training.torch
import torch.cuda.amp as amp 
scaler = amp.GradScaler() 
#实例化自适应混合精度策略类的对象
policy = tiacc_training.torch .tiacc_torch_warp.MixedPrecision_TrainingPolicy(policy,start_step,hold_step,end_step,test_interval,test_step)
#根据输入的参数得到当前epoch是否需要开启混合精度
mixed_precision = policy.enable_mixed_precision(epoch,lr,loss,scaler=scaler)
with amp.autocast(enabled=mixed_precision):
      outputs = model(inputs)
     loss = criterion(outputs, targets)
scaler.scale(loss).backward()
scaler.step(optimizer)
scaler.update()
```

自适应混合精度优化实测效果：
<table>
     <tr>
         <th>硬件环境</th>  
         <th>模型</th> 
         <th>GPU 卡数</th> 
				 <th>原生 PyTorch(examples/sec per V100)</th>
				 <th>TI-ACC 数据 IO 优化(examples/sec per V100)</th>
				 <th>TI-ACC 数据 IO + 自适应混合精度优化(examples/sec per V100)</th>
     </tr>
  <tr>      
      <td rowspan="2">腾讯云 GN10Xp.20XLARGE320</td>   
      <td>resnet50<br>mmcls</td>   
      <td><nobr>8（单机）</nobr></td>   
			<td>70.8 </td> 
			<td>350.5</td>
			<td>379.2 </td>
     </tr> 
		  <tr>        
      <td>centernet<br>mmdet</td>   
      <td></nobr>8（单机）</nobr></td>   
			<td>26.4</td> 
			<td>28.6</td>
			<td>30.6</td> 
     </tr>
</table>

#### 使用通信优化后的 embedding 变量构造（TensorFlow+PS）
```
#将tensorflow原生的get_variable（）替换为TI-ACC优化后的get_variable（）
import tiacc_training.tensorflow
embeddings = tiacc_training.tensorflow.get_variable(name="embeddings",devices=["/job:ps/replica:0/task:0/CPU:0", "/job:ps/replica:0/task:1/CPU:0"],initializer=tf.compat.v1.random_normal_initializer(0, 0.005),dim=32)
```

#### 使用通信优化后的 embedding lookup 计算（TensorFlow+PS）
```
#将tensorflow原生的embedding_lookup_sparse()替换为TI-ACC优化后的embedding_lookup_sparse()
import tiacc_training.tensorflow
sp_tensor = tiacc_training.tensorflow.SparseTensor(indices=[[0,0],[3,1],[2,2],[1,0]], values=[0,1,2,6], dense_shape=(3,3))sparse_weights = tf.nn.embedding_lookup_sparse(params=embeddings,sp_ids=sp_tensor,name="sparse-weights")
```

embedding 变量构造+lookup 计算优化实测效果：
<table>
     <tr>
         <th>硬件环境</th>  
         <th>模型</th>  
         <th>GPU 卡数</th>  
				 <th>原生 TensorFlow(global_steps/sec per V100)</th> 
				 <th>TI-ACC 优化后 (global_steps/sec per V100)</th> 
     </tr>
  <tr>      
      <td rowspan="2">腾讯云 GN10Xp.20XLARGE320</td>   
      <td> DeepFM</td>   
      <td><nobr>16（双机）</nobr></td>  
			<td>41.9-56</td>
			<td>96.1-103.3 </td>
     </tr> 
  <tr>
      <td>Wide & Deep</td>   
      <td><nobr>16（双机）</nobr></td>
			<td>49.9-69</td>   
      <td>120-128</td>
     </tr> 
</table>


#### 提交分布式加速训练任务
整理多机多卡 yaml 文件并执行，执行命令如下：
```
kubectl create -f benchmark.yaml
```

双机16卡分布式训练 yaml 示例如下：
```
# benchmark.yaml
apiVersion: kubeflow.org/v1
kind: MPIJob
metadata:
  name: TIACC-benchmarks
spec:
  slotsPerWorker: 8
  cleanPodPolicy: Running
  mpiReplicaSpecs:
    Launcher:
      replicas: 1
      template:
         spec:
           containers:
           - image:xxx # TI-ACC训练加速镜像
             name: TIACC-benchmarks
             command:
             - mpirun
             - --allow-run-as-root
             - -np
             - "16"
             - -bind-to
             - none
             - -map-by
             - slot
             - -x
             - NCCL_DEBUG=INFO
             - -x
             - LD_LIBRARY_PATH
             - -x
             - PATH
             - -mca
             - pml
             - ob1
             - -mca
             - btl
             - ^openib
             - python
             - run.py # 训练的代码文件，其中已包含TI-ACC加速能力
         resources:
           limits:
             nvidia.com/gpu: 8
       imagePullSecrets:
         - name: tiacc-reg #上述步骤创建的imagePullSecrets
           

    Worker:
      replicas: 2
      template:
        spec:
          containers:
          - image: mpioperator/tensorflow-benchmarks:latest
            name: tensorflow-benchmarks
            resources:
              limits:
                nvidia.com/gpu: 8
          imagePullSecrets:
             - name: regcred
```
#### 训练加速类/函数说明
##### init_tiacc_training 函数

初始化 DDP 通信加速优化，会默认将原生 DDP 相关的函数调整为调用 TI-ACC 通信加速能力，原生 DDP 相关的主要模块/类包括：torch.distributed和torch.nn.parallel.DistributedDataParallel()。



##### IndexTFRDataset 类
实现实例化训练过程中数据集的功能，底层实现了对于 CV 场景下的图片小文件 IO 的优化。
初始化参数：

| 参数          | 类型     | 是否必填 | 参数说明                                    | 示例                                                         | 默认值 |
| ------------- | -------- | -------- | ------------------------------------------- | ------------------------------------------------------------ | ------ |
| tfrecored_dir | STRING   | 是       | 存放此数据 tfrecord 文件的目录。              | './tfrecord_train_path'                                      | 无     |
| tfrecord_file | STRING   | 是       | 存放此数据 tfrecord index（标签+索引）的文件 | './tfrecord_train_path/train.index'                          | 无     |
| transform     | Callable | 否       | 数据预处理变换方式                          | 'transforms.Compose([         transforms.RandomHorizontalFlip(),     transforms.ToTensor(),        transforms.Normalize(mean=rgb_mean, std=rgb_std)        ])' | None   |

实例化对象：

| 对象    | 类型              | 对象说明                   |
| ------- | ----------------- | -------------------------- |
| dataset | IndexTFRDataset 类 | 训练过程中读取数据集的对象 |

##### adaptfp16.MixedPrecision_TrainingPolicy 类
实现对训练过程中自动混合精度自适应策略的实例化，自适应策略包括时间混合精度、时间学习率混合精度策略、损失函数混合精度策略。


初始化参数：

| 参数               | 类型 | 是否必填 | 参数说明                                                     | 示例 | 默认值 |
| ------------------ | ---- | -------- | ------------------------------------------------------------ | ---- | ------ |
| policy             | INT  | 是       | 自适应混合精度策略<br>0：时间混合精度，适用于通用自适应情况<br>1：时间学习率混合精度策略，适用于训练过程中某一阶段loss波动出现异常的情况<br>2：损失函数混合精度策略，适用于训练过程中 loss 下降过快或过慢情况。 | 0    | 无     |
| start_time         | INT  | 否       | 开启自适应混合精度的开始时间，一般建议设为10。策略为0和1时必填，为2时非必填。 | 10   | 10     |
| end_time           | INT  | 否       | 开启自适应混合精度的结束时间，一般建议设为最后一个 epoch 时间。策略为0和1时必填，为2时非必填。 | 1000 | None   |
| hold_time          | INT  | 否       | 开启策略1时的保持时间，在保持时间内采用统一策略：开启或者不开启。一般建议为训练过程中 loss 异常波动的持续时间。策略为1时必填，为0和2时非必填。 | 20   | None   |
| interval_time      | INT  | 否       | 开启策略2的间隔时间，默认值为1000，即每间隔1000轮 epoch 开启策略2。策略为2时需要填写，为0和1时无需必填。 | 1000 | 1000   |
| interval_hold_time | INT  | 否       | 在 interval_time 间隔时间开启策略2后的保持时间，默认值为100，如interval_time为1000，即在1000-1100，2000-2100开启策略2。策略为2时需要填写，为0和1时无需必填。 | 100  | 100    |

实例化对象：

| 对象   | 类型                            | 对象说明                                     |
| ------ | ------------------------------- | -------------------------------------------- |
| policy | MixedPrecision_TrainingPolicy类 | 训练过程中自动混合精度自适应策略的实例化对象 |

#### enable_mixed_precision 函数方法
属于 MixedPrecision_TrainingPolicy 类，根据输入的参数得到当前 epoch 是否需要开启自动混合精度。

输入参数：

| 参数   | 类型                      | 是否必填 | 参数说明                  | 示例   | 默认值 |
| ------ | ------------------------- | -------- | ------------------------- | ------ | ------ |
| epoch  | INT                       | 是       | 当前的 epoch               | 20     | 无     |
| scaler | torch.cuda.amp.GradScaler | 是       | 梯度缩放实例化对象        | scaler | 无     |
| lr     | float                     | 否       | lr 是当前 epoch 的学习率     | 0.01   | None   |
| loss   | float                     | 否       | loss 是上一轮 epoch 的损失值 | 0.1    | None   |


输出参数：

| 输出参数        | 类型 | 参数说明                                                     |
| --------------- | ---- | ------------------------------------------------------------ |
| mixed_precision | BOOL | 输入的参数得到当前 epoch 是否需要开启自动混合精度，是返回 TRUE，否则返回 FLASE。 |

	
	
