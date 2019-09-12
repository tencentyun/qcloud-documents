Tensorflow 组件为用户提供了基于 Python API 的 Tensorflow 运行环境，用户可将编写好的脚本及依赖文件上传至组件进行算法训练。

## 版本说明
Tensorflow 组件中使用的 Python 版本和支持的第三方模块版本信息如下：
   - Python 2.7.12
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
   








