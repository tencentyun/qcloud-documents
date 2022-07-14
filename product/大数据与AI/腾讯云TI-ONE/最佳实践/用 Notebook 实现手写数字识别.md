## 案例背景
手写数字识别是图像识别领域基本任务之一，旨在通过机器学习或深度学习算法将每张手写数字图片分类到0 - 9的数字标签中。在海量的手写数字图像数据集中，MNIST 数据集被学术界、工业界广泛研究。

本文通过腾讯云 TI 平台 TI-ONE 提供的 Notebook，利用 TensorFlow 框架构建一个简单的神经网络来实现 MNIST 手写数字识别。通过本文的学习，您可了解到如何通过 TI-ONE 实现您自己的代码。

## 数据集介绍
用户可从 [MNIST 官网](http://yann.lecun.com/exdb/mnist/) 下载 MNIST 数据集，该数据集由来自250个不同人手写的数字构成，共包含60,000个训练数据，10,000个测试数据，每个数据都是一张28px * 28px大小的灰度图像，该图像空白像素标记为0，有笔迹的地方用0 - 1之间的数值标记笔迹颜色的深浅。手写数字图像示例如下：
![](https://main.qcloudimg.com/raw/426361bfc93a89a622b17d4d5d491cb1/1568170022438.png)

## 整体流程
在腾讯云 TI 平台 TI-ONE 提供的 Notebook 中完成手写数字识别的任务，我们需要完成以下几个步骤：
1. 新建 Notebook 实例
2. 在 Notebook 中，创建 MNIST 手写数字识别项目
   - 创建 Python 文件
   - 从 MNIST 官网下载数据集并上传到项目文件夹中
3. 利用 TensorFlow 实现手写数字识别：
   - 安装并导入所需依赖包
   - 加载 MNIST 数据集
   - 数据集可视化展示
   - 构建手写数字识别模型
   - 模型评估输出模型准确率

## 详细流程
#### 新建 Notebook 实例
1. 登录 [腾讯云 TI 平台 TI-ONE 控制台](https://console.cloud.tencent.com/tione/project/list) 后，单击菜单栏的【Notebook】，页面跳转至 Notebook 实例列表页面。新增实例，配置参数（以下以广州地域为例说明）：
   - 地区：广州
   - Notebook名称：mnist
   - 资源选择：您可按需选择
   - 存储大小：10
   - Root 权限：允许
   - 生命周期配置：不使用生命周期脚本
   - Git 存储：无
   - VPC：无 VPC
   - CLS 日志服务：关闭
   - 自动停止：关闭
2. 待 Notebook 实例创建完成后状态为：运行中，单击【打开】进入 Notebook 操作页面

#### 创建 MNIST 手写数字识别项目
1. 在 Notebook 操作页面，选择【conda_tensorflow_py3】内核，进入项目后，将项目重命名为：MNIST.ipynb
2. 在 MNIST.ipynb 的同级目录处，新建文件夹【MNIST_data】，并将 [MNIST 官网](http://yann.lecun.com/exdb/mnist/) 提供的四个数据集下载后上传至该文件夹中：
 - train-images-idx3-ubyte.gz
 - train-labels-idx1-ubyte.gz
 - t10k-images-idx3-ubyte.gz
 - t10k-labels-idx1-ubyte.gz

![](https://main.qcloudimg.com/raw/21fe51c6350e640b07aa5d873b2889d7.png)

#### 利用 TensorFlow 实现 MNIST 手写数字识别
1. 在 Notebook 中导入所需依赖包，您可直接复制以下所有代码块到 Notebook 中运行。
```
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
```

2. 加载 MNIST 数据集
```text
 mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
```

3. 可视化查看数据内容
选择数据集中的一个示例打印出来，查看数据内容。
>?此处打印的数据每次都是随机的，可能内容不一样。

为更直接查看数据图像内容，我们可将数据 reshape 成28 * 28的矩阵，然后打印一个黑白图片（Greys），同时输出查看该图片的标签（数字“8”的标签会在10维向量中第9位设置为1，其余为0）
```text
im = mnist.train.images[0].reshape(28, 28)
plt.imshow(im, cmap='Greys')
plt.show()
print(mnist.train.labels[0])
```

![](https://main.qcloudimg.com/raw/52f9418ea4d2c891a08761f12a3148a9/1568184594782.png)

4. 搭建手写数字识别模型
```
   # 模型构建
   sess = tf.InteractiveSession()
   x = tf.placeholder(tf.float32, [None, 784])
   W = tf.Variable(tf.zeros([784,10]))
   b = tf.Variable(tf.zeros([10]))
   
   y = tf.nn.softmax(tf.matmul(x,W) + b)
   
   y_ = tf.placeholder(tf.float32, [None,10])
   cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),reduction_indices=[1]))
   train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
   
   # 模型训练
   tf.global_variables_initializer().run()
   
   for i in range(1000):
       batch_xs, batch_ys = mnist.train.next_batch(100)
       train_step.run({x: batch_xs, y_: batch_ys})
```

5. 模型评估
```
   correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
   accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
   
   print('MNIST手写数字模型准确率：')
   print(accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))
```

>!由于随机因素的存在，模型每次运行准确率不一定完全一致

模型准确率输出可参考下图示例：
![](https://main.qcloudimg.com/raw/e30ac5515b436238545355a0509056e0.png)
