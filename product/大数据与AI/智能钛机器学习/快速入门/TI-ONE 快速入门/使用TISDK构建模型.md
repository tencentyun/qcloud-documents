## 操作背景
- TI SDK 是腾讯云 TI 平台 TI-ONE 提供的开源软件包。用户可以使用 TI SDK 提交机器学习和深度学习训练任务到 TI-ONE，更多详情请见 [TI SDK 简介](https://cloud.tencent.com/document/product/851/44454)。
- 为了方便您有效地使用腾讯云 TI 平台 TI-ONE 的 TI SDK，本文档将通过一个分类案例向您演示使用流程。
- 在使用之前，请确保您已经完成了 [注册与开通服务](https://cloud.tencent.com/document/product/851/39086)。

## 操作步骤

### 步骤1：数据说明
本案例训练数据已经存放在上海地域的 COS 中 [单击查看](https://tesla-ap-shanghai-1256322946.cos.ap-shanghai.myqcloud.com/cephfs/tesla_common/deeplearning/dataset/contest/demo.zip)，您可以下载到本地或者到 Notebook 中使用，在 Notebook 中使用须知：

- 请在上海地域执行例子中的代码
- 推荐使用 kernel: conda_tensorflow_py3
- 用户需在 Notebook 中同级目录下创建一个名为 code 的文件夹，然后将下载好的 [main.py](https://common-datasets-1259675134.cos.ap-guangzhou.myqcloud.com/kobe_predict/main.py) 文件上传到 code 文件夹中。

### 步骤2：引入依赖

```python
from __future__ import absolute_import, print_function
from ti import session
import sys
from ti.tensorflow import TensorFlow
```

### 步骤3：初始化参数

```python
# 初始化session
ti_session = session.Session()
# 训练数据存放的路径.格式为cos://作为前缀拼接bucket名称再拼接训练数据存放的路径
inputs = 'cos://tesla-ap-shanghai-1256322946/cephfs/tesla_common/deeplearning/dataset/contest/demo'
# 指定训练集、测试集和训练结果路径
hyperparameters = {'train_path': '/opt/ml/input/data/training/iris_training.csv',
                   'test_path': '/opt/ml/input/data/training/iris_test.csv',
                   'result_dir': '/opt/ml/output'}
# 授权给TI的服务角色
role = "TIONE_QCSRole"
```

### 步骤4：构建训练任务

```python
# 创建一个Tensorflow Estimator
tf_estimator = TensorFlow(role=role,
                          train_instance_count=1,
                          train_instance_type='TI.3XLARGE24.12core24g',
                          py_version='py3',
                          script_mode=True,
                          hyperparameters=hyperparameters,
                          framework_version='1.14.0',
                          entry_point='main.py',
                          source_dir='code')
```

### 步骤5：提交任务，开始训练

```python
# 提交Tensorflow训练任务
tf_estimator.fit(inputs)
```

    Training job request : {
      "TrainingJobName": "tensorflow-2020-04-15-03-26-49-992",
      "AlgorithmSpecification": {
        "TrainingInputMode": "File",
        "TrainingImageName": "ccr.ccs.tencentyun.com/ti_public/tensorflow:1.14.0-py3"
      },
      "InputDataConfig": [
        {
          "DataSource": {
            "CosDataSource": {
              "DataDistributionType": "FullyReplicated",
              "DataType": "COSPrefix",
              "Bucket": "tesla-ap-shanghai-1256322946",
              "KeyPrefix": "cephfs/tesla_common/deeplearning/dataset/contest/demo"
            }
          },
          "ChannelName": "training"
        }
      ],
      "OutputDataConfig": {
        "CosOutputBucket": "ti-ap-shanghai-100010875047-1259675134",
        "CosOutputKeyPrefix": ""
      },
      "ResourceConfig": {
        "InstanceCount": 1,
        "InstanceType": "TI.3XLARGE24.12core24g",
        "VolumeSizeInGB": 0
      },
      "RoleName": "TIONE_QCSRole",
      "StoppingCondition": {
        "MaxRuntimeInSeconds": 86400
      },
      "HyperParameters": "{\"train_path\": \"\\\"/opt/ml/input/data/training/iris_training.csv\\\"\", \"test_path\": \"\\\"/opt/ml/input/data/training/iris_test.csv\\\"\", \"result_dir\": \"\\\"/opt/ml/output\\\"\", \"ti_submit_directory\": \"\\\"cos://ti-ap-shanghai-100010875047-1259675134/tensorflow-2020-04-15-03-26-49-992/source/source.tar.gz\\\"\", \"ti_program\": \"\\\"main.py\\\"\", \"ti_container_log_level\": \"20\", \"ti_job_name\": \"\\\"tensorflow-2020-04-15-03-26-49-992\\\"\", \"ti_region\": \"\\\"ap-shanghai\\\"\"}"
    }
    
    Training job response : {
      "TrainingJobName": "tensorflow-2020-04-15-03-26-49-992",
      "RequestId": "06bb534b-f874-4ba6-9610-1d41f5044417"
    }


### 步骤6：查看输出模型
如果训练任务完成有模型输出，那么 TI 会将模型上传到 cos 上。
您可以通过`output_path='cos://'`指定模型存储的 cos 路径。如果没指定，TI 会按以下格式创建存储桶`ti-[region]-[uin]-[appid]`，最终模型会放在`#{bucket}/#{job_name}/output/`目录下。

### 步骤7：查看训练日志
- TI 训练过程中会把日志上传到 [腾讯云日志服务](https://cloud.tencent.com/product/cls) 中，使用腾讯云日志服务需要先进行开通，计费详情请参考 [CLS 购买指南](https://cloud.tencent.com/document/product/614/11323 )。
- TI 会针对训练任务创建 TiOne 日志集和 TrainingJob 日志主题，通过日志检索功能可以搜索对应训练任务的日志。
- 目前 TI 会默认创建一个日志集（TI）和日志主题（TrainingJob）。
- TI 内置了任务名称（job）关键词，您可以通过以下条件过滤指定任务的日志：

```
job: #{job_name}
```

更多日志检索语法请参考 [开启索引](https://cloud.tencent.com/document/product/614/16981) 文档。

### 步骤8：查看提交历史和监控
您可以在 TI 产品控制台上的【任务列表】>【SDK 任务】中查看您提交的 SDK 任务历史，单击【任务名称】列中的任务名可以看到任务的详细信息，在列表的右侧【监控】可以查看任务运行的资源监控图表。

至此，我们完成了使用腾讯云 TI 平台 TI-ONE 的 TI SDK 训练模型的流程。
