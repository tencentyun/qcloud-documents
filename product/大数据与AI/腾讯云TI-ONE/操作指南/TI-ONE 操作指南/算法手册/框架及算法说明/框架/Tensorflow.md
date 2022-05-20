Tensorflow 框架为用户提供了基于 Python API 的 Tensorflow 运行环境，用户可将编写好的脚本及依赖文件上传至该框架进行算法训练。

## 版本说明
Tensorflow 框架版本及框架中使用的 Python 版本和支持的第三方模块版本信息如下：
<table>
     <tr>
         <th width=25%>Tensorflow 版本</th>  
         <th width=25%>Python 版本</th>  
         <th width=25%>scipy 版本</th> 
         <th width=25%>numpy 版本</th> 
     </tr>
     <tr>      
      <td>tensorflow 2.0</td>   
      <td>Python 3.5</td>   
      <td>scipy 1.1.0</td>   
	<td>numpy 1.18.5</td>  
     </tr>
     <tr>      
      <td>tensorflow 1.14</td>   
      <td>Python 3.5</td>   
      <td>scipy 1.1.0</td>   
	<td>numpy 1.15.4</td>  
     </tr> 
     	<tr>      
      <td>tensorflow 1.12</td>   
      <td>Python 3.5</td>   
      <td>scipy 1.1.0</td>   
	<td>numpy 1.15.4</td>  
     </tr> 
</table>

如果您需要使用其他第三方的 lib，可使用 pip 在代码内安装，示例如下：
```python
from pip._internal import main
main(['install', "package_name"])
```


## 操作步骤
1. **添加组件**
 从左侧菜单栏中，选择【框架】>【深度学习】列表下的【Tensorflow 】节点，并将其拖拽至画布中。
2. **配置参数**
 - 脚本及依赖包文件上传 ：将任务脚本上传至程序脚本框。如果需要依赖文件，则压缩为 zip 文件后通过 依赖包文件 框上传。
 - 程序依赖：指定位于 COS 中的用户依赖文件路径，指定内容将被拷贝到程序脚本同一级目录下。支持目录或者文件依赖，若存在多个文件则以英文逗号分隔 。
 - 程序参数：指定运行任务脚本的参数。
 - TensorBoard 目录：指定 Tensorboard 保存路径。
3. **配置资源**
在【资源参数】列表框配置任务的资源参数。
4. **运行**
单击【保存】并运行工作流。
5. **查看 Tensorflow 控制台和日志**
在 Tensorflow 节点上单击右键菜单，可查看任务状态和详细日志。  
6. **查看 Tensorboard**
  组件处于“运行中”状态时，您可以右键单击任务栏，通过【Tesnorflow 控制台】>【Tensorboard】查看 Tensorboard 信息。

## 案例说明
本案例提供一段代码，向您演示如何利用 TensorFlow 框架运行自定义代码，如何通过工作流页面向自定义代码传参，如何查看代码日志/报错信息等。
本案例代码修改自 TensorFlow 的官方项目。
![](https://main.qcloudimg.com/raw/699578068afaa722ce193bb8c9c7d621.png)

1. 程序的入口脚本为 premade_estimator.py。单击【Tensorflow 框架】的【程序脚本】输入框，选择premade_estimator.py 脚本文件上传。
2. 如果入口脚本需要 import 项目中的其它自己编写的模块，需要将其它模块的代码压缩成 zip 包，并上传到【Tensorflow】组件的【依赖包文件】中，该 zip 包会被添加到 Python 的 path 中。在本 demo 中，我们将 iris_data.py 和 estimator_test.py 两个文件压缩成 iris.zip，上传至【依赖包文件】中，此时，程序脚本中可以使用import iris_data 来引入这一模块。
3. 如果入口脚本需要启动参数，如本 demo 中，入口脚本 premade_estimator.py 可以接收--batch_size，--train_steps，--train_path 和--test_path 四个参数，则将参数及其取值填写到【程序参数】输入框中。
示例代码为：
--train_steps 2000
--batch_size 100
--train_path ${ai_dataset_lib}/demo/other/iris_training.csv
--test_path ${ai_dataset_lib}/demo/other/iris_test.csv
4. 如果自行编写的 Tensorflow 代码会产生用于 Tensorboard 展示的文件（如 events 文件），则可以在自定义的代码中，将这些文件输出到 COS 的某个特定目录，并在【Tensorboard 目录】输入框中填写该目录的路径。如果填写了，训练过程中可以在【Tensorflow 控制台】>【Tensorboard】中查看 Tensorboard。
5. 运行后，可以右键单击算子，并在【Tensorflow 控制台】>【App 详情】中查看 stdout 和 stderr 两个日志。







