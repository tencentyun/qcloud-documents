Spark组件是面向使用Python的Spark用户，用户通过Python编写Spark应用程序，通过PySpark组件完成部署，也支持pyspark的sql功能，本文有部分使用方法介绍（更多用法请参考社区指引:Spark SQL, DataFrames and Datasets Guide）。

和标准的Spark相比，pySpark支持上传Python脚本和实时修改，更加的灵活，而且支持SQL功能，所以我们推荐用来数据预处理。

运行版本说明

PySpark 组件中使用的 Python 版本和支持的第三方模块版本信息如下：

    Python version is [2.7.5]
    scipy version is [0.12.1]
    numpy version is [1.7.1]

若有需求使用其他第三方的 lib，可使用 pip 在代码内安装，示例如下：

    import pip
    pip.main(['install', "package_name"])



使用阶段

1. 添加组件

从左边栏中，组件>机器学习 列表下拖拽出 PySpark 节点至画布中。
![](https://main.qcloudimg.com/raw/a03a4058eb8eb15883248cfc0a9bb5bd.png)




2.参数配置

- 脚本及依赖包文件上传：
  将任务脚本上传至 程序脚本 框。如果需要依赖文件，则压缩为 zip 文件后通过 依赖包文件 框上传。
![](https://main.qcloudimg.com/raw/f502e40c73117cfddef50af122cec760.png)


- 算法参数：
  指定你的PySpark应用程序所需的参数，即传给PySpark脚本的参数，可选项
- 配置资源：
  指定你的PySpark应用程序用到的配置文件，可选项
![](https://main.qcloudimg.com/raw/8a66c5933c95aabe787630f268cb669b.png)


3. 资源配置

  在 资源参数 列表配置任务的资源参数。

- num-executors：指定分配的Executor个数
- driver-memory：指定Driver需要的内存大小，单位为GB
- executor-cores：指定每个Executor上需要的cpu core数
- executor-memory：指定每个Executor上需要的内存大小，单位为GB
- spark-conf：指定Spark的属性参数，换行分割，例如 spark.default.parallelism=200
 ![](https://main.qcloudimg.com/raw/ee08ffcc7bc7c94e3db4bdc75ccf4790.png) 

4. 运行

单击【保存】并运行工作流。



5. 查看 PySpark 控制台和日志

在 PySpark 节点上单击右键菜单可查看任务状态和详细日志。

![](https://main.qcloudimg.com/raw/3ec62ffb32a86b4bc57545098b219537.png)
![](https://main.qcloudimg.com/raw/4c2f9e2163fa984a6328fc8719f80c9c.png)
 



PySpark使用建议

使用PySpark的目的是更好地借助其分布式计算的优势，来解决单机完成不了的计算。如果你在PySpark中仍然是调用常规的Python库做单机计算，那就失去了使用PySpark的意义了。下面举例说明如何编写PySpark分布式计算代码。

使用Spark的DataFrame，而不要使用Pandas的DataFrame

PySpark本身就具有类似pandas.DataFrame的DataFrame，所以直接使用PySpark的DataFrame即可，基于PySpark的DataFrame的操作都是分布式执行的，而pandas.DataFrame是单机执行的，例如：

    ...
    df = spark.read.json("examples/src/main/resources/people.json")
    df.show()
    # +----+-------+
    # | age|   name|
    # +----+-------+
    # |null|Michael|
    # |  30|   Andy|
    # |  19| Justin|
    # +----+-------+
    
    pandas_df = df.toPandas()
    age = pandas_df['age']
    ...

上述代码中12行将PySpark的DataFrame转换成pandas.DataFrame，然后获取'age'列，注意df.toPandas()操作会将分布在各节点的数据全部收集到driver上，再转成单机的pandas.DataFrame数据结构，如果数据量很小还可以接受，但是数据量较大时，就不可取了，其实PySpark的DataFrame本身支持很多操作，直接基于它实现后续的业务逻辑即可，例如上述代码可以改成：

    age = df.select('age')

在Task里使用python库，而不是在driver上使用python库

下面有段代码，将数据全部collect到driver端，然后使用sklearn进行预处理。

    from sklearn import preprocessing
    data = np.array(rdd.collect(), dtype=np.float)
    normalized = preprocessing.normalize(data)

上述代码其实就退化为单机程序了，如果数据量较大的话，collect操作会把driver的内存填满，甚至OOM，通常基于RDD或DataFrame的API可以满足大多数需求，例如标准化操作：

    from pyspark.ml.feature import Normalizer
    
    df = spark.read.format("libsvm").load(path)
    
    # Normalize each Vector using $L^1$ norm.
    normalizer = Normalizer(inputCol="features", outputCol="normFeatures", p=1.0)
    l1NormData = normalizer.transform(dataFrame)

就算RDD或DataFrame没有满足你要求的API，你可以自行写一个处理函数，针对每条记录进行处理：

    # record -> other record
    def process_fn(record):
      # your process logic
      # for example
      # import numpy as np
      # x = np.array(record, type=np.int32)
      # ...
    
    # record -> True or Flase
    def judge_fn(record):
      # return True or Flase
    
    processed = rdd.map(process_fn).map(lambda x: x[1:3])
    filtered = processed.filter(judge_fn)

process_fn或judge_fn会分发到每个节点上分布式执行，你可以在process_fn或judge_fn中使用任何python库(如numpy, scikit-learn等)

更多关于Spark的使用可以参考如下文档：

- rdd
- dataframe
- python api

