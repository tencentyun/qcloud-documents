## Jupyter Notebook 简介
Jupyter Notebook 是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。详情可查看 [Jupyter Notebook 官方介绍](https://jupyter-notebook.readthedocs.io/en/latest/notebook.html)。

简而言之，Jupyter Notebook 是以网页的形式打开，可以在网页页面中直接编写代码和运行代码，代码的运行结果也会直接在代码块下显示。如在编程过程中需要编写说明文档，可在同一个页面中直接编写，便于作及时的说明和解释。

### 组成部分
- 网页应用
网页应用即基于网页形式的、结合了编写说明文档、数学公式、交互计算和其他富媒体形式的工具。简言之，网页应用是可以实现各种功能的工具。
- 文档
Jupyter Notebook 中所有交互计算、编写说明文档、数学公式、图片以及其他富媒体形式的输入和输出，都是以文档的形式体现的。这些文档是保存为后缀名为`.ipynb`的`JSON`格式文件，不仅便于版本控制，也方便与他人共享。此外，文档还可以导出为 HTML、LaTeX、PDF 等格式。

### Jupyter Notebook 的主要特点
1. 编程时具有语法高亮 、缩进、tab 补全的功能。
2. 可直接通过浏览器运行代码，同时在代码块下方展示运行结果。
3. 以富媒体格式展示计算结果。富媒体格式包括 HTML、LaTeX、PNG、SVG 等。
4. 对代码编写说明文档或语句时，支持 Markdown 语法。
5. 支持使用 LaTeX 编写数学性说明。

## 安装 jupyter
进入 EMR [购买页](https://cloud.tencent.com/product/emr)。
- 选择产品版本：EMR-V2.3.0。
- 在【可选组件】列表中，选择【tensorflowonspark 1.4.4】后就会默认安装 Jupyter，安装目录位于`/usr/local/server/jupyter`；jupyter 不会启动任何服务，如果您没有安装 tensorflowonspark，那默认的安装路径位于`/usr/local/server/apps/jupyter`。

## 使用 jupyter
### 初始化 jupyter 配置
```
Usage: init.sh [password] [port]
# 示例
./init.sh 123456 10086
```
一路回车，会出现提示：
```
[hadoop@10 jupyter]$ ./init.sh 123456 10086
Your password is: 123456
Your signature is: sha1:139fa061bae6:bcdc6a7870878458c7c14594fe65dd21f85f84a4
Generating a 4096 bit RSA private key
.............................++
..................................................................................++
writing new private key to '/usr/local/service/jupyter/conf/jkey.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:
State or Province Name (full name) []:
Locality Name (eg, city) [Default City]:
Organization Name (eg, company) [Default Company Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (eg, your name or your server's hostname) []:
Email Address []:
Jupyter config has already generated at /usr/local/service/jupyter/conf/jupyter_notebook_config.py
Now, you can execute the following command to start jupyter:
jupyter notebook --config=/usr/local/service/jupyter/conf/jupyter_notebook_config.py --allow-root
```
这里生成了 jupyter 配置，您也可以修改生成的配置文件`jupyter_notebook_config.py`中的相关参数，参考 jupyter 官网即可。
>!最后一行是启动命令，复制这行命令即可启动 jupyter。


### 启动 jupyter notebook
```
jupyter notebook --config=/usr/local/service/jupyter/conf/jupyter_notebook_config.py --allow-root
[I 10:47:46.972 NotebookApp] Writing notebook server cookie secret to /home/hadoop/.local/share/jupyter/runtime/notebook_cookie_secret
[I 10:47:47.748 NotebookApp] Serving notebooks from local directory: /usr/local/service/jupyter
[I 10:47:47.749 NotebookApp] The Jupyter Notebook is running at:
[I 10:47:47.749 NotebookApp] https://(10.0.0.7 or 127.0.0.1):10086/
[I 10:47:47.749 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```
### 访问 jupyter 
在 web 页面上打开 jupyter（在此之前可能需要去安全组打开 jupyter 端口）：
```
https://IP:10086/
```
这里端口10086是上面初始化`init.sh`的参数。
![](https://main.qcloudimg.com/raw/fc370907923fb342b0b27b1fad1f6d2a.png)
在这里输入刚设置的密码后即可进入 jupyter 主页。

### 使用 jupyter 进行开发操作
#### **创建目录**
![](https://main.qcloudimg.com/raw/a3f45bd82c24abf780f9916ea388f693.png)
#### **rename 目录**
![](https://main.qcloudimg.com/raw/7ec7be4ee84cd0a2ba5ac9e69561856b.png)
#### **编写 tensorflow 代码**
可参考 [tensorflow 官网](https://github.com/tensorflow/docs/tree/master/site/en/r1/tutorials)。
![](https://main.qcloudimg.com/raw/ae58da462ab0f93f1078737959998397.png)
>?这里需下载数据集，国内网速会比较慢。
>
```
import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
tf.keras.layers.Flatten(input_shape=(28, 28)),
tf.keras.layers.Dense(512, activation=tf.nn.relu),
tf.keras.layers.Dropout(0.2),
tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
```
#### 运行代码
重新在 jupyter 上执行模型训练。
![](https://main.qcloudimg.com/raw/5c77e7740257a832c92ed87d2058f9ae.png)
#### 停止 jupyter 服务
```
./stop_jupy.sh [jupyter_port]
```

