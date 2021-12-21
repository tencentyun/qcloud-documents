Angel 是由腾讯自研并开源的高性能分布式机器学习和图计算平台，它提供了用于特征工程、模型构建、参数调优、模型服务和 AutoML 的全栈设施，包括传统机器学习、深度学习、图表示学习和图神经网络等算法。

凭借 Angel 强大的 PS Service 能力，Spark on Angel 扩展了 Spark 的参数更新能力，使 Spark 也具备高速训练大模型的能力而不用再顾虑 Spark Driver 的单点性能问题。Spark on Angel 组件一般用来运行用户自己实现的算法，如果需要运行 Spark on Angel 自带算法，建议您使用各个算法对应的算法组件。

## 操作步骤
1. **添加组件**
 从左侧菜单栏中，选择【框架】>【机器学习】列表下的【Spark on Angel】节点，并将其拖拽至画布中。
2. **配置参数**
 - 作业 Jar 包：通过该配置框上传您的 Spark on Angel 应用程序 Jar 包。
 - 主类名：指定您的 Spark on Angel 应用程序的入口类，即 main 函数所在的类。
 - 程序参数：您的 Spark on Angel 应用程序所需的参数，即传给 main 函数的参数。
3. **配置资源**
 - num-executors：任务启动的 spark executor 个数，可根据数据量来配置，一般训练数据量越大，需要的 worker 个数越多。
 - spark.ps.instances：Angel ps 个数，可根据模型大小来配置，一般模型越大，需要的 PS 个数越多。
 - driver 节点资源类型：请选择合适的 drive 节点机型。
 - executor 节点资源类型：请选择合适的 executor 节点机型。
 - master 节点资源类型：请选择合适的 master 节点机型。
 - ps 节点资源类型：请选择合适的 ps 节点机型。
 - spark conf 参数。
4. **运行**
单击【保存】并运行工作流。
5. **查看 Spark 控制台和日志**
在 Spark on Angel 节点上单击右键菜单，可查看任务状态。 



## 案例说明
本案例向您阐述如何在腾讯云 TI 平台 TI-ONE 使用 Spark on Angel 组件离线训练自己实现的算法模型。

### 示例代码
平台内置的 Spark on Angel 版本是 2.3.1，所以用户在本地打包时请引入 Spark on Angel 2.3.1 相关的依赖。使用  maven 作为打包工具，此时打包后的 jar 包我们命名为 spark-on-angel-examples.jar。

代码取自官方 example，[LogisticRegression on Spark on Angel](https://github.com/Angel-ML/angel/blob/branch-2.3.1/spark-on-angel/examples/src/main/scala/com/tencent/angel/spark/examples/cluster/OfflineRunner.scala)。

```scala
/*
 * Tencent is pleased to support the open source community by making Angel available.
 *
 * Copyright (C) 2017-2018 THL A29 Limited, a Tencent company. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in 
 * compliance with the License. You may obtain a copy of the License at
 *
 * https://opensource.org/licenses/Apache-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 *
 */


package com.tencent.angel.spark.examples.cluster

import com.tencent.angel.RunningMode
import com.tencent.angel.conf.AngelConf
import com.tencent.angel.ml.core.conf.{MLConf, SharedConf}
import com.tencent.angel.spark.context.PSContext
import com.tencent.angel.spark.ml.core.{ArgsUtil, GraphModel, OfflineLearner}
import org.apache.spark.{SparkConf, SparkContext}

object OfflineRunner {

  def main(args: Array[String]): Unit = {
    val params = ArgsUtil.parse(args)

    // Train data path
    val input = params.getOrElse("input", "")

    // Can be used in train/predict mode, it means model output path in train mode and model load path in predict mode
    val output = params.getOrElse("modelPath", "")
    val actionType = params.getOrElse("actionType", "train")
    val network = params.getOrElse("network", "LogisticRegression")

    // Model load path in train mode, just use in train mode
    val modelPath = params.getOrElse("model", "")

    // Predict result save path, just use in predict mode
    val predictPath = params.getOrElse("predictPath", "")

    // set running mode, use angel_ps mode for spark
    SharedConf.get().set(AngelConf.ANGEL_RUNNING_MODE, RunningMode.ANGEL_PS.toString)

    // build SharedConf with params
    SharedConf.addMap(params)

    val dim = SharedConf.indexRange.toInt

    println(s"dim=$dim")

    // load data
    val conf = new SparkConf()

    // we set the load model path for angel-ps to load the meta information of model
    actionType match {
      case MLConf.ANGEL_ML_TRAIN => {
        if(modelPath.length > 0)
          conf.set(AngelConf.ANGEL_LOAD_MODEL_PATH, modelPath)
      }
      case MLConf.ANGEL_ML_PREDICT => {
        if(output.length > 0)
          conf.set(AngelConf.ANGEL_LOAD_MODEL_PATH, output)
      }
    }

    val sc   = new SparkContext(conf)

    // start PS
    PSContext.getOrCreate(sc)

    val className = "com.tencent.angel.spark.ml.classification." + network
    val model = GraphModel(className)
    val learner = new OfflineLearner

    actionType match {
      case MLConf.ANGEL_ML_TRAIN => learner.train(input, output, modelPath, dim, model)
      case MLConf.ANGEL_ML_PREDICT => learner.predict(input, predictPath, output, dim, model)
    }
  }
}
```


### 平台配置
#### 1. 添加组件

从左侧菜单栏中，选择【框架】>【机器学习】列表下的 Spark on Angel 节点，并将其拖拽至画布中。

#### 2. 配置参数

 - 作业 Jar 包：通过该配置框上传本地编译后的 spark-on-angel-examples.jar。
 - 主类名：指定您的 Spark on Angel 应用程序的入口类，即 main 函数所在的类。
 - 程序参数：您的 Spark on Angel 应用程序所需的参数，即传给 main 函数的参数。

#### 3. 配置资源
您可按需选择资源参数。

#### 4. 运行
单击【保存】并运行工作流。

### 查看 Spark 控制台
在 Spark on Angel 节点上单击右键菜单【Spark 控制台】，可查看任务状态。

### 运行结果
运行成功后，在用户指定的模型保存目录下会有模型文件生成。
![](https://main.qcloudimg.com/raw/0c8fa269de5a0cf3cf31aec4d7456019.png)

