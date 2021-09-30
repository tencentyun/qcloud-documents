TensorFlow 是一个端到端开源机器学习平台。它拥有一个全面而灵活的生态系统，其中包含各种工具、库和社区资源，可助力研究人员推动先进机器学习技术的发展，并使开发者能够轻松地构建和部署由机器学习提供支持的应用。
- 轻松地构建模型
在即刻执行环境中使用 Keras 等直观的高阶 API 轻松地构建和训练机器学习模型，此环境使我们能够快速迭代模型并轻松地调试模型。
- 随时随地进行可靠的机器学习生产
无论您使用哪种语言，都可以在云端、本地、浏览器中或设备上轻松地训练和部署模型。
- 强大的研究实验
一个简单而灵活的架构，可以更快地将新想法从概念转化为代码，然后创建出先进的模型，并最终对外发布。

## Tensorflow 架构
 ![](https://main.qcloudimg.com/raw/a4a4aab73f265e233ee76fa00cfa3ae1.png)
- 客户端（Client）
将计算过程定义为数据流图。使用`_Session_`初始化数据流图的执行。
- 分布式主控端（Master）
修剪图中的某些特殊子图，即`Session.run()`中所定义的参数。将子图划分为在不同进程和设备中运行的多个部分。将图分发给不同的工作进程。由工作进程初始化子图的计算。
- 工作进程（Worker service）（每个任务的）
使用内核实现调度图操作并在合适的硬件（CPU、GPU 等）执行。向其他工作进程发送或从其接收操作的结果。
- 内核实现
执行一个独立的图操作计算。

## EMR 支持 Tensorflow
- Tensorflow 版本：v1.14.0
- 目前 Tensorflow 只支持运行在 CPU 机型，暂不支持 GPU 机型
- 支持 tensorflow on spark 做分布式训练
 
## Tensorflow 开发示例
首先需要安装 Tensorflow，切换到 root 用户下，密码为创建 EMR 集群时设置的密码，先安装 python-pip 工具再安装依赖包：
```
[hadoop@172 hbase]$ su
Password: ********
[root@172 hbase]# yum install python-pip
[root@172 hbase]# pip install Tensorflow
```
编写代码：`test.py`
```
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print sess.run(hello)
a = tf.constant(10)
b = tf.constant(111)
print sess.run(a+b)
exit()
```
执行如下命令：
```
python test.py
```
更多用法请参考 Tensorflow 官网。
