## CHDFS 准备工作

1. 在腾讯云官网创建 CHDFS 文件系统和 CHDFS 挂载点，配置好权限信息。
2. 通过腾讯云 VPC 环境的 CVM 机器访问创建好的 CHDFS，详情请参见 [创建 CHDFS](https://cloud.tencent.com/document/product/1105/37234)。
3. 当挂载成功后，打开 hadoop 命令行工具，并执行以下命令，验证 CHDFS 功能是否正常。
```bash
hadoop fs -ls ofs://f4xxxxxxxxxxxxxxx.chdfs.ap-beijing.myqcloud.com/
```
如果能看到以下类似的输出，则表示云 HDFS 功能一切正常。
![](https://main.qcloudimg.com/raw/3be9476976dd7da027ea6e634652c00b.png)

## Tensorflow 准备工作

1. 通过 [官方 Github](https://github.com/tensorflow/tensorflow) 下载 Tensorflow。
2. 参考 [腾讯云支持 CHDFS patch](https://github.com/tensorflow/tensorflow/compare/master...jimmyyan:master#diff-b6e19034b00093723ad953a6ffb8528b9d311a86a650be0bb7ad58900bfb03f9R187)，修改 tensorflow 源码，本文示例采用 tensorflow 2.5版本编译。
3. 参考 [tensorflow 编译教程](https://tensorflow.google.cn/install/source?spm=a2c4g.11186623.0.0.1d575b294FeONq)，编译修改源码后的 tensorflow。
4. 待编译完成后，安装 tensorflow 模块，并且验证。
>? tensorflow 代码版本差异较大，如果您使用的 tensorflow 非2.5版本，遇到代码问题，可以寻求 CHDFS 团队协助。
>


## Tesorflow 读写 CHDFS 验证

1. 在 CHDFS 上创建测试文件：
```bash
hadoop fs -copyFromLocal ./testfile ofs://f4xxxxxxxxxxxxxxx.chdfs.ap-beijing.myqcloud.com/testfile

hadoop fs -cat ofs://f4xxxxxxxxxxxxxxx.chdfs.ap-beijing.myqcloud.com/testfile
hello, world
```
2. 使用 TensorFlow 的 API 查看 CHDFS 上的数据。
```bash
➜  ~ python3
Python 3.9.6 (default, Jun 29 2021, 05:25:02)
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> with tf.gfile.Open('ofs://f4xxxxxxxxxxxxxxx.chdfs.ap-beijing.myqcloud.com/testfile') as rf:
...     rf.read()
'hello, world\n'
>>> 
```
>? `ofs://f4xxxxxxxxxxxxxxx.chdfs.ap-beijing.myqcloud.com` 为测试的挂在点信息，需要您替换成真实的挂载点信息。
>
