目前TI-ACC处于公测阶段，请参考以下使用要求和步骤进行使用。

## 使用要求
TI-ACC 推理加速仅支持以下操作系统、Python 版本、设备类型、框架版本及镜像版本：
- 操作系统：Linux
- Python 版本：Python 3.6
- 设备类型：GPU 支持 CUDA 10.0、10.2、11.1
- 框架版本：Tensorflow1.15，PyTorch 1.7.1、1.8.1、1.9.0
- 镜像版本：

<table>
     <tr>
         <th>框架类型</th>  
         <th>仓库地址</th>  
         <th>镜像版本</th>  
     </tr>
  <tr>      
      <td rowspan="5">PyTorch</td>     
      <td  rowspan="6">tiacc-test.tencentcloudcr.com/ti-acc/ti-accv1.0</td> 
      <td>tiacc-inference-v1.0.0-torch1.7.1-cu102-py36-ubuntu18.04</td>   
     </tr> 
  <tr>      
      <td>tiacc-inference-v1.0.0-torch1.8.1-cu102-py36-ubuntu18.04</td>   
     </tr> 
   <tr>      
      <td>tiacc-inference-v1.0.0-torch1.8.1-cu111-py36-ubuntu18.04</td>   
     </tr> 
	<tr>
	<td>tiacc-inference-v1.0.0-torch1.9.0-cu102-py36-ubuntu18.04</td>
	</tr>
  <tr>
	<td>tiacc-inference-v1.0.0-torch1.9.0-cu111-py36-ubuntu18.04</td>
	</tr>
	<tr>
	<td>TensorFlow</td>
	<td>tiacc-inference-v1.0.0-tensorflow1.15-cu100-py36-ubuntu18.04</td>
	</tr>
</table>

