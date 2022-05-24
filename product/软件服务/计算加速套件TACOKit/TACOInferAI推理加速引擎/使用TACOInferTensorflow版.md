
本文介绍如何使用 TACO Infer。

## TF 模型优化

### 模型准备

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


### 调用优化接口
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
3. 模型优化结束后，会产出一个保存在您指定的目录中的优化后的模型，以及一个包括硬件信息，软件信息及优化过程相关指标的优化报告。关于优化报告的详细字段说明，请参考 [优化报告](#Optimization)。优化报告的详细信息如以下样例所示：
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
优化完成后，在配置好的模型输出目录，可查看如下所示产出的优化模型。Taco 优化模型后会产出一个和输入模型保持同一格式的模型供您进行部署。
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





## SDK 部署 TF 模型

根据上述步骤使用 TACO Infer 产出优化模型，并且验证模型的性能和正确性符合预期后，您即可通过该步骤将模型部署在实际生产环境中。

### 环境准备

- 服务器：参考 [安装 TACO Infer](https://cloud.tencent.com/document/product/1573/74091)，选购 CPU 机型。
- ABI 版本：TACO Infer 支持 CXX11 ABI。如有其他版本需求请通过 [联系我们](https://cloud.tencent.com/document/product/1573/74094) 获取支持。
- SDK 包安装：在开发部署模型之前，您需要前往腾讯云官网下载 TACO Kit SDK 安装包，解压后可查看安装包中包含三个动态链接库和一个可执行文件：
```bash
[root@VM-3-46-centos inceptionv3]# ll lib/
total 416180
-rwxr-xr-x 1 root root   1018440 Mar 31 20:25 libomp-1fdec59b.so
-rwxr-xr-x 1 root root  42617800 Mar 31 20:25 libtaco_tf.so
-rwxr-xr-x 1 root root 125954112 Mar 31 20:25 libtidy_ops.so
-rwxr-xr-x 1 root root 256572616 Mar 31 20:25 tidy_vm
```
<dx-alert infotype="explain" title="">
 - 建议您将所有 TACO 库文件拷贝到系统库目录 `/usr/lib` 下，以便链接器 ld 进行链接时可定位。或您也可以将 TACO 库文件拷贝到其他路径，并在 `LD_LIBRARY_PATH` 环境变量中添加库所在路径。
 - 请确保所有的 TACO 库文件位于同一路径下。
</dx-alert>




### 推理代码开发

以下代码以 TensorFlow C++ API 展示优化后模型的加载运行过程，您只需要按照标准的 TensorFlow C++ API 加载经过优化的模型即可，和加载普通的 TF 模型没有任何区别。
```c++
#include <string>
#include <vector>

#include "tensorflow/core/framework/graph.pb.h"
#include "tensorflow/core/framework/tensor.h"
#include "tensorflow/core/graph/default_device.h"
#include "tensorflow/core/graph/graph_def_builder.h"
#include "tensorflow/core/lib/core/threadpool.h"
#include "tensorflow/core/lib/strings/stringprintf.h"
#include "tensorflow/core/platform/init_main.h"
#include "tensorflow/core/platform/logging.h"
#include "tensorflow/core/platform/types.h"
#include "tensorflow/core/public/session.h"
#include "tensorflow/core/public/session_options.h"
#include "tensorflow/cc/client/client_session.h"
#include "tensorflow/core/protobuf/meta_graph.pb.h"
#include "tensorflow/c/c_api.h"

using tensorflow::GraphDef;
using tensorflow::int32;
using tensorflow::string;

void LoadFrozenPbModel(
    const std::unique_ptr<tensorflow::Session>& session,
    std::string model_path,
    bool as_text) {
  GraphDef graph_def;
  tensorflow::Status load_graph_status;
  std::cout << "Model Path: " << model_path << std::endl;
  if (as_text) {
    load_graph_status =
        ReadTextProto(tensorflow::Env::Default(), model_path, &graph_def);
  } else {
    load_graph_status =
        ReadBinaryProto(tensorflow::Env::Default(), model_path, &graph_def);
  }

  if (!load_graph_status.ok()) {
	  std::cout << "Failed to load model: " << model_path
                    << load_graph_status.ToString() << std::endl;
  }

  auto session_status = session->Create(graph_def);
  if (!session_status.ok()) {
      std::cout << "Failed to create session" << session_status.ToString() << std::endl;
  }
}

void RunInference(
    const std::string& model_path,
    const std::vector<std::pair<std::string, tensorflow::Tensor>>& inputs,
    const std::vector<string>& output_tensor_names,
    const std::vector<string>& target_node_names,
    std::vector<tensorflow::Tensor>& outputs) {  // NOLINT
  // Create session
  tensorflow::SessionOptions options;
  std::unique_ptr<tensorflow::Session> session(tensorflow::NewSession(options));
  // Load model
  LoadFrozenPbModel(session, model_path, false);

  TF_CHECK_OK(
      session->Run(inputs, output_tensor_names, target_node_names, &outputs));
}

int main() {
  std::string model_path = "./optimized_model/fast-transformer-encoder.pb";

  // Create test input data
  std::vector<std::pair<std::string, tensorflow::Tensor>> inputs;
  auto input_tensor = tensorflow::Tensor(
      tensorflow::DT_FLOAT, tensorflow::TensorShape({1, 32, 768}));
  auto flat = input_tensor.flat<float>();
  for (int i = 0; i < 24576; i++) {
    flat(i) = 0.5;
  }
  string input_name = "Placeholder";
  inputs.emplace_back(input_name, input_tensor);

  // Create output tensor
  const std::vector<string> output_tensor_names = {"mul_1:0"};
  const std::vector<string> target_node_names = {};
  std::vector<tensorflow::Tensor> outputs;

  RunInference(
      model_path, inputs, output_tensor_names, target_node_names, outputs);

  std::cout << "Output tensor: [" << std::endl;
  for (int i = 0; i < 10; i++) {
	  std::cout << outputs[0].flat<float>()(i) << std::endl;
  }
  std::cout << "]" << std::endl;
}
```


### 编译链接
编译以上代码时，需要链接 Taco 提供的 `libtaco_tf.so` 和 `libtidy_ops.so` 两个动态库，及链接 TensorFlow 提供的 `libtensorflow_framework.so` 和 `libtensorflow_cc.so` 两个动态链接库。其中，`libtensorflow_framework.so` 位于 TensorFlow 的 Python 安装目录中。而 `libtensorflow_cc.so` 没有随着TensorFlow Python 安装包一起发行，需要您下载 TensorFlow 源码自行编译。

1. 执行以下命令，完成编译。
```bash
git clone https://github.com/tensorflow/tensorflow
cd tensorflow
git checkout ${xxx version}
./configure
bazel build --config=opt //tensorflow:libtensorflow_cc.so
```
2. `libtensorflow_cc.so` 编译完成后，即可进行模型部署代码的编译。编译参数如下所示：
```bash
#!/bin/bash

gcc -std=c++11 \
    -I/root/taco_test/1.15.0/include \
    -L/root/taco_test/venv/taco_dev/lib64/python3.6/site-packages/tensorflow_core -ltensorflow_framework \
    -L/root/taco_test/lib -ltensorflow_cc -ltaco_tf -ltidy_ops \
    -lstdc++ \
    -o tf_sdk_demo tf_sdk_demo.cc
```
编译完成后，得到一个可运行的二进制文件。如下所示：
```
[root@VM-3-56-ubuntu (Taco Dev) /home/ubuntu/taco_test/test_taco_sdk_demo]
#ll
-rw-rw-r--  1  500  500 3.4K Mar 29 16:04 taco_sdk_demo.cc
-rwxr-xr-x  1 root root  99K Mar 29 16:04 taco_sdk_demo*
drwxr-xr-x  2 root root 4.0K Mar 29 16:06 ./
drwxrwxr-x 10  500  500 4.0K Mar 29 16:58 ../
```
3. 确认相关的动态链接库已经正确链接：
```bash
(taco_dev) [root@VM-3-46-centos fast_transformer_encoder]# ldd tf_sdk_demo
	linux-vdso.so.1 =>  (0x00007fff34bea000)
	libtensorflow_framework.so.1 => /root/taco_test/venv/taco_dev/lib64/python3.6/site-packages/tensorflow_core/libtensorflow_framework.so.1 (0x00007efff59ab000)
	libtensorflow_cc.so.1 => /usr/local/lib/libtensorflow_cc.so.1 (0x00007effee66f000)
	libtaco_tf.so => /usr/local/lib/libtaco_tf.so (0x00007effec488000)
	libtidy_ops.so => /usr/local/lib/libtidy_ops.so (0x00007effea335000)
	libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00007effea02d000)
	libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007effe9e17000)
	libc.so.6 => /lib64/libc.so.6 (0x00007effe9a49000)
	librt.so.1 => /lib64/librt.so.1 (0x00007effe9841000)
	libpthread.so.0 => /lib64/libpthread.so.0 (0x00007effe9625000)
	libdl.so.2 => /lib64/libdl.so.2 (0x00007effe9421000)
	libm.so.6 => /lib64/libm.so.6 (0x00007effe911f000)
	/lib64/ld-linux-x86-64.so.2 (0x00007efff76b7000)
	libomp-1fdec59b.so => /usr/local/lib/libomp-1fdec59b.so (0x00007effe8e4e000)
	libcurl.so.4 => /lib64/libcurl.so.4 (0x00007effe8be4000)
	libuuid.so.1 => /lib64/libuuid.so.1 (0x00007effe89df000)
	libcrypto.so.10 => /lib64/libcrypto.so.10 (0x00007effe857c000)
	libidn.so.11 => /lib64/libidn.so.11 (0x00007effe8349000)
	libssh2.so.1 => /lib64/libssh2.so.1 (0x00007effe811c000)
	libssl3.so => /lib64/libssl3.so (0x00007effe7eb9000)
	libsmime3.so => /lib64/libsmime3.so (0x00007effe7c91000)
	libnss3.so => /lib64/libnss3.so (0x00007effe7958000)
	libnssutil3.so => /lib64/libnssutil3.so (0x00007effe7728000)
	libplds4.so => /lib64/libplds4.so (0x00007effe7524000)
	libplc4.so => /lib64/libplc4.so (0x00007effe731f000)
	libnspr4.so => /lib64/libnspr4.so (0x00007effe70e1000)
	libgssapi_krb5.so.2 => /lib64/libgssapi_krb5.so.2 (0x00007effe6e94000)
	libkrb5.so.3 => /lib64/libkrb5.so.3 (0x00007effe6bab000)
	libk5crypto.so.3 => /lib64/libk5crypto.so.3 (0x00007effe6978000)
	libcom_err.so.2 => /lib64/libcom_err.so.2 (0x00007effe6774000)
	liblber-2.4.so.2 => /lib64/liblber-2.4.so.2 (0x00007effe6565000)
	libldap-2.4.so.2 => /lib64/libldap-2.4.so.2 (0x00007effe6310000)
	libz.so.1 => /lib64/libz.so.1 (0x00007effe60fa000)
	libssl.so.10 => /lib64/libssl.so.10 (0x00007effe5e88000)
	libkrb5support.so.0 => /lib64/libkrb5support.so.0 (0x00007effe5c78000)
	libkeyutils.so.1 => /lib64/libkeyutils.so.1 (0x00007effe5a74000)
	libresolv.so.2 => /lib64/libresolv.so.2 (0x00007effe585a000)
	libsasl2.so.3 => /lib64/libsasl2.so.3 (0x00007effe563d000)
	libselinux.so.1 => /lib64/libselinux.so.1 (0x00007effe5416000)
	libcrypt.so.1 => /lib64/libcrypt.so.1 (0x00007effe51df000)
	libpcre.so.1 => /lib64/libpcre.so.1 (0x00007effe4f7d000)
	libfreebl3.so => /lib64/libfreebl3.so (0x00007effe4d7a000)
```

### 推理计算
部署程序编译完成后，运行即可加载优化后的模型并进行推理计算。可查看模型正常加载运行，并输出了推理计算结果。如下所示：
```bash
[root@VM-3-56-ubuntu (Taco Dev) /home/ubuntu/taco_test/test_taco_sdk_demo]
#./taco_sdk_demo

2022-03-31 20:52:21.702558: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2022-03-31 20:52:21.703465: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (VM-3-46-centos): /proc/driver/nvidia/version does not exist
Model Path: ./optimized_model/fast-transformer-encoder.pb
...
Output tensor: [
0.692124
-1.30981
1.93331
-0.0825812
-0.423409
-0.73291
-2.13366
0.758448
-1.25149
0.659645
]
```



## 优化报告[](id:Optimization)

Taco 优化模型后会产生一个 json 格式的优化报告，该报告包含了优化模型的硬件，软件以及一些总结信息。如下所示：
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
优化报告字段说明如下：
- **hardware**：硬件环境信息，包括设备类型、规格等。
- **software**：软件环境信息，包括框架以及框架版本。
- **summary**：模型优化的综合性信息，包括当前工作目录、输入模型路径、输出模型目录、优化时间、模型格式、运行状态、模型优化效果等。
