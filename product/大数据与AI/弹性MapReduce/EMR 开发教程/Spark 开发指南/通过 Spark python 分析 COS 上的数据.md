本节主要是通过 Spark Python 来进行 wordcount 的工作。
## 1.	开发准备
- 因为任务中需要访问腾讯云对象存储（COS），所以需要在 COS 中先 [创建一个存储桶（Bucket）](https://cloud.tencent.com/document/product/436/6232)。
- 确认您已经开通了腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置见面选择 Spark 组件，并且在基础配置页面勾选“开启 COS”，在下方填写自己的 SecretId 和 SecretKey。SecretId 和 SecretKey 可以在 [API 密钥管理界面](https://console.cloud.tencent.com/cam/capi) 查看。如果还没有密钥，请单击【新建密钥】建立一个新的密钥。

## 2.	数据准备
需要处理的文件需要事先上传到 COS 中。如果文件在本地那么就可以通过 [COS 控制台直接上传](https://cloud.tencent.com/document/product/436/13321)。如果文件在 EMR 集群上，可以使用 Hadoop 命令上传。指令如下：
```
[hadoop@10 hadoop]$ hadoop fs -put $testfile cosn:// $bucketname/
```
其中 $testfile 为要统计的文件的完整路径加名字，$bucketname 为您的存储桶名。上传完成后可以查看文件是否已经在 COS 中。

## 3.	运行样例
首先需要登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里我们可以选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入 Spark 安装目录`/usr/local/service/spark`：
```
[root@172 ~]# su hadoop
[hadoop@172 root]$ cd /usr/local/service/spark
```
新建一个 Python 文件 wordcount.py，并添加如下代码：
```
from __future__ import print_function

import sys 
from operator import add
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    sc = spark.sparkContext

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)

    output = counts.collect()
    counts.saveAsTextFile(sys.argv[2])

    spark.stop()
```
通过如下指令提交任务：
```
[hadoop@10   spark]$   ./bin/spark-submit   --master yarn   ./wordcount.py 
cosn://$bucketname/$yourtestfile cosn:// $bucketname/$output
```
其中 $bucketname 为您的 COS 存储桶名，$yourtestfile 为您的测试文件在存储桶中的完整路径加名字。$output 为您的输出文件夹。**$output 为一个未创建的文件夹，如果执行指令前该文件夹已经存在，会导致程序运行失败。**

成功后程序自动运行，可以在目标存储桶中查看到输出文件：
```
[hadoop@172 spark]$ hadoop fs -ls cosn:// $bucketname/$output
Found 2 items
-rw-rw-rw- 1 hadoop Hadoop 0 2018-06-29 15:35 cosn:// $bucketname/$output /_SUCCESS
-rw-rw-rw- 1 hadoop Hadoop 2102 2018-06-29 15:34 cosn:// $bucketname/$output /part-00000
```
最后的结果也可以通过如下指令查看：
```
[hadoop@172 spark]$ hadoop fs -cat cosn:// $bucketname/$output /part-00000
(u'', 27)
(u'code', 1)
(u'both', 1)
(u'Hadoop', 1)
(u'Bureau', 1)
(u'Department', 1)
```
同样可以把结果输出到 HDFS 中，只需要更改指令中的输出位置即可，如下所示：
```
[hadoop@10spark]$   ./bin/spark-submit   ./wordcount.py
cosn://$bucketname/$yourtestfile /user/hadoop/$output
```
其中`/user/hadoop/`为 HDFS 中的路径，如果不存在用户可以自己创建。
任务结束后，可以通过如下命令看到 Spark 运行日志：
```
[hadoop@10 spark]$  /usr/local/service/hadoop/bin/yarn logs -applicationId $yourId
```
其中 $yourId 应该替代为您的任务 ID。任务 ID 可以在 YARN 的 WebUI 上面进行查看。