## 使用步骤
### 步骤1：创建 TKE 集群
参考 [TKE 创建集群](https://cloud.tencent.com/document/product/457/54231) 的指南创建 TKE 集群实例。
![](https://qcloudimg.tencent-cloud.cn/raw/c3e76d577081bc2814df825f3d039a80.png)

### 步骤2：申请临时登录指令
线下 [申请](https://cloud.tencent.com/apply/p/vl6fzemdq1) 加速产品私有镜像仓库临时登录指令，并创建镜像拉取密钥 imagePullSecrets，参考如下命令：

```
kubectl create secret docker-registry tiacc-inference-reg --docker-server=
tiacc-test.tencentcloudcr.com --docker-username=<your-name> --docker-password=<your-pword>
```
>?`<your-pword>`为临时登录指令。


### 步骤3：使用加速
#### 使用推理加速
推理加速容器构建，执行命令如下：

```
kubectl create -f tiacc-inference-test.yaml
```

yaml 示例如下：
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tiacc-inference-test
spec:
  progressDeadlineSeconds: 600
  replicas: 1
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      k8s-app: tiacc-inference-test
      qcloud-app: tiacc-inference-test
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
    type: RollingUpdate
  template:
    metadata:
      creationTimestamp: null
      labels:
        k8s-app: tiacc-inference-test
        qcloud-app: tiacc-inference-test
    spec:
      containers:
      - env:
        - name: NVIDIA_DRIVER_CAPABILITIES
          value: compute
        - name: NVIDIA_VISIBLE_DEVICES
          value: "0"
        - name: PATH
          value: /usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
        - name: CUDA_VERSION
          value: 10.2.89
        - name: CUDA_PKG_VERSION
          value: 10-2=10.2.89-1
        - name: LD_LIBRARY_PATH
          value: /usr/local/nvidia/lib:/usr/local/nvidia/lib64
        - name: NVIDIA_REQUIRE_CUDA
          value: cuda>=10.2 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411 brand=tesla,driver>=418,driver<419 brand=tesla,driver>=440,driver<441
        - name: NCCL_VERSION
          value: 2.9.6
        - name: LIBRARY_PATH
          value: /usr/local/cuda/lib64/stubs
        image: tiacc-test.tencentcloudcr.com/tiacc/tiacc_pytorch:tiacc-inference-0.5.0-torch1.8.1-cu102-py36-ubuntu18.04 # 推理加速image地址
        imagePullPolicy: Always
        name: tiacc-inference-test
        resources:
          limits:
            cpu: "1"
            memory: 4Gi
            nvidia.com/gpu: "1"
          requests:
            cpu: "1"
            memory: 1Gi
        securityContext:
          privileged: false
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      imagePullSecrets:
      - name: tiacc-inference-reg # 上述步骤创建的imagePullSecrets
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
```

容器构建完成后，python3.6 运行如下代码：

```
#引入部分引入推理加速包
import tiacc_inference
#模型定义和训练，得到input_model
...
#对训练完成的model进行推理加速
output_model,optimized_report = tiacc_inference.optimize(input_model,optimization_level,device_type,input_shapes,input_nodes_names,output_nodes_names,test_data,save_path,optimization_config)

```


#### 推理实测效果
<table>
     <tr>
         <th>硬件环境</th>  
         <th>模型</th>  
         <th>Batchsize</th> 
				 <th>torchscript（ms）</th>
				 <th>TI-ACC（ms）</th>
				 <th>加速比</th>
     </tr>
  <tr>      
      <td rowspan="13">腾讯云 GN7.2XLARGE32</td>   
      <td rowspan="2">resnet50<br>(torchvision)<br>224x224</td>   
      <td>1</td>   
			<td>5.4622 </td> 
			<td>1.1482</td> 
			<td>4.8x</td> 
     </tr> 
  <tr>
      <td>8</td>   
      <td>27.062</td>
			<td>4.5707</td>
			<td>5.9x</td>
     </tr> 
  <tr> 
	     <td rowspan="2">resnet50<br>(mmcls)<br>224x224</td>   
       <td>1</td>   
      <td>7.7667</td>   
      <td> 4.3958 </td>   
			<td>1.8x</td>
     </tr> 
		   <tr>      
       <td>8</td>   
      <td>36.806</td>   
      <td>14.1152</td> 
			<td>2.6x</td>
     </tr> 
		 		<tr>      
       <td rowspan="2">centernet<br>640x640</td>   
      <td>1</td>   
			<td>20.9992</td> 
			<td>4.7775</td>
			<td>4.4x</td>
     </tr> 
  <tr>
      <td>8</td>   
      <td>170.5488</td>
			<td>34.3523</td>
			<td>5.0x</td>
     </tr> 
			<tr>      
      <td rowspan="2">yolov3<br>(ultralytics)<br>640x640</td>   
      <td>1</td>   
			<td>47.19</td> 
			<td>10.3671</td>
			<td>4.5x</td>
     </tr> 
  <tr>
      <td>8</td>   
      <td>302.983</td>
			<td>82.6971</td>
			<td>3.7x</td>
     </tr> 
  <tr>  
	    <td>Cascade Mask R-CNN<br>(mmdet)<br>2016x3008</td>  
      <td>1</td>   
      <td>600.0671</td>   
      <td>165.8467</td> 
			<td>3.6x</td>
     </tr> 
		   <tr> 
			 <td>Faster R-CNN<br>(mmdet)<br>1088x800</td>  
       <td>1</td>   
      <td>107.3483</td>   
      <td>35.5021</td>
			<td>3.0x</td>
     </tr> 
		 <tr>      
       <td>Vision Transformer<br>224x224</td>   
      <td>8</td>   
			<td>28.887</td> 
			<td>10.53</td>
			<td>2.7x</td>
     </tr> 
  <tr>
	<td>Wide & Deep<br>(NVIDIA DeepLearningExamples)</td>   
      <td>512</td>   
      <td>15.7</td>
			<td>4.436</td>
			<td>3.5x</td>
     </tr> 
  <tr> 
	<td>DeepFM<br>(NVIDIA DeepLearningExamples)</td>   
       <td>512</td>   
      <td>12.91</td>   
      <td>4.51</td>
			<td>2.9x</td>
     </tr> 
</table>



#### 推理加速接口说明
- 输入参数及说明

<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>是否必填</th>
<th>参数说明</th>
<th>默认值</th>
<th>示例</th>
</tr>
</thead>
<tbody><tr>
<td>input_model</td>
<td>多种（STRING+torch.jit.ScriptModule 类型 + GraphDef 类型）</td>
<td>是</td>
<td>输入待优化的原始模型。<br>如果是 Pytorch 模型，支持以下格式：<br></li><li>torch.jit.ScriptModule 导出的模型文件，以.pt、.pth 为后缀（计算图结构+参数的模型）。<br></li><li>torch.jit.ScriptModule 对象。<br>如果是 tensorflow 模型，支持以下格式：<br></li><li>SavedModel 方式保存的模型文件夹路径。<br></li><li>Frozen&nbsp;Graph 方式保存的模型文件.以 .pb 为后缀。<br></li><li>GraphDef 对象。</li></td>
<td>无</td>
<td>字符串格式的路径，<code>'./lzz'</code>、<code>'./lzz.pb'</code></td>
</tr>
<tr>
<td>optimization_level</td>
<td>INT</td>
<td>是</td>
<td>推理加速的优化级别。<br>0：无损。<br>1：FP16。</td>
<td>无</td>
<td>0</td>
</tr>
<tr>
<td>device_type</td>
<td>INT</td>
<td>是</td>
<td>运行设备。0：GPU。</td>
<td>无</td>
<td>0</td>
</tr>
<tr>
<td>input_shapes</td>
<td>多种（LIST[STRING]+LIST[LIST)]+LIST[DICT]）</td>
<td>是</td>
<td>模型输入的相关信息，主要包括形状 shape 和类型 data_type 最外层是 list，其中每个元素代表一个输入节点 input，每个 input 允许 str、list、dict 的格式，允许嵌套：<br><li>str 用于单一节点固定输入尺寸。<br><li>list 用于多节点固定尺寸。<br><li>dict 用于输入非固定尺寸或者非 float 类型，对应的 key 为 'seperate|range,int|float|half'，seperate 静态，value 填写的是 range 表示动态，value 填写的是 min 和 max。</td>
<td>无</td>
<td><li>单一节点固定尺寸：[ '1 * 3 * 224 * 224' ]<br><li>多节点固定尺寸：[[ '1 * 3 * 224 * 224' ],[ '1 * 3 * 512 * 512' ]]<br><li>单节点非固定静态尺寸：[{'seperate': ['1 * 3 * 224 * 224','2 * 3 * 224 * 224']}]<br><li>单节点非固定动态尺寸：[{'range': ['1 * 3 * 224 * 224','10 * 3 * 224 * 224']}]</td>
</tr>
<tr>
<td>inputs_nodes_names</td>
<td>LIST[STRING]</td>
<td>否</td>
<td>原始模型的输入节点。如果不指定该参数，则系统尝试自动推断。</td>
<td>None</td>
<td>[“lzz_input1”,“lzz_input2”]</td>
</tr>
<tr>
<td>outputs_nodes_names</td>
<td>LIST[STRING]</td>
<td>否</td>
<td>原始模型的输出节点。如果不指定该参数，则系统尝试自动推断。</td>
<td>None</td>
<td>[“lzz_output”]</td>
</tr>
<tr>
<td>test_data</td>
<td>多种（LIST[DICT[STRING, np.ndarray]]+LIST[Tuple[torch.tensor, ]]）</td>
<td>否</td>
<td>用于模型推理速度对比的测试数据。用户给出则使用用户给出的测试数据；如果用户不给出，那么 TI-ACC 来自动提供测试数据。对于不同类型的模型，其测试数据格式存在差异， PyTorch 模型的测试数据为若干组输入Tensor Tuple，类型为LIST[Tuple[torch.tensor, ]]。TensorFlow 模型的测试数据为包含若干组 feed_dict 的列表，类型为 LIST[DICT[STRING, np.ndarray]]</td>
<td>None</td>
<td>-</td>
</tr>
<tr>
<td>save_path</td>
<td>STRING</td>
<td>否</td>
<td>优化模型的保存路径。如果需要将优化后的模型进行保存，则必填。如果是 pytorch 模型格式，支持以下方式：torch.jit.ScriptModule 保存方式，即填写导出的模型文件，以 .pt/.pth 为后缀；如果是 tensorflow 模型格式，支持以下方式：savemodel 保存方式，即填写模型文件夹路径；frozen graph 保存方式，即填写保存的模型文件名。</td>
<td>None</td>
<td><code>‘../lzz’</code>、<code>‘../lzz.pb’</code>、<code>‘../lzz.pbt’</code></td>
</tr>
<tr>
<td>optimization_config</td>
<td>tiacc 中自定义的 OptimizeConfig 类</td>
<td>否</td>
<td>用于指导模型优化 tf.nn.embedding_lookup_sparse 层。设置参数时，需包含前缀 "tiemb/"。<br>参数包括：最大 batch 数（max_batch_size、int 类型），slot 数（slot_num、int 类型），最大 nnz 数（max_nnz、int 类型），gpu cache 使用率（cache_percentage、float 类型），cpu cache 使用率（cpu_cache_percentage、float 类型），gpu cache命中率阈值（hit_rate_threshold、float 类型），是否开启分布式模式（enable_distributed、bool 类型）。另外还有 output_names 参数，该参数类型和 output_nodes_names 相同。如果用户手动设置了 output_nodes_names，tiacc 内部自动将 names 同步到 output_names 参数中。用户应尽量使用 output_nodes_names 进行设置，而非在 config 中设置。</td>
<td>output_names、max_batch_size、slot_num、max_nnz 无默认值 cache_percentage 默认值为0.2cpu_cache_percentage 默认值为 1.0hit_rage_threshold 默认值为 0.95enable_distributed 默认值为 false</td>
<td><pre><code>optimization_config = tiacc_tf<span class="hljs-selector-class">.OptimizeConfig</span>()
optimization_config<span class="hljs-selector-class">.parameter_map</span><span class="hljs-selector-attr">[<span class="hljs-string">"tiemb/max_batch_size"</span>]</span><span class="hljs-selector-class">.i</span> = batch_size
optimization_config<span class="hljs-selector-class">.parameter_map</span><span class="hljs-selector-attr">[<span class="hljs-string">"tiemb/slot_num"</span>]</span><span class="hljs-selector-class">.i</span> = slot_num
optimization_config<span class="hljs-selector-class">.parameter_map</span><span class="hljs-selector-attr">[<span class="hljs-string">"tiemb/max_nnz"</span>]</span><span class="hljs-selector-class">.i</span> = max_nnz
optimization_config<span class="hljs-selector-class">.parameter_map</span><span class="hljs-selector-attr">[<span class="hljs-string">"tiemb/cache_percentage"</span>]</span><span class="hljs-selector-class">.f</span> = <span class="hljs-number">0.2</span>
optimization_config<span class="hljs-selector-class">.parameter_map</span><span class="hljs-selector-attr">[<span class="hljs-string">"tiemb/cpu_cache_percentage"</span>]</span><span class="hljs-selector-class">.f</span> = <span class="hljs-number">1.0</span>
optimization_config<span class="hljs-selector-class">.parameter_map</span><span class="hljs-selector-attr">[<span class="hljs-string">"tiemb/hit_rate_threshold"</span>]</span><span class="hljs-selector-class">.f</span> = <span class="hljs-number">0.95</span>
optimization_config<span class="hljs-selector-class">.parameter_map</span><span class="hljs-selector-attr">[<span class="hljs-string">"tiemb/enable_distributed"</span>]</span><span class="hljs-selector-class">.b</span> = False</code></pre></td>
</tr>
</tbody></table>

- 输出参数及说明

<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>参数说明</th>
<th>示例</th>
</tr>
</thead>
<tbody><tr>
<td>optimized_report</td>
<td>OptimizedReport</td>
<td>输出的优化报告</td>
<td><pre style="color:white">
optimized_report: {
  // 软件环境，包括框架、CUDA。
  "software_environment": [
    {
      "software": "tensorflow",
      "version": "1.15.0"
    },
    {
      "software": "cuda",
      "version": "9.0.176"
    },
    {
      "software": "cuDNN",
      "version": "7.4"
    },
    {
      "software": "TensorRT",
      "version": "5"
    }
  ],
  // 硬件环境。
  "hardware_environment": {
    "device_type": "gpu"
    "microarchitecture": "V100"
  },
  // 测试数据信息。
    "test_data_info": {
    "test_data_source": "user provided/tiacc provided",       
    "test_data_shape": " (1, 9240)" ,                                                                              
    "test_data_type": " int32"
  },
  // 优化结果。
"optimization_result": {
    "baseline": "10.00 ms",   
    "optimized": "4.38 ms",   
    "speedup": "2.28"         
  }
}
</td>
</tr>
</tbody></table>

- 输出报告字段含义

<table>
     <tr>
         <th>字段</th>  
         <th>子字段</th>  
         <th>描述</th> 
				 <th>示例</th>
     </tr>
  <tr>      
      <td rowspan="2">software_environment</td>   
      <td>software</td>   
      <td rowspan="2">软件环境，包括：模型训练框架+版本、CUDA+版本、cudnn+版本、tensorRT+版本。</td>   
			<td rowspan="2"> 
			<pre style="color:white">
 "software_environment": [
    {
      "software": "tensorflow",
      "version": "1.15.0"
    },
    {
      "software": "cuda",
      "version": "9.0.176"
    },
    {
      "software": "cuDNN",
      "version": "7.4"
    },
    {
      "software": "TensorRT",
      "version": "5"
    }
  ]
	</pre>
	</td> 
  </tr> 
  <tr>
      <td >version</td>   
     </tr> 
  <tr>      
      <td rowspan="2">hardware_environment</td>   
      <td>device_type</td>   
      <td rowspan="2">硬件环境，包括 device_type 类型以及显卡类型。</td>   
			<td rowspan="2"> 
			<pre style="color:white">
  "hardware_environment": {
    "device_type": "gpu"
    "microarchitecture": "V100"
  }
	</pre>
			</td> 
     </tr> 
  <tr>
      <td >microarchitecture</td>   
     </tr> 
		  <tr>      
      <td rowspan="3">test_data_info</td>   
      <td>test_data_source</td>   
      <td rowspan="3">测试数据信息，包括测试数据来源和测试数据的形状和类型。数据来源有两类，如果用户本身提供了测试数据，则为：user provided，如果用户没有提供，则为：tiacc provided，即 tiacc 自动提供的测试数据。</td>   
			<td rowspan="3"> 
			<pre style="color:white">
 "test_data_info": {
    "test_data_source": "user provided/tiacc provided",
    "test_data_shape": " (1, 9240)" ,
    "test_data_type": " int32"
  }
	</pre>
			</td> 
     </tr> 
  <tr>
      <td>test_data_shape</td>   
     </tr> 
		 <tr>
      <td>test_data_type</td>   
     </tr> 
		 <tr>      
      <td rowspan="5">optimization_result</td>   
      <td>baseline_time</td>   
      <td rowspan="5">优化结果，包括原始模型的平均时延 baseline，优化后的模型的平均时延 optimized，原始模型的 qps，以及优化后的模型的 qps，以及加速比 speedup。</td>   
			<td rowspan="5">
		 <pre style="color:white">
 "optimization_result": {
    "baseline_time": "10.00 ms",   
    "optimized_time": "4.38 ms",   
    "baseline_qps": "100",   
    "optimized_qps": "228",   
    "speedup": "2.28"          
  }
</pre>
</td> 
     </tr> 
  <tr>
      <td>optimized_time</td>   
     </tr> 
		 <tr>
      <td>baseline_qps</td>   
     </tr> 
		<tr>
      <td>optimized_qps</td>   
     </tr> 
		 <tr>
      <td>speedup</td>   
     </tr> 
</table>


















