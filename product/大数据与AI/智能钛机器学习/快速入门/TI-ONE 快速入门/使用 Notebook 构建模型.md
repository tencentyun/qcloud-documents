## 操作背景
- Notebook 是腾讯云 TI 平台 TI-ONE 为开发者量身打造的灵活的交互式开发工具，您可以在腾讯云 TI 平台 Notebook 中完成数据准备、数据预处理、算法调试与模型训练，无需多平台切换，更多详情请见 [Notebook 简介](https://cloud.tencent.com/document/product/851/44449)。
- 为了方便您有效地使用腾讯云 TI 平台 TI-ONE 的 Notebook，本文档将通过一个案例向您演示使用流程。
- 在使用之前，请确保您已经完成了 [注册与开通服务](https://cloud.tencent.com/document/product/851/39086)。

## 操作步骤

### 步骤1：创建实例
1. 登录 [腾讯云 TI 平台 TI-ONE 控制台](https://console.cloud.tencent.com/tione/notebook) ，单击左侧导航栏的【Notebook】，页面将跳转至 Notebook 的实例列表页面，此页面将罗列用户创建的所有 Notebook 实例。
2. 在 Notebook 实例列表页，单击左上角【新增实例】，跳转至创建 Notebook 实例的设置页面。
3. 在【新增实例】页面，可填写以下相关字段：
   - **地区**：此字段不可修改，将自动显示平台选择的地区。
   - **Notebook 名称**：设置此 Notebook 实例的名称。
   - **资源选择**：选择此实例需要配置的资源。（**注意：**只要 Notebook 实例处于运行中，都将对配置的资源进行按时收费。 ）
   - **存储大小**：Notebook 实例的存储大小（以 GB 为单位），最小值为 10GB 且为10的倍数，注意：请大于当前硬盘值，最大值为 1000 GB。
 - 单击【高级设置】此选项可根据需求进行设置（默认不展开），可配置：
    - **Root 权限**：选择是否赋予 root 权限来访问 Notebook。如果启用 Root 权限，则所有 Notebook 实例用户具有管理员权限，并且可以访问和编辑实例上的所有文件。
    - **生命周期配置**：选择是否使用生命周期脚本。
    - **Git 存储：**此为可选项，用户可以前往 Git 存储库-新增存储库进行配置。
    - **VPC**：用户可以选择配置自有的 VPC 网络。
    - **CLS 日志服务**：用户可以自行选择是否开通 CLS 日志服务。
    - **自动停止**：开启该选项后，该实例将在运行时长超过您选择的时长后自动停止。
 - 且平台会根据您以上选择的配置，计算对应的价格：
    - **计算资源价格**：平台根据您选择的配置显示相关价格。
    - **存储资源价格**：平台根据您选择的配置显示相关价格。
    - **总价**：平台根据您选择的配置显示相关价格。
4. 以上信息已填写完成后，单击【创建】，Notebook 列表中将新增一条实例记录，用户可单击【状态】查看实例创建进程，当实例状态由【创建中】变为【运行中】时，单击【打开】进入 Notebook 实例内部。
5. 进入实例内部后，您可以根据需要设置内核环境。本案例使用 conda_tensorflow_py3。
![](https://main.qcloudimg.com/raw/7c929ad851ef6d243634647ac54de279.png)



### 步骤2：数据导入

本案例代码来自 Tensorflow 官方项目。我们使用公共的鸢尾花（iris）数据集训练模型，该数据集包含四个特征，分别是花萼长度、花萼宽度、花瓣长度、花瓣宽度，我们根据这四个特征将鸢尾花分成三种物种。

```python
CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']
```

本测试数据存储在 COS 广州地域，您可 [单击查看](https://tesla-ap-guangzhou-1256322946.cos.ap-guangzhou.myqcloud.com/cephfs/tesla_common/deeplearning/dataset/contest/demo.zip)，在 Notebook 中导入所需数据。

```python
!pip install wget
import wget, tarfile
filename = wget.download("https://tesla-ap-guangzhou-1256322946.cos.ap-guangzhou.myqcloud.com/cephfs/tesla_common/deeplearning/dataset/contest/demo.zip")
print(filename)
```

```python
import zipfile
zFile = zipfile.ZipFile(filename, "r")
for fileM in zFile.namelist(): 
    zFile.extract(fileM, "./")
    print(fileM)
zFile.close();
```

### 步骤3：模型训练
您可以自行编写代码进行模型构建、模型训练、模型评估。

```python
import pandas as pd
import tensorflow as tf


CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth',
                    'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']


def load_train_data(train_path, y_name='Species'):
    """Returns the iris dataset as (train_x, train_y)"""

    train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
    train_x, train_y = train, train.pop(y_name)

    return (train_x, train_y)


def load_test_data(test_path):
    """Returns the iris dataset as test_x"""

    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES[:-1], header=0)
   
    return test


def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    return dataset


def eval_input_fn(features, labels, batch_size):
    """An input function for evaluation or prediction"""
    features=dict(features)
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)

    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the dataset.
    return dataset
```

```python
import os
def main():
    
    batch_size = 100
    
    train_steps = 1000

    # Fetch the data
    (train_x, train_y) = load_train_data("iris_training.csv")

    # Feature columns describe how to use the input.
    my_feature_columns = []
    for key in train_x.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    # Build 2 hidden layer DNN with 10, 10 units respectively.
    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # Two hidden layers of 10 nodes each.
        hidden_units=[10, 10],
        # The model must choose between 3 classes.
        n_classes=3,
    )

    # Train the Model.
    classifier.train(
        input_fn=lambda: train_input_fn(train_x, train_y,
                                                  batch_size),
        steps=train_steps)

    # Generate predictions from the model
    test_x = load_test_data("iris_test.csv")

    predictions = classifier.predict(
        input_fn=lambda: eval_input_fn(test_x,
                                                 labels=None,
                                                 batch_size=batch_size))
    result = []
    template = 'Prediction is "{}" ({:.1f}%)'
    for pred_dict in predictions:
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]
        print(template.format(SPECIES[class_id],
                              100 * probability))
        result.append(class_id)

    result_df = pd.DataFrame(data=result)

    result_df.to_csv("result_file", index=False)
    
    print("result file is saved")


main()
```

### 步骤4：结果保存
#### 1. 结果文件路径
您可以自行指定将实验结果保存到 [个人存储桶](https://console.cloud.tencent.com/cos5) 中的特定 COS 文件路径下。

path：结果文件路径。
bucket：指定存储桶。注意：请指定用户对应地域下的个人 COS 存储桶，使用示例中的存储桶会导致报错。
key_prefix：存储桶下 COS 路径地址。

```python
from ti import session
ti_session = session.Session()
inputs = ti_session.upload_data(path="result_file", bucket="demo-project-ap-guangzhou-1259675134", key_prefix="contest")
```

#### 2. 结果文件查看
您可以到 COS 中您指定的路径下查看结果文件。此外，您可以自行下载文件，单击【详情】，还可在详情页面获取【对象地址】。
![](https://main.qcloudimg.com/raw/4386d90ad0f6a9016dd5fc4cde7fe8df.png)
至此，我们完成了使用腾讯云 TI 平台 TI-ONE 的 Notebook 训练模型的流程。
