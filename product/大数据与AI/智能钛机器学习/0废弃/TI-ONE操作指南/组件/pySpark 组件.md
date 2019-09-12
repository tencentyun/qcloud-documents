Spark组件是面向使用Python的Spark用户，用户通过Python编写Spark应用程序，通过PySpark组件完成部署，也支持pyspark的sql功能，本文有部分使用方法介绍（更多用法请参考社区指引:[Spark SQL, DataFrames and Datasets Guide](http://spark.apache.org/docs/latest/sql-programming-guide.html)）。

和标准的Spark相比，pySpark支持上传Python脚本和实时修改，更加的灵活，而且支持SQL功能，所以我们推荐用来数据预处理。

### 1. **从左侧组件列表里拖拽出一个PySpark节点**


![](https://main.qcloudimg.com/raw/b3347ed7c805332139b03fd5f8edfb90.png)



### 2. **单击任务节点，会从右侧弹出配置框**

![](https://main.qcloudimg.com/raw/bb1a61a1165ed1edb03015e86eac9161.png)

> * 执行脚本：通过该配置框上传你的PySpark脚本，必填项
> * 依赖包文件：指定你的PySpark应用程序依赖的包，可以是.py .zip .egg文件，可选项
> * 算法参数：指定你的PySpark应用程序所需的参数，即传给PySpark脚本的参数，可选项
> * 配置资源：指定你的PySpark应用程序用到的配置文件，可选项

其他配置操作与Spark组件类似。


##  PySpark使用建议

使用PySpark的目的是更好地借助其分布式计算的优势，来解决单机完成不了的计算。如果你在PySpark中仍然是调用常规的Python库做单机计算，那就失去了使用PySpark的意义了。下面举例说明如何编写PySpark分布式计算代码。

### 使用Spark的DataFrame，而不要使用Pandas的DataFrame

PySpark本身就具有类似`pandas.DataFrame`的`DataFrame`，所以直接使用PySpark的`DataFrame`即可，基于PySpark的`DataFrame`的操作都是分布式执行的，而`pandas.DataFrame`是单机执行的，例如：

```python
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
```

上述代码中12行将PySpark的`DataFrame`转换成`pandas.DataFrame`，然后获取'age'列，注意`df.toPandas()`操作会将分布在各节点的数据全部收集到driver上，再转成单机的`pandas.DataFrame`数据结构，如果数据量很小还可以接受，但是数据量较大时，就不可取了，其实PySpark的`DataFrame`本身支持很多操作，直接基于它实现后续的业务逻辑即可，例如上述代码可以改成：

```python
age = df.select('age')
```

### 在Task里使用python库，而不是在driver上使用python库

下面有段代码，将数据全部`collect`到driver端，然后使用sklearn进行预处理。

```
from sklearn import preprocessing
data = np.array(rdd.collect(), dtype=np.float)
normalized = preprocessing.normalize(data)
```

上述代码其实就退化为单机程序了，如果数据量较大的话，`collect`操作会把driver的内存填满，甚至OOM，通常基于`RDD`或`DataFrame`的API可以满足大多数需求，例如标准化操作：

```python
from pyspark.ml.feature import Normalizer

df = spark.read.format("libsvm").load(path)

# Normalize each Vector using $L^1$ norm.
normalizer = Normalizer(inputCol="features", outputCol="normFeatures", p=1.0)
l1NormData = normalizer.transform(dataFrame)
```

就算`RDD`或`DataFrame`没有满足你要求的API，你可以自行写一个处理函数，针对每条记录进行处理：

```python
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
```

`process_fn`或`judge_fn`会分发到每个节点上分布式执行，你可以在`process_fn`或`judge_fn`中使用任何python库(如numpy, scikit-learn等)

更多关于Spark的使用可以参考如下文档：
 * [rdd](http://spark.apache.org/docs/2.1.1/programming-guide.html)
 * [dataframe](http://spark.apache.org/docs/2.1.1/sql-programming-guide.html)
 * [python api](http://spark.apache.org/docs/2.1.1/api/python/index.html)
