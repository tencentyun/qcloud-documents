Analytics Zoo 作为一个数据分析 + AI 平台，能够帮助用户利用 Spark 的各种流水线、内置模型、特征操作等，构建基于大数据的深度学习端到端应用。 某种意义上它是 Spark 和 BigDL 的扩充，可以将 Spark、TensorFlow、Keras 和 BigDL 无缝合并到一个集成管道中，方便地扩展到企业已有的大型 Apache Hadoop/Spark 集群，进行分布式训练或推理。


## 操作步骤
1. **添加组件**
从左侧菜单栏中，选择【框架】>【机器学习】列表下的 Analytics Zoo 节点，并将其拖拽至画布中。
2. **配置参数**
 - 脚本及依赖包文件上传 ：
   将执行脚本上传至执行脚本框。如果需要依赖文件，则压缩为 zip 文件后通过依赖包文件框上传。
 - 算法参数：
   指定运行执行脚本的参数。
 - Python 版本：指定 Python 版本，Analytics Zoo 目前支持 Python3.5。
 - 版本号：目前支持Analytics Zoo。
3. **配置资源**
在【资源参数】列表框配置任务的资源参数。
 - num-executors：指定分配的计算节点数目。
 - driver-memory：指定主节点内存大小，上限为14GB。
 - executor-cores：指定每个子节点分配的 CPU Core 数，推荐2 - 3。
 - executor-memory：指定每个子节点分配的内存大小，上限为55GB，推荐单个 core 分配2 - 3GB。
 - spark-conf：指定 Spark 常用参数配置，如压缩、序列化、网络等。例如 spark.cores.max = 1000。
4. **运行**
单击【保存】并运行工作流。
5. **查看 Spark 控制台和日志**
在该节点上单击右键菜单，单击【Spark 控制台】，可查看任务状态和详细日志。

## 案例说明
Analytics Zoo 为用户提供基于 LSTM 的算法，用于时间序列数据的异常检测。它将影响当前时间的一系列值（例如最近50个小时的数据）作为模型的输入来训练模型，然后使用训练好的模型预测下一个数据点。当实际值与模型预测值相距较大时，定义为异常。我们将通过一个异常检测的案例向您介绍 Analytics Zoo 的使用方法。

#### 数据准备
我们使用 [Numenta Anomaly Benchmark](https://raw.githubusercontent.com/numenta/NAB/master/data/realKnownCause/nyc_taxi.csv) 的一个数据集（NYC taxi passengers）作为案例的数据集。该数据集包含10320条样本，每条样本表示特定时间纽约市的出租车乘客总数。数据格式如下所示：

```
timestamp,value
2014-07-01 00:00:00,10844
2014-07-01 00:30:00,8127
2014-07-01 01:00:00,6210
2014-07-01 01:30:00,4656
2014-07-01 02:00:00,3820
2014-07-01 02:30:00,2873
2014-07-01 03:00:00,2369
2014-07-01 03:30:00,2064
2014-07-01 04:00:00,2221
```

在您运行案例之前，您需要先下载数据，解压压缩包，并将数据文件 nyc_taxi.csv 上传到 COS 上去。


### 执行脚本准备

#### 参数定义
在脚本的开头，定义算法所需的参数。这里包括数据路径、batch_size、epoch 次数、展开长度四个参数。

```python
parser.add_option("--input_dir", dest="input_dir")
parser.add_option("-b", "--batch_size", dest="batch_size", default="1024")
parser.add_option("--nb_epoch", dest="nb_epoch", default="20")
parser.add_option("--unroll_len", dest="unroll_len", default="24")
```

### 数据预处理
为了准备 AnomalyDetrctor 模型的输入，使用 unroll 方法对时间序列数据进行展开。

```python
## 加载数据
def load_and_scale(input_path):
    df = pd.read_csv(input_path)
    df['datetime'] = pd.to_datetime(df['timestamp'])
    df['hours'] = df['datetime'].dt.hour
    df['awake'] = (((df['hours'] >= 6) & (df['hours'] <= 23)) | (df['hours'] == 0)).astype(int)
    print(df.head(10))
    sqlContext = SQLContext(sc)
    dfspark = sqlContext.createDataFrame(df[["value", "hours", "awake"]])
    feature_size = len(["value", "hours", "awake"])
    return AnomalyDetector.standardScale(dfspark), feature_size

df_scaled, feature_size = load_and_scale(options.input_dir)
data_rdd = df_scaled.rdd.map(lambda row: [x for x in row])
unrolled = AnomalyDetector.unroll(data_rdd, int(options.unroll_len), predict_step=1)
[train, test] = AnomalyDetector.train_test_split(unrolled, 1000)
```

#### 模型训练
您能够使用下面的 Python API 创建一个 AnomalyDetrctor 模型，使用 mse 作为 loss，rmsprop 作为优化器进行训练。
```python
from zoo.models.anomalydetection import AnomalyDetector
model = AnomalyDetector(feature_shape=(10, 3), hidden_layers=[8, 32, 15], dropouts=[0.2, 0.2, 0.2])
model.compile(loss='mse', optimizer='rmsprop', metrics=['mae'])
model.fit(train, batch_size=int(options.batch_size), nb_epoch=int(options.nb_epoch))
```

#### 异常检测
模型训练完成之后，您可以使用训练好的模型进行预测，检测数据点是否是异常。
```python
y_predict = model.predict(test, batch_per_thread=int(options.batch_size))\
        .map(lambda x: float(x[0]))
y_truth = test.map(lambda x: float(x.label.to_ndarray()[0]))
anomalies = AnomalyDetector.detect_anomalies(y_predict, y_truth, 50)
```

#### 传递算法参数
通过算法参数传递参数给执行脚本进行执行。
```shell
--input_dir ${ai_dataset_lib}/analytics/nyc_taxi.csv
--batch_size 1000
--nb_epoch 2
--unroll_len 24
```

同时，“Python 版本”选择 Python3.5， “版本号”选择 analytics_zoo。

#### 运行工作流
单击【保存】并运行工作流。

