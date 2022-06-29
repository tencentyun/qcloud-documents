

## 优化接口

TACO Infer 为您提供了一套简单易用的模型优化接口。对于 CPU 计算设备，优化接口为 `optimize_cpu`。代码如下：

```python
def optimize_cpu(
    input_model: Union[str, torch.nn.Module],
    output_model_dir: str,
    test_data: Optional[Dict[str, np.array]],
    optimize_config: OptimizeConfig = OptimizeConfig(),
    model_config: ModelConfig = ModelConfig(),
) -> Dict:
```


### 输入参数说明

<table>
<tr>
<th>参数</th>
<th>是否必选</th>
<th>说明</th>
</tr>
<tr>
<td>input_model</td>
<td>必选</td>
<td>待优化的模型。对于 TensorFlow，该参数为模型文件所在路径。TACO Infer 支持 TensorFlow frozen pb 和 saved model 两种模型格式。</td>
</tr>
<tr>
<td>output_model_dir</td>
<td>必选</td>
<td>优化后模型的保存目录。</td>
</tr>
<tr>
<td>test_data</td>
<td>必选</td>
<td>优化过程中需要使用到的模型输入的测试数据。TACO Infer 在优化模型的过程中需要使用测试数据对模型的性能，精度等指标进行评估，以指导模型优化过程。对于 TF 模型，该参数为 session run 所需的  feed_dict。<b>需注意，test_data 只接受 numpy array 数据格式。</b><br>构建 test_data 的方式示例如下：
```
import numpy as np

def gen_test_data(batch_size = 1):
    INPUT_NAME = "input:0"
    image_size = 299
    input_data = np.random.rand(batch_size, image_size, image_size, 3)
    return {INPUT_NAME: input_data}
```
</td>
</tr>
<tr>
<td>optimize_config</td>
<td>可选</td>
<td>优化配置。您可以通过它指导 TACO Infer 提供更高质量的优化：
<ul style="margin-bottom:0px">
<li>通过 <code>print(optimize_config)</code> 可以查看默认（或修改后的）配置。</li>
<li>通过 <code>print(optimize_cfg.help())</code> 了解有哪些可配置项及如何配置。</li>
</ul>
</td>
</tr>
<tr>
<td>model_config</td>
<td>可选</td>
<td>模型配置。例如，对于存在1个以上 signature 的 TF SavedModel，您可以通过配置 <code>model_config</code> 知会 TACO Infer 哪一个需要被优化：
<ul style="margin-bottom:0px">
<li>通过 <code>print(model_config)</code>可以查看默认（或修改后的）配置。</li>
<li>通过 <code>print(model_cfg.help())</code> 了解有哪些可配置项及如何配置。示例如下：</li>
```
print(model_cfg.help())

How-to-assign-a-"model_config":
tensorflow.inputs:
type: <class 'list'>, default value: None
Input tensor names as a list. Items may use node name as prefix, such as 
"Placeholder:0", or saved model signature.

tensorflow.outputs:
type: <class 'list'>, default value: None
Output tensor names as a list.

tensorflow.saved_model.signature:
type: <class 'str'>, default value: None
Tell TACO Inf which signature to use if more than 1 signature.

Example of updating a config:
model_config.parse({"tensorflow.inputs": ['Placeholder:0']})
```
</ul>
</td>
</tr>
</table>






### 输出参数说明 [](id:Optimization)

优化模型后会产生一个 JSON 格式的优化报告，该报告包含了优化模型的硬件，软件以及一些总结信息。输出参数如下所示：
```json
{
    "hardware": {
        "cpu": "AMD EPYC 7K62 48-Core Processor, family '23', model '49'",
        "target device": "AMD EPYC 7K62 48-Core Processor, family '23', model '49'",
        "reference": "https://en.wikichip.org/wiki/intel/cpuid"
    },
    "software": {
        "framework": "tensorflow",
        "framework version": "1.15.0"
    },
    "summary": {
        "working_directory": "/root/taco_test/fast_transformer_encoder",
        "input_model": "./model/fast-transformer-encoder.pb",
        "output_model_dir": "./optimized_model",
        "optimization time": "3min 46s 398ms",
        "model format": "tensorflow frozen pb",
        "status": "satisfactory",
        "baseline latency": "49ms 517us",
        "accelerated latency": "27ms 12us",
        "speedup": "1.83"
    }
}
```
输出字段说明如下：
- **hardware**：硬件环境信息，包括设备类型、规格等。
- **software**：软件环境信息，包括框架以及框架版本。
- **summary**：模型优化的综合性信息，包括当前工作目录、输入模型路径、输出模型目录、优化时间、模型格式、运行状态、模型优化效果等。


## Config 使用方式

`OptimizeConfig` 和 `ModelConfig` 使用方法是一致的。均支持通过 `parse` 接口设置相关属性的值，通过 "`.`" 获取属性值或者赋值。Config 使用示例如下所示：

```python
from taco import ModelConfig


cfg = ModelConfig()

# assign by parse()
cfg.parse({"tensorflow.inputs": ['Placeholder:0']})

print(cfg.tensorflow.inputs)

# assign by .
cfg.tensorflow.saved_model.signature = "predictions"

print(cfg.tensorflow.saved_model.signature)
```
