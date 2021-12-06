目前 TI-ACC 处于内测阶段，请先进行 [申请内测权限](https://cloud.tencent.com/apply/p/vl6fzemdq1) 拿到私有镜像临时登录指令，然后进行使用。

## 使用要求
TI-ACC 推理加速仅支持以下操作系统、Python 版本、设备类型及框架版本：
- 操作系统：Linux
- Python 版本：Python 3.6
- 设备类型：GPU 支持 CUDA 10.2
- 框架版本：PyTorch 1.7.1、1.8.1、1.9.0

## 使用步骤
### 步骤1：环境搭建
#### 创建 CVM 实例
参考 [购买 NVIDIA GPU 实例](https://cloud.tencent.com/document/product/560/30211) 创建实例。其中：
- **镜像**：请选择 Ubuntu 18.04 及以上版本，并勾选“后台自动安装 GPU 驱动”，使用自动安装功能安装 GPU 驱动。CUDA 驱动及 cuDNN 的自动安装非本次部署的必选项，您可根据实际情况选择。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/213fb397749294793c7a894923c876ca.png)
- **系统盘**：考虑到 Docker 镜像的大小以及训练中间状态文件的存储，推荐配置100G以上的系统盘。

#### 安装 Docker
请对应实例的操作系统类型，参考以下文档安装 Docker。

| 操作系统 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| CentOS   | 参考 [Docker 官方文档 - 在 CentOS 中安装 Docker](https://docs.docker.com/engine/install/centos/) 进行安装。 |
| Ubuntu   | 参考 [Docker 官方文档 - 在 Ubuntu 中安装 Docker](https://docs.docker.com/engine/install/ubuntu/) 进行安装。 |

#### 安装 nvidia-docker
安装 nvidia-docker，详情请参见 [NVIDIA 官方文档](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)。
#### 申请临时登录指令
线下 [申请](https://cloud.tencent.com/apply/p/vl6fzemdq1) 加速产品私有镜像仓库临时登录指令以及相关 tag 信息。
#### 获取加速镜像
- 使用线下申请的私有镜像临时登录指令，登录腾讯云容器服务 Docker Registry 加速镜像仓库，参考命令如下所示：
```
docker login tiacc-test.tencentcloudcr.com --username xxx --password xxx
```
>!username 为账号 ID，password 为临时登录指令。

- 从 Registry 加速镜像仓库拉取镜像，参考命令如下所示：
```
docker pull tiacc-test.tencentcloudcr.com/tiacc/tiacc_pytorch:[tag]
```
>!tag 为镜像名称。

#### 启动加速镜像
启动加速镜像并进入容器实例，参考命令如下所示：
```
docker run -it --net=host --privileged --rm --gpus all --shm-size=32g --ulimit memlock=-1 --ulimit stack=67108864 --name TI-ACC-inference-gpu -d tiacc-test.tencentcloudcr.com/tiacc/tiacc_pytorch:[tag]
```


### 步骤2：使用加速
#### 使用推理加速
```
#引入部分引入推理加速包
import tiacc_inference
#模型定义和训练，得到input_model
...
#对训练完成的model进行推理加速
output_model,optimized_report = tiacc_inference.optimize(input_model,optimization_level,device_type,input_info,test_data,save_path)
```

#### 推理实测效果
<table>
     <tr>
         <th>硬件环境</th>  
         <th>模型</th>  
         <th>batch</th> 
				 <th>torchscript（时延，ms）</th>
				 <th>TI-ACC（时延，ms）</th>
				 <th>TI-ACC（fp16）（时延，ms）</th>
     </tr>
  <tr>      
      <td rowspan="12">腾讯云GN7.2XLARGE32</td>   
      <td rowspan="4">resnet50<br>torchvision<br>224x224</td>   
      <td>1</td>   
			<td>7.10 </td> 
			<td>3.35</td> 
			<td>1.10 </td> 
     </tr> 
  <tr>
      <td>16</td>   
      <td>42.67</td>
			<td>30.75</td>
			<td>7.97 </td>
     </tr> 
  <tr>      
       <td>32</td>   
      <td>82.79</td>   
      <td>59.01 </td>   
			<td>14.12</td>
     </tr> 
		   <tr>      
       <td>64</td>   
      <td>162.67</td>   
      <td>115.62</td> 
			<td>26.49</td>
     </tr> 
		 		   <tr>      
       <td rowspan="4">resnest50<br>mmcls<br>224x224</td>   
      <td>1</td>   
			<td>12.47 </td> 
			<td>7.78</td>
			<td>5.22</td>
     </tr> 
  <tr>
      <td>16</td>   
      <td>61.22 </td>
			<td>44.40</td>
			<td>24.53</td>
     </tr> 
  <tr>      
       <td>32</td>   
      <td>168.47 </td>   
      <td>85.63</td> 
			<td>46.03</td>
     </tr> 
		   <tr>      
       <td>64</td>   
      <td>348.70</td>   
      <td>171.82</td>
			<td>88.44</td>
     </tr> 
		 <tr>      
       <td rowspan="4">centernet-custom</td>   
      <td>1</td>   
			<td>29.28</td> 
			<td>13.88</td>
			<td>4.89 </td>
     </tr> 
  <tr>
      <td>2</td>   
      <td>56.18 </td>
			<td>27.22</td>
			<td>9.41</td>
     </tr> 
  <tr>      
       <td>4</td>   
      <td>113.25</td>   
      <td>53.53</td>
			<td>16.03 </td>
     </tr> 
		   <tr>      
       <td>8</td>   
      <td>232.11</td>   
      <td>108.45 </td>
			<td>32.41</td>
     </tr> 
</table>



#### 推理加速接口说明
- 输入参数及说明

| 参数               | 类型                                        | 是否必填 | 参数说明                                                     | 默认值 | 示例                                                         |
| ------------------ | ------------------------------------------- | -------- | ------------------------------------------------------------ | ------ | ------------------------------------------------------------ |
| input_model        | 多种（STRING+torch.jit.ScriptModule类型）   | 是       | 输入待优化的原始模型。Pytorch 模型格式，支持以下格式：torch.jit.ScriptModule 导出的模型文件，以 .pt、.pth 为后缀（计算图结构+参数的模型）；torch.jit.ScriptModule 对象 | 无     | 字符串格式的路径，'./lzz'、'./lzz.pb                         |
| optimization_level | INT                                         | 是       | 推理加速的优化级别。0：无损；1：FP16                         | 无     | 0                                                            |
| device_type        | INT                                         | 是       | 运行设备。0：GPU                                             | 无     | 0                                                            |
| input_shapes       | 多种（LIST[STRING]+LIST[LIST)]+LIST[DICT]） | 是       | 模型输入的相关信息，主要包括形状 shape 和类型 data_type 最外层是 list，其中每个元素代表一个输入节点 input，每个 input 允许 str、list、dict 的格式，允许嵌套：str 用于单一节点固定输入尺寸；list 用于多节点固定尺寸；dict 用于输入非固定尺寸或者非 float 类型，对应的 key 为 'seperate\|range,int\|float\|half'，seperate 静态，value 填写的是 range 表示动态，value 填写的是 min 和 max | 无     | 单一节点固定尺寸：[ '1 * 3 * 224 * 224' ]多节点固定尺寸：[[ '1 * 3 * 224 * 224' ],[ '1 * 3 * 512 * 512' ]]单节点非固定静态尺寸：[{'seperate': ['1 * 3 * 224 * 224','2 * 3 * 224 * 224']}]单节点非固定动态尺寸：[{'range': ['1 * 3 * 224 * 224','10 * 3 * 224 * 224']}] |
| test_data          | 多种（LIST[Tuple[torch.tensor, ]]）         | 否       | 用于模型推理速度对比的测试数据。用户给出则使用用户给出的测试数据；如果用户不给出，那么 TI-ACC 来自动提供测试数据。对于不同类型的模型，其测试数据格式存在差异， PyTorch 模型的测试数据为若干组输入Tensor Tuple，类型为 LIST[Tuple[torch.tensor, ]] | None   | /                                                            |
| save_path          | STRING                                      | 否       | 优化模型的保存路径。如果需要将优化后的模型进行保存，则必填。如果是 pytorch 模型格式，支持以下方式：torch.jit.ScriptModule 保存方式，即填写导出的模型文件，以 .pt/.pth 为后缀 | None   | ‘../lzz’、‘../lzz.pb’、‘../lzz.pbt                           |


- 输出参数及说明

| 参数             | 类型                                     | 参数说明                                                    | 示例                                                         |
| ---------------- | ---------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| output_model     | 多种（GraphDef 类型 + torch.nn.Module 类型） | 优化后的模型，输出与 input_model 输入模型相同类型的模型对象。 | /                                                            |
| optimized_report | OptimizedReport                          | 输出的优化报告                                              | optimized_report: {  // 软件环境、包括框架、CUDA。"software_environment": [    {      "software": "tensorflow",      "version": "1.15.0"    },    {      "software": "cuda",      "version": "9.0.176"    },    {      "software": "cuDNN",      "version": "7.4"    },    {      "software": "TensorRT",      "version": "5"    }  ],  // 硬件环境。  "hardware_environment": {    "device_type": "gpu"    "microarchitecture": "V100"  },  // 测试数据信息。    "test_data_info": {    "test_data_source": "user provided/tiacc provided",           "test_data_shape": " (1, 9240)" ,                                                                               "test_data_type": " int32"  },  // 优化结果。"optimization_result": {    "baseline": "10.00 ms",       "optimized": "4.38 ms",       "speedup": "2.28"           }} |

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
			<td rowspan="2"> "software_environment": [
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
  ]</td> 
     </tr> 
  <tr>
      <td >version</td>   
     </tr> 
  <tr>      
      <td rowspan="2">hardware_environment</td>   
      <td>device_type</td>   
      <td rowspan="2">硬件环境，包括 device_type 类型以及显卡类型。</td>   
			<td rowspan="2"> "hardware_environment": {
    "device_type": "gpu"
    "microarchitecture": "V100"
  }</td> 
     </tr> 
  <tr>
      <td >microarchitecture</td>   
     </tr> 
		  <tr>      
      <td rowspan="3">test_data_info</td>   
      <td>test_data_source</td>   
      <td rowspan="3">测试数据信息，包括测试数据来源和测试数据的形状和类型。数据来源有两类，如果用户本身提供了测试数据，则为：user provided，如果用户没有提供，则为：tiacc provided，即 tiacc 自动提供的测试数据。</td>   
			<td rowspan="3"> "test_data_info": {
    "test_data_source": "user provided/tiacc provided",       
    "test_data_shape": " (1, 9240)" ,                                                                               "test_data_type": " int32"
  }</td> 
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
			<td rowspan="5">"optimization_result": {
    "baseline_time": "10.00 ms",   
    "optimized_time": "4.38 ms",   
    "baseline_qps": "100",   
    "optimized_qps": "228",   
    "speedup": "2.28"          
  }
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


















