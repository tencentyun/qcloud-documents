## 背景

本文指导如何使用 Python 的工具包 pyarrow 操作 CHDFS。

## 部署环境

1. Python 3.7版本及以上。PyArrow 目前与 Python 3.7、3.8、3.9 和 3.10 兼容。
2. 使用如下命令，安装 pyarrow 库：
```
pip3 install pyarrow -image pip3 install pyarrow -image -i http://mirrors.tencent.com/pypi/simple --trusted-host mirrors.tencent.com
```

## 部署组件

部署 CHDFS 插件的方法，请参考 [挂载 CHDFS](https://cloud.tencent.com/document/product/1105/36368)。

## 编写 Python 程序

1. 使用 pyarrow 访问 CHDFS，示例代码如下：
```
import pyarrow as pa

host = "ofs://xxx-xxx.chdfs.ap-guangzhou.myqcloud.com"
fs = pa.hdfs.connect(host, 0)
# open（path, mode）模式w,文件不存在创建一个文件
out_file = fs.open("ofs://xxx-xxx.chdfs.ap-guangzhou.myqcloud.com/ppyarrow.txt","wb")
out_file.write(str.encode("hello world, pyarrow")) #写
out_file.close()

in_file = fs.open("ofs://xxx-xxx.chdfs.ap-guangzhou.myqcloud.com/ppyarrow.txt","rb")
# 将光标重置到起始位置
in_file.seek(0)
data = in_file.read() # 读
print("写入的数据为%s."%(data))
in_file.close()

# 列出文件
ls_file = fs.ls("ofs://xxx-xxx.chdfs.ap-guangzhou.myqcloud.com/")
print("目录文件为%s." %(ls_file))

# 创建目录
fs.mkdir("ofs://xxx-xxx.chdfs.ap-guangzhou.myqcloud.com/pyarrowtest")
# 移动并重命名文件
fs.mv("ofs://xxx-xxx.chdfs.ap-guangzhou.myqcloud.com/ppyarrow.txt", "ofs://xxx-xxx.chdfs.ap-guangzhou.myqcloud.com/pyarrowtest/tina.txt")
# 列出文件
mv_file = fs.ls("ofs://xxx-xxx.chdfs.ap-guangzhou.myqcloud.com/pyarrowtest")
print("移动后的目录文件为%s." %(mv_file))

# 删除测试文件，重新列出文件
fs.delete("ofs://xxx-xxx.chdfs.ap-guangzhou.myqcloud.com/pyarrowtest/tina.txt")
de_file = fs.ls("ofs://xxx-xxx.chdfs.ap-guangzhou.myqcloud.com/pyarrowtest/")
print("删除文件后的pyarrowtest目录下文件为%s." %(de_file))
```
2. 设置环境变量，示例如下：
```
export JAVA_HOME=/usr/local/jdk   #设置JAVA_HOME，根据自己安装位置定
export HADOOP_HOME=/usr/local/service/hadoop  #设置HADOOP_HOME，hadoop的安装位置
export CLASSPATH=`$HADOOP_HOME/bin/hadoop classpath --glob`
#参考网址https://arrow.apache.org/docs/python/filesystems.html#hadoop-file-system-hdfs
```
3. 执行 Python 文件：
```
python3 libtest.py
```
4. 执行过程及结果如下：
![](https://qcloudimg.tencent-cloud.cn/raw/34bbfa9024866e17474311cb6a99da60.png)

## 相关参考

- [Filesystem Interface](https://arrow.apache.org/docs/python/filesystems.html#hadoop-file-system-hdfs)
- [Building Python and OpenSSL from source, but ssl module fails](https://stackoverflow.com/questions/60536472/building-python-and-openssl-from-source-but-ssl-module-fails)

