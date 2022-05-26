

## 操作场景
本文以自然语言处理领域经典模型 Transformer Encoder 为例，展示 TACO Infer 优化部署 TensorFlow 模型的完整流程。

<dx-alert infotype="explain" title="">
请确保您已经完成 [安装 TACO Infer](https://cloud.tencent.com/document/product/1573/74091)，若您有更多场景需求欢迎 [联系我们](https://cloud.tencent.com/document/product/1573/74094)。
</dx-alert>


## 操作步骤

### 准备模型

1. 单击 [链接](https://taco-1251783334.cos.ap-shanghai.myqcloud.com/model/tensorflow/graph_def/fast-transformer/fast-transformer-encoder.pb)，下载本文档中使用的模型。
2. 下载完成后，可执行 `ll` 命令查看。如下所示：
```bash
[root@VM-3-46-centos model]# ll
total 332436
-rw-r--r-- 1 root root 340411049 Mar 31 18:07 fast-transformer-encoder.pb
```


### 模型优化

优化代码如下所示：
```python
from taco import optimize_cpu, ModelConfig, OptimizeConfig
import numpy as np

input_model = "./model/fast-transformer-encoder.pb"
output_model_dir = "./optimized_model"
optimize_config = OptimizeConfig()
model_config = ModelConfig()


def gen_test_data(batch_size = 1):
    MAX_SEQ_LEN = 32
    HIDDEN_DIM = 768
    INPUT_NAME = "Placeholder:0"
    rng = np.random.RandomState(2022)
    input_data = rng.randn(batch_size, MAX_SEQ_LEN, HIDDEN_DIM)
    return {INPUT_NAME: input_data}


report = optimize_cpu(
    input_model,
    output_model_dir,
    test_data=gen_test_data(batch_size=1),
    optimize_config = optimize_config,
    model_config = model_config
)
```

### 优化效果
优化效果如下，可知优化后的模型对比优化前的模型达到了2.03倍的性能提升。

```bash
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
        "optimization time": "5min 30s 387ms",
        "model format": "tensorflow frozen pb",
        "status": "satisfactory",
        "baseline latency": "95ms 380us",
        "accelerated latency": "46ms 892us",
        "speedup": "2.03",
    }
}
```


### 推理代码开发
以下代码以 TensorFlow C++ API 展示优化后模型的加载运行过程：
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

// Load frozen pb model from model path on disk 
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

// Run inference by calling tensorflow session->Run API
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

### 编译部署
进行模型部署代码的编译，编译参数如下所示：
```bash
#!/bin/bash

gcc -std=c++11 \
    -I/root/taco_test/1.15.0/include \
    -L/root/taco_test/venv/taco_dev/lib64/python3.6/site-packages/tensorflow_core -ltensorflow_framework \
    -L/root/taco_test/lib -ltensorflow_cc -ltaco_tf -ltidy_ops \
    -lstdc++ \
    -o tf_sdk_demo tf_sdk_demo.cc
```
