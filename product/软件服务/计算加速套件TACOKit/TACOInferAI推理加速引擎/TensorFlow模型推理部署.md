
## 操作场景
本文介绍如何使用 TACO Infer 部署模型。在部署前，请确保您已完成 [TensorFlow 模型优化](https://cloud.tencent.com/document/product/1573/74092)，并且验证模型的性能和正确性符合预期后，您即可通过本文将模型部署在实际生产环境中。



## 操作步骤

### 环境准备

- 服务器：参考 [TACO Infer 安装](https://cloud.tencent.com/document/product/1573/74091)，选购 CPU 机型。
- ABI 版本：TACO Infer 支持 CXX11 ABI。如有其他版本需求请通过 [联系我们](https://cloud.tencent.com/document/product/1573/74094) 获取支持。
- SDK 包安装：在开发部署模型之前，请确保您已经安装了 TACO Infer SDK 安装包，详情请参见 [获取 Wheel 包及 SDK 包](https://cloud.tencent.com/document/product/1573/74091#getWheelSDK)。解压后可查看安装包中包含三个动态链接库和一个可执行文件：
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
