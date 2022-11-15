## 操作场景
本文介绍如何使用 TACO Infer 优化模型。

<dx-alert infotype="explain" title="">
请确保您已经完成相关环境的安装配置，详情请参见 [安装 TACO Infer](https://cloud.tencent.com/document/product/1573/74091)。
</dx-alert>





## 操作步骤

### 准备模型

TACO Infer 支持 TensorFlow frozen pb 和 saved model 两种主要的模型格式。在模型优化前，需在磁盘上导出模型文件。您可以自行训练导出支持格式的模型或下载公开的网络模型。导出模型示例代码如下：

```python
import tensorflow as tf


def export_frozen_pb(save_dir, file_name):
  g = tf.Graph()
  with g.as_default():
      px = tf.placeholder(shape=shape, dtype=dtype, name="px")
      py = tf.placeholder(shape=shape, dtype=dtype, name="py")
      c = tf.constant(random_data(positive_constant), name="c")
      x = px + py
      x = x * x
      x = tf.nn.relu(x)
      x = tf.abs(x)
      x = x + c
      y = tf.rsqrt(x)
      z = tf.nn.relu(x)
      tf.io.write_graph(g.as_graph_def(), save_dir, file_name)
```

### 导入 TACO Infer

使用 TACO Infer 优化模型首先需要导入 python 模块，代码如下：
```python
from taco import optimize_cpu, OptimizeConfig, ModelConfig
```


### 调用优化接口[](id:callInterface)
1. 配置输入模型、输出模型目录、测试数据、优化配置、模型配置后，调用 optimize_cpu 即可对模型进行优化。关于优化接口参数的详细信息，请参见 [接口文档](https://cloud.tencent.com/document/product/1573/74093)。优化接口代码如下：
```python
report = optimize_cpu(
    input_model,
    output_model_dir,
    test_data = test_data,
    optimize_config = optimize_config,
    model_config = model_config
)
```
2. 优化过程中，可以看到如下类似的优化日志：
```plaintext
2022-03-31 16:54:19,581 [INFO] [optimize_model.py:27] Load frozen pb from /root/taco_test/model/fast-transformer-encoder.pb
2022-03-31 16:54:40,213 [INFO] [optimize_model.py:27] Matched 12 [softmax_pattern] in the graph.
2022-03-31 16:54:52,545 [INFO] [optimize_model.py:27] Matched 0 [conv2_d_pattern] in the graph.
2022-03-31 16:54:57,316 [INFO] [optimize_model.py:27] Matched 72 [mat_mul_pattern] in the graph.
2022-03-31 16:55:05,606 [INFO] [optimize_model.py:27] Matched 0 [avg_pool_pattern] in the graph.
2022-03-31 16:55:10,354 [INFO] [optimize_model.py:27] Matched 0 [max_pool_pattern] in the graph.
2022-03-31 16:55:15,088 [INFO] [optimize_model.py:27] Matched 0 [mat_mul_bias_add_relu_pattern] in the graph.
2022-03-31 16:55:19,952 [INFO] [optimize_model.py:27] Matched 72 [mat_mul_bias_add_pattern] in the graph.
2022-03-31 16:55:28,033 [INFO] [optimize_model.py:27] Matched 0 [conv2_d_bias_add_relu_pattern] in the graph.
2022-03-31 16:55:32,676 [INFO] [optimize_model.py:27] Matched 0 [conv2_d_bias_add_pattern] in the graph.
2022-03-31 16:55:37,246 [INFO] [optimize_model.py:27] Matched 0 [conv2_d_fused_batch_norm_relu_pattern] in the graph.
2022-03-31 16:55:41,781 [INFO] [optimize_model.py:27] Matched 0 [conv2_d_fused_batch_norm_pattern] in the graph.
```
3. 模型优化结束后，会产出一个保存在您指定的目录中的优化后的模型，以及一个包括硬件信息，软件信息及优化过程相关指标的优化报告。关于优化报告的详细字段说明，请参考 [输出参数说明](https://cloud.tencent.com/document/product/1573/74093#Optimization)。优化报告的详细信息如以下样例所示：
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
        "working_directory": "/root/taco_test/optimize",
        "input_model": "./model/fast-transformer-encoder.pb",
        "output_model_dir": "./optimized_model",
        "optimization time": "3min 43s 902ms",
        "model format": "tensorflow frozen pb",
        "status": "satisfactory",
        "baseline latency": "95ms 380us",
        "accelerated latency": "46ms 892us",
        "speedup": "2.03",
    }
}
```
优化完成后，在配置好的模型输出目录，可查看如下所示产出的优化模型。TACO Infer 优化模型后会产出一个和输入模型保持同一格式的模型供您进行部署。
```bash
[root@VM-3-46-centos optimized_model]# ll
total 332440
-rw-r--r-- 1 root root 340411615 Mar 31 21:03 fast-transformer-encoder.pb
```




### 问题调试
如果在使用 TACO Infer 过程中遇到问题，您还可以在进行模型优化前设置以下环境变量，导出详细的日志信息到指定的日志文件中：
```bash
export TACO_LOG_FILE=path/to/log_file
export TACO_LOG_LEVEL=debug
```
例如，将日志信息导出到当前工作目录下的 `taco_log` 文件中：
```bash
[root@VM-3-46-centos fast_transformer_encoder]# export TACO_LOG_FILE=./taco_log
[root@VM-3-46-centos fast_transformer_encoder]# export TACO_LOG_LEVEL=debug
[root@VM-3-46-centos fast_transformer_encoder]# python optimize_model.py
```
优化完成之后，可以看到当前工作目录下生成了一个名为 `taco_log` 的日志文件和一个名为 `taco_log.trace` 的 trace 文件：
```bash
[root@VM-3-46-centos fast_transformer_encoder]# ll
-rw-r--r-- 1 root root 86388 Apr 14 14:23 taco_log
-rw-r--r-- 1 root root 41358 Apr 14 14:23 taco_log.trace
drwxr-xr-x 2 root root  4096 Mar 31 18:07 model
drwxr-xr-x 2 root root  4096 Apr 14 14:23 optimized_model
-rw-r--r-- 1 root root   674 Mar 31 18:09 optimize_model.py
```
 - `taco_log.trace` 文件：包含一些编码后的 trace 信息。
 - `taco_log` 文件：包含明文的详细日志信息，内容如下所示：
```bash
...
2022-04-14 14:20:17,351 [DEBUG] [optimize_model.py:24] zen_softmax_rewrite receives 1 input models
2022-04-14 14:20:17,365 [INFO] [optimize_model.py:24] Matched 12 [softmax_pattern] in the graph.
2022-04-14 14:20:17,746 [DEBUG] [optimize_model.py:24] Matched original nodes: ['layer_0/attention/self/Softmax']
2022-04-14 14:20:17,746 [DEBUG] [optimize_model.py:24] Origin root node name of graph segment: layer_0/attention/self/Softmax
2022-04-14 14:20:17,749 [DEBUG] [optimize_model.py:24] Matched original nodes: ['layer_1/attention/self/Softmax']
2022-04-14 14:20:17,749 [DEBUG] [optimize_model.py:24] Origin root node name of graph segment: layer_1/attention/self/Softmax
2022-04-14 14:20:17,751 [DEBUG] [optimize_model.py:24] Matched original nodes: ['layer_10/attention/self/Softmax']
2022-04-14 14:20:17,751 [DEBUG] [optimize_model.py:24] Origin root node name of graph segment: layer_10/attention/self/Softmax
2022-04-14 14:20:17,754 [DEBUG] [optimize_model.py:24] Matched original nodes: ['layer_11/attention/self/Softmax']
2022-04-14 14:20:17,754 [DEBUG] [optimize_model.py:24] Origin root node name of graph segment: layer_11/attention/self/Softmax
2022-04-14 14:20:17,757 [DEBUG] [optimize_model.py:24] Matched original nodes: ['layer_2/attention/self/Softmax']
2022-04-14 14:20:17,757 [DEBUG] [optimize_model.py:24] Origin root node name of graph segment: layer_2/attention/self/Softmax
2022-04-14 14:20:17,760 [DEBUG] [optimize_model.py:24] Matched original nodes: ['layer_3/attention/self/Softmax']
2022-04-14 14:20:17,760 [DEBUG] [optimize_model.py:24] Origin root node name of graph segment: layer_3/attention/self/Softmax
2022-04-14 14:20:17,762 [DEBUG] [optimize_model.py:24] Matched original nodes: ['layer_4/attention/self/Softmax']
2022-04-14 14:20:17,762 [DEBUG] [optimize_model.py:24] Origin root node name of graph segment: layer_4/attention/self/Softmax
2022-04-14 14:20:17,765 [DEBUG] [optimize_model.py:24] Matched original nodes: ['layer_5/attention/self/Softmax']
2022-04-14 14:20:17,765 [DEBUG] [optimize_model.py:24] Origin root node name of graph segment: layer_5/attention/self/Softmax
2022-04-14 14:20:17,768 [DEBUG] [optimize_model.py:24] Matched original nodes: ['layer_6/attention/self/Softmax']
2022-04-14 14:20:17,768 [DEBUG] [optimize_model.py:24] Origin root node name of graph segment: layer_6/attention/self/Softmax
2022-04-14 14:20:17,770 [DEBUG] [optimize_model.py:24] Matched original nodes: ['layer_7/attention/self/Softmax']
2022-04-14 14:20:17,771 [DEBUG] [optimize_model.py:24] Origin root node name of graph segment: layer_7/attention/self/Softmax
2022-04-14 14:20:17,773 [DEBUG] [optimize_model.py:24] Matched original nodes: ['layer_8/attention/self/Softmax']
2022-04-14 14:20:17,773 [DEBUG] [optimize_model.py:24] Origin root node name of graph segment: layer_8/attention/self/Softmax
2022-04-14 14:20:17,776 [DEBUG] [optimize_model.py:24] Matched original nodes: ['layer_9/attention/self/Softmax']
2022-04-14 14:20:17,776 [DEBUG] [optimize_model.py:24] Origin root node name of graph segment: layer_9/attention/self/Softmax
2022-04-14 14:20:21,215 [DEBUG] [optimize_model.py:24] Loading the TACO native passes.
...
```
您可以根据日志文件中的信息尝试解决问题，也可以通过 [联系我们](https://cloud.tencent.com/document/product/1573/74094) 将日志文件及 trace 文件发送给 TACO 技术团队寻求协助。


### 模型验证

经过上述步骤得到优化过的模型后，您可以使用 TensorFlow 的 python 接口加载该模型，验证其性能和正确性。加载模型运行的代码如下所示：
<dx-alert infotype="notice" title="">
由于优化后的模型包含经过高度优化的 TACO Kit 自定义算子，因此运行模型之前，需要使用 TensorFlow 的`load_op_library` 接口加载位于 `${Taco Infer python安装目录}/lib` 目录中的两个包含自定义算子的动态链接库。
</dx-alert>
```python
import tensorflow as tf
import numpy as np


def gen_test_data(batch_size = 1):
    MAX_SEQ_LEN = 32
    HIDDEN_DIM = 768
    rng = np.random.RandomState(2022)
    input_data = rng.randn(batch_size, MAX_SEQ_LEN, HIDDEN_DIM)
    return input_data


def run_model(pb_model_path, input_name='', output_name='', test_data=None):
    load_library()
    graph_def = read_pb_model(pb_model_path)

    tf.import_graph_def(graph_def, name="")
    with tf.Session() as sess:
        output_tensor = sess.graph.get_tensor_by_name(output_name + ':0')
        input_tensor = sess.graph.get_tensor_by_name(input_name + ':0')
        output = sess.run([output_tensor], {input_tensor: test_data})
    print(output)


def load_library():
    tf.load_op_library("/root/taco_test/venv/taco_dev/lib64/python3.6/site-packages/taco/lib/libtaco_tf.so")
    tf.load_op_library("/root/taco_test/venv/taco_dev/lib64/python3.6/site-packages/taco/lib/libtidy_ops.so")


def read_pb_model(pb_model_path):
    with tf.gfile.GFile(pb_model_path, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        return graph_def


if __name__ == '__main__':
    pb_model_path = "./optimized_model/fast-transformer-encoder.pb"
    input_name = "Placeholder"
    output_name = "mul_1"
    test_data = gen_test_data()
    run_model(pb_model_path, input_name=input_name, output_name=output_name, test_data=test_data)
```
根据实际的输出模型目录和 Taco Infer python 安装目录调整相关参数后，运行以上代码，即可加载优化后的模型进行推理计算。输出日志如下，可查看模型正常运行并且输出了计算结果。
```bash
[root@VM-3-46-centos fast_transformer_encoder]#python run_model.py

...

[array([[[ 0.10604528,  2.0389333 ,  0.7614179 , ...,  1.8888083 ,
          0.9291879 , -0.42675698],
        [-0.42543304,  1.1162308 , -0.03524539, ...,  0.54224205,
          2.1540937 ,  0.760207  ],
        [-0.38016492,  0.4529049 ,  0.647373  , ..., -0.4969776 ,
         -0.04796869,  0.6062175 ],
        ...,
        [ 0.        ,  0.        ,  0.        , ..., -0.        ,
          0.        , -0.        ],
        [ 0.        ,  0.        , -0.        , ...,  0.        ,
         -0.        ,  0.        ],
        [-0.        ,  0.        ,  0.        , ..., -0.        ,
          0.        ,  0.        ]]], dtype=float32)]
```
