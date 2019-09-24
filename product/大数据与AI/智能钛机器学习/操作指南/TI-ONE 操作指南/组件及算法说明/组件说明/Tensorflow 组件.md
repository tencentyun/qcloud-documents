Tensorflow 组件为用户提供了基于 Python API 的 Tensorflow 运行环境，用户可将编写好的脚本及依赖文件上传至组件进行算法训练。

## 版本说明
Tensorflow 组件中使用的 Python 版本和支持的第三方模块版本信息如下：
   - Python 2.7/3.5
   - SciPy 1.0.0
   - NumPy 1.14.0
   
如果您需要使用其他第三方的 lib，可使用 pip 在代码内安装，示例如下：
```
import pip
pip.main(['install', "package_name"])
```


## 操作步骤
1. **添加组件**
 从左侧菜单栏中，选择【组件】>【深度学习】列表下的 Tensorflow 节点，并将其拖拽至画布中。
2. **配置参数**
 - 脚本及依赖包文件上传 ：
  将任务脚本上传至 程序脚本 框。如果需要依赖文件，则压缩为zip文件后通过 依赖包文件 框上传。
![](https://main.qcloudimg.com/raw/f502e40c73117cfddef50af122cec760.png)
 - 程序依赖：
  指定位于 COS 中的用户依赖文件路径，指定内容将被拷贝到程序脚本同一级目录下。支持目录或者文件依赖，若存在多个文件则以英文逗号分隔 。
 - 程序参数：
  指定运行任务脚本的参数。
 - TensorBoard 目录 :
  指定 Tensorboard 保存路径。
 - Python 版本：指定 Tensorflow 运行的 Python 版本，支持 Python 2.7 和 Python 3.5 两个版本。
![](https://main.qcloudimg.com/raw/1012cc3a97a1167ef922d291fa9c080a.png)
3. **配置资源**
  在【资源参数】列表框配置任务的资源参数。
![](https://main.qcloudimg.com/raw/3c14b0568ea191bcdf63219619b07c73.png)
4. **运行**
单击【保存】并运行工作流。
5. **查看 Tensorflow 控制台和日志**
在 Tensorflow 节点上单击右键菜单，可查看任务状态和详细日志。
![](https://main.qcloudimg.com/raw/3e63d0f8bd8d5a3eca04eafea4fff667.png)  
详细日志如下：
![](https://main.qcloudimg.com/raw/e08fd4e5993050ca8c8f3a497696f02e.png)
>?stdout.log 为全部日志，stderr.log 为错误日志。

6. **查看 Tensorboard**
  组件处于“运行中”状态时，您可以右键单击任务栏，通过【Tesnorflow 控制台】>【Tensorboard】查看 Tensorboard 信息。
![](https://main.qcloudimg.com/raw/4068ddf48a43bc659966d938d014e2d0.png)


案例说明：

本案例提供了一段从文件读取IRIS数据集，训练基于神经网络的分类器，评估分类器的效果，并用训练好的分类器对新的数据进行预测代码，并展示如何让代码在智能钛平台上运行。

代码修改自Tensorflow[官方项目](https://github.com/tensorflow/models/tree/master/samples/core/get_started)。

![](https://main.qcloudimg.com/raw/699578068afaa722ce193bb8c9c7d621.png)

1. 程序的入口脚本为premade_estimator.py。因此，我们点击【Tensorflow组件】的【程序脚本】输入框，选择premade_estimator.py这个脚本文件上传。

2. 如果入口脚本需要import项目中的其它自己编写的模块，需要将其它模块的代码压缩成zip包，并上传到【Tensorflow】组件的【依赖包文件】中，该zip包会被添加到python的path中。在本demo中，我们将iris_data.py和estimator_test.py两个文件压缩成iris.zip，上传至【依赖包文件】中，此时，程序脚本中可以使用import iris_data来引入这一模块。

3. 如果入口脚本需要启动参数，如本demo中，入口脚本premade_estimator.py可以接收--batch_size，--train_steps，--train_path和--test_path四个参数，则将参数及其取值填写到【程序参数】输入框中。
示例代码为：
--train_steps 2000
--batch_size 100
--train_path ${ai_dataset_lib}/demo/other/iris_training.csv
--test_path ${ai_dataset_lib}/demo/other/iris_test.csv

4. 如果自行编写的Tensorflow代码会产生用于Tensorboard展示的文件（如events文件），则可以在自定义的代码中，将这些文件输出到cos的某个特定目录，并在【Tensorboard目录】输入框中填写该目录的路径。如果填写了，训练过程中可以在【日志信息】——【Tensorflow控制台】——【Tensorboard】中查看Tensorboard。

5. 运行后，可以右键点击算子，并在【日志信息】——【Tensorflow控制台】——【App详情】中查看stdout和stderr两个日志。
   








