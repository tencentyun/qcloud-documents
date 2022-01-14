## 案例背景
腾讯云 TI 平台 TI-ONE 的 Tensorflow 框架为用户提供了基于 Python API 的 Tensorflow 运行环境，用户可将编写好的脚本及依赖文件上传至框架进行算法训练。

本文以鸢尾花分类任务为例，向用户演示，如何利用 TI-ONE 的深度学习框架 TensorFlow 运行自定义代码，如何通过工作流页面向自定义代码传参，如何查看代码日志/报错信息等。整个工作流运行耗时仅几十秒。

## 数据集介绍
本案例代码修改自 Tensorflow 官方项目。
本案例使用公共的鸢尾花（iris）数据集训练模型，该数据集包含四个特征，分别是花萼长度、花萼宽度、花瓣长度、花瓣宽度，我们根据这四个特征将鸢尾花分成三种物种。

```python
CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']
```

## 整体流程
在腾讯云 TI 平台 TI-ONE 运行用户自定义 TensorFlow 代码，主要包含以下步骤：
1.数据与代码准备。
2.利用 TensorFlow 框架搭建分类模型。
3.运行自定义代码及评估效果查看。
工作流示意图如下：
![](https://main.qcloudimg.com/raw/4b326182a9123aad246122ec0f747e57.png)

>!您可以按需自行配置资源参数，不同资源实例类型对应的价格不同。选择资源时，您可以参看资源参数右上角的**计费说明**。

## 详细流程

#### 一、数据与代码准备
本案例代码取自 TensorFlow 官方项目。

```python
#  Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""An Example of a DNNClassifier for the Iris dataset."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse

import tensorflow as tf

import iris_data

parser = argparse.ArgumentParser()

parser.add_argument('--batch_size', default=100, type=int,
                    help='batch size')
parser.add_argument('--train_steps', default=1000, type=int,
                    help='number of training steps')
parser.add_argument('--train_path', type=str,
                    help='path to the train data file.')
parser.add_argument('--test_path', type=str,
                    help='path to the test data file.')
parser.add_argument('--export_dir', type=str,
                    help='path to export the train model (.pb file)')


def main(argv):
    args = parser.parse_args(argv[1:])

    # Fetch the data
    (train_x, train_y), (test_x, test_y) = iris_data.load_data(args.train_path,
                                                               args.test_path)

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
        input_fn=lambda: iris_data.train_input_fn(train_x, train_y,
                                                  args.batch_size),
        steps=args.train_steps)

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=lambda: iris_data.eval_input_fn(test_x, test_y,
                                                 args.batch_size))

    def serving_input_receiver_fn():
        input_placeholder = tf.placeholder(shape=[4], dtype=tf.string)
        sepal_length_placeholder = tf.strings.to_number(input_placeholder[0:1])
        sepal_width_placeholder = tf.strings.to_number(input_placeholder[1:2])
        petal_length_placeholder = tf.strings.to_number(input_placeholder[2:3])
        petal_width_placeholder = tf.strings.to_number(input_placeholder[3:])

        # How the input data is fed into model_fn.
        features = {
            "SepalLength": sepal_length_placeholder,
            "SepalWidth": sepal_width_placeholder,
            "PetalLength": petal_length_placeholder,
            "PetalWidth": petal_width_placeholder
        }

        return tf.estimator.export.ServingInputReceiver(features,
                                                        input_placeholder)

    if not tf.gfile.Exists(args.export_dir):
        tf.gfile.MakeDirs(args.export_dir)

    classifier.export_saved_model(
        export_dir_base=args.export_dir,
        serving_input_receiver_fn=serving_input_receiver_fn)

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    # Generate predictions from the model
    expected = ['Setosa', 'Versicolor', 'Virginica']
    predict_x = {
        'SepalLength': [5.1, 5.9, 6.9],
        'SepalWidth': [3.3, 3.0, 3.1],
        'PetalLength': [1.7, 4.2, 5.4],
        'PetalWidth': [0.5, 1.5, 2.1],
    }

    predictions = classifier.predict(
        input_fn=lambda: iris_data.eval_input_fn(predict_x,
                                                 labels=None,
                                                 batch_size=args.batch_size))

    template = '\nPrediction is "{}" ({:.1f}%), expected "{}"'

    for pred_dict, expec in zip(predictions, expected):
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(iris_data.SPECIES[class_id],
                              100 * probability, expec))


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)

```

#### 二、利用 TensorFlow 组件搭建分类模型
TensorFlow 是 Google 开源的一种深度学习系统，腾讯云 TI 平台为用户提供了 GPU 集群平台，用户只需申请权限就可以简单配置深度学习任务。Tensorflow 组件中使用的 Python 版本和支持的第三方模块版本信息如下：
 - Python 3.5
 - SciPy 1.0.0
 - NumPy 1.14.0

1. 在 [腾讯云 TI 平台 TI-ONE 控制台](https://console.cloud.tencent.com/tione/project/list) 的左侧导航栏，选择【框架】>【深度学习】>【 TensorFlow】，并拖入画布中。
2. 单击该组件，在右侧弹窗中配置组件参数和资源参数。
![](https://main.qcloudimg.com/raw/9009730a50d712f8066118a0ff3a2682.png)
 - 程序脚本：
    - 单击此处上传用户的自定义代码。
    - 在本文中，内容为上文代码。您可以单击上传本地文件，或选择【新建脚本】，贴入上段代码，将其命名为premade_estimator.py
![](https://main.qcloudimg.com/raw/1cb32b866c8ea97f996930ab8b368173.png)
上传完成后如下图展示：
![](https://main.qcloudimg.com/raw/25f17c0e4c96a7145d52e8884fa21b2a.png) 
 - 依赖包文件：
     - 如果入口脚本需要 import 项目中的其它自己编写的模块，需要将其它模块的代码上传至此。多个.py文件需要压缩成 zip 包上传，该 zip 包会被添加到 Python 的 path 中。
     - 在本文中，我们将 iris_data.py 和 estimator_test.py 两个文件压缩成 iris.zip，您可通过此 [链接](https://jenny-1256633383.cos.ap-chengdu.myqcloud.com/iris.zip) 下载文件，并上传至【依赖包文件】中。
![](https://main.qcloudimg.com/raw/7c9964be5b6b54304590f71ec0127423.png)
上传完成后如下图展示：
![](https://main.qcloudimg.com/raw/ed7ff9fa04a89ec26409c5bb45d0e2d1.png)
 - 程序参数：此处填入用户自定义参数，自定义参数将会传递给入口 py 文件。用户可以在自己的 COS 存储桶中先新建一个文件夹，命名为tf_model，模型将会存储至该路径中，以便后续导入模型时查找。
			--train_path ${ai_dataset_lib}/demo/other/iris_training.csv
			--test_path ${ai_dataset_lib}/demo/other/iris_test.csv
			--export_dir ${cos}/tf_model
 - TensorBoard 目录：指定 Tensorboard 保存路径。本案例此处无需填写。
 - 程序依赖：指定存储于 cos 上的依赖文件的路径，指定内容将被拷贝到程序脚本同一级目录下。本案例此处无需填写。
 - 资源类型：您可按需选择。

#### 三、运行调度及评估效果查看
单击画布上方运行按钮可运行工作流，更多详情请参考 [运行工作流](https://cloud.tencent.com/document/product/851/45653#.E8.BF.90.E8.A1.8C.E5.B7.A5.E4.BD.9C.E6.B5.81)。运行成功后在组件上右击，在【Tensorflow 日志】>【日志详情】中查看日志，模型效果如下图展示：
![](https://main.qcloudimg.com/raw/5baec332b121ffd37aba6bbc441befe1.png)

至此，我们完成了利用腾讯云 TI 平台 TI-ONE 的深度学习框架 TensorFlow 运行自定义代码的全部流程。


