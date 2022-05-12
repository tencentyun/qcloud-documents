## 案例背景
Spark 框架面向使用 Scala/Java 的 Spark 用户，用户编写 Spark 应用程序并编译打包成 jar 包后，可通过腾讯云 TI 平台 TI-ONE 提供的 Spark 框架运行自定义代码。本案例以利用 Spark 计算圆周率为例，向用户介绍：如何在 TI-ONE 上使用 Spark 框架，如何上传 jar 包，如何通过工作流页面向自定义代码传参，在自定义代码中如何读取 COS 上的文件，以及如何查看代码日志/报错信息。整个工作流运行耗时约几十秒。

## 整体流程
在腾讯云 TI 平台 TI-ONE 运行用户自定义 Spark 代码，主要包含以下步骤：
1. 本地编译源代码，完成打包。
2. 利用 Spark 框架完成圆周率计算。
3. 查看工作流运行状态和结果。

整体工作流如下：
<img src="https://main.qcloudimg.com/raw/cc3b3d871a4fd1e5eeac3da1a23f04a6.png" style="zoom:50%;" />

>!您可以按需自行配置资源参数，不同资源实例类型对应的价格不同。选择资源时，您可以参看资源参数右上角的**计费说明**。

## 详细流程

#### 一、本地准备
1. 下载代码
本案例使用的计算圆周率代码来自 Spark 官方：[利用 Spark 框架计算圆周率](https://github.com/apache/spark/blob/master/examples/src/main/scala/org/apache/spark/examples/SparkPi.scala)，您也可通过链接下载，或直接拷贝以下代码到本地进行编译。

```
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// scalastyle:off println
package org.apache.spark.examples

import scala.math.random

import org.apache.spark.sql.SparkSession

/** Computes an approximation to pi */
object SparkPi {
  def main(args: Array[String]) {
    val spark = SparkSession
      .builder
      .appName("Spark Pi")
      .getOrCreate()
    val slices = if (args.length > 0) args(0).toInt else 2
    val n = math.min(100000L * slices, Int.MaxValue).toInt // avoid overflow
    val count = spark.sparkContext.parallelize(1 until n, slices).map { i =>
      val x = random * 2 - 1
      val y = random * 2 - 1
      if (x*x + y*y <= 1) 1 else 0
    }.reduce(_ + _)
    println(s"Pi is roughly ${4.0 * count / (n - 1)}")
    spark.stop()
  }
}
// scalastyle:on println
```

2. 本地打包
由于腾讯云 TI 平台 TI-ONE 内置的 Spark 版本是2.4，所以用户在本地打包时请引入 Spark 2.4 相关的依赖。您可以选择 sbt 或者 maven 作为打包工具，并将打包后的 jar 包命名为 pi-1.0.jar 。您也可以直接下载我们打包好的 [jar 包](https://csy-classification-1256633383.cos.ap-shanghai.myqcloud.com/pi-1.0.jar) 进行以下步骤的使用体验。

#### 二、利用 Spark 框架完成圆周率计算
1. 在 [腾讯云 TI 平台 TI-ONE 控制台](https://console.cloud.tencent.com/tione/project/list) 的左侧导航栏，选择【框架】>【机器学习】>【Spark】，并拖入画布中。
2. 配置组件参数
>?Spark 框架需用户上传自己的 jar 包，PySpark 框架需用户上传 Python 文件。

 -  在右侧弹出的配置栏中，单击【作业 jar 包】：上传用户在本地编译源代码后打的 jar 包：[pi-1.0.jar](https://csy-classification-1256633383.cos.ap-shanghai.myqcloud.com/pi-1.0.jar)（您也可以直接下载我们打好的 jar 包进行体验）。
 - 主类名：org.apache.spark.examples.SparkPi （填写格式与代码名保持一致，即：包名+类名）。
![](https://main.qcloudimg.com/raw/2a9ebb2aab9571d58cd8003dcc4c6ac5.png)
 - 程序参数：100（此处填写用户自定义参数取值，在代码中可通过参数 args[0] 读取用户填写的第一个值，args[1] 读取第二个值，以此类推）。
![](https://main.qcloudimg.com/raw/365f1f51da0e38aa6b40fab790909c1e.png)
 - 配置文件：此案例中无需配置文件（该参数代表的资源文件在代码中可通过 getResourceAsStream('xxx.txt') 获取）。

3. 配置资源参数（用户可根据自身代码调整分配资源）
 - driver 节点资源类型：您可按需选择
 - executor节点资源类型：您可按需选择
 - num-executors：1
 - spark-conf：本案例中可不填（spark 的配置参数，例如 spark.shuffle.service.enabled=false，用空格或者回车分割多个 conf）
4. 运行工作流
单击右键【Spark】，选择起点运行，待运行成功（耗时约20s）。
<img src="https://main.qcloudimg.com/raw/fdb71ce371ae1bb1415e9a4010a7c3c3.png" style="zoom:67%;" />

#### 三、查看工作流运行状态和结果
1. 单击右键【Spark】，单击【Spark 控制台】可查看该工作流运行相关日志。
2. 单击【stdout】 即可在日志中查看圆周率 PI 的计算结果。
![](https://main.qcloudimg.com/raw/5247942cf3191e8ae317babf3d0e6872.png)


