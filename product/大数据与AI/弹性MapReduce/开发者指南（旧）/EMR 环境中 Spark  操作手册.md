本文档只描述了基本的 Spark 任务提交以及 Spark 计算任务如何访问腾讯云对象存储上的数据，详细资料可以参考 [Spark 官方文档](http://spark.apache.org/docs/2.0.2/) 。
## 命令行模式提交 Spark 任务
### 事前说明
* 在做相关操作前需要登录到 EMR 集群中的 Master 节点机器；
* 登录机器后使用命令 `su hadoop` 切换到 hadoop 用户；
* Spark 软件路径在 `/usr/local/service/spark` 下；
* 相关日志路径在 `/data/emr` 下；
* 提供了必要的测试用例，分为 jar 包和 Python 两种； 
* jar 包位于 Spark 目录的 `examples/jars/` 下，Python 文件位于 `examples/demo` 下；
* 提供测试用到的数据文件，需要提前在集群中上传。
<span id ="jump">
    
### 1. 数据准备
</span>
数据存放分为存放在 HDFS 集群和存放在 COS 两种位置。根据两种数据存在位置，下面详细介绍其数据准备方式。
* 数据存放在 HDFS，可以通过如下命令将数据文件拷贝到 HDFS 集群：
```
    /usr/local/service/hadoop/bin/hdfs dfs -mkdir /example
    /usr/local/service/hadoop/bin/hdfs dfs -mkdir /example/source
    /usr/local/service/hadoop/bin/hdfs dfs -put
    /usr/local/service/spark/examples/src/main/resources/*
    /example/source
```
* 数据存放在 COS，数据存放在 COS 有两种数据准备方式：
**方式一：**通过 COS 的控制台上传，如果数据文件已经在 COS 可以通过如下命令查看（注意替换文件路径）：
```
    /usr/local/service/hadoop/bin/hdfs dfs -ls cosn://bucketname/example/source
```
**方式二：**通过命令上传 COS（注意替换文件路径）：
```
    /usr/local/service/hadoop/bin/hdfs dfs -mkdir cosn://bucketname/example
    /usr/local/service/hadoop/bin/hdfs dfs -mkdir cosn://bucketname/example/source
    /usr/local/service/hadoop/bin/hdfs dfs -put
    /usr/local/service/spark/examples/src/main/resources/*
    cosn://bucketname/example/source
```

### 2. 任务提交模式
您可使用如下格式提交 Spark 任务：
```
    ./bin/spark-submit [options] <app jar | python file> [app options]
```
详细参数说明可以参考 [Spark 官方文档](http://spark.apache.org/docs/2.0.2/submitting-applications.html) 。
### 3. 提交 Spark 计算任务
本任务实现一个单词统计任务，统计输入文件的单词计数。
**jar 包任务读取 HDFS 文件**
在 Spark 安装目录下通过如下命令提交任务：
```
    ./bin/spark-submit
      --class tencent.emr.spark.tspark_example.WordCount
      examples/jars/tspark-example*.jar
      hdfs:///example/source/people.txt
```
**jar 包任务读取 COS 文件**
在 Spark 安装目录下通过如下命令提交任务（注意替换文件路径）：
```
    ./bin/spark-submit
      --class tencent.emr.spark.tspark_example.WordCount
      examples/jars/tspark-example*.jar
      cosn://bucketname/example/source/people.txt
```
**Python 任务读取 HDFS 文件**
在 Spark 安装目录下通过如下命令提交任务：
```
    ./bin/spark-submit examples/demo/wordcount.py hdfs:///example/source/people.txt
```
**Python 任务读取 COS 文件**
在 Spark 安装目录下通过如下命令提交任务（注意替换文件路径）：
```
    ./bin/spark-submit examples/demo/wordcount.py cosn://bucketname/example/source/people.txt
```
### 4. 查看任务日志
任务运行结果会直接打印到控制台。
```
    Justin,: 1
    Michael,: 1
    19: 1
    30: 1
    29: 1
    Andy,: 1
```
任务结束后，可以通过如下命令看到 Spark 运行日志（注意替换您的任务 ID，如 application_1489458311206_10547）：
```
    /usr/localrvice/hadoop/bin/yarn logs -applicationId application_1489458311206_10547
```
### 5. Spark SQL
本任务演示从文本文件和 json 文件中读取数据，进行一些简单的 SQL 操作。
**jar 包任务访问 HDFS 文件**
在 Spark 安装目录下通过如下命令提交任务：
```
    ./bin/spark-submit
      --class encent.emr.spark.tspark_example.SparkSQLExample
      examples/jars/tspark-example*.jar
      hdfs:///example/source/people.json
      hdfs:///example/source/people.txt
```
**jar 包任务访问 COS 文件**
在 Spark 安装目录下通过如下命令提交任务（注意替换文件路径）：
```
    ./bin/spark-submit
      --class tencent.emr.spark.tspark_example.SparkSQLExample
      examples/jars/tspark-example*.jar
      cosn://bucketname/example/source/people.json
      cosn://bucketname/example/source/people.txt
```
**Python 任务访问 HDFS 文件**
在 Spark 安装目录下通过如下命令提交任务：
```
    ./bin/spark-submit
    examples/demo/basic.py
    hdfs:///example/source/people.json
    hdfs:///example/source/people.txt
```
**Python 任务访问 COS 文件**
在 Spark 安装目录下通过如下命令提交任务（注意替换文件路径）：
```
    ./bin/spark-submit
    examples/demo/basic.py
    cosn://bucketname/example/source/people.json
    cosn://bucketname/example/source/people.txt
```
#### 查看任务日志
* 任务运行结果会直接打印到控制台（此处示例为部分数据）。
```
    ----------------------------
      age         name
    ----------------------------
      null        Michael
       30         Andy
       19         Justin
    ----------------------------
```
* 任务结束后，可以通过如下命令看到 Spark 运行日志（注意替换您的任务 ID）。
```
    /usr/localrvice/hadoop/bin/yarn logs -applicationId application_1489458311206_10548
```

#### Spark SQL 操作 Hive 表
本任务演示在文件中读取 kv 数据，然后在 Hive 中创建和操作表。
>**注意：**
>1. 该任务会移动原数据文件，如要重复测试请重新准备相应数据。
>2. COS 和 HDFS 不能混合测试，如实有必要，请先从 Hive 中删除 src 表。

**jar 包任务访问 HDFS 文件**
在 Spark 安装目录下通过如下命令提交任务：
```
    ./bin/spark-submit
      --class tencent.emr.spark.tspark_example.SparkHiveExample
      examples/jars/tspark-example*.jar
      hdfs:///example/source/kv1.txt
```
**jar 包任务访问 COS 文件**
在 Spark 安装目录下通过如下命令提交任务（注意替换文件路径）：
```
    ./bin/spark-submit
      --class tencent.emr.spark.tspark_example.SparkHiveExample
      examples/jars/tspark-example*.jar
      cosn://emrtest/example/source/kv1.txt
```
**Python 任务访问 HDFS 文件**
在 Spark 安装目录下通过如下命令提交任务：
```
    ./bin/spark-submit examples/demo/hive.py hdfs:///example/source/kv1.txt
```
**Python 任务访问 COS 文件**
在 Spark 安装目录下通过如下命令提交任务（注意替换文件路径）：
```
    ./bin/spark-submit examples/demo/hive.py cosn://bucketname/example/source/kv1.txt
```
#### 查看任务日志
* 任务运行结果会直接打印到控制台（此处示例为部分数据）。
```
    ----------------------------
      key         value
    ----------------------------
      238         val_238
       86         val_86
      311         val_311
       27         val_27
      165         val_165
      409         val_400
      255         val_255
      278         val_278
    ----------------------------
```
* 任务结束后，可以通过如下命令看到 Spark 运行日志（注意替换您的任务 ID）。
```
    /usr/localrvice/hadoop/bin/yarn logs -applicationId application_1489458311206_10549
```

### 6. Spark Streaming
本任务演示从 net 中实时读取流式数据进行单词计数。
**jar 包方式**
在 Spark 安装目录下通过如下命令提交任务，等待数据：
```
    ./bin/spark-submit
      --class tencent.emr.spark.tspark_example.NetworkWordCount
      examples/jars/tspark-example*.jar localhost 9999
```
**Python 方式**
在 Spark 安装目录下通过如下命令提交任务，等待数据：
```
    ./bin/spark-submit examples/demo/network_wordcount.py localhost 9999
```
**运行和查看输出**
新开一个窗口，依次执行以下命令：
```
    yum -y install nc
    nc -lk 9999
```
然后输入任意单词，单词以空格分割，回车结束一行输入。在原来的窗口可以看到类似如下的单词计数输出：
```
    ----------------------------
    Time:2017-03-16 20:18:15
    ----------------------------
    
    ----------------------------
    Time:2017-03-16 20:18:16
    ----------------------------
    (u'rt', 2)
    (u'', 1)
    (u'tr', 1)
    (u'trt', 1)
    ----------------------------
    Time: 2017-03-16 20:18:17
    ----------------------------
```
## 基于 HUE 的 Spark 任务操作
### 1. 数据准备
数据准备同 [通过命令行准备数据](#jump) 一致。
### 2. 登录 HUE 进行操作
通过 EMR 控制的快捷入口可以找到 HUE 的登录页面，找到如下入口， 如下图。
![](//mc.qcloudimg.com/static/img/0c216d3f9dac1c9daa8935d4b688ba50/image.png)
进入页面后单击【Create】按钮，弹出如下对话框，拖拽 SparkProgram。
![](//mc.qcloudimg.com/static/img/fccdfc197136f95c320b83f4017b9bba/image.png)
>**注意：**文件需要提前上传到 HDFS。

单击【Add】后给任务添加参数，如下图：
![](//mc.qcloudimg.com/static/img/13c1069522b048b429ea51efebe545ca/image.png)
>**注意：**
>如果文件位于 COS，可以直接填写 COS 路径如：`cosn://buckname/example/source/people.txt`

设置好参数后单击右上角的保存，然后再单击【提交】，保存完之后，箭头 2 处会有【提交】按钮。
![](//mc.qcloudimg.com/static/img/bb62338cd2cd6c45d6dc2dd693f2df9d/image.png)
此时任务进入提交，单击箭头处，可查看任务日志。
![](//mc.qcloudimg.com/static/img/6ba2d768b1abf5595e277e16fb5df0a6/image.png)

### 3. 在 HUE 中调度 Spark 任务
进入任务调度创建页面，入口如下图：
![](//mc.qcloudimg.com/static/img/d839a8367e6a8b2b70843d5cc9e0dc0f/image.png)
进入创建页面后单击【Create】按钮，进入下图：
![](//mc.qcloudimg.com/static/img/6ec89b776e767d09ac569dce384377d1/image.png)
选定好流程后，设置调度时间，如下图：
![](//mc.qcloudimg.com/static/img/6125e6b4b9cb39d78d8397c78945743b/image.png)
【hour】可以选择小时里某些分钟；
【day】可以选择某天的小时和分钟；
【week】可以选择周一到周天的小时和分钟；
【month】可以选择当前月下的天、小时、分钟；
【year】选择当前年下的月、日、小时、分钟。
选择好调度时间后单击提交即可，可以通过【Workflows】>【Dashboards】>【Coordinators】查看已经存储在调度任务。
![](//mc.qcloudimg.com/static/img/e47a806bd2b9228784b7b9c5834882b3/image.png)
下图为经存在的任务列表。
![](//mc.qcloudimg.com/static/img/d4e06a57026e5b286c504176f8c24ce8/image.png)
